---
title: "Buhar Türbini Boyutlandırma ve Seçim Rehberi — Steam Turbine Sizing & Selection Guide"
category: solutions
equipment_type: steam_turbine
keywords: [boyutlandırma, sizing, türbin seçimi, turbine selection, back-pressure, condensing, extraction, kademe sayısı, stage selection, vendor değerlendirme, yatırım maliyeti, CAPEX, exergy bazlı boyutlandırma]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/solutions/efficiency_improvement.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/condensing.md, steam_turbine/equipment/extraction.md, steam_turbine/economics/feasibility.md, steam_turbine/systems/steam_turbine_chp.md, factory/cogeneration.md]
use_when: ["Yeni türbin yatırımı değerlendirilirken", "CHP fizibilite çalışmasında türbin boyutu belirlenirken", "Mevcut türbin değiştirilirken veya yükseltilirken", "PRV yerine türbin ikamesi planlanırken", "Karşı basınçlı vs yoğuşmalı türbin kararı verilirken"]
priority: low
last_updated: 2026-02-02
---
# Buhar Türbini Boyutlandırma ve Seçim Rehberi — Steam Turbine Sizing & Selection Guide

> Son güncelleme: 2026-02-02

## Özet

**Kapsam:** Bu rehber, yeni buhar türbini yatırımı, CHP (Combined Heat and Power) fizibilitesi veya mevcut ekipman yenileme projelerinde türbin tipi seçimi, buhar koşulları optimizasyonu, boyutlandırma hesaplaması, kademe sayısı belirleme, tedarikci degerlendirme ve yatirim maliyeti tahminini kapsar.

**Neden Gerekli:**
- Yeni tesis kurulumunda veya mevcut PRV (Pressure Reducing Valve) yerine türbin ikamesi planlandiginda dogru boyut ve tip secimi kritiktir
- Yanlis boyutlandirma kalici verim kayiplarina, asiri yatirim maliyetine veya yetersiz kapasiteye yol acar
- Exergy perspektifinden boyutlandirma, enerji bazli secime kiyasla %5-15 daha yuksek yasam dongusu tasarrufu saglayabilir

**Hedef Kitle:** Enerji muhendisleri, tesis yoneticileri, proje muhendisleri, CHP fizibilite ekipleri

## 1. Karar Cercevesi — Back-Pressure vs Condensing vs Extraction

### 1.1 Turbin Tipi Secim Karar Agaci

```
                         BUHAR TURBİNİ TİP SEÇİMİ
                         ═════════════════════════
                                    │
                     Proses ısı talebi var mı?
                                    │
                    ┌───────────────┴────────────────┐
                   EVET                             HAYIR
                    │                                 │
        Isı talebi kararlı mı?               ──► YOĞUŞMALİ TÜRBİN
        (yıl boyunca ±%20 içinde)                 (Condensing)
                    │                                 │
            ┌───────┴───────┐                  Maksimum elektrik
           EVET           HAYIR                üretimi hedeflenir
            │               │
      HPR > 3 mü?    Elektrik öncelikli mi?
            │               │
      ┌─────┴─────┐   ┌────┴─────┐
     EVET       HAYIR EVET     HAYIR
      │           │     │        │
  KARŞI       ÇEKİŞLİ  ÇEKİŞLİ  KARŞI
  BASINCI     TÜRBİN   TÜRBİN   BASINCI
  TÜRBİN     (Ext.)   (Ext-    TÜRBİN
  (BP)        +Kond.    Cond.)  (BP)
              opsiyonu          + Tepe
                                 kazanı
```

> **Kritik Kural:** Proses isi talebi kararliysa ve HPR (Heat-to-Power Ratio) > 3 ise, karsi basincli turbin ekonomik olarak en avantajli secimdir. Proses isi talebi degiskense veya elektrik uretimi oncelikliyse cekisli turbin tercih edilmelidir.

### 1.2 Turbin Tipi Karsilastirma Tablosu

| Parametre | Karsi Basincli (BP) | Yogusmal (Condensing) | Cekisli (Extraction) |
|-----------|---------------------|----------------------|----------------------|
| **Elektrik verimi** | %15-25 | %30-42 | %20-35 |
| **Toplam enerji verimi** | %80-92 | %30-42 | %65-85 |
| **Toplam exergy verimi** | %25-38 | %30-44 | %28-42 |
| **HPR** | 3-10 | -- | 1-8 (degisken) |
| **Esneklik** | Dusuk (sabit HPR) | Yuksek (elektrik bazli) | Yuksek (degisken HPR) |
| **Kondenser gereksinimi** | Hayir | Evet | Kismi/Evet |
| **Sogutma suyu ihtiyaci** | Yok | Yuksek | Orta |
| **Yatirim maliyeti (EUR/kW)** | 400-1,200 | 700-1,500 | 600-1,400 |
| **Karmasiklik** | Basit | Orta | Yuksek |
| **Bakim maliyeti** | Dusuk | Orta | Orta-Yuksek |
| **Ideal uygulama** | Kararli proses isi | Salt elektrik | Degisken isi+elektrik |

### 1.3 Sektore Gore Onerilen Turbin Tipi

| Sektor | Onerilen Tip | Gerekce |
|--------|-------------|---------|
| Kagit & seluloz | Extraction | Degisken kurutma ve proses buhari talebi |
| Seker | Back-pressure | Kampanya doneminde kararli proses isi |
| Kimya | Extraction-Condensing | Birden fazla basinc seviyesinde buhar ihtiyaci |
| Gida isleme | Back-pressure | Dusuk/orta basinc proses buhari, kararli talep |
| Rafineri | Extraction | Coklu basinc seviyeleri, yuksek esneklik |
| Cimento | Condensing | Atik isi geri kazanim, proses buhari yok |
| Tekstil | Back-pressure | Kararli dusuk basincli buhar talebi |

## 2. Buhar Kosullari Optimizasyonu (Steam Conditions Optimization)

### 2.1 Giris Basinci Secimi

Giris basinci (inlet pressure), turbin entalpi dusumunu ve dolayisiyla guc ciktisini dogrudan etkiler. Yuksek giris basinci daha fazla guc uretimi saglar ancak kazan ve boru maliyetini artirir.

```
Giris basinci secim kriterleri:
- Mevcut kazan basinci varsa: Mevcut basinc ile calismak en ekonomik
- Yeni kazan kuruluyorsa: Proses+turbin ihtiyacina gore optimize et
- PRV ikamesi: Mevcut HP buhar basinci giris basinci olur

Basinc-guc iliskisi (yaklasik):
P_giris arttikca → Δh artar → W_turbin artar
Ancak: P_giris > 60 bar → kazan ve boru maliyeti onemli olcude artar

Tipik giris basinci araliklari:
- Kucuk endustriyel (<2 MW): 10-25 bar
- Orta endustriyel (2-10 MW): 20-45 bar
- Buyuk endustriyel (10-50 MW): 40-85 bar
- Santral tipi (>50 MW): 85-250 bar
```

### 2.2 Giris Sicakligi Secimi

| Sicaklik Sinifi | Sicaklik [°C] | Avantaj | Dezavantaj | Tipik Uygulama |
|-----------------|---------------|---------|------------|----------------|
| Doymus buhar (saturated) | P'ye bagli | Superheater gereksiz, dusuk maliyet | Cikista yuksek nem, dusuk verim | Cok kucuk turbinler, ORC |
| Hafif kizgin | 250-350 | Orta maliyet, nem kontrolu | Sinirli guc artisi | Kucuk endustriyel |
| Orta kizgin | 350-450 | Iyi guc/maliyet dengesi | Alasimsiz celik siniri (~425°C) | Orta endustriyel |
| Yuksek kizgin | 450-540 | Yuksek guc, dusuk cikis nemi | Krom-molibden celigi gerekli | Buyuk endustriyel/santral |
| Cok yuksek kizgin | 540-600 | Maksimum verim | Ostenitik celik, yuksek maliyet | Buyuk santraller |

> **Pratik Kural:** Giris buhari en az 50°C kizginlik derecesine (superheat) sahip olmalidir. Bu, turbin cikisinda asiri nemliligin onune gecer ve kanat erozyonunu azaltir.

### 2.3 Cikis Kosullari

```
Karsi basincli turbin cikis basinci:
- Proses buhar basincina esittir (tipik 2-15 bar)
- Daha dusuk cikis basinci → daha fazla guc → ancak proses ihtiyacini karsilamali

Yogusmali turbin cikis basinci:
- Kondenser vakumu: 0.05-0.10 bar (tipik)
- Sogutma suyu sicakligi belirler: P_kond ≈ P_sat(T_sogutma + 10-15°C)
- Dusuk vakum → yuksek guc uretimi

Cekisli turbin:
- Cekis noktasi: Proses basinc seviyesinde (ornegin 4-8 bar)
- Exhaust: Kondensere (0.05-0.10 bar) veya dusuk basincli prosese
```

### 2.4 Sektore Gore Tipik Buhar Kosullari

| Sektor | Giris Basinci [bar] | Giris Sicakligi [°C] | Cikis Basinci [bar] | Tipik Guc [MW] |
|--------|--------------------|-----------------------|---------------------|----------------|
| Kagit & seluloz | 40-65 | 420-500 | 3-6 (LP), 10-15 (MP) | 5-30 |
| Seker | 20-40 | 350-420 | 1.5-3 | 2-15 |
| Kimya | 40-85 | 420-520 | 3-8 (cekis), 0.05 (kond.) | 5-50 |
| Gida isleme | 10-25 | 250-350 | 2-5 | 0.5-5 |
| Rafineri | 40-85 | 420-520 | 3-10 (coklu seviye) | 10-80 |
| Cimento (WHR) | 10-30 | 280-400 | 0.05-0.10 | 3-15 |
| Enerji santral | 100-250 | 540-600 | 0.04-0.08 | 50-600+ |

## 3. Boyutlandirma Hesaplamasi (Sizing Calculation)

### 3.1 Boyutlandirma Adimlari

```
Adim 1: Proses isi talebinden buhar debisini belirle
═══════════════════════════════════════════════════
Q_proses = Proses isi talebi [kW]
h_cikis = Turbin cikis entalpisi [kJ/kg]
h_kondensat = Kondensat donuş entalpisi [kJ/kg]

m_buhar = Q_proses / (h_cikis - h_kondensat)  [kg/s]

Adim 2: Kullanilabilir entalpi dusumunu hesapla
═══════════════════════════════════════════════
Δh_is = h_giris - h_cikis,is  [kJ/kg] (izentropik)
Δh_gercek = η_is × Δh_is     [kJ/kg] (gercek)

Burada:
- h_giris: Giris buhari entalpisi (CoolProp veya buhar tablolarindan)
- h_cikis,is: Izentropik cikis entalpisi (s_cikis = s_giris kosulunda)
- η_is: Tahmini izentropik verim (benchmarks.md referans)

Adim 3: Turbin guc ciktisini tahmin et
═══════════════════════════════════════
W_turbin = m_buhar × Δh_gercek  [kW]
W_elek = W_turbin × η_mek × η_jen  [kW]

Burada:
- η_mek = 0.97-0.99 (mekanik verim)
- η_jen = 0.95-0.98 (jenerator verimi)

Adim 4: Kademe sayisini sec (bolum 4'e bakiniz)
═══════════════════════════════════════════════
```

### 3.2 Hesaplama Ornegi — 3 MW Karsi Basincli Turbin (Kagit Fabrikasi)

```
Senaryo: Kagit fabrikasi, proses isi talebi 20 MW_th
         Mevcut kazan: 45 bar, 420°C
         Proses buhar basinci: 4 bar
         Kondensat donusu: 85°C

Adim 1: Buhar debisi
─────────────────────
h_cikis (4 bar, gercek) → daha sonra belirlenecek
h_kondensat (85°C, sivi) = 356 kJ/kg

Once izentropik cikisi hesaplayalim:
h_giris = h(45 bar, 420°C) = 3,272 kJ/kg
s_giris = s(45 bar, 420°C) = 6.840 kJ/(kg·K)

Izentropik cikis (4 bar, s = 6.840):
h_cikis,is = h(4 bar, s = 6.840) = 2,752 kJ/kg

Tahmini η_is = 0.78 (5-10 MW sinifi, benchmarks.md referans)

Gercek cikis entalpisi:
h_cikis = 3,272 - 0.78 × (3,272 - 2,752) = 3,272 - 405.6 = 2,866.4 kJ/kg

Buhar debisi (proses isi talebinden):
m_buhar = 20,000 / (2,866.4 - 356) = 20,000 / 2,510.4 = 7.97 kg/s ≈ 28.7 ton/h

Adim 2: Entalpi dusumu
──────────────────────
Δh_is = 3,272 - 2,752 = 520 kJ/kg
Δh_gercek = 0.78 × 520 = 405.6 kJ/kg

Adim 3: Guc ciktisi
───────────────────
W_turbin = 7.97 × 405.6 = 3,233 kW
W_elek = 3,233 × 0.98 × 0.97 = 3,073 kW ≈ 3.1 MW

Adim 4: Dogrulama
─────────────────
HPR = 20,000 / 3,073 = 6.51 (tipik BP turbin araligi: 3-10 ✓)
SSC = 7.97 × 3,600 / 3,073 = 9.33 kg/kWh (tipik: 8-14 ✓)

Sonuc: ~3 MW karsi basincli turbin, 45 bar/420°C giris, 4 bar cikis
       Buhar debisi: ~29 ton/h
       7-10 kademeli turbin (bolum 4'te detay)
```

### 3.3 PRV Ikamesi Boyutlandirma

```
Mevcut PRV uzerinden gecen buhar:
m_PRV = olculmus debi [kg/s]

Turbin guc potansiyeli:
W_pot = m_PRV × (h_HP - h_LP) × η_is × η_mek × η_jen  [kW]

Ornek:
m_PRV = 5 kg/s, h_HP (25 bar, 350°C) = 3,128 kJ/kg
h_LP,is (4 bar, s = s_HP) = 2,720 kJ/kg
η_is = 0.65 (kucuk turbin), η_mek = 0.98, η_jen = 0.96

W_pot = 5 × (3,128 - 2,720) × 0.65 × 0.98 × 0.96
      = 5 × 408 × 0.65 × 0.9408
      = 1,247 kW ≈ 1.25 MW

Yillik tasarruf: 1,247 × 7,000 × 0.10 = EUR 872,900/yil
```

## 4. Kademe Sayisi Secimi (Stage Selection)

### 4.1 Kademe Tipleri

| Kademe Tipi | Basinc Orani (tek kademe) | Tipik Uygulama | Avantaj | Dezavantaj |
|-------------|--------------------------|----------------|---------|------------|
| Impuls — Curtis (hiz bilesimi) | 2:1 - 8:1 | Ilk kademe, kucuk turbinler | Yuksek basinc dusumu/kademe | Dusuk verim |
| Impuls — Rateau (basinc bilesimi) | 1.2:1 - 2:1 | Cok kademeli HP/IP bolum | Orta verim, iyi kismi yuk | Daha fazla kademe gerekli |
| Reaksiyon (Parsons) | 1.1:1 - 1.5:1 | Buyuk turbin LP bolum | Yuksek verim | Fazla kademe, eksenel itki |

### 4.2 Kademe Sayisi Tahmin Tablosu

| Toplam Basinc Orani (P_giris/P_cikis) | Onerilen Kademe Sayisi | Tipik Konfigürasyon |
|---------------------------------------|----------------------|---------------------|
| 2:1 - 5:1 | 1-3 | Tek kademeli veya Curtis+Rateau |
| 5:1 - 15:1 | 3-8 | Curtis giriş + Rateau kademeleri |
| 15:1 - 50:1 | 6-15 | Curtis + Rateau (HP) + Reaksiyon (LP) |
| 50:1 - 200:1 | 10-25 | Cok kademeli, muhtemelen cift govde |
| >200:1 | 20-40+ | Santral tipi, HP+IP+LP govdeler |

### 4.3 Donme Hizi Secimi

```
Donme hizi secimi:
═════════════════
Dogal senkron hizlar (50 Hz sebekelerde):
- 3,000 rpm: Kucuk-orta turbinler (<15 MW)
  → Daha kompakt, daha ucuz, dogrudan senkron jenerator
- 1,500 rpm: Buyuk turbinler (>15 MW)
  → Daha buyuk kanat yuksekligi, daha iyi LP kademe verimi
- 750 rpm: Cok buyuk santral turbinleri (>200 MW)
  → Nadiren endustriyel uygulamalarda

Reduktor (gearbox) kullanimi:
- Turbin optimal hizi ≠ jenerator senkron hizi ise reduktor gerekli
- Ornek: Tek kademeli turbin 6,000-12,000 rpm → reduktor → jenerator 3,000 rpm
- Reduktor kaybi: %1.5-2.5
- Reduktor maliyeti: EUR 20,000-80,000 (kapasiteye bagli)

Karar kriteri:
- W < 3 MW: Hem 3,000 rpm hem reduktorlu opsiyonlari degerlendir
- W = 3-15 MW: 3,000 rpm dogrudan couplingpreferans
- W > 15 MW: 1,500 rpm tercih edilir
```

### 4.4 Ornek — 3 MW Kagit Fabrikasi Turbini Kademe Secimi

```
Bolum 3.2'deki ornek icin kademe secimi:

Basinc orani: 45 / 4 = 11.25:1
Onerilen kademe: 5-10 (tablodan)

Konfigürasyon secimi:
- 1 adet Curtis giriş kademesi (2-hiz sırali): Basinc dusumu ~3:1
- 6-8 adet Rateau kademesi: Kalan basinc dusumu

Donme hizi: 3,000 rpm (3 MW < 15 MW esigi)
Reduktor: Gereksiz (dogal senkron hiz)

Toplam: 7-9 kademe, tek govde, 3,000 rpm, dogrudan coupling
```

## 5. Hacimsel Akis ve Son Kademe Boyutlandirma

### 5.1 Cikis Hacimsel Akis Hesabi

```
Cikis hacimsel akis (turbin boyutunun anahtar parametresi):
V_cikis = m_buhar × v_cikis  [m³/s]

Burada:
v_cikis = spesifik hacim @ cikis kosullari [m³/kg]

Ornek degerler:
| Cikis Basinci [bar] | v_cikis [m³/kg] | 10 kg/s icin V_cikis [m³/s] |
|---------------------|-----------------|----------------------------|
| 10.0 (BP, yuksek) | 0.20 | 2.0 |
| 4.0 (BP, orta) | 0.46 | 4.6 |
| 1.5 (BP, dusuk) | 1.16 | 11.6 |
| 0.10 (kond., iyi) | 14.7 | 147 |
| 0.05 (kond., cok iyi) | 28.2 | 282 |

Not: Yogusmali turbinlerde cikis hacimsel akis devasa boyutlara ulasir.
Son kademe kanat yuksekligi bu akisi yonetmek icin tasarlanir.
```

### 5.2 Son Kademe Kanat Yuksekligi Tahmini

```
Son kademe annuler alan:
A_annuler = V_cikis / V_axial  [m²]

V_axial = tipik 100-250 m/s (yogusmali), 80-150 m/s (karsi basincli)

Kanat yuksekligi (yaklasik):
L_kanat = A_annuler / (π × D_orta)  [m]

D_orta = orta cap, turbin boyutuna bagli [m]
```

## 6. Vendor Degerlendirme Kriterleri (Vendor Evaluation)

### 6.1 Teknik Kriterler

| Kriter | Agirlik [%] | Degerlendirme Olcutu | Hedef Deger |
|--------|------------|---------------------|-------------|
| Garantili izentropik verim | 25 | η_is [%] @ tasarim noktasi | Benchmark ust ceyrek |
| Turndown orani (minimum yuk) | 10 | Minimum kararli yuk / Nominal yuk | <%30 |
| Kismi yuk verimi | 10 | η_is @ %50 yuk / η_is @ %100 yuk | >%90 |
| Baslatma suresi (startup time) | 5 | Soguk baslatma suresi [dakika] | <60 dk |
| Ilk overhaul araligi | 10 | Saat cinsinden [h] | >40,000 h |
| Referans sayisi (benzer guc) | 5 | Ayni boyut sinifinda referans | >10 referans |
| Buhar tüketimi (SSC) | 10 | kg/kWh @ tam yuk | Benchmark altinda |
| Titresim seviyesi | 5 | mm/s (ISO 10816) | <2.8 mm/s (Zone A) |

### 6.2 Ticari Kriterler

| Kriter | Agirlik [%] | Degerlendirme Olcutu |
|--------|------------|---------------------|
| CAPEX (turbin + jenerator + yardimci) | 30 | EUR toplam |
| Garanti suresi | 10 | Yil (standart: 2 yil) |
| Yedek parca bulunabilirlik suresi | 10 | Hafta cinsinden kritik parcalar |
| Servis anlasmasi secenekleri | 10 | LTSA (Long Term Service Agreement) |
| Teslimat suresi | 15 | Ay cinsinden (siparis → commissioning) |
| Yerel servis / temsilci | 10 | Ulke icinde servis imkani |
| Ödeme kosullari | 15 | Avans orani, taksit yapisi |

### 6.3 Baslica Turbin Uretici ve Ozellikleri

| Uretici | Merkez | Guc Araligi | Guclu Yonler | Dikkat Noktasi |
|---------|--------|------------|--------------|----------------|
| Siemens Energy | Almanya | 0.5-1,900 MW | Genis urun yelpazesi, dijital cozumler | Yuksek CAPEX |
| GE Steam Power | ABD | 5-1,800 MW | Santral deneyimi, servis agi | Buyuk turbinlere odakli |
| MAN Energy Solutions | Almanya | 2-180 MW | Endustriyel CHP uzmanligi | Orta-buyuk segment |
| Dresser-Rand (Siemens) | ABD | 0.5-60 MW | Endustriyel, API standartlari | Siemens'e entegre |
| Shin Nippon Machinery | Japonya | 0.5-50 MW | Maliyet-verim dengesi, Asya pazari | Avrupa servisi sinirli |
| Triveni Turbine | Hindistan | 0.5-30 MW | Rekabetci fiyat, hizli teslimat | Premium segmentte sinirli |
| Turboden (Mitsubishi) | Italya | 0.2-15 MW (ORC) | ORC uzmanligi, dusuk sicaklik | Sadece ORC |
| Elliott (Ebara) | ABD | 0.5-50 MW | API turkiye, mekanik tahrik | Servis agi |

### 6.4 Vendor Degerlendirme Puanlama Matrisi Sablonu

```
Vendor Degerlendirme Matrisi
════════════════════════════════════════════════════════════════
                          Vendor A    Vendor B    Vendor C
Kriter          Agirlik   Puan  Skor  Puan  Skor  Puan  Skor
──────────────  ───────   ────  ────  ────  ────  ────  ────
Garanti η_is     25%       8    2.00   7    1.75   9    2.25
Turndown          10%      7    0.70   8    0.80   6    0.60
Kismi yuk η       10%      7    0.70   7    0.70   8    0.80
Baslatma suresi    5%      6    0.30   8    0.40   7    0.35
Overhaul araligi  10%      8    0.80   7    0.70   8    0.80
Referans           5%      9    0.45   6    0.30   7    0.35
SSC               10%      8    0.80   7    0.70   9    0.90
Titresim           5%      8    0.40   8    0.40   7    0.35
CAPEX             30%      6    1.80   9    2.70   7    2.10
Garanti suresi    10%      7    0.70   6    0.60   8    0.80
Yedek parca       10%      8    0.80   5    0.50   7    0.70
Servis anlasma    10%      8    0.80   6    0.60   7    0.70
Teslimat          15%      6    0.90   8    1.20   7    1.05
Yerel servis      10%      9    0.90   4    0.40   6    0.60
Odeme             15%      7    1.05   8    1.20   7    1.05
──────────────  ───────   ────  ─────  ────  ─────  ────  ─────
TOPLAM (teknik)   100%          6.15        5.75        6.40
TOPLAM (ticari)   100%          6.95        7.20        7.00
BİRLEŞİK (%50/%50)             6.55        6.48        6.70
──────────────────────────────────────────────────────────────
Puanlama: 1 (en dusuk) - 10 (en yuksek)
```

## 7. Yatirim Maliyeti Tahminleri (Investment Cost Estimates)

### 7.1 Turbin + Jenerator CAPEX (2026 Tahmini Degerler)

| Kapasite [MW] | Birim Maliyet [EUR/kW] | Toplam CAPEX [EUR] | Turbin Tipi |
|---------------|------------------------|---------------------|-------------|
| 0.5 | 1,500-2,500 | 750,000-1,250,000 | BP, tek/cift kademe |
| 1.0 | 1,000-1,800 | 1,000,000-1,800,000 | BP/Ext, cok kademe |
| 2.0 | 800-1,400 | 1,600,000-2,800,000 | BP/Ext, cok kademe |
| 5.0 | 600-1,000 | 3,000,000-5,000,000 | BP/Ext/Cond |
| 10.0 | 500-800 | 5,000,000-8,000,000 | BP/Ext/Cond |
| 20.0 | 400-650 | 8,000,000-13,000,000 | Ext/Cond |

> **Not:** Yukaridaki maliyetler turbin + jenerator + kontrol sistemi paketini kapsar. Montaj, insaat, BOP ve devreye alma ayri hesaplanir.

### 7.2 Ek Maliyet Kalemleri

| Maliyet Kalemi | Oran (Turbin CAPEX'e gore) | Aciklama |
|----------------|---------------------------|----------|
| Insaat ve yapi isleri (civil works) | %10-20 | Temel, turbin binasi, ses yalitimi |
| BOP — Dengeleme tesisleri (Balance of Plant) | %15-30 | Borulama, vanalar, kondenser, dearator |
| Elektrik baglantisi (grid connection) | %5-15 | Transformator, sviçgir, koruma |
| Devreye alma (commissioning) | %3-5 | Test, ayar, performans testi |
| Muhendislik ve proje yonetimi | %8-12 | Detay tasarim, proje yonetimi |
| Yedek parca ilk stok | %3-5 | Kritik yedek parcalar |
| Egitim | %1-2 | Operasyon ve bakim egitimi |
| **Toplam Ek Maliyet** | **%45-90** | Turbin CAPEX uzerine |

### 7.3 Birim Maliyet (Spesifik Maliyet) Trendi

```
Spesifik yatirim maliyeti (EUR/kW) vs. kapasite:

EUR/kW
 3000 │ ×
      │   ×
 2500 │     ×
      │
 2000 │       ×
      │
 1500 │         ×
      │           ×
 1000 │             ×─────×
      │                     ×───────×──────
  500 │
      │
    0 └──────────────────────────────────────
      0.5  1   2    5   10   20   50   100 MW

Kural: Her kapasite ikiye katlandiginda birim maliyet ~%15-25 duser
(olcek ekonomisi — economies of scale)
```

### 7.4 Toplam Proje Maliyeti Ornegi

```
Ornek: 5 MW karsi basincli turbin CHP projesi

Turbin + jenerator + kontrol:     EUR 4,000,000  (800 EUR/kW)
Insaat ve yapi isleri (%15):      EUR   600,000
BOP — borulama, kondenser vb (%25): EUR 1,000,000
Elektrik baglantisi (%10):        EUR   400,000
Devreye alma (%4):                EUR   160,000
Muhendislik (%10):                EUR   400,000
Yedek parca (%4):                 EUR   160,000
Egitim (%1):                      EUR    40,000
─────────────────────────────────────────────
Toplam proje maliyeti:            EUR 6,760,000  (1,352 EUR/kW)

Yillik elektrik uretimi: 5,000 × 7,000 = 35,000,000 kWh
Yillik gelir (0.10 EUR/kWh): EUR 3,500,000
Basit geri odeme suresi (SPP): 6,760,000 / 3,500,000 = 1.93 yil
```

## 8. Exergy Perspektifinden Boyutlandirma

### 8.1 Exergy Bazli Secim Ilkeleri

Geleneksel boyutlandirma enerji (1. yasa) bazlidir ve turbin secimini yalnizca enerji verimliligi uzerinden yapar. Exergy (2. yasa) bazli yaklasim ise termodinamik kalitenin en verimli kullanilmasini hedefler.

```
Exergy bazli boyutlandirma prensipleri:

1. BUHAR KOSULLARINI EXERGY YIKIMINI MINIMIZE EDECEK SEKILDE SEC
   ─────────────────────────────────────────────────────────────
   Giris exergisi: ex_giris = (h_giris - h₀) - T₀ × (s_giris - s₀)
   Yuksek basinc ve sicaklik → yuksek exergy → daha fazla is potansiyeli

2. PRV YERINE MUTLAKA TURBIN KULLAN
   ─────────────────────────────────
   PRV exergy yikimi: Ex_yikim,PRV = m × T₀ × (s_cikis - s_giris) [kW]
   Turbin ile ayni basinc dusumu → exergy ise donusur

3. PROSES ISI SICAKLIGINI MINIMUMDA TUT
   ──────────────────────────────────────
   Proses isisi ne kadar dusuk sicaklikta verilebiliyorsa,
   turbin uzerindeki entalpi dusumu o kadar fazla olur.
   Ornek: Proses 120°C yerine 140°C'de ihtiyac duyuyorsa
   → cikis basinci daha yuksek → turbin gucu dusuk
   → Exergy perspektifi: Minimum gerekli sicaklikta proses tasarla!

4. KASKAT BUHAR KULLANIMI
   ──────────────────────
   Yuksek exergyali buhari once turbinden gecir,
   sonra prosese ver. Asla PRV ile basinci dusurme.
```

### 8.2 Exergy Bazli Karsilastirma Ornegi

```
Senaryo: 40 bar, 400°C buhar → 4 bar proses buhari, m = 10 kg/s

Opsiyon A: PRV ile basinc dusurme (turbin yok)
─────────────────────────────────────────────
h_giris = 3,214 kJ/kg, s_giris = 6.769 kJ/(kg·K)
h_cikis,PRV = 3,214 kJ/kg (izentalpik), s_cikis,PRV = 7.586 kJ/(kg·K)

Ex_yikim,PRV = 10 × 298.15 × (7.586 - 6.769) = 2,436 kW
Elektrik uretimi: 0 kW
Proses isisi: 10 × (3,214 - 356) = 28,580 kW

Opsiyon B: Karsi basincli turbin (η_is = 0.78)
─────────────────────────────────────────────
h_cikis = 3,214 - 0.78 × (3,214 - 2,753) = 2,854.4 kJ/kg
s_cikis = 7.06 kJ/(kg·K)

W_turbin = 10 × (3,214 - 2,854.4) = 3,596 kW
Ex_yikim = 10 × 298.15 × (7.06 - 6.769) - 0 = 867 kW
  (Turbin exergy yikimi dahil, ancak 3,596 kW ise donustu!)
Proses isisi: 10 × (2,854.4 - 356) = 24,984 kW

KARSILASTIRMA:
                    PRV         Turbin      Fark
Elektrik [kW]:     0           3,596       +3,596
Ex yikim [kW]:     2,436       867         -1,569
Proses isi [kW]:   28,580      24,984      -3,596

Not: Turbin opsiyonunda proses isisi 3,596 kW daha dusuk cunku
bu enerji elektrik olarak cikti. Ancak eksik proses isisi,
kazandan ek buhar ile karsilanabilir. Net fayda:
→ 3,596 kW elektrik × 0.10 EUR/kWh = EUR 2,517,200/yil (7,000 h)
→ Ek yakıt maliyeti: 3,596 / 0.88 × 0.035 EUR/kWh = ~EUR 1,000,000/yil
→ Net fayda: ~EUR 1,500,000/yil
```

### 8.3 Boyutlandirmada Exergy Optimizasyon Kontrol Listesi

| Kontrol Noktasi | Exergy Etkisi | Aksiyon |
|-----------------|---------------|---------|
| PRV uzerinden gecen buhar akisi var mi? | Her PRV exergy yikir | PRV → turbin ikamesi degerlendir |
| Giris buhar sicakligi yeterli mi? | Dusuk kizginlik → dusuk exergy | En az 50°C superheat sağla |
| Cikis basinci minimum mu? | Yuksek cikis basinci → az is | Proses minimumuna indir |
| Kondenser vakumu optimize mi? | Kotu vakum → guc kaybi | Sogutma sistemi iyilestir |
| Çoklu basinc seviyeleri var mi? | Tek seviye → exergy israfı | Cekisli turbin ile kaskat kullan |
| Feedwater heating var mi? | FWH olmazsa cevrim verimi dusuk | Turbin cekisi ile FWH ekle |
| Turbin izentropik verimi yeterli mi? | Dusuk η_is → yuksek exergy yikim | Uygun kademe sayisi ve boyut sec |

## 9. Boyutlandirma Icin Genel Kontrol Listesi

```
TURBIN BOYUTLANDIRMA KONTROL LISTESI
═════════════════════════════════════
□ Proses isi talebi profili belirlendi (saatlik/mevsimsel)
□ Buhar kosullari (giris P, T; cikis P) belirlendi
□ Buhar debisi hesaplandi
□ Turbin tipi secildi (BP / Condensing / Extraction)
□ Izentropik verim tahmini yapildi (benchmarks referans)
□ Guc ciktisi hesaplandi
□ Kademe sayisi ve tipi secildi
□ Donme hizi belirlendi (3,000 veya 1,500 rpm)
□ Reduktor gereksinimi degerlendiridi
□ Cikis hacimsel akis kontrol edildi (son kademe boyutu)
□ Yardimci ekipman listelendi (pompa, kondenser, dearator)
□ Vendor spesifikasyonu hazirlandi
□ En az 3 tedarikci teklifi alindi
□ Teknik ve ticari degerlendirme yapildi
□ Exergy bazli optimizasyon kontrol edildi
□ Yatirim maliyeti ve SPP hesaplandi
□ Fizibilite raporu onaylandi
```

## İlgili Dosyalar

- Hesaplama formulleri: `steam_turbine/formulas.md` -- Turbin guc, exergy ve CHP formulleri
- Benchmark verileri: `steam_turbine/benchmarks.md` -- Verimlilik karsilastirma tablolari, sektorel benchmark
- Verim iyilestirme: `steam_turbine/solutions/efficiency_improvement.md` -- Mevcut turbin verim iyilestirme cozumleri
- Kondensat optimizasyonu: `steam_turbine/solutions/condensate_optimization.md` -- Kondensat ve besleme suyu
- Yuk eslestirme: `steam_turbine/solutions/load_matching.md` -- Turbin isletme optimizasyonu
- Karsi basincli turbin: `steam_turbine/equipment/back_pressure.md` -- BP turbin detaylari
- Yogusmali turbin: `steam_turbine/equipment/condensing.md` -- Condensing turbin detaylari
- Cekisli turbin: `steam_turbine/equipment/extraction.md` -- Ara cekisli turbin detaylari
- CHP sistemleri: `steam_turbine/systems/steam_turbine_chp.md` -- CHP konfigurasyonlari
- Fizibilite analizi: `steam_turbine/economics/feasibility.md` -- CHP fizibilite degerlendirme cercevesi
- Kojenerasyon: `factory/cogeneration.md` -- CHP temelleri ve karsilastirma
- Fabrika benchmarklari: `factory/factory_benchmarks.md` -- Sektorel karsilastirma
- Ekipmanlar arasi firsatlar: `factory/cross_equipment.md` -- Fabrika seviyesi entegrasyon

## Referanslar

- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Horlock, J.H. (2003). *Advanced Gas Turbine Cycles*, Pergamon Press.
- Horlock, J.H. (1966). *Axial Flow Turbines: Fluid Mechanics and Thermodynamics*, Butterworths.
- Bejan, A. (2016). *Advanced Engineering Thermodynamics*, 4th Edition, Wiley.
- Bejan, A., Tsatsaronis, G. & Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition, McGraw-Hill.
- Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
- API 612 (2005). *Petroleum, Petrochemical and Natural Gas Industries -- Steam Turbines -- Special-Purpose Applications*, API.
- ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
- ASME PTC 6S (1988). *Procedures for Routine Performance Tests of Steam Turbines*, ASME.
- Sanders, W.P. (2001). *Turbine Steam Path Engineering*, PennWell Publishing.
- Leyzerovich, A.S. (2008). *Steam Turbines for Modern Fossil-Fuel Power Plants*, Fairmont Press.
- US DOE (2012). *Improving Steam System Performance -- A Sourcebook for Industry*, 2nd Edition.
- Tsatsaronis, G. & Morosuk, T. (2012). "Advanced exergy-based methods used to understand and improve energy-conversion systems," *Energy*.
- EU Directive 2012/27/EU, "Energy Efficiency Directive -- High Efficiency Cogeneration."
- Baumann, K. (1921). "Some recent developments in large steam turbine practice," *Journal of the Institution of Electrical Engineers*, 59(302).
