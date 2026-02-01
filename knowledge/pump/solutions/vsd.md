---
title: "Çözüm: VSD (Değişken Hızlı Sürücü) ile Pompa Kontrolü — Variable Speed Drive for Pump Control"
category: solutions
equipment_type: pump
keywords: [VSD, değişken hız, pompa, enerji tasarrufu]
related_files: [pump/formulas.md, pump/benchmarks.md, pump/equipment/centrifugal.md]
use_when: ["Pompaya VSD önerisi değerlendirilirken", "Değişken debi ihtiyacı analiz edilirken"]
priority: high
last_updated: 2026-01-31
---
# Çözüm: VSD (Değişken Hızlı Sürücü) ile Pompa Kontrolü — Variable Speed Drive for Pump Control

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Sabit hızlı santrifüj pompalar, debi kontrolünü kısma vanası (throttle valve) ile sağlar. Vana kısıldığında pompa aynı güçte çalışmaya devam eder; fazla enerji vana üzerinde ısıya dönüşür. Affinity Laws gereği bu durum büyük enerji israfına yol açar.

**Çözüm:** VSD (Variable Speed Drive / Değişken Frekanslı Sürücü) ile pompa motor hızını gerçek zamanlı talebe göre ayarlamak. Kısma vanası yerine hız kontrolü ile debi ve basınç düzenlenir.

**Tipik Tasarruf:** %20-60 (sistem tipine bağlı)
**Tipik ROI:** 1-3 yıl

## Çalışma Prensibi

VSD, gelen AC elektriği DC'ye çevirir, ardından değişken frekanslı AC'ye geri dönüştürür:
- **Frekans kontrolü:** 10-60 Hz aralığında (50 Hz sabit yerine)
- **Hız kontrolü:** Motor hızı frekansla doğru orantılı: `N = 120 × f / P_kutup`
- **Debi kontrolü:** Santrifüj pompada debi hıza doğru orantılıdır
- **Kısma vanası eliminasyonu:** VSD ile vana tam açık kalır, enerji kaybı ortadan kalkar

## Affinity Laws (Benzerlik Yasaları) — Pompalarda

Affinity Laws santrifüj pompalar için tam geçerlidir (pozitif deplasmanlı pompalarda geçerli değildir):

| Parametre | İlişki | Açıklama |
|-----------|--------|----------|
| Debi (Q) | Q ∝ N | Debi, hızla doğru orantılı |
| Basınç (H) | H ∝ N² | Head, hızın karesi ile orantılı |
| Güç (P) | P ∝ N³ | Güç, hızın küpü ile orantılı |

**Kritik sonuç:** %50 hız düşüşünde teorik güç tüketimi sadece %12.5 olur. Ancak gerçek tasarruf, sistem eğrisinin statik ve dinamik head bileşenlerine bağlıdır.

## Sistem Eğrisi Türüne Göre Tasarruf

| Sistem Tipi | Statik Head Oranı | Dinamik (Sürtünme) Head Oranı | VSD Tasarrufu | Açıklama |
|-------------|-------------------|-------------------------------|---------------|----------|
| Yüksek sürtünme (HVAC, soğutma) | <%20 | >%80 | %40-60 | Affinity Laws tam etkili; VSD en verimli |
| Karışık sistem | %30-50 | %50-70 | %20-40 | Orta düzeyde tasarruf |
| Yüksek statik head (kuyu, yüksek bina) | >%60 | <%40 | %10-20 | VSD avantajı sınırlı; dikkatli analiz gerekli |

**Uyarı:** Yüksek statik head sistemlerinde hız düşürüldüğünde pompa hızla shut-off noktasına yaklaşır. Bu durumda VSD tek başına uygun çözüm olmayabilir.

## Kısmi Yük Tasarruf Karşılaştırması (Throttle vs VSD)

| Debi % | Throttle Vana Güç % | VSD Güç % | VSD Tasarrufu |
|--------|---------------------|-----------|---------------|
| 100% | 100% | 100% | %0 |
| 80% | ~85% | ~52% | ~%39 |
| 60% | ~75% | ~22% | ~%71 |
| 50% | ~70% | ~15% | ~%79 |
| 40% | ~68% | ~10% | ~%85 |

*Not: Tablo değerleri yüksek sürtünme head'li (düşük statik head) sistem içindir. Statik head arttıkça VSD tasarrufu azalır.*

## Uygulanabilirlik Kriterleri

### VSD Ne Zaman Uygulanmalı
- Debi gereksinimi zamanla %30-80 arasında değişiyorsa
- Kısma vanası sürekli kısık çalışıyorsa (<%80 açık)
- Bypass hattı açık çalışıyorsa
- HVAC soğutma/ısıtma sirkürasyon pompaları
- Proses suyu sistemleri (değişken üretim)
- Sistem ağırlıklı olarak sürtünme head'ine sahipse

### VSD Ne Zaman Uygulanmamalı
- Sürekli tam yük (>%90): VSD elektroniği %2-3 kayıp ekler
- Çok küçük pompalar (<2 kW): Maliyet/fayda dengesizliği
- Yüksek statik head oranı (>%70): Tasarruf potansiyeli düşük
- Pozitif deplasmanlı pompalar: Affinity Laws geçerli değil
- Pompa minimum hızın altında kavitasyon riski varsa

## Minimum Hız Sınırları

| Konu | Minimum Hız Limiti | Açıklama |
|------|-------------------|----------|
| Kavitasyon (NPSH) | Genelde >%30 nominal hız | Düşük hızda NPSH margin azalabilir |
| Motor soğutma | >%20-25 nominal hız | Ayrı soğutma fanı yoksa motor aşırı ısınır |
| Yataklama (bearing) | >%15-20 nominal hız | Yağ filmi stabilitesi bozulur |
| Mekanik salmastra | >%25 nominal hız | Yüzey hızı yetersiz kalır |
| Rezonans | Belirli hız aralıkları atlanmalı | Kritik hızlar VSD'de bypass frekansı olarak girilmeli |

## Retrofit vs Yeni VSD Pompa

| Faktör | VSD Retrofit (Mevcut Pompaya) | Yeni VSD Entegre Pompa |
|--------|-------------------------------|----------------------|
| Yatırım maliyeti | Yeni ünitenin %30-50'si | Tam yeni ünite maliyeti |
| Motor uyumluluğu | IE3/IE4 invertör uyumlu motor gerekebilir | Fabrika eşleştirilmiş |
| Pompa optimizasyonu | Sabit hız için optimize impeller | Değişken hız için optimize tasarım |
| Hız aralığı | %30-100 (sınırlı) | %20-100 (geniş) |
| Verimlilik | İyi, ancak entegre çözümden %3-8 düşük | En iyi kısmi yük verimi |
| Garanti | Orijinal garanti etkilenebilir | Tam üretici garantisi |
| Tavsiye edilen durum | Bütçe kısıtlı; pompa <8 yaş | Pompa yenileme zamanı gelmiş |

## Yatırım Maliyeti

| Pompa Gücü | VSD Retrofit (Sürücü + Kurulum) | Yeni VSD Entegre Pompa |
|------------|--------------------------------|----------------------|
| 5.5 kW | €2,500-4,500 | €6,000-10,000 |
| 11 kW | €3,500-6,000 | €10,000-16,000 |
| 22 kW | €5,000-9,000 | €16,000-25,000 |
| 37 kW | €7,000-12,000 | €22,000-35,000 |
| 55 kW | €10,000-16,000 | €30,000-48,000 |
| 75 kW | €13,000-20,000 | €40,000-60,000 |
| 110 kW | €18,000-28,000 | €55,000-85,000 |
| 160 kW | €24,000-38,000 | €75,000-115,000 |

*Kurulum maliyetleri kablo, trafo, harmonik filtre ve devreye alma dahil.*

## ROI Hesabı

### Formül
```
Yıllık_tasarruf_kWh = P_nominal × Çalışma_saati × (Güç%_Throttle - Güç%_VSD) / 100
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Yıllık_tasarruf_EUR
```

### Örnek Hesap
- 55 kW santrifüj pompa, 6,000 saat/yıl, ortalama %65 debi gereksinimi
- Sistem: düşük statik head, ağırlıklı sürtünme head
- Elektrik: €0.15/kWh
- Throttle ile: ~%78 güç = 42.9 kW ortalama
- VSD ile: ~%28 güç = 15.4 kW ortalama (kübik yasa etkisi)
- Yıllık tasarruf: (42.9 - 15.4) × 6,000 = 165,000 kWh = **€24,750/yıl**
- VSD retrofit maliyeti: €14,000
- **Geri ödeme: 14,000 / 24,750 = 0.57 yıl (≈7 ay)**

*Not: Bu, sürtünme ağırlıklı ideal bir senaryodur. Statik head yüksek sistemlerde geri ödeme 2-3 yıla uzayabilir.*

## Uygulama Adımları

1. **Sistem analizi:** Mevcut sistem eğrisini belirle; statik ve dinamik head bileşenlerini hesapla
2. **Yük profili ölçümü:** Minimum 1 haftalık debi/basınç profilleme ile gerçek talep dağılımını ölç
3. **Tasarruf hesabı:** Affinity Laws ve gerçek sistem eğrisi ile beklenen tasarrufu hesapla
4. **VSD kararı:** Retrofit veya yeni VSD pompa arasında karar ver
5. **Elektrik altyapısı:** Harmonik filtre, EMC uyumu, kablo boyutu ve motor uyumluluğunu kontrol et
6. **Kurulum ve devreye alma:** VSD parametreleri (min/max frekans, rampa süreleri, bypass frekansları) ayarla
7. **Doğrulama:** Kurulum sonrası 2 haftalık güç profilleme ile gerçek tasarrufu ölç ve doğrula

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Harmonikler | VSD elektrik şebekesine harmonik bozulma yaratır | Harmonik filtre, IEEE 519 uyumu |
| Motor ısınma | Düşük hızda motor soğutması azalır | İnvertör uyumlu motor (IE3+), ayrı fan |
| Kavitasyon | Düşük hızda NPSH margin değişir | Minimum hız sınırı belirle, NPSH hesabı yap |
| Rezonans | Belirli hızlarda mekanik rezonans | Kritik frekansları belirle, bypass frekansı ayarla |
| EMC parazit | Elektromanyetik girişim | Ekranlı kablolar, uygun topraklama |
| Yatak ömrü | Düşük hızda yağlama yetersizliği | Minimum hız limiti (%20-25) |

## İlgili Dosyalar
- Pompa exergy formülleri: `formulas/pump_exergy.md`
- Pompa boyutlandırma: `solutions/pump_right_sizing.md`
- İmpeller kesme: `solutions/pump_impeller_trimming.md`
- Paralel pompa: `solutions/pump_parallel_operation.md`
- Sistem optimizasyonu: `solutions/pump_system_optimization.md`

## Referanslar
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition
- DOE Pumping Systems Tip Sheet #11, "Adjustable Speed Pumping Applications"
- Europump / Hydraulic Institute / DOE, "Variable Speed Pumping: A Guide to Successful Applications"
- Hydraulic Institute, ANSI/HI 14.3-2019, "Rotodynamic Pumps for Design and Application"
- Europump, "Assessing the Energy Efficiency of Pumps and Pump Units"
