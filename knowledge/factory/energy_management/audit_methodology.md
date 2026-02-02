---
title: "Enerji Denetimi Pratik Rehberi (Energy Audit Practical Guide)"
category: factory
equipment_type: factory
keywords: [enerji denetimi, energy audit, saha çalışması, checklist, ölçüm, ExergyLab, veri toplama, denetim planı]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/audit_levels.md, factory/energy_management/iso_50002.md, factory/energy_management/en_16247.md, factory/methodology.md, factory/data_collection.md]
use_when: ["Enerji denetimi planlandığında", "Saha çalışması checklist'i gerektiğinde", "ExergyLab ile denetim entegrasyonu sorgulandığında"]
priority: high
last_updated: 2026-02-01
---

# Enerji Denetimi Pratik Rehberi (Energy Audit Practical Guide)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

Bu dosya, endüstriyel enerji denetiminin saha uygulamasına yönelik pratik bir rehberdir. Mevcut `methodology.md` dosyası teorik çerçeveyi, `audit_levels.md` dosyası denetim seviyelerini (ASHRAE Level I/II/III) ele alırken, bu rehber tamamen sahaya odaklanır: denetim öncesi hazırlık, saha çalışması checklist'leri, ölçüm cihazı seçimi, ExergyLab entegrasyonu, rapor yapısı ve yaygın hataların önlenmesini kapsar.

Pratik denetim rehberinin amacı, denetçiye adım adım izlenecek bir yol haritası sunarak denetim kalitesini standartlaştırmak ve tekrar edilebilir sonuçlar elde etmektir. Türkiye'deki YEGM enerji etüdü gereksinimleri ile uluslararası standartlar (ISO 50002, EN 16247) gözetilmiştir.

```
Denetim süreç özeti:
Hazırlık (2 hafta) → Saha çalışması (3-5 gün) → Analiz (2-4 hafta) → Raporlama (1-2 hafta)
```

## 2. Denetim Öncesi Hazırlık (Pre-Audit Preparation)

### 2.1 Veri Talep Listesi (Data Request Checklist)

Denetimden en az 2 hafta önce tesisten aşağıdaki veriler talep edilmelidir:

| No | Veri Kalemi | Süre / Detay | Öncelik |
|----|-------------|--------------|---------|
| 1 | Enerji faturaları (elektrik) | Son 24 ay, aylık | Kritik |
| 2 | Enerji faturaları (doğalgaz / sıvı yakıt) | Son 24 ay, aylık | Kritik |
| 3 | Üretim verileri | Son 24 ay, aylık üretim miktarı + birim | Kritik |
| 4 | Ekipman envanteri | Nameplate verileri, yaş, kapasite | Yüksek |
| 5 | Proses akış şeması (PFD) | Güncel, ana ekipmanlar ve akışlar | Yüksek |
| 6 | Tesis yerleşim planı (layout) | Ölçekli, ekipman konumları | Yüksek |
| 7 | SCADA / BMS ekran görüntüleri | Tipik çalışma koşulları | Orta |
| 8 | Önceki enerji etüdü raporları | Varsa, son 5 yıl | Orta |
| 9 | Bakım kayıtları | Son 12 ay, ana ekipmanlar | Orta |
| 10 | Çalışma takvimi | Vardiya, tatil, sezon, duruş planı | Orta |
| 11 | Su faturaları | Son 12 ay | Düşük |
| 12 | Mevcut EnMS dokümanları | ISO 50001 varsa | Düşük |

### 2.2 Ön Analiz (Preliminary Analysis)

```
Saha ziyaretinden önce yapılacak ön analiz:

1. Enerji tüketim profili:
   ├── Aylık elektrik ve yakıt tüketim grafiği
   ├── Mevsimsel patern tespiti
   ├── Taban yük (baseload) belirleme
   └── Spesifik enerji tüketimi (SEC): kWh/ton ürün

2. Enerji maliyet dağılımı:
   ├── Kaynak bazlı maliyet (elektrik vs yakıt)
   ├── Talep (demand) maliyeti oranı
   ├── Reaktif enerji cezası
   └── Toplam enerji maliyeti / ciro oranı

3. Benchmark kontrolü:
   ├── Sektörel SEC karşılaştırma
   ├── Sapma yüzdesini hesapla
   └── Odaklanılacak alanları ön belirle

4. Enerji dengesi tahmini:
   ├── Fatura verilerinden yaklaşık denge
   ├── Büyük tüketicileri tahmin et
   └── Ölçüm noktalarını planla
```

### 2.3 Açılış Toplantısı Planı (Kick-off Meeting)

```
Açılış toplantısı gündemi (1-2 saat):

1. Tanışma ve proje ekibi tanıtımı
2. Denetim amacı, kapsamı ve beklentilerin netleştirilmesi
3. Tesis genel bilgi sunumu (tesis yöneticisi tarafından)
4. Enerji tüketim verileri durumu (eksik veri tespiti)
5. Saha güvenlik kuralları ve erişim prosedürleri
6. Günlük program ve refakatçi ataması
7. İletişim kanalları (acil iletişim dahil)
8. Sorular ve ek talepler

Katılımcılar:
├── Tesis müdürü / genel müdür yardımcısı
├── Enerji yöneticisi
├── Bakım müdürü
├── Üretim planlama sorumlusu
└── Denetim ekibi (tüm üyeler)
```

## 3. Saha Çalışması Rehberi (Field Work Guide)

### 3.1 Günlük Program (Örnek 3 Günlük Denetim)

```
Gün 1 — Açılış ve Isıl Sistemler:
═══════════════════════════════════════
09:00  Açılış toplantısı
10:00  Tesis genel turu (walk-through, fotoğraf)
12:00  Öğle arası
13:00  Kazan dairesi (baca gazı ölçümü, yalıtım kontrolü)
15:00  Buhar dağıtım sistemi (kapan kontrolü, kaçak tespiti)
16:30  Kondensat geri dönüş değerlendirmesi
17:00  Güç analizörü kurulumu (ana pano + 2-3 büyük tüketici)

Gün 2 — Elektrik ve Mekanik Sistemler:
═══════════════════════════════════════
09:00  Kompresör dairesi (SPC ölçümü, ısı geri kazanım, kaçak)
11:00  Soğutma sistemi (chiller COP, kondenser, soğutma kulesi)
12:00  Öğle arası
13:00  Pompa/fan sistemleri (güç profili, kısma vana pozisyonu)
15:00  Motor verimliliği kontrolleri (büyük motorlar >15 kW)
16:00  Termal kamera taraması (yalıtım, elektrik pano, motor)
17:00  Gün sonu veri derleme

Gün 3 — Özel Sistemler ve Kapanış:
═══════════════════════════════════════
09:00  Aydınlatma (lux ölçümü, çalışma saatleri, LED potansiyeli)
10:30  HVAC sistemi (sıcaklık, nem, hava değişim oranı)
11:30  Proses spesifik ölçümler (kurutma, fırın, proses ısıtma)
12:00  Öğle arası
13:00  Güç analizörü verisi indirme ve hızlı analiz
14:00  Enerji dengesi kontrol hesabı
15:00  Ön bulgular derleme
16:00  Kapanış toplantısı (ön bulgular sunumu)
17:00  Ek veri taleplerini iletme
```

### 3.2 Ekipman Bazlı Kontrol Noktaları (Equipment Checklists)

**Kompresör Sistemi:**
```
☐ Çekilen güç ölçümü (tam yük + kısmi yük): ____ kW
☐ Üretilen debi (anemometre veya ultrasonik): ____ m³/min
☐ SPC hesaplama: ____ kW/(m³/min) [Hedef: <6.0 @ 7 bar]
☐ Sistem basıncı (kompresör çıkış vs kullanım noktası): ΔP = ____ bar
☐ VSD durumu: Var / Yok / Uygulanabilir
☐ Kaçak tespiti (ultrasonik): ____ adet, tahmini oran: ____%
☐ Isı geri kazanım durumu: Var / Yok / Potansiyel: ____ kW
☐ Soğutma suyu çıkış sıcaklığı: ____ °C
```

**Kazan Sistemi:**
```
☐ Baca gazı analizi: O₂ = ____%, CO = ____ ppm, T_baca = ____ °C
☐ Yakma verimi (hesaplanan): ____% [Hedef: >88% doğalgaz]
☐ Gövde yüzey sıcaklığı (termal kamera): ____ °C [Hedef: <60°C]
☐ Yalıtım durumu (boru, vana, flanş): İyi / Orta / Kötü
☐ Buhar kapanı kontrolü: Toplam ____, Arızalı ____, Kaçak ____
☐ Kondensat geri dönüş oranı: ____% [Hedef: >80%]
☐ Blowdown sıklığı/miktarı: ____ L/saat, Isı geri kazanım: Var / Yok
☐ Economizer durumu: Var / Yok, Çıkış T: ____ °C
```

**Chiller Sistemi:**
```
☐ Soğutma kapasitesi ölçümü: ____ kW (veya ____ TR)
☐ Elektrik tüketimi: ____ kW
☐ COP hesaplama: ____ [Hedef: >5.0 su soğutmalı, >3.0 hava soğutmalı]
☐ CHW giriş/çıkış sıcaklığı: ____ / ____ °C [Hedef ΔT: 5-6°C]
☐ Kondenser su giriş/çıkış sıcaklığı: ____ / ____ °C
☐ Kondenser yaklaşım sıcaklığı: ____ °C [Hedef: <3°C]
☐ Kule yaklaşım sıcaklığı: ____ °C [Hedef: <5°C]
☐ Dağıtım yalıtımı ve bypass kontrolü
```

**Pompa Sistemi:**
```
☐ Çekilen güç: ____ kW
☐ Debi (ultrasonik clamp-on): ____ m³/h
☐ Basma yüksekliği (giriş-çıkış basınç farkı): ____ m
☐ Pompa verimi (hesaplanan): ____% [Hedef: >70%]
☐ Kontrol yöntemi: Kısma / Bypass / VSD / On-Off
☐ Kısma vanası pozisyonu: ____% (açıklık)
☐ Motor verimlilik sınıfı: IE__ [Hedef: IE3 veya üzeri]
☐ Paralel pompa çalışma stratejisi değerlendirmesi
```

**Aydınlatma Sistemi:**
```
☐ Aydınlatma gücü yoğunluğu (LPD): ____ W/m² [Sektöre göre hedef]
☐ Lux seviyesi ölçümü (çalışma yüzeyi): ____ lux [Standart: EN 12464]
☐ Lamba tipi envanteri: Floresan ____, LED ____, HID ____
☐ Çalışma saatleri ve kontrol yöntemi (zamanlayıcı, sensör, manuel)
☐ Doğal aydınlatma potansiyeli değerlendirmesi
```

**Buhar Dağıtım Sistemi:**
```
☐ Buhar hattı izolasyon durumu (termal kamera)
☐ Çıplak vana/flanş sayısı: ____ adet, tahmini kayıp: ____ kW
☐ Kondensat geri dönüş hattı durumu
☐ Buhar basıncı dağılımı (üretim → kullanım noktası)
☐ PRV (basınç düşürme vanası) konumları ve kapasiteleri
```

**Elektrik Dağıtım Sistemi:**
```
☐ Güç faktörü (cos φ): ____ [Hedef: >0.98]
☐ Harmonik bozulma (THD): ____% [Hedef: <%5]
☐ Trafo yükleme oranı: ____% [İdeal: %40-70]
☐ Trafo kayıpları (boşta + yüklü): ____ kW
☐ Faz dengesizliği: ____% [Hedef: <%2]
```

## 4. Ölçüm Cihazları ve Teknikler (Measurement Instruments and Techniques)

| Cihaz | Ölçüm Parametresi | Doğruluk | Kullanım Alanı |
|-------|-------------------|----------|----------------|
| Güç analizörü (3-faz) | kW, kVAr, cos φ, THD, profil | ±%0.5-1.0 | Motor, kompresör, chiller, ana pano |
| Ultrasonik debimetre (clamp-on) | Su/yağ debisi [m³/h] | ±%1-3 | Boru hattı, CHW, kondenser suyu |
| IR termometre / termal kamera | Yüzey sıcaklığı [°C] | ±1-2°C | Yalıtım, elektrik bağlantı, motor |
| Baca gazı analizörü | O₂, CO, CO₂, T_baca | ±%0.2 (O₂) | Kazan yakma kontrolü |
| Ultrasonik kaçak dedektörü | Basınçlı hava/buhar kaçak [dB] | Nitel (konum) | Basınçlı hava, buhar hattı |
| Lux metre | Aydınlatma seviyesi [lux] | ±%3-5 | Aydınlatma denetimi |
| Nem ve sıcaklık ölçer | Sıcaklık [°C], RH [%] | ±0.5°C, ±%2 | Ortam koşulları, HVAC |
| Tachometre (temassız) | Devir [rpm] | ±%0.05 | Motor, fan, pompa devri |
| Pitot tüpü / anemometre | Hava hızı [m/s], debi [m³/h] | ±%2-5 | Kanal hava debisi, kompresör |

```
Ölçüm cihazı hazırlık checklist'i:

☐ Tüm cihazların kalibrasyonu güncel (sertifika var)
☐ Yedek batarya/şarj cihazı
☐ CT (akım trafosu) uygun aralıkta (örn. 100A, 500A, 1000A)
☐ Veri kayıt kartı / hafıza yeterli
☐ Bağlantı kabloları ve adaptörler
☐ Kişisel koruyucu donanım (PPE): kulaklık, gözlük, eldiven, baret
☐ Kaçak etiketleme malzemesi (yapışkan etiket, sprey boya)
☐ Fotoğraf makinası / cep telefonu (belgeme için)
```

## 5. ExergyLab ile Denetim Entegrasyonu (ExergyLab Integration)

### 5.1 Saha Verilerinin ExergyLab'a Girişi

```
ExergyLab entegrasyon akış diyagramı:

Adım 1: Saha Ölçümleri
├── Sıcaklık ölçümleri [°C] → Her ekipman giriş/çıkış
├── Basınç ölçümleri [bar] → Her ekipman giriş/çıkış
├── Debi ölçümleri [m³/h, kg/s] → Akışkan debi
├── Güç ölçümleri [kW] → Elektrik tüketimi
└── Yakıt debisi [m³/h, kg/h] → Yakıt tüketimi

Adım 2: ExergyLab Veri Girişi
├── Kompresör modülü: T_giriş, P_giriş, T_çıkış, P_çıkış, Ẇ_elektrik
├── Kazan modülü: T_su, P_su, T_buhar, P_buhar, ṁ_yakıt, LHV
├── Chiller modülü: T_CHW_giriş/çıkış, T_kond_giriş/çıkış, Ẇ_komp
├── Pompa modülü: T_giriş, P_giriş, T_çıkış, P_çıkış, Q̇, Ẇ
└── Fabrika modülü: Tüm ekipmanlar birlikte

Adım 3: ExergyLab Çıktıları
├── Ekipman bazında exergy verimi [%]
├── Exergy yıkım miktarı [kW] ve sıralaması
├── Sankey diyagramı (exergy akış)
├── Benchmark karşılaştırma (sektörel)
├── Cross-equipment entegrasyon fırsatları
└── AI destekli yorumlama ve öneri raporu

Adım 4: Denetim Raporuna Entegrasyon
├── Exergy verimlilik haritası → Hotspot görselleştirme
├── Exergy bazlı önceliklendirme → Doğru yatırım sıralaması
├── Sankey → Yönetici sunumu için görsel
└── AI önerileri → Rapor taslağı oluşturma desteği
```

### 5.2 Exergy Analizinin Geleneksel Denetimi Zenginleştirmesi

| Boyut | Geleneksel Denetim | ExergyLab Destekli Denetim |
|-------|-------------------|---------------------------|
| Verimlilik ölçüsü | Enerji verimi (1. yasa) | Exergy verimi (2. yasa) |
| Kayıp analizi | Yalnızca niceliksel (kW, MWh) | Niteliksel (exergy kalitesi) |
| Önceliklendirme | Enerji büyüklüğüne göre | Exergy yıkımına göre |
| Cross-equipment | Sınırlı (genellikle gözden kaçar) | Sıcaklık eşleştirme fırsatları |
| Gizli kayıplar | Görülmeyebilir | Sıcaklık düşürme kayıpları tespit edilir |
| Benchmark | Enerji verimi bazlı | Exergy verimi bazlı (daha hassas) |
| Rapor görselliği | Standart tablo/grafik | Sankey + AI yorumlama |

### 5.3 Sahada Exergy Fark Yaratan Durumlar

```
Durum 1: Kazan enerji verimi %90, exergy verimi %42
→ Geleneksel: "Kazan verimli, iyileştirme potansiyeli sınırlı"
→ ExergyLab: "Yüksek sıcaklıklı buhar düşük T proseste kullanılıyor.
  Kaskad kullanım veya basınç kademesi ile exergy iyileştirme fırsatı"

Durum 2: Kompresör SPC = 6.2 kW/(m³/min) — benchmark dahilinde
→ Geleneksel: "Benchmark dahilinde, öncelik düşük"
→ ExergyLab: "Exergy verimi %12. Mekanik enerji→ısı dönüşüm kaybı
  yüksek. Isı geri kazanım ile toplam exergy kullanımı artırılabilir"

Durum 3: Pompa sistemi kısma vanası %40 kısık
→ Geleneksel: "VSD retrofit öner"
→ ExergyLab: "Exergy yıkımı 2 noktada: motor→pompa + vana kısma.
  VSD ile exergy verimi %45→%72 (+27 puan) — en yüksek iyileşme oranı"
```

## 6. Denetim Raporu Yapısı (Audit Report Structure)

### 6.1 Kısa Rapor Özeti (Executive Summary — 2-3 sayfa)

```
Executive summary bölümleri:
1. Denetim amacı ve kapsamı (1 paragraf)
2. Tesis genel profili (1 paragraf)
3. Toplam enerji tüketimi ve maliyeti (tablo)
4. Tespit edilen toplam tasarruf potansiyeli (€/yıl, kWh/yıl, CO₂)
5. Top-5 iyileştirme fırsatı (tablo: öneri, tasarruf, yatırım, GÖS)
6. Genel değerlendirme ve önerilen yol haritası (1 paragraf)
```

### 6.2 Detaylı Rapor Yapısı (10 Bölüm)

| Bölüm | Başlık | İçerik Özeti |
|-------|--------|-------------|
| 1 | Giriş | Denetim amacı, kapsamı, yöntem, ekip, standart referansı |
| 2 | Tesis Genel Bilgileri | Sektör, ürün, kapasite, çalışma takvimi, yerleşim |
| 3 | Enerji Tüketim Analizi | Kaynak bazlı tüketim, SEC, maliyet, trend |
| 4 | Enerji Dengesi | Sankey diyagramı, alan/ekipman bazlı dağılım |
| 5 | Sistem Bazlı Değerlendirme | Kazan, kompresör, chiller, pompa, aydınlatma, HVAC |
| 6 | Exergy Analizi (ExergyLab) | Exergy verimlilik haritası, yıkım sıralaması |
| 7 | İyileştirme Fırsatları | ECM listesi (bulgu + öneri kartları) |
| 8 | Ekonomik Değerlendirme | SPP, NPV, IRR, portföy özeti |
| 9 | Uygulama Yol Haritası | Fazlı uygulama planı, önceliklendirme matrisi |
| 10 | Sonuç ve Öneriler | Genel değerlendirme, stratejik öneriler |

### 6.3 Bulgu Kartı Formatı (Finding Card — F-XX)

```
BULGU KARTI — F-03
════════════════════════════════════════
Başlık: Kazan baca gazı O₂ seviyesi yüksek
Sistem: Buhar kazanı (Kazan-01, 4 ton/h)
Seviye: ASHRAE Level II

Mevcut Durum:
  O₂ = %5.8, CO = 25 ppm, Baca T = 195°C
  Yakma verimi = %84.5

İyi Uygulama (Best Practice):
  O₂ = %2.5, CO < 50 ppm, Baca T = 165°C
  Yakma verimi = %90.2

İlgili Öneri: R-03
Exergy Etkisi: Exergy verimi %38 → %41 (+3 puan)
Kanıt: Baca gazı ölçüm raporu (Ek-B), termal kamera (Foto-12)
```

### 6.4 Öneri Kartı Formatı (Recommendation Card — R-XX)

```
ÖNERİ KARTI — R-03
════════════════════════════════════════
Başlık: O₂ trim kontrolü kurulumu + yakıcı bakımı
İlgili Bulgu: F-03
Sistem: Buhar kazanı (Kazan-01)
Uygulama Kolaylığı: Kolay (duruş gerektirmez)

Teknik Açıklama:
  Kazan yakıcısına O₂ trim kontrol sistemi eklenmesi
  ve yakıcı membranlarının bakımı/değiştirilmesi.

Tasarruf Hesabı:
  ΔQ = 2,000 kW × (90.2 - 84.5) / 84.5 = 135 kW termal
  Yıllık enerji: 135 × 6,000 h = 810,000 kWh/yıl
  Yıllık maliyet: 810,000 × €0.045/kWh = €36,450/yıl
  CO₂ azaltma: 810,000 × 0.202 / 1,000 = 163.6 ton/yıl

Yatırım Maliyeti:
  O₂ sensör + kontrolör: €8,000
  Yakıcı bakımı: €2,000
  Komisyonlama: €2,000
  Toplam: €12,000

Ekonomik Göstergeler:
  GÖS (SPP) = 12,000 / 36,450 = 0.33 yıl (4 ay)
  NPV (10 yıl, %10) = €212,000
  IRR > %100

Öncelik: YÜKSEK (GÖS < 1 yıl)
Faz: Faz 1 (hemen uygulama)
```

## 7. Yaygın Hatalar ve Önleme (Common Mistakes and Prevention)

| No | Yaygın Hata | Sonucu | Önleme Yöntemi |
|----|-------------|--------|----------------|
| 1 | Temsili olmayan ölçüm zamanı | Yanlış yük profili, hatalı tasarruf tahmini | Normal üretim döneminde ölçüm yap, tatil/bakım döneminden kaçın |
| 2 | Tek noktadan güç ölçümü | Yük değişkenliğini kaçırma | Minimum 1 hafta sürekli kayıt (15 dk aralık) |
| 3 | Nameplate verilerine güvenme | Gerçek performansı yansıtmaz | Saha ölçümü ile doğrula, nameplate sadece referans |
| 4 | ECM etkileşimini göz ardı etme | Toplam tasarrufta %10-25 hata | Etkileşim matrisi oluştur, sıralı uygulama hesapla |
| 5 | Enerji dengesi kontrolü yapılmaması | Büyük hatalar fark edilmez | Giriş ≈ Çıkış + Kayıp kontrolü, %5'ten fazla fark araştır |
| 6 | Yatırım maliyetini hafife alma | GÖS'un gerçekte daha uzun olması | Tedarikçi teklifi al, montaj + komisyonlama dahil et |
| 7 | Düşük sıcaklık kayıplarını ihmal | Exergy fırsatlarını kaçırma | ExergyLab ile exergy analizi, sıcaklık kalitesini değerlendir |
| 8 | Operatör görüşü almama | Pratik engelleri görememe | Her sistem için operatör/bakımcı ile görüşme yap |
| 9 | Fotoğraf/kanıt eksikliği | Rapor inandırıcılığı düşer | Her bulgu için fotoğraf, termal kamera görüntüsü kaydet |
| 10 | Raporu geciktirme | Veri tazeliğini kaybetme | Saha sonrası 3 hafta içinde taslak, 5 hafta içinde final |

## 8. Çalışılmış Örnek — Metal İşleme Fabrikası (Worked Example)

### 8.1 Tesis Profili

```
Tesis: Orta ölçekli metal işleme fabrikası (İstanbul, Türkiye)
Sektör: Otomotiv parça üretimi
Çalışma: 3 vardiya, 6 gün/hafta, 6,000 h/yıl
Enerji tüketimi: 5,200 MWh/yıl elektrik + 12,000 MWh/yıl doğalgaz
Enerji maliyeti: €624,000/yıl (elektrik) + €540,000/yıl (gaz) = €1,164,000/yıl
Ana ekipmanlar: 2 buhar kazanı (6+4 ton/h), 3 kompresör (75+55+37 kW),
  1 chiller (400 kW), 8 pompa (7.5-22 kW), endüksiyon fırınları
```

### 8.2 3 Günlük Denetim Özeti

```
Gün 1 — Açılış + ısıl sistemler:
├── Açılış toplantısı: 12 kişi katılım
├── Tesis turu: 8 üretim bölümü ziyaret, 47 fotoğraf
├── Kazan-01 baca gazı: O₂=%5.2, T=205°C, η=%83.5
├── Kazan-02 baca gazı: O₂=%3.8, T=185°C, η=%87.1
├── Buhar kapanı: 34 adet kontrol, 5 arızalı, 3 kaçak
├── Kondensat dönüş: %55 (düşük — eksik hatlar tespit)
└── Güç analizörü: Ana pano + kompresör + chiller'a kurulum

Gün 2 — Elektrik + mekanik:
├── Kompresör: SPC = 6.8 kW/(m³/min) (yüksek — kaçak etkisi)
├── Kaçak tespiti: 28 adet, tahmini kaçak %22
├── Chiller: COP = 3.8 (düşük — fouling şüphesi)
├── Kondenser yaklaşım: 5.2°C (yüksek)
├── Pompa-04 (22 kW): Vana %35 kısık, VSD yok
├── Pompa-06 (15 kW): Vana %50 kısık, VSD yok
├── Motor envanteri: 3 adet IE1 motor (>15 kW) tespit
└── Termal kamera: 12 yalıtım eksikliği, 2 sıcak elektrik bağlantı

Gün 3 — Özel sistemler + kapanış:
├── Aydınlatma: %60 floresan, LPD = 14 W/m² (yüksek)
├── Endüksiyon fırın verimliliği: %68 (makul)
├── Güç analizörü veri indirme: 72 saatlik profil
├── Enerji dengesi: Giriş 17,200 MWh, çıkış+kayıp 16,500 MWh (fark %4 — kabul)
├── Ön bulgular: 11 bulgu, 9 öneri, toplam tasarruf tahmini €185,000/yıl
└── Kapanış toplantısı: Yönetim + teknik ekip, ön sunumu olumlu karşıladı
```

### 8.3 ExergyLab Sonuçları (Ön)

```
ExergyLab fabrika analizi sonuçları:
├── Fabrika toplam exergy verimi: %28 (sektör ortalaması %32)
├── En yüksek exergy yıkım: Kazan-01 → 480 kW_ex (%38 exergy verimi)
├── Cross-equipment #1: Kompresör atık ısı → Kazan besleme suyu (€9,200/yıl)
├── Cross-equipment #2: Chiller desuperheater → Proses sıcak su (€11,500/yıl)
├── VSD fırsatı: 2 pompa + soğutma kulesi fanları (€28,000/yıl)
└── Toplam exergy bazlı tasarruf potansiyeli: €203,000/yıl (%17.4)
```

## 9. İlgili Dosyalar

- [Denetim Seviyeleri](audit_levels.md) -- ASHRAE Level I/II/III detay karsilastirma
- [ISO 50002](iso_50002.md) -- ISO 50002 denetim standardi
- [EN 16247](en_16247.md) -- EN 16247 Avrupa denetim standardi
- [Metodoloji (genel)](../methodology.md) -- Teorik audit cercevesi
- [Turkiye Mevzuati](turkey_legislation.md) -- YEGM etud gereksinimleri
- [Veri Toplama](../data_collection.md) -- Veri toplama rehberi
- [INDEX](INDEX.md) -- Enerji yonetimi bilgi tabani navigasyonu

## 10. Referanslar

- ASHRAE, "Procedures for Commercial Building Energy Audits", 2nd Edition, 2011
- ISO 50002:2014, "Energy audits -- Requirements with guidance for use"
- EN 16247-1:2022, "Energy audits -- Part 1: General requirements"
- EN 16247-3:2022, "Energy audits -- Part 3: Processes"
- YEGM, "Enerji Etudu Usul ve Esaslari Hakkinda Teblig"
- Thumann, A. & Younger, W., "Handbook of Energy Audits", 9th Edition, Fairmont Press
- Turner, W.C. & Doty, S., "Energy Management Handbook", 9th Edition, Fairmont Press, 2013
- US DOE, "Energy Audit Tips" serisi (kompressor, kazan, pompa, motor)
- IPMVP, "International Performance Measurement and Verification Protocol", EVO, 2022
- Krarti, M., "Energy Audit of Building Systems: An Engineering Approach", 3rd Edition, CRC Press
