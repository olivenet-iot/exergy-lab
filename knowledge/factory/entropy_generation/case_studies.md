---
title: "Vaka Calismalari — Endustriyel EGM Uygulamalari (Case Studies — Industrial EGM Applications)"
category: factory
equipment_type: factory
keywords: [vaka calismasi, endustriyel uygulama, cimento, sogutma, boru agi, retrofit, EGM sonuclari]
related_files: [factory/entropy_generation/industrial_applications.md, factory/entropy_generation/overview.md, factory/case_studies.md]
use_when: ["Endustriyel EGM uygulama ornekleri aranirken", "Vaka calismasi referansi gerektiginde", "EGM'nin gercek dunya sonuclari gosterilecekken"]
priority: medium
last_updated: 2026-02-01
---

# Vaka Calismalari — Endustriyel EGM Uygulamalari (Case Studies — Industrial EGM Applications)

Bu dosya, Entropi Uretim Minimizasyonu (Entropy Generation Minimization — EGM) metodolojisinin gercek endustriyel sistemlere uygulanmasindan elde edilen detayli vaka calismalarini sunar. Her vaka; problem tanimi, EGM analizi, uygulanan cozumler ve olculebilir sonuclari icerir.

> **Onemli:** Bu vaka calismalari, EGM'nin yalnizca akademik bir arac olmadigini, somut endustriyel tasarruflar saglayan pratik bir optimizasyon yontemi oldugunu gostermektedir.

---

## Vaka 1: Cimento Fabrikasi Atik Isi Optimizasyonu (Cement Plant Waste Heat Optimization)

### 1.1 Problem Tanimi

Bir cimento fabrikasinda (yillik kapasite: 1.2 milyon ton klinker) asagidaki ana ekipmanlar bulunmaktadir:

| Ekipman | Sicaklik (°C) | Debi | Mevcut Durum |
|---|---|---|---|
| Doner firin baca gazi (Rotary kiln exhaust) | 350 | 120,000 Nm³/h | Kismi isi geri kazanimi |
| Klinker sogutucusu egzozu (Clinker cooler exhaust) | 280 | 85,000 Nm³/h | Atmosfere atiliyor |
| On isitici kulesi (Preheater tower) | 4 kademeli | — | Mevcut tasarim |

**Mevcut durum:**
- Firin baca gazindan kismi isi geri kazanimi ile ham madde (raw meal) on isitmasi yapilmaktadir
- Klinker sogutucusu egzozunun buyuk kismi atmosfere atilmaktadir
- Toplam atik isi potansiyeli ≈ 28 MW(t) iken yalnizca ≈ 12 MW(t) geri kazanilmaktadir
- Fabrika elektrik tuketimi: 18 MW (sebekeden)
- Cevre sicakligi referansi: T₀ = 298.15 K (25 °C)

**Enerji analizi siniri:** Klasik enerji analizi yalnizca "baca gazi sicak, isi geri kazanilmali" der. Ancak **hangi noktada ne kadar entropi uretildigi** ve dolayisiyla **nerede oncelikli mudahale edilmesi gerektigi** konusunda bilgi vermez.

### 1.2 EGM Analizi (Entropy Generation Mapping)

#### 1.2.1 Sistem Sinirlari ve Olcumler

EGM analizi icin tum isi transferi yuzeylerinde sicaklik, debi ve basinc olcumleri yapilmistir. Entropi uretim hizi (Ṡ_gen) her bir bilesende hesaplanmistir:

**Firin baca gazi hatti:**

| Bilesken | T_sicak (°C) | T_soguk (°C) | Q̇ (kW) | Ṡ_gen (kW/K) | Pay (%) |
|---|---|---|---|---|---|
| On isitici 4. kademe (Preheater Stage 4) | 350 → 290 | 680 → 750 | 4,200 | 1.82 | 22.5 |
| On isitici 3. kademe | 290 → 245 | 580 → 680 | 3,100 | 1.53 | 18.9 |
| On isitici 2. kademe | 245 → 210 | 420 → 580 | 2,400 | 1.21 | 15.0 |
| On isitici 1. kademe | 210 → 185 | 280 → 420 | 1,700 | 0.85 | 10.5 |
| Baca gazi — atmosfer (Exhaust to atmosphere) | 185 → 25 | — | 5,600 | 2.15 | 26.6 |
| **Toplam firin hatti** | | | **17,000** | **7.56** | **93.5** |

**Klinker sogutucusu hatti:**

| Bilesken | T_sicak (°C) | T_soguk (°C) | Q̇ (kW) | Ṡ_gen (kW/K) | Pay (%) |
|---|---|---|---|---|---|
| Sogutma havasi — klinker | 1200 → 100 | 25 → 280 | 9,500 | — | — |
| Soguk egzoz — atmosfer | 280 → 25 | — | 2,500 | 0.53 | 6.5 |
| **Toplam sogutucusu hatti** | | | **12,000** | **0.53** | **6.5** |

**Toplam sistem Ṡ_gen = 8.09 kW/K**

**Gouy-Stodola karsiligi:**
$$\dot{X}_{yıkım} = T_0 \times \dot{S}_{gen} = 298.15 \times 8.09 = 2{,}412 \text{ kW} \approx 2.41 \text{ MW}$$

Bu, 2.41 MW is potansiyelinin tersinmezlikler nedeniyle yok edildigini gosterir.

#### 1.2.2 Bejan Sayisi Analizi (Bejan Number Analysis)

Her bir isi degistiricisi icin Bejan sayisi (Be) hesaplanmistir:

$$Be = \frac{\dot{S}_{gen,\Delta T}}{\dot{S}_{gen,\Delta T} + \dot{S}_{gen,\Delta P}}$$

| Bilesken | Be | Yorum |
|---|---|---|
| On isitici 4. kademe | 0.92 | Isi transferi ΔT baskin → yaklasma sicakligi azaltilmali |
| On isitici 3. kademe | 0.89 | Isi transferi ΔT baskin |
| On isitici 2. kademe | 0.87 | Isi transferi ΔT baskin |
| On isitici 1. kademe | 0.83 | Isi transferi baskin, ancak ΔP etkisi artmaya basliyor |

**Tani (Diagnosis):** Be > 0.85 olan bilesenler icin **isi transferi yuzeyini artirmak** (yaklasma sicakligini dusurmek) onceliklidir. Be < 0.5 olsaydi boru/kanal boyutlandirma optimizasyonu yapilacakti.

### 1.3 Cozum (Solution)

EGM analizinin bulgularina dayanarak asagidaki mudahaleler uygulanmistir:

#### 1.3.1 Atik Isi Geri Kazanim Kazani (Waste Heat Recovery Boiler — WHR)

- Klinker sogutucusu egzozuna (280 °C) bir WHR kazan yerlestirilmistir
- WHR kazandan uretilen buhar ile ORC (Organic Rankine Cycle) turkbini beslenmistir
- ORC calisma akiskani: R-245fa (kritik sicaklik 154 °C)
- Buharlastirici sicakligi: 130 °C, yogusturucu sicakligi: 35 °C
- ORC termal verim (thermal efficiency): ηth ≈ 12.5%

**ORC Entropi Uretim Analizi:**

| ORC Bileseni | Ṡ_gen (kW/K) | Pay (%) |
|---|---|---|
| Buharlastirici (Evaporator) | 0.18 | 34.0 |
| Turbin (Turbine) | 0.12 | 22.6 |
| Yogusturucu (Condenser) | 0.15 | 28.3 |
| Pompa (Pump) | 0.02 | 3.8 |
| Boru kayiplari (Piping losses) | 0.06 | 11.3 |
| **Toplam ORC** | **0.53** | **100** |

#### 1.3.2 On Isitici Kademelerinin Optimizasyonu

EGM analizi, 4. kademe on isiticida en yuksek Ṡ_gen degerinin oldugunu gostermistir (1.82 kW/K). Nedeni: sicak gaz ile ham madde arasindaki buyuk ΔT.

**Uygulanan iyilestirmeler:**
- 4. kademe siklon isi transfer yuzey alani %30 artirilmistir
- Yaklasma sicakligi (approach temperature): 60 °C → 35 °C
- Sonuc: 4. kademe Ṡ_gen = 1.82 → 1.24 kW/K (%32 azalma)

#### 1.3.3 Ekonomizer Eklenmesi

- Firin baca gazi cikisina ekonomizer eklenmistir
- Baca gazi sicakligi: 185 °C → 120 °C
- Geri kazanilan isi: ≈ 2,200 kW → kazanin besleme suyu isitmasi
- Ekonomizer Ṡ_gen = 0.35 kW/K (dusuk ΔT tasarimi sayesinde)

### 1.4 Sonuclar (Results)

| Parametre | Once (Before) | Sonra (After) | Degisim |
|---|---|---|---|
| Toplam Ṡ_gen (kW/K) | 8.09 | 5.26 | **−35%** |
| Exergy yikimi (kW) | 2,412 | 1,568 | −844 kW |
| ORC elektrik uretimi | 0 | 2.5 MW | +2.5 MW |
| Baca gazi sicakligi (°C) | 185 | 120 | −65 °C |
| Yillik elektrik tasarrufu | — | ≈ 18,000 MWh | — |
| Yillik tasarruf | — | ≈ €800,000 | — |
| Toplam yatirim | — | €2,800,000 | — |
| Geri odeme suresi (Payback) | — | **3.5 yil** | — |

> **Anahtar bulgu:** Enerji analizinde "verimli" gorunen on isitici sistemi, EGM ile incelendiginde 4. kademede ciddi entropi uretimi ortaya cikmistir. Sadece enerji bazli analiz, ORC potansiyelini de gozden kacirabilirdi.

---

## Vaka 2: Sogutma Sistemi EGM Retrofit (Refrigeration System EGM Retrofit)

### 2.1 Problem Tanimi

Bir gida isleme tesisinde (et isletmesi) mevcut sogutma sistemi:

| Parametre | Deger |
|---|---|
| Sogutma kapasitesi (Cooling capacity) | 500 kW |
| Sogutucu akiskan (Refrigerant) | R-404A |
| Kompresör tipi | Vidali (Screw), 15 yasinda |
| COP (mevcut) | 3.2 (sektor ortalamasi: 4.0–4.5) |
| Yogusma sicakligi (Condensing temp.) | 42 °C |
| Buharlasma sicakligi (Evaporating temp.) | −5 °C |
| Kondenser yaklasma sicakligi | 8 °C (standart: 3–5 °C) |
| Genlesme vanasi tipi | Termostatik (TXV) |
| Sogutulmus su ΔT | 4 °C (olmasi gereken: 5–6 °C) |
| Cevre sicakligi T₀ | 298.15 K (25 °C) |

**Sorunlar:**
- Dusuk COP nedeniyle yuksek enerji tuketimi
- Kondenser kirlilik (fouling) nedeniyle yuksek yaklasma sicakligi
- TXV vanalari ile asiri isitma (superheat) kontrolu yetersiz
- Sogutulmus su tarafinda dusuk ΔT → yuksek pompalama gucu

### 2.2 EGM Analizi (Component-by-Component S_gen Breakdown)

Her bilesende entropi uretimi hesaplanmistir. Toplam sistem Ṡ_gen = 0.587 kW/K.

#### 2.2.1 Bilesen Bazli Entropi Uretim Haritasi

| Bilesen | Ṡ_gen (kW/K) | Pay (%) | Ana Neden |
|---|---|---|---|
| Genlesme vanasi (Expansion valve — TXV) | 0.223 | **38.0** | Kisma tersinmezligi (throttling irreversibility) |
| Kompresör (Compressor) | 0.147 | **25.0** | Dusuk izentropik verim (ηis = 0.68) |
| Yogusturucu (Condenser) | 0.129 | **22.0** | Yuksek yaklasma ΔT = 8 °C, kirlilik |
| Buharlastirici (Evaporator) | 0.088 | **15.0** | Dusuk su tarafi ΔT → yuksek ṁ → yuksek ΔP |

#### 2.2.2 Genlesme Vanasi Detayli Analizi

Genlesme vanasindaki entropi uretimi, izentalpik kisma islemi (isenthalpic throttling) nedeniyle olusur:

$$\dot{S}_{gen,exp} = \dot{m}_r \times (s_{out} - s_{in})$$

R-404A icin:
- Yogusturucu cikisi: T = 37 °C, sivi (subcooled 5 °C), h = 256.3 kJ/kg, s = 1.198 kJ/(kg·K)
- Buharlastirici girisi: T = −5 °C, iki fazli, h = 256.3 kJ/kg, s = 1.283 kJ/(kg·K)
- Kutle debisi: ṁ = 2.62 kg/s
- Ṡ_gen = 2.62 × (1.283 − 1.198) = **0.223 kW/K**

> **Kritik bulgu:** Genlesme vanasi, hicbir hareketli parcasi olmayan, enerji kaybetmeyen bir cihaz olmasina ragmen, **toplam entropi uretiminin %38'inden** sorumludur. Klasik enerji analizi bu kaybi goremez!

#### 2.2.3 Yogusturucu Bejan Sayisi

$$Be_{kond} = \frac{\dot{S}_{gen,\Delta T}}{\dot{S}_{gen,\Delta T} + \dot{S}_{gen,\Delta P}} = \frac{0.105}{0.105 + 0.024} = 0.81$$

Be = 0.81 → Isi transferi tersinmezligi baskin → yaklasma sicakligini dusurmek oncelikli.

#### 2.2.4 Buharlastirici Bejan Sayisi

$$Be_{buh} = \frac{\dot{S}_{gen,\Delta T}}{\dot{S}_{gen,\Delta T} + \dot{S}_{gen,\Delta P}} = \frac{0.052}{0.052 + 0.036} = 0.59$$

Be = 0.59 → Hem isi transferi hem de basinc dusumu onemli → her ikisi de optimize edilmeli.

### 2.3 Cozum — Asamali Retrofit (Phased Retrofit)

EGM analizinin onceliklendirmesine gore 3 asamali bir retrofit plani uygulanmistir:

#### Asama 1: Yogusturucu Temizligi + Sogutma Kulesi Dolgu Yenileme (Dusuk Maliyet)

- Yogusturucu tupu kimyasal temizlik (chemical cleaning)
- Sogutma kulesi dolgusu (cooling tower fill) yenilenmesi
- **Sonuc:** Yaklasma sicakligi 8 °C → 4 °C
- Yogusma sicakligi: 42 °C → 38 °C
- Yogusturucu Ṡ_gen: 0.129 → 0.082 kW/K (%36 azalma)
- COP artisi: 3.2 → 3.55

#### Asama 2: Elektronik Genlesme Vanasi (EEV) Kurulumu

- TXV → EEV (Electronic Expansion Valve) degisimi
- PID bazli asiri isitma kontrolu: superheat 8 K → 5 K
- Daha dusuk buharlasma sicakligi dalgalanmasi
- **Sonuc:** Genlesme Ṡ_gen: 0.223 → 0.195 kW/K (%12.5 azalma)
- Toplam sistem Ṡ_gen iyilesmesi: ≈ %5
- COP artisi: 3.55 → 3.72

#### Asama 3: Sogutulmus Su ΔT Optimizasyonu

- Buharlastirici su tarafi ΔT: 4 °C → 6 °C
- Su debisi azaltildi: ṁ_su = 29.8 → 19.9 kg/s
- Pompalama gucu: 7.5 kW → 3.8 kW
- Buharlastirici Ṡ_gen: 0.088 → 0.065 kW/K (%26 azalma)
- **Sonuc:** COP artisi: 3.72 → 4.10

#### Gelecek Asama 4 (Planli): Chiller Degisimi

- R-404A → R-513A (dusuk GWP)
- Yeni yuksek verimli vidali kompresör (ηis = 0.82)
- Beklenen COP: ≥ 4.8
- Beklenen toplam Ṡ_gen azalmasi: ≈ %45 (mevcut sisteme gore)

### 2.4 Sonuclar (Results)

| Parametre | Once | Asama 1 | Asama 2 | Asama 3 | Toplam Degisim |
|---|---|---|---|---|---|
| COP | 3.2 | 3.55 | 3.72 | 4.10 | **+28%** |
| Ṡ_gen (kW/K) | 0.587 | 0.540 | 0.512 | 0.423 | **−28%** |
| Elektrik tuketimi (kW) | 156.3 | 140.8 | 134.4 | 121.9 | −34.4 kW |
| Yillik enerji tasarrufu | — | — | — | 180 MWh | — |
| Yillik tasarruf | — | — | — | €18,000 | — |
| Toplam yatirim (Asama 1–3) | — | — | — | €25,000 | — |
| Geri odeme suresi | — | — | — | **1.4 yil** | — |

> **Anahtar bulgu:** Genlesme vanasi — enerji analizinde "gorunmez" bir bilesen — EGM ile en buyuk iyilestirme hedefi olarak tanimlanmistir. Asamali retrofit yaklasimi, dusuk baslangic yatirimi ile hizli geri donusu mumkun kilmistir.

---

## Vaka 3: Boru Agi Yeniden Tasarimi (Pipe Network Redesign)

### 3.1 Problem Tanimi

Bir kimya tesisinde sogutma suyu dagitim agi:

| Parametre | Deger |
|---|---|
| Toplam sogutma noktasi sayisi | 15 adet |
| Toplam debi | ṁ = 200 kg/s |
| Mevcut boru capi (tum sebekede) | DN200 (tek tip) |
| Kisma vanasi (Throttle valve) sayisi | 12 adet |
| Toplam pompalama gucu | 75 kW (2 × sabit hizli pompa) |
| Su sicakligi | 30 °C (giris) → degisken (cikis) |
| Basinc | 4 bar (pompa cikisi), 1.5 bar (geri donus) |
| Cevre sicakligi T₀ | 298.15 K |

**Mevcut tasarim sorunlari:**
- Tum borular ayni capta (DN200) → bazi hatlarda asiri hiz, bazilerinde dusuk hiz
- Debi dengelemesi icin 12 adet kisma vanasi kullanilmakta
- Vanalar surekli olarak enerjiyi isi olarak dissipe etmekte (throttling loss)
- Bazi dal borulari icin DN200 asiri buyuk → dusuk hiz → kotu isi transferi
- Bazi dal borulari icin DN200 yetersiz → yuksek hiz → yuksek ΔP

### 3.2 EGM Analizi (Network Entropy Generation Mapping)

#### 3.2.1 Entropi Uretim Kaynaklari

Boru agindaki toplam entropi uretimi iki ana kaynaktan olusur:

$$\dot{S}_{gen,boru} = \dot{S}_{gen,\Delta P} + \dot{S}_{gen,\Delta T}$$

Sogutma suyu sistemi icin ΔT kaynakli Ṡ_gen ihmal edilebilir duzeydedir (boru yalitimi yeterli, sicaklik farki dusuk). Dolayisiyla baskin kaynak **basinc dusumu** (ΔP) dir:

$$\dot{S}_{gen,\Delta P} = \frac{\dot{m} \times \Delta P}{\rho \times T}$$

#### 3.2.2 Bilesen Bazli Ṡ_gen Haritasi

| Bilesen Grubu | Ṡ_gen (kW/K) | Pay (%) | Aciklama |
|---|---|---|---|
| Kisma vanalari (Throttle valves) | 0.203 | **45.0** | 12 vana, toplam ΔP ≈ 1.2 bar |
| Dal borulari (Branch pipes) | 0.135 | **30.0** | DN200 bazi hatlar icin yetersiz |
| Dirsekler ve T-parcalari (Fittings) | 0.058 | 12.9 | Yerel kayiplar |
| Ana kolon (Main header) | 0.023 | **5.1** | DN200 ana hat icin uygun |
| Pompa tersinmezligi | 0.031 | 6.9 | Sabit hiz, kismi yuk calismasi |
| **Toplam** | **0.450** | **100** | — |

**Gouy-Stodola karsiligi:**
$$\dot{X}_{yıkım} = 298.15 \times 0.450 = 134.2 \text{ kW}$$

Bu deger, pompanin tukettiginden (75 kW) bile fazladir — cunku pompanin kendisi de bu tersinmezlikleri asabilmek icin enerji harcamaktadir.

#### 3.2.3 Ag Bejan Sayisi Analizi

Boru agi icin genel Bejan sayisi:

$$Be_{ag} = \frac{\dot{S}_{gen,\Delta T}}{\dot{S}_{gen,\Delta T} + \dot{S}_{gen,\Delta P}} = \frac{0.008}{0.008 + 0.442} = 0.018$$

Be ≈ 0.02 → Basinc dusumu tamamen baskin. Optimizasyon stratejisi: **akis direncini azaltmak** (boru boyutlandirma + vana eleminasyonu).

### 3.3 Cozum — Konstruktal/EGM Tabanli Yeniden Tasarim

Bejan'in konstruktal teori (constructal theory) prensipleri ile EGM analizi birlikte kullanilarak ag yeniden tasarlanmistir.

#### 3.3.1 Boru Boyutlandirma Optimizasyonu

EGM'ye gore optimal boru capi, entropi uretiminin minimumunda bulunur. Boru capini artirmak ΔP'yi azaltir ancak malzeme maliyetini artirir. Optimal nokta:

$$D_{opt} \propto \dot{m}^{3/7}$$

Bu ilisikye gore yeniden boyutlandirma:

| Hat | Eski Cap | Yeni Cap | Debi (kg/s) | Gerekce |
|---|---|---|---|---|
| Ana kolon (Main header) | DN200 | **DN250** | 200 | Toplam akis → buyutuldu |
| Alt-kolon 1 (Sub-header 1) | DN200 | **DN150** | 80 | Gercek debi ile orantili |
| Alt-kolon 2 (Sub-header 2) | DN200 | **DN150** | 70 | Gercek debi ile orantili |
| Alt-kolon 3 (Sub-header 3) | DN200 | **DN125** | 50 | Gercek debi ile orantili |
| Dal borulari (Branches) | DN200 | **DN80–DN125** | 5–25 | Her noktanin debisine gore |

#### 3.3.2 Kisma Vanasi Eleminasyonu

Boru boyutlarinin dogru secilmesiyle debi dengelemesi boru direnci ile saglanmistir:

- **Onceki:** 12 kisma vanasi → toplam ΔP = 1.2 bar
- **Sonraki:** Yalnizca 4 ayar vanasi (balanslama icin) → toplam ΔP = 0.15 bar
- 8 vana tamamen kaldirilmistir

#### 3.3.3 Degisken Hizli Pompa (VSD) Uygulamasi

- 2 × sabit hizli pompa → 2 × degisken hizli surucu (VSD) pompasi
- Diferansiyel basinc kontrolu ile debi yonetimi
- Kismi yukte verim: sabit %45 → VSD ile %72

### 3.4 Sonuclar (Results)

| Parametre | Once (Before) | Sonra (After) | Degisim |
|---|---|---|---|
| Toplam Ṡ_gen (kW/K) | 0.450 | 0.180 | **−60%** |
| Exergy yikimi (kW) | 134.2 | 53.7 | −80.5 kW |
| Pompalama gucu (kW) | 75 | 32 | **−57%** |
| Kisma vanasi sayisi | 12 | 4 | −8 adet |
| Yillik enerji tasarrufu | — | 344 MWh | — |
| Yillik tasarruf | — | €34,400 | — |
| Toplam yatirim | — | €120,000 | — |
| Geri odeme suresi | — | **3.5 yil** | — |

> **Anahtar bulgu:** Kisma vanalari, boru agindaki Ṡ_gen'in %45'inden sorumludur. Dogru boru boyutlandirmasi ile vana ihtiyaci ortadan kaldirilmis ve pompalama gucu %57 azalmistir. Konstruktal teori prensipleri (D_opt ∝ ṁ^{3/7}) pratik ve etkili sonuclar vermistir.

---

## Vaka 4: Kazan Sistemi EGM Optimizasyonu (Boiler System EGM Optimization)

### 4.1 Problem Tanimi

Bir tekstil fabrikasinda buhar kazan sistemi:

| Parametre | Deger |
|---|---|
| Kazan tipi | Dogal gazli, ates tuplu (fire-tube) |
| Buhar kapasitesi | 10 ton/h (doymus buhar, 8 bar) |
| Kazan verimi (enerji, LHV bazli) | %86 |
| Kazan verimi (exergy) | %32 |
| Baca gazi sicakligi | 220 °C |
| Ekonomizer | Yok |
| Hava on isiticisi (Air preheater) | Yok |
| Fazla hava orani (Excess air) | %15 (O₂ = %3.2) |
| Kondensat geri donus orani | %60 |
| Blowdown orani | %5 |
| Besleme suyu sicakligi | 65 °C |
| Cevre sicakligi T₀ | 298.15 K (25 °C) |

**Kritik gozlem:** Enerji verimi %86 iken exergy verimi yalnizca %32'dir. Bu 54 puanlik fark, kazan sistemlerinin en buyuk tersinmezlik kaynagi oldugunu gosterir. Enerji analizine gore kazan "iyi" durumda gorulur, ancak EGM gercek resmi ortaya koyar.

### 4.2 EGM Analizi (Boiler S_gen Breakdown)

#### 4.2.1 Toplam Entropi Uretim Haritasi

Dogal gaz kazaninda temel entropi uretim kaynaklari:

$$\dot{S}_{gen,toplam} = \dot{S}_{gen,yanma} + \dot{S}_{gen,baca} + \dot{S}_{gen,\Delta T} + \dot{S}_{gen,blowdown} + \dot{S}_{gen,radyasyon}$$

Kazan termal gucu: Q̇_kazan = 7,200 kW (buhar uretimi icin)
Yakit giris gucu: Q̇_yakit = 8,372 kW (LHV bazli)

| Tersinmezlik Kaynagi | Ṡ_gen (kW/K) | Pay (%) | Azaltilabilirlik |
|---|---|---|---|
| Yanma tersinmezligi (Combustion irreversibility) | 5.22 | **58.0** | Kismi (partially reducible) |
| Baca gazi isi kaybi (Flue gas heat loss) | 1.62 | **18.0** | Onemli olcude azaltilabilir |
| Isi transferi ΔT (Flame → water) | 1.08 | **12.0** | Kismi |
| Blowdown kaybi | 0.45 | **5.0** | Azaltilabilir |
| Radyasyon ve diger | 0.63 | **7.0** | Sinirli |
| **Toplam** | **9.00** | **100** | — |

**Gouy-Stodola karsiligi:**
$$\dot{X}_{yıkım} = 298.15 \times 9.00 = 2{,}683 \text{ kW} \approx 2.68 \text{ MW}$$

#### 4.2.2 Yanma Tersinmezligi Detayi

Yanma, kazandaki en buyuk entropi kaynagi (%58) olup, temel olarak yakit kimyasal exergy'sinin yuksek sicakliktaki yalim icinde isi enerjisine donusmesinden kaynaklanir:

$$\dot{S}_{gen,yanma} = \dot{m}_{yakit} \times \left[ s_{urunler} - s_{reaktanlar} - \frac{q_{reaksiyon}}{T_{alev}} \right]$$

**Neden bu kadar buyuk?**
- Dogal gaz kimyasal exergy/enerji orani ≈ 1.04
- Ancak enerji, alev sicakliginda (≈ 1800 °C) isi olarak aciga cikar
- Bu isi, ≈ 170 °C (ortalama buhar sicakligi) seviyesine transfer edilir
- Sicaklik orani: T_alev/T_buhar ≈ 2073/443 ≈ 4.7
- Bu devasa sicaklik farki, kacinilmaz entropi uretir

**Azaltma stratejileri:**
- Hava on isitma (combustion air preheating): alev sicakligini artirmaz ama baca kaybini azaltir
- Fazla hava optimizasyonu: daha az soguk hava → alev sicakligi artar → ΔT kismi azalir
- Yakit degisimi ile temelden degisim mumkun degil (yanma dogasi geregi)

#### 4.2.3 Isi Transfer Yuzeyleri Bejan Sayisi

Kazanin isi transfer bolgeleri icin:

| Bolge | T_sicak (°C) | T_soguk (°C) | Be | Yorum |
|---|---|---|---|---|
| Radyant bolge (Furnace) | 1800 → 1000 | 170 (buhar) | 0.98 | ΔT tamamen baskin |
| Konvektif bolge (Convective) | 1000 → 350 | 170 (buhar) | 0.95 | ΔT baskin |
| Baca gazi gecisi | 350 → 220 | 65 (besleme suyu) | 0.88 | ΔT baskin, ΔP etkisi az |

Tum bolgelerde Be > 0.85 → isi transferi tersinmezligi dominant. Ancak yanma bolgesinde ΔT'yi azaltmak pratikte sinirlidir (buhar sicakligi sabittir).

### 4.3 Cozum (Solution)

EGM bulgularina gore, yanma tersinmezligi buyuk olcude kacinilmaz oldugundan, **baca gazi kaybi** ve **yardimci kayiplar** hedeflenmistir:

#### 4.3.1 Yogusturucu Ekonomizer (Condensing Economizer)

- Paslanmaz celik (SS316L) yogusturucu ekonomizer eklenmistir
- Baca gazi sicakligi: 220 °C → 65 °C
- Su buharin yogusmasi ile ek isi geri kazanimi (latent heat recovery)
- Geri kazanilan isi: ≈ 720 kW
- Besleme suyu sicakligi: 65 °C → 95 °C

**Ekonomizer Ṡ_gen analizi:**

| Bolge | Gaz T (°C) | Su T (°C) | Ṡ_gen (kW/K) |
|---|---|---|---|
| Kuru bolge (Dry section) | 220 → 130 | 80 → 95 | 0.21 |
| Yogusma bolgesi (Condensing) | 130 → 65 | 65 → 80 | 0.15 |
| **Toplam ekonomizer** | | | **0.36** |

Eklenen Ṡ_gen (0.36 kW/K) < Kazanilan Ṡ_gen azalmasi (1.62 → 0.45 = 1.17 kW/K azalma)
**Net kazanc: 0.81 kW/K entropi uretim azalmasi**

#### 4.3.2 Fazla Hava Optimizasyonu

- O₂ sensoru ve otomatik damper kontrolu kurulmustur
- Fazla hava: %15 → %10 (O₂: %3.2 → %2.1)
- Daha az soguk hava → daha yuksek alev sicakligi → daha az baca gazi debisi
- **Sonuc:** Baca gazi debisinde %8 azalma → ek enerji tasarrufu

#### 4.3.3 Kondensat Geri Donus Optimizasyonu

- Kondensat geri donus orani: %60 → %85
- Yeni kondensat tanki ve pompasi eklenmistir
- Buhar tuzaklari (steam traps) kontrol edilmis, 8 adet degistirilmistir
- Besleme suyu sicakligi artisi → ekonomizer yukunde azalma → baca gazi daha soguk cikabilir

**Enerji etkisi:**
- Kondensat donusu ile geri kazanilan enthalpy: ≈ 380 kW
- Taze su isitmasi icin harcanan enerji azalmasi: %25

#### 4.3.4 Blowdown Optimizasyonu

- Su aritma sistemi iyilestirilmistir (yumusatma + ters ozmoz)
- Blowdown orani: %5 → %2
- Flas buhar geri kazanimi (Flash steam recovery) eklenmistir
- Flas tank basinci: 1.5 bar → %30 flas buhar → besleme suyu tanki

**Blowdown Ṡ_gen azalmasi:**
- Onceki Ṡ_gen (blowdown): 0.45 kW/K
- Sonraki Ṡ_gen (blowdown): 0.12 kW/K
- Azalma: %73

### 4.4 Sonuclar (Results)

| Parametre | Once (Before) | Sonra (After) | Degisim |
|---|---|---|---|
| Baca gazi sicakligi (°C) | 220 | 65 | −155 °C |
| Enerji verimi (LHV) | %86 | %95 | +9 puan |
| Exergy verimi | %32 | %37 | +5 puan |
| Toplam Ṡ_gen (kW/K) | 9.00 | 7.02 | **−22%** |
| Yanma Ṡ_gen (kW/K) | 5.22 | 4.95 | −5% (fazla hava opt.) |
| Baca gazi Ṡ_gen (kW/K) | 1.62 | 0.45 | −72% |
| Blowdown Ṡ_gen (kW/K) | 0.45 | 0.12 | −73% |
| Yillik yakit tasarrufu | — | %12 | — |
| Yillik tasarruf | — | €96,000 | — |
| Toplam yatirim | — | €180,000 | — |
| Geri odeme suresi | — | **1.9 yil** | — |

> **Anahtar bulgu:** Kazan exergy verimi yalnizca %32 → %37'ye cikmistir — bu sinirli gorunebilir. Ancak asil neden, yanma tersinmezliginin (%58) dogal gaz kazanlarinda buyuk olcude kacinilmaz olmasidir. EGM analizi, "nereye kadar iyilestirme yapilabilecegini" acikca gosterir ve gercekci beklentiler olusturur.

---

## Genel Cikarimlar (Cross-Case Lessons)

### Ortak Bulgular

Dort vaka calismasindaki ortak temalar:

1. **EGM, enerji analizinin goremedigi firsatlari tanimlar**
   - Genlesme vanalari (Vaka 2): Enerji analizinde gorunmez, EGM'de %38 pay
   - Kisma vanalari (Vaka 3): Enerji analizinde "basinc kontrolu", EGM'de %45 pay
   - Baca gazi (Vaka 4): Enerji analizinde "%86 verim = iyi", EGM'de %18 iyilestirme potansiyeli

2. **Genlesme/kisma (throttling) cihazlari en buyuk Ṡ_gen kaynagi**
   - Vaka 2: TXV → %38
   - Vaka 3: Kisma vanalari → %45
   - Her iki durumda da bu cihazlar enerji analizinde "kayipsiz" gorunmektedir

3. **Isi transferi tersinmezligi (ΔT) ikinci en buyuk hedef**
   - Vaka 1: On isitici ΔT optimizasyonu → %32 Ṡ_gen azalmasi (4. kademe)
   - Vaka 4: Ekonomizer eklenmesi → baca gazi Ṡ_gen %72 azalma
   - Yaklasma sicakliklarinin dusurulmesi her zaman etkili

4. **Bejan sayisi (Be) mukemmel bir teshis araci**
   - Be > 0.8: Isi transfer yuzeyini artir, yaklasma sicakligini dusur
   - Be < 0.3: Akis direncini azalt, boru boyutunu optimize et
   - 0.3 < Be < 0.8: Her iki strateji birlikte uygulanmali

5. **Yanma tersinmezligi sinirli olcude azaltilabilir**
   - Vaka 4: %58 paya ragmen yalnizca %5 azaltma mumkun
   - Temelden degistirmek icin yakit degisimi veya elektrikli isitma gerekli
   - EGM bu siniri acikca gosterir → gercekci beklenti olusturur

### Yatirim Getiri Karsilastirmasi (Investment Return Comparison)

| Vaka | Sektor | Ṡ_gen Azalma | Enerji Tasarrufu | Yatirim (€) | Geri Odeme (yil) | Spesifik Maliyet (€/kW tasarruf) |
|---|---|---|---|---|---|---|
| 1 — Cimento atik isi | Cimento | %35 | 2.5 MW elektrik | 2,800,000 | 3.5 | 1,120 |
| 2 — Sogutma retrofit | Gida | %28 | 180 MWh/yil | 25,000 | 1.4 | 1,220 |
| 3 — Boru agi | Kimya | %60 | 344 MWh/yil | 120,000 | 3.5 | 2,791 |
| 4 — Kazan optimizasyonu | Tekstil | %22 | %12 yakit | 180,000 | 1.9 | 1,875 |

**Onemli gozlemler:**
- En dusuk yatirim/en hizli geri donus: Vaka 2 (sogutma retrofit) — €25,000, 1.4 yil
- En yuksek mutlak tasarruf: Vaka 1 (cimento) — 2.5 MW, €800,000/yil
- En yuksek Ṡ_gen azalma yuzdesi: Vaka 3 (boru agi) — %60
- En sinirli iyilestirme: Vaka 4 (kazan) — %22, yanma tersinmezligi nedeniyle

### EGM Uygulama Yol Haritasi (Implementation Roadmap)

Herhangi bir endustriyel tesiste EGM uygulamasi icin onerilen adimlar:

1. **Haritalama (Mapping):** Tum bilesenler icin Ṡ_gen hesapla
2. **Onceliklendirme (Prioritization):** En buyuk Ṡ_gen payina sahip bilesenlerden basla
3. **Tani (Diagnosis):** Bejan sayisi ile mekanizmayi belirle (ΔT vs ΔP)
4. **Fizibilite (Feasibility):** Azaltilabilirlik degerlendirmesi yap (yanma gibi kacinilmaz kaynaklari ayir)
5. **Asamali Uygulama (Phased Implementation):** Dusuk maliyetli, yuksek etkili onlemlerden basla
6. **Dogrulama (Verification):** Uygulama sonrasi olcumlerle Ṡ_gen azalmasini dogrula

---

## İlgili Dosyalar (Related Files)

- `factory/entropy_generation/overview.md` — EGM genel bakis ve felsefesi
- `factory/entropy_generation/fundamentals.md` — Temel formul ve kavramlar
- `factory/entropy_generation/bejan_number.md` — Bejan sayisi detayli analiz
- `factory/entropy_generation/heat_exchanger_egm.md` — Isi degistirici EGM analizi
- `factory/entropy_generation/refrigeration_egm.md` — Sogutma sistemi EGM
- `factory/entropy_generation/pipe_flow_egm.md` — Boru akisi EGM
- `factory/case_studies.md` — Genel fabrika vaka calismalari

---

## Referanslar (References)

1. Bejan, A. *Entropy Generation Minimization*, CRC Press, 1996.
2. Bejan, A. *Advanced Engineering Thermodynamics*, 4th Edition, Wiley, 2016.
3. Madlool, N.A., Saidur, R., Hossain, M.S., Rahim, N.A. "A critical review on energy use and savings in the cement industries," *Renewable and Sustainable Energy Reviews*, 15(4), 2042–2060, 2011.
4. Atmaca, A., Yumrutas, R. "Thermodynamic and exergoeconomic analysis of a cement plant: Part I — Methodology," *Energy Conversion and Management*, 79, 790–798, 2014.
5. Acikkalp, E., Aras, H., Hepbasli, A. "Advanced exergy analysis of a trigeneration system with a diesel-gas engine operating in a refrigerator plant building," *Energy and Buildings*, 80, 268–275, 2014.
6. Tsatsaronis, G. "Recent developments in exergy analysis and exergoeconomics," *International Journal of Exergy*, 5(5-6), 489–499, 2008.
7. Dincer, I., Rosen, M.A. *Exergy: Energy, Environment and Sustainable Development*, 3rd Edition, Elsevier, 2021.
8. Bejan, A., Lorente, S. "Constructal law of design and evolution: Physics, biology, technology, and society," *Journal of Applied Physics*, 113(15), 2013.
9. Kotas, T.J. *The Exergy Method of Thermal Plant Analysis*, Butterworths, 1985.
10. Szargut, J., Morris, D.R., Steward, F.R. *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*, Hemisphere Publishing, 1988.
