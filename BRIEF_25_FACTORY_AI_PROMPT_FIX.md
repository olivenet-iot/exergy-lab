# BRIEF_25: Factory AI Prompt Taşması — Pinch Verisi Optimizasyonu

> **Tarih:** 2026-02-05
> **Öncelik:** Kritik (Bug Fix)
> **Tahmini Süre:** 1-2 saat
> **Etkilenen Dosyalar:** api/services/claude_code_service.py

---

## 1. Problem

Fabrika AI yorumlama prompt'u 100,864 karakter — limit 50,000. Truncation yapılıyor ama yetmiyor, Claude JSON response üretemiyor.

Log:
```
Factory prompt exceeds 50000 chars (100864), truncating knowledge section
Could not extract JSON from Claude factory response
```

### Kök Neden

BRIEF_24 ile eklenen `_format_pinch_for_prompt()` fonksiyonu pinch verilerini prompt'a ekliyor. Ancak PinchResult içindeki ham veriler çok büyük:

- `composite_curves`: Onlarca (T, H) nokta çifti → JSON olarak binlerce karakter
- `grand_composite_curve`: Benzer boyut
- `problem_table`: Her sıcaklık aralığı için satır (N aralık × 7 alan)
- `streams`: Her akış için ~10 alan × akış sayısı
- `hen_matches`: Her eşleştirme detayı

Bu verilerin tamamı AI yorumlama prompt'una gereksiz. Claude'un yorumlama için ihtiyaç duyduğu sadece **özet metrikler**.

---

## 2. Çözüm

### 2.1 `_format_pinch_for_prompt()` Fonksiyonunu Optimize Et

Pinch verisini prompt'a eklerken sadece özet metrikleri gönder, görselleştirme verilerini (composite curves, GCC, problem table) **gönderme**.

**Öncesi (tahmini):**
```python
def _format_pinch_for_prompt(pinch_data: dict) -> str:
    # Muhtemelen pinch_data'nın tamamını veya büyük bölümünü string'e çeviriyor
    ...
```

**Sonrası:**
```python
def _format_pinch_for_prompt(pinch_data: dict) -> str:
    """Pinch analizi özetini AI prompt'u için formatla. Maksimum ~500 karakter."""
    if not pinch_data or not pinch_data.get("is_valid"):
        return ""
    
    lines = [
        "\n## Pinch Analizi Sonuçları",
        f"- Pinch sıcaklığı: {pinch_data.get('pinch_temperature_C', 'N/A')}°C (ΔT_min: {pinch_data.get('delta_T_min_C', 10)}°C)",
        f"- Minimum dış ısıtma (QH_min): {pinch_data.get('QH_min_kW', 'N/A')} kW",
        f"- Minimum dış soğutma (QC_min): {pinch_data.get('QC_min_kW', 'N/A')} kW",
        f"- Maksimum ısı geri kazanım: {pinch_data.get('max_heat_recovery_kW', 'N/A')} kW",
    ]
    
    # Mevcut durum karşılaştırması (varsa)
    if pinch_data.get("QH_current_kW"):
        lines.append(f"- Mevcut dış ısıtma: {pinch_data['QH_current_kW']} kW → Fazla: {pinch_data.get('QH_excess_kW', 0)} kW")
    if pinch_data.get("QC_current_kW"):
        lines.append(f"- Mevcut dış soğutma: {pinch_data['QC_current_kW']} kW → Fazla: {pinch_data.get('QC_excess_kW', 0)} kW")
    
    # Tasarruf
    if pinch_data.get("savings_potential_pct"):
        lines.append(f"- Tasarruf potansiyeli: %{pinch_data['savings_potential_pct']} ({pinch_data.get('annual_savings_EUR', 0)} EUR/yıl)")
    
    # Akış özeti (detay değil, sadece sayılar)
    lines.append(f"- Akış sayısı: {pinch_data.get('num_hot_streams', 0)} sıcak, {pinch_data.get('num_cold_streams', 0)} soğuk")
    
    # HEN eşleştirme özeti (tam detay değil, sadece özet)
    hen_matches = pinch_data.get("hen_matches", [])
    if hen_matches:
        lines.append(f"- HEN önerileri: {len(hen_matches)} eşleştirme")
        # Sadece ilk 3 eşleştirmenin kısa özeti
        for i, match in enumerate(hen_matches[:3]):
            q = match.get("Q_exchange_kW", 0)
            desc = match.get("description", "")
            # Açıklamayı kısalt
            if len(desc) > 80:
                desc = desc[:77] + "..."
            lines.append(f"  {i+1}. {desc} ({q} kW)")
    
    # Uyarılar (varsa, kısa)
    warnings = pinch_data.get("warnings", [])
    if warnings:
        lines.append(f"- Uyarılar: {'; '.join(w[:60] for w in warnings[:2])}")
    
    return "\n".join(lines)
```

### 2.2 Fabrika Prompt Genel Boyut Kontrolü

`_format_pinch_for_prompt` dışında, genel prompt boyutunu da kontrol et. `interpret_factory_analysis()` fonksiyonunda:

1. Pinch verisinden **büyük alanları çıkar** (frontend'e gönderilir zaten, AI'a gerek yok):
   - `composite_curves` — çıkar
   - `grand_composite_curve` — çıkar
   - `problem_table` — çıkar
   - `streams` (tam liste) — çıkar, sadece sayı gönder

2. Ekipman analiz sonuçlarından da **gereksiz büyük alanları çıkar**:
   - Her ekipmanın `sankey_data` alanı prompt'a dahil edilmemeli
   - Her ekipmanın `radar_data` alanı prompt'a dahil edilmemeli
   - Sadece temel metrikler: exergy_efficiency_pct, exergy_destroyed_kW, annual_loss_EUR, exergoeconomic alanları

```python
def _summarize_equipment_for_prompt(result: dict) -> dict:
    """Ekipman sonucunu AI prompt için özetle. Görselleştirme verilerini çıkar."""
    # Prompt'a dahil edilecek alanlar (whitelist)
    PROMPT_KEYS = [
        "equipment_type", "subtype", "name",
        "exergy_in_kW", "exergy_out_kW", "exergy_destroyed_kW",
        "exergy_efficiency_pct", "thermal_efficiency_pct",
        "annual_loss_kWh", "annual_loss_EUR",
        "recoverable_heat_kW",
        "exergy_destroyed_avoidable_kW", "exergy_destroyed_unavoidable_kW",
        "avoidable_ratio_pct",
        "exergoeconomic_f_factor", "exergoeconomic_r_factor",
        "exergoeconomic_Z_dot_eur_h", "exergoeconomic_C_dot_destruction_eur_h",
        "exergoeconomic_c_product_eur_kWh", "exergoeconomic_total_cost_rate_eur_h",
        "grade",  # Benchmark notu
    ]
    return {k: v for k, v in result.items() if k in PROMPT_KEYS and v is not None}
```

### 2.3 Factory Prompt Boyut Hedefi

Mevcut yapı:
```
[system prompt] + [knowledge] + [analiz verileri] + [görev talimatı]
```

Hedef bütçe:
| Bölüm | Maks Karakter |
|-------|---------------|
| System prompt | ~2,000 |
| Knowledge (kırpılmış) | ~15,000 |
| Ekipman sonuçları (özetlenmiş) | ~10,000 |
| Fabrika agregat metrikleri | ~2,000 |
| Pinch özeti | ~500 |
| Görev talimatı | ~3,000 |
| **TOPLAM** | **~32,500** |

Bu, 50K limitin altında kalır ve Claude'a yeterli context verir.

---

## 3. Uygulama Adımları

1. `api/services/claude_code_service.py` aç
2. `_format_pinch_for_prompt()` fonksiyonunu bul ve yukarıdaki optimize versiyonla değiştir
3. `interpret_factory_analysis()` fonksiyonunda:
   a. Ekipman sonuçlarını prompt'a eklerken `_summarize_equipment_for_prompt()` kullan
   b. Pinch verisinden composite_curves, grand_composite_curve, problem_table, streams alanlarını çıkar
   c. sankey_data ve radar_data alanlarını prompt'a dahil etme
4. Prompt boyutunu hesapla ve logla: `logger.info(f"Factory prompt size: {len(prompt)} chars")`
5. Truncation limitini kontrol et — 50K yeterli olmalı ama gerekirse ayarla

---

## 4. Doğrulama

1. Fabrika projesi oluştur (en az 3-4 ekipman)
2. Analiz çalıştır
3. AI yorumlama çalıştır
4. Logda:
   - `Factory prompt size: XXXXX chars` → 50,000'in altında olmalı
   - `Could not extract JSON` hatası **OLMAMALI**
   - AI yanıtı gelecek ve frontend'de görünecek
5. `pytest tests/ -v` — regresyon kontrolü

---

## 5. Claude Code Prompt

```
PROJECT_ANALYSIS.md ve BRIEF_25_FACTORY_AI_PROMPT_FIX.md dosyalarını oku.

Bug Fix: Fabrika AI yorumlama prompt'u 100K+ karaktere ulaşıyor ve Claude JSON response üretemiyor.

1. api/services/claude_code_service.py dosyasını aç.
2. _format_pinch_for_prompt() fonksiyonunu bul. Eğer pinch verilerinin tamamını (composite_curves, grand_composite_curve, problem_table, streams) prompt'a ekliyorsa, bunları çıkar. Sadece Brief'teki özet metrikleri ekle (pinch T, QH_min, QC_min, savings, HEN sayısı + ilk 3 eşleştirme özeti). Fonksiyon çıktısı maksimum ~500 karakter olmalı.
3. interpret_factory_analysis() fonksiyonunu bul. Ekipman analiz sonuçlarını prompt'a ekleyen kısmı bul. Her ekipmandan sadece temel metrikleri dahil et — sankey_data, radar_data, composite_curves gibi görselleştirme verilerini prompt'tan çıkar. Brief 2.2'deki _summarize_equipment_for_prompt() whitelist yaklaşımını kullan.
4. Fabrika agregatlarından da gereksiz büyük alanları çıkar (sankey_data gibi).
5. Prompt'un toplam boyutunu logla: logger.info(f"Factory prompt: {len(prompt)} chars")
6. Mevcut truncation mekanizmasının doğru çalıştığını kontrol et.
7. pytest tests/ -v çalıştır — hiçbir test kırılmamalı.

Hedef: Prompt boyutu 35,000 karakter altına inmeli. Claude JSON response doğru üretebilmeli.
```

---

*BRIEF_25 — Factory AI Prompt Taşması Fix*
*Tarih: 2026-02-05*
