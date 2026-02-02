---
skill_id: exergy_fundamentals
version: 1.0
type: core
---

# Exergy Temelleri

## Temel Kavramlar

### Exergy Nedir?
Exergy, bir sistemin çevresiyle dengeye gelene kadar yapabileceği maksimum iştir. Enerji korunur ama exergy yok olur (2. Yasa).

### Exergy vs Enerji
- **Enerji verimi:** Çıkış/Giriş enerji oranı
- **Exergy verimi:** Çıkış/Giriş exergy oranı (termodinamik kalite)

### Neden Exergy?
Kazan %88 enerji verimi gösterebilir ama %35 exergy verimi. Exergy gerçek iyileştirme potansiyelini gösterir.

## Exergy Hesaplama Temelleri

### Fiziksel Exergy
```
ex_physical = (h - h₀) - T₀(s - s₀)
```
- h: Entalpi
- s: Entropi
- ₀: Referans çevre koşulları (T₀=25°C, P₀=1 atm)

### Kimyasal Exergy
Yakıtlar için:
```
Ex_fuel = m_fuel × LHV × φ
```
- φ: Kimyasal exergy faktörü (~1.04-1.08 hidrokarbonlar için)

### Exergy Yıkımı (İrreversibl)
```
I = Ex_in - Ex_out - Ex_useful
```

## Benchmark Değerlendirme Kuralları

| Exergy Verimi | Değerlendirme |
|---------------|---------------|
| > 50% | Mükemmel |
| 40-50% | İyi |
| 30-40% | Ortalama |
| 20-30% | Düşük |
| < 20% | Kritik |

Bu değerler ekipman tipine göre ayarlanmalı (bkz. equipment skills).

## EGM (Entropy Generation Minimization) Perspektifi

### Gouy-Stodola Bağlantısı
Entropi üretimi ile exergy yıkımı doğrudan ilişkilidir:
```
I = T₀ × S_gen
```
- I: Exergy yıkımı (irreversibility) [kW]
- T₀: Referans çevre sıcaklığı [K] (genellikle 298 K)
- S_gen: Entropi üretim hızı [kW/K]

**Fiziksel anlam:** Her kW/K entropi üretimi, T₀ kW exergy yıkımına eşdeğerdir.

### Bejan Sayısı (Bejan Number)
İrreversibllik kaynaklarını ayırt etmek için:
```
Be = S_gen_ΔT / (S_gen_ΔT + S_gen_ΔP)
```
- S_gen_ΔT: Isı transferi kaynaklı entropi üretimi [kW/K]
- S_gen_ΔP: Akış sürtünmesi kaynaklı entropi üretimi [kW/K]

**Yorumlama:**
- Be > 0.5 → Isı transferi baskın → ΔT düşür (approach temperature azalt)
- Be < 0.5 → Sürtünme baskın → Akış direncini düşür (boru çapı artır, vana azalt)
- Be = 0.5 → Optimal denge noktası

### Entropi Üretim Sayısı (N_s)
```
N_s = S_gen / (Q̇/T_min)
```
Boyutsuz ölçek — farklı ekipmanları karşılaştırmak için kullanılır.

### EGM Karar Kuralları
- S_gen yüksek → Optimizasyon potansiyeli var
- Bejan sayısı → Hangi irreversibility kaynağını hedefle
- N_s > 0.5 → Ciddi termodinamik kayıp, acil müdahale gerekli
- N_s < 0.1 → Termodinamik açıdan iyi performans

### EGM vs Exergy Analizi
- **Exergy analizi:** "Bu ekipmanda 50 kW exergy yıkılıyor" (mevcut durum)
- **EGM:** "Bu ekipman şu parametrelerde olursa exergy yıkımı minimuma iner" (optimum tasarım)

Detaylı bilgi: `knowledge/factory/entropy_generation/` dizini (19 dosya)

## İleri Exergy Kavramları

### Kaçınılabilir/Kaçınılamaz Dekompozisyon (Avoidable/Unavoidable)
```
I_total = I_AV + I_UN
```
- **I_AV (Kaçınılabilir):** Mevcut teknoloji ile azaltılabilir exergy yıkımı
- **I_UN (Kaçınılamaz):** BAT (Best Available Technology) koşullarında bile mevcut olan yıkım
- **θ = I_AV / I_total:** Göreceli kaçınılabilirlik oranı

| θ Aralığı | Sınıf | Anlamı |
|-----------|-------|--------|
| > 0.5 | Yüksek | Büyük iyileştirme potansiyeli |
| 0.3-0.5 | Orta | Anlamlı potansiyel |
| < 0.3 | Düşük | Çoğunlukla termodinamik limit |

### Endojen/Ekzojen Dekompozisyon (Endogenous/Exogenous)
```
I_total = I_EN + I_EX
```
- **I_EN (Endojen):** Bileşenin kendi iç tersinmezliğinden kaynaklanan yıkım
- **I_EX (Ekzojen):** Diğer bileşenlerin performansından kaynaklanan dolaylı yıkım

### 4-Yollu Dekompozisyon (Four-Way Splitting)
```
I_total = I_EN_AV + I_EN_UN + I_EX_AV + I_EX_UN
```
| Kategori | Anlamı | Aksiyon |
|----------|--------|---------|
| I_EN_AV | Bileşenin kendi kaçınılabilir yıkımı | Bileşeni iyileştir (1. öncelik) |
| I_EN_UN | Bileşenin kaçınılamaz yıkımı | Aksiyon yok (limit) |
| I_EX_AV | Diğer bileşenlerden kaynaklanan kaçınılabilir | Diğer bileşenleri iyileştir |
| I_EX_UN | Sistem yapısal limiti | Aksiyon yok |

**Gerçek iyileştirme potansiyeli:** IP_real = I_EN_AV + I_EX_AV

### Modifiye Exergetik Verimlilik
```
ε* = (Ex_P + I_UN) / (Ex_F - I_AV)
```
- Konvansiyonel ε'dan her zaman yüksektir
- ε* ≈ 1.0 ise bileşen zaten limitte çalışıyor

Detaylı bilgi: `knowledge/factory/advanced_exergy/` dizini (18 dosya)

## Exergoekonomik Temel Kavramlar

### SPECO Yöntemi (Specific Exergy Costing)
Exergy akışlarına maliyet atama metodolojisi:
```
Ċ = c × Ėx
```
- Ċ: Exergy maliyet akışı [€/saat]
- c: Birim exergy maliyeti [€/kWh]
- Ėx: Exergy akışı [kW]

### Exergy Yıkım Maliyeti (Ċ_D)
```
Ċ_D,k = c_F,k × Ėx_D,k
```
Her bileşenin exergy yıkımının parasal karşılığı.

### Exergoekonomik Faktör (f_k)
```
f_k = Ż_k / (Ż_k + Ċ_D,k)
```
- f_k < 0.25 → Exergy yıkım maliyeti baskın → Verim artır
- f_k = 0.25-0.65 → Dengeli
- f_k > 0.65 → Yatırım maliyeti baskın → Daha ucuz bileşen seç

### Göreceli Maliyet Farkı (r_k)
```
r_k = (c_P,k - c_F,k) / c_F,k
```
- r_k yüksek → Bileşen birim exergy maliyetini çok artırıyor
- Yüksek r_k + düşük f_k → Öncelikli iyileştirme hedefi

Detaylı bilgi: `knowledge/factory/exergoeconomic/` dizini (21 dosya)

## Pinch Analizi Temelleri

### Minimum Enerji Gereksinimi (MER)
Pinch analizi, bir prosesin minimum ısıtma (QH,min) ve soğutma (QC,min) ihtiyacını belirler.

### Bileşik Eğriler (Composite Curves)
Sıcak ve soğuk akışların sıcaklık-entalpi diyagramında üst üste çizilmesi:
- İki eğrinin en yakın noktası = **Pinch noktası**
- ΔT_min: Minimum yaklaşım sıcaklığı (genellikle 10-20°C)

### Üç Altın Kural (Pinch Rules)
1. **Pinch üzerinden ısı transferi yapma** (cross-pinch transfer)
2. **Pinch üstünde soğutma utility kullanma**
3. **Pinch altında ısıtma utility kullanma**

İhlal durumunda: Her kW cross-pinch transfer → +1 kW ısıtma + 1 kW soğutma utility

### Grand Composite Curve (GCC)
Utility seçimi ve çoklu utility seviyesi optimizasyonu için kullanılır.

Detaylı bilgi: `knowledge/factory/pinch/` dizini (18 dosya)
