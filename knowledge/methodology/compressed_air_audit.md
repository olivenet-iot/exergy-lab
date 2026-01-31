# Basınçlı Hava Sistemi Enerji Denetimi Metodolojisi

> Son güncelleme: 2026-01-31

## Genel Bakış

Bu metodoloji, ISO 11011:2013 "Compressed Air — Energy Efficiency — Assessment" standardına dayalı olarak basınçlı hava sistemlerinin enerji verimliliği değerlendirmesi için 5 adımlı bir süreç tanımlar.

## ISO 11011 Çerçevesi

### Standart Hakkında
- **ISO 11011:2013:** Basınçlı hava sistemlerinin enerji verimliliği değerlendirmesi
- Her büyüklük ve sektördeki basınçlı hava sistemlerine uygulanabilir
- Hem arz (üretim) hem talep (kullanım) tarafını kapsar

### Değerlendirme Seviyeleri
| Seviye | Açıklama | Kapsam |
|--------|----------|--------|
| Seviye 1 | Yürüyerek inceleme (walk-through) | Kalitatif, genel durum tespiti |
| Seviye 2 | Detaylı değerlendirme | Kantitatif ölçümler, analiz |
| Seviye 3 | Kapsamlı değerlendirme | Tam enstrümantasyon, uzun süreli izleme |

### Sistem Sınırları
1. **Arz tarafı:** Elektrik beslemesinden basınçlı hava üretimine
2. **Arıtma:** Kurutma, filtrasyon, kondansat yönetimi
3. **Dağıtım:** Boru, depolama, basınç düzenleme
4. **Talep tarafı:** Kullanım noktası uygulamaları

## Adım 1: Ön Hazırlık (Pre-Audit)

### 1.1 Toplanacak Bilgiler (En az 12 aylık)

| Kategori | Detay |
|----------|-------|
| Enerji faturaları | Aylık elektrik tüketimi ve talep ücretleri; basınçlı hava payı |
| Ekipman envanteri | Tüm kompresörler, kurutucular, filtreler, tanklar, drenajlar |
| Sistem şemaları | P&ID, boru yerleşimi, tek hat elektrik şeması |
| Üretim programı | Vardiya düzeni, mevsimsel değişimler, duruş dönemleri |
| Bakım kayıtları | Servis geçmişi, değişen parçalar, bilinen sorunlar |
| Önceki denetim raporları | Varsa önceki değerlendirmeler |
| Mevcut izleme verileri | Debi/basınç izleme (varsa) |

### 1.2 Ön Görüşme Soruları (Tesis Yönetimine)

1. Kaç kompresör kurulu? Tipleri ve yaşları?
2. Tipik çalışma basıncı? Son dönemde değişti mi?
3. Hava kalitesi gereksinimleri (ISO 8573-1 sınıfı)?
4. Ana basınçlı hava tüketicileri neler?
5. Bilinen kaçak sorunları var mı?
6. VSD kompresör veya master controller var mı?
7. Kompresör sıralaması nasıl yönetiliyor?
8. Bakım programı nedir?
9. Üretimden basınç şikayetleri var mı?
10. Talep değişti mi (yeni hatlar, kaldırılan ekipman)?
11. Genişleme veya değişiklik planları?
12. Elektrik tarife yapısı?

### 1.3 Denetim Ekipman Listesi

| Ekipman | Örnek Modeller | Amacı | Yaklaşık Maliyet |
|---------|---------------|-------|-----------------|
| Güç analizörü | Fluke 435-II, Hioki PW3198 | Güç profilleme (kW, kVA, PF) | €4,000-8,000 |
| Pens ampermetre | Fluke 376 FC | Anlık akım ölçümü | €300-500 |
| Dijital manometre | Keller LEO 2 (0-16 bar) | Basınç ölçümü | €200-400 |
| Diferansiyel basınç ölçer | Testo 510i | Filtre/kurutucu ΔP | €150-300 |
| IR termometre | Fluke 62 MAX+ | Yüzey sıcaklığı | €50-150 |
| Ultrasonik kaçak dedektörü | SDT 270, UE UP100 | Kaçak tespiti | €2,000-6,000 |
| Akustik görüntüleme kamerası | Fluke ii910, FLIR Si124 | Hızlı kaçak görselleştirme | €15,000-30,000 |
| Veri kaydedici | Onset HOBO, Yokogawa | Uzun süreli P, T, I kayıt | €500-2,000 |
| Basınçlı hava debimetre | VP FlowScope | Hat veya daldırma tipi | €2,000-5,000 |
| Çiğ noktası ölçer | Vaisala DMT143 | Kurutucu çıkış doğrulama | €1,000-3,000 |
| Anemometre | Testo 405i | Havalandırma, giriş havası | €100-200 |
| Kamera | Akıllı telefon/dijital | Durum belgeleme | — |

## Adım 2: Saha Çalışması (Field Work)

### 2.1 Sistem Envanteri

#### Her Kompresör İçin Kaydedilecekler
- Üretici, model, seri numarası
- Nominal güç (kW veya HP)
- Nominal kapasite (m³/min, CFM veya l/s, belirtilen basınçta)
- Nominal çıkış basıncı (bar veya PSI)
- Kontrol yöntemi (load/unload, modülasyon, VSD, on/off)
- Üretim yılı
- Çalışma saati (kontrolörden)
- Yük saati vs toplam saat
- Motor nameplate: gerilim, akım, güç faktörü, verim sınıfı (IE2/IE3/IE4)

#### Her Kurutucu İçin
- Tip (soğutmalı, desiccant ısıtmalı/ısıtmasız, HOC, membran)
- Nominal kapasite
- Nominal çiğ noktası (PDP)
- Purge hava tüketimi (desiccant tip için)
- Enerji tüketimi

#### Tanklar, Filtreler, Drenajlar
- Tank hacimleri ve konumları (ıslak/kuru)
- Filtre tipleri, konumları, mevcut ΔP değerleri
- Drenaj tipleri (timer/demand/no-loss)

### 2.2 Ölçümler

#### Güç Profilleme (KRİTİK ÖLÇÜM)
- **Süre:** Minimum 24 saat, ideal: 1 tam üretim haftası (168 saat)
- **Aralık:** 1 dakika veya daha kısa
- **Kayıt:** kW, kVA, faz başına A, güç faktörü
- **TÜM kompresörler eşzamanlı** olarak kaydedilmeli
- Hafta sonu / üretim dışı saatler dahil edilmeli (kaçak tespiti için)

#### Basınç Profilleme
- Kompresör çıkış basıncı
- Sistem ana hat basıncı (kurutucu/filtre sonrası)
- Uzak kullanım noktası basınçları (en az 2-3 kritik nokta)
- 1 dakika aralıkla, güç verisi ile senkron

#### Sıcaklık Ölçümleri
- Ortam/giriş havası sıcaklığı
- Kompresör çıkış sıcaklığı
- Aftercooler çıkış sıcaklığı
- Kompresör odası sıcaklığı
- Yağ sıcaklığı (kontrolör ekranından)

#### Debi Ölçümü (Ekipman mevcutsa)
- Toplam sistem debisi (daldırma veya hat tipi debimetre)
- Bireysel kompresör debileri
- Kritik tüketici debileri

### 2.3 Kaçak Taraması

#### Sistematik Tarama Protokolü
1. Kompresör odasından başla, ana hattı takip et
2. Tüm branş hatlarını dağıtım noktalarına kadar tara
3. Yüksek olasılıklı noktalara odaklan (bkz. aşağıdaki liste)
4. Her kaçağı benzersiz ID ile etiketle
5. Fotoğrafla
6. Kaçak log tablosuna kaydet (konum, tahmini boyut, öncelik)

#### Yüksek Olasılıklı Kaçak Noktaları
1. Quick-connect kaplinler (tüm kaçakların ~%50'si)
2. Hortum bağlantıları ve fitingler
3. FRL üniteleri (filtre-regülatör-lubrikatör)
4. Pnömatik valf/silindir bağlantıları
5. Dişli boru bağlantıları
6. Flanş bağlantıları
7. Kondansat drenajları (açık kalan veya sızan)
8. Basınç regülatörleri
9. Kesme vanaları (tam oturmayan)
10. Kullanılmayan ekipman (hala basınçlı hatlar)

### 2.4 Görsel İnceleme

#### Kompresör Odası Kontrol Listesi
- [ ] Oda sıcaklığı (<40°C, ideal <35°C)
- [ ] Havalandırma yeterliliği (panjurlar açık, fanlar çalışıyor)
- [ ] Giriş havası kaynağı (oda havası mı, dış hava kanalı mı)
- [ ] Giriş filtresi durumu (görsel, ΔP)
- [ ] Yağ seviyesi ve durumu
- [ ] Kondansat drenaj çalışması (manuel test)
- [ ] Titreşim veya olağandışı ses
- [ ] Kontrolör hata kodları veya uyarılar
- [ ] Kayış durumu (kayış tahrikli ise)
- [ ] Soğutucu temizliği (toz/kir birikimi)

#### Dağıtım Sistemi Kontrol Listesi
- [ ] Boru malzemesi ve durumu (korozyon, kabuk)
- [ ] Boru boyutlandırma yeterliliği
- [ ] Ölü uçlar (kullanılmayan ama basınçlı branşlar)
- [ ] Borularda kondansat birikimi (yetersiz eğim/drenaj)
- [ ] Destek ve izolasyon durumu

#### Talep Tarafı Kontrol Listesi
- [ ] Uygunsuz kullanımlar (açık üfleme, soğutma, kurutma, vakum üretimi)
- [ ] Basınç regülatörleri uygun ayarlı mı?
- [ ] Ekipman iyi durumda mı (silindirler, aletler)?
- [ ] Kullanılmayan ekipman hala bağlı ve hava tüketiyor mu?

### 2.5 Operatör Görüşmeleri

1. Hangi saatler/vardiyalarda hava talebi en yüksek?
2. Herhangi bir noktada basınç problemi var mı?
3. Son kaçak taraması ne zaman yapıldı?
4. Filtreler ne sıklıkla değişiyor?
5. Mevsimsel talep değişimleri var mı?
6. En büyük hava tüketicisi hangi ekipman?
7. Basınçlı havayı etkileyen gelecek planlar?
8. Kompresör davranışında değişiklik fark ettiniz mi?

## Adım 3: Veri Analizi

### 3.1 Yük Profili Analizi

```
Yük_faktörü = Ortalama_kW / Nominal_kW × 100 [%]

Load/unload kompresör için:
Yük% = T_yüklü / (T_yüklü + T_boşta) × 100

Gerçek_debi = Nominal_debi × Yük% / 100 [m³/min]
```

**Hesaplanacak metrikler:**
- Kompresör başına ortalama yük faktörü
- Pik talep / ortalama talep oranı
- Baz yük (minimum sürekli talep — genelde kaçak + sürekli prosesler)
- Üretim dışı talep (saf kaçak göstergesi)
- Yük değişkenliği (standart sapma)

### 3.2 Spesifik Güç Hesabı

```
SPC = Toplam_kW / Toplam_debi [kW/(m³/min), belirtilen basınçta]
```

#### Benchmark Karşılaştırması (7 bar)

| Kategori | SPC [kW/(m³/min)] | Değerlendirme |
|----------|-------------------|-------------|
| < 5.0 | En iyi uygulama | VSD, optimize, yeni ekipman |
| 5.0-5.5 | Çok iyi | İyi bakımlı modern sistem |
| 5.5-6.5 | İyi | Standart verimli |
| 6.5-7.5 | Ortalama | İyileştirme alanı var |
| 7.5-8.5 | Ortalamanın altı | Önemli tasarruf potansiyeli |
| > 8.5 | Kötü | Acil müdahale gerekli |

### 3.3 Exergy Analizi

ExergyLab engine kullanarak:
1. Exergy girişi hesapla (tüm kompresörlere toplam elektrik gücü)
2. Exergy çıkışı hesapla (kullanım noktalarında debi ağırlıklı basınç exergy'si)
3. Exergy yıkım dağılımını belirle:
   - Sıkıştırma tersinmezliği
   - Isı kaybı
   - Basınç düşüşleri
   - Kaçaklar
   - Kontrol kayıpları
4. Sistem exergy verimini benchmark ile karşılaştır
5. En büyük exergy yıkım kaynaklarını belirle

### 3.4 Kaçak Oranı Hesabı

Üretim dışı güç ölçümünden:
```
Kaçak_debisi = V̇_nominal × (P_üretimsiz / P_tam_yük) [m³/min]

Load/unload için:
Kaçak_debisi = V̇_nominal × [T_yüklü_üretimsiz / (T_yüklü + T_boşta)_üretimsiz]
```

Ultrasonik taramadan (bireysel kaçakların toplamı):
```
Toplam_kaçak = Σ(V̇_kaçak_i)
Kaçak% = Toplam_kaçak / V̇_toplam_talep × 100
```

## Adım 4: Raporlama

### Rapor Yapısı

#### 1. Yönetici Özeti (1 sayfa)
- Sistem genel bakışı (kompresör sayısı, toplam kapasite, yıllık enerji maliyeti)
- Temel bulgular (3-5 madde)
- Toplam tasarruf potansiyeli (kWh/yıl ve €/yıl)
- Öncelikli öneriler ve ROI
- Uygulama zaman çizelgesi özeti

#### 2. Sistem Tanımı (2-4 sayfa)
- Ekipman envanter tablosu
- Sistem şeması/yerleşimi
- Çalışma koşulları (basınç, vardiya, üretim)
- Kontrol stratejisi açıklaması

#### 3. Mevcut Durum Değerlendirmesi (3-5 sayfa)
- Enerji tüketimi analizi (kWh, maliyet, trend)
- Yük profili analizi (grafiklerle)
- Spesifik güç hesabı
- Sistem exergy verimi
- Benchmark karşılaştırması

#### 4. Bulgular ve Analiz (5-10 sayfa)
Her bulgu için:
- Açıklama, ölçüm verileri, fotoğraflar
- Mevcut durum niceliği
- Temel neden
- Etki (kWh/yıl, €/yıl, CO₂)

#### 5. İyileştirme Önerileri (3-5 sayfa)

Öncelik matrisi formatında:

| # | Öneri | Yatırım | Yıllık Tasarruf | Geri Ödeme | Öncelik |
|---|-------|---------|----------------|------------|---------|
| 1 | Kaçak onarımı | €2,000 | €15,000 | 0.1 yıl | YÜKSEK |
| 2 | Basınç optimizasyonu | €0 | €8,000 | 0 yıl | YÜKSEK |
| 3 | VSD retrofit | €25,000 | €12,000 | 2.1 yıl | ORTA |
| 4 | Isı geri kazanımı | €10,000 | €5,000 | 2.0 yıl | ORTA |

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
- **Faz 1:** Hızlı kazanımlar (0-3 ay) — kaçak, basınç, kontrol
- **Faz 2:** Orta vadeli (3-12 ay) — VSD, ısı geri kazanımı
- **Faz 3:** Uzun vadeli (1-3 yıl) — ekipman yenileme, sistem yeniden tasarım
- Tasarruf doğrulama izleme planı

#### 8. Ekler
- A: Ham ölçüm verileri (güç profilleri, basınç logları)
- B: Ekipman nameplate fotoğrafları
- C: Kaçak tarama logu (fotoğraflı)
- D: Hesaplama detayları
- E: Ekipman teknik şartnameleri (önerilmiş ise)

## Adım 5: Doğrulama ve Takip

### Uygulama Sonrası Doğrulama
- Öneri uygulandıktan sonra 1-4 haftalık güç profilleme
- Önceki/sonraki karşılaştırması
- IPMVP (International Performance Measurement and Verification Protocol) yöntemiyle doğrulama

### Sürekli İzleme KPI'ları

| KPI | Formül | Ölçüm Sıklığı |
|-----|--------|---------------|
| SPC | Toplam kW / Toplam m³/min | Aylık |
| Kaçak oranı | Kaçak debisi / Toplam debi | 6 ayda bir |
| Sistem exergy verimi | Ex_çıkış / Ex_giriş | Yıllık (denetimde) |
| Basınç kararlılığı | P_max - P_min | Sürekli |
| Enerji yoğunluğu | kWh / üretim birimi | Aylık |

## ISO 11011 — Genel Enerji Denetiminden (ISO 50002) Farkları

| Özellik | ISO 11011 | ISO 50002 |
|---------|-----------|-----------|
| Kapsam | Basınçlı hava spesifik | Genel enerji |
| KPI'lar | SPC, kaçak oranı, PDP | Genel enerji göstergeleri |
| Ölçüm yöntemleri | Basınçlı havaya özel rehberlik | Genel |
| Arz/talep | İkisi de zorunlu | Üretim odaklı |
| Hava kalitesi | Enerji ile birlikte değerlendirilir | Kapsam dışı |

## Tipik Bulgular ve Tasarruf Aralıkları

| Kategori | Tipik Bulgu | Tipik Tasarruf |
|----------|------------|---------------|
| Hava kaçakları | Toplam havanın %20-30'u kaçıyor | %10-25 |
| Basınç optimizasyonu | Sistem basıncı 1-2 bar yüksek | %6-14 |
| Kontrol iyileştirme | Kötü sıralama, geniş basınç bandı | %5-15 |
| Isı geri kazanımı | Giren enerjinin %70-94'ü atık ısı | Dolaylı tasarruf |
| Kurutucu optimizasyonu | Aşırı spesifike veya verimsiz kurutucu | %2-10 |
| Uygunsuz kullanım | Açık üfleme, vakum üretimi | %5-20 |
| Dağıtım | Yetersiz boru, ölü uçlar | %2-5 |

## İlgili Dosyalar
- Tüm ekipman dosyaları: `equipment/compressor_*.md`, `equipment/compressed_air_systems.md`
- Benchmark verileri: `benchmarks/compressor_benchmarks.md`
- Tüm çözüm dosyaları: `solutions/compressor_*.md`
- Exergy formülleri: `formulas/compressor_exergy.md`

## Referanslar
- ISO 11011:2013, "Compressed Air — Energy Efficiency — Assessment"
- ISO 50002:2014, "Energy Audits — Requirements with guidance for use"
- DOE/AMO, "Improving Compressed Air System Performance: A Sourcebook for Industry"
- Compressed Air Challenge, "Best Practices for Compressed Air Systems"
- British Compressed Air Society (BCAS), "Best Practice Guide"
- European Commission BREF, "Energy Efficiency"
- Carbon Trust, "Compressed Air — Opportunities for Businesses" (CTG027)
- IPMVP, "International Performance Measurement and Verification Protocol"
