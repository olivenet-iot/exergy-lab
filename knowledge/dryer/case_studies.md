---
title: "Kurutma Fırını Vaka Çalışmaları (Industrial Dryer Case Studies)"
category: dryer
equipment_type: dryer
keywords:
  - vaka çalışması
  - case study
  - uygulama örneği
  - önce/sonra
  - enerji tasarrufu
related_files:
  - dryer/formulas.md
  - dryer/benchmarks.md
  - dryer/solutions/exhaust_heat_recovery.md
  - dryer/solutions/air_recirculation.md
  - dryer/solutions/heat_pump_retrofit.md
  - dryer/solutions/mechanical_dewatering.md
  - dryer/sectors/food_drying.md
  - dryer/sectors/paper_drying.md
  - dryer/sectors/textile_drying.md
  - dryer/sectors/ceramic_drying.md
  - dryer/sectors/wood_drying.md
  - factory/case_studies.md
use_when:
  - "Kurutma vaka çalışmaları referans alınırken"
  - "Benzer uygulama örnekleri aranırken"
priority: low
last_updated: 2026-02-01
---

# Kurutma Fırını Vaka Çalışmaları (Industrial Dryer Case Studies)

## Genel Bakış

Bu dokuman, farklı sektorlerdeki kurutma sistemlerinde uygulanan enerji verimliligi iyilestirmelerini belgeleyen 5 detayli vaka calismasi icermektedir. Her vaka calismasi; tesis profili, mevcut durum (before), uygulanan onlemler, sonuclar (after), ekonomik degerlendirme ve ogrenilenler dersler bolumlerini icerir.

Vaka calismalari, ExergyLab platformundaki AI yorumlama sisteminin kullanicilara benzer tesislerle karsilastirmali oneriler sunmasi icin referans olarak kullanilir. Enerji verimi yerine **exergy verimi** odakli analiz yaklasimi her vakada vurgulanmaktadir.

**Kapsanan sektorler:**
- Gida (sut tozu — sprey kurutucu)
- Tekstil (stenter)
- Ahsap / kereste (isı pompasi retrofit)
- Seramik (karo — firin-kurutucu entegrasyonu)
- Gida (sebze — cok onlemli paket)

**Temel metrikler:** SEC (Specific Energy Consumption — spesifik enerji tuketimi, kJ/kg su), SMER (Specific Moisture Extraction Rate — spesifik nem uzaklastirma orani, kg/kWh), exergy verimi (%), yatirim (EUR), basit geri odeme suresi (SPP — Simple Payback Period, yil).

---

## Vaka 1: Sut Tozu Fabrikasi — Sprey Kurutucu Iyilestirme (Spray Dryer Optimization)

### Tesis Profili

| Parametre | Deger |
|-----------|-------|
| Sektor | Gida — sut tozu uretimi (dairy — milk powder) |
| Kurutucu tipi | Sprey kurutucu (spray dryer) |
| Uretim kapasitesi | 2,500 kg sut tozu/saat |
| Besleme | Konsantre sut (%48 kati madde) |
| Calisma suresi | 7,200 saat/yil |
| Enerji kaynagi | Dogal gaz (direkt hava isitma) |
| Kurulum yili | 2012 |
| Konum | Orta Anadolu, Turkiye |

### Mevcut Durum (Before)

Tesisin sprey kurutucu sistemi tek kademeli calisiyor, giris havasi 220 °C, egzoz havasi 95 °C sicaklikta dogrudan atmosfere atiliyordu. Atomizasyon noktasinda optimize edilmemis nozu tasarimi nedeniyle damlacik boyut dagilimi genisti ve kurutma homojenitesi dusuktu. Egzoz hava debisi yaklasik 55,000 Nm3/h olup, isi geri kazanim sistemi bulunmuyordu.

| Parametre | Deger |
|-----------|-------|
| Giris havasi sicakligi | 220 °C |
| Egzoz havasi sicakligi | 95 °C |
| SEC (Specific Energy Consumption) | 5,200 kJ/kg su |
| SMER (Specific Moisture Extraction Rate) | 0.48 kg/kWh |
| Exergy verimi | 5.2% |
| Enerji verimi | 43% |
| Yillik dogal gaz tuketimi | 14,200 MWh/yil |
| Yillik enerji maliyeti | 710,000 EUR/yil |
| Egzoz isi kaybi | Toplam girdinin ~%35'i |

**Exergy analizi degerlendirmesi:** %5.2 exergy verimi, sprey kurutucular icin "ortalamanin alti" sinifina karsilik gelmektedir (benchmark: %5-10 tipik, >%10 iyi). Yuksek sicaklikli giris havasi (220 °C) dusuk sicaklikli buharlasmaya (~65 °C) kullanildigi icin buyuk exergy yikimi olusuyordu. Egzoz havasi 95 °C sicaklikta atilmasi, geri kazanilabilir exergy kaybinin ana kaynagiydi.

### Uygulanan Onlemler

Uc asamali iyilestirme programi uygulandi:

**Onlem 1: Egzoz Isi Geri Kazanimi (Exhaust Heat Recovery)**
- Regeneratif donerli isi degistirici (rotary heat wheel) kurulumu
- Egzoz havasi 95 °C'den 58 °C'ye sogutuldu
- Giris taze havasi 15 °C'den 52 °C'ye on isitildi
- Geri kazanilan isi gucu: 480 kW
- Paslanmaz celik rotor, gida uyumlu malzeme (AISI 316L)
- Otomatik temizleme sistemi (sut tozu fouling onleme)

**Onlem 2: Iki Kademeli Kurutma (2-Stage: Spray + Fluidized Bed Dryer — FBD)**
- Sprey kurutucu cikisinda ek akiskan yatak kurutucu (FBD) eklendi
- Sprey kurutucu cikis nemi: %6-8 (onceki: %3.5 hedef)
- FBD ile son kurutma: %6-8'den %3.5'a
- FBD giris havasi: 85 °C (dusuk exergy enerji yeterli)
- Sprey kurutucu egzoz sicakligi 95 °C'den 80 °C'ye dustu (daha az kurutma yuku)

**Onlem 3: Optimize Edilmis Atomizasyon (Optimized Atomization)**
- Basinc nozulu yerine iki akiskanlı nozul (two-fluid nozzle) sistemi
- Damlacik boyutu dagilimi daraltildi (CV: %35'ten %18'e)
- Daha homojen kurutma, daha az asiri kurutma kaybi
- Toz kalitesi iyilesmesi (yogunluk, cozunurluk)

### Sonuclar (After)

| Parametre | Oncesi | Sonrasi | Degisim |
|-----------|--------|---------|---------|
| SEC | 5,200 kJ/kg su | 3,800 kJ/kg su | -%26.9 |
| SMER | 0.48 kg/kWh | 0.66 kg/kWh | +%37.5 |
| Exergy verimi | 5.2% | 7.8% | +2.6 puan |
| Enerji verimi | 43% | 59% | +16 puan |
| Giris havasi sicakligi | 220 °C | 220 °C | Degisim yok |
| Sprey kurutucu egzoz sicakligi | 95 °C | 80 °C | -15 °C |
| Nihai egzoz sicakligi (baca) | 95 °C | 58 °C | -37 °C |
| Yillik dogal gaz tuketimi | 14,200 MWh/yil | 10,380 MWh/yil | -3,820 MWh/yil |
| Yillik enerji maliyeti | 710,000 EUR/yil | 519,000 EUR/yil | -191,000 EUR/yil |
| CO2 emisyonu azaltma | — | 770 ton/yil | — |

### Ekonomik Degerlendirme

| Parametre | Deger |
|-----------|-------|
| Onlem 1 — Regeneratif isi degistirici | 85,000 EUR |
| Onlem 2 — FBD eklenmesi | 72,000 EUR |
| Onlem 3 — Nozul degisimi + kontrol | 23,000 EUR |
| Toplam yatirim | 180,000 EUR |
| Yillik brut tasarruf (enerji) | 191,000 EUR/yil |
| Ek isletme maliyeti (FBD elektrik, bakim) | -96,000 EUR/yil |
| Yillik net tasarruf | 95,000 EUR/yil |
| Basit geri odeme suresi (SPP) | 1.9 yil |
| NPV (10 yil, %8 iskonto orani) | 458,000 EUR |
| IRR (Internal Rate of Return) | 48% |

### Ogrenilenler Dersler

1. **Regeneratif donerli isi degistirici**, sprey kurutucu icin en etkin egzoz isi geri kazanim yontemidir; plakali isi degistiriciye gore fouling toleransi daha yuksektir.
2. **Iki kademeli kurutma** (sprey + FBD), tek kademeli sprey kurutucuya gore %20-30 enerji tasarrufu saglar. Ikinci kademe dusuk exergy enerji ile calisabilir, bu da exergy verimini arttirir.
3. **Atomizasyon optimizasyonu** dogrudan enerji tasarrufu saglamazken, homojen kurutma ile asiri kurutma kaybini %3-5 azaltir ve urun kalitesini iyilestirir.
4. Sut tozu sprey kurutucularinda egzoz fouling (sut tozu birikimi) ciddi risktir; otomatik CIP temizleme sistemi zorunludur.
5. Exergy verimi %5.2'den %7.8'e cikti; ancak sprey kurutucunun inherent yuksek sicaklik farki nedeniyle %10'u asmak zordur — bu siniri asmak icin isi pompasi entegrasyonu gerekir.

---

## Vaka 2: Tekstil Fabrikasi — Stenter Optimizasyonu (Stenter Frame Optimization)

### Tesis Profili

| Parametre | Deger |
|-----------|-------|
| Sektor | Tekstil — boyama ve terbiye (dyeing & finishing) |
| Kurutucu tipi | 10 odali gaz yakitli stenter (gas-fired tenter frame) |
| Kumas genisligi | 1.8 m |
| Calisma hizi | 35 m/min |
| Calisma suresi | 6,000 saat/yil |
| Enerji kaynagi | Dogal gaz (direkt yakici — direct-fired burner) |
| Toplam termal kapasite | 1,600 kW |
| Kurulum yili | 2008 |
| Konum | Bursa, Turkiye |

### Mevcut Durum (Before)

Stenter, 180 °C giris havasi sicakliginda calisiyor, egzoz havasi dogrudan bacadan atiliyordu. Isi geri kazanim sistemi bulunmuyordu. Brulor tunning yapilmamisti ve hava/yakit orani optimum degerin %15 uzerindeydi. Kumas hizi sabit ayarliydi (urun tipi farketmeksizin). Mangle (sikma) silindirlerinin basinci dusuktu, kumaslar stentere yuksek nemle giriyordu.

| Parametre | Deger |
|-----------|-------|
| Giris havasi sicakligi | 180 °C |
| Egzoz havasi sicakligi | 145 °C |
| SEC | 5,500 kJ/kg su |
| SMER | 0.45 kg/kWh |
| Exergy verimi | 6.1% |
| Enerji verimi | 41% |
| Resirkulasyon orani | %50 |
| Mangle cikis nemi | %65 (yasbaz) |
| Yillik dogal gaz tuketimi | 9,600 MWh/yil |
| Yillik enerji maliyeti | 480,000 EUR/yil |
| Egzoz VOC emisyonu | 380 mg/Nm3 |

**Exergy analizi degerlendirmesi:** %6.1 exergy verimi, tekstil stenterleri icin "ortalamanin alti" sinifinda (%5-10 tipik). Egzoz sicakligi 145 °C ile "kritik" seviyedeydi (benchmark: >150 °C asiri, 120-150 °C kotu). Resirkulasyon orani %50 ile dusuktu.

### Uygulanan Onlemler

Dort asamali iyilestirme paketi uygulandi:

**Onlem 1: Egzoz Isi Geri Kazanimi (Plate Heat Exchanger)**
- Paslanmaz celik plakali isi degistirici (plate HX) kurulumu
- Egzoz havasi 145 °C'den 90 °C'ye sogutuldu
- Taze hava 15 °C'den 72 °C'ye on isitildi
- Geri kazanilan isi gucu: 320 kW
- Otomatik temizleme sistemi (oligomer ve yag fouling icin)

**Onlem 2: Brulor Ayari (Burner Tuning)**
- Hava/yakit orani optimize edildi (fazla hava: %15'ten %5'e)
- O2 analiz cihazi ve otomatik trim kontrolu eklendi
- Yanma verimi: %88'den %94'e

**Onlem 3: Hiz Optimizasyonu (Speed Optimization)**
- Urun tipine gore degisken hiz profili tanimlandi
- Hafif kumaslar: 45 m/min (onceki: 35 m/min — gerekmedigindu yavas calisiyor)
- Agir kumaslar: 25 m/min (yeterli kurutma icin)
- VFD (Variable Frequency Drive) ile konveyor ve fan hiz kontrolu

**Onlem 4: Mangle Iyilestirmesi (Mangle/Padder Improvement)**
- Mangle silindir basinci artirildi (2 bar'dan 4 bar'a)
- Silindirler yenilendi (sertlik: Shore 65'ten Shore 80'e)
- Kumas giris nemi: %65'ten %55'e dustu (yasbaz)
- Termal kurutma yuku %28 azaldi

### Sonuclar (After)

| Parametre | Oncesi | Sonrasi | Degisim |
|-----------|--------|---------|---------|
| SEC | 5,500 kJ/kg su | 3,600 kJ/kg su | -%34.5 |
| SMER | 0.45 kg/kWh | 0.69 kg/kWh | +%53.3 |
| Exergy verimi | 6.1% | 9.8% | +3.7 puan |
| Enerji verimi | 41% | 63% | +22 puan |
| Egzoz sicakligi (baca) | 145 °C | 90 °C | -55 °C |
| Resirkulasyon orani | %50 | %50 | Degisim yok (bu projede degistirilmedi) |
| Mangle cikis nemi | %65 | %55 | -10 puan |
| Yillik dogal gaz tuketimi | 9,600 MWh/yil | 6,280 MWh/yil | -3,320 MWh/yil |
| Yillik enerji maliyeti | 480,000 EUR/yil | 314,000 EUR/yil | -166,000 EUR/yil |
| VOC emisyonu | 380 mg/Nm3 | 220 mg/Nm3 | -%42 |
| CO2 emisyonu azaltma | — | 670 ton/yil | — |

**Not:** Egzoz debisi de azaldigi icin VOC konsantrasyonu azaldi ve toplam VOC emisyonu daha da dusuk oldu.

### Ekonomik Degerlendirme

| Parametre | Deger |
|-----------|-------|
| Onlem 1 — Plakali isi degistirici + temizleme | 35,000 EUR |
| Onlem 2 — Brulor tunning + O2 kontrol | 8,000 EUR |
| Onlem 3 — VFD + hiz kontrol sistemi | 12,000 EUR |
| Onlem 4 — Mangle silindir yenileme | 10,000 EUR |
| Toplam yatirim | 65,000 EUR |
| Yillik brut tasarruf (enerji) | 166,000 EUR/yil |
| Ek isletme maliyeti (bakim, elektrik) | -124,000 EUR/yil |
| Yillik net tasarruf | 42,000 EUR/yil |
| Basit geri odeme suresi (SPP) | 1.5 yil |
| NPV (10 yil, %8 iskonto orani) | 217,000 EUR |
| IRR | 58% |

### Ogrenilenler Dersler

1. **Mangle iyilestirmesi** en dusuk maliyetli onlemdir (%28 termal yuk azaltma, 10,000 EUR yatirim). Mekanik su alma, termal kurutmadan 50-70 kat daha exergy-verimlidir.
2. **Stenter egzozunda oligomer fouling** en buyuk operasyonel zorluktur. Otomatik temizleme olmadan isi degistirici verimi 3-6 ay icinde %50'ye duser.
3. **Brulor tunning** neredeyse sifir maliyetle %5-8 yakit tasarrufu saglar; ancak duzenli bakim gerektirir (yilda 2 kez).
4. **Hiz optimizasyonu** urun kalitesini iyilestirir (dusuk gramajli kumaslar icin daha yuksek hiz, uniform kurutma) ve enerji tasarrufu saglar.
5. Resirkulasyon orani bu projede degistirilmedi; %50'den %70-75'e cikarilmasi ek %10-15 tasarruf potansiyeli tasimaktadir (gelecek faz).

---

## Vaka 3: Kereste Kurutma — Isi Pompasi Retrofit (Heat Pump Kiln Retrofit)

### Tesis Profili

| Parametre | Deger |
|-----------|-------|
| Sektor | Ahsap isleme — kereste kurutma (wood drying) |
| Kurutucu tipi | Geleneksel buhar isitmali firin (conventional steam-heated kiln) |
| Firin kapasitesi | 60 m3 kereste / batch |
| Batch suresi (cam kerestesi, 50 mm) | 10 gun |
| Yillik uretim | 30 batch/yil = 1,800 m3/yil |
| Calisma suresi | 7,000 saat/yil |
| Enerji kaynagi | Dogal gaz yakitli buhar kazani (%85 kazan verimi) |
| Kurutma sicakligi | 70 °C (geleneksel program) |
| Kurulum yili | 2005 |
| Konum | Bolu, Turkiye |

### Mevcut Durum (Before)

Geleneksel buhar serpantinli firin, dogal gaz yakitli kazan ile beslenmekteydi. Kurutma programi sabit 70 °C'de calisiyor, egzoz hava penceresi (vent) surekli acik tutuluyor, nem kontrolu basit on/off histerezis ile yapiliyordu. Firin yalitimi zayiflamis, yuzey sicakliklari IR termografi ile 45-55 °C olarak olculmustu.

| Parametre | Deger |
|-----------|-------|
| Kurutma sicakligi | 70 °C |
| SEC | 4,000 kJ/kg su |
| SMER | 0.60 kg/kWh |
| Exergy verimi | 8.5% |
| Enerji verimi | 56% |
| Yillik enerji tuketimi (termal) | 1,050 MWh/yil |
| Yillik enerji maliyeti | 78,000 EUR/yil |
| Kurutma kusur orani (catla, egri) | %4.5 |
| Kereste giris nemi | %55-65 (yasbaz, ortalama %60) |
| Kereste cikis nemi | %10-12 (yasbaz) |

**Exergy analizi degerlendirmesi:** %8.5 exergy verimi, konvansiyonel kereste firinlari icin "ortalama" sinifindadir (%5-10 tipik). Kurutma 70 °C'de gerceklesirken enerji kaynagi dogal gaz (kimyasal exergy faktoru ~1.04) olmasi, buyuk bir exergy kalite uyumsuzlugu (mismatch) yaratiyordu. Bu vakada isi pompasi retrofit icin ideal bir aday profili mevcuttu: dusuk kurutma sicakligi, kapali alan, uzun batch suresi.

### Uygulanan Onlemler

Tam isi pompasi retrofit uygulandi:

**Ana Onlem: Isi Pompali Nem Alma Retrofit (Heat Pump Dehumidification Retrofit)**
- Buhar serpantin sistemi sokuldu
- Kapali devre isi pompali kurutma sistemi (closed-loop heat pump dehumidification) kuruldu
- Evaporator: Firin icindeki nemli havayi sogutarak nemi yogusturur
- Kondenser: Sogutulmus havayi yeniden isitir ve firina geri gonderir
- Sogutucu akiskan: R-134a
- Isitma kapasitesi: 95 kW (kondenser)
- Sogutma kapasitesi: 68 kW (evaporator)
- Kompresor elektrik tuketimi: 28 kW
- Fanlar: 7 kW
- Toplam elektrik tuketimi: 35 kW
- Ortalama COP: 3.4
- Kurutma sicakligi: 50 °C (program optimize edildi)
- Gelismis PLC kontrol sistemi (nem, sicaklik, denge nemi bazli)

### Sonuclar (After)

| Parametre | Oncesi | Sonrasi | Degisim |
|-----------|--------|---------|---------|
| SEC | 4,000 kJ/kg su | 1,200 kJ/kg su | -%70 |
| SMER | 0.60 kg/kWh | 2.50 kg/kWh | +%317 |
| Exergy verimi | 8.5% | 22.0% | +13.5 puan |
| Enerji verimi | 56% | 78% | +22 puan |
| Kurutma sicakligi | 70 °C | 50 °C | -20 °C |
| Batch suresi (cam, 50 mm) | 10 gun | 12 gun | +2 gun (+%20) |
| Yillik enerji tuketimi (elektrik) | — | 245 MWh/yil | — |
| Yillik enerji tuketimi (termal) | 1,050 MWh/yil | 0 MWh/yil | -%100 |
| Yillik enerji maliyeti | 78,000 EUR/yil | 29,400 EUR/yil | -48,600 EUR/yil |
| Kurutma kusur orani | %4.5 | %1.2 | -%73 |
| CO2 emisyonu azaltma | — | 185 ton/yil | — |

**Not:** Batch suresi %20 uzamasina ragmen, dusuk sicaklikta (50 °C) kontrollü kurutma kusur oranini %73 azaltti. Kusurlarin ekonomik degeri (catlamis/egilmis kereste kaybi) yillik ~8,000 EUR ek tasarruf saglamaktadir.

### Ekonomik Degerlendirme

| Parametre | Deger |
|-----------|-------|
| Isi pompasi unitesi (kompresor, evaporator, kondenser) | 58,000 EUR |
| PLC kontrol sistemi + sensorler | 12,000 EUR |
| Montaj ve mekanik isler | 10,000 EUR |
| Buhar sistemi sokulme | 5,000 EUR |
| Toplam yatirim | 85,000 EUR |
| Yillik enerji tasarrufu | 48,600 EUR/yil |
| Ek fayda (kusur azaltma: %4.5 → %1.2) | ~8,000 EUR/yil |
| Kazan bakimi eliminasyonu | ~3,000 EUR/yil |
| Net yillik fayda (toplam) | ~35,000 EUR/yil |
| Basit geri odeme suresi (SPP) | 2.4 yil |
| NPV (10 yil, %8 iskonto orani) | 150,000 EUR |
| IRR | 37% |

**Not:** Net yillik tasarruf hesabinda, elektrik birim fiyatinin dogal gaz birim fiyatindan yuksek olmasi dikkate alinmistir (elektrik: 0.12 EUR/kWh, dogal gaz: 0.05 EUR/kWh).

### Ogrenilenler Dersler

1. **Isi pompasi retrofit**, kereste kurutmada en yuksek exergy verimi artisi saglayan onlemdir (%8.5 → %22). Dusuk kurutma sicakligi (50-55 °C) isi pompasi icin ideal calisma noktasidir.
2. **Kapali devre calisma** egzoz emisyonunu sifirlar (VOC, nem), cevre mevzuatina tam uyum saglar.
3. **Batch suresi uzamasi** (%20) ilk bakista dezavantaj gibi gorunse de, dusuk kusur orani ve dusuk isletme maliyeti bunu fazlasiyla telafi eder. Toplam uretim kapasitesi icin ek firin yatirimi degerlendirilmelidir.
4. **PLC kontrol sistemi** kritik oneme sahiptir; sabit sicaklik yerine denge nemi (EMC — Equilibrium Moisture Content) bazli dinamik kontrol, hem enerji hem kalite icin gereklidir.
5. Isi pompasi COP'u 3.4 ile her 1 kWh elektrik icin 3.4 kWh isi saglamaktadir; bu, dogal gaz kazani + serpantin sisteminin 0.85 kWh/kWh (kazan verimi) ile kiyaslandiginda %300 exergy avantaji yaratir.

---

## Vaka 4: Seramik Karo — Firin-Kurutucu Entegrasyonu (Kiln-Dryer Heat Integration)

### Tesis Profili

| Parametre | Deger |
|-----------|-------|
| Sektor | Seramik — karo uretimi (ceramic tile manufacturing) |
| Kurutucu tipi | Roller kurutucu (roller dryer), 5 bolge |
| Firin tipi | Roller kiln, 1,180 °C pisirim sicakligi |
| Uretim kapasitesi | 12,000 m2 karo/gun |
| Karo boyutu | 60 x 60 cm |
| Calisma suresi | 7,500 saat/yil |
| Enerji kaynagi | Dogal gaz |
| Kurulum yili | 2010 |
| Konum | Bilecik, Turkiye |

### Mevcut Durum (Before)

Roller kurutucu, ayri dogal gaz yakicilari ile isitiliyordu. Roller kiln sogutma bolgesinden cikan sicak hava (320-380 °C, ortalama 350 °C) dogrudan bacadan atmosfere atiliyordu. Kurutucu ve firin birbirinden bagimsiz enerji sistemleri olarak calisiyordu.

| Parametre | Deger |
|-----------|-------|
| Kurutucu giris havasi sicakligi | 200 °C (ayri yakici ile) |
| Kurutucu egzoz sicakligi | 110 °C |
| SEC (kurutucu) | 3,200 kJ/kg su |
| SMER | 0.78 kg/kWh |
| Exergy verimi (kurutucu) | 11% |
| Firin sogutma egzoz sicakligi | 350 °C (ortalama) |
| Firin sogutma egzoz debisi | 22,000 Nm3/h |
| Kurutucu yillik dogal gaz tuketimi | 5,600 MWh/yil |
| Kurutucu yillik enerji maliyeti | 280,000 EUR/yil |
| Toplam fabrika exergy verimi | 19% |

**Exergy analizi degerlendirmesi:** Kurutucu %11 exergy verimi ile "ortalama" sinifindaydi (%8-15 tipik seramik kurutucu). Ancak asil exergy kaybi fabrika genelinde gerceklesiyordu: firin sogutma bolgesinden 350 °C sicaklikta atilan hava, yuksek exergy icerigi tasiyordu [(1 - 298/623) = 0.52 Carnot faktoru]. Bu atigin kurutucuya yonlendirilmesi, cross-equipment exergy firsatiydi.

### Uygulanan Onlemler

**Ana Onlem: Firin Sogutma Egzozunun Kurutucuya Yonlendirilmesi (Kiln Exhaust Ducting to Dryer)**
- Firin sogutma bolgesinden kurutucu giris hava kanalina izoleli celik kanal sistemi dösendi
- Kanal uzunlugu: 38 m
- Kanal izolasyonu: 100 mm tas yunu (k = 0.040 W/m.K)
- Otomatik damper sistemi (3 adet motorlu damper)
- Sicaklik bazli PID kontrol (kurutucu giris havasi 180-210 °C hedef)
- Firin duruslari icin yedek dogal gaz yakici muhafaza edildi

**Teknik Detaylar:**
- Firin sogutma egzoz sicakligi: 350 °C
- Kanaldaki isi kaybi: ~15 °C (yalitimli, 38 m)
- Kurutucu giris havasi (atik isi ile): 335 °C → damperle karistirma ile 200 °C'ye dusuruldu
- Kurutucu enerji ihtiyacinin %70'i firin atik isisindan karsilandi
- Kalan %30 icin mevcut dogal gaz yakici korundu

### Sonuclar (After)

| Parametre | Oncesi | Sonrasi | Degisim |
|-----------|--------|---------|---------|
| SEC (kurutucu — satin alinan enerji bazinda) | 3,200 kJ/kg su | 1,100 kJ/kg su | -%65.6 |
| SMER (satin alinan enerji bazinda) | 0.78 kg/kWh | 2.27 kg/kWh | +%191 |
| Exergy verimi (kurutucu) | 11% | 18% | +7 puan |
| Kurutucu dogal gaz tuketimi | 750 kW | 225 kW | -%70 |
| Firin sogutma egzoz sicakligi (baca) | 350 °C | 130 °C | -220 °C |
| Kurutucu yillik dogal gaz tuketimi | 5,600 MWh/yil | 1,690 MWh/yil | -3,910 MWh/yil |
| Kurutucu yillik enerji maliyeti | 280,000 EUR/yil | 84,500 EUR/yil | -195,500 EUR/yil |
| Toplam fabrika exergy verimi | 19% | 27% | +8 puan |
| CO2 emisyonu azaltma | — | 790 ton/yil | — |

**Not:** SEC ve SMER degerleri "satin alinan enerji" (purchased energy) bazindadir. Atik isi bedelsiz kabul edilmistir. Toplam enerji bazinda bakinca kurutucu hala ~3,200 kJ/kg su tukettyor, ancak bunun %70'i bedelsiz atik isidir.

### Ekonomik Degerlendirme

| Parametre | Deger |
|-----------|-------|
| Celik kanal sistemi (izoleli, 38 m) | 22,000 EUR |
| Damper ve aktuatorler (3 adet) | 8,000 EUR |
| PID kontrol sistemi + sensorler | 7,000 EUR |
| Montaj ve insaat isleri | 13,000 EUR |
| Toplam yatirim | 50,000 EUR |
| Yillik enerji tasarrufu (dogal gaz) | 195,500 EUR/yil |
| Ek isletme maliyeti (fan elektrik, bakim) | -120,500 EUR/yil |
| Net yillik tasarruf | 75,000 EUR/yil |
| Basit geri odeme suresi (SPP) | 0.7 yil (~8 ay) |
| NPV (10 yil, %8 iskonto orani) | 453,000 EUR |
| IRR | >100% |

### Ogrenilenler Dersler

1. **Firin-kurutucu isi entegrasyonu**, seramik sektorundeki en yuksek etkili ve en hizli geri donen yatirimdir (SPP: 8 ay). Bu tip cross-equipment firsatlar ancak fabrika geneli exergy analizi ile tespit edilebilir.
2. **Kanal yalitimi kritiktir:** 38 m mesafede yalitimsiz kanal ile 60-80 °C isi kaybi olusurken, 100 mm tas yunu ile kayip 15 °C'ye dusuruldu.
3. **Damper kontrol sistemi** esneklik saglar: firin ve kurutucu farkli programlarda calistiginda, damperler otomatik olarak hava dagitimini ayarlar.
4. **Yedek yakici sisteminin muhafazasi** zorunludur; firin bakim duraklarinda kurutucu yaliz basina calisabilmelidir.
5. Fabrika geneli exergy verimi %19'dan %27'ye cikti — bu, tek ekipman optimizasyonuyla elde edilemeyecek bir iyilesmedir. **ExergyLab'in cross-equipment analiz modulunun degerini kanitlayan bir vakadir.**

---

## Vaka 5: Gida (Sebze) Kurutma — Cok Onlemli Paket (Multi-Measure Package for Vegetable Drying)

### Tesis Profili

| Parametre | Deger |
|-----------|-------|
| Sektor | Gida — kurutulmus sebze uretimi (dried vegetable production) |
| Kurutucu tipi | Tek bolgeli bant kurutucu (single-zone belt dryer) |
| Urun cesitleri | Domates, biber, sogan, patlicanl |
| Uretim kapasitesi | 1,500 kg yasmalzeme/saat |
| Calisma suresi | 5,000 saat/yil (mevsimsel agirlikli) |
| Enerji kaynagi | Dogal gaz (buhar kazani + hava isitici serpantin) |
| Kurulum yili | 2009 |
| Konum | Denizli, Turkiye |

### Mevcut Durum (Before)

Tek bolgeli bant kurutucu 80 °C sabit sicaklikta calisiyor, hava resirkulasyonu bulunmuyor, tum egzoz dogrudan bacadan atiliyordu. Sebzeler yikanarak direkt olarak bantli konveyore yerlestiriliyor, herhangi bir mekanik on-su alma islemi uygulanmiyordu. Giris nemi urun tipine gore %85-95 arasinda degismekte, ortalama %90 yasbaz olarak kabul edilmekteydi. Cikis nemi %8-12 yasbaz (urun tipine gore).

| Parametre | Deger |
|-----------|-------|
| Kurutma sicakligi | 80 °C (sabit, tek bolge) |
| Giris malzeme nemi | %90 (yasbaz, ortalama) → %70 kurubaz |
| Cikis malzeme nemi | %10 (yasbaz) |
| SEC | 4,500 kJ/kg su |
| SMER | 0.55 kg/kWh |
| Exergy verimi | 6.8% |
| Enerji verimi | 50% |
| Egzoz sicakligi | 60 °C |
| Egzoz bagil nemi | %45 (dusuk — verimsiz hava kullanimi) |
| Yillik enerji tuketimi | 6,750 MWh/yil |
| Yillik enerji maliyeti | 337,500 EUR/yil |

**Exergy analizi degerlendirmesi:** %6.8 exergy verimi, bant kurutucular icin "ortalamanin alti" sinifindadir (%6-12 tipik gida bant kurutucu). Dusuk egzoz bagil nemi (%45), havanin nem tasima kapasitesinin yetersiz kullanildigini gosteriyordu. Mekanik on-su alma olmamasamdan, termal kurutma yuku gereksiz yere yuksekti — 1 kg suyun mekanik olarak uzaklastirilmasi, termal buharlastirmaya gore ~50 kat daha az exergy tuketir.

### Uygulanan Onlemler

Uc asamali iyilestirme paketi uygulandi:

**Onlem 1: Vidalı Pres ile Mekanik On-Su Alma (Screw Press Pre-Dewatering)**
- Vidalı pres (screw press) kurulumu, kurutucu oncesine
- Giris malzeme nemi: %90 yasbaz → %70 yasbaz (pres sonrasi)
- Kurubaz olarak: giren nem %70'den %50'ye dustu (mutlak nem)
- Buharlastirilacak su miktari: ortalama %40 azaldi
- Vidalı pres elektrik tuketimi: 11 kW
- Sebze yapisi bozulmadan sikistrima (ayarlanabilir kontra basinc)

**Onlem 2: 3 Bolgeli Sicaklik Profili (3-Zone Temperature Profile)**
- Tek bolgeli 80 °C → 3 bolgeli degisken sicaklik:
  - Bolge 1 (giris): 90 °C — yuksek nem, sabit kurutma hizi donemi
  - Bolge 2 (orta): 75 °C — gecis bolgesi
  - Bolge 3 (cikis): 60 °C — dusuk nem, azalan kurutma hizi donemi, urun kalitesi koruma
- Her bolge icin bagimsiz sicaklik kontrolu
- Urun tipine gore 5 farkli kurutma programi (recete) tanimlandi

**Onlem 3: Kismi Hava Resirkulasyonu (Partial Air Recirculation)**
- Bolge 3 egzoz havasinin %60'i Bolge 1'e geri yonlendirildi
- Bolge 1'de dusuk nemli egzoz havasi, yuksek nemli malzeme uzerinden geciriliyor
- Taze hava ihtiyaci %35 azaldi
- Resirkulasyon kanallari, nem sensoru bazli otomatik damperler ile donatildi

### Sonuclar (After)

| Parametre | Oncesi | Sonrasi | Degisim |
|-----------|--------|---------|---------|
| Giris malzeme nemi (kurutucuya) | %90 (yasbaz) | %70 (yasbaz) | -20 puan |
| SEC | 4,500 kJ/kg su | 2,200 kJ/kg su | -%51.1 |
| SMER | 0.55 kg/kWh | 1.13 kg/kWh | +%105 |
| Exergy verimi | 6.8% | 12.5% | +5.7 puan |
| Enerji verimi | 50% | 72% | +22 puan |
| Egzoz sicakligi (Bolge 3, baca) | 60 °C | 52 °C | -8 °C |
| Egzoz bagil nemi | %45 | %68 | +23 puan |
| Buharlastirilacak su miktari | 1,200 kg/h | 720 kg/h | -%40 |
| Yillik enerji tuketimi (termal) | 6,750 MWh/yil | 3,300 MWh/yil | -3,450 MWh/yil |
| Ek elektrik tuketimi (pres) | 0 | 55 MWh/yil | — |
| Yillik enerji maliyeti | 337,500 EUR/yil | 171,600 EUR/yil | -165,900 EUR/yil |
| CO2 emisyonu azaltma | — | 695 ton/yil | — |

**Onlemlerin bireysel katki analizi:**

| Onlem | Tahmini Katki (SEC Azaltma) | Aciklama |
|-------|---------------------------|----------|
| 1 — Vidalı pres (mekanik on-su alma) | ~%40 | Termal yuk dogrudan azaldi |
| 2 — 3 bolgeli sicaklik profili | ~%8 | Dusuk sicaklik bolgesinde exergy uyumu iyilesti |
| 3 — Kismi resirkulasyon | ~%12 | Taze hava isitma yuku azaldi |
| **Toplam** | **~%51** | Onlemler arasinda sinerjik etki mevcut |

### Ekonomik Degerlendirme

| Parametre | Deger |
|-----------|-------|
| Onlem 1 — Vidalı pres + montaj | 55,000 EUR |
| Onlem 2 — 3 bolgeli donusum (damper, sensor, kontrol) | 35,000 EUR |
| Onlem 3 — Resirkulasyon kanallari + fanlar | 30,000 EUR |
| Toplam yatirim | 120,000 EUR |
| Yillik brut enerji tasarrufu | 165,900 EUR/yil |
| Ek isletme maliyeti (pres elektrik, bakim, posa bertaraf) | -100,900 EUR/yil |
| Net yillik tasarruf | 65,000 EUR/yil |
| Basit geri odeme suresi (SPP) | 1.8 yil |
| NPV (10 yil, %8 iskonto orani) | 316,000 EUR |
| IRR | 50% |

### Ogrenilenler Dersler

1. **Mekanik on-su alma** (vidalı pres), yuksek nemli gida urunlerinde en etkili ilk adimdir. 1 kg suyun vidalı presle uzaklastirilmasi ~7 kJ exergy tuketirken, termal buharlastirma ~300-450 kJ exergy tuketir (50-70 kat fark).
2. **3 bolgeli sicaklik profili** exergy uyumunu iyilestirir: yuksek nemli (kolay kurutma) bolgede yuksek sicaklik, dusuk nemli (zor kurutma) bolgede dusuk sicaklik kullanilarak gereksiz exergy yikimi onlenir.
3. **Kismi resirkulasyon** ozellikle cikis bolgesinde etkilidir cunku bu bolgedeki dusuk nemli egzoz havasi hala nem tasima kapasitesine sahiptir.
4. **Egzoz bagil nemi %45'ten %68'e cikmasi**, hava nem tasima kapasitesinin cok daha verimli kullanildigini gosterir (benchmark: %50-70 iyi, >%70 cok iyi).
5. Cok onlemli paket uygulama, tekil onlemlerin toplamindan daha fazla tasarruf saglar (sinerjik etki). Onlem siralama stratejisi: once mekanik (en dusuk exergy maliyeti), sonra termal optimizasyon, sonra geri kazanim.

---

## Ozet Tablosu — Tum Vaka Calismalari Karsilastirmasi

| # | Vaka | Sektor | Ana Onlem(ler) | SEC Oncesi (kJ/kg) | SEC Sonrasi (kJ/kg) | SEC Azalma | SMER Oncesi | SMER Sonrasi | Exergy Oncesi | Exergy Sonrasi | Yatirim (EUR) | Tasarruf (EUR/yil) | SPP (yil) |
|---|------|--------|----------------|--------------------|--------------------|------------|-------------|-------------|--------------|---------------|---------------|-------------------|-----------|
| 1 | Sut tozu sprey | Gida | Egzoz HR + 2 kademe + atomizasyon | 5,200 | 3,800 | %26.9 | 0.48 | 0.66 | %5.2 | %7.8 | 180,000 | 95,000 | 1.9 |
| 2 | Tekstil stenter | Tekstil | Egzoz HR + brulor + hiz + mangle | 5,500 | 3,600 | %34.5 | 0.45 | 0.69 | %6.1 | %9.8 | 65,000 | 42,000 | 1.5 |
| 3 | Kereste firinl | Ahsap | Isi pompasi retrofit | 4,000 | 1,200 | %70.0 | 0.60 | 2.50 | %8.5 | %22.0 | 85,000 | 35,000 | 2.4 |
| 4 | Seramik karo | Seramik | Firin-kurutucu entegrasyonu | 3,200 | 1,100* | %65.6 | 0.78 | 2.27* | %11.0 | %18.0 | 50,000 | 75,000 | 0.7 |
| 5 | Sebze kurutma | Gida | Pres + 3 bolge + resirkulasyon | 4,500 | 2,200 | %51.1 | 0.55 | 1.13 | %6.8 | %12.5 | 120,000 | 65,000 | 1.8 |

*Satin alinan enerji bazinda (purchased energy only)

### Temel Cikarimlar

1. **En hizli ROI:** Seramik firin-kurutucu entegrasyonu (SPP: 0.7 yil) — cross-equipment firsatlar en yuksek getiriyi saglar.
2. **En yuksek enerji tasarrufu (SEC):** Isi pompasi retrofit (%70) — dusuk sicaklikli kurutma uygulamalarinda benzersiz verimlilik.
3. **En yuksek exergy verimi artisi:** Isi pompasi retrofit (+13.5 puan, %8.5 → %22) — exergy kalite uyumu en iyi bu teknolojide gerceklesir.
4. **En dusuk yatirim:** Seramik entegrasyon (50,000 EUR) ve tekstil stenter paketi (65,000 EUR) — mevcut altyapi kullanildigi icin dusuk maliyet.
5. **Mekanik on-su alma etkisi:** Gida vakasinda vidalı pres tek basina %40 SEC azaltma sagladi — yuksek nemli urunlerde her zaman ilk degerlendirilmelidir.
6. **Cok onlemli yaklasim:** Tekstil ve gida vakalarinda birden fazla onlemin birlesimi, sinerjik etki ile tekil toplamin uzerinde tasarruf sagladi.
7. **Exergy analizi farki:** Geleneksel enerji analizi tum vakalarda %40-80 enerji verimi gosterirken, exergy analizi gercek termodinamik performansin %5-22 oldugunu ortaya koydu. Bu fark, iyilestirme onceliklerini belirlemede kritik oneme sahiptir.

### Yatirim Getiri Grafigi (Investment vs. Return)

```
SPP (yil)
  3 |
    |
2.5 |         * Vaka 3 (Kereste HP)
    |
  2 |   * Vaka 1 (Sprey)
    | * Vaka 5 (Sebze)
1.5 | * Vaka 2 (Stenter)
    |
  1 |
    | * Vaka 4 (Seramik)
0.5 |
    |
  0 +--+--+--+--+--+--+--+--+--+--+--+--> Yatirim (kEUR)
    0 20 40 60 80 100 120 140 160 180 200

Not: Tum vakalar SPP < 2.5 yil — endustriyel enerji yatirimlarinda
tipik kabul esigi olan 3 yilin altinda.
```

---

## İlgili Dosyalar

- `dryer/formulas.md` — Kurutucu exergy analizi hesaplama formulleri ve denklemleri
- `dryer/benchmarks.md` — Kurutucu performans karsilastirma degerleri (SMER, exergy verimi siniflandirmasi)
- `dryer/solutions/exhaust_heat_recovery.md` — Egzoz havasi isi geri kazanim cozumleri (Vaka 1, 2)
- `dryer/solutions/air_recirculation.md` — Hava geri deviri cozumleri (Vaka 5)
- `dryer/solutions/heat_pump_retrofit.md` — Isi pompasi retrofit rehberi (Vaka 3)
- `dryer/solutions/mechanical_dewatering.md` — Mekanik on-su alma cozumleri (Vaka 5)
- `dryer/sectors/food_drying.md` — Gida kurutma uygulamalari (Vaka 1, 5)
- `dryer/sectors/paper_drying.md` — Kagit kurutma uygulamalari
- `dryer/sectors/textile_drying.md` — Tekstil kurutma uygulamalari (Vaka 2)
- `dryer/sectors/ceramic_drying.md` — Seramik kurutma uygulamalari (Vaka 4)
- `dryer/sectors/wood_drying.md` — Kereste kurutma uygulamalari (Vaka 3)
- `factory/case_studies.md` — Fabrika geneli vaka calismalari (cross-equipment ornekleri)

## Referanslar

1. US DOE (2016). *Improving Process Heating System Performance: A Sourcebook for Industry*, 2nd Edition, US Department of Energy, Advanced Manufacturing Office.
2. Carbon Trust (2011). *Industrial Energy Efficiency Accelerator — Guide to the Drying and Dehydration Sector* (CTG058), Carbon Trust, UK.
3. EU BREF (2007). *Best Available Techniques Reference Document for the Ceramic Manufacturing Industry*, European Commission, Joint Research Centre.
4. EU BREF (2015). *Best Available Techniques Reference Document for the Production of Pulp, Paper and Board*, European Commission.
5. EU BREF (2003). *Reference Document on Best Available Techniques in the Textile Industry*, European Commission.
6. EU BREF (2019). *Reference Document on Best Available Techniques for Energy Efficiency*, European Commission.
7. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press.
8. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*, 2nd Edition, CRC Press.
9. Kemp, I.C. (2012). "Fundamentals of Energy Analysis of Dryers," in *Modern Drying Technology*, Vol. 4, Wiley.
10. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier.
11. Colak, N. & Hepbasli, A. (2009). "A review of heat pump drying: Part 1 — Systems, models and studies," *Energy Conversion and Management*, 50, 2180-2186.
12. Hasanbeigi, A. & Price, L. (2012). "A review of energy use and energy efficiency technologies for the textile industry," *Renewable and Sustainable Energy Reviews*, 16(6), 3648-3665.
13. Aghbashlo, M. et al. (2013). "A review on exergy analysis of drying processes and systems," *Renewable and Sustainable Energy Reviews*, 22, 1-22.
14. Stenstrom, S. (2020). "Drying of Paper: A Review 2000-2018," *Drying Technology*, 38(7), 825-845.
