---
title: "Kutle Dengesi ve Materyal Akis Analizi (Mass Balance and Material Flow Analysis — MFA)"
category: factory
equipment_type: factory
keywords: [kütle dengesi, malzeme, akış]
related_files: [factory/energy_flow_analysis.md, factory/system_boundaries.md, factory/data_collection.md]
use_when: ["Kütle dengesi hazırlanırken", "Malzeme akışı analiz edilirken"]
priority: low
last_updated: 2026-01-31
---
# Kutle Dengesi ve Materyal Akis Analizi (Mass Balance and Material Flow Analysis — MFA)

> Son güncelleme: 2026-01-31

## Genel Bakis

Kutle dengesi, endustriyel sistemlerdeki tum madde giris ve cikislarinin sistematik olarak izlenmesini saglayan temel bir muhendislik aracidir. Materyal Akis Analizi (MFA), kutle dengesini tum hammadde, ara urun, urun, yan urun, atik ve emisyon akislarini kapsayacak sekilde genisletir. Enerji ve exergy analizi ile birlikte kullanildiginda, fabrikanin kaynak verimliliginin butunsel bir resmini ortaya koyar.

Bu dosya; kutle dengesi prensipleri, MFA metodolojisi, giris-cikis analizi, su dengesi, hammadde takibi, atik akis nicelendirme, materyal verimlilik gostergeleri ve enerji/exergy analizi entegrasyonunu kapsar.

## 1. Kutle Dengesi Temel Prensipleri (Mass Balance Fundamentals)

### 1.1 Kutle Korunumu Yasasi

```
Kararli hal (steady-state) kutle dengesi:

m_dot_giris = m_dot_cikis + dm/dt

Kararli hal icin (dm/dt = 0):
Sigma(m_dot_giris) = Sigma(m_dot_cikis)

Burada:
- m_dot_giris = tum giris kutle akislari [kg/h veya ton/yil]
- m_dot_cikis = tum cikis kutle akislari (urun + atik + emisyon) [kg/h]
- dm/dt = sistem icindeki kutle degisim hizi [kg/h]

Kapanma kriteri:
Hata = |m_giris - m_cikis| / m_giris x 100 [%]
Kabul edilebilir: +-5% (genel), +-2% (hassas proses)
```

### 1.2 Kutle Dengesi Siniflari

| Denge Turu | Kapsam | Kullanim | Zorluk |
|---|---|---|---|
| Toplam kutle dengesi | Tum madde akislari | Genel kontrol | Dusuk |
| Bilesen dengesi | Tek bir kimyasal bilesen | Emisyon/atik takibi | Orta |
| Su dengesi | Yalnizca su akislari | Su yonetimi | Orta |
| Enerji-kutle dengesi | Enerji + kutle birlesik | Proses optimizasyonu | Yuksek |
| Exergy-kutle dengesi | Exergy + kutle birlesik | Termodinamik analiz | Yuksek |

### 1.3 Kutle Dengesi Adimlari

```
Adim 1: Sistem sinirlarini tanimla (bkz. system_boundaries.md)
Adim 2: Tum giris akislarini listele ve olc
        - Hammaddeler, su, hava, yakit, kimyasallar
Adim 3: Tum cikis akislarini listele ve olc
        - Urunler, yan urunler, atiklar, emisyonlar, atik su
Adim 4: Kutle dengesini kur ve kapanmayi kontrol et
Adim 5: Eksik/bilinmeyen akislari hesapla (fark yontemi)
Adim 6: Materyal akis diyagramini ciz
Adim 7: Verimlilik gostergelerini hesapla
```

## 2. MFA Metodolojisi (Material Flow Analysis Methodology)

### 2.1 MFA Genel Cercevesi

```
MFA Seviyeleri:
1. Tesis seviyesi: Fabrika geneli toplam akislar
2. Proses seviyesi: Her uretim asamasi icin ayri denge
3. Bilesen seviyesi: Kritik hammadde/kirletici bazinda
4. Yasam dongusu: Hammadde cikarimindan urun omru sonuna

Endustriyel enerji denetiminde genellikle Seviye 1 ve 2 kullanilir.
```

### 2.2 Giris-Cikis Analizi (Input-Output Analysis)

```
GIRISLER:                              CIKISLAR:
─────────                              ────────
Hammaddeler [ton/yil] ────┐     ┌──── Urunler [ton/yil]
                          │     │
Yardimci malzemeler ──────┤     ├──── Yan urunler [ton/yil]
                          │     │
Su (sebeke + kuyu) ───────┤     ├──── Kati atik [ton/yil]
                          │     │
Yakit (gaz, oil) ─────────┤ FAB ├──── Atik su [m3/yil]
                          │RIKA │
Basingli hava ────────────┤     ├──── Hava emisyonu [ton/yil]
                          │     │       (CO2, NOx, SOx, PM)
Elektrik [kWh/yil] ──────┤     ├──── Isil atik [kW]
                          │     │
Ambalaj malzemesi ────────┘     └──── Ambalaj atigi [ton/yil]
```

### 2.3 Tipik Endustriyel Materyal Akislari

| Sektor | Ana Hammadde | Su Tuketimi [m3/ton urun] | Atik Orani [%] | Ana Atik Turu |
|---|---|---|---|---|
| Tekstil | Iplik, boya, kimyasal | 80-150 | 5-15 | Atik su, curuf |
| Gida (sut) | Sut, seker, katki | 3-8 | 2-8 | Organik, atik su |
| Kagit | Seluloz, kimyasal | 15-40 | 8-20 | Camur, lif atigi |
| Cimento | Klinker, alci, katki | 0.3-0.8 | 1-3 | Toz, baca gazi |
| Metal isleme | Metal, yag, sogutma siv. | 5-20 | 3-10 | Metal talaslari, yag |
| Kimya | Cesitli kimyasallar | 10-50 | 2-15 | Kimyasal atik |
| Otomotiv | Metal, plastik, boya | 4-10 | 3-8 | Boya curugu, metal |

## 3. Su Dengesi (Water Balance)

### 3.1 Su Dengesi Formulu

```
Su dengesi:
V_giris = V_urun + V_atik_su + V_buharlaslma + V_kacak + V_diger

Burada:
- V_giris = toplam su girisi (sebeke + kuyu + yagmur) [m3/yil]
- V_urun = urune gecen su [m3/yil]
- V_atik_su = atik su debi [m3/yil]
- V_buharlaslma = sogutma kulesi + proses buharlasma [m3/yil]
- V_kacak = sistem kacaklari [m3/yil]
- V_diger = temizlik, bahce, insani kullanim [m3/yil]
```

### 3.2 Su Tuketim Dagilimi (Tipik Fabrika)

| Su Kullanim Alani | Tipik Pay [%] | Tasarruf Potansiyeli [%] |
|---|---|---|
| Proses suyu | 40-60 | 10-25 |
| Sogutma suyu (acik cevrim) | 15-30 | 30-50 (kapali cevrim) |
| Kazan besleme suyu | 5-15 | 10-30 (kondensat geri donus) |
| Temizlik/yikama | 5-15 | 20-40 |
| Insani kullanim | 2-5 | 10-20 |
| Bahce/dis alan | 1-5 | 50-80 (yagmur suyu) |

### 3.3 Su Dengesi Ornegi

```
Tekstil fabrikasi su dengesi:

GIRISLER:
- Sebeke suyu: 120,000 m3/yil
- Kuyu suyu: 30,000 m3/yil
- Toplam giris: 150,000 m3/yil

CIKISLAR:
- Proses atik su (aritma): 85,000 m3/yil (%56.7)
- Sogutma kulesi buharlasma: 28,000 m3/yil (%18.7)
- Kazan blowdown: 5,000 m3/yil (%3.3)
- Urune gecen nem: 8,000 m3/yil (%5.3)
- Temizlik/insani atik su: 12,000 m3/yil (%8.0)
- Kacak (hesaplanan): 7,000 m3/yil (%4.7)
- Diger: 5,000 m3/yil (%3.3)
- Toplam cikis: 150,000 m3/yil

Kapanma: 150,000 / 150,000 = %100 ✓

Spesifik su tuketimi:
Uretim = 2,000 ton/yil
SEC_su = 150,000 / 2,000 = 75 m3/ton urun
Sektor ortalamasi: 80-150 m3/ton → Iyi performans
```

## 4. Hammadde Takibi ve Materyal Verimlilik (Raw Material Tracking)

### 4.1 Materyal Verimlilik Gostergeleri

```
1. Materyal verimlilik orani:
   eta_mat = m_urun / m_hammadde x 100 [%]

2. Atik yoğunlugu:
   W_spesifik = m_atik / m_urun [kg atik/ton urun]

3. Geri donusum orani:
   R = m_geri_donusum / m_atik_toplam x 100 [%]

4. Su verimliligi:
   eta_su = V_urun_su / V_giris_su x 100 [%]

5. Enerji-materyal baglanti gostergesi:
   EMR = E_toplam / m_urun [kWh/ton urun]
   (Bu gosterge SEC ile aynidir, bkz. kpi_definitions.md)
```

### 4.2 Materyal Verimlilik Performans Tablosu

| Performans Seviyesi | eta_mat [%] | W_spesifik | R [%] | Aksiyon |
|---|---|---|---|---|
| Mukemmel | >95 | Sektore ozgu en dusuk | >90 | Referans tesis |
| Iyi | 90-95 | Sektore ozgu iyi | 70-90 | Ince ayar |
| Ortalama | 85-90 | Sektor ortalamasi | 50-70 | Sistematik iyilestirme |
| Dusuk | 75-85 | Ortalamanin ustunde | 30-50 | Ciddi program |
| Kritik | <75 | Cok yuksek | <30 | Acil mudahale |

## 5. Atik Akis Nicelendirme (Waste Stream Quantification)

### 5.1 Atik Kategorileri

```
Kati atiklar:
- Uretim artiklari (metal, plastik, kagit kesurleri)
- Proses atiklari (curuf, camur, filtre keki)
- Ambalaj atiklari (karton, plastik, palet)
- Tehlikeli atiklar (yag, kimyasal, boya)

Sivi atiklar:
- Proses atik suyu (organik/inorganik kirleticiler)
- Sogutma suyu purjleri
- Kazan blowdown
- Yikama/temizlik suyu

Gaz emisyonlari:
- Yanma urunleri (CO2, NOx, SOx, CO)
- Proses emisyonlari (VOC, toz, koku)
- Kacak emisyonlar (sogutma gazi, basingli hava)
```

### 5.2 Emisyon Hesaplama

```
CO2 emisyonu (yanma kaynakli):
m_CO2 = m_yakit x EF

Emisyon faktorleri (EF):
- Dogalgaz: 2.02 kgCO2/Nm3 (veya 56.1 kgCO2/GJ)
- Fuel oil: 3.15 kgCO2/kg
- Komur (linyit): 1.8-2.5 kgCO2/kg (ture bagli)
- Elektrik (Turkiye sebekesi): ~0.47 kgCO2/kWh

Toplam karbon ayak izi:
CF = m_CO2_yakit + m_CO2_elektrik + m_CO2_proses [tCO2/yil]

Spesifik karbon yoğunlugu:
CI = CF / m_urun [kgCO2/ton urun]
```

## 6. Enerji/Exergy Analizi ile Entegrasyon

### 6.1 Kutle-Enerji-Exergy Uc Boyutlu Analiz

```
Entegre analiz cercevesi:

1. Kutle dengesi    → Madde akislarinin miktari
2. Enerji dengesi   → Enerji akislarinin miktari (1. yasa)
3. Exergy dengesi   → Enerji kalitesi ve yikim (2. yasa)

Birlesik denge:
Kutle:   Sigma(m_dot_giris) = Sigma(m_dot_cikis)
Enerji:  Sigma(E_giris) = Sigma(E_cikis)
Exergy:  Sigma(Ex_giris) = Sigma(Ex_cikis) + Sigma(I_k)

Her akis icin uc boyutlu tanimlama:
- m_dot [kg/s]: kutle debisi
- h [kJ/kg]: ozgul entalpi → E = m_dot x h
- ex [kJ/kg]: ozgul exergy → Ex = m_dot x ex
```

### 6.2 Entegre Analiz Tablosu Sablonu

| Akis No | Aciklama | m_dot [kg/s] | T [C] | P [kPa] | h [kJ/kg] | s [kJ/kgK] | ex [kJ/kg] | E [kW] | Ex [kW] |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Yakit girisi | — | — | — | LHV | — | phi x LHV | Q_yakit | Ex_yakit |
| 2 | Hava girisi | — | T0 | P0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Besleme suyu | — | T_bes | P_bes | h_bes | s_bes | ex_bes | E_bes | Ex_bes |
| 4 | Buhar cikis | — | T_bhr | P_bhr | h_bhr | s_bhr | ex_bhr | E_bhr | Ex_bhr |
| 5 | Baca gazi | — | T_baca | P0 | h_bg | s_bg | ex_bg | E_bg | Ex_bg |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

### 6.3 Kutle-Exergy Eslestirme Ornegi

```
Kazan sistemi entegre analiz:

Giris akislari:
| Akis        | m_dot [kg/s] | ex [kJ/kg]  | Ex [kW]  |
|-------------|-------------|-------------|----------|
| Dogalgaz    | 0.111       | 35,880      | 3,987    |
| Hava        | 1.94        | 0           | 0        |
| Besleme suyu| 1.39        | 28.8        | 40       |
| TOPLAM      |             |             | 4,027    |

Cikis akislari:
| Akis        | m_dot [kg/s] | ex [kJ/kg]  | Ex [kW]  |
|-------------|-------------|-------------|----------|
| Buhar       | 1.39        | 858         | 1,193    |
| Baca gazi   | 2.05        | 106         | 218      |
| Yuzey kaybi | —           | —           | 9        |
| YIKIM       | —           | —           | 2,607    |
| TOPLAM      |             |             | 4,027    |

Kutle dengesi: 0.111 + 1.94 + 1.39 = 3.44 kg/s ≈ 1.39 + 2.05 = 3.44 kg/s ✓
Exergy dengesi: 4,027 = 1,193 + 218 + 9 + 2,607 = 4,027 kW ✓
```

## 7. Hesaplama Ornegi: Fabrika Kutle Dengesi (Worked Example)

### 7.1 Senaryo

Orta olcekli sut isleme fabrikasi:
- Uretim kapasitesi: 200 ton sut/gun
- Urunler: Pastorize sut, yogurt, peynir
- Calisma: 350 gun/yil, 16 saat/gun

### 7.2 Gunluk Kutle Dengesi

```
GIRISLER (ton/gun):
- Ham sut: 200.0
- Su (proses + temizlik): 150.0
- Katkı maddeleri (maya, kultur, tuz): 2.5
- Ambalaj malzemesi: 5.0
- Dogalgaz: 3.2 (yakit — enerji icin)
- Hava (yanma): ~55.0 (yakit ile orantili)
- Toplam giris: ~415.7 ton/gun

CIKISLAR (ton/gun):
- Pastorize sut: 120.0
- Yogurt: 50.0
- Peynir: 18.0
- Peynir alti suyu: 35.0
- Atik su: 130.0
- Kati atik (ambalaj, organik): 3.5
- Baca gazi (CO2, H2O, N2): ~58.2
- Buharlasma (sogutma kulesi): 1.0
- Toplam cikis: ~415.7 ton/gun

Kapanma: 415.7 / 415.7 ≈ %100 ✓
```

### 7.3 Materyal Verimlilik

```
Hammadde → urun donusum:
eta_sut = (120 + 50 + 18) / 200 = %94 (sut bazli, peynir alti suyu dahil %111.5)
Not: Peynir alti suyu yan urun olarak degerlendirilirse verimlilik artar

Su verimliligi:
V_giris = 150 ton/gun
V_atik_su = 130 ton/gun
V_urune_gecen ≈ 10 ton/gun
V_buharlasma ≈ 1 ton/gun
V_diger ≈ 9 ton/gun
Kapanma: 130 + 10 + 1 + 9 = 150 ✓

Spesifik su tuketimi:
SEC_su = (150 x 350) / (188 x 350/1000) = 52,500 / 65.8 ≈ 798 L/ton urun
Veya: 150 / 188 ≈ 0.80 m3/ton urun (gun bazli)

Sektörel karsilastirma (sut isleme):
Iyi uygulama: 0.6-1.0 m3/ton sut girisi
Bu fabrika: 0.75 m3/ton sut → Iyi performans
```

### 7.4 Atik ve Emisyon Ozeti

```
Yillik atik ozeti:
| Atik Turu          | Miktar [ton/yil] | Yonetim             |
|--------------------|-------------------|---------------------|
| Atik su            | 45,500            | Biyolojik aritma    |
| Peynir alti suyu   | 12,250            | Yan urun satisi     |
| Kati organik atik  | 490               | Kompostlama         |
| Ambalaj atigi      | 735               | Geri donusum        |
| CO2 emisyonu       | 2,300             | (atmosfere)         |

Spesifik CO2 yogunlugu:
Uretim = 65,800 ton/yil
CI = 2,300 / 65.8 = 35 kgCO2/ton urun
Sektor ortalamasi: 50-100 kgCO2/ton → Iyi performans
```

## 8. MFA Raporlama ve Gorsellestime

### 8.1 Materyal Akis Diyagrami (MFD)

```
Materyal akis diyagrami, Sankey diyagramina benzer sekilde
kutle akislarini oransal oklarla gosterir:

HAM SUT (200) ══════════════════════╗
                                     ║
SU (150) ════════════════════════╗   ║
                                  ║   ║
KATKI (2.5) ═══════════════╗     ║   ║
                            ║     ║   ║
         ╔══════════════════╩═════╩═══╣
         ║    SUT ISLEME FABRIKASI     ║
         ╠════════════════════════════╝
         ║
         ║──── Pastorize sut (120) ────→ URUN
         ║──── Yogurt (50) ────────────→ URUN
         ║──── Peynir (18) ────────────→ URUN
         ║──── Peynir alti suyu (35) ──→ YAN URUN
         ║──── Atik su (130) ──────────→ ARITMA
         ║──── Kati atik (3.5) ────────→ GERI DONUSUM
         ║──── Baca gazi (58.2) ───────→ ATMOSFER
         ╚═══════════════════════════════

(Birim: ton/gun, yaklasik degerler)
```

### 8.2 Performans Izleme

```
Aylik izlenmesi gereken MFA gostergeleri:

| Gosterge                 | Birim          | Hedef        | Frekans |
|--------------------------|----------------|--------------|---------|
| Hammadde verimlilik      | %              | >93          | Haftalik|
| Spesifik su tuketimi     | m3/ton urun    | <0.80        | Gunluk  |
| Atik yogunlugu           | kg/ton urun    | <30          | Aylik   |
| Geri donusum orani       | %              | >80          | Aylik   |
| CO2 yogunlugu            | kgCO2/ton urun | <40          | Aylik   |
| Enerji-materyal orani    | kWh/ton urun   | Sektore ozgu | Aylik   |
```

## İlgili Dosyalar

- [Sistem Sinirlari](system_boundaries.md) — Kontrol hacimleri ve olcum noktalari
- [Enerji Akis Analizi](energy_flow_analysis.md) — Enerji dengesi ve Sankey diyagramlari
- [Exergy Akis Analizi](exergy_flow_analysis.md) — Exergy dengesi ve Grassmann diyagramlari
- [KPI Tanimlari](kpi_definitions.md) — SEC, EUI ve diger performans gostergeleri
- [Exergy Temelleri](exergy_fundamentals.md) — Exergy temel kavramlar
- [Enerji Yonetimi](energy_management.md) — ISO 50001 ve enerji izleme
- [Kazan Formulleri](../boiler/formulas.md) — Kazan kutle ve enerji dengeleri
- [Kompressor Formulleri](../compressor/formulas.md) — Basingli hava kutle akislari
- [Chiller Formulleri](../chiller/formulas.md) — Sogutma sistemi akislari

## Referanslar

- Brunner, P.H. & Rechberger, H., "Practical Handbook of Material Flow Analysis," CRC Press, 2nd Edition, 2016
- ISO 14040:2006, "Environmental management — Life cycle assessment — Principles and framework"
- ISO 14044:2006, "Environmental management — Life cycle assessment — Requirements and guidelines"
- EU BREF, "Energy Efficiency," European Commission, 2009
- Baccini, P. & Brunner, P.H., "Metabolism of the Anthroposphere," MIT Press, 2012
- Schmidt, M. (2008), "The Sankey Diagram in Energy and Material Flow Management," Journal of Industrial Ecology, 12(1), 82-94
- Allwood, J.M. et al. (2011), "Material efficiency: A white paper," Resources, Conservation and Recycling, 55(3), 362-381
- European Environment Agency, "Material resources and waste — 2020 update"
