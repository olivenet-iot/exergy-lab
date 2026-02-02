---
skill_id: integration_expert
version: 1.0
type: factory
triggers:
  - factory_analysis
  - cross_equipment_opportunities
dependencies:
  - factory/factory_analyst.md
knowledge_files:
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/heat_integration.md
  - knowledge/factory/waste_heat_recovery.md
  - knowledge/factory/pinch_analysis.md
  - knowledge/factory/pinch/INDEX.md
  - knowledge/factory/pinch/fundamentals.md
  - knowledge/factory/pinch/hen_design.md
  - knowledge/factory/pinch/hen_retrofit.md
  - knowledge/factory/pinch/utility_systems.md
  - knowledge/factory/pinch/stream_data.md
---

# Entegrasyon Uzmanı

## Uzmanlık Alanı

Ekipmanlar arası enerji/exergy entegrasyonu:
- Atık ısı geri kazanımı
- Isı değiştirici ağı tasarımı
- Pinch analizi temelleri
- Kojenerasyon fırsatları

## Entegrasyon Matrisi

| Kaynak | Sıcaklık | Potansiyel Kullanım |
|--------|----------|---------------------|
| Kompresör atık ısısı | 70-90°C | Besleme suyu, bina ısıtma |
| Kazan baca gazı | 150-250°C | Ekonomizer, hava ön ısıtma |
| Kazan blowdown | 100-180°C | Flash tank, ön ısıtma |
| Chiller kondenser | 35-45°C | Düşük sıcaklık ısıtma |
| Fırın egzozu | 200-400°C | Buhar üretimi, ORC |

## Eşleştirme Kuralları

```
Isı transferi için:
ΔT_min = 10-20°C (minimum sıcaklık farkı)

Sıcaklık eşleştirmesi:
- Kaynak sıcaklığı > Hedef sıcaklığı + ΔT_min

Örnek:
Kompresör: 85°C
Besleme suyu: 20°C → 60°C
ΔT = 85 - 60 = 25°C > 10°C ✓ Uygun
```

## Yatırım Tahminleri

| Teknoloji | Maliyet | Birim |
|-----------|---------|-------|
| Plakali eşanjör | €100-200 | /kW |
| Ekonomizer | €150-300 | /kW |
| Heat recovery unit | €200-400 | /kW |
| Absorption chiller | €300-500 | /kW soğutma |
| ORC sistemi | €2000-4000 | /kW elektrik |

## Pinch Tabanlı Eşleştirme Kuralları

### Golden Rule Kontrolü (Altın Kural)

```
Pinch üstü eşleştirme:
- CP_hot ≤ CP_cold (sıcak akış CP'si soğuk akıştan küçük veya eşit olmalı)
- Aksi halde akış bölme (stream splitting) gerekli
- Sıcak akış sayısı ≤ soğuk akış sayısı

Pinch altı eşleştirme:
- CP_cold ≤ CP_hot (soğuk akış CP'si sıcak akıştan küçük veya eşit olmalı)
- Aksi halde akış bölme gerekli
- Soğuk akış sayısı ≤ sıcak akış sayısı
```

### Cross-Pinch Transfer Tespiti ve Uyarı

```
Cross-pinch transfer kontrolü:
1. Mevcut eşanjörler pinch sıcaklığının her iki tarafında mı çalışıyor?
2. Cross-pinch transfer miktarı = QH,mevcut - QH,min
3. Cross-pinch > %10 ise → "Pinch ihlali tespit edildi" uyarısı ver

Uyarı mesajı:
"Bu eşanjör pinch noktası üzerinden ısı transfer ediyor.
 Cross-pinch transfer: X kW → Toplam utility artışı: 2×X kW
 Referans: pinch/hen_retrofit.md"
```

### HEN Retrofit Değerlendirmesi

```
Retrofit önceliklendirme:
1. En büyük cross-pinch transferi olan eşanjörü belirle
2. Mevcut eşanjör alanının yeterliliğini değerlendir
3. Yeni eşanjör ekleme vs. mevcut yeniden borulama (repiping) karşılaştır
4. Network pinch analizi ile kısıtlayıcı eşanjörü bul

Referans: knowledge/factory/pinch/hen_retrofit.md
```

### Kurutma Fırını Entegrasyon Kalıpları (Dryer Integration)

| Kaynak | Hedef | Entegrasyon | Tasarruf Potansiyeli |
|--------|-------|-------------|---------------------|
| Kurutma fırını egzozu | Isı geri kazanım eşanjörü | Egzoz havası → taze hava ön ısıtma | %15-30 enerji tasarrufu |
| Kurutma fırını egzozu | Absorpsiyonlu chiller | Egzoz ısısı → soğutma üretimi | Serbest soğutma kapasitesi |
| Kazan buharı | Kurutma fırını | Buhar → kurutma ısısı | Doğrudan ısı kaynağı |
| Kompresör atık ısısı | Kurutma fırını ön ısıtma | Atık ısı → hava ön ısıtma | %5-15 enerji tasarrufu |
| Kurutma fırını | Mekanik ön su alma | Termal öncesi mekanik kurutma | %30-50 enerji azalma |

### Buhar Türbini / CHP Entegrasyon Kalıpları (Steam Turbine Integration)

| Kaynak | Hedef | Entegrasyon | Tasarruf Potansiyeli |
|--------|-------|-------------|---------------------|
| Kazan yüksek basınçlı buhar | Karşı basınçlı türbin | HP buhar → elektrik + LP buhar | Elektrik üretimi + proses buharı |
| Türbin çıkış buharı | Proses ısıtma / kurutma | LP/MP buhar → proses ihtiyacı | CHP verimi %75-85 |
| Baca gazı atık ısısı | ORC türbin | Düşük sıcaklık → elektrik | %5-12 ek elektrik |
| PRV (basınç düşürme vanası) | Mikro türbin ikamesi | Basınç enerjisi → elektrik | %100 enerji geri kazanım |
| Türbin kondensat | Kazan besleme suyu | Sıcak kondensat geri dönüş | %5-10 yakıt tasarrufu |
| Gaz türbini egzozu | HRSG → buhar türbini | Kombine çevrim | Verim %50 → %55-60 |

## Dikkat Edilecekler

1. **Mesafe:** Kaynak-hedef arası mesafe maliyeti artırır
2. **Senkronizasyon:** Kaynak ve hedef aynı anda mı çalışıyor?
3. **Güvenilirlik:** Entegrasyon sistem güvenilirliğini etkiler mi?
4. **Bakım:** Ek bakım ihtiyacı
5. **Legionella riski:** 25-45°C su stagnasyonu önlenmeli
