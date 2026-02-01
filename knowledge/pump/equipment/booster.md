# Hidrofor / Basınç Artırıcı Sistemler — Booster/Pressure Boosting Systems

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Çok pompalı basınç artırıcı (booster) paket sistemi
- Kapasite aralığı: 1 - 500+ m³/h
- Basınç aralığı: 2 - 16 bar
- Yapı: 2-6 pompa + VSD + basınç tankı + kontrol ünitesi
- Yaygın markalar: Grundfos Hydro MPC, KSB Hya, Wilo COR, DAB E.sybox, Lowara GHV, Xylem e-SV

## Çalışma Prensibi
Hidrofor (booster) sistemi, şebeke veya depo basıncının yetersiz olduğu durumlarda su basıncını artırmak için kullanılır. Tipik olarak birden fazla santrifüj pompa paralel bağlanarak çalışır. Akıllı kontrol ünitesi (CU 352 gibi), talebe göre pompa sayısını ve hızını ayarlayarak sabit çıkış basıncı sağlar.

### Sistem Bileşenleri
- **Pompalar:** Çok kademeli dikey santrifüj (CR/CRE tipi) — 2 ila 6 adet paralel
- **VSD (Değişken Hız Sürücü):** Her pompaya entegre veya harici frekans konvertörü
- **Basınç tankı (Genleşme tankı):** On-off çevrimlerini azaltır, su darbesi sönümler (20-500 L)
- **Kontrol ünitesi:** PID basınç kontrolü, kaskad pompa yönetimi, alarm ve izleme
- **Vanalar:** Çek vana, izolasyon vanası, basınç tahliye vanası
- **Sensörler:** Basınç transmitteri (çıkış), akış anahtarı, kuru çalışma koruması

## Sistem Konfigürasyonları

### Tek Pompa Sistemi
- Basit uygulamalar: küçük binalar, sulama
- Kapasite: 1-20 m³/h
- Avantaj: Düşük maliyet, basit kurulum
- Dezavantaj: Yedeklilik yok, kapasite sınırlı

### Paralel Pompa Sistemi (2-6 pompa)
- Orta-büyük uygulamalar: yüksek binalar, endüstriyel tesisler
- Kapasite: 5-500+ m³/h
- Avantaj: Yedeklilik, geniş kapasite aralığı, yüksek verim
- Dezavantaj: Yüksek yatırım, karmaşık kontrol

### Kaskad Kontrol Stratejisi
Akıllı kontrol ünitesi aşağıdaki adımları izler:
1. Talep artınca ilk pompa hızlanır (VSD ile)
2. İlk pompa maksimuma ulaşınca ikinci pompa devreye girer
3. İki pompa birlikte hızlanır
4. Talep azalınca ters sırada pompalar devreden çıkar
5. Çalışma süreleri eşitlenmesi için pompa sıralaması otomatik değişir

## Kontrol Yöntemleri

| Yöntem | Çalışma Prensibi | Verimlilik | Uygulama |
|--------|-------------------|------------|----------|
| On-off | Pompa açılır/kapanır, basınç tankı ile | Düşük (%30-50) | Küçük konut sistemleri |
| Sabit basınç (VSD) | PID ile sabit çıkış basıncı | İyi (%50-65) | Standart hidrofor |
| Orantısal basınç (VSD) | Basınç set noktası debiye göre düşer | Çok iyi (%55-70) | Bina HVAC, yangın |
| Sabit sıcaklık (sirkülasyon) | Sıcaklık geri beslemeli | İyi | Sıcak su sirkülasyonu |
| Multi-pump kaskad (VSD) | Tüm pompalar VSD ile birlikte | En iyi (%60-70+) | Modern paket sistemler |

## Enerji Dağılımı (Tipik)
- Faydalı hidrolik iş (wire-to-water): %40-70
- Motor kayıpları: %5-10
- VSD kayıpları: %2-5
- Pompa hidrolik kayıpları: %10-20
- Boru sürtünme kayıpları: %5-15
- Kontrol/throttle kayıpları: %5-15

## Wire-to-Water Verimlilik

```
Wire-to-water verimi:

η_w2w = η_motor × η_VSD × η_pompa × η_sistem

Burada:
  η_motor  = Motor verimi (%90-96, IE sınıfına bağlı)
  η_VSD    = VSD verimi (%95-98)
  η_pompa  = Pompa verimi (%60-85, BEP'te en yüksek)
  η_sistem = Sistem verimi — boru kayıpları ve kontrol kayıpları (%80-95)

Örnek: 0.93 × 0.97 × 0.75 × 0.90 = 0.609 → %60.9 wire-to-water verim
```

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü (toplam) | kW | 0.5-200+ | Güç analizörü |
| Çıkış basıncı | bar | 2-16 | Basınç transmitteri |
| Su debisi | m³/h | 1-500+ | Debimetre (elektromanyetik, ultrasonik) |
| Giriş basıncı | bar | 0-6 | Basınç transmitteri |

### Opsiyonel (daha detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Her pompa elektrik gücü | kW | 0.25-50 | CT + voltaj (pompa bazında) |
| Her pompa devri | RPM | 500-3600 | VSD ekranı |
| Su sıcaklığı | °C | 5-80 | Termometre |
| Pompa çevrim sayısı | adet/saat | 0-20 | Kontrol paneli |
| Çalışma saati (pompa bazında) | saat/yıl | 1000-8760 | Sayaç |
| Basınç tankı ön şişirme | bar | 1-10 | Basınç göstergesi |

### Nameplate Bilgileri
- Marka ve model (örn. Grundfos Hydro MPC-E 4 CRE 20-3)
- Pompa sayısı ve her pompa nominal gücü (kW)
- Nominal debi (m³/h) ve nominal basınç (bar/m)
- Motor verimlilik sınıfı (IE2/IE3/IE4/IE5)
- VSD tipi (entegre veya harici)
- Kontrol ünitesi modeli
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Wire-to-water verim | %55 | VSD kontrollü ortalama sistem |
| Motor verimi | %91 | IE3 seviyesi, 5-15 kW |
| Pompa verimi | %70 | BEP yakınında çalışma varsayımı |
| VSD verimi | %97 | Modern frekans konvertörü |
| Çalışma saati | 4000 saat/yıl | Bina uygulaması |
| Yük profili (ortalama) | %60 | Tipik bina talep profili |
| Giriş basıncı | 2 bar | Şebeke suyu, Türkiye tipik |
| cosφ (güç faktörü) | 0.85 | VSD'siz; VSD ile ~0.95+ |
| Basınç tankı hacmi | 50 L | 2-3 pompalı küçük sistem |
| Boru basınç kaybı | %15 çıkış basıncının | Orta uzunluk boru hattı |

## Basınç Tankı (Genleşme Tankı) Boyutlandırma

```
Basınç tankı minimum hacmi:

V_tank = Q_min × t_min / (ΔP / P_ort)

Burada:
  V_tank  = Tank hacmi (litre)
  Q_min   = Minimum debi (L/s) — pompa çevrim sınırlaması
  t_min   = Minimum çalışma süresi (saniye) — tipik 60-120 s
  ΔP      = Açma-kapama basınç farkı (bar) — tipik 0.5-1.5 bar
  P_ort   = Ortalama çalışma basıncı (bar)

Pratik kural: VSD sistemlerde küçük tank yeterli (20-50 L),
on-off sistemlerde büyük tank gerekli (100-500 L)
```

## Verimlilik Kıyaslaması (Benchmarks)

| Kategori | Wire-to-Water Verim | Spesifik Enerji | Not |
|----------|--------------------|--------------------|-----|
| Düşük | <%40 | >0.50 kWh/m³/bar | On-off kontrol, aşırı boyutlu pompa |
| Ortalama | %40-55 | 0.35-0.50 kWh/m³/bar | VSD, standart pompa |
| İyi | %55-65 | 0.25-0.35 kWh/m³/bar | Multi-pump VSD, doğru boyutlama |
| Best-in-class | >%65 | <0.25 kWh/m³/bar | IE5 motor, orantısal basınç, optimize boru |

## Uygulama Alanları

| Uygulama | Tipik Basınç (bar) | Tipik Debi (m³/h) | Özel Gereksinimler |
|----------|-------------------|-------------------|-------------------|
| Bina su basınçlandırma | 3-8 | 5-100 | Gürültü sınırı, kompakt boyut |
| Yüksek bina (>10 kat) | 6-16 | 10-200 | Bölgeli basınç, yüksek güvenilirlik |
| Yangın söndürme (sprinkler) | 6-12 | 50-500+ | Yedeklilik, dizel pompa, jockey pompa |
| Endüstriyel proses suyu | 3-10 | 10-500+ | Sürekli çalışma, korozyon direnci |
| Sulama | 2-6 | 5-200 | Değişken talep, kuru çalışma koruması |
| HVAC sirkülasyon | 2-6 | 5-100 | Orantısal basınç kontrolü |

## Enerji Tasarrufu Fırsatları

### 1. VSD Retrofit (On-Off → VSD)
- Eski on-off kontrollü sisteme VSD eklenmesi
- Tipik tasarruf: %25-50
- Geri ödeme: 1-3 yıl
- Ek avantaj: Su darbesi azalır, ömür uzar

### 2. Orantısal Basınç Kontrolü
- Sabit basınç yerine debiye bağlı değişken basınç set noktası
- Düşük debide basınç set noktası düşer → enerji tasarrufu
- Tipik tasarruf: %10-20 (sabit basınca kıyasla)

### 3. Pompa Boyutlandırma Optimizasyonu
- Aşırı boyutlu pompaların küçük ve verimli pompalarla değiştirilmesi
- Daha fazla, daha küçük pompa = daha iyi kısmi yük verimi
- Tipik tasarruf: %15-30

### 4. Gece Modu / Düşük Talep Yönetimi
- Gece saatlerinde tek pompa düşük devirde çalışır
- Diğer pompalar tamamen kapatılır
- Basınç set noktası düşürülebilir

### 5. Boru Optimizasyonu
- Küçük çaplı borularda yüksek sürtünme kaybı = ek pompa enerjisi
- Boru çapı artırma veya dirsek sayısı azaltma
- Her %10 boru kaybı azaltma ≈ %10 pompa enerjisi tasarrufu

## Dikkat Edilecekler

1. **Minimum akış koruması:** Pompanın minimum akış noktasının altında çalışması hasara yol açar — kontrol sistemi bunu engellemelidir
2. **Pompa sıralama (rotation):** Tüm pompaların eşit çalışması için otomatik sıralama zorunlu — aksi halde erken yıpranma
3. **Gece modu:** Düşük talep dönemlerinde küçük tek pompa yeterli — gereksiz pompa çalıştırmadan kaçınılmalı
4. **Basınç tankı bakımı:** Membran ve ön şişirme basıncı yıllık kontrol — düşük basınç pompa çevrimini artırır
5. **Kuru çalışma koruması:** Su kesilmesinde pompayı koruyan sensör/anahtar şart — motor yanması riski
6. **Kavitasyon:** Giriş basıncı düşükse NPSH kontrolü yapılmalı — özellikle yüksek katlı binalarda
7. **Su darbesi:** Pompa aniden durduğunda su darbesi oluşabilir — VSD ile yumuşak durdurma veya darbeli çek vana
8. **Aşırı boyutlama:** En yaygın sorun — güvenlik marjı nedeniyle pompa çok büyük seçilir, BEP'ten uzakta çalışır

## İlgili Dosyalar
- Pompa motorları ve sürücüler: `equipment/pump_motors_drives.md`
- Pompa sistemleri genel: `equipment/pumping_systems_overview.md`
- Vakum pompaları: `equipment/pump_vacuum.md`

## Referanslar
- Grundfos, "Pressure Boosting System Design Guide"
- Grundfos, "Hydro MPC BoosterpaQ Technical Documentation"
- KSB, "Selecting Centrifugal Pumps — Handbook"
- Wilo, "COR Booster System Planning Guide"
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition
- Hydraulic Institute, "Pump System Assessment and Optimization"
- ASHRAE 90.1 — Energy Standard for Buildings (Service Water Boosters)
- Europump, "Guide to Variable Speed Pumping"
