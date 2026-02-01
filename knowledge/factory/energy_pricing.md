---
title: "Enerji Fiyatlandirma ve Tarife Yapilari (Energy Pricing and Tariff Structures)"
category: factory
equipment_type: factory
keywords: [enerji fiyat, tarife, maliyet]
related_files: [factory/economic_analysis.md, factory/life_cycle_cost.md, factory/utility_analysis.md]
use_when: ["Enerji maliyeti analiz edilirken", "Tarife optimizasyonu değerlendirilirken"]
priority: low
last_updated: 2026-01-31
---
# Enerji Fiyatlandirma ve Tarife Yapilari (Energy Pricing and Tariff Structures)

> Son güncelleme: 2026-01-31

## Genel Bakis

Enerji fiyatlandirma yapisi, enerji denetim onerilerinin ekonomik degerlendirilmesinde temel giris parametresidir. Elektrik tarife yapilari (talep ucreti, zaman bazli fiyatlama, pik/pik disi), dogalgaz fiyatlandirmasi, Turkiye enerji piyasasi (EPDK, BOTAS) ve AB enerji fiyatlari, denetim raporlarindaki maliyet-fayda analizlerini dogrudan etkiler. Yanlis veya eksik fiyatlandirma varsayimlari, denetim onerilerinin oncelik siralamasini tamamen degistirebilir.

Bu dosya; elektrik ve dogalgaz tarife yapilarini, Turkiye enerji piyasasi duzenleme cercevesini, AB fiyat karsilastirmalarini, fiyatlandirmanin denetim onerilerine etkisini, talep yonetimi stratejilerini ve reaktif guc cezalarini kapsar.

## 1. Elektrik Tarife Yapilari (Electricity Tariff Structures)

### 1.1 Tarife Bilesenleri

Endustriyel elektrik faturasi genellikle su bilesenlerden olusur:

```
Toplam Fatura = Aktif Enerji Bedeli
              + Talep (Demand) Ucreti
              + Reaktif Enerji Cezasi
              + Dagitim Bedeli
              + Iletim Bedeli
              + Vergiler ve Fonlar

Bilesenlerin tipik paylari (Turkiye endustriyel):
| Bilesen               | Tipik Pay [%] |
|-----------------------|---------------|
| Aktif enerji bedeli   | 55-70         |
| Talep ucreti          | 10-20         |
| Dagitim bedeli        | 8-15          |
| Iletim bedeli         | 2-5           |
| Reaktif ceza          | 0-8           |
| Vergi ve fonlar       | 5-12          |
```

### 1.2 Aktif Enerji Fiyatlandirmasi

```
Tek zamanli tarife:
C_enerji = E_tuketim x p_enerji [EUR/ay]

Burada:
- E_tuketim = aylik aktif enerji tuketimi [kWh]
- p_enerji = birim enerji fiyati [EUR/kWh]

Cok zamanli (ToU — Time of Use) tarife:
C_enerji = E_pik x p_pik + E_gun x p_gun + E_gece x p_gece [EUR/ay]

Burada:
- E_pik = puant donem tuketimi [kWh]
- E_gun = gunduz donem tuketimi [kWh]
- E_gece = gece donem tuketimi [kWh]
- p_pik, p_gun, p_gece = ilgili donem birim fiyatlari [EUR/kWh]
```

### 1.3 Turkiye Zaman Dilimleri (EPDK)

| Donem | Saat Araligi | Aciklama | Fiyat Carpani* |
|---|---|---|---|
| Gece (T1) | 22:00 — 06:00 | Dusuk talep donemi | x0.50 |
| Gunduz (T2) | 06:00 — 17:00 | Normal talep donemi | x1.00 (referans) |
| Puant (T3) | 17:00 — 22:00 | Yuksek talep donemi | x1.50 |

*Carpanlar yaklasik degerlerdir; gercek fiyatlar EPDK tarafindan belirlenir.

### 1.4 Turkiye Endustriyel Elektrik Fiyatlari (2025-2026 yaklasik)

| Tarife Grubu | Tek Zamanli [EUR/kWh] | Gunduz [EUR/kWh] | Puant [EUR/kWh] | Gece [EUR/kWh] |
|---|---|---|---|---|
| Sanayi (OG) | 0.090-0.110 | 0.085-0.100 | 0.130-0.155 | 0.050-0.065 |
| Sanayi (AG) | 0.100-0.125 | 0.095-0.115 | 0.145-0.170 | 0.055-0.075 |
| Serbest tuketici (OG) | 0.075-0.095 | 0.070-0.090 | 0.110-0.140 | 0.040-0.060 |
| OSB | 0.080-0.100 | 0.075-0.095 | 0.115-0.145 | 0.045-0.062 |

```
Not:
- OG: Orta gerilim (1-36 kV)
- AG: Alcak gerilim (<1 kV)
- OSB: Organize Sanayi Bolgesi (ozel tarife)
- Serbest tuketici: Yillik tuketimi >1,400 kWh olan tuketiciler
  (EPDK siniri yillik guncellenir)
- Fiyatlar vergi, fon ve dagitim dahil yaklasik toplam birim maliyettir
- 1 EUR ≈ 35-40 TL (2025-2026 yaklasik)
```

## 2. Talep (Demand) Ucreti (Demand Charges)

### 2.1 Talep Ucreti Hesaplama

```
Talep ucreti:
C_talep = P_demand x p_demand [EUR/ay]

Burada:
- P_demand = fatura donemi icindeki maksimum talep gucu [kW]
  (genellikle 15 dakikalik ortalama en yuksek deger)
- p_demand = birim talep fiyati [EUR/kW/ay]

Turkiye'de talep ucreti:
- OG sanayi: ~3.0-5.0 EUR/kW/ay
- AG sanayi: ~3.5-6.0 EUR/kW/ay
- OSB: ~2.5-4.5 EUR/kW/ay
```

### 2.2 Talep Faktoru ve Yuk Faktoru

```
Talep faktoru (Demand Factor):
DF = P_max / P_kurulu

Burada:
- P_max = olculen maksimum talep [kW]
- P_kurulu = toplam kurulu guc [kW]

Yuk faktoru (Load Factor):
LF = E_ortalama / P_max = (E_tuketim / t) / P_max

Burada:
- E_tuketim = donem enerji tuketimi [kWh]
- t = donem suresi [saat]
- P_max = donem icindeki maksimum talep [kW]

Performans degerlendirmesi:
| Yuk Faktoru | Degerlendirme | Aksiyon |
|-------------|---------------|---------|
| >0.85       | Mukemmel      | Optimal yukleme |
| 0.70-0.85   | Iyi           | Kucuk iyilestirmeler |
| 0.55-0.70   | Ortalama      | Yuk yonetimi gerekli |
| 0.40-0.55   | Dusuk         | Ciddi pik yonetimi |
| <0.40       | Kritik        | Yeniden yapilandirma |
```

### 2.3 Talep Ucreti Azaltma Stratejileri

```
1. Yuk kaydirma (Load Shifting):
   - Pik saatlerden gece saatlerine kaydirma
   - Tasarruf: (p_pik - p_gece) x E_kaydirilan
   - Ornek: 100 kW x 5 saat x (0.14 - 0.05) = 45 EUR/gun

2. Yuk dengeleme (Load Leveling):
   - Esitli anlarda ekipman calistirilmasi
   - Pik talep azaltilmasi → demand charge azalir
   - Ornek: P_max 500'den 400'e → (500-400) x 4.0 = 400 EUR/ay

3. Pik tasima (Peak Shaving):
   - Jenerator veya enerji depolama ile pik anlarini karsilama
   - UPS veya batarya sistemi
   - Ornek: 200 kW pik tasima → 200 x 4.0 = 800 EUR/ay tasarruf

4. Otomasyon ve kontrol:
   - Demand controller (talep sinirlandirici)
   - Siralamali ekipman baslatma (staggered start)
   - Oncelikli yuk atma (load shedding)
```

### 2.4 Talep Ucreti Hesaplama Ornegi

```
Fabrika elektrik profili:
- Kurulu guc: 1,500 kW
- Maksimum talep (olculen): 1,100 kW
- Aylik tuketim: 550,000 kWh
- Calisma: 720 saat/ay (30 gun, 24 saat)

Hesaplamalar:
Talep faktoru: DF = 1,100 / 1,500 = %73.3
Yuk faktoru: LF = (550,000 / 720) / 1,100 = 763.9 / 1,100 = %69.4

Talep ucreti: 1,100 x 4.5 = 4,950 EUR/ay
Enerji bedeli: 550,000 x 0.095 = 52,250 EUR/ay
Toplam: 57,200 EUR/ay

Talep ucretinin payi: 4,950 / 57,200 = %8.7

Yuk dengeleme ile P_max = 850 kW hedef:
Yeni talep ucreti: 850 x 4.5 = 3,825 EUR/ay
Tasarruf: 4,950 - 3,825 = 1,125 EUR/ay = 13,500 EUR/yil
```

## 3. Reaktif Guc ve Guc Faktoru (Reactive Power and Power Factor)

### 3.1 Guc Faktoru Tanimi

```
Guc faktoru:
cos(phi) = P / S = Aktif Guc / Gorunen Guc

Burada:
- P = aktif (gercek) guc [kW]
- Q = reaktif guc [kVAR]
- S = gorunen guc [kVA] = sqrt(P^2 + Q^2)
- cos(phi) = guc faktoru

Endustriyel sistemlerde tipik guc faktorleri:
| Ekipman              | cos(phi)    | Reaktif Tuketim |
|----------------------|-------------|-----------------|
| Asenkron motor (tam yuk) | 0.80-0.90 | Yuksek         |
| Asenkron motor (bos)     | 0.15-0.30 | Cok yuksek     |
| Kaynak makinesi          | 0.40-0.65 | Cok yuksek     |
| Ark firini (EAF)         | 0.70-0.80 | Yuksek         |
| Floresan aydinlatma      | 0.50-0.70 | Orta           |
| LED aydinlatma           | 0.90-0.99 | Dusuk          |
| VSD/frekansi degistirici | 0.95-0.99 | Dusuk          |
```

### 3.2 Turkiye Reaktif Enerji Cezasi (EPDK)

```
EPDK duzenlemesine gore:

Endüktif reaktif enerji cezasi:
- Q_induktif / P > 0.20 (cos phi < 0.98 induktif) ise ceza uygulanir
- Ceza: Fazla reaktif enerji x ceza birim fiyati

Kapasitif reaktif enerji cezasi:
- Q_kapasitif / P > 0.15 (cos phi < 0.989 kapasitif) ise ceza uygulanir
- Gece saatlerinde asiri kompanzasyon sonucu olusabilir

Ceza hesaplama:
C_reaktif = (Q_fazla - Q_sinir) x p_reaktif [EUR/ay]

Burada:
- Q_fazla = olculen reaktif enerji [kVARh]
- Q_sinir = izin verilen sinir [kVARh]
- p_reaktif = reaktif enerji ceza birim fiyati [EUR/kVARh]

Turkiye'de reaktif enerji ceza fiyati:
Endüktif: ~0.03-0.05 EUR/kVARh
Kapasitif: ~0.03-0.05 EUR/kVARh (genellikle ayni)
```

### 3.3 Guc Faktoru Duzeltme (Kompanzasyon)

```
Kompanzasyon kapasitesi hesabi:
Q_komp = P x (tan(phi_1) - tan(phi_2)) [kVAR]

Burada:
- P = aktif guc [kW]
- phi_1 = mevcut guc faktoru acisi
- phi_2 = hedef guc faktoru acisi

Ornek:
P = 800 kW, cos(phi_1) = 0.82, hedef cos(phi_2) = 0.98
tan(phi_1) = 0.698, tan(phi_2) = 0.203
Q_komp = 800 x (0.698 - 0.203) = 396 kVAR

Kompanzasyon yatirimi:
- Sabit kompanzasyon: ~8-12 EUR/kVAR (kurulum dahil)
- Otomatik kompanzasyon: ~15-25 EUR/kVAR (kurulum dahil)
- Harmonik filtreli: ~30-50 EUR/kVAR (kurulum dahil)

Yatirim: 396 x 20 = 7,920 EUR (otomatik)
Yillik tasarruf (reaktif ceza): ~3,000-8,000 EUR/yil
SPP: ~1.0-2.6 yil
```

### 3.4 Guc Faktoru Performans Tablosu

| cos(phi) | Degerlendirme | Ceza Durumu | Aksiyon |
|---|---|---|---|
| >0.98 | Mukemmel | Ceza yok | Mevcut durumu koru |
| 0.95-0.98 | Iyi | Dusuk/yok | Izlemeye devam |
| 0.90-0.95 | Ortalama | Olasi ceza | Kompanzasyon degerlendir |
| 0.80-0.90 | Dusuk | Kesin ceza | Otomatik kompanzasyon kur |
| <0.80 | Kritik | Yuksek ceza | Acil kompanzasyon + neden analizi |

## 4. Dogalgaz Fiyatlandirmasi (Natural Gas Pricing)

### 4.1 Turkiye Dogalgaz Piyasasi

```
Turkiye dogalgaz yapisi:
- BOTAS: Toptan alim ve satim (temel tedarikci)
- EPDK: Duzenleme ve lisanslama
- Dagitim sirketleri: Bolgesel dagitim (IGDAS, ESGAZ, BURSAGAZ vb.)
- Serbest piyasa: Ozel tedarikcilar (buyuk tuketiciler icin)

Dogalgaz fiyat bilesenleri:
C_gaz = V_gaz x (p_gaz + p_dagitim + p_iletim + vergiler)

Burada:
- V_gaz = tuketim hacmi [Nm3]
- p_gaz = dogalgaz birim fiyati [EUR/Nm3]
- p_dagitim = dagitim bedeli [EUR/Nm3]
- p_iletim = iletim bedeli [EUR/Nm3]
```

### 4.2 Turkiye Dogalgaz Fiyatlari (2025-2026 yaklasik)

| Tuketici Grubu | Birim Fiyat [EUR/Nm3] | Birim Fiyat [EUR/kWh_th] | Not |
|---|---|---|---|
| Sanayi (kucuk) | 0.35-0.45 | 0.034-0.044 | <300,000 Nm3/yil |
| Sanayi (orta) | 0.30-0.40 | 0.029-0.039 | 300,000-3,000,000 Nm3/yil |
| Sanayi (buyuk) | 0.25-0.35 | 0.024-0.034 | >3,000,000 Nm3/yil |
| Elektrik uretimi | 0.22-0.30 | 0.021-0.029 | Santral kullanimi |
| Konut | 0.20-0.30 | 0.019-0.029 | Subvansiyonlu |

```
Donusum:
1 Nm3 dogalgaz = 10.33 kWh (LHV bazli)
1 Nm3 dogalgaz = 34.5 MJ (LHV bazli)
1 Nm3 dogalgaz ≈ 0.85 kg (standart kosullarda)

Not: Turkiye'de dogalgaz fiyatlari TL cinsindendir ve doviz
kuruna bagli olarak sik degisir. Yukaridaki EUR degerleri
yaklasik donusumlerdir. Guncel fiyatlar icin BOTAS ve
dagitim sirketi web siteleri kontrol edilmelidir.
```

### 4.3 Dogalgaz Maliyet Hesaplama Ornegi

```
Fabrika dogalgaz maliyeti:
- Tuketim: 500 Nm3/h x 6,000 h/yil = 3,000,000 Nm3/yil
- Birim fiyat: 0.32 EUR/Nm3 (orta sanayi)
- Yillik maliyet: 3,000,000 x 0.32 = 960,000 EUR/yil

Alternatif birim:
- Enerji bazli: 3,000,000 x 10.33 = 30,990,000 kWh_th/yil
- Birim fiyat: 960,000 / 30,990,000 = 0.031 EUR/kWh_th
- MJ bazli: 960,000 / (30,990,000 x 3.6) = 0.0086 EUR/MJ
```

## 5. AB Enerji Fiyatlari Karsilastirmasi (EU Energy Price Comparison)

### 5.1 AB Endustriyel Elektrik Fiyatlari (2025 yaklasik)

| Ulke | Fiyat [EUR/kWh] | Turkiye'ye Gore | Not |
|---|---|---|---|
| Almanya | 0.18-0.25 | x1.8-2.5 | Yuksek (EEG surcharge) |
| Fransa | 0.12-0.16 | x1.2-1.6 | Orta (nukleer avantaj) |
| Italya | 0.18-0.24 | x1.8-2.4 | Yuksek |
| Ispanya | 0.13-0.18 | x1.3-1.8 | Orta-yuksek |
| Polonya | 0.12-0.16 | x1.2-1.6 | Orta |
| Romanya | 0.10-0.14 | x1.0-1.4 | Yakin |
| AB ortalamasi | 0.15-0.20 | x1.5-2.0 | — |
| Turkiye | 0.08-0.11 | x1.0 | Referans |

### 5.2 AB Endustriyel Dogalgaz Fiyatlari (2025 yaklasik)

| Ulke | Fiyat [EUR/kWh_th] | Fiyat [EUR/Nm3] | Turkiye'ye Gore |
|---|---|---|---|
| Almanya | 0.04-0.06 | 0.41-0.62 | x1.2-1.7 |
| Fransa | 0.04-0.05 | 0.41-0.52 | x1.2-1.5 |
| Italya | 0.04-0.06 | 0.41-0.62 | x1.2-1.7 |
| Ispanya | 0.04-0.05 | 0.41-0.52 | x1.2-1.5 |
| Polonya | 0.03-0.05 | 0.31-0.52 | x1.0-1.5 |
| AB ortalamasi | 0.04-0.05 | 0.41-0.52 | x1.2-1.5 |
| Turkiye | 0.03-0.04 | 0.30-0.40 | x1.0 |

### 5.3 Karsilastirma Cikarimi

```
Turkiye enerji fiyatlari AB ortalamasinin altindadir:
- Elektrik: AB ortalamasinin ~%50-60'i
- Dogalgaz: AB ortalamasinin ~%70-80'i

Bu durum su sonuclari dogurur:
1. Enerji verimlilik projelerinin SPP'si Turkiye'de daha uzundur
   (ayni tasarruf, daha dusuk fiyat → daha uzun geri odeme)
2. AB'de ekonomik olan projeler Turkiye'de marjinal olabilir
3. CBAM (Carbon Border Adjustment) ile Turkiye ihracatcilari icin
   karbon maliyeti eklenecek → verimlilik projeleri daha cazip olacak
4. Enerji fiyat artis trendi devam ederse SPP'ler kisalacak
```

## 6. Fiyatlandirmanin Denetim Onerilerine Etkisi (Impact on Audit Recommendations)

### 6.1 Fiyat Duyarliligi

```
Enerji verimlilik projesinin SPP'si fiyata dogrudan baglidir:
SPP = C_yatirim / (E_tasarruf x p_enerji)

p_enerji artarsa → SPP azalir (proje daha cazip)
p_enerji azalirsa → SPP artar (proje daha az cazip)

Duyarlilik:
dSPP/dp = -C_yatirim / (E_tasarruf x p^2)

Ornek:
VSD yatirimi: C = 18,000 EUR, E_tasarruf = 100,000 kWh/yil

| Elektrik Fiyati [EUR/kWh] | Yillik Tasarruf [EUR] | SPP [yil] |
|---------------------------|----------------------|-----------|
| 0.06                      | 6,000                | 3.00      |
| 0.08                      | 8,000                | 2.25      |
| 0.10                      | 10,000               | 1.80      |
| 0.12                      | 12,000               | 1.50      |
| 0.15                      | 15,000               | 1.20      |
| 0.20                      | 20,000               | 0.90      |
```

### 6.2 Elektrik/Gaz Fiyat Orani

```
Elektrik/gaz fiyat orani, teknoloji secimini etkiler:

r_e/g = p_elektrik / p_gaz_termal

Turkiye: r_e/g = 0.095 / 0.031 ≈ 3.1
AB ort.: r_e/g = 0.17 / 0.045 ≈ 3.8

| r_e/g | Etki |
|-------|------|
| <2.5  | Elektrikli isitma (isi pompasi) bazen rekabetci |
| 2.5-3.5 | Isi pompasi COP >3.5 ile rekabetci |
| 3.5-4.5 | Isi pompasi COP >4.5 gerekli |
| >4.5  | Gaz bazli isitma kesinlikle avantajli |

Kojenerasyon (CHP) ekonomisi:
- r_e/g > 3.0 ise CHP genellikle ekonomik
- r_e/g < 2.5 ise CHP marjinal
- Turkiye'de r_e/g ≈ 3.1 → CHP projeleri degerlendirilmeli
```

### 6.3 Zaman Bazli Fiyatlama Etkisi

```
ToU tarifesi varliginda optimizasyon firsatlari:

1. Sogutma enerjisi depolamali (Thermal Energy Storage — TES):
   - Gece buzlu su uret (dusuk fiyat)
   - Gunduz depodan kullan (yuksek fiyat)
   - Tasarruf: Q_sogutma / COP x (p_gun - p_gece) x h_kaydirma

2. Basingli hava depolamali:
   - Gece fazla uretim, gunduz tanktan kullan
   - Kompressor boyutu kucultme + dusuk fiyat

3. Uretim programlama:
   - Enerji yogun prosesleri gece kaydirma
   - Firin, kurutma gibi termal prosesler icin ugun

Ornek (sogutma TES):
Sogutma yuku: 300 kW, 10 saat/gun (gunduz)
Chiller COP: 4.5
Elektrik: 300/4.5 = 66.7 kW
Gunduz fiyati: 0.10 EUR/kWh, Gece fiyati: 0.05 EUR/kWh
Gunduz maliyeti: 66.7 x 10 x 0.10 = 66.7 EUR/gun
TES ile (gece uretim): 66.7 x 10 x 0.05 = 33.3 EUR/gun
Tasarruf: 33.4 EUR/gun x 250 gun = 8,350 EUR/yil
TES yatirim: ~25,000-40,000 EUR
SPP: 3.0-4.8 yil
```

## 7. Talep Yonetimi Stratejileri (Demand Management Strategies)

### 7.1 Talep Tepkisi (Demand Response — DR)

```
Demand Response programlari:
1. Fiyat bazli DR: Yuksek fiyat saatlerinde tuketim azaltma
2. Tesvik bazli DR: Sebeke operatoru talebiyle yuk atma (odullu)
3. Otomatik DR: SCADA/BMS ile otomatik yuk yonetimi

Turkiye'de DR durumu:
- EPIAS (Enerji Piyasalari Isletme A.S.) uzerinden dengeleme piyasasi
- Talep tarafli katilim (TTK) mekanizmasi (gelisimde)
- Buyuk tuketiciler icin dogrudan sebeke anlasmalari
```

### 7.2 Enerji Depolama ve Pik Yonetimi

```
Enerji depolama secenekleri:

| Teknoloji         | Kapasite      | Maliyet [EUR/kWh] | Verim [%] | Omur [yil] |
|-------------------|---------------|-------------------|-----------|------------|
| Li-ion batarya    | 50-5,000 kWh  | 200-400           | 85-95     | 10-15      |
| Buz depolama (TES)| 100-10,000 kWhth | 30-80          | 90-95     | 20-30      |
| Sicak su deposu   | 50-5,000 kWhth| 10-30             | 80-90     | 20-30      |
| Basingli hava tank| 10-500 kWh    | 50-150            | 85-90     | 20-30      |

Pik tasima (peak shaving) ornegi:
Fabrika: P_max = 1,200 kW, P_ortalama = 800 kW
Batarya: 200 kW / 400 kWh → 2 saat pik tasima
Yeni P_max: 1,000 kW
Talep ucreti tasarrufu: (1,200-1,000) x 4.5 x 12 = 10,800 EUR/yil
Batarya maliyeti: ~120,000 EUR
SPP: 11.1 yil → Sadece talep ucreti icin ekonomik degil
     Ancak ToU arbitraj + pik tasima kombinasyonu ile 5-7 yil mumkun
```

## 8. Hesaplama Ornegi: Fabrika Enerji Maliyet Analizi (Worked Example)

### 8.1 Senaryo

Orta olcekli metal isleme fabrikasi:
- Elektrik: 1,500 kW ortalama yuk, 2,200 kW pik talep
- Dogalgaz: 300 Nm3/h (isitma firini + kazan)
- Calisma: 5,500 saat/yil (3 vardiya, 230 gun)
- Guc faktoru: cos(phi) = 0.84
- Tarife: Cok zamanli (ToU), orta gerilim

### 8.2 Elektrik Maliyet Hesabi

```
Tuketim dagilimi (tahmini):
| Donem   | Saat    | Oran [%] | Tuketim [kWh/yil] | Fiyat [EUR/kWh] | Maliyet [EUR] |
|---------|---------|----------|--------------------|-----------------|--------------
| Gece    | 8 h/gun | 33       | 2,722,500          | 0.055           | 149,738       |
| Gunduz  | 11 h/gun| 46       | 3,795,000          | 0.090           | 341,550       |
| Puant   | 5 h/gun | 21       | 1,732,500          | 0.140           | 242,550       |
| TOPLAM  |         | 100      | 8,250,000          | ort: 0.089      | 733,838       |

Talep ucreti:
C_talep = 2,200 x 4.5 x 12 = 118,800 EUR/yil

Reaktif enerji cezasi:
Q_reaktif = P x tan(phi) = 1,500 x tan(acos(0.84)) = 1,500 x 0.646 = 970 kVAR
Q_sinir = P x 0.20 = 1,500 x 0.20 = 300 kVAR (EPDK siniri)
Q_fazla = 970 - 300 = 670 kVAR
Ceza (yaklasik): 670 x 5,500 x 0.04 = 147,400 kVARh x 0.04 ≈ 5,896 EUR/yil
Not: Gercek ceza hesabi aylik bazda ve olculen kVARh degerlerine goredir.

Toplam elektrik maliyeti:
C_elektrik = 733,838 + 118,800 + 5,896 = 858,534 EUR/yil
```

### 8.3 Dogalgaz Maliyet Hesabi

```
Dogalgaz tuketimi:
V_gaz = 300 x 5,500 = 1,650,000 Nm3/yil
Birim fiyat: 0.35 EUR/Nm3 (kucuk-orta sanayi)
C_gaz = 1,650,000 x 0.35 = 577,500 EUR/yil
```

### 8.4 Toplam Enerji Maliyet Ozeti

```
| Kalem              | Maliyet [EUR/yil] | Pay [%] |
|--------------------|-------------------|---------|
| Elektrik - enerji  | 733,838           | 51.1    |
| Elektrik - talep   | 118,800           | 8.3     |
| Elektrik - reaktif | 5,896             | 0.4     |
| Dogalgaz           | 577,500           | 40.2    |
| TOPLAM             | 1,436,034         | 100.0   |

Spesifik enerji maliyeti:
Uretim: 12,000 ton/yil
C_spesifik = 1,436,034 / 12,000 = 119.7 EUR/ton urun

Enerji maliyetinin urun maliyetindeki payi:
Ortalama urun fiyati: ~2,500 EUR/ton (yaklasik)
Enerji/urun = 119.7 / 2,500 = %4.8
(Metal isleme sektoru icin tipik aralik: %3-8)
```

### 8.5 Tasarruf Firsatlari (Fiyat Bazli)

```
| Oneri                          | Yillik Tasarruf [EUR] | SPP [yil] | Notlar                    |
|-------------------------------|----------------------|-----------|---------------------------|
| Guc faktoru duzeltme (0.98)   | 5,896                | 1.5       | Otomatik kompanzasyon     |
| Yuk dengeleme (P_max→1,800)   | 21,600               | 0.5       | Siralamali baslatma       |
| Gece kaydirma (%10 puantten)  | 14,700               | 0         | Operasyonel degisiklik    |
| Economizer (dogalgaz %5)      | 28,875               | 2.5       | Firin baca gazi geri kaz. |
| VSD (pompalar, 120 kW)        | 18,000               | 1.8       | %25 enerji tasarrufu      |
| Kompressor optimizasyonu      | 22,000               | 2.0       | VSD + kacak onarimi       |
| LED aydinlatma                | 8,500                | 2.5       | %50 enerji tasarrufu      |
| TOPLAM                        | 119,571              | —         | Toplam maliyetin %8.3'u   |
```

## 9. Enerji Fiyat Projeksiyonlari ve Risk

### 9.1 Fiyat Projeksiyonu

```
Enerji fiyat projeksiyonu (Turkiye, reel bazda):

| Donem      | Elektrik [EUR/kWh] | Degisim | Dogalgaz [EUR/Nm3] | Degisim |
|------------|--------------------|---------|--------------------|---------|
| 2025 (baz) | 0.095              | —       | 0.35               | —       |
| 2026       | 0.100              | +%5     | 0.37               | +%6     |
| 2027       | 0.108              | +%8     | 0.40               | +%8     |
| 2028       | 0.115              | +%7     | 0.42               | +%5     |
| 2030       | 0.130              | +%13*   | 0.48               | +%14*   |

*Kumulatif artis (2028-2030)

Etkileyen faktorler:
1. Kuresel enerji fiyatlari (petrol, LNG)
2. TL/EUR kuru
3. EPDK duzenleme kararlari
4. Yenilenebilir enerji payinin artmasi (dusurme etkisi)
5. CBAM ve karbon fiyatlamasi (artirma etkisi)
6. Turkiye ETS (Emisyon Ticaret Sistemi, planlamada)
```

### 9.2 Karbon Fiyatlamasi Etkisi

```
AB CBAM (Carbon Border Adjustment Mechanism):
- 2026'dan itibaren kademeli yururluk
- Celik, cimento, aluminyum, gubre, elektrik, hidrojen
- Turkiye ihracatcilari icin ek karbon maliyeti

Ornek etki hesabi:
Metal isleme fabrikasi:
- CO2 emisyonu: 4,500 tCO2/yil
- AB karbon fiyati: ~80-100 EUR/tCO2 (2025-2026)
- Potansiyel ek maliyet: 4,500 x 90 = 405,000 EUR/yil

Bu ek maliyet, enerji verimlilik projelerinin ekonomik
cazibesini onemli olcude artiracaktir:
- Her 1% verimlilik → ~4,050 EUR/yil karbon maliyeti azalma
- Toplam %10 verimlilik → 40,500 EUR/yil ek tasarruf
```

## İlgili Dosyalar

- [Ekonomik Analiz](economic_analysis.md) — NPV, IRR, SPP yatirim degerlendirme
- [Enerji Akis Analizi](energy_flow_analysis.md) — Enerji dengesi ve maliyet dagilimi
- [Exergy Akis Analizi](exergy_flow_analysis.md) — Exergy bazli onceliklendirme
- [KPI Tanimlari](kpi_definitions.md) — SEC, EUI gostergeleri
- [Enerji Yonetimi](energy_management.md) — ISO 50001 ve enerji izleme
- [Kutle Dengesi](mass_balance.md) — Materyal akis ve emisyon hesaplari
- [Kazan Denetimi](../boiler/audit.md) — Kazan enerji maliyet analizi
- [Kompressor Denetimi](../compressor/audit.md) — Basingli hava maliyet analizi
- [Chiller Denetimi](../chiller/audit.md) — Sogutma sistemi maliyet analizi
- [Pompa Denetimi](../pump/audit.md) — Pompa sistemi maliyet analizi

## Referanslar

- EPDK (Enerji Piyasasi Duzenleme Kurumu), "Elektrik Piyasasi Tarife Yonetmeligi"
- EPDK, "Dogalgaz Piyasasi Tarife Yonetmeligi"
- BOTAS, "Dogalgaz Toptan Satis Fiyat Tarifesi," 2025
- European Commission, "Quarterly Report on European Electricity Markets," 2025
- Eurostat, "Electricity prices for non-household consumers," 2025
- IEA (International Energy Agency), "World Energy Outlook 2025"
- Turkish Ministry of Energy, "National Energy Efficiency Action Plan (NEEAP)"
- EU Regulation 2023/956, "Carbon Border Adjustment Mechanism (CBAM)"
- ASHRAE, "Procedures for Commercial Building Energy Audits," 2nd Edition, 2011
- Turner, W.C. & Doty, S., "Energy Management Handbook," 9th Edition, Fairmont Press, 2013
- Thumann, A. & Younger, W., "Handbook of Energy Audits," 9th Edition, Fairmont Press, 2012
