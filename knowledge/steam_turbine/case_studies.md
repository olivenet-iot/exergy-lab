---
title: "Buhar Türbini Vaka Çalışmaları — Steam Turbine Case Studies"
category: reference
equipment_type: steam_turbine
keywords: [buhar türbini, vaka çalışması, CHP, ORC, PRV, Türkiye]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/orc.md, steam_turbine/equipment/micro_turbine.md]
use_when: ["Referans vaka çalışması gerektiğinde", "Benzer projeler araştırılırken"]
priority: low
last_updated: 2026-01-31
---
# Buhar Türbini Vaka Çalışmaları — Steam Turbine Case Studies

> Son güncelleme: 2026-01-31

Bu dosya, Türk endüstrisinden gerçekçi buhar türbini ve CHP uygulamalarını içermektedir. Her vaka; tesis bilgileri, mevcut durum, uygulama detayları, exergy analizi sonuçları ve çıkarılan derslerle birlikte sunulmaktadır.

---

## 1. Şeker Fabrikası — Karşı Basınçlı (Back-Pressure) CHP

### Tesis Bilgileri

| Parametre | Değer |
|-----------|-------|
| Sektör | Şeker (Sugar) |
| Konum | Orta Anadolu, Türkiye |
| Kapasite | 6,000 ton pancar/gün |
| Çalışma modu | Kampanya dönemi (Ekim-Ocak) |
| Yıllık çalışma süresi | 5,000 saat/yıl |
| Yakıt | Biyokütle (küspe — bagasse) + doğalgaz destek |

### Mevcut Durum

Tesis, 40 bar / 400°C girişli, 4 bar çıkışlı, 10 MW nominal güçlü bir karşı basınçlı (back-pressure) buhar türbinine sahiptir. Çıkış buharı tamamen proses ısıtma (evaporatörler, kristalizasyon, kurutma) için kullanılmaktadır. Kazan yakıtının yaklaşık %60'ı küspeden (bagasse), %40'ı doğalgazdan karşılanmaktadır.

Türbin 2008 yılında devreye alınmış olup son major overhaul 2019'da yapılmıştır. Mevcut çalışma saati: ~55,000 saat.

### Uygulama — Exergy Analizi ve Performans Değerlendirmesi

```
Giriş koşulları:
  P_giriş = 40 bar, T_giriş = 400°C
  h_giriş = 3,214 kJ/kg, s_giriş = 6.769 kJ/(kg·K)
  ex_giriş = 1,200 kJ/kg

Çıkış koşulları:
  P_çıkış = 4 bar
  η_is = %78 (ölçülen — design %82)
  h_çıkış = 2,855 kJ/kg
  s_çıkış = 7.08 kJ/(kg·K)
  ex_çıkış = 740 kJ/kg

Buhar debisi: ṁ = 52 ton/h = 14.44 kg/s

Türbin gücü:
  Ẇ_türbin = 14.44 × (3,214 - 2,855) = 5,182 kW
  Ẇ_elek = 5,182 × 0.98 × 0.97 = 4,926 kW ≈ 4.9 MW

Exergy dengesi:
  Ėx_giriş = 14.44 × 1,200 = 17,328 kW
  Ėx_çıkış = 14.44 × 740 = 10,686 kW
  Ẇ_türbin = 5,182 kW
  Ėx_yıkım = 17,328 - 10,686 - 5,182 = 1,460 kW

Exergy verimi (iş bazlı):
  η_ex,iş = 5,182 / (17,328 - 10,686) = 5,182 / 6,642 = %78.0

CHP exergy verimi:
  Q̇_proses = 14.44 × (2,855 - 335) = 36,385 kW = 36.4 MW_th
  T_proses,ort = 385 K → Ex_proses = 36,385 × (1 - 298.15/385) = 8,208 kW
  Q̇_yakıt = 47,500 kW (kazan η = %86)
  Ėx_yakıt = 47,500 × 1.04 = 49,400 kW (doğalgaz-biyokütle karışım φ)
  η_ex,CHP = (4,926 + 8,208) / 49,400 = %26.6 → Orta/düşük sınır

HPR = 36,385 / 4,926 = 7.39
η_enerji = (4,926 + 36,385) / 47,500 = %86.9
PES = 1 - 1 / (0.104/0.442 + 0.766/0.90) = %13.2 → Yüksek verimli CHP ✓
```

### Sonuçlar

| Parametre | Değer | Benchmark | Durum |
|-----------|-------|-----------|-------|
| η_is | %78 | %65-78 (şeker sektörü) | Kabul edilebilir |
| η_ex,iş | %78.0 | >%72 İyi | İyi |
| η_ex,CHP | %26.6 | %25-35 (şeker) | Orta — iyileştirme potansiyeli |
| HPR | 7.39 | 5-10 (BP türbin) | Normal |
| η_enerji | %86.9 | %78-88 | İyi |
| PES | %13.2 | >%10 gerekli | Uygun |

**Tespit edilen kayıplar:**
- η_is design'dan %4 puan düşük → ~55K saat çalışma sonucu bozunma
- Ėx_yıkım = 1,460 kW → toplam giriş exergisinin %8.4'ü türbin iç tersinmezliği

### ROI Tablosu

| Öneri | Yıllık Tasarruf | Yatırım | SPP |
|-------|-----------------|---------|-----|
| Sızdırmazlık yenileme (η_is +%2) | €42,000 | €35,000 | 0.8 yıl |
| Kanat muayene + kaplama | €65,000 | €120,000 | 1.8 yıl |
| Küspe kurutucu (yakıt tasarrufu) | €80,000 | €200,000 | 2.5 yıl |
| Toplam overhaul (η_is +%4) | €130,000 | €280,000 | 2.2 yıl |

### Dersler (Lessons Learned)

1. Kampanya dönemi çalışmasında (5,000 saat/yıl) sık devreye alma/devreden çıkarma termal yorulmaya neden olur; overhaul aralığı saat yerine **çevrim sayısı** ile de değerlendirilmelidir.
2. Biyokütle yakıtlarda (küspe) nem oranı değişkenliği kazan verimini %82-90 arasında sallandırır; bu durum türbin giriş koşullarını da etkiler.
3. Şeker sektöründe η_ex,CHP genelde düşüktür çünkü proses buharı düşük sıcaklıkta (4 bar, ~144°C) kullanılır — exergy içeriği düşüktür.
4. %4 η_is bozunması yıllık ~€130,000 ek yakıt maliyetine karşılık gelir; overhaul ROI 2.2 yıl ile cazip seviyededir.

---

## 2. Kağıt Fabrikası — Extraction-Condensing Türbin

### Tesis Bilgileri

| Parametre | Değer |
|-----------|-------|
| Sektör | Kağıt ve Karton (Pulp & Paper) |
| Konum | Marmara Bölgesi, Türkiye |
| Kapasite | 250,000 ton/yıl ambalaj kartonu |
| Çalışma modu | Sürekli — yıl boyu |
| Yıllık çalışma süresi | 8,000 saat/yıl |
| Yakıt | Doğalgaz |

### Mevcut Durum

15 MW extraction-condensing buhar türbini, 60 bar / 480°C giriş buharı ile çalışmaktadır. İki çekiş noktası bulunmaktadır:
- Birincil çekiş (primary extraction): 6 bar — kağıt kurutma silindirlerine
- İkincil çekiş (secondary extraction): 2 bar — hamur hazırlama ve genel ısıtma

Yoğuşma bölümü 0.07 bar vakumda çalışarak ek elektrik üretmektedir.

### Uygulama — Verim İyileştirme Projesi

İyileştirme öncesi ve sonrası karşılaştırma:

```
İYİLEŞTİRME ÖNCESİ (2023 denetimi):

Giriş: P = 60 bar, T = 480°C, ṁ = 72 ton/h = 20 kg/s
  h_giriş = 3,380 kJ/kg, ex_giriş = 1,320 kJ/kg

Birincil çekiş (6 bar): ṁ_ext1 = 12 ton/h = 3.33 kg/s
İkincil çekiş (2 bar): ṁ_ext2 = 18 ton/h = 5.0 kg/s
Yoğuşma: ṁ_kond = 42 ton/h = 11.67 kg/s

Ölçülen η_is = %76 (design: %83)
  → %7 puan bozunma (65K saat, 2006 devreye alma)
  → Ölçülen güç: 12.8 MW (design: 15 MW @ tam yük)

Exergy analizi:
  Ėx_giriş = 20 × 1,320 = 26,400 kW
  Ẇ_türbin = 12,800 kW
  Ėx_çekiş1 = 3.33 × 520 = 1,732 kW (6 bar çıkış)
  Ėx_çekiş2 = 5.0 × 310 = 1,550 kW (2 bar çıkış)
  Ėx_kondenser = 11.67 × 48 = 560 kW (vakum)
  Ėx_yıkım = 26,400 - 12,800 - 1,732 - 1,550 - 560 = 9,758 kW

  η_ex,iş = 12,800 / 26,400 = %48.5 (düşük — condensing kısmı dahil)
  η_ex,CHP = (12,800 + 1,732 + 1,550) / (Ėx_yakıt)
    Ėx_yakıt = Q̇_yakıt × 1.04 = (72 × (3,380 - 335) / 0.88) × 1.04 / 3.6
    ≈ 72,000 × 1.04 / 3.6 ≈ 65,100 kW (yaklaşık)
  η_ex,CHP ≈ 16,082 / 65,100 = %24.7 (düşük)

İYİLEŞTİRME SONRASI (2024, major overhaul + kontrol sistemi yenileme):

Yapılan işlemler:
1. Major overhaul — rotor çıkarma, kanat muayene/değişim
2. Tüm sızdırmazlıklar yenileme (interstage + shaft seals)
3. Governor/kontrol sistemi dijitale dönüştürme
4. Kondenser temizliği ve vakum sistemi iyileştirme

İyileşme:
  η_is: %76 → %82 (+%6 puan)
  Ẇ_türbin: 12,800 → 14,200 kW (+1,400 kW, +%10.9)
  Kondenser vakum: 0.07 bar → 0.055 bar (iyileştirme)

Ek güç kazancı: 1,400 kW × 8,000 saat = 11,200 MWh/yıl
```

### Sonuçlar

| Parametre | Önce | Sonra | İyileşme |
|-----------|------|-------|----------|
| η_is | %76 | %82 | +%6 puan |
| Ẇ_elek | 12.8 MW | 14.2 MW | +1.4 MW |
| η_ex,CHP | %24.7 | %29.1 | +%4.4 puan |
| Yıllık üretim | 102,400 MWh | 113,600 MWh | +11,200 MWh |
| Kondenser vakum | 0.070 bar | 0.055 bar | -15 mbar |

### ROI Tablosu

| Kalem | Değer |
|-------|-------|
| Toplam yatırım (overhaul + kontrol + kondenser) | €650,000 |
| Ek yıllık elektrik üretimi | 11,200 MWh |
| Elektrik birim fiyatı (şebeke alış tasarrufu) | €0.085/kWh |
| Yıllık tasarruf | €952,000 |
| Basit geri ödeme süresi (SPP) | 0.68 yıl |
| 10 yıllık NPV (%8 iskonto) | €5.7M |
| IRR | >%100 |

### Dersler (Lessons Learned)

1. %7 η_is bozunması olan 65K saatlik bir extraction-condensing türbinde overhaul **en yüksek ROI** yatırımıdır.
2. Kontrol sistemi dijitalleştirmesi (DCS/PLC tabanlı) extraction noktalarında optimum debi dağılımı sağlayarak ek %1-2 verim kazanımı getirir.
3. Kondenser vakum iyileştirmesi (15 mbar) yalnızca yoğuşma kısmındaki güce etki eder; kağıt sektöründe extraction oranı yüksek olduğundan etkisi sınırlı kalabilir.
4. Kağıt sektöründe 8,000 saat/yıl sürekli çalışma, yatırım geri dönüş süresini önemli ölçüde kısaltır.

---

## 3. Kimya Tesisi — ORC Atık Isı Geri Kazanımı

### Tesis Bilgileri

| Parametre | Değer |
|-----------|-------|
| Sektör | Kimya (Petrochemicals) |
| Konum | İzmit Körfezi, Türkiye |
| Proses | Ekzotermik reaktör (polimerizasyon) |
| Atık ısı kaynağı | Reaktör soğutma suyu, 180°C |
| Atık ısı kapasitesi | 3,500 kW_th (sürekli) |
| Yıllık çalışma süresi | 7,500 saat/yıl |

### Mevcut Durum

Ekzotermik polimerizasyon reaktöründen çıkan 180°C soğutma suyu (basınçlı), mevcut durumda kule soğutucusu (cooling tower) ile atmosfere atılmaktadır. Bu, yüksek exergy içerikli bir ısının tamamen yok edilmesi anlamına gelmektedir.

```
Atık ısı exergy potansiyeli:
  Q̇_atık = 3,500 kW
  T_kaynak = 180°C = 453.15 K
  T₀ = 298.15 K

  Ėx_atık = 3,500 × (1 - 298.15/453.15) = 3,500 × 0.342 = 1,197 kW
  → 1.2 MW exergy potansiyeli boşa gidiyor
```

### Uygulama — 500 kW ORC Sistemi

```
ORC sistem özellikleri:
  Çalışma akışkanı: R245fa
  Güç çıkışı: 500 kW_e (net)
  Evaporatör: 180°C giriş → 120°C çıkış (kaynak tarafı)
  Kondenser: Hava soğutmalı, 35°C

Termal verim:
  η_th = 500 / 3,500 = %14.3

Exergy verimi:
  η_ex = 500 / 1,197 = %41.8

Exergy dengesi (ORC sistemi):
  Ėx_giriş = 1,197 kW (ısı kaynağından)
  Ẇ_net = 500 kW (elektrik)
  Ėx_kondenser = 1,197 × 0.08 = 96 kW (atık — düşük T)
  Ėx_yıkım = 1,197 - 500 - 96 = 601 kW

Exergy yıkım dağılımı:
  Evaporatör ΔT kayıpları: ~250 kW (%42)
  Türbin iç kayıplar: ~180 kW (%30)
  Kondenser ΔT kayıpları: ~120 kW (%20)
  Pompa + diğer: ~51 kW (%8)
```

### Sonuçlar

| Parametre | Değer | Benchmark (100-150°C ORC) | Durum |
|-----------|-------|---------------------------|-------|
| η_th | %14.3 | %12-18 | İyi |
| η_ex | %41.8 | %35-55 | Ortalama-İyi |
| Net güç | 500 kW | — | — |
| Yıllık üretim | 3,750 MWh | — | — |
| Spesifik maliyet | 2,800 EUR/kW | 1,500-4,000 | Ortalama |

### ROI Tablosu

| Kalem | Değer |
|-------|-------|
| ORC modül (500 kW, R245fa, hava soğutmalı) | €1,050,000 |
| Montaj + bağlantı + mühendislik | €280,000 |
| Otomasyon ve elektrik bağlantısı | €70,000 |
| **Toplam yatırım** | **€1,400,000** |
| Yıllık elektrik üretimi | 3,750 MWh |
| Elektrik birim fiyatı (şebeke alışı) | €0.085/kWh |
| Yıllık tasarruf | €318,750 |
| Basit geri ödeme süresi (SPP) | 4.4 yıl |
| 15 yıllık NPV (%8 iskonto) | €1.33M |
| IRR | %19.5 |

### Dersler (Lessons Learned)

1. ORC sistemleri 150-200°C aralığında %12-18 termal verime ulaşabilir; ancak exergy verimi %40-55 aralığında olup termodinamik potansiyelin iyi değerlendirildiğini gösterir.
2. Hava soğutmalı kondenser seçimi su tüketimini sıfırlar, ancak yaz aylarında (ortam 35-40°C) güç çıkışı %8-12 düşer; yıllık ortalama hesaplarda bu mevsimsellik dikkate alınmalıdır.
3. R245fa mevcut durumda yaygın ORC akışkanıdır, ancak GWP = 1,030 olması nedeniyle gelecekte R1233zd(E) (GWP = 1) geçişi planlanmalıdır.
4. Kimya sektöründe ekzotermik reaktör atık ısıları genellikle sürekli ve kararlıdır — ORC için ideal kaynak profilidir.
5. €2,800/kW birim maliyet, ORC için ortalama seviyededir; daha büyük kapasiteler (>1 MW) birim maliyeti €1,500-2,200/kW'a indirebilir.

---

## 4. Gıda Fabrikası — Mikro Türbin ile PRV İkamesi

### Tesis Bilgileri

| Parametre | Değer |
|-----------|-------|
| Sektör | Gıda İşleme (Süt ürünleri) |
| Konum | Güneydoğu Anadolu, Türkiye |
| Ürün | UHT süt, peynir, yoğurt |
| Buhar sistemi | 20 bar kazan → PRV → 4 bar proses |
| Buhar debisi | 8 ton/h (ortalama) |
| Yıllık çalışma süresi | 6,500 saat/yıl |

### Mevcut Durum

Tesiste 20 bar'lık kazan buharı, bir basınç düşürücü vana (PRV — Pressure Reducing Valve) ile 4 bar proses basıncına düşürülmektedir. PRV'de izentalpik (enthalpy sabit) bir genişleme gerçekleşir; bu süreç tamamen tersinmez (irreversible) olup buharın exergisi boşa harcanır.

```
PRV exergy kaybı hesabı:
  ṁ = 8 ton/h = 2.222 kg/s

  PRV giriş (20 bar, doymuş buhar):
    h_giriş = 2,799 kJ/kg, s_giriş = 6.340 kJ/(kg·K)
    ex_giriş = (2,799 - 104.89) - 298.15 × (6.340 - 0.3674) = 913 kJ/kg

  PRV çıkış (4 bar, izentalpik → h_çıkış = h_giriş = 2,799 kJ/kg):
    s_çıkış = 7.172 kJ/(kg·K) (kızdırılmış buhar @ 4 bar, 2,799 kJ/kg)
    ex_çıkış = (2,799 - 104.89) - 298.15 × (7.172 - 0.3674) = 666 kJ/kg

  Exergy kaybı (PRV):
    Δex = 913 - 666 = 247 kJ/kg
    Ėx_kayıp = 2.222 × 247 = 549 kW → Tamamen boşa giden exergy!

  Yıllık exergy kaybı: 549 × 6,500 = 3,568 MWh/yıl
```

### Uygulama — 250 kW Mikro Türbin Kurulumu

```
Mikro türbin özellikleri:
  Tip: Tek kademeli aksiyal (single-stage axial)
  Güç: 250 kW (brüt), 240 kW (net, yardımcılar dahil)
  Giriş: 20 bar doymuş buhar
  Çıkış: 4 bar
  η_is: %62 (tek kademe, küçük türbin)
  η_mek × η_jen: %94

Türbin performansı:
  Ẇ_türbin = 2.222 × (2,799 - h_çıkış) [kW]
  h_çıkış,is (izentropik, s = 6.340 @ 4 bar) = 2,385 kJ/kg
  h_çıkış = 2,799 - 0.62 × (2,799 - 2,385) = 2,799 - 256.7 = 2,542 kJ/kg

  Ẇ_türbin = 2.222 × (2,799 - 2,542) = 571 kW
  Ẇ_elek = 571 × 0.94 = 537 kW

  Not: Gerçek güç debiye ve koşullara göre değişir.
  Nominal koşullarda ~250 kW net (garanti) değeri kullanılmıştır.

  Exergy verimi:
  η_ex = 250 / 549 = %45.5
  (PRV'de bu değer %0'dı — tamamen kayıp)

  Kalan exergy kaybı = 549 - 250 = 299 kW
  → Mikro türbin PRV kaybının %45.5'ini geri kazanıyor
```

### Sonuçlar

| Parametre | PRV (Mevcut) | Mikro Türbin | İyileşme |
|-----------|-------------|--------------|----------|
| Exergy kaybı | 549 kW (%100) | 299 kW (%54.5) | -%45.5 |
| Elektrik üretimi | 0 kW | 250 kW | +250 kW |
| Proses buharı | Değişiklik yok | Değişiklik yok | Aynı |
| Yıllık elektrik | 0 | 1,625 MWh | +1,625 MWh |

### ROI Tablosu

| Kalem | Değer |
|-------|-------|
| Mikro türbin modülü (250 kW) | €525,000 |
| Montaj, boru, vana, bypass sistemi | €95,000 |
| Elektrik bağlantısı ve otomasyon | €55,000 |
| **Toplam yatırım** | **€675,000** |
| Yıllık elektrik üretimi | 1,625 MWh |
| Elektrik birim fiyatı | €0.085/kWh |
| Yıllık bakım maliyeti | €12,000 |
| Net yıllık tasarruf | €126,125 |
| Basit geri ödeme süresi (SPP) | 5.4 yıl |
| 15 yıllık NPV (%8 iskonto) | €405,000 |
| IRR | %15.2 |

**Not:** Elektrik birim fiyatı €0.10/kWh'e yükseldiğinde SPP = 4.5 yıla düşer. Daha yüksek debi (>12 ton/h) ve daha büyük ΔP koşullarında SPP 2-3 yıla kadar inebilir.

### Dersler (Lessons Learned)

1. PRV ikamesi, **sıfır ek yakıt ile** elektrik üreten nadir projelerdendir — mevcut buhar akışındaki exergy potansiyelini değerlendirir.
2. 8 ton/h ve 16 bar ΔP koşullarında potansiyel 250 kW civarıdır; debi >3 ton/h ve ΔP >10 bar olan her PRV noktası türbin ikamesi için değerlendirilmelidir.
3. Tek kademeli mikro türbin η_is değeri (%55-65) büyük çok kademeli türbinlerden düşüktür; ancak basitlik ve düşük bakım avantajı sunar.
4. Bypass PRV hattı mutlaka korunmalıdır — türbin bakım/arıza durumunda proses buharı kesintisiz devam etmelidir.
5. Gıda sektöründe hijyen gereksinimleri nedeniyle buhar kalitesi kritiktir; türbin çıkış buharının prosese uygunluğu doğrulanmalıdır.

---

## 5. Tekstil Fabrikası — CHP Modernizasyon (Overhaul vs. Yenileme)

### Tesis Bilgileri

| Parametre | Değer |
|-----------|-------|
| Sektör | Tekstil (Boyahane + Kurutma) |
| Konum | Bursa, Türkiye |
| Kapasite | 15,000 ton kumaş/yıl |
| Çalışma modu | Sürekli — 2 vardiya |
| Yıllık çalışma süresi | 6,000 saat/yıl |
| Yakıt | Doğalgaz |

### Mevcut Durum

Tesiste 1994 yılında devreye alınmış, 3 MW nominal güçlü bir karşı basınçlı buhar türbini bulunmaktadır. 30 yıllık hizmet süresinde 2 kez major overhaul yapılmıştır (2006 ve 2016). Mevcut çalışma saati: ~120,000 saat.

```
Mevcut performans:
  Giriş: 25 bar, 350°C
  Çıkış: 3 bar (proses — boyahane + kurutma)
  ṁ = 22 ton/h = 6.11 kg/s
  η_is = %58 (design: %70 — %12 puan bozunma)
  Ẇ_elek = 1,650 kW (design: 3,000 kW)

  h_giriş = 3,120 kJ/kg, ex_giriş = 1,050 kJ/kg
  h_çıkış = 2,843 kJ/kg (gerçek)
  h_çıkış,is = 2,643 kJ/kg

  Exergy analizi:
  Ėx_giriş = 6.11 × 1,050 = 6,416 kW
  Ẇ_türbin = 6.11 × (3,120 - 2,843) = 1,693 kW
  η_ex,iş = %48.2 → Kritik seviye (<60%)
```

### Uygulama — İki Senaryo Karşılaştırması

**Senaryo A: Major Overhaul (Mevcut Türbin)**
```
Kapsam: Rotor çıkarma, kanat değişimi, sızdırmazlık, rulman, vana
Beklenen iyileşme: η_is %58 → %66 (+%8 puan)
Overhaul süresi: 6 hafta
Kalan ömür: ~5-8 yıl (sonra yeniden overhaul veya değiştirme)

Overhaul sonrası:
  Ẇ_elek ≈ 2,100 kW (tahmini)
  Ek güç: +450 kW
  Yıllık ek üretim: 450 × 6,000 = 2,700 MWh
```

**Senaryo B: Yeni Yüksek Verimli Türbin**
```
Kapsam: Mevcut türbin sökümü, yeni çok kademeli BP türbin montajı
Yeni türbin: 3.5 MW, η_is = %78
Devreye alma süresi: 4-5 ay (imalat + montaj)
Beklenen ömür: 25-30 yıl

Yeni türbin performansı:
  Giriş: 25 bar, 350°C (mevcut kazan ile uyumlu)
  Çıkış: 3 bar
  η_is = %78
  Ẇ_elek = 2,900 kW
  Ek güç (mevcut duruma göre): +1,250 kW
  Yıllık ek üretim: 1,250 × 6,000 = 7,500 MWh

  η_ex,iş = %72.4 → İyi seviye
```

### Sonuçlar — Karşılaştırma

| Parametre | Mevcut | Senaryo A (Overhaul) | Senaryo B (Yeni) |
|-----------|--------|----------------------|------------------|
| η_is | %58 | %66 | %78 |
| η_ex,iş | %48.2 | %55.8 | %72.4 |
| Ẇ_elek | 1,650 kW | 2,100 kW | 2,900 kW |
| Yatırım | — | €180,000 | €1,800,000 |
| Yıllık ek tasarruf | — | €229,500 | €637,500 |
| SPP | — | 0.8 yıl | 2.8 yıl |
| Kalan ömür | 2-4 yıl | 5-8 yıl | 25-30 yıl |
| 15 yıllık NPV (%8) | — | €750,000* | €3,660,000 |

*Overhaul NPV'si 8 yılda yeniden overhaul veya değiştirme maliyetini içerir.

### ROI Tablosu — Seçilen Senaryo: B (Yeni Türbin)

| Kalem | Değer |
|-------|-------|
| Yeni türbin (3.5 MW BP) | €1,400,000 |
| Sökum + montaj + mühendislik | €250,000 |
| Elektrik ve otomasyon | €100,000 |
| Eski türbin hurda değeri | -€50,000 |
| İşletme kaybı (4.5 ay duruş) | €100,000 |
| **Toplam net yatırım** | **€1,800,000** |
| Yıllık ek elektrik üretimi | 7,500 MWh |
| Yıllık tasarruf | €637,500 |
| SPP | 2.8 yıl |
| IRR | %32 |

### Dersler (Lessons Learned)

1. 30 yıllık bir türbinde %12 puan η_is bozunması, toplam güç çıkışının %45'ini kaybettirmektedir — kümülatif etkisi çok yüksektir.
2. Overhaul seçeneği düşük SPP sunar (0.8 yıl) ancak kalan ömür sınırlıdır (5-8 yıl); uzun vadede yeni türbin daha avantajlıdır.
3. Karar kriteri olarak **yalnızca SPP değil**, 15-20 yıllık NPV ve kalan ömür birlikte değerlendirilmelidir.
4. >100K saat veya η_is bozunma >%10 olan türbinlerde yeni türbin seçeneği ciddi olarak incelenmelidir.
5. Yeni türbin giriş koşullarının mevcut kazan kapasitesiyle uyumlu olması kritiktir; kazan yetersizse kazan yenileme de projeye dahil edilmelidir.
6. Tekstil sektöründe CHP modernizasyonu, boyahane + kurutma proseslerinin yoğun buhar talebi nedeniyle yüksek HPR (>8) ile yüksek enerji verimi sağlar, ancak exergy verimi düşük kalır (proses sıcaklığı ~134°C).

---

## Vaka Çalışmaları Özet Karşılaştırma

| Vaka | Sektör | Uygulama | Güç [kW] | η_ex | Yatırım [EUR] | SPP [yıl] |
|------|--------|----------|----------|------|---------------|-----------|
| 1 | Şeker | BP CHP (mevcut analiz) | 4,926 | %26.6 (CHP) | Overhaul: €280K | 2.2 |
| 2 | Kağıt | Extraction-Condensing (overhaul) | 14,200 | %29.1 (CHP) | €650K | 0.68 |
| 3 | Kimya | ORC atık ısı | 500 | %41.8 | €1,400K | 4.4 |
| 4 | Gıda | Mikro türbin PRV ikamesi | 250 | %45.5 | €675K | 5.4 |
| 5 | Tekstil | Yeni türbin (modernizasyon) | 2,900 | %72.4 (iş) | €1,800K | 2.8 |

**Genel gözlem:** Overhaul projeleri en kısa SPP'yi sunar (0.7-2.2 yıl), ORC ve mikro türbin projeleri daha uzun geri dönüş süresine sahiptir (4-5.5 yıl) ancak atık enerji/exergy geri kazanımı sağladıkları için ek yakıt tüketmezler.

---

## İlgili Dosyalar

- [Formüller](formulas.md) — Exergy hesaplama formülleri
- [Benchmarklar](benchmarks.md) — Türbin verimlilik karşılaştırma verileri
- [Karşı Basınçlı Türbin](equipment/back_pressure.md) — BP türbin detayları
- [ORC](equipment/orc.md) — Organic Rankine Cycle bilgileri
- [Mikro Türbin](equipment/micro_turbine.md) — Mikro türbin PRV ikamesi
- [Verim İyileştirme](solutions/efficiency_improvement.md) — İyileştirme çözümleri
- [Bakım](solutions/maintenance.md) — Bakım ve overhaul planlaması
- [CHP Sistemleri](systems/steam_turbine_chp.md) — CHP konfigürasyonları
- [Fizibilite](economics/feasibility.md) — CHP fizibilite kriterleri
- [Fabrika Benchmarkları](../factory/factory_benchmarks.md) — Fabrika sektörel benchmark

## Referanslar

- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition, McGraw-Hill.
- Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
- US DOE (2012). *Improving Steam System Performance — A Sourcebook for Industry*, 2nd Edition.
- EU Directive 2012/27/EU, "Energy Efficiency Directive — High Efficiency Cogeneration."
- Tsatsaronis, G. & Morosuk, T. (2012). "Advanced exergy-based methods used to understand and improve energy-conversion systems," *Energy*.
- ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
- Turboden (2022). *ORC Technology Overview — Medium-to-Large Scale Heat Recovery Applications*.
- Siemens Energy (2023). *Industrial Steam Turbine Reference Projects — Turkey*.
- Turkish Sugar Factories Corporation (2020). *Enerji Verimliliği Raporu*.
