---
title: "Egzoz Isı Geri Kazanımı (Dryer Exhaust Heat Recovery)"
category: dryer
equipment_type: dryer
keywords: [egzoz ısı geri kazanımı, exhaust heat recovery, ısı eşanjörü, ısı tekeri, kurutma WHR]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/psychrometrics.md, dryer/equipment/tunnel_dryer.md, dryer/equipment/belt_dryer.md, dryer/equipment/rotary_dryer.md, dryer/equipment/spray_dryer.md, dryer/solutions/air_recirculation.md, factory/waste_heat_recovery.md, factory/cross_equipment.md, factory/heat_integration.md]
use_when: ["Egzoz sıcaklığı > 80°C olduğunda", "Kurutma egzoz ısı kaybı yüksek olduğunda", "Kurutma enerji verimliliği düşük olduğunda"]
priority: high
last_updated: 2026-02-01
---
# Egzoz Isı Geri Kazanımı (Dryer Exhaust Heat Recovery)

> Son güncelleme: 2026-02-01

## Genel Bakis

**Problem:** Endüstriyel kurutucularda egzoz havasi genellikle 80-180°C sicaklikta ve yüksek nemde atmosfere atilir. Bu egzoz havasi, kurutma sürecine verilen toplam termal enerjinin %20-40'ini tasir. Sicak ve nemli egzoz havasinin dogrudan atmosfere birakilmasi ciddi bir exergy kaybi olusturur. Özellikle sürekli calisan konvektif kurutucularda bu kayip yillik bazda büyük miktarlara ulasir.

**Çözüm:** Egzoz havasinda isi geri kazanim sistemi kurularak sicak egzoz havasi ile gelen taze hava arasinda isi transferi saglanir. Taze hava ön isitilarak brülör veya isitici yükü azaltilir ve yakit tüketimi düsürülür. Farkli teknolojiler (plakali esanjör, döner isi carki, devirdaim bobini, yogusturma) farkli kosullara uygun çözümler sunar.

**Tipik Tasarruf:** %10-25 yakit tüketiminde azalma
**Tipik ROI:** 0.8-2.5 yil

## Tetikleyici Kosullar (Trigger Conditions)

Bu çözüm asagidaki kosullardan biri veya birkaçi karsilandiginda öncelikli olarak degerlendirilmelidir:

| Tetikleyici | Esik Deger | Açiklama |
|-------------|------------|----------|
| Egzoz sicakligi (T_exhaust) | > 80°C | Isil geri kazanim için minimum ekonomik esik |
| Egzoz isi kaybi orani | > %25 toplam giris enerjisi | Toplam termal girdinin önemli kismi egzozla atiliyor |
| Egzoz-ortam sicaklik farki (ΔT) | > 60°C | Yeterli sicaklik gradyani mevcut |
| Yillik çalisma süresi | > 3,000 saat/yil | Yatirim geri dönüs süresi makul |
| Kurutucu isil kapasitesi | > 100 kW | Ekonomik ölçekte tasarruf potansiyeli |
| Egzoz debisi | > 2,000 m³/h | Yeterli hava hacmi |
| Exergy verim düsüklügü | Exergy verimi < %30 | Egzoz kaybi exergy dengesini bozuyor |

### Ne Zaman Uygulanmamali

- Egzoz sicakligi < 80°C ise isi geri kazanim potansiyeli sinirlidir
- Egzoz havasi asiri kirli, yapiskan veya korozif maddeler içeriyorsa (özel tasarim gerekir)
- Kurutucunun kalan ömrü kisaysa (< 2 yil)
- Yillik çalisma süresi düsükse (< 1,500 saat/yil)
- Egzoz kanalinda yeterli montaj alani yoksa

## Teknoloji Seçenekleri (Technology Options)

### 1. Plakali Hava-Hava Isi Esanjörü (Air-to-Air Plate Heat Exchanger)

Sabit plakalaran olustulan, genellikle çapraz akisli (cross-flow) esanjör. Egzoz ve taze hava akislari birbirinden fiziksel olarak ayridir.

| Parametre | Deger |
|-----------|-------|
| Isil verimlilik (effectiveness) | %50-70 |
| Yatirim maliyeti | 20-40 €/kW geri kazanilan kapasite |
| Basinç kaybi | 100-300 Pa (her taraf) |
| Çapraz kontaminasyon riski | Yok (fiziksel ayirma) |
| Bakim gereksinimi | Düsük (yilda 2-4 kez temizlik) |
| Uygun sicaklik araligi | 80-200°C egzoz |
| Tipik ömür | 15-20 yil |

**Avantajlar:** Düsük maliyet, basit yapi, kontaminasyon riski yok, gida/ilaç sektörüne uygun.
**Dezavantajlar:** Orta verimlilik, büyük boyut (düsük isi transfer katsayisi nedeniyle), fouling durumunda verimlilik düsüsü.

### 2. Döner Isi Çarki (Rotary Heat Wheel / Thermal Wheel)

Termal kütlesi yüksek döner bir disk egzoz tarafinda isi depolar, taze hava tarafinda bu isiyi birakir.

| Parametre | Deger |
|-----------|-------|
| Isil verimlilik (effectiveness) | %70-85 |
| Yatirim maliyeti | 30-60 €/kW geri kazanilan kapasite |
| Basinç kaybi | 150-400 Pa (her taraf) |
| Çapraz kontaminasyon riski | Var (sizinti %1-5) |
| Bakim gereksinimi | Orta (yatak, conta, sürücü motor) |
| Uygun sicaklik araligi | 80-250°C egzoz |
| Tipik ömür | 15-25 yil |

**Avantajlar:** En yüksek verimlilik, kompakt boyut, hem duyulur (sensible) hem gizli (latent) isi transferi yapabilir.
**Dezavantajlar:** Çapraz kontaminasyon riski (purge sektörü ile azaltilir), hareketli parçalar (motor, yatak), gida/ilaç sektöründe sinirli kullanim.

### 3. Devirdaim Bobini (Runaround Coil System)

Iki ayri serpantin ve aralarinda dolasan bir isi tasiyici akiskan (genellikle glikol-su karisimi) kullanir.

| Parametre | Deger |
|-----------|-------|
| Isil verimlilik (effectiveness) | %40-60 |
| Yatirim maliyeti | 40-80 €/kW geri kazanilan kapasite |
| Basinç kaybi | 100-250 Pa (hava tarafi) |
| Çapraz kontaminasyon riski | Yok (tamamen ayri devreler) |
| Bakim gereksinimi | Orta (pompa, glikol, vana) |
| Uygun sicaklik araligi | 60-200°C egzoz |
| Tipik ömür | 15-20 yil |

**Avantajlar:** Egzoz ve taze hava kanallari fiziksel olarak birbirinden uzak olabilir, kontaminasyon riski sifir, esnek yerlesim.
**Dezavantajlar:** En düsük verimlilik (çift isi transferi nedeniyle), ek pompa enerji tüketimi, glikol degisim maliyeti, donma korumasinin zorunlulugu.

### 4. Yogusturma Isı Geri Kazanimi (Condensing Heat Recovery)

Egzoz havasini çig noktasinin altina sogutarak su buharinin yogusma gizli isisi dahil geri kazanim saglar.

| Parametre | Deger |
|-----------|-------|
| Isil verimlilik (effectiveness) | %80-95 (gizli isi dahil) |
| Yatirim maliyeti | 60-120 €/kW geri kazanilan kapasite |
| Basinç kaybi | 200-500 Pa |
| Çapraz kontaminasyon riski | Yok |
| Bakim gereksinimi | Yüksek (kondensat, korozyon) |
| Uygun sicaklik araligi | 60-120°C egzoz (düsük T, yüksek nem) |
| Tipik ömür | 10-15 yil |

**Avantajlar:** En yüksek toplam isi geri kazanimi (gizli isi dahil), düsük sicaklikli egzozlarda bile etkili, kondensat suyu geri kazanimi.
**Dezavantajlar:** Yüksek yatirim maliyeti, korozyon riski (asidik kondensat), kondensat yönetim sistemi gerekli, malzeme secimi kritik (paslanmaz celik veya polimer kaplamali).

### Teknoloji Karsilastirma Özeti

| Teknoloji | Verimlilik (η_HX) | Çapraz Kontaminasyon | Basinç Kaybi | Bakim | Birim Maliyet (€/kW) |
|-----------|-------------------|---------------------|--------------|-------|----------------------|
| Plakali esanjör (Plate HX) | %50-70 | Yok | Orta | Düsük | 20-40 |
| Döner isi çarki (Rotary wheel) | %70-85 | Var (%1-5 sizinti) | Düsük-Orta | Orta | 30-60 |
| Devirdaim bobini (Run-around coil) | %40-60 | Yok | Düsük | Orta | 40-80 |
| Yogusturma (Condensing HR) | %80-95 | Yok | Yüksek | Yüksek | 60-120 |

## Seçim Kriterleri — Karar Agaci (Technology Selection Decision Tree)

Asagidaki karar agaci, tesis kosullarina en uygun isi geri kazanim teknolojisini belirlemek için kullanilir:

```
[1] Egzoz havasi temiz mi? (Toz, lif, yag damlacigi yok veya düsük)
 ├─ EVET → [2] Egzoz ve taze hava kanallari yakin mi? (< 5 m mesafe)
 │   ├─ EVET → [3] Çapraz kontaminasyon kabul edilebilir mi?
 │   │   ├─ EVET → Döner isi çarki (Rotary heat wheel)
 │   │   │         ✓ En yüksek verimlilik (%70-85)
 │   │   │         ✓ Kompakt boyut
 │   │   └─ HAYIR → [4] Egzoz sicakligi < 100°C ve nem yüksek mi?
 │   │       ├─ EVET → Yogusturma isi geri kazanimi (Condensing HR)
 │   │       │         ✓ Gizli isi dahil geri kazanim
 │   │       │         ✓ Düsük T egzozlarda etkili
 │   │       └─ HAYIR → Plakali isi esanjörü (Plate HX)
 │   │                   ✓ Iyi verimlilik (%50-70)
 │   │                   ✓ Düsük maliyet ve bakim
 │   └─ HAYIR → Devirdaim bobini (Run-around coil)
 │               ✓ Uzak kanallarda çalisir
 │               ✓ Kontaminasyon riski sifir
 └─ HAYIR → [5] Kirlilik seviyesi ne düzeyde?
     ├─ ORTA (toz, hafif lif) → Plakali HX + otomatik temizlik sistemi
     │                           ✓ Genis kanatçik araligi (> 4 mm)
     │                           ✓ Üflemeli/yikamali temizlik
     └─ YÜKSEK (yapiskan, yag, agir toz) → Devirdaim bobini + kolay
                                             temizlenebilir serpantin
                                             ✓ Düz borulu serpantin (finned degil)
                                             ✓ CIP (Clean-In-Place) sistemi
```

### Sektöre Göre Önerilen Teknoloji

| Sektör | Egzoz Karakteri | Önerilen Teknoloji | Gerekçe |
|--------|-----------------|-------------------|---------|
| Gida (tahil, makarna) | Temiz, orta T | Plakali HX veya Döner çark | Çapraz kontaminasyon hassasiyeti |
| Tekstil | Lifli, orta T | Plakali HX + filtre | Lif birikimi temizlenmeli |
| Kagit/Selüloz | Lifli, yüksek nem | Yogusturma HR | Yüksek nem; gizli isi potansiyeli |
| Seramik/Tugla | Tozlu, yüksek T | Run-around coil | Kirli egzoz, uzak kanal |
| Kimya (granül, toz) | Tozlu, orta T | Run-around coil | Kontaminasyon riski, tozlu ortam |
| Ahsap/Kereste | Orta kirlilik | Plakali HX + temizlik | VOC dikkat, yangindan korunma |
| Ilaç | Çok temiz | Plakali HX | Sifir kontaminasyon zorunlu |

## Hesaplama Örnegi (Calculation Example)

### Senaryo: Bant Kurutucu (Belt Dryer) — 120°C Egzoz, 8,000 m³/h

**Giris Verileri:**

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Egzoz sicakligi (T_exhaust) | 120 | °C |
| Egzoz debisi (V_exhaust) | 8,000 | m³/h |
| Egzoz hava yogunlugu (@120°C) | 0.898 | kg/m³ |
| Kütle debisi (ṁ_air) | 8,000 × 0.898 / 3,600 = 2.0 | kg/s |
| Ortam sicakligi (T_ambient) | 20 | °C |
| Egzoz bagilinemi (RH_exhaust) | %35 | - |
| Brülör verimi (η_burner) | %90 | - |
| Yillik çalisma süresi | 6,500 | saat/yil |
| Dogal gaz fiyati | 0.045 | €/kWh |

### Adim 1: Mevcut Egzoz Isi Kaybi

```
Q_exhaust_sensible = ṁ_air × Cp_air × (T_exhaust - T_ambient)
                   = 2.0 × 1.005 × (120 - 20)
                   = 201.0 kW (duyulur isi kaybi)
```

### Adim 2: Teknoloji Bazinda Geri Kazanim Hesabi

**Seçenek A — Plakali Esanjör (η_HX = %60):**
```
T_fresh_preheated = T_ambient + η_HX × (T_exhaust - T_ambient)
                  = 20 + 0.60 × (120 - 20) = 80°C

Q_recovered = ṁ_air × Cp_air × (T_fresh_preheated - T_ambient)
            = 2.0 × 1.005 × (80 - 20) = 120.6 kW

Fuel_saving = Q_recovered / η_burner = 120.6 / 0.90 = 134.0 kW esdeger
```

**Seçenek B — Döner Isi Çarki (η_HX = %78):**
```
T_fresh_preheated = 20 + 0.78 × (120 - 20) = 98°C

Q_recovered = 2.0 × 1.005 × (98 - 20) = 156.8 kW

Fuel_saving = 156.8 / 0.90 = 174.2 kW esdeger
```

**Seçenek C — Devirdaim Bobini (η_HX = %50):**
```
T_fresh_preheated = 20 + 0.50 × (120 - 20) = 70°C

Q_recovered = 2.0 × 1.005 × (70 - 20) = 100.5 kW

Fuel_saving = 100.5 / 0.90 = 111.7 kW esdeger
```

### Adim 3: Yillik Tasarruf Karsilastirmasi

| Teknoloji | Q_recovered [kW] | Yakit Tasarrufu [kW] | Yillik Tasarruf [kWh/yil] | Yillik Maliyet Tasarrufu [€/yil] |
|-----------|------------------|---------------------|--------------------------|----------------------------------|
| Plakali HX (%60) | 120.6 | 134.0 | 871,000 | 39,195 |
| Döner çark (%78) | 156.8 | 174.2 | 1,132,300 | 50,954 |
| Run-around (%50) | 100.5 | 111.7 | 726,050 | 32,672 |

### Adim 4: Exergy Perspektifi

Egzoz havasinin exergy içerigi sadece sicakliga degil, termodinamik kaliteye baglidir:

```
Ex_thermal = ṁ × Cp × [(T_exhaust - T0) - T0 × ln(T_exhaust/T0)]

T0 = 293 K (20°C), T_exhaust = 393 K (120°C):
Ex_thermal = 2.0 × 1.005 × [(120 - 20) - 293 × ln(393/293)]
           = 2.01 × [100 - 293 × 0.2936]
           = 2.01 × [100 - 86.03]
           = 2.01 × 13.97
           = 28.08 kW exergy
```

201 kW enerji kaybina karsilik yalnizca 28 kW exergy kaybi vardir. Bu, egzoz isisinin düsük termodinamik kalitede (düsük sicaklikta) oldugunu gösterir. Ancak bu exergy sifir maliyetle geri kazanildigi için ekonomik degeri yüksektir ve Carnot siniri içinde kullanimi verimlidir.

## Yatirim Maliyeti ve ROI (Investment Cost and Return)

### Yatirim Maliyeti Tablosu — Kurutucu Kapasitesine Göre

| Kurutucu Kapasitesi | Plakali HX [€] | Döner Çark [€] | Run-Around Coil [€] | Yogusturma HR [€] |
|--------------------|-----------------|-----------------|---------------------|-------------------|
| 50-100 kW | 8,000-15,000 | 12,000-20,000 | 10,000-18,000 | 15,000-25,000 |
| 100-300 kW | 15,000-25,000 | 20,000-35,000 | 18,000-30,000 | 30,000-50,000 |
| 300-500 kW | 25,000-35,000 | 30,000-45,000 | 28,000-40,000 | 45,000-70,000 |
| 500-1,000 kW | 35,000-50,000 | 40,000-60,000 | 38,000-55,000 | 60,000-100,000 |

**Not:** Maliyetler montaj, kanal modifikasyonu, kontrol sistemi ve devreye alma dahildir. Yogusturma HR maliyetine kondensat yönetim sistemi dahildir.

### ROI Hesabi — Yukaridaki Örnek Senaryo (Belt Dryer, 300 kW sinifi)

| Teknoloji | Yatirim [€] | Yillik Tasarruf [€/yil] | Geri Ödeme Süresi (SPP) [yil] | 5 Yillik Net Kazanç [€] |
|-----------|-------------|------------------------|------------------------------|--------------------------|
| Plakali HX | 25,000 | 39,195 | 0.64 | 170,975 |
| Döner çark | 35,000 | 50,954 | 0.69 | 219,770 |
| Run-around coil | 30,000 | 32,672 | 0.92 | 133,360 |
| Yogusturma HR | 50,000 | 55,000* | 0.91 | 225,000 |

*Yogusturma HR, gizli isi geri kazanimi ile ek %10-15 tasarruf saglar (nem yüksekse).

### Kurutucu Tipine Göre ROI Beklentisi

| Kurutucu Tipi | Tipik Egzoz T [°C] | En Uygun Teknoloji | Tipik SPP [yil] |
|--------------|--------------------|--------------------|-----------------|
| Bant kurutucu (Belt dryer) | 80-140 | Plakali HX / Döner çark | 0.6-1.5 |
| Tünel kurutucu (Tunnel dryer) | 70-120 | Plakali HX / Yogusturma | 0.8-2.0 |
| Döner kurutucu (Rotary dryer) | 100-200 | Döner çark / Plakali HX | 0.8-1.8 |
| Sprey kurutucu (Spray dryer) | 80-120 | Run-around coil / Plakali HX | 1.0-2.5 |
| Akiskan yatak (Fluidized bed) | 60-100 | Yogusturma HR / Plakali HX | 1.2-2.5 |

## Uygulama Adimlari (Step-by-Step Implementation)

### Faz 1 — Ön Degerlendirme (1-2 hafta)

1. **Egzoz karakterizasyonu:** Egzoz havasi sicakligini, debisini, nem içerigini ve kirlilik seviyesini ölç. En az 1 hafta boyunca sürekli veri kaydet. Farkli ürün ve yük kosullarinda ölçüm yap
2. **Çig noktasi analizi:** Egzoz havasinin su çig noktasini ve varsa asit çig noktasini hesapla. Isi esanjörü çikis sicakliginin çig noktasinin üzerinde kalmasini sagla
3. **Enerji denetimi:** Mevcut kurutucu enerji tüketimini, exergy verimini ve egzoz kayip oranini belirle. Benchmark degerleriyle karsilastir

### Faz 2 — Teknoloji Seçimi ve Tasarim (2-4 hafta)

4. **Teknoloji seçimi:** Karar agacini (yukaridaki bölüm) kullanarak proses gereksinimlerine, çapraz kontaminasyon riskine ve montaj alanina göre uygun isi esanjörü tipini belirle
5. **Termal tasarim:** NTU-etkinlik (NTU-effectiveness) veya LMTD yöntemiyle isi esanjörünü boyutlandir. Fouling faktörünü dahil et (kurutma egzozlari için tipik fouling faktörü: 0.002-0.005 m²·K/W)
6. **Basinç kaybi hesabi:** Egzoz ve taze hava tarafindaki basinç kayiplarini hesapla. Mevcut fan kapasitesinin yeterlilgini kontrol et; gerekirse fan güçlendirmesi veya VFD eklenmesini planla
7. **Kanal tasarimi:** Egzoz ve taze hava kanallarinin esanjöre baglanti noktalarini tasarla. Damper sistemi ile by-pass hatti ekle (by-pass, bakim ve düsük yük kosullari için zorunludur)

### Faz 3 — Detay Mühendislik (2-3 hafta)

8. **Malzeme seçimi:** Egzoz sicakligi, nemi ve kirlilik içerigine göre uygun esanjör malzemesini belirle:
   - Standart: Alüminyum kanatçikli galvaniz çelik
   - Korozif ortam: AISI 316L paslanmaz çelik
   - Asidik kondensat: Polimer kaplamali veya cam kaplamali
9. **Temizlik sistemi tasarimi:** Fouling riskine göre temizlik çözümünü belirle:
   - Düsük kirlilik: Yüksek basinçli hava üfleme (soot blowing)
   - Orta kirlilik: Su ile yikama (wash-down) sistemi
   - Yüksek kirlilik: CIP (Clean-In-Place) kimyasal yikama
10. **Kontrol sistemi:** Damper pozisyonu, fan hizi ve sicaklik kontrolü için otomasyon sistemi tasarla. Çig noktasi altina düsme durumunda by-pass otomatik olarak devreye girmelidir

### Faz 4 — Montaj ve Devreye Alma (2-4 hafta)

11. **Tedarik ve montaj:** Esanjör ünitesini, kanallari, damperleri, sensörleri ve kontrol panelini temin et ve monte et. Kurutucu durus süresini minimize etmek için ön montaj (prefabrikasyon) yap
12. **Devreye alma:** Sistemi asamali olarak devreye al. Sicaklik, basinç ve debi sensörlerini kalibre et. By-pass damperini test et
13. **Performans dogrulama:** Devreye alma sonrasi en az 2 hafta veri toplayarak tasarrufu dogrula. Beklenen Q_recovered degeri ile ölçülen degeri karsilastir. Sapma > %15 ise kök neden analizi yap

### Faz 5 — Izleme ve Optimizasyon (sürekli)

14. **Sürekli izleme:** Isi esanjörü girsi/çikis sicakliklarini, basinç kayiplarini ve geri kazanim oranini sürekli izle. Verimlilik düsüsü fouling göstergesidir
15. **Bakim programi:** Planlanan periyodik temizlik ve bakim takvimini olustur. Fouling trendi ile temizlik araligini optimize et

## Riskler ve Dikkat Edilecekler (Risks and Considerations)

| Risk | Açiklama | Önlem |
|------|----------|-------|
| Fouling (kirlenme) | Kurutma egzozundaki toz, lif (lint), yag damlaciklari esanjör yüzeyinde birikerek verimliligi düsürür | Düzenli temizlik programi; otomatik üfleme sistemi; uygun kanatçik araligi (> 3 mm); basinç kaybi izleme ile fouling tespiti |
| Yogusma ve korozyon (Condensation) | Egzoz havasi çig noktasinin altina sogursa yogusma olusur; asidik bilesenlerin varliginda sülfürik/hidroklorik asit korozyonu baslar | Esanjör çikis sicakligini çig noktasinin en az 10-15°C üzerinde tut; by-pass damper sistemi kur; malzeme seçimini buna göre yap |
| Asit çig noktasi (Acid dew point) | Bazi kurutma proseslerinde egzozda HCl, SO₂ veya organik asitler bulunabilir; yogusma halinde agresif korozyon baslar | Egzoz gaz analizi yap; asit çig noktasi hesapla; minimum esanjör çikis sicakligini buna göre ayarla; paslanmaz çelik veya polimer kaplamali malzeme kullan |
| Çapraz kontaminasyon | Döner çark sistemlerinde egzoz kirlilginin taze havaya geçme riski | Gida/ilaç sektöründe plakali esanjör veya run-around coil tercih et; döner çarkta purge sektörü kullan (sizintiyi %0.5'in altina düsürür) |
| Basinç kaybi (Pressure drop) | Esanjör ek basinç kaybi yaratir; mevcut fan yetmeyebilir | Tasarim asamasinda fan kapasitesini dogrula; VFD (Variable Frequency Drive) ekle; ek fan enerjisini tasarruftan düs |
| Yangin riski | Kurutma egzozundaki yanici toz veya buharlarin esanjörde birikmesi | Yangin söndürme sistemi; sicaklik alarmlari; ATEX sertifikali ekipman (gerekiyorsa); düzenli temizlik |
| Düsük yük performansi | Düsük yükte egzoz sicakligi ve debisi azalir, geri kazanim düser | Modülasyon kontrolü; minimum by-pass ayari; kademeli (staged) kontrol |
| Mevsimsel etki | Yaz aylarinda taze hava sicakligi yükselir, ΔT düser, geri kazanim azalir | ROI hesabinda yillik ortalama kosullari kullan; mevsimsel düzeltme uygula |
| Kondensat yönetimi | Yogusturma sistemlerinde kondensat toplama, aritma ve desarj gereklidir | Kondensat toplama tavasi, nötralizasyon tanki (pH 6-9 arasi desarj); yönetmeliklere uygun desarj |

### Basinç Kaybi Yönetimi — Detay

Isi esanjörünün yaratacagi ek basinç kaybi, fan enerji tüketimini arttirir. Bu ek tüketiminm tasarruftan düsülmesi gerekir:

```
P_fan_additional = V̇ × ΔP_HX / (η_fan × 1000) [kW]

Örnek: 8,000 m³/h debi, 250 Pa ek basinç kaybi, %65 fan verimi
P_fan_additional = (8000/3600) × 250 / (0.65 × 1000) = 0.85 kW

Yillik ek fan enerjisi = 0.85 × 6,500 = 5,525 kWh/yil
Ek maliyet (@0.12 €/kWh elektrik) = €663/yil
```

Bu deger, yillik ~39,000 €/yil tasarrufun yalnizca %1.7'sidir; ihmal edilebilir düzeydedir.

## Tipik Tasarruf Özeti (Typical Savings Summary)

| Parametre | Deger Araligi |
|-----------|---------------|
| Enerji tasarruf orani | %10-25 (toplam kurutucu enerjisinde) |
| Geri ödeme süresi (SPP) | 0.8-2.5 yil |
| Yillik CO₂ azaltimi | 50-300 ton CO₂/yil (tesise bagli) |
| Esanjör ömrü | 10-25 yil (teknoloji ve bakima bagli) |
| Ek fan enerji tüketimi | Tasarrufun %1-3'ü (net tasarrufu minimal etkiler) |

### Kombine Uygulama Potansiyeli

Egzoz isi geri kazanimi, diger kurutma optimizasyonlariyla birlikte uygulandiginda sinerjik etkiler olusturur:

| Kombine Çözüm | Ek Tasarruf | Toplam Tasarruf |
|---------------|-------------|-----------------|
| Egzoz HR + Hava geri deviri (Recirculation) | +%5-10 | %20-35 |
| Egzoz HR + Sicaklik optimizasyonu | +%3-8 | %15-30 |
| Egzoz HR + Mekanik ön su alma (Dewatering) | +%10-20 | %25-40 |
| Egzoz HR + Isi pompasi retrofit | +%15-30 | %30-50 |

## İlgili Dosyalar

- Kurutucu exergy formülleri: `dryer/formulas.md`
- Kurutucu benchmarklari: `dryer/benchmarks.md`
- Psikrometrik hesaplamalar: `dryer/psychrometrics.md`
- Tünel kurutucu: `dryer/equipment/tunnel_dryer.md`
- Bant kurutucu: `dryer/equipment/belt_dryer.md`
- Döner kurutucu: `dryer/equipment/rotary_dryer.md`
- Sprey kurutucu: `dryer/equipment/spray_dryer.md`
- Hava geri deviri çözümü: `dryer/solutions/air_recirculation.md`
- Isi pompasi retrofit: `dryer/solutions/heat_pump_retrofit.md`
- Fabrika atik isi geri kazanimi: `factory/waste_heat_recovery.md`
- Fabrika çapraz ekipman firsatlari: `factory/cross_equipment.md`
- Fabrika isi entegrasyonu: `factory/heat_integration.md`

## Referanslar

- Mujumdar, A.S., "Handbook of Industrial Drying," 4th Edition, CRC Press — Heat Recovery Systems Chapter
- US DOE/AMO, "Improving Process Heating System Performance: A Sourcebook for Industry," 3rd Edition
- Carbon Trust, "Industrial Energy Efficiency — Heat Recovery," Guide CTG018
- EU BREF (Best Available Techniques Reference Document), "Energy Efficiency," Chapter 3: Heat Recovery Techniques
- Kemp, I.C., "Reducing Dryer Energy Use by Process Integration Techniques," Drying Technology, Vol. 30
- Strumillo, C., Jones, P.L., Zylla, R., "Energy Aspects in Drying," Handbook of Industrial Drying, 4th Ed.
- ASHRAE Handbook — HVAC Systems and Equipment, Heat Recovery Chapter
- Bahu, R.E., "Energy Considerations in Dryer Design," Drying Technology Journal, Vol. 9, No. 4
- IEA Industrial Energy Technology and Systems Analysis (ETSAP), "Industrial Drying — Technology Brief"
- Perry's Chemical Engineers' Handbook, 9th Edition — Section 12: Psychrometry, Evaporative Cooling, and Solids Drying
- EN 1886, "Ventilation for Buildings — Air Handling Units — Mechanical Performance"
- Kudra, T., Mujumdar, A.S., "Advanced Drying Technologies," 2nd Edition, CRC Press — Chapter on Heat Recovery
