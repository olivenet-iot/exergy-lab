---
title: "Kurutma Exergy Hesaplamalari (Industrial Dryer Exergy Calculations)"
category: reference
equipment_type: dryer
keywords: [exergy, kurutma, dryer, termodinamik, hesaplama, SMER, SEC, psikrometri, buharlaşma, nemli hava, entropi üretimi, exergy dengesi, kurutma hızı, kurutma eğrisi]
related_files: [dryer/benchmarks.md, dryer/psychrometrics.md, dryer/audit.md, dryer/equipment/belt_dryer.md, dryer/equipment/tunnel_dryer.md, dryer/equipment/spray_dryer.md, dryer/equipment/rotary_dryer.md, dryer/equipment/fluidized_bed.md, dryer/equipment/heat_pump_dryer.md, dryer/equipment/drum_dryer.md, dryer/equipment/infrared_dryer.md, dryer/solutions/exhaust_heat_recovery.md, dryer/solutions/air_recirculation.md, dryer/solutions/heat_pump_retrofit.md, dryer/solutions/insulation.md, dryer/solutions/temperature_optimization.md, dryer/solutions/mechanical_dewatering.md, dryer/solutions/solar_preheating.md, factory/cross_equipment.md]
use_when: ["Kurutma firini exergy hesaplamasi yapilirken", "Kurutma verimliligi formullerine ihtiyac duyuldugunda", "SMER veya SEC hesaplamasi gerektiginde", "Nemli hava exergy hesabi yapilirken", "Kurutma prosesi entropi uretimi analiz edilirken"]
priority: high
last_updated: 2026-02-01
---
# Kurutma Exergy Hesaplamalari (Industrial Dryer Exergy Calculations)

> Son guncelleme: 2026-02-01

## Genel Bakis (Overview)

Endustriyel kurutma, en enerji-yogun birim islemlerden biridir ve toplam endustriyel
enerji tuketiminin %10-25'ini olusturabilir. Kurutma prosesi dogasi geregi exergy-yikici
(exergy-destructive) bir islemdir: faydali urun nem uzaklastirmadir (moisture removal),
ancak enerji girdisi (sicak hava, buhar vb.) buharlasimanin gercekte gerektirdiginden
cok daha yuksek exergy icerir. Bu nedenle konvektif kurutucularda exergy verimi tipik
olarak %5-15 gibi cok dusuk seviyelerdedir. Isi pompali kurutucularda bu deger %15-30
araligina yukselebilir.

Exergy analizi, enerji analizinin gosteremedigi kayip kaynaklarini ve iyilestirme
potansiyellerini ortaya koyar. Kurutucularda enerji (birinci yasa) verimi %35-65
arasindayken, exergy (ikinci yasa) verimi yalnizca %5-30 arasindadir. Bu buyuk fark,
yuksek sicaklikli enerji kaynaginin (>150 C) dusuk sicaklikli bir isleme (~60-100 C
buharlasma) kullanilmasinin yarattigi termodinamik kalite kaybindan kaynaklanir.

Bu dokuman, endustriyel kurutucularin tam exergy analizini yapabilmek icin gereken
tum formulleri, tablolari ve ornek hesaplamalari icerir.

---

## 1. Kurutma Exergy Dengesi (Drying Exergy Balance)

### 1.1 Genel Exergy Dengesi

Acik sistem kararli hal (steady-state) exergy dengesi:

```
Ex_in = Ex_out + Ex_destroyed + Ex_loss

Burada:
- Ex_in      = toplam exergy girisi [kW]
- Ex_out     = faydali exergy cikisi [kW]
- Ex_destroyed = ic tersinmezliklerden yikilan exergy [kW]
- Ex_loss    = cevreye kaybolan exergy (egzoz, yuzey kaybi vb.) [kW]
```

### 1.2 Kurutucu Exergy Dengesi Bilesenleri

Konvektif bir kurutucu icin detayli exergy dengesi:

```
GIRIS TARAFINDA:
  Ex_hot_air   = sicak havanin exergy'si [kW]
  Ex_wet_prod  = giren nemli urunun exergy'si [kW]
  Ex_fan       = fan mekanik gucu (elektrik) [kW]
  Ex_aux       = yardimci ekipman gucu [kW]

CIKIS TARAFINDA:
  Ex_exhaust   = egzoz havasinin exergy'si [kW]
  Ex_dry_prod  = cikan kuru urunun exergy'si [kW]

EXERGY YIKIMI:
  I_heating    = isitma tersinmezligi [kW]
  I_drying     = kurutma prosesi (kutle transferi) tersinmezligi [kW]
  I_mixing     = karisim tersinmezligi [kW]
  I_fan        = fan tersinmezligi [kW]

EXERGY KAYBI:
  Ex_shell     = govde yuzey kaybi [kW]

Denge:
(Ex_hot_air + Ex_wet_prod + Ex_fan + Ex_aux)
  = (Ex_exhaust + Ex_dry_prod) + (I_heating + I_drying + I_mixing + I_fan) + Ex_shell
```

### 1.3 Isitici Sisteme Gore Exergy Girisi

**Dogal gaz brulor ile isitma:**
```
Ex_fuel = m_fuel x ex_ch [kW]

Burada:
- m_fuel = yakit kutle debisi [kg/s]
- ex_ch  = yakitin spesifik kimyasal exergy'si [kJ/kg]
- Dogal gaz: ex_ch = 51,850 kJ/kg, phi = ex_ch / LHV = 1.04
```

**Sicak hava Carnot yaklasimiyla (brulor sonrasi):**
```
Ex_hot_air = Q_heater x (1 - T_0 / T_supply) [kW]

Burada:
- Q_heater = isitici isi gucu [kW]
- T_0      = olum durumu sicakligi = 298.15 K (25 C)
- T_supply = kurutucu giris hava sicakligi [K]
```

**Elektrikli isitma:**
```
Ex_elec = W_electric [kW]
```
Elektrik saf exergy'dir (%100 exergy icerigi).

**Buhar serpantin isitmasi:**
```
Ex_steam = m_steam x [(h_in - h_out) - T_0 x (s_in - s_out)] [kW]

Burada:
- m_steam    = buhar kutle debisi [kg/s]
- h_in, s_in = giren buharin entalpi ve entropisi
- h_out, s_out = cikan kondensatin entalpi ve entropisi
```

### 1.4 Toplam Exergy Girisi

```
Ex_total_in = Ex_heat_source + Ex_fan + Ex_aux [kW]

Burada:
- Ex_heat_source = isitici kaynagin exergy'si (brulor, buhar, elektrik) [kW]
- Ex_fan         = fan elektrik gucu [kW]
- Ex_aux         = yardimci ekipman gucu (konveyor, rotasyon vb.) [kW]
```

---

## 2. Exergy Verimi Tanimlari (Exergy Efficiency Definitions)

### 2.1 Fonksiyonel (Rational) Exergy Verimi

Kurutma prosesinin asil amaci olan nem uzaklastirmanin exergy'sini temel alir:

```
eta_ex_func = Ex_evaporation / Ex_total_in x 100 [%]

Burada:
- Ex_evaporation = buharlasma exergy'si (faydali cikti) [kW]
- Ex_total_in    = toplam exergy girisi [kW]
```

### 2.2 Evrensel (Universal) Exergy Verimi

Tum cikis exergy'lerini toplam girise oranlar:

```
eta_ex_univ = (Ex_exhaust + Ex_dry_prod) / (Ex_hot_air + Ex_wet_prod + Ex_fan + Ex_aux) x 100 [%]

Burada:
- Pay:   tum cikis akimlarinin exergy'leri toplami
- Payda: tum giris akimlarinin exergy'leri toplami
```

**Not:** Evrensel verim her zaman fonksiyonel verimden yuksektir, cunku egzoz
havasi exergy'si de "cikis" olarak sayilir. Ancak fonksiyonel verim, sistemin
gercek amacina ne kadar iyi hizmet ettigini daha dogru yansitir.

### 2.3 Iyilestirme Potansiyeli (Van Gool)

```
IP = (1 - eta_ex_func) x (Ex_total_in - Ex_evaporation) [kW]

Burada:
- IP = iyilestirme potansiyeli [kW]
```

IP degeri yuksek olan bilesenlere oncelikli mudahale edilmelidir.

### 2.4 Kurutucu Tipine Gore Exergy Verimi Karsilastirmasi

| Kurutucu Tipi | eta_ex_func [%] | eta_ex_univ [%] | Aciklama |
|---------------|----------------|-----------------|----------|
| Konvektif tunel/bant | 5 - 15 | 25 - 45 | Yuksek egzoz exergy kaybi |
| Doner kurutucu (rotary) | 8 - 18 | 30 - 50 | Daha iyi temas ama hala dusuk |
| Akiskan yatak (fluidized bed) | 10 - 20 | 35 - 55 | Iyi isi/kutle transferi |
| Sprey kurutucu (spray) | 5 - 15 | 20 - 40 | Yuksek hava hacmi, yuksek kayip |
| Silindir kurutucu (drum) | 12 - 25 | 40 - 60 | Iletimli, az egzoz |
| Infrared kurutucu | 10 - 22 | 35 - 55 | Dogrudan radyasyon, az hava |
| Isi pompali kurutucu (heat pump) | 15 - 30 | 50 - 70 | COP ile exergy kazanci |
| Kizgin buhar (superheated steam) | 20 - 40 | 55 - 75 | En yuksek, buhar geri kazanimi |

---

## 3. SMER - Spesifik Nem Cikarma Orani (Specific Moisture Extraction Rate)

### 3.1 Temel SMER Formulu

SMER, kurutma verimliligininin en pratik gostergesidir:

```
SMER = m_w / E_input [kg/kWh]

Burada:
- m_w     = buharlaistirilan su miktari [kg/h]
- E_input = toplam enerji tuketimi [kWh/h] = toplam guc [kW]
```

### 3.2 Buharlaistirilan Su Hesabi

Yasbaz (wet basis) nem orani ile:
```
m_w = m_in - m_out [kg/h]

m_out = m_in x (1 - X_in) / (1 - X_out) [kg/h]

Burada:
- m_in   = giren malzeme debisi [kg/h]
- m_out  = cikan malzeme debisi [kg/h]
- X_in   = giren nem orani (yasbaz) [-]
- X_out  = cikan nem orani (yasbaz) [-]
```

Kurubaz (dry basis) nem orani ile:
```
W_in  = X_in / (1 - X_in)  [kg su / kg kuru kati]
W_out = X_out / (1 - X_out) [kg su / kg kuru kati]

m_dry_solid = m_in x (1 - X_in) [kg/h]

m_w = m_dry_solid x (W_in - W_out) [kg/h]
```

### 3.3 Kurutucu Tipine Gore Tipik SMER Degerleri

| Kurutucu Tipi | SMER [kg/kWh] | Aciklama |
|---------------|---------------|----------|
| Tunel kurutucu (tunnel dryer) | 0.5 - 1.0 | Dusuk verimlilik, yaygin |
| Bant kurutucu (belt dryer) | 0.6 - 1.2 | Orta verim |
| Doner kurutucu (rotary dryer) | 0.8 - 1.5 | Iyi temas, orta-iyi verim |
| Akiskan yatak (fluidized bed) | 0.8 - 1.5 | Iyi isi transferi |
| Sprey kurutucu (spray dryer) | 0.5 - 1.0 | Cok ince damlacik, yuksek egzoz kaybi |
| Silindir kurutucu (drum dryer) | 1.0 - 1.8 | Iletimli, daha verimli |
| Infrared kurutucu | 0.8 - 1.5 | Dogrudan radyasyon |
| Isi pompali kurutucu (heat pump) | 2.0 - 5.0 | En verimli, COP avantaji |
| Kizgin buhar kurutucu (SSD) | 1.5 - 3.0 | Geri kazanim dahili |

### 3.4 SMER Performans Siniflandirmasi

| SMER [kg/kWh] | Performans Sinifi | Aksiyon |
|----------------|-------------------|---------|
| < 0.3 | Cok kotu | Acil mudahale gerekli |
| 0.3 - 0.5 | Kotu | Kapsamli iyilestirme |
| 0.5 - 1.0 | Ortalama | Standart konvektif icin tipik |
| 1.0 - 1.5 | Iyi | Optimize konvektif veya iletimli |
| 1.5 - 3.0 | Cok iyi | Gelismis sistem, SSD veya HP |
| > 3.0 | Mukemmel | Isi pompali, tam optimize |

---

## 4. SEC - Spesifik Enerji Tuketimi (Specific Energy Consumption)

### 4.1 Temel SEC Formulu

SEC, birim su buharlaistirmak icin gereken enerjidir:

```
SEC = E_input / m_w [kJ/kg su]

Burada:
- E_input = toplam enerji tuketimi [kJ/h veya kW x 3600]
- m_w     = buharlaistirilan su miktari [kg/h]

Birim donusumu: SEC [kJ/kg] = 3,600 / SMER [kg/kWh]
```

### 4.2 Teorik Minimum SEC

Serbest suyun buharlaistirma enerjisi SEC icin alt sinir olusturur:

```
SEC_min = h_fg [kJ/kg su]

Burada:
- h_fg = buharlasmma gizli isisi (latent heat of evaporation)
- 100 C'de: h_fg = 2,257 kJ/kg
-  80 C'de: h_fg = 2,309 kJ/kg
-  60 C'de: h_fg = 2,358 kJ/kg
-  40 C'de: h_fg = 2,406 kJ/kg
```

### 4.3 SEC Oran Indeksi (SEC Ratio)

```
SEC_ratio = SEC_actual / SEC_min [-]

Burada:
- SEC_ratio = 1.0: ideal (pratik olarak ulasilamaz)
- SEC_ratio < 1.5: cok iyi (isi pompali sistemlerde mumkun)
- SEC_ratio = 2.0 - 4.0: tipik konvektif kurutucu
- SEC_ratio > 5.0: kotu performans
```

### 4.4 Kurutucu Tipine Gore Tipik SEC Degerleri

| Kurutucu Tipi | SEC [kJ/kg su] | SEC_ratio | Aciklama |
|---------------|----------------|-----------|----------|
| Tunel kurutucu | 3,600 - 7,200 | 1.6 - 3.2 | Yaygin, orta performans |
| Bant kurutucu | 3,000 - 6,000 | 1.3 - 2.7 | Cok kademeli mumkun |
| Doner kurutucu | 2,400 - 4,500 | 1.1 - 2.0 | Iyi temas |
| Akiskan yatak | 2,400 - 4,500 | 1.1 - 2.0 | Iyi isi transferi |
| Sprey kurutucu | 3,600 - 7,200 | 1.6 - 3.2 | Yuksek hava orani |
| Silindir kurutucu | 2,000 - 3,600 | 0.9 - 1.6 | Iletimli isi transferi |
| Isi pompali | 720 - 1,800 | 0.3 - 0.8 | COP > 1 avantaji |
| Kizgin buhar (SSD) | 1,200 - 2,400 | 0.5 - 1.1 | Buhar geri kazanimi |

---

## 5. Nemli Hava Exergy'si (Moist Air Exergy)

### 5.1 Nemli Havanin Toplam Spesifik Exergy'si

Nemli havanin exergy'si termal ve kimyasal bilesenden olusur:

```
ex_moist_air = ex_thermal + ex_chemical [kJ/kg kuru hava]
```

### 5.2 Termal Exergy Bileseni

```
ex_thermal = (Cp_a + omega x Cp_v) x [(T - T_0) - T_0 x ln(T / T_0)]
           + (1 + 1.608 x omega) x R_a x T_0 x ln(P / P_0) [kJ/kg kuru hava]

Burada:
- Cp_a  = kuru havanin ozel isisi = 1.005 kJ/kg.K
- Cp_v  = su buharinin ozel isisi = 1.872 kJ/kg.K
- omega = nem orani [kg su / kg kuru hava]
- T     = hava sicakligi [K]
- T_0   = olum durumu sicakligi = 298.15 K (25 C)
- R_a   = kuru hava gaz sabiti = 0.287 kJ/kg.K
- P     = toplam basinc [kPa]
- P_0   = olum durumu basinci = 101.325 kPa
- 1.608 = M_a / M_v = 28.97 / 18.015 (molekul agirligi orani)
```

### 5.3 Kimyasal Exergy Bileseni

Nemli havanin kimyasal exergy'si, ortam nem oranindan farkli nem oranina sahip
olmasindan kaynaklanir:

```
ex_chemical = R_a x T_0 x [(1 + 1.608 x omega) x ln((1 + 1.608 x omega_0) / (1 + 1.608 x omega))
            + 1.608 x omega x ln(omega / omega_0)] [kJ/kg kuru hava]

Burada:
- omega_0 = olum durumu (ortam) nem orani [kg su / kg kuru hava]
- omega   = nemli havanin nem orani [kg su / kg kuru hava]
```

### 5.4 Toplam Nemli Hava Exergy Formulu (Birlesiik)

```
ex_ma = (Cp_a + omega x Cp_v) x [(T - T_0) - T_0 x ln(T / T_0)]
      + (1 + 1.608 x omega) x R_a x T_0 x ln(P / P_0)
      + R_a x T_0 x [(1 + 1.608 x omega) x ln((1 + 1.608 x omega_0) / (1 + 1.608 x omega))
        + 1.608 x omega x ln(omega / omega_0)]  [kJ/kg kuru hava]
```

### 5.5 Cesitli Hava Durumlarinda Exergy Degerleri

T_0 = 25 C, P_0 = 101.325 kPa, omega_0 = 0.010 kg/kg, m_air = 1 kg/s kuru hava icin:

| Durum | T [C] | omega [kg/kg] | ex_thermal [kJ/kg] | ex_chemical [kJ/kg] | ex_total [kJ/kg] |
|-------|-------|---------------|-------------------|--------------------|-----------------:|
| Ortam | 25 | 0.010 | 0.0 | 0.0 | 0.0 |
| Isitilmis | 80 | 0.010 | 6.5 | 0.0 | 6.5 |
| Isitilmis | 120 | 0.010 | 19.8 | 0.0 | 19.8 |
| Isitilmis | 150 | 0.010 | 33.8 | 0.0 | 33.8 |
| Isitilmis | 200 | 0.010 | 60.9 | 0.0 | 60.9 |
| Egzoz | 60 | 0.050 | 2.3 | 8.7 | 11.0 |
| Egzoz | 70 | 0.070 | 4.2 | 14.1 | 18.3 |
| Egzoz | 80 | 0.100 | 6.5 | 22.9 | 29.4 |
| Egzoz | 90 | 0.130 | 9.5 | 32.1 | 41.6 |
| Egzoz | 100 | 0.170 | 13.0 | 44.7 | 57.7 |

**Onemli Gozlem:** Egzoz havasinda kimyasal exergy bileseni (nem farkindan kaynaklanan)
genellikle termal bilesenden daha buyuktur. Bu, kurutucu exergy analizinde nemli hava
kimyasal exergy'sinin ihmal edilmemesi gerektigini gosterir.

---

## 6. Egzoz Exergy Kaybi (Exhaust Air Exergy Loss)

### 6.1 Toplam Egzoz Exergy Kaybi

```
Ex_exhaust = m_air x ex_ma_exhaust [kW]

Burada:
- m_air         = kuru hava kutle debisi [kg/s]
- ex_ma_exhaust = egzoz havasinin spesifik exergy'si [kJ/kg kuru hava]
                  (Bolum 5.4 formuluyle hesaplanir)
```

### 6.2 Egzoz Exergy'sinin Bilesenleri (Ayri Hesap)

**Kuru hava termal bileseni:**
```
Ex_exh_dry = m_air x Cp_a x [(T_ex - T_0) - T_0 x ln(T_ex / T_0)] [kW]
```

**Nem termal bileseni:**
```
Ex_exh_vapor = m_air x omega_ex x Cp_v x [(T_ex - T_0) - T_0 x ln(T_ex / T_0)] [kW]
```

**Kimyasal (konsantrasyon) bileseni:**
```
Ex_exh_chem = m_air x R_a x T_0 x [(1 + 1.608 x omega_ex) x ln((1 + 1.608 x omega_0) / (1 + 1.608 x omega_ex))
            + 1.608 x omega_ex x ln(omega_ex / omega_0)] [kW]
```

**Toplam:**
```
Ex_exhaust = Ex_exh_dry + Ex_exh_vapor + Ex_exh_chem [kW]
```

### 6.3 Egzoz Sicakligina Gore Termal Exergy Kaybi

T_0 = 25 C, m_air = 1 kg/s kuru hava, omega_ex = 0.010 (yalnizca termal bilesen):

| T_exhaust [C] | T_exhaust [K] | Carnot | ex_dry [kJ/kg] | Kayip sinifi |
|---------------|--------------|--------|----------------|-------------|
| 40 | 313.15 | 0.048 | 0.7 | Cok iyi |
| 50 | 323.15 | 0.077 | 2.9 | Cok iyi |
| 60 | 333.15 | 0.104 | 6.5 | Iyi |
| 70 | 343.15 | 0.130 | 11.5 | Ortalama |
| 80 | 353.15 | 0.155 | 17.8 | Yuksek |
| 90 | 363.15 | 0.179 | 25.2 | Yuksek |
| 100 | 373.15 | 0.201 | 33.8 | Cok yuksek |
| 120 | 393.15 | 0.242 | 54.7 | Asiri |
| 150 | 423.15 | 0.295 | 93.6 | Asiri |

**Not:** Kurutucu egzoz sicakligi genellikle 50-100 C arasindadir.
80 C'nin uzerindeki egzoz sicakliklari isi geri kazanimi ile degerlendirilmelidir.

### 6.4 Geri Kazanilabilir Egzoz Exergy'si

```
Ex_recoverable = Ex_exhaust x eta_hx x f_approach [kW]

Burada:
- eta_hx     = isi degistirici verimi (tipik 0.60 - 0.80)
- f_approach = yaklasma sicakligi faktoru (tipik 0.70 - 0.90)
```

Yillik egzoz geri kazanim tasarrufu:
```
Tasarruf_yillik = Ex_recoverable x calisma_saati x enerji_fiyati [EUR/yil]
```

---

## 7. Isi Transferi Tersinmezligi (Heat Transfer Irreversibility)

### 7.1 Genel Entropi Uretimi Formulu

Sonlu sicaklik farkiyla isi transferinde entropi uretimi:

```
S_gen_HT = Q_dot x (1/T_cold - 1/T_hot) [kW/K]

I_HT = T_0 x S_gen_HT [kW]

Burada:
- Q_dot  = isi transfer hizi [kW]
- T_hot  = sicak akiskan sicakligi [K]
- T_cold = soguk akiskan (malzeme/hava) sicakligi [K]
- I_HT   = isi transferi tersinmezligi (exergy yikimi) [kW]
- T_0    = olum durumu sicakligi [K]
```

### 7.2 Kurutucuda Isitma Tersinmezligi

**Brulor/isitici ile hava isitma:**

Havanin T_amb'dan T_supply'a isitilmasindaki entropi uretimi:
```
S_gen_heating = m_air x Cp_a x ln(T_supply / T_amb) - Q_heater / T_source [kW/K]

I_heating = T_0 x S_gen_heating [kW]

Burada:
- T_source = isi kaynagi sicakligi [K]
  - Brulor alev sicakligi: ~2,000-2,200 K (dogal gaz)
  - Buhar serpantin: T_sat (buhar sicakligi)
  - Elektrik: T ~ sonsuz (Carnot = 1)
```

### 7.3 Kurutma Odasinda Entropi Uretimi

Hava-malzeme etkilesiminde (isi + kutle transferi birlikte):
```
S_gen_drying = m_air x (s_ex - s_in) + m_prod_out x s_prod_out - m_prod_in x s_prod_in
             + m_w x s_vapor_out [kW/K]

I_drying = T_0 x S_gen_drying [kW]
```

### 7.4 Sicaklik Farkinin Tersinmezlige Etkisi

Isitici-hava sicaklik farki arttikca tersinmezlik artar:

| T_source [C] | T_supply [C] | delta_T [C] | I_HT / Q [%] | Aciklama |
|-------------|-------------|------------|--------------|----------|
| 200 | 150 | 50 | 2.5 | Dusuk tersinmezlik |
| 500 | 150 | 350 | 15.2 | Orta tersinmezlik |
| 1,000 | 150 | 850 | 22.8 | Yuksek tersinmezlik |
| 2,000 | 150 | 1,850 | 27.1 | Brulor alevi, cok yuksek |

**Sonuc:** Dusuk sicaklikli kurutma prosesi icin yuksek sicaklikli alev kullanmak,
buyuk tersinmezlik yaratir. Bu nedenle isi pompali veya atik isi kaynakli kurutma
termodinamik acidin cok daha uygundur.

### 7.5 Bejan Sayisi (Bejan Number)

Isi transferi ve akiskan suriinme tersinmezliklerinin oranini gosterir:
```
Be = S_gen_HT / (S_gen_HT + S_gen_friction) [-]

Burada:
- Be = 1: tersinmezligin tamami isi transferinden
- Be = 0: tersinmezligin tamami suriinmeden
- Kurutucularda tipik Be = 0.85 - 0.95 (isi transferi baskindur)
```

---

## 8. Radyasyon ve Iletim Kayiplari (Surface Radiation and Conduction Losses)

### 8.1 Kurutucu Govdesi Toplam Isi Kaybi

```
Q_shell = Q_convection + Q_radiation [kW]

Q_convection = h_conv x A_surface x (T_surface - T_amb) [kW]
Q_radiation  = epsilon x sigma x A_surface x (T_surface^4 - T_amb^4) [kW]

Burada:
- h_conv    = dogal konveksiyon katsayisi = 5 - 10 W/m2.K (ic mekan, dusuk hava hizi)
- A_surface = kurutucu dis yuzey alani [m2]
- T_surface = dis yuzey sicakligi [K]
- T_amb     = ortam sicakligi [K]
- epsilon   = yuzey yayinliligi (emisivite) [-]
  - Cilali metal: 0.05 - 0.10
  - Boyali celik: 0.85 - 0.95
  - Yalitim kaplama: 0.20 - 0.50
- sigma     = Stefan-Boltzmann sabiti = 5.67 x 10^-8 W/m2.K4
```

Birlesiik (pratik) yaklasim:
```
Q_shell = h_combined x A_surface x (T_surface - T_amb) [kW]

h_combined ≈ 10 - 15 W/m2.K (dogal konveksiyon + radyasyon birlesiik)
```

### 8.2 Govde Kaybi Exergy'si

```
Ex_shell = Q_shell x (1 - T_0 / T_surface) [kW]
```

**Not:** Govde yuzey sicakligi, ic sicakliktan dusuk oldugundan, govde kaybi
exergy'si nispeten dusuktur. Ancak enerji kaybi olarak onemli olabilir.

### 8.3 Yalitim Kalinliginin Etkisi

Yalitimli duvar icin isi kaybi (duz duvar modeli):
```
Q_shell_insulated = (T_inside - T_amb) / R_total x A [W]

R_total = 1/h_i + t_wall/k_wall + t_ins/k_ins + 1/h_o [m2.K/W]

Burada:
- h_i    = ic isi transfer katsayisi ≈ 20-50 W/m2.K
- t_wall = duvar kalinligi [m]
- k_wall = duvar iletkenlik katsayisi [W/m.K] (celik: 50 W/m.K)
- t_ins  = yalitim kalinligi [m]
- k_ins  = yalitim iletkenlik katsayisi [W/m.K]
  - Cam yunu (glass wool): k = 0.035 - 0.045 W/m.K
  - Tas yunu (rock wool): k = 0.035 - 0.040 W/m.K
  - Kalsiyum silikat: k = 0.060 - 0.080 W/m.K
- h_o    = dis isi transfer katsayisi ≈ 10 - 15 W/m2.K
```

### 8.4 Tipik Govde Kayiplari

| Kurutucu Tipi | Govde Kaybi / Q_input [%] | Aciklama |
|---------------|--------------------------|----------|
| Tunel kurutucu (iyi yalitim) | 3 - 8 | Buyuk yuzey alani |
| Doner kurutucu | 5 - 12 | Donen yuzey, yalitim zor |
| Sprey kurutucu | 3 - 7 | Buyuk hacim, kucuk yuzey/hacim orani |
| Bant kurutucu | 4 - 10 | Orta yuzey alani |
| Akiskan yatak | 3 - 6 | Kompakt tasarim |
| Silindir kurutucu | 2 - 5 | Kucuk yuzey alani |

### 8.5 Optimum Yalitim Kalinligi (Ekonomik)

```
t_opt = sqrt(k_ins x Q_shell x C_energy x H / (C_ins x r)) [m]

Burada:
- C_energy = enerji birim maliyeti [EUR/kWh]
- H        = yillik calisma suresi [saat/yil]
- C_ins    = yalitim birim maliyeti [EUR/m3]
- r        = iskonto orani [-]
```

---

## 9. Mekanik Exergy Girdisi (Fan Power Exergy Input)

### 9.1 Fan Guc Hesabi

```
W_fan = (m_air x delta_P) / (rho_air x eta_fan) [kW]

Burada:
- m_air    = hava kutle debisi [kg/s]
- delta_P  = fan basinc farki [Pa]
- rho_air  = hava yogunlugu [kg/m3] (T ve P'ye bagli)
- eta_fan  = fan toplam verimi [-] (tipik 0.60 - 0.85)
```

### 9.2 Fan Exergy Analizi

Fan elektrik girdisi saf exergy'dir:
```
Ex_fan = W_fan_electric [kW]
```

Fan tersinmezligi:
```
I_fan = W_fan_electric - (Ex_air_out - Ex_air_in) [kW]

eta_ex_fan = (Ex_air_out - Ex_air_in) / W_fan_electric x 100 [%]

Burada:
- Ex_air_out = fan cikisindaki hava exergy'si [kW]
- Ex_air_in  = fan girisindeki hava exergy'si [kW]
- Tipik eta_ex_fan = %55-80
```

### 9.3 Fan Gucunun Toplam Enerji Icerisindeki Payi

| Kurutucu Tipi | W_fan / E_total [%] | Aciklama |
|---------------|-------------------:|----------|
| Tunel / bant kurutucu | 3 - 8 | Dusuk basinc dususu |
| Sprey kurutucu | 5 - 12 | Yuksek hava hacmi |
| Akiskan yatak | 8 - 15 | Yuksek basinc dususu (yatak) |
| Doner kurutucu | 3 - 7 | Orta hava debisi |

### 9.4 VSD (Degisken Hizli Surucu) ile Tasarruf

```
W_fan_VSD = W_fan_nominal x (n/n_nominal)^3 [kW] (affinity law)

Tasarruf = W_fan_nominal - W_fan_VSD [kW]

Burada:
- n         = gercek fan hizi [rpm]
- n_nominal = nominal fan hizi [rpm]
```

---

## 10. Kurutma Hizi ve Kurutma Egrisi (Drying Rate and Drying Curve)

### 10.1 Kurutma Hizi Tanimi

```
R_drying = -m_dry x (dW/dt) [kg su / s]

Burada:
- m_dry = kuru kati kutlesi [kg]
- W     = kurubaz nem orani [kg su / kg kuru kati]
- t     = zaman [s]
```

### 10.2 Sabit Kurutma Hizi Donemi (Constant Rate Period)

Yuzey nemi serbestce buharlaistigi donem (W > W_critical):
```
R_constant = h_c x A / h_fg x (T_air - T_wb) [kg/s]

Burada:
- h_c   = konvektif isi transfer katsayisi [W/m2.K]
- A     = kurutma yuzey alani [m2]
- h_fg  = buharlasmma gizli isisi [kJ/kg]
- T_air = hava sicakligi [C veya K]
- T_wb  = yas termometre (wet-bulb) sicakligi [C veya K]
```

Bu donemde malzeme sicakligi yaklasik olarak yas termometre sicakliginda kalir.

### 10.3 Azalan Kurutma Hizi Donemi (Falling Rate Period)

Ic nem difuzyonunun sinirladigi donem (W < W_critical):
```
R_falling = R_constant x (W - W_eq) / (W_cr - W_eq) [kg/s]

Burada:
- W_eq = denge nem orani (equilibrium moisture content) [kg/kg]
- W_cr = kritik nem orani (critical moisture content) [kg/kg]
```

### 10.4 Kritik Nem Orani

Kurutma hizinin sabitten azalana gecis noktasi:

| Malzeme Tipi | W_cr [kg su/kg kuru kati] | Aciklama |
|-------------|--------------------------|----------|
| Tahillar (grains) | 0.25 - 0.35 | Orta gozenkli |
| Sebze/meyve | 1.0 - 3.0 | Yuksek gozenkli |
| Seramik | 0.10 - 0.20 | Dusuk gozenkli |
| Kagit/karton | 0.50 - 0.80 | Lifli yapi |
| Tekstil | 0.30 - 0.60 | Malzemeye bagli |
| Ahsap | 0.25 - 0.40 | Tur ve kesime bagli |

### 10.5 Kurutma Suresi Tahmini

Sabit hiz donemi:
```
t_constant = m_dry x (W_in - W_cr) / R_constant [s]
```

Azalan hiz donemi:
```
t_falling = m_dry x (W_cr - W_eq) / R_constant x ln[(W_cr - W_eq) / (W_out - W_eq)] [s]
```

Toplam:
```
t_total = t_constant + t_falling [s]
```

### 10.6 Kurutma Egrisi ve Exergy Iliskisi

- Sabit hiz doneminde: exergy verimi nispeten yuksektir (etkin buharlasmma)
- Azalan hiz doneminde: exergy verimi duser (ic difuzyon siniri, hava isisi
  yeterince kullanilmadan egzozdan cikar)
- Optimum kurutma: sabit hiz donemini uzatmak (hava hizi, sicaklik optimizasyonu)

---

## 11. Psikrometrik Hesaplamalar (Psychrometric Calculations)

### 11.1 Nem Orani (Humidity Ratio)

```
omega = 0.622 x P_v / (P_total - P_v) [kg su / kg kuru hava]

Burada:
- P_v     = su buhari kismi basinci [kPa]
- P_total = toplam basinc = 101.325 kPa (deniz seviyesi)
- 0.622   = M_v / M_a = 18.015 / 28.97
```

Bagli nem (relative humidity) ile:
```
P_v = phi x P_sat(T) [kPa]

Burada:
- phi    = bagli nem orani (0-1 arasi) [-]
- P_sat  = doyma basinci [kPa] (sicakliga bagli)
```

### 11.2 Doyma Basinci (Antoine Denklemi)

```
ln(P_sat) = A - B / (C + T) [kPa, C]

A = 16.262, B = 3799.89, C = 226.35 (su icin, 0-200 C arasi)
```

Veya Magnus formulu (pratik, 0-100 C):
```
P_sat = 0.6108 x exp(17.27 x T / (T + 237.3)) [kPa, C]
```

### 11.3 Nemli Havanin Entalpisi

```
h_ma = Cp_a x T + omega x (h_fg_0 + Cp_v x T) [kJ/kg kuru hava]

Burada:
- Cp_a   = 1.005 kJ/kg.K
- Cp_v   = 1.872 kJ/kg.K
- h_fg_0 = 0 C'deki buharlasmma gizli isisi = 2,501 kJ/kg
- T      = hava sicakligi [C]
```

### 11.4 Yas Termometre (Wet-Bulb) Sicakligi

Yas termometre sicakligi, psikrometrik cetvelden veya iteratif cozumle bulunur:

```
h_ma(T_db, omega) = h_ma(T_wb, omega_sat(T_wb))

Yani:
Cp_a x T_db + omega x (2501 + 1.872 x T_db)
  = Cp_a x T_wb + omega_sat(T_wb) x (2501 + 1.872 x T_wb)

Burada:
- T_db = kuru termometre sicakligi [C]
- T_wb = yas termometre sicakligi [C]
- omega_sat(T_wb) = T_wb'deki doyma nem orani [kg/kg]
```

### 11.5 Ciy Noktasi Sicakligi (Dew Point)

```
T_dp = (237.3 x ln(P_v / 0.6108)) / (17.27 - ln(P_v / 0.6108)) [C]

Burada:
- P_v = omega x P_total / (0.622 + omega) [kPa]
```

### 11.6 Tipik Kurutma Prosesi Psikrometrik Degisimi

```
Nokta 1 (Ortam):           T_1 = 25 C,  phi_1 = %60,  omega_1 = 0.012 kg/kg
Nokta 2 (Isitma sonrasi):  T_2 = 150 C, phi_2 < %1,   omega_2 = 0.012 kg/kg
Nokta 3 (Egzoz):           T_3 = 80 C,  phi_3 ≈ %50,  omega_3 = 0.080-0.150 kg/kg

Isitma (1->2): Sensible isitma, omega sabit
Kurutma (2->3): Adyabatik yakinlasim, entalpinin buyuk kismi buharl. icin kullanilir
```

---

## 12. Enerji Verimi vs Exergy Verimi Karsilastirmasi

### 12.1 Enerji Verimi (Birinci Yasa)

```
eta_energy = (m_w x h_fg) / Q_input x 100 [%]

Burada:
- m_w     = buharlaistirilan su kutle debisi [kg/s]
- h_fg    = buharlasmma gizli isisi ≈ 2,257 kJ/kg (100 C'de)
- Q_input = toplam isi girdisi [kW]
```

### 12.2 Exergy Verimi (Ikinci Yasa)

```
eta_exergy = Ex_evaporation / Ex_total_input x 100 [%]

Burada:
- Ex_evaporation = m_w x [h_fg - T_0 x (h_fg / T_evap)] [kW]
- Ex_total_input = isitici exergy + fan gucu + yardimci guc [kW]
```

### 12.3 Iki Verim Arasindaki Iliski

```
eta_exergy / eta_energy = (1 - T_0 / T_evap) / (1 - T_0 / T_source)

Burada:
- T_evap   = buharlasmma sicakligi [K]
- T_source = isi kaynagi sicakligi [K]
```

Bu oran her zaman 1'den kucuktur cunku T_evap < T_source.

### 12.4 Neden Bu Kadar Buyuk Fark Var?

Buharlasmma exergy'si, buharlasmma enerjisinin cok kucuk bir kismidir:

| T_evap [C] | T_evap [K] | h_fg [kJ/kg] | ex_evap [kJ/kg] | ex/h_fg [%] |
|------------|-----------|-------------|----------------|-------------|
| 40 | 313.15 | 2,406 | 115 | 4.8 |
| 50 | 323.15 | 2,382 | 183 | 7.7 |
| 60 | 333.15 | 2,358 | 247 | 10.5 |
| 70 | 343.15 | 2,334 | 307 | 13.2 |
| 80 | 353.15 | 2,309 | 360 | 15.6 |
| 90 | 363.15 | 2,283 | 409 | 17.9 |
| 100 | 373.15 | 2,257 | 454 | 20.1 |

**Kritik Gozlem:** 60 C'de buharlasmma exergy'si yalnizca 247 kJ/kg iken gizli isi
2,358 kJ/kg'dir. Yani buharlasmma enerjisinin yalnizca %10.5'i is uretme kapasitesine
sahiptir. Kurutma prosesinin inherent olarak exergy-destructive olmasinin temel nedeni
budur.

### 12.5 Karsilastirma Tablosu

| Kurutucu Tipi | eta_energy [%] | eta_exergy [%] | Oran | Anlami |
|---------------|---------------|---------------|------|--------|
| Konvektif tunel | 35 - 50 | 5 - 12 | 5-7x | Buyuk termodinamik kalite kaybi |
| Bant kurutucu | 40 - 55 | 7 - 15 | 4-5x | Orta kalite kaybi |
| Doner kurutucu | 45 - 60 | 8 - 18 | 4-5x | Iyi malzeme temasi |
| Akiskan yatak | 50 - 65 | 10 - 20 | 4-5x | Iyi isi/kutle transferi |
| Sprey kurutucu | 40 - 55 | 5 - 15 | 5-7x | Yuksek hava/urun orani |
| Isi pompali | 60 - 80 | 15 - 30 | 3-4x | COP > 1 avantaji |
| Kizgin buhar (SSD) | 70 - 90 | 20 - 40 | 2-3x | Buhar geri kazanimi |

**Yorum:** Enerji verimi %50 gibi "kabul edilebilir" gorinen bir kurutucu, exergy
acisindan yalnizca %10 verimli olabilir. Bu, iyilestirme potansiyelinin enerji
analizinin onerdigi degerden cok daha buyuk oldugunu gosterir.

---

## 13. Ornek Hesaplama: Konvektif Bant Kurutucu (Worked Example)

### 13.1 Senaryo Tanimi

Bir gida isletmesinde konvektif bant kurutucu ile urun kurutulmaktadir.

**Girdiler:**
- Urun: Gida urunuu (sebze/meyve)
- Urun debisi (giren): m_in = 500 kg/h (yasbaz)
- Giren nem orani: X_in = %60 (yasbaz, wet basis)
- Cikan nem orani: X_out = %10 (yasbaz, wet basis)
- Kurutucu giris hava sicakligi: T_supply = 150 C = 423.15 K
- Egzoz hava sicakligi: T_exhaust = 80 C = 353.15 K
- Isitma: Dogal gaz brulor (Q_heater = 300 kW)
- Brulor verimi: eta_burner = 0.90
- Fan gucu: W_fan = 18 kW
- Yardimci ekipman (konveyor vb.): W_aux = 5 kW
- Kuru hava debisi: m_air = 4,500 kg/h = 1.25 kg/s
- Ortam sicakligi: T_0 = 25 C = 298.15 K
- Ortam bagli nemi: phi_0 = %60 --> omega_0 = 0.012 kg/kg
- Egzoz nem orani: omega_ex = 0.090 kg/kg (olculmus)
- Kurutucu dis yuzey alani: A_surface = 35 m2
- Dis yuzey sicakligi: T_surface = 55 C = 328.15 K
- Calisma suresi: 4,000 saat/yil
- Dogal gaz fiyati: 0.05 EUR/kWh

---

### 13.2 Adim 1 - Buharlaistirilan Su Miktari

```
Kuru kati kutlesi:
m_dry_solid = m_in x (1 - X_in) = 500 x (1 - 0.60) = 200 kg/h

Cikan urun kutlesi:
m_out = m_dry_solid / (1 - X_out) = 200 / (1 - 0.10) = 222.2 kg/h

Buharlaistirilan su:
m_w = m_in - m_out = 500 - 222.2 = 277.8 kg/h = 0.0772 kg/s
```

Kurubaz nem oranlari:
```
W_in  = X_in / (1 - X_in)   = 0.60 / 0.40 = 1.50 kg su/kg kuru kati
W_out = X_out / (1 - X_out) = 0.10 / 0.90 = 0.111 kg su/kg kuru kati

Kontrol: m_w = m_dry_solid x (W_in - W_out)
            = 200 x (1.50 - 0.111)
            = 200 x 1.389
            = 277.8 kg/h  (uyumlu)
```

---

### 13.3 Adim 2 - SMER ve SEC Hesabi

```
E_total = Q_heater + W_fan + W_aux = 300 + 18 + 5 = 323 kW

SMER = m_w [kg/h] / E_total [kW]
     = 277.8 / 323
     = 0.860 kg/kWh  --> "Ortalama" sinifi

SEC = E_total x 3600 / m_w [kJ/kg su]
    = 323 x 3600 / 277.8
    = 4,186 kJ/kg su

SEC_ratio = SEC / h_fg = 4,186 / 2,309 = 1.81  (h_fg @ 80 C)
```

---

### 13.4 Adim 3 - Enerji Verimi

```
Q_evap = m_w x h_fg = 0.0772 x 2,309 = 178.3 kW  (h_fg @ 80 C egzoz)

eta_energy = Q_evap / E_total x 100
           = 178.3 / 323 x 100
           = 55.2%
```

---

### 13.5 Adim 4 - Exergy Girisi

**Isitici exergy girisi (brulor dahil gercekci hesap):**
```
Yakit enerji girisi:
Q_fuel = Q_heater / eta_burner = 300 / 0.90 = 333.3 kW

Yakit exergy girisi (phi = 1.04):
Ex_fuel = Q_fuel x phi = 333.3 x 1.04 = 346.7 kW
```

**Alternatif: Carnot yaklasimiyla (brulor sonrasi sicak hava):**
```
Ex_hot_air = Q_heater x (1 - T_0 / T_supply)
           = 300 x (1 - 298.15 / 423.15)
           = 300 x 0.295
           = 88.6 kW
```

**Fan ve yardimci exergy:**
```
Ex_fan = W_fan = 18 kW
Ex_aux = W_aux = 5 kW
```

**Toplam exergy girisi (brulor dahil):**
```
Ex_total_in = Ex_fuel + Ex_fan + Ex_aux
            = 346.7 + 18 + 5
            = 369.7 kW
```

---

### 13.6 Adim 5 - Buharlasmma Exergy'si

Ortalama buharlasmma sicakligi ~70 C = 343.15 K olarak kabul edelim:
```
ex_evap = h_fg - T_0 x s_fg
        = 2,334 - 298.15 x (2,334 / 343.15)
        = 2,334 - 2,027
        = 307 kJ/kg

Ex_evaporation = m_w x ex_evap
               = 0.0772 x 307
               = 23.7 kW
```

---

### 13.7 Adim 6 - Exergy Verimi

**Fonksiyonel exergy verimi:**
```
eta_ex = Ex_evaporation / Ex_total_in x 100
       = 23.7 / 369.7 x 100
       = 6.4%
```

Bu deger konvektif bant kurutucularin tipik araligina (%5-15) uymaktadir.

---

### 13.8 Adim 7 - Egzoz Exergy Kaybi (Detayli)

**Termal bilesen (kuru hava):**
```
Ex_exh_dry = m_air x Cp_a x [(T_ex - T_0) - T_0 x ln(T_ex / T_0)]
           = 1.25 x 1.005 x [(353.15 - 298.15) - 298.15 x ln(353.15 / 298.15)]
           = 1.256 x [55.0 - 298.15 x 0.1691]
           = 1.256 x [55.0 - 50.42]
           = 1.256 x 4.58
           = 5.75 kW
```

**Nem termal bileseni:**
```
Ex_exh_vapor = m_air x omega_ex x Cp_v x [(T_ex - T_0) - T_0 x ln(T_ex / T_0)]
             = 1.25 x 0.090 x 1.872 x [55.0 - 50.42]
             = 0.2106 x 4.58
             = 0.96 kW
```

**Kimyasal (konsantrasyon) bileseni:**
```
Ex_exh_chem = m_air x R_a x T_0 x [(1 + 1.608 x 0.090) x ln((1 + 1.608 x 0.012) / (1 + 1.608 x 0.090))
            + 1.608 x 0.090 x ln(0.090 / 0.012)]

Ara hesaplar:
(1 + 1.608 x 0.090) = 1.1447
(1 + 1.608 x 0.012) = 1.0193
ln(1.0193 / 1.1447) = ln(0.8904) = -0.1161
1.608 x 0.090 = 0.1447
ln(0.090 / 0.012) = ln(7.5) = 2.015

Ex_exh_chem = 1.25 x 0.287 x 298.15 x [1.1447 x (-0.1161) + 0.1447 x 2.015]
            = 1.25 x 0.287 x 298.15 x [-0.1329 + 0.2916]
            = 107.0 x 0.1587
            = 16.98 kW
```

**Toplam egzoz exergy kaybi:**
```
Ex_exhaust = 5.75 + 0.96 + 16.98 = 23.69 kW
```

**Gozlem:** Kimyasal bilesen (16.98 kW), termal bilesenlerin (6.71 kW) toplaminin
~2.5 kati buyuktur. Bu, egzoz havasindaki nemin tasidigi exergy'nin ne kadar onemli
oldugunu gosterir.

---

### 13.9 Adim 8 - Govde (Shell) Exergy Kaybi

```
Q_shell = h_combined x A_surface x (T_surface - T_amb)
        = 12 x 35 x (55 - 25)
        = 12 x 35 x 30
        = 12,600 W = 12.6 kW

Ex_shell = Q_shell x (1 - T_0 / T_surface)
         = 12.6 x (1 - 298.15 / 328.15)
         = 12.6 x 0.0914
         = 1.15 kW
```

---

### 13.10 Adim 9 - Isitma Tersinmezligi

Dogal gaz brulor alev sicakligi ~2,000 K, ardinda hava 150 C'ye isitilir:

```
Yanma tersinmezligi (yakit exergy'sinin ~%27'si):
I_combustion = 0.27 x Ex_fuel = 0.27 x 346.7 = 93.6 kW

Hava isitma tersinmezligi (alev -> sicak hava):
I_heat_transfer = Ex_fuel - I_combustion - Ex_hot_air - Q_shell_burner
                ≈ 346.7 - 93.6 - 88.6 - 10.0
                = 154.5 kW (brulor radyasyon kaybi dahil)
```

---

### 13.11 Adim 10 - Tam Exergy Dengesi

```
EXERGY GIRISI:
  Yakit exergy'si (dogal gaz):   346.7 kW  (93.8%)
  Fan elektrik girdisi:           18.0 kW  (4.9%)
  Yardimci ekipman:                5.0 kW  (1.3%)
  -----------------------------------------------
  TOPLAM GIRIS:                  369.7 kW  (100.0%)

FAYDALI EXERGY CIKISI:
  Buharlasmma exergy'si:          23.7 kW  (6.4%)

EXERGY KAYIPLARI VE YIKIMLARI:
  Yanma tersinmezligi:            93.6 kW  (25.3%)
  Isitma tersinmezligi:          154.5 kW  (41.8%)
  Egzoz havasi exergy kaybi:      23.7 kW  (6.4%)
  Kurutma prosesi tersinmezligi:  58.9 kW  (15.9%)
  Govde kayiplari (exergy):        1.2 kW  (0.3%)
  Fan tersinmezligi:               5.4 kW  (1.5%)
  Diger (kapatilmamis fark):       8.7 kW  (2.4%)
  -----------------------------------------------
  TOPLAM KAYIP/YIKIM:           346.0 kW  (93.6%)
  -----------------------------------------------
  TOPLAM:                        369.7 kW  (100.0%)
```

---

### 13.12 Adim 11 - Yillik Maliyet Analizi

```
Toplam yillik enerji tuketimi:
E_yillik = E_total x calisma_saati = 323 x 4,000 = 1,292,000 kWh/yil

Yillik enerji maliyeti:
Maliyet_yillik = E_yillik x enerji_fiyati = 1,292,000 x 0.05 = 64,600 EUR/yil

Exergy kayip maliyeti:
Ex_kayip_yillik = (Ex_total_in - Ex_evaporation) x 4,000 = 346.0 x 4,000 = 1,384,000 kWh/yil

Iyilestirme potansiyeli (Van Gool IP):
IP = (1 - 0.064) x 346.0 = 323.9 kW
IP_yillik = 323.9 x 4,000 x 0.05 = 64,780 EUR/yil
```

---

### 13.13 Adim 12 - Iyilestirme Onceliklendirme

Exergy kayip dagilimindan en buyuk iyilestirme firsatlari:

| Sira | Kayip Kalemi | Exergy [kW] | Pay [%] | Iyilestirme Onerisi |
|------|-------------|------------|---------|---------------------|
| 1 | Isitma tersinmezligi | 154.5 | 41.8% | Atik isi kaynagi veya isi pompasi kullan |
| 2 | Yanma tersinmezligi | 93.6 | 25.3% | Gaz brulor yerine atik isi/buhar/HP |
| 3 | Kurutma prosesi | 58.9 | 15.9% | Hava hizi/sicaklik optimizasyonu |
| 4 | Egzoz kaybi | 23.7 | 6.4% | Egzoz isi geri kazanimi (preheating) |
| 5 | Fan tersinmezligi | 5.4 | 1.5% | VSD, dusen basinc azaltma |
| 6 | Govde kaybi | 1.2 | 0.3% | Ek yalitim (yatirim/getiri analizi yap) |

**Oncelikli mudahale:** Isitma tersinmezligi + yanma tersinmezligi toplam %67.1
olusturuyor. Isi kaynaginin kalitesini kurutma prosesinin gerektirdigi seviyeye
indirmek (ornegin isi pompasi veya atik isi kullanimi) en buyuk tasarrufu saglar.

**Potansiyel tasarruf (isi pompali sisteme gecis):**
```
Mevcut exergy verimi: %6.4
Hedef exergy verimi (HP): %20
Gerekli exergy girisi (HP): Ex_evaporation / 0.20 = 23.7 / 0.20 = 118.5 kW

Mevcut elektrik esdegeri: 323 kW
HP elektrik tuketimi: ~118.5 kW (COP ≈ 3.0 ile yaklasik)
Enerji tasarrufu: 323 - 118.5 = 204.5 kW = %63 azalma

Yillik maliyet tasarrufu: 204.5 x 4,000 x 0.05 = 40,900 EUR/yil
Tipik yatirim maliyeti: 80,000 - 120,000 EUR
Basit geri odeme suresi: ~2.0 - 2.9 yil
```

---

## 14. Exergy Akis Diyagrami (Grassmann Diagram)

### 14.1 Konvektif Kurutucu Tipik Exergy Akisi

```
EXERGY GIRISI (100%)
|
|-- Isitici exergy girdisi (85-95%)
|   |
|   |-- Yanma tersinmezligi (%20-30) ------------> EXERGY YIKIMI
|   |   [Kimyasal reaksiyon, termodinamik zorunluluk]
|   |
|   |-- Isitma tersinmezligi (%15-40) -----------> EXERGY YIKIMI
|   |   [Yuksek T kaynak -> dusuk T proses isi transferi]
|   |
|   |-- Kurutma prosesi tersinmezligi (%10-20) --> EXERGY YIKIMI
|   |   [Nemli malzeme - hava etkilesimi]
|   |
|   |-- Egzoz havasi exergy kaybi (%5-15) -------> KAYIP (GERI KAZANILAB ILIR)
|   |   [Sicak, nemli egzoz havasi]
|   |
|   |-- Govde kayiplari (%1-5) ------------------> KAYIP
|   |   [Radyasyon ve konveksiyon]
|   |
|   |-- Faydali buharlasmma exergy'si (%5-15) ---> FAYDALI CIKIS
|       [Hedef: nem uzaklastirma]
|
|-- Fan elektrik girdisi (3-10%)
|   |-- Fan tersinmezligi (%1-5) -----------------> EXERGY YIKIMI
|
|-- Yardimci ekipman (1-5%)
    |-- Konveyor, vb. tersinmezligi (%0.5-3) ----> EXERGY YIKIMI
```

### 14.2 Isi Pompali Kurutucu Exergy Akisi

```
EXERGY GIRISI (100% - tamami elektrik)
|
|-- Kompressor elektrik girdisi (75-85%)
|   |
|   |-- Kompressor tersinmezligi (%20-30) -------> EXERGY YIKIMI
|   |
|   |-- Kondenser -> hava isitma (%30-40) -------> ISI GERI KAZANIMI (dahili)
|   |
|   |-- Evaporator <- egzoz sogutma (%15-25) ----> EGZOZ GERI KAZANIMI (dahili)
|   |
|   |-- Faydali buharlasmma exergy (%15-30) -----> FAYDALI CIKIS
|
|-- Fan elektrik girdisi (10-20%)
|
|-- Yardimci (%5-10%)
```

---

## 15. Enerji ve Exergy Verimi Iyilestirme Stratejileri Ozeti

| Strateji | Enerji Tasarrufu | Exergy Verimi Artisi | Yatirim | Geri Odeme |
|----------|-----------------|---------------------|---------|-----------|
| Egzoz geri kazanimi | %10-25 | +%1-4 puan | 10,000-50,000 EUR | 1-3 yil |
| Hava resirkulasyonu | %5-15 | +%0.5-2 puan | 5,000-20,000 EUR | 0.5-2 yil |
| Yalitim iyilestirme | %3-8 | +%0.3-1 puan | 3,000-15,000 EUR | 1-3 yil |
| Sicaklik optimizasyonu | %5-15 | +%1-3 puan | 2,000-10,000 EUR | 0.5-1 yil |
| VSD fan surucusu | %2-5 | +%0.2-0.5 puan | 3,000-8,000 EUR | 1-2 yil |
| Mekanik on susuzlastirma | %20-40 | +%3-8 puan | 20,000-80,000 EUR | 1-3 yil |
| Isi pompasi retrofit | %40-65 | +%8-20 puan | 60,000-200,000 EUR | 2-5 yil |
| Kizgin buhar (SSD) | %30-50 | +%10-25 puan | 100,000-500,000 EUR | 3-7 yil |

---

## 16. Sinirlamalar

1. **Sabit kurutma hizi kabulu:** Hesaplamalar ortalama kararli hal (steady-state)
   icin yapilmistir. Kurutma hizi egrisi boyunca degisen performans ayri ayri
   modellenmemistir.

2. **Homojen hava dagilimi:** Kurutucu icindeki hava dagiliminin homojen oldugu
   varsayilmistir. Gercekte olu bolge (dead zone) ve kisa devre akislari
   performansi dusurur.

3. **Sicakliga bagli ozellikler:** Cp, h_fg gibi termodinamik ozellikler sabit
   veya ortalama deger olarak alinmistir. Gercekte sicaklikla degisir.

4. **Bagli nem etkisi:** Malzeme icindeki bagli su (bound moisture) icin
   buharlasmma enerjisi serbest sudan daha yuksektir. Bu etki ihmal edilmistir.

5. **Malzeme exergy'si:** Kurutulan malzemenin kendisinin exergy degisimi
   (kimyasal ve fiziksel) hesaba katilmamistir.

6. **Radyasyon isitma:** Infrared ve mikrodalga kurutma icin ozel exergy
   modeli gerekmektedir; bu basit konvektif model yetersiz kalir.

7. **Gecis rejimleri:** Baslangic, durdurma ve yuk degisimi sirasindaki
   gecici rejim kayiplari dahil degildir.

---

## İlgili Dosyalar

- `dryer/benchmarks.md` -- Kurutucu performans karsilastirma ve sektorel benchmark degerleri
- `dryer/psychrometrics.md` -- Nemli hava termodinamigi ve detayli psikrometrik hesaplar
- `dryer/audit.md` -- Kurutma sistemleri enerji/exergy denetim proseduru
- `dryer/equipment/belt_dryer.md` -- Bant kurutucu detayli analiz
- `dryer/equipment/tunnel_dryer.md` -- Tunel kurutucu detayli analiz
- `dryer/equipment/spray_dryer.md` -- Sprey kurutucu detayli analiz
- `dryer/equipment/rotary_dryer.md` -- Doner kurutucu detayli analiz
- `dryer/equipment/fluidized_bed.md` -- Akiskan yatak kurutucu analiz
- `dryer/equipment/heat_pump_dryer.md` -- Isi pompali kurutucu analiz
- `dryer/equipment/drum_dryer.md` -- Silindir kurutucu analiz
- `dryer/equipment/infrared_dryer.md` -- Infrared kurutucu analiz
- `dryer/solutions/exhaust_heat_recovery.md` -- Egzoz isi geri kazanimi
- `dryer/solutions/air_recirculation.md` -- Hava geri deviri
- `dryer/solutions/heat_pump_retrofit.md` -- Isi pompasi retrofit
- `dryer/solutions/insulation.md` -- Yalitim iyilestirme
- `dryer/solutions/temperature_optimization.md` -- Sicaklik optimizasyonu
- `dryer/solutions/mechanical_dewatering.md` -- Mekanik on susuzlastirma
- `dryer/solutions/solar_preheating.md` -- Gunes enerjisi on isitma
- `factory/cross_equipment.md` -- Ekipmanlar arasi entegrasyon firsatlari (kompressor atik isisi -> kurutucu on isitma vb.)

---

## Referanslar

- Mujumdar, A.S., "Handbook of Industrial Drying," CRC Press, 4th Edition, 2014
- Dincer, I. & Rosen, M.A., "Exergy: Energy, Environment and Sustainable Development," Elsevier, 3rd Edition, 2013
- Kemp, I.C., "Fundamentals of Energy Analysis of Dryers," in Modern Drying Technology, Vol. 4: Energy Savings, Wiley-VCH, 2012
- Kemp, I.C., "Reducing Dryer Energy Use by Process Integration and Pinch Analysis," Drying Technology, 23(9-11), 2089-2104, 2005
- Cengel, Y.A. & Boles, M.A., "Thermodynamics: An Engineering Approach," McGraw-Hill, 9th Edition, 2019
- Bejan, A., "Advanced Engineering Thermodynamics," Wiley, 4th Edition, 2016
- Aghbashlo, M. et al. (2013), "A review on exergy analysis of drying processes and systems," Renewable and Sustainable Energy Reviews, 22, 1-22
- Akpinar, E.K. (2004), "Energy and exergy analyses of drying of red pepper slices in a convective type dryer," International Communications in Heat and Mass Transfer, 31(8), 1165-1176
- Erbay, Z. & Icier, F. (2010), "A review of thin layer drying of foods: theory, modeling, and experimental results," Critical Reviews in Food Science and Nutrition, 50(5), 441-464
- Colak, N. & Hepbasli, A. (2009), "A review of heat pump drying: Part 1 -- Systems, models and studies," Energy Conversion and Management, 50, 2180-2186
- Szargut, J., Morris, D.R. & Steward, F.R., "Exergy Analysis of Thermal, Chemical, and Metallurgical Processes," Hemisphere Publishing, 1988
- ASHRAE Handbook -- Fundamentals, Chapter 6: Psychrometrics, 2021
- US DOE, "Improving Process Heating System Performance: A Sourcebook for Industry," 2nd Edition, 2007
- Carbon Trust, "Industrial Energy Efficiency Accelerator -- Guide to the Drying and Dehydration Sector," 2011
- ISO 13579:2002, "Industrial furnaces and associated processing equipment -- Method of measuring energy balance and calculating efficiency"
