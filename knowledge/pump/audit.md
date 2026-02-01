---
title: "Pompa Sistemi Enerji Denetimi Metodolojisi"
category: reference
equipment_type: pump
keywords: [enerji denetimi, pompa, ölçüm, analiz]
related_files: [pump/formulas.md, pump/benchmarks.md, pump/equipment/systems_overview.md]
use_when: ["Pompa enerji denetimi planlanırken", "Pompa sistemi ölçümleri değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Pompa Sistemi Enerji Denetimi Metodolojisi

> Son güncelleme: 2026-01-31

## Genel Bakış

Bu metodoloji, ISO/ASME 14414:2019 "Pump System Energy Assessment" standardına dayalı olarak pompa sistemlerinin enerji verimliliği değerlendirmesi için 5 adımlı bir süreç tanımlar.

## ISO/ASME 14414 Çerçevesi

### Standart Hakkında
- **ISO/ASME 14414:2019:** Pompa sistemi enerji değerlendirmesi
- ASME ile ortak geliştirilmiş uluslararası standart
- Her büyüklük ve sektördeki pompa sistemlerine uygulanabilir
- Açık ve kapalı döngü pompa sistemlerini kapsar
- Elektrik tahrikli sistemlere odaklanır; buhar türbini/motor tahriklere de uygulanabilir
- ISO 50001, ISO 50002 ve ISO 50003 çerçevesi ile uyumlu

### Değerlendirme Seviyeleri
| Seviye | Açıklama | Kapsam |
|--------|----------|--------|
| Ön tarama (Pre-screening) | Hızlı değerlendirme | Yüksek potansiyelli pompaların belirlenmesi |
| Seviye 1 | Yürüyen inceleme (walk-through) | Kalitatif, genel durum tespiti |
| Seviye 2 | Detaylı değerlendirme | Kantitatif ölçümler, pompa eğrisi analizi |
| Seviye 3 | Kapsamlı değerlendirme | Tam enstrümantasyon, uzun süreli izleme |

### Sistem Sınırları
1. **Elektrik beslemesi:** Şebeke/trafo'dan pompa motoruna
2. **Tahrik sistemi:** Motor, VSD (varsa), kaplin
3. **Pompa ünitesi:** Pompa, erişilebiliyorsa iç bileşenler
4. **Boru sistemi:** Emme ve basma hatları, valf, fiting, filtre
5. **Kontrol elemanları:** Throttle valf, bypass, on/off kontrol
6. **Kullanım noktası:** Proses gereksinimi (debi, basınç)

## Adım 1: Ön Hazırlık (Pre-Audit)

### 1.1 Toplanacak Bilgiler (En az 12 aylık)

| Kategori | Detay |
|----------|-------|
| Enerji faturaları | Aylık elektrik tüketimi ve talep ücretleri; pompa sistemi payı |
| Ekipman envanteri | Tüm pompalar, motorlar, VSD'ler, valf ve kontrol elemanları |
| Sistem şemaları | P&ID, boru yerleşimi, tek hat elektrik şeması |
| Pompa eğrileri | Üretici H-Q, verim, NPSHr eğrileri (orijinal ve test) |
| Üretim programı | Vardiya düzeni, mevsimsel değişimler, duruş dönemleri |
| Bakım kayıtları | Servis geçmişi, değişen parçalar, bilinen sorunlar |
| Önceki denetim raporları | Varsa önceki değerlendirmeler |
| Mevcut izleme verileri | Debi/basınç/güç izleme (SCADA, DCS verisi varsa) |

### 1.2 Ön Görüşme Soruları (Tesis Yönetimine)

1. Kaç pompa kurulu? Tipleri ve yaşları?
2. Tipik çalışma basıncı ve debi gereksinimleri?
3. Ana pompa tüketicileri/kullanım noktaları neler?
4. Bilinen verim sorunları veya kavitasyon problemleri var mı?
5. VSD kullanan pompa var mı? Kaç tanesi?
6. Throttle veya bypass valf ile kontrol edilen pompalar var mı?
7. Pompa sıralaması/çalışma senaryosu nasıl yönetiliyor?
8. Bakım programı nedir? Titreşim izleme yapılıyor mu?
9. Üretimden debi/basınç şikayetleri var mı?
10. Mevsimsel veya günlük debi değişimleri var mı?
11. Genişleme veya değişiklik planları?
12. Elektrik tarife yapısı ve enerji maliyeti?

### 1.3 Ön Tarama Kriterleri (ISO/ASME 14414 Annex E)

Aşağıdaki kriterlere sahip pompalar öncelikli değerlendirilmelidir:
- Yıllık çalışma süresi > 2000 saat VE nominal güç > 15 kW
- Throttle valf ile kontrol edilen pompalar
- Bypass hattı sürekli açık olan pompalar
- BEP'ten %30'dan fazla sapan pompalar
- 15 yaşından büyük pompalar
- Kavitasyon veya titreşim problemi bilinen pompalar
- Aşırı boyutlu olduğu bilinen/şüpheli pompalar

### 1.4 Denetim Ekipman Listesi

| Ekipman | Örnek Modeller | Amacı | Yaklaşık Maliyet |
|---------|---------------|-------|-----------------|
| Güç analizörü | Fluke 435-II, Hioki PW3198 | Güç profilleme (kW, kVA, PF) | €4,000-8,000 |
| Pens ampermetre | Fluke 376 FC | Anlık akım ölçümü | €300-500 |
| Dijital manometre | Keller LEO 2 | Basınç ölçümü (emme/basma) | €200-400 |
| Diferansiyel basınç ölçer | Testo 510i | Filtre, valf ΔP ölçümü | €150-300 |
| Ultrasonik debimetre | Flexim FLUXUS F601 | Boru üzerinden debi ölçümü (non-invasive) | €3,000-8,000 |
| Elektromanyetik debimetre | Endress+Hauser Promag | Hat tipi, iletken sıvılar | €2,000-5,000 |
| IR termometre | Fluke 62 MAX+ | Yüzey sıcaklığı | €50-150 |
| Titreşim ölçer | SKF CMVL 3860 | Titreşim analizi (hız, ivme) | €1,000-3,000 |
| Veri kaydedici | Onset HOBO, Yokogawa | Uzun süreli P, T, I kayıt | €500-2,000 |
| Tahoskop | Shimpo DT-205LR | Devir sayısı ölçümü | €200-500 |
| Termal kamera | FLIR E54 | Termal görüntüleme (motor, rulman) | €3,000-8,000 |
| Kamera (dijital) | Akıllı telefon/dijital | Durum belgeleme | — |

## Adım 2: Saha Çalışması (Field Work)

### 2.1 Sistem Envanteri

#### Her Pompa İçin Kaydedilecekler
- Üretici, model, seri numarası
- Pompa tipi (santrifüj, PD, dalgıç vb.)
- Nominal güç (kW veya HP)
- Nominal debi (m³/h, BEP noktasında)
- Nominal hat (m, BEP noktasında)
- İmpeller çapı (mm, orijinal ve trim edilmiş)
- Devir sayısı (rpm)
- Kademe sayısı (çok kademeli ise)
- Kontrol yöntemi (throttle, bypass, VSD, on/off)
- Üretim yılı
- Çalışma saati (varsa kontrolörden veya bakımdan)

#### Her Motor İçin
- Nominal güç (kW)
- Gerilim, akım, güç faktörü
- Verim sınıfı (IE1/IE2/IE3/IE4/IE5)
- Devir sayısı (rpm)
- Seri numarası ve üretim yılı

#### VSD (Değişken Hızlı Sürücü) Varsa
- Üretici ve model
- Nominal güç (kW)
- Çalışma frekans aralığı (Hz)
- Mevcut çalışma frekansı

#### Boru ve Valf Sistemi
- Boru çapları ve malzeme
- Toplam boru uzunlukları (emme ve basma)
- Valf tipleri ve konumları
- Throttle valf pozisyonları
- Bypass hattı varlığı ve durumu

### 2.2 Ölçümler

#### Güç Profilleme (KRİTİK ÖLÇÜM)
- **Süre:** Minimum 24 saat, ideal: 1 tam üretim haftası (168 saat)
- **Aralık:** 1 dakika veya daha kısa
- **Kayıt:** kW, kVA, faz başına A, güç faktörü
- **TÜM pompalar eşzamanlı** olarak kaydedilmeli
- Hafta sonu / üretim dışı saatler dahil edilmeli (baz yük tespiti için)
- VSD'li pompalarda frekans değeri de kaydedilmeli

#### Basınç Profilleme
- Pompa emme basıncı (vakummetreli)
- Pompa basma basıncı
- Throttle valf öncesi ve sonrası basınç (valf ΔP)
- Kullanım noktası basınçları (en az 2-3 kritik nokta)
- 1 dakika aralıkla, güç verisi ile senkron

#### Debi Ölçümü
- Toplam sistem debisi (ultrasonik veya elektromanyetik debimetre)
- Bireysel pompa debileri
- Bypass debisi (bypass hattı varsa)
- Kritik tüketici debileri

#### Sıcaklık Ölçümleri
- Sıvı sıcaklığı (emme, pompa için NPSHa hesabı)
- Motor kasa sıcaklığı (IR termometre)
- Rulman sıcaklıkları
- Ortam sıcaklığı

#### Titreşim Ölçümü
- Her pompa ve motor için 3 eksende (yatay, dikey, aksiyel)
- Referans: ISO 10816-7 (pompa titreşim sınırları)
- Alarm seviyeleri: < 4.5 mm/s (iyi), 4.5-7.1 mm/s (uyarı), > 7.1 mm/s (tehlike)

### 2.3 Throttle Valf Pozisyon Kontrolü

Throttle valf ile kontrol edilen her pompa için:
```
1. Valf tam açık mı yoksa kısık mı? (pozisyon kaydı)
2. Valf pozisyonu sabit mi yoksa modüle ediliyor mu?
3. Minimum ve maksimum valf pozisyonları
4. Valf ΔP ölçümü (diferansiyel manometre ile)
5. Valf konumuna göre tahmini debi yüzdeleri
```

Sürekli kısık çalışan valf = tasarruf fırsatı (VSD veya impeller trim).

### 2.4 Görsel İnceleme

#### Pompa Kontrol Listesi
- [ ] Titreşim veya olağandışı ses
- [ ] Salmastra/mekanik conta kaçağı
- [ ] Temel bağlantıları ve hizalama durumu
- [ ] Boyama ve korozyon durumu
- [ ] Emme filtresi/süzgeç durumu
- [ ] Pompa etiket bilgileri okunabilir mi?

#### Motor Kontrol Listesi
- [ ] Motor kasa sıcaklığı (el ile veya IR)
- [ ] Havalandırma açıklıkları temiz mi?
- [ ] Anormal ses veya titreşim
- [ ] Kaplin durumu ve hizalama
- [ ] Elektrik bağlantıları (gevşeme, korozyon)

#### Boru ve Vana Kontrol Listesi
- [ ] Boru destekleri ve izolasyon
- [ ] Korozyon veya erozyon izleri
- [ ] Kaçak belirtileri (flanşlarda, fitinglede)
- [ ] Valf durumu (tam açık mı, kapalı mı, kısık mı?)
- [ ] Emme hattı: hava girişi riski, uygun eğim
- [ ] Ölü uçlar (kullanılmayan ama basınçlı branşlar)
- [ ] Genleşme boşluğu / esnek bağlantı durumu

#### Kontrol Sistemi Kontrolü
- [ ] Throttle valf pozisyonu ve tipi
- [ ] Bypass hattı: açık mı, ne kadar debi geçiyor?
- [ ] VSD: doğru mu çalışıyor, frekans aralığı
- [ ] Otomasyon/SCADA entegrasyonu var mı?

### 2.5 Operatör Görüşmeleri

1. Hangi saatler/vardiyalarda debi talebi en yüksek?
2. Herhangi bir noktada basınç veya debi problemi var mı?
3. Kavitasyon sesi duyuluyor mu (hangi pompa, ne zaman)?
4. Pompalar ne sıklıkla bakım görüyor?
5. Mevsimsel talep değişimleri var mı?
6. En büyük sıvı tüketicisi hangi proses?
7. Pompa davranışında değişiklik fark ettiniz mi (titreşim, gürültü, sıcaklık)?
8. Pompa arıza geçmişi (son 2 yıl)?

## Adım 3: Veri Analizi

### 3.1 Wire-to-Water Verim Hesabı

```
η_w2w = P_hyd / P_electric × 100   [%]

Burada:
P_hyd = ρ × g × Q × H / 1000   [kW]
P_electric = ölçülen elektrik gücü [kW]

Q = debimetre ölçümü [m³/s]
H = (P_basma - P_emme) / (ρ × g) + (V_basma² - V_emme²)/(2g) + (z_basma - z_emme)
```

Hesaplanacak metrikler:
- Her pompa için wire-to-water verimi
- Sistem toplam wire-to-water verimi
- Benchmark ile karşılaştırma (bkz. pump_benchmarks.md)

### 3.2 BEP Analizi (Pompa Eğrisi Üzerinde Operasyon Noktası)

```
1. Ölçülen debi ve hattan operasyon noktasını belirle
2. Üretici H-Q eğrisi üzerinde BEP noktasını işle
3. Operasyon noktasının BEP'e göre sapmasını hesapla:
   Sapma(%) = (Q_op - Q_BEP) / Q_BEP × 100
4. BEP sapmasına göre verim kaybını değerlendir
5. BEP sapmasına göre mekanik risk seviyesini belirle
```

Kabul edilebilir aralık: BEP'in %70 ile %120'si arası.
Tercih edilen aralık: BEP'in %80 ile %110'u arası.

### 3.3 Exergy Analizi (ExergyLab Engine Kullanarak)

1. Exergy girişi hesapla (her pompaya toplam elektrik gücü)
2. Exergy çıkışı hesapla (kullanım noktalarında faydalı hidrolik güç)
3. Exergy yıkım dağılımını belirle:
   - Motor kayıpları
   - VSD kayıpları (varsa)
   - Pompa iç kayıpları (hidrolik, volümetrik, mekanik)
   - Boru sürtünüm kaybı
   - Throttle valf kaybı
   - Bypass kaybı
   - Aşırı boyutlandırma kaybı
4. Sistem exergy verimini benchmark ile karşılaştır
5. En büyük exergy yıkım kaynaklarını belirle
6. Grassmann (exergy akış) diyagramı oluştur

### 3.4 Benchmark Karşılaştırması

| Metrik | Ölçüm Değeri | Benchmark | Durum |
|--------|-------------|-----------|-------|
| Wire-to-water verim | ... % | >%55 (iyi) | ... |
| SEC [kWh/m³] | ... | ... (hat'a bağlı) | ... |
| BEP sapması | ... % | <%20 (iyi) | ... |
| Sistem exergy verimi | ... % | >%40 (iyi) | ... |

## Adım 4: Raporlama

### Rapor Yapısı

#### 1. Yönetici Özeti (1 sayfa)
- Sistem genel bakışı (pompa sayısı, toplam kapasite, yıllık enerji maliyeti)
- Temel bulgular (3-5 madde)
- Toplam tasarruf potansiyeli (kWh/yıl ve €/yıl)
- Öncelikli öneriler ve ROI
- Uygulama zaman çizelgesi özeti

#### 2. Sistem Tanımı (2-4 sayfa)
- Ekipman envanter tablosu
- Sistem şeması/yerleşimi (P&ID)
- Çalışma koşulları (basınç, debi, vardiya, üretim)
- Kontrol stratejisi açıklaması

#### 3. Mevcut Durum Değerlendirmesi (3-5 sayfa)
- Enerji tüketimi analizi (kWh, maliyet, trend)
- Yük profili analizi (grafiklerle)
- Wire-to-water verim hesabı
- BEP analizi (pompa eğrisi üzerinde operasyon noktası)
- Sistem exergy verimi
- Benchmark karşılaştırması

#### 4. Bulgular ve Analiz (5-10 sayfa)
Her bulgu için:
- Açıklama, ölçüm verileri, fotoğraflar
- Mevcut durum niceliği (kW, kWh, verim)
- Temel neden
- Etki (kWh/yıl, €/yıl, CO₂)

#### 5. İyileştirme Önerileri (3-5 sayfa)

Öncelik matrisi formatında:

| # | Öneri | Yatırım | Yıllık Tasarruf | Geri Ödeme | Öncelik |
|---|-------|---------|----------------|------------|---------|
| 1 | VSD uygulaması (Pompa-1) | €8,000 | €5,900 | 1.4 yıl | YÜKSEK |
| 2 | İmpeller trim (Pompa-3) | €1,200 | €3,500 | 0.3 yıl | YÜKSEK |
| 3 | Throttle eliminasyonu | €0 | €1,900 | 0 yıl | YÜKSEK |
| 4 | Aşınma halkası yenileme | €800 | €600 | 1.3 yıl | ORTA |
| 5 | Pompa değişimi (boyut düzeltme) | €15,000 | €4,200 | 3.6 yıl | ORTA |

Her öneri için:
- Teknik açıklama
- Yatırım maliyet tahmini
- Yıllık tasarruf hesabı (varsayımlarla)
- Basit geri ödeme süresi
- CO₂ azaltma
- Uygulama karmaşıklığı (düşük/orta/yüksek)

#### 6. ROI Hesapları (2-3 sayfa)
- Her öneri için detaylı hesaplama
- Anahtar varsayımlara duyarlılık analizi
- Birden fazla önlem uygulandığında kombine tasarruf
- Büyük yatırımlar için net bugünkü değer

#### 7. Uygulama Yol Haritası (1-2 sayfa)
- **Faz 1:** Hızlı kazanımlar (0-3 ay) — throttle eliminasyonu, impeller trim, kontrol iyileştirme
- **Faz 2:** Orta vadeli (3-12 ay) — VSD uygulaması, aşınma halkası yenileme
- **Faz 3:** Uzun vadeli (1-3 yıl) — pompa değişimi, sistem yeniden tasarım, boru optimizasyonu
- Tasarruf doğrulama izleme planı

#### 8. Ekler
- A: Ham ölçüm verileri (güç profilleri, basınç logları, debi kayıtları)
- B: Ekipman etiket fotoğrafları
- C: Pompa eğrisi analiz grafikleri
- D: Hesaplama detayları (exergy dağılımı, tasarruf hesapları)
- E: Ekipman teknik şartnameleri (önerilmiş ise)

### Tipik Bulgular ve Tasarruf Aralıkları

| Kategori | Tipik Bulgu | Tipik Tasarruf |
|----------|------------|---------------|
| Throttle eliminasyonu (VSD) | Sürekli kısık valf, %20-50 fazla enerji | %15-40 |
| Aşırı boyutlandırma | BEP'ten >%30 sapma, düşük verim | %10-25 |
| İmpeller trim | Pompa aşırı hat üretiyor | %10-20 |
| VSD uygulaması | Değişken debili sistem, sabit hız | %20-50 |
| Aşınma halkası yenileme | İç kaçak artmış, verim düşük | %2-8 |
| Boru optimizasyonu | Yetersiz boru çapı, yüksek sürtünüm | %2-10 |
| Kontrol iyileştirme | Bypass açık, kötü pompa sıralaması | %5-15 |
| Motor yenileme (IE3/IE4) | Eski IE1/IE2 motor | %2-5 |
| Pompa değişimi | Çok eski veya yanlış tip pompa | %15-30 |

## Adım 5: Doğrulama ve Takip

### Uygulama Sonrası Doğrulama

- Öneri uygulandıktan sonra 2-4 haftalık güç ve debi profilleme
- Önceki/sonraki karşılaştırması (aynı koşullarda)
- IPMVP (International Performance Measurement and Verification Protocol) yöntemiyle doğrulama
- Opsiyon A (Kısmen ölçümlü) veya Opsiyon B (Tüm parametreler ölçümlü)

### Sürekli İzleme KPI'ları

| KPI | Formül | Ölçüm Sıklığı |
|-----|--------|---------------|
| Wire-to-water verimi | P_hyd / P_electric × 100 | Aylık (sürekli izleme idealdir) |
| SEC [kWh/m³] | Toplam kWh / Toplam m³ | Aylık |
| BEP sapması | (Q_op - Q_BEP) / Q_BEP × 100 | Yıllık (denetimde) |
| Sistem exergy verimi | Ex_çıkış / Ex_giriş × 100 | Yıllık (denetimde) |
| Basınç kararlılığı | P_max - P_min | Sürekli |
| Titreşim seviyesi | mm/s RMS | Aylık veya sürekli |
| Enerji yoğunluğu | kWh / üretim birimi | Aylık |
| Motor akımı | I [A] | Sürekli (SCADA ile) |

## ISO/ASME 14414 — Genel Enerji Denetiminden (ISO 50002) Farkları

| Özellik | ISO/ASME 14414 | ISO 50002 |
|---------|----------------|-----------|
| Kapsam | Pompa sistemi spesifik | Genel enerji |
| KPI'lar | W2W verim, SEC, BEP sapması | Genel enerji göstergeleri |
| Ölçüm yöntemleri | Pompa sistemine özel rehberlik | Genel |
| Sistem sınırı | Elektrikten kullanım noktasına | Üretim odaklı |
| Kontrol analizi | Throttle, bypass, VSD detaylı | Genel kontrol |
| Boyutlandırma | Pompa-sistem uyumu analizi | Kapsam dışı |
| Annex'ler | Ön tarama, SEC, parazitik güç, örnekler | Genel |

## İlgili Dosyalar

- Benchmark verileri: `benchmarks/pump_benchmarks.md`
- Exergy formülleri: `formulas/pump_exergy.md`
- Çözüm dosyaları: (oluşturulacak) `solutions/pump_*.md`

## Referanslar

- ISO/ASME 14414:2019, "Pump System Energy Assessment"
- ISO 9906:2012, "Rotodynamic Pumps — Hydraulic Performance Acceptance Tests"
- ISO 50002:2014, "Energy Audits — Requirements with guidance for use"
- ISO 10816-7, "Mechanical vibration — Evaluation of machine vibration by measurements on non-rotating parts — Part 7: Rotodynamic pumps"
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition
- Hydraulic Institute, "Pump Life Cycle Costs: A Guide to LCC Analysis for Pumping Systems"
- Hydraulic Institute, "Optimizing Pumping Systems" (ANSI/HI)
- Europump, "Variable Speed Pumping: A Guide to Successful Applications"
- IPMVP, "International Performance Measurement and Verification Protocol"
- API 610, "Centrifugal Pumps for Petroleum, Petrochemical and Natural Gas Industries"
