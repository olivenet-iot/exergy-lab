# Enerji Yönetim Sistemleri (Energy Management Systems — ISO 50001)

> Son güncelleme: 2026-01-31

## Genel Bakış

Enerji yönetim sistemi (EnMS), bir organizasyonun enerji performansını sistematik olarak iyileştirmek için politika, süreç ve prosedürleri tanımlayan yapılandırılmış bir çerçevedir. ISO 50001:2018 standardı, Plan-Do-Check-Act (PDCA) döngüsüne dayalı küresel enerji yönetim sistemi standardıdır.

## 1. ISO 50001:2018 Yapısı (ISO 50001 Structure)

### 1.1 Yüksek Seviye Yapı (HLS — High Level Structure)

ISO 50001:2018, Annex SL yüksek seviye yapısını takip eder ve ISO 9001, ISO 14001 gibi diğer yönetim sistemi standartlarıyla entegre edilebilir.

| Madde | Başlık | İçerik |
|---|---|---|
| 4 | Organizasyonun bağlamı | İç/dış konular, ilgili taraflar, kapsam |
| 5 | Liderlik | Enerji politikası, rol/sorumluluklar, enerji ekibi |
| 6 | Planlama | Risk/fırsatlar, hedefler, eylem planları |
| 7 | Destek | Kaynaklar, yetkinlik, farkındalık, iletişim, dokümantasyon |
| 8 | Operasyon | Operasyonel planlama, tasarım, satın alma |
| 9 | Performans değerlendirme | İzleme, ölçüm, iç denetim, yönetim gözden geçirme |
| 10 | İyileştirme | Uygunsuzluk, düzeltici faaliyet, sürekli iyileştirme |

### 1.2 PDCA Döngüsü (Plan-Do-Check-Act)

```
PLAN (Planla) — Madde 4, 5, 6:
├── Enerji politikası oluştur
├── Enerji inceleme (energy review) yap
├── Önemli enerji kullanımlarını (SEU) belirle
├── Enerji temel çizgisini (EnB) oluştur
├── Enerji performans göstergelerini (EnPI) tanımla
├── Hedef ve eylem planları belirle
└── Yasal gereksinimleri belirle

DO (Uygula) — Madde 7, 8:
├── Kaynakları sağla
├── Yetkinlik ve farkındalık eğitimleri ver
├── Operasyonel kontrolleri uygula
├── Tasarım ve satın alma kriterlerini uygula
└── Eylem planlarını hayata geçir

CHECK (Kontrol et) — Madde 9:
├── EnPI'ları izle ve ölç
├── Enerji performansını değerlendir
├── İç denetim yap
└── Yönetim gözden geçirmesi yap

ACT (Önlem al) — Madde 10:
├── Uygunsuzlukları belirle ve düzelt
├── Kök neden analizi yap
├── Sürekli iyileştirme fırsatlarını değerlendir
└── Bir sonraki döngüyü planla
```

## 2. Enerji İnceleme (Energy Review)

### 2.1 Enerji İnceleme Süreci

```
Adım 1: Enerji tüketim analizi
- Son 12-36 aylık enerji verilerini topla
- Kaynak bazında dağılımı belirle (elektrik, gaz, fuel oil, vb.)
- Mevsimsel ve üretim bazlı trendleri analiz et

Adım 2: Önemli enerji kullanımlarını (SEU) belirle
- Enerji tüketim dağılımını çıkar (Pareto analizi)
- Toplam tüketimin %80'ini oluşturan kullanımları SEU olarak tanımla
- Her SEU için mevcut performansı değerlendir

Adım 3: İyileştirme fırsatlarını belirle
- Her SEU için tasarruf potansiyelini hesapla
- Teknik ve ekonomik fizibiliteyi değerlendir
- Önceliklendirme yap
```

### 2.2 Pareto Analizi Örneği

```
Orta ölçekli tekstil fabrikası — Enerji dağılımı:

| SEU | Enerji [MWh/yıl] | Pay [%] | Kümülatif [%] |
|-----|------------------|---------|---------------|
| Boyahane buharı | 4,200 | 28.0 | 28.0 |
| Kurutma | 2,850 | 19.0 | 47.0 |
| Basınçlı hava | 1,950 | 13.0 | 60.0 |
| Ram (terbiye) | 1,500 | 10.0 | 70.0 |
| Aydınlatma + HVAC | 1,200 | 8.0 | 78.0 |
| Motorlar (genel) | 1,050 | 7.0 | 85.0 |
| Kazan yardımcıları | 750 | 5.0 | 90.0 |
| Diğer | 1,500 | 10.0 | 100.0 |
| TOPLAM | 15,000 | 100.0 | — |

SEU'lar: Boyahane buharı, kurutma, basınçlı hava, ram, aydınlatma+HVAC
(ilk 5 kalem toplam tüketimin %78'i)
```

## 3. Enerji Performans Göstergeleri — EnPI (Energy Performance Indicators)

### 3.1 EnPI Seçimi

Her SEU için en az bir EnPI tanımlanmalıdır:

| SEU | Önerilen EnPI | Formül | Birim |
|---|---|---|---|
| Buhar sistemi | Spesifik buhar tüketimi | ton_buhar / ton_ürün | ton/ton |
| Basınçlı hava | Spesifik güç (SPC) | kW_elekt / (m³/min) | kW/(m³/min) |
| Soğutma | COP veya kW/TR | kW_soğutma / kW_elekt | — |
| Aydınlatma | Güç yoğunluğu | kW / m² | W/m² |
| Genel fabrika | SEC | kWh_toplam / ton_ürün | kWh/ton |

### 3.2 EnPI İzleme Periyotları

| EnPI Türü | İzleme Sıklığı | Veri Kaynağı |
|---|---|---|
| Toplam SEC | Aylık | Faturalar + üretim verileri |
| Alt sistem EnPI | Haftalık/aylık | Alt sayaçlar |
| Ekipman EnPI | Günlük/anlık | BMS/SCADA |
| Exergy verimi | Aylık/çeyreklik | Hesaplama |
| CUSUM | Aylık | Regresyon modeli |

## 4. Enerji Temel Çizgisi — EnB (Energy Baseline)

### 4.1 Baseline Oluşturma

```
EnB oluşturma adımları:
1. Temel çizgi dönemi seçimi (minimum 12 ay)
2. Enerji verileri ile ilgili değişkenleri eşleştirme
3. İstatistiksel model oluşturma (regresyon analizi)
4. Modeli doğrulama (R², CV-RMSE, NMBE)

Regresyon modeli:
E = β₀ + β₁ × P + β₂ × HDD + β₃ × CDD + ε

Doğrulama kriterleri (ASHRAE Guideline 14):
- R² ≥ 0.75 (aylık veri)
- CV-RMSE ≤ %25 (aylık veri)
- NMBE ≤ ±%10
```

### 4.2 Baseline Ayarlama

```
EnB ayarlanması gerekli durumlar:
1. Üretim kapasitesi değişikliği (>%10)
2. Yeni ürün/proses eklenmesi
3. Bina/tesis genişlemesi
4. Enerji kaynağı değişikliği
5. Önemli ekipman değişikliği

Ayarlama yöntemi:
E_baz_ayarlanmış = β₀ + β₁ × P_raporlama + β₂ × HDD_raporlama + β₃ × CDD_raporlama

Tasarruf = E_baz_ayarlanmış - E_gerçek_raporlama
```

### 4.3 Hesaplama Örneği

```
Gıda fabrikası — Aylık veri ile regresyon:

E [MWh/ay] = 120 + 2.8 × P [ton/ay] + 0.5 × HDD

R² = 0.92, CV-RMSE = %12

Nisan ayı:
P = 300 ton, HDD = 120
E_baz = 120 + 2.8 × 300 + 0.5 × 120 = 120 + 840 + 60 = 1,020 MWh
E_gerçek = 960 MWh

Tasarruf = 1,020 - 960 = 60 MWh (%5.9)
```

## 5. Önemli Enerji Kullanımları — SEU (Significant Energy Uses)

### 5.1 SEU Belirleme Kriterleri

| Kriter | Açıklama | Eşik |
|---|---|---|
| Toplam enerji payı | Tüketim büyüklüğü | >%5 |
| Tasarruf potansiyeli | İyileştirme fırsatı | >%10 iyileştirme |
| Değişkenlik | Tüketim dalgalanması | >%20 varyasyon |
| Kontrol edilebilirlik | Operasyonel kontrol imkânı | Yüksek |
| Stratejik önem | Kurumsal hedeflerle uyum | Yüksek |

### 5.2 SEU İçin Gerekli Bilgiler

```
Her SEU için:
1. Mevcut enerji performansı (ölçülmüş)
2. İlgili değişkenler (üretim, hava, vardiya vb.)
3. İlgili personel (operatörler, bakım ekibi)
4. Mevcut kontrol yöntemleri
5. İyileştirme fırsatları listesi
6. EnPI tanımı ve hedef değer
```

## 6. Operasyonel Kontroller (Operational Controls)

### 6.1 Operasyonel Kontrol Matrisi

| Sistem | Kontrol Parametresi | Hedef Aralık | İzleme |
|---|---|---|---|
| Kazan | Baca gazı O₂ | %2.0-3.0 | Sürekli (O₂ trim) |
| Kazan | Baca gazı sıcaklığı | <180°C | Sürekli |
| Kompresör | Sistem basıncı | 6.5-7.0 bar | Sürekli |
| Kompresör | Kaçak oranı | <%15 | 6 ayda bir |
| Chiller | CHW giriş/çıkış sıcaklığı | 12/7°C | Sürekli |
| Chiller | Kondenser yaklaşım | <3°C | Haftalık |
| Aydınlatma | Çalışma saatleri | Vardiya programına göre | Otomatik |
| HVAC | İç mekân sıcaklığı | 20-24°C (kış), 24-26°C (yaz) | Sürekli |

### 6.2 Sapma Yönetimi

```
Sapma tespit ve müdahale süreci:

1. İzleme: EnPI'ları düzenli kontrol et
2. Tespit: Hedef aralık dışına çıkış
3. Bildirim: İlgili personele alarm/bildirim
4. Analiz: Sapma nedenini araştır
5. Müdahale: Düzeltici faaliyet uygula
6. Doğrulama: Normal çalışmaya dönüşü doğrula
7. Kayıt: Olayı ve çözümü dokümante et
```

## 7. Enerji Satın Alma ve Tasarım

### 7.1 Enerji Verimli Satın Alma Kriterleri

| Ekipman | Minimum Verimlilik | Standart |
|---|---|---|
| Elektrik motoru | IE3 (>0.75 kW), IE4 önerilir | IEC 60034-30-1 |
| Kompresör | SPC <6.0 kW/(m³/min) @7 bar | ISO 1217 |
| Kazan | Enerji verimi >%90 (LHV) | EN 12953 |
| Chiller | COP >5.0 (su soğutmalı) | EN 14511 |
| Aydınlatma | LED, >130 lm/W | EN 13201 |
| Pompa | MEI ≥0.7 | EU 547/2012 |
| VSD | IE2 sınıfı | EN 61800-9-2 |

### 7.2 Yaşam Döngüsü Maliyet (LCC) Yaklaşımı

```
Satın alma kararında LCC kullanımı:

LCC = Yatırım + Σ(Enerji_maliyetiᵢ / (1+r)ⁱ) + Σ(Bakım_maliyetiᵢ / (1+r)ⁱ)

Tipik enerji/toplam maliyet oranları (20 yıl):
- Motor: %95 enerji, %5 satın alma
- Kompresör: %75-80 enerji, %15-20 satın alma
- Kazan: %85-90 yakıt, %5-10 satın alma
- Pompa: %85 enerji, %10 satın alma, %5 bakım
```

## 8. Türkiye Enerji Yönetimi Mevzuatı

### 8.1 Yasal Zorunluluklar

```
Enerji Verimliliği Kanunu (No. 5627):

Yıllık enerji tüketimi ≥ 1,000 TEP olan sanayi işletmeleri:
1. Enerji yöneticisi atamak (zorunlu)
2. 4 yılda bir enerji etüdü yaptırmak
3. Yıllık enerji tüketim raporu YEGM'e bildirmek
4. Enerji verimlilik hedeflerine uymak

Yıllık enerji tüketimi ≥ 50,000 TEP:
1. Enerji yönetim birimi kurmak
2. ISO 50001 belgelendirme (teşvik kapsamında)
3. Enerji yoğunluğunu azaltma taahhüdü
```

### 8.2 Enerji Yöneticisi Yetkinlikleri

| Yetkinlik | Gereksinim |
|---|---|
| Eğitim | Mühendislik veya teknik bölüm lisans |
| Sertifika | YEGM onaylı enerji yöneticisi sertifikası |
| Deneyim | Minimum 2 yıl enerji alanında |
| Sürekli gelişim | 3 yılda bir yenileme eğitimi |

### 8.3 VAP ve Gönüllü Anlaşma

```
VAP (Verimlilik Artırıcı Proje):
- Yatırımın %30'una kadar devlet desteği (max 5M TL)
- Geri ödeme süresi <5 yıl olan projeler
- YEGM tarafından değerlendirme ve onay

Gönüllü Anlaşma:
- 3 yılda %10 enerji yoğunluğu azaltma taahhüdü
- Karşılığında vergi ve harç muafiyetleri
- EVD şirketleri tarafından izleme ve doğrulama
```

## 9. ISO 50001 Uygulama Performans Göstergeleri

| Performans Kriteri | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| Yıllık enerji tasarrufu | <%2 | %2-5 | %5-10 | >%10 |
| EnPI izleme sıklığı | Yıllık | Aylık | Haftalık | Gerçek zamanlı |
| SEU kapsamı | <%50 | %50-70 | %70-90 | >%90 |
| Çalışan farkındalığı | Düşük | Orta | Yüksek | Kültürel |
| Yönetim katılımı | Pasif | Destekleyici | Aktif | Lider |

## İlgili Dosyalar

- [Metodoloji](methodology.md) — Fabrika enerji audit metodolojisi
- [KPI Tanımları](kpi_definitions.md) — EnPI detaylı tanımlar
- [Ekonomik Analiz](economic_analysis.md) — Yatırım analizi metodları
- [Ölçüm ve Doğrulama](measurement_verification.md) — IPMVP protokolleri
- [Performans Göstergeleri](performance_indicators.md) — Hedefler ve izleme
- [Uygulama](implementation.md) — Uygulama stratejileri ve engeller

## Referanslar

- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- ISO 50003:2021, "Energy management systems — Requirements for bodies providing audit and certification"
- ISO 50004:2020, "Energy management systems — Guidance for the implementation, maintenance and improvement"
- ISO 50006:2014, "Measuring energy performance using energy baselines (EnB) and energy performance indicators (EnPI)"
- Türkiye Enerji Verimliliği Kanunu (No. 5627) ve ilgili yönetmelikler
- YEGM, "Enerji Yönetimi Uygulama Rehberi"
- US DOE, "Superior Energy Performance (SEP) Program"
