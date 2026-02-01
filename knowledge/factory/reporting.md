# Enerji Audit Raporlama (Energy Audit Reporting)

> Son güncelleme: 2026-01-31

## Genel Bakış

Enerji audit raporunun kalitesi, teknik analizin doğruluğu kadar önemlidir. İyi yazılmış bir rapor; karar vericileri ikna eder, uygulama ekiplerine yol gösterir ve kurumsal hafıza oluşturur. Bu dosya; rapor yapısı ve şablonları, yönetici özeti formatı, bulguların sunumu, öneri formatlama yöntemleri, finansal özet tabloları, uygulama yol haritası formatı, görsel iletişim ilkeleri ve rapor kalite kontrol listesini kapsar. ASHRAE, ISO 50002, Türkiye YEGM ve müşteriye özel format standartları ele alınmaktadır.

## 1. Rapor Yapısı ve Formatlar (Report Structure)

### 1.1 Genel Rapor Yapısı

```
Enerji Audit Raporu — Standart Bölümler:

Ön Kısım:
  1. Kapak sayfası (Tesis adı, tarih, audit seviyesi, hazırlayan)
  2. İçindekiler
  3. Yönetici özeti (Executive Summary) — 1-2 sayfa
  4. Kısaltmalar ve tanımlar

Ana Kısım:
  5. Tesis tanımı ve genel bilgiler
  6. Enerji tüketim analizi (fatura analizi, enerji dengesi)
  7. Sistem bazlı detaylı analiz
     7.1 Kazan/buhar sistemi
     7.2 Basınçlı hava sistemi
     7.3 Soğutma sistemi
     7.4 Pompa sistemi
     7.5 Aydınlatma
     7.6 HVAC
     7.7 Proses sistemleri
  8. Exergy analizi (varsa)
  9. Bulgular ve öneriler
  10. Ekonomik analiz ve önceliklendirme
  11. Uygulama yol haritası

Ek Kısım:
  12. Ölçüm verileri ve grafikler
  13. Hesaplama detayları
  14. Ekipman listeleri
  15. Fotoğraflar ve termografik görüntüler
```

### 1.2 Format Standartları Karşılaştırma

| Özellik | ASHRAE | ISO 50002 | YEGM (Türkiye) | Müşteriye Özel |
|---|---|---|---|---|
| Audit seviyesi | Level I/II/III | Detaylı/Genel | Detaylı (zorunlu) | Değişken |
| Minimum kapsam | Elektrik, gaz, su | Tüm enerji kaynakları | Tüm kaynaklar + exergy | Anlaşmaya bağlı |
| Ekonomik analiz | SPP, LCC | SPP, NPV, IRR | SPP, NPV zorunlu | Genellikle SPP+NPV |
| Yönetici özeti | Önerilen | Zorunlu | Zorunlu | Zorunlu |
| Ölçüm verileri | Level II/III'te | Zorunlu | Zorunlu (ham veri) | Özet yeterli |
| Exergy analizi | Opsiyonel | Opsiyonel | Zorunlu (>1000 TEP) | Nadiren istenir |
| Rapor dili | İngilizce | Yerel | Türkçe (zorunlu) | Müşteri tercihi |
| Sayfa sayısı (tipik) | 30-100 | 40-120 | 60-200 | 20-80 |

## 2. Yönetici Özeti Şablonu (Executive Summary Template)

### 2.1 Tek Sayfa Yönetici Özeti

```
[TESİS ADI] — ENERJİ AUDIT RAPORU YÖNETİCİ ÖZETİ

Audit Bilgileri:
  Tesis: [Tesis adı ve konumu]
  Sektör: [Sektör / alt sektör]
  Audit seviyesi: [ASHRAE Level II / ISO 50002 Detaylı]
  Audit tarihi: [GG.AA.YYYY — GG.AA.YYYY]
  Hazırlayan: [Firma / Mühendis adı]

Mevcut Durum:
  Yıllık enerji tüketimi: [X,XXX,XXX kWh] (elektrik) + [X,XXX,XXX Nm³] (doğalgaz)
  Yıllık enerji maliyeti: €[X,XXX,XXX]
  Spesifik enerji tüketimi (SEC): [X.XX kWh/ton]
  Sektör benchmark: [X.XX kWh/ton] (ortalama) / [X.XX kWh/ton] (en iyi uygulama)
  Exergy verimliliği: %[XX]
  Performans sınıfı: [Düşük / Ortalama / İyi / Mükemmel]

Temel Bulgular:
  1. [En önemli bulgu — 1 cümle]
  2. [İkinci bulgu — 1 cümle]
  3. [Üçüncü bulgu — 1 cümle]

Toplam Tasarruf Potansiyeli:
  Enerji tasarrufu: [X,XXX,XXX kWh/yıl] (%[XX] azaltma)
  Maliyet tasarrufu: €[XXX,XXX]/yıl
  CO₂ azaltma: [X,XXX ton CO₂/yıl]
  Toplam yatırım: €[XXX,XXX]
  Ortalama geri ödeme: [X.X yıl]
  Toplam NPV (15 yıl): €[X,XXX,XXX]

Öncelikli Projeler (Top 5):
  | # | Proje | Tasarruf [€/yıl] | Yatırım [€] | SPP [yıl] |
  |---|-------|------------------|-------------|-----------|
  | 1 | [Proje adı] | [€XX,XXX] | [€XX,XXX] | [X.X] |
  | 2 | [Proje adı] | [€XX,XXX] | [€XX,XXX] | [X.X] |
  | 3 | [Proje adı] | [€XX,XXX] | [€XX,XXX] | [X.X] |
  | 4 | [Proje adı] | [€XX,XXX] | [€XX,XXX] | [X.X] |
  | 5 | [Proje adı] | [€XX,XXX] | [€XX,XXX] | [X.X] |
  | TOPLAM | | [€XXX,XXX] | [€XXX,XXX] | [X.X] |

Önerilen Uygulama Takvimi:
  Hemen (0-3 ay): [Quick wins — düşük/sıfır yatırımlı önlemler]
  Kısa vade (3-12 ay): [Orta yatırımlı projeler]
  Orta vade (1-3 yıl): [Stratejik yatırımlar]
```

## 3. Bulgu Tablosu Formatı (Findings Table)

### 3.1 Sistem Bazlı Bulgu Özeti

| Sistem | Mevcut Durum | Benchmark | Boşluk | Tasarruf Potansiyeli | Öncelik |
|---|---|---|---|---|---|
| Kazan/Buhar | η=%84, Exη=%32 | η>%90, Exη>%40 | %6 / 8 puan | €45,000/yıl | Yüksek |
| Basınçlı hava | 7.2 kW/(Nm³/dk) | <6.0 kW/(Nm³/dk) | %17 | €28,000/yıl | Yüksek |
| Soğutma | COP=3.8, ExCOP=0.28 | COP>5.0, ExCOP>0.35 | %24 / 7 puan | €15,000/yıl | Orta |
| Pompa | η=%55 | η>%70 | %15 | €12,000/yıl | Orta |
| Aydınlatma | 12 W/m², T8 | <6 W/m², LED | %50 | €9,000/yıl | Düşük-Orta |
| HVAC | EUI: 180 kWh/m² | EUI<120 kWh/m² | %33 | €7,000/yıl | Düşük |
| **TOPLAM** | | | | **€116,000/yıl** | |

### 3.2 Detaylı Bulgu Kartı Şablonu

```
BULGU KARTI — [Bulgu No: F-XX]

Başlık: [Kısa ve açıklayıcı başlık]
Sistem: [Kazan / Kompresör / Chiller / Pompa / vb.]
Önem derecesi: [Kritik / Yüksek / Orta / Düşük]
Fotoğraf/Görsel: [Referans no veya gömülü]

Mevcut Durum:
  [2-3 cümle ile mevcut durumun teknik tanımı]
  [Ölçüm verileri ve gözlemler]

Sorun/Fırsat:
  [Ne oluyor ve neden sorun? Veya ne yapılabilir?]
  [Enerji kaybı miktarı ve maliyeti]

Performans Verisi:
  | Parametre | Mevcut | Hedef/Benchmark | Fark |
  |-----------|--------|-----------------|------|
  | [Param 1] | [Değer] | [Değer] | [%XX] |
  | [Param 2] | [Değer] | [Değer] | [%XX] |

Enerji/Maliyet Etkisi:
  Enerji kaybı: [XX,XXX kWh/yıl] ([Elektrik/Gaz])
  Maliyet etkisi: €[XX,XXX]/yıl
  CO₂ etkisi: [XX ton CO₂/yıl]
```

## 4. Öneri Kartı Şablonu (Recommendation Card Template)

### 4.1 Detaylı Öneri Formatı

```
ÖNERİ KARTI — [Öneri No: R-XX]

Başlık: [Kısa ve anlaşılır öneri başlığı]
İlgili bulgu: [F-XX referansı]
Sistem: [Sistem adı]
Kategori: [Quick Win / Orta Vade / Stratejik]
Uygulama zorluğu: [Kolay / Orta / Zor]

Açıklama:
  [Önerinin detaylı teknik tanımı — 3-5 cümle]
  [Uygulama yöntemi ve gereksinimler]

Teknik Detay:
  Mevcut: [Mevcut ekipman/durum]
  Önerilen: [Önerilen ekipman/durum]
  Teknik parametreler: [Boyut, kapasite, verim vb.]

Enerji Tasarrufu:
  Elektrik: [XX,XXX kWh/yıl]
  Doğalgaz: [XX,XXX Nm³/yıl]
  Toplam (birincil): [XX,XXX kWh/yıl]
  Tasarruf oranı: %[XX] (sistem bazında)

Ekonomik Analiz:
  Yatırım maliyeti: €[XX,XXX]
    - Ekipman: €[XX,XXX]
    - Montaj: €[XX,XXX]
    - Mühendislik: €[XX,XXX]
  Yıllık tasarruf: €[XX,XXX]
  Yıllık bakım (ek): €[X,XXX]
  Net yıllık fayda: €[XX,XXX]
  SPP: [X.X yıl]
  NPV (15 yıl, %8): €[XX,XXX]
  IRR: %[XX]

Çevresel Etki:
  CO₂ azaltma: [XXX ton/yıl]
  Diğer: [Gürültü azaltma, su tasarrufu vb.]

Risk ve Engeller:
  - [Risk 1 ve azaltma yöntemi]
  - [Risk 2 ve azaltma yöntemi]

Uygulama Takvimi:
  Hazırlık: [X hafta/ay]
  Tedarik: [X hafta/ay]
  Montaj: [X hafta/ay]
  Devreye alma: [X hafta/ay]
  Toplam: [X ay]

Doğrulama (M&V):
  IPMVP Opsiyon: [A / B / C / D]
  Ölçüm yöntemi: [Kısa açıklama]
  Beklenen belirsizlik: ±%[XX]
```

## 5. Finansal Özet Tablosu Formatı (Financial Summary)

### 5.1 Proje Portföyü Finansal Özet

| # | Öneri | Kategori | Yatırım [€] | Tasarruf [€/yıl] | SPP [yıl] | NPV [€] | IRR [%] | CO₂ [t/yıl] | Öncelik |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | Kaçak onarımı | Quick Win | 3,000 | 22,000 | 0.14 | 135,000 | >%500 | 48 | 1-Acil |
| R-02 | Hat basıncı düşürme | Quick Win | 500 | 12,000 | 0.04 | 75,000 | >%500 | 26 | 1-Acil |
| R-03 | Buhar kapanı değişimi | Quick Win | 8,000 | 18,000 | 0.44 | 104,000 | >%200 | 95 | 1-Acil |
| R-04 | Kompresör VSD | Orta Vade | 22,000 | 14,500 | 1.52 | 62,000 | %65 | 32 | 2-Yüksek |
| R-05 | Economizer | Orta Vade | 38,000 | 15,000 | 2.53 | 54,000 | %38 | 79 | 2-Yüksek |
| R-06 | LED aydınlatma | Orta Vade | 30,000 | 11,000 | 2.73 | 35,000 | %35 | 24 | 3-Normal |
| R-07 | Chiller optimizasyonu | Orta Vade | 18,000 | 8,000 | 2.25 | 30,000 | %43 | 17 | 3-Normal |
| R-08 | Isı geri kazanımı | Stratejik | 65,000 | 25,000 | 2.60 | 95,000 | %38 | 132 | 2-Yüksek |
| R-09 | Motor değişimi | Stratejik | 45,000 | 12,000 | 3.75 | 28,000 | %25 | 26 | 3-Normal |
| R-10 | CHP (kojenerasyon) | Stratejik | 400,000 | 95,000 | 4.21 | 240,000 | %22 | 350 | 4-Planlı |
| | **TOPLAM** | | **€629,500** | **€232,500** | **2.71** | **€858,000** | | **829** | |

### 5.2 Kategori Bazlı Finansal Özet

| Kategori | Proje Sayısı | Toplam Yatırım [€] | Yıllık Tasarruf [€] | Ort. SPP [yıl] | Toplam NPV [€] |
|---|---|---|---|---|---|
| Quick Win (0-3 ay) | 3 | 11,500 | 52,000 | 0.22 | 314,000 |
| Orta Vade (3-12 ay) | 4 | 108,000 | 48,500 | 2.23 | 181,000 |
| Stratejik (1-3 yıl) | 3 | 510,000 | 132,000 | 3.86 | 363,000 |
| **TOPLAM** | **10** | **€629,500** | **€232,500** | **2.71** | **€858,000** |

## 6. Uygulama Zaman Çizelgesi Şablonu (Implementation Timeline)

### 6.1 Gantt Tarzı Zaman Çizelgesi

```
Uygulama yol haritası:

              Q1/2026  Q2/2026  Q3/2026  Q4/2026  Q1/2027  Q2/2027
R-01 Kaçak    ████
R-02 Basınç   ██
R-03 Kapan    ████████
R-04 VSD               ████████████
R-05 Econo              ████████████████
R-06 LED                         ████████████
R-07 Chiller                     ████████
R-08 Isı GK                              ████████████████
R-09 Motor                                        ████████████
R-10 CHP                                          ████████████████████

Semboller:
  ██ = Aktif uygulama dönemi
  Boşluk = Planlama/tedarik

Kümülatif tasarruf (tahmini):
  Q1/2026 sonu: €13,000/çeyrek → €52,000/yıl
  Q2/2026 sonu: €25,000/çeyrek → €100,000/yıl
  Q4/2026 sonu: €45,000/çeyrek → €180,000/yıl
  Q2/2027 sonu: €58,000/çeyrek → €232,500/yıl (tam etki)
```

## 7. Görsel İletişim İlkeleri (Visual Communication)

### 7.1 Grafik Türü Seçimi

| Veri Türü | Önerilen Grafik | Kullanım | Kaçınılacak |
|---|---|---|---|
| Zaman serisi (SEC trend) | Çizgi grafik | Trend gösterimi, hedef çizgisi | 3D grafik |
| Enerji dağılımı | Pasta/halka grafik | Max 7 dilim | Çok dilimli pasta |
| Sistem karşılaştırma | Yatay bar grafik | Benchmark çizgisi ile | Yığılmış bar (karmaşık) |
| Enerji-üretim ilişkisi | Scatter plot | Regresyon çizgisi ile | Bağlantısız noktalar |
| Tasarruf fırsatları | Pareto grafik | %80/20 kuralı | Sıralamasız bar |
| Enerji akışı | Sankey diyagram | Fabrika enerji dengesi | Karmaşık, çok akışlı |
| Isı kayıpları | Termografik görüntü | Önce/sonra karşılaştırma | İşaretsiz görüntü |
| Ekonomik karşılaştırma | Balon grafik (SPP vs NPV vs yatırım) | Çoklu boyut | 2D tablo (yeterli değil) |

### 7.2 Renk Kodlaması Standartları

```
Tutarlı renk kodlaması rapor genelinde:

Performans renkleri:
  Kırmızı (#E74C3C): Kritik / acil müdahale / hedefin çok altında
  Turuncu (#F39C12): Düşük / uyarı / hedefin altında
  Sarı (#F1C40F): Ortalama / dikkat / sınırda
  Yeşil (#27AE60): İyi / hedefte / kabul edilebilir
  Mavi (#2980B9): Mükemmel / hedefin üzerinde

Enerji kaynağı renkleri:
  Sarı (#F39C12): Elektrik
  Mavi (#3498DB): Doğalgaz
  Gri (#95A5A6): Kömür
  Yeşil (#2ECC71): Biyokütle / yenilenebilir
  Kırmızı (#E74C3C): Fuel oil / dizel

Eylem renkleri:
  Yeşil: Quick win — hemen uygula
  Mavi: Orta vade — planlı uygulama
  Mor: Stratejik — uzun vadeli yatırım
```

## 8. Rapor Kalite Kontrol Listesi

### 8.1 Teknik Kalite Kontrol

| Kontrol Maddesi | Durum | Not |
|---|---|---|
| Enerji dengesi tutarlı mı? (Girdi ≈ Çıktı + Kayıp, fark <%10) | ☐ | |
| SEC hesaplamaları doğru mu? (birim kontrolü) | ☐ | |
| Benchmark değerleri güncel ve kaynaklı mı? | ☐ | |
| Ölçüm belirsizlikleri belirtilmiş mi? | ☐ | |
| Tasarruf hesaplamaları tekrarlanabilir mi? (formüller + veriler) | ☐ | |
| Ekonomik analiz tutarlı mı? (SPP, NPV, IRR çapraz kontrol) | ☐ | |
| Exergy analizi (varsa) metodolojik olarak doğru mu? | ☐ | |
| Tüm varsayımlar açıkça belirtilmiş mi? | ☐ | |
| Birimler tutarlı mı? (SI sistemi, €, kWh) | ☐ | |
| Fotoğraflar ve termografik görüntüler açıklayıcı mı? | ☐ | |

### 8.2 Sunum Kalite Kontrol

| Kontrol Maddesi | Durum | Not |
|---|---|---|
| Yönetici özeti tek başına anlaşılır mı? | ☐ | |
| Teknik jargon açıklanmış mı? | ☐ | |
| Grafikler eksen etiketli ve başlıklı mı? | ☐ | |
| Tablolarda birimler belirtilmiş mi? | ☐ | |
| Sayfa numaralandırma ve çapraz referanslar doğru mu? | ☐ | |
| Yazım ve dil bilgisi kontrol edilmiş mi? | ☐ | |
| Müşteri/tesis gizlilik politikasına uygun mu? | ☐ | |
| Rapor müşterinin beklentilerine ve kapsam sözleşmesine uygun mu? | ☐ | |
| Uygulama önerileri açık ve uygulanabilir mi? | ☐ | |
| Önceliklendirme mantıklı ve gerekçeli mi? | ☐ | |

### 8.3 Yasal ve Standart Uyumluluk

| Kontrol Maddesi | Standart | Durum |
|---|---|---|
| ISO 50002 zorunlu bölümleri mevcut mu? | ISO 50002:2014 | ☐ |
| ASHRAE audit seviyesi gereksinimleri karşılanıyor mu? | ASHRAE Procedures | ☐ |
| YEGM rapor formatına uygun mu? | Enerji Verimlilik Kanunu | ☐ |
| Mühendis yetki belgeleri eklenmiş mi? | YEGM Yönetmeliği | ☐ |
| Ölçüm cihazı kalibrasyon sertifikaları mevcut mu? | ISO 17025 | ☐ |
| Gizlilik/NDA koşullarına uyulmuş mu? | Sözleşme | ☐ |

## İlgili Dosyalar

- [Ölçüm ve Doğrulama](measurement_verification.md) — M&V rapor formatları ve tasarruf doğrulama
- [Ekonomik Analiz](economic_analysis.md) — SPP, NPV, IRR hesaplama yöntemleri
- [Performans Göstergeleri](performance_indicators.md) — KPI tanımları ve hedefler
- [Fabrika Benchmarkları](factory_benchmarks.md) — Sektörel karşılaştırma verileri
- [Uygulama](implementation.md) — Uygulama yol haritası ve değişim yönetimi
- [Veri Toplama](data_collection.md) — Ölçüm cihazları ve veri kalitesi
- [Metodoloji](methodology.md) — Audit metodolojisi ve seviyeleri
- [KPI Tanımları](kpi_definitions.md) — Performans gösterge tanımları
- [Kazan Audit](../boiler/audit.md) — Kazan audit prosedürü
- [Kompresör Audit](../compressor/audit.md) — Kompresör audit prosedürü
- [Chiller Audit](../chiller/audit.md) — Chiller audit prosedürü

## Referanslar

- ISO 50002:2014, "Energy audits — Requirements with guidance for use"
- ASHRAE, "Procedures for Commercial Building Energy Audits," 2nd Edition, 2011
- EN 16247-1:2012, "Energy audits — Part 1: General requirements"
- EN 16247-3:2014, "Energy audits — Part 3: Processes"
- T.C. Resmi Gazete, "Enerji Verimliliği Kanunu (5627)," 2007
- T.C. Resmi Gazete, "Enerji Kaynaklarının ve Enerjinin Kullanımında Verimliliğin Artırılmasına Dair Yönetmelik," 2008
- Turner, W.C. & Doty, S., "Energy Management Handbook," 9th Edition, Fairmont Press, 2013
- Thumann, A. & Younger, W., "Handbook of Energy Audits," 9th Edition, Fairmont Press, 2012
- Capehart, B.L., Turner, W.C. & Kennedy, W.J., "Guide to Energy Management," 8th Edition, Fairmont Press, 2016
- Tufte, E.R., "The Visual Display of Quantitative Information," Graphics Press, 2001
