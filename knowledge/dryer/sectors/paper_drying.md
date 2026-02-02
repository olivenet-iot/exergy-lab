---
title: "Kağıt ve Selüloz Kurutma (Paper and Pulp Drying)"
category: dryer
equipment_type: dryer
keywords:
  - kağıt kurutma
  - paper drying
  - silindir kurutma
  - yankee dryer
  - selüloz
  - hamur
related_files:
  - dryer/formulas.md
  - dryer/benchmarks.md
  - dryer/equipment/drum_dryer.md
  - dryer/equipment/infrared_dryer.md
  - dryer/solutions/exhaust_heat_recovery.md
  - dryer/solutions/insulation.md
  - dryer/solutions/mechanical_dewatering.md
  - factory/sector_paper.md
use_when:
  - "Kağıt sektörü kurutma analiz edilirken"
priority: medium
last_updated: 2026-02-01
---

# Kağıt ve Selüloz Kurutma (Paper and Pulp Drying)

## Genel Bakış

Kağıt kurutma, kağıt üretim sürecinde tek başına en büyük enerji tüketim noktasıdır. Toplam fabrika enerjisinin **%50-65**'i kurutma bölümünde harcanır. Çok silindirli (multi-cylinder) kurutma bölümü, modern kağıt makinelerinde baskın teknolojidir; buhar ile ısıtılan 40-60 adet çelik silindir üzerinden kağıt şeridi (web) temas yoluyla kurutulur.

Kağıt üretiminin enerji yoğunluğu, kurutma bölümünün performansına doğrudan bağlıdır. Kurutma öncesi mekanik su alma (press section) verimliliğindeki her %1'lik iyileşme, kurutma bölümünde yaklaşık %4 buhar tasarrufu sağlar. Bu nedenle exergy analizi, yalnızca kurutma bölümünü değil, pres-kurutma entegrasyonunu da kapsamalıdır.

### Kağıt Fabrikası Enerji Profili

| Parametre | Değer | Birim |
|-----------|-------|-------|
| Kurutmanın toplam enerji payı | 50 - 65 | % |
| Buhar tüketimi (tipik) | 1.2 - 1.8 | kg buhar/kg su buharlaştırma |
| Özgül enerji tüketimi (SEC) | 3,000 - 5,000 | kJ/kg su buharlaştırma |
| Sektörel SMER (buhar bazında) | 0.7 - 1.2 | kg/kWh |
| Tipik exergy verimi | 15 - 30 | % |
| Üretim hızı (modern makine) | 200 - 2,000 | m/min |

## Kurutma Konfigürasyonları

### 1. Çok Silindirli Kurutucu (Multi-Cylinder Dryer)

Kağıt endüstrisinde en yaygın kurutma yöntemidir. Kağıt şeridi, buhar ile ısıtılan çelik silindirlerin üzerinden geçerken temas (conductive) yoluyla kurutulur. Silindirler iki sıra halinde dizilir ve kağıt şeridi keçe (felt/fabric) yardımıyla sıkıca silindirlere bastırılır.

| Parametre | Değer | Birim |
|-----------|-------|-------|
| Silindir çapı | 1.5 - 1.83 | m |
| Silindir sayısı | 40 - 60 | adet |
| Buhar basıncı (ilk grup) | 1.5 - 3.0 | bar |
| Buhar basıncı (son grup) | 3.0 - 6.0 | bar |
| Yüzey sıcaklığı | 80 - 130 | °C |
| Kurutma hızı | 15 - 30 | kg su/m².h |

**Çalışma prensibi:**
1. Kağıt şeridi, keçe ile birlikte silindire sarılır
2. Buhar, silindir içinde yoğuşarak (condensation) latent ısısını silindir duvarına aktarır
3. Isı, iletim (conduction) yoluyla kağıda transfer edilir
4. Kağıttaki su buharlaşır ve silindirler arası boşlukta (pocket) uzaklaştırılır
5. Kondensat, sifon sistemi ile silindir içinden alınır

### 2. Yankee Kurutucu (Yankee Dryer)

Tek büyük çaplı silindir, özellikle tişü kağıdı (tissue paper) üretiminde kullanılır. Yüksek kapasiteli hava üfleyici (impingement hood) ile kombine edilir.

| Parametre | Değer | Birim |
|-----------|-------|-------|
| Silindir çapı | 3.0 - 6.7 | m |
| Buhar basıncı | 5.0 - 10.0 | bar |
| Yüzey sıcaklığı | 95 - 160 | °C |
| Hood hava sıcaklığı | 350 - 550 | °C |
| Kurutma kapasitesi | 200 - 400 | kg su/m².h |

Yankee kurutucuda kurutma enerjisinin yaklaşık %60-70'i hood (sıcak hava üfleyici) tarafından, %30-40'ı buhar silindiri tarafından sağlanır. Yüksek hood sıcaklıkları, büyük exergy yıkımı kaynağıdır.

### 3. Hava Geçirmeli Kurutma (Through-Air Drying - TAD)

Sıcak hava, kağıt şeridi içinden zorlanarak geçirilir. Daha hacimli (bulky) ve yumuşak tişü kağıdı üretir ancak enerji tüketimi yüksektir.

| Parametre | Değer | Birim |
|-----------|-------|-------|
| Hava sıcaklığı | 120 - 180 | °C |
| Hava hızı (şeritten geçen) | 0.5 - 3.0 | m/s |
| Enerji tüketimi | 4,000 - 7,000 | kJ/kg su buharlaştırma |
| SMER | 0.5 - 0.9 | kg/kWh |

TAD teknolojisi, konvansiyonel Yankee sistemine göre %30-50 daha fazla enerji tüketir, ancak üstün ürün kalitesi (yumuşaklık, hacim) sağlar. Exergy açısından, yüksek sıcaklıklı havanın düşük sıcaklık buharlaştırma için kullanılması ciddi tersinmezlik yaratır.

### 4. IR Destekli Kurutma (Infrared Boosters)

Kızılötesi (IR) kurutma, kağıt üretiminde genellikle ana kurutma yöntemi olarak değil, destekleyici teknoloji olarak kullanılır.

| Parametre | Değer | Birim |
|-----------|-------|-------|
| IR dalga boyu | 2 - 5 | mikron (orta IR) |
| Yüzey güç yoğunluğu | 20 - 60 | kW/m² |
| Verimlilik (gaz IR) | 40 - 60 | % |
| Verimlilik (elektrik IR) | 80 - 95 | % |

**Kullanım alanları:**
- Enine (cross-direction - CD) nem profili düzeltme
- Kaplama sonrası hızlı kurutma
- Kurutma kapasitesi artırma (bottleneck giderme)

### 5. Hava Çarptırma (Air Impingement)

Yüksek hızlı sıcak hava jetleri doğrudan kağıt yüzeyine yönlendirilir. Yankee hood'unda ve bağımsız impingement kurutucularında kullanılır.

| Parametre | Değer | Birim |
|-----------|-------|-------|
| Hava sıcaklığı | 200 - 550 | °C |
| Jet hızı | 60 - 120 | m/s |
| Nozul-yüzey mesafesi | 10 - 25 | mm |
| Isı transfer katsayısı | 200 - 500 | W/m².K |

## Proses Akışı

Kağıt üretiminde su giderme, üç ardışık aşamada gerçekleşir. Her aşamanın enerji verimliliği ve exergy etkisi farklıdır:

### Aşama 1: Elek Bölümü (Wire/Forming Section)

| Parametre | Değer |
|-----------|-------|
| Giriş katılık oranı | %0.5 - 1.0 (hamur konsantrasyonu) |
| Çıkış katılık oranı | ~%20 |
| Su giderme yöntemi | Yerçekimi + vakum |
| Enerji tüketimi | Düşük (mekanik) |

### Aşama 2: Pres Bölümü (Press Section)

| Parametre | Değer |
|-----------|-------|
| Giriş katılık oranı | ~%20 |
| Çıkış katılık oranı (konvansiyonel) | %40 - 45 |
| Çıkış katılık oranı (shoe press) | %45 - 52 |
| Su giderme yöntemi | Mekanik basınç |
| Enerji tüketimi | Orta (mekanik) |

**Kritik kural:** Pres bölümünde her %1 katılık artışı, kurutma bölümünde yaklaşık **%4 buhar tasarrufu** sağlar. Bu, kağıt endüstrisindeki en önemli enerji verimliliği ilkesidir.

### Aşama 3: Kurutma Bölümü (Dryer Section)

| Parametre | Değer |
|-----------|-------|
| Giriş katılık oranı | %40 - 50 |
| Çıkış katılık oranı | %92 - 96 |
| Su giderme yöntemi | Termal buharlaştırma |
| Enerji tüketimi | Çok yüksek (buhar/gaz) |

Proses akış özeti:

```
Elek (%20) → Pres (%40-50) → Kurutma (%92-96)
   Yerçekimi    Mekanik basınç   Termal buharlaştırma
   ~0 kJ/kg su  ~50 kJ/kg su    ~3,000-5,000 kJ/kg su
```

Mekanik su alma (pres), termal kurutmadan yaklaşık **50-100 kat daha az** enerji gerektirir. Bu nedenle pres bölümü optimizasyonu, exergy açısından en büyük iyileştirme fırsatıdır.

## Benchmarklar

### Buhar Tüketimi (Kağıt Türüne Göre)

| Kağıt Türü | Buhar Tüketimi (kg buhar/kg su) | SEC (kJ/kg su) | Exergy Verimi (%) |
|------------|--------------------------------|----------------|-------------------|
| Ambalaj kağıdı (linerboard) | 1.2 - 1.5 | 2,700 - 3,400 | 20 - 30 |
| Yazma/baskı kağıdı | 1.3 - 1.7 | 2,900 - 3,800 | 18 - 27 |
| Tişü kağıdı (Yankee) | 1.5 - 2.0 | 3,400 - 4,500 | 15 - 25 |
| Tişü kağıdı (TAD) | 2.0 - 3.0 | 4,500 - 6,800 | 10 - 18 |
| Karton (board) | 1.3 - 1.6 | 2,900 - 3,600 | 18 - 28 |
| Selüloz (market pulp) | 1.4 - 1.8 | 3,100 - 4,000 | 15 - 25 |

### SMER Benchmarkları

| Performans Seviyesi | SMER (kg/kWh, buhar bazında) | Açıklama |
|--------------------|-------------------------------|----------|
| Mükemmel | > 1.2 | En iyi uygulamalar, shoe press + optimize kurutma |
| İyi | 1.0 - 1.2 | Modern makine, iyi bakım |
| Ortalama | 0.7 - 1.0 | Standart endüstriyel performans |
| Ortalamanın altı | 0.5 - 0.7 | İyileştirme potansiyeli yüksek |
| Kötü | < 0.5 | Acil müdahale gerekli |

### Exergy Verimi Sınıflandırması

Kağıt kurutma, temas (conductive) mekanizması sayesinde konvektif kurutuculara göre daha yüksek exergy verimine sahiptir:

| Exergy Verimi (%) | Sınıf | Tipik Durum |
|-------------------|-------|-------------|
| > 28 | Mükemmel | Shoe press + optimize buhar kademeleme |
| 22 - 28 | İyi | Modern çok silindirli, iyi bakım |
| 15 - 22 | Ortalama | Standart çok silindirli kurutma |
| 10 - 15 | Ortalamanın altı | Eski makine veya kötü bakım |
| < 10 | Kötü | Sistem revizyonu gerekli |

## İyileştirme Fırsatları

### 1. Pres Bölümü İyileştirme — Shoe Press

Mekanik su almanın artırılması, en yüksek getirili iyileştirmedir:

| Parametre | Konvansiyonel Pres | Shoe Press | Fark |
|-----------|-------------------|------------|------|
| Çıkış katılık oranı | %40 - 45 | %45 - 52 | +5-10 puan |
| Nip basıncı | 5 - 8 MPa | 8 - 12 MPa |  |
| Nip uzunluğu | 30 - 50 mm | 200 - 300 mm |  |
| Buhar tasarrufu | Baz | %20 - 40 | Önemli |
| Yatırım | — | 500,000 - 2,000,000 € |  |
| Geri dönüş süresi | — | 2 - 4 yıl |  |

Her %1 katılık artışı kurutma bölümünde ~%4 buhar tasarrufu sağladığından, shoe press ile +5 puan katılık artışı **~%20 buhar tasarrufu** demektir.

### 2. Cep Havalandırma Optimizasyonu (Pocket Ventilation)

Silindirler arası boşluklarda (pocket) biriken nemli hava, kurutma hızını düşürür:

| Parametre | Değer |
|-----------|-------|
| Tipik buhar tasarrufu | %5 - 10 |
| Yatırım | 15,000 - 40,000 € |
| Geri dönüş süresi | 0.5 - 1.5 yıl |
| Etki mekanizması | Nemli havanın uzaklaştırılması, buharlaşma hızının artırılması |

Optimize edilmiş cep havalandırma sistemi, kuru hava besleme ve nemli hava egzozu ile silindirler arası nem taşıma kapasitesini artırır.

### 3. Hood Egzoz Isı Geri Kazanımı (Hood Exhaust Heat Recovery)

Kurutma bölümü hood'undan çıkan sıcak nemli hava, önemli enerji içerir:

| Parametre | Açık Hood | Kapalı Hood (Closed) |
|-----------|-----------|---------------------|
| Egzoz sıcaklığı | 60 - 80 °C | 80 - 95 °C |
| Egzoz nemi | Düşük | Yüksek (yoğuşturulabilir) |
| Isı geri kazanım potansiyeli | %5 - 10 | %10 - 20 |
| Yatırım | — | 100,000 - 400,000 € |
| Geri dönüş süresi | — | 1.5 - 3 yıl |

Kapalı hood sistemi, egzoz havasını yoğunlaştırarak daha yüksek sıcaklıkta ve nemde toplar; bu da ısı geri kazanım verimini artırır.

### 4. Kondensat Sistemi Optimizasyonu

| İyileştirme | Buhar Tasarrufu | Yatırım | Geri Dönüş |
|-------------|----------------|---------|------------|
| Flash buhar geri kazanımı (flash steam recovery) | %5 - 10 | 20,000 - 60,000 € | 1 - 2 yıl |
| Sifon sistemi iyileştirme | %3 - 5 | 10,000 - 30,000 € | 0.5 - 1 yıl |
| Kondensat geri dönüş optimizasyonu | %2 - 4 | 5,000 - 15,000 € | 0.5 - 1 yıl |

**Flash buhar geri kazanımı:** Yüksek basınçlı kondensattan (3-6 bar) üretilen flash buhar, düşük basınçlı silindir grupları (1.5-2 bar) için kullanılabilir.

### 5. IR Ön Kurutma Optimizasyonu (IR Pre-Drying)

IR kurutucuların stratejik yerleşimi, kurutma kapasitesini artırır ve enerji profili düzeltir:

| Parametre | Değer |
|-----------|-------|
| Tipik uygulama | Kaplama sonrası veya nem profili düzeltme |
| Enerji tasarrufu (profilleme ile) | %3 - 5 |
| Aşırı kurutma azaltma | Her %1 aşırı kurutma = ~%3-5 ekstra enerji |
| Yatırım (IR profilleme) | 50,000 - 200,000 € |
| Geri dönüş süresi | 1 - 2 yıl |

### 6. Buhar Kademeleme (Steam Cascade / Multi-Pressure Groups)

Exergy optimizasyonunun en önemli stratejisi, buhar basıncının kademeli kullanılmasıdır:

| Kurutma Bölgesi | Buhar Basıncı (bar) | Sıcaklık (°C) | Gerekçe |
|-----------------|---------------------|---------------|---------|
| Ön kurutma (1. grup) | 1.5 - 2.0 | 112 - 120 | Yüksek nem, düşük basınç yeterli |
| Orta kurutma (2. grup) | 2.5 - 3.5 | 128 - 139 | Artan iç direnç, artan basınç |
| Son kurutma (3. grup) | 4.0 - 6.0 | 144 - 159 | Düşük nem, yüksek sıcaklık gerekli |

Bu kademeleme, toplam exergy yıkımını **%10-15** azaltır; her aşamada sadece gerekli kadar buhar kalitesi (exergy) kullanılır. Yüksek basınçlı buharın tüm silindirlere dağıtılması, büyük exergy israfıdır.

## Exergy Analizi

### Exergy Akış Diyagramı

Kağıt kurutma bölümünün exergy dengesi:

```
Buhar Exergy Girdisi (100%)
├── Kağıt kurutma (faydalı exergy): 15-30%
├── Kondensat geri dönüş exergy: 10-15%
├── Hood egzoz exergy kaybı: 15-25%
├── Yüzey ısı kaybı exergy: 5-10%
├── Kondensat flash kayıp: 3-5%
└── İç tersinmezlik (irreversibility): 25-40%
```

### Buhar Exergy Girdisi vs Buharlaştırma Exergy'si

Buhar exergy'si ve kurutma için gereken minimum exergy arasındaki fark, iyileştirme potansiyelini gösterir:

| Parametre | Değer | Birim |
|-----------|-------|-------|
| Buhar exergy'si (5 bar, doymuş) | ~780 | kJ/kg buhar |
| Buhar exergy'si (3 bar, doymuş) | ~640 | kJ/kg buhar |
| Suyun 80°C'de buharlaştırma exergy'si | ~180 | kJ/kg su |
| Exergy oranı (gerçek/minimum) | 3 - 5x | — |

Bu 3-5 katlık fark, kağıt kurutmada exergy iyileştirme potansiyelinin büyüklüğünü gösterir.

### Kondensat Geri Dönüş Exergy'si

Kondensatın sıcak olarak kazandairesine geri dönmesi önemli exergy tasarrufu sağlar:

| Kondensat Sıcaklığı (°C) | Spesifik Exergy (kJ/kg) | Geri Kazanım Değeri |
|---------------------------|------------------------|---------------------|
| 100 | ~30 | Düşük |
| 120 | ~50 | Orta |
| 140 | ~75 | İyi |
| 160 | ~105 | Çok iyi |

### Hood Kayıpları

Hood egzozundan çıkan nemli sıcak hava, düşük exergy yoğunluğuna rağmen büyük hacimsel debisi nedeniyle toplam exergy kaybına önemli katkıda bulunur:

| Hood Tipi | Egzoz Sıcaklığı (°C) | Egzoz Nemi (g/kg kuru hava) | Exergy Kaybı (toplam girdinin %) |
|-----------|----------------------|----------------------------|---------------------------------|
| Açık hood | 60 - 80 | 40 - 80 | 15 - 25 |
| Kapalı hood | 80 - 95 | 100 - 200 | 10 - 18 |
| Yankee hood | 200 - 300 | 150 - 300 | 20 - 30 |

### Exergy Analizi Pratik İpuçları (Kağıt Sektörü Özel)

1. **Buhar kalitesi eşleştirme:** Her kurutma grubunda minimum gerekli buhar basıncı kullanılmalıdır. 6 bar buharın 1. grup (düşük nem direnci) için kullanılması, büyük exergy yıkımıdır.

2. **Mekanik vs termal:** Shoe press ile her kg suyu mekanik olarak almak, termal kurutmadan **~50 kat daha az** exergy tüketir. Bu, kağıt endüstrisindeki en büyük exergy iyileştirme fırsatıdır.

3. **Flash buhar:** Yüksek basınçlı kondensattan üretilen flash buhar, düşük basınçlı silindir grupları için exergy-uyumlu kaynaktır. Exergy kademesi korunmuş olur.

4. **Egzoz exergy'si:** Kurutma bölümünden çıkan nemli sıcak hava (60-95 °C), düşük exergy yoğunluğuna rağmen büyük hacimsel debisi nedeniyle önemli exergy kaybı oluşturur.

5. **Cross-equipment fırsatı:** Kağıt fabrikasında buhar türbin çıkışındaki düşük basınçlı buhar (back-pressure turbine), kurutma için idealdir. Kojenerasyon (CHP) ile fabrika geneli exergy optimizasyonu sağlanır.

## Türkiye Kağıt Sektörü

### Sektör Genel Görünümü

Türkiye, Avrupa'nın önde gelen kağıt ve karton üreticilerinden biridir. Toplam yıllık üretim kapasitesi yaklaşık **10-12 milyon ton** seviyesindedir ve büyüme trendi devam etmektedir.

### Başlıca Tesisler ve Kapasiteler

| Tesis / Bölge | Ana Ürün | Yaklaşık Kapasite (ton/yıl) | Kurutma Teknolojisi |
|---------------|----------|-----------------------------|--------------------|
| Hayat Kimya (Kocaeli/Mersin) | Tişü | 300,000+ | Yankee + hood |
| Olmuksan IP (Kocaeli) | Ambalaj, oluklu | 500,000+ | Çok silindirli |
| Modern Karton (Kocaeli) | Karton, ambalaj | 400,000+ | Çok silindirli |
| Kahramanmaraş Kağıt (OYKA) | Kağıt, karton | 350,000+ | Çok silindirli |
| Denizli bölgesi tesisleri | Tişü, temizlik | 200,000+ | Yankee |
| Çorlu/Trakya bölgesi | Kağıt, karton | 300,000+ | Çok silindirli |

### Türkiye'ye Özel Enerji Verileri

| Parametre | Değer | Birim |
|-----------|-------|-------|
| Doğalgaz maliyeti (endüstriyel, 2025) | 0.03 - 0.05 | €/kWh |
| Buhar maliyeti (fabrika içi) | 25 - 40 | €/ton buhar |
| Elektrik maliyeti (endüstriyel) | 0.08 - 0.12 | €/kWh |
| Tipik çalışma saati | 7,500 - 8,400 | h/yıl |
| Ortalama buhar tüketimi | 1.4 - 1.8 | kg/kg su buharlaştırma |

### İyileştirme Potansiyeli

Türkiye kağıt sektöründe tipik iyileştirme fırsatları:

| Önlem | Tasarruf Potansiyeli | Yaygınlık |
|-------|---------------------|-----------|
| Shoe press retrofit | %15 - 30 buhar tasarrufu | Orta (yeni tesislerde yaygın) |
| Cep havalandırma optimizasyonu | %5 - 10 | Düşük (çoğu tesiste eksik) |
| Hood ısı geri kazanımı | %8 - 15 | Orta |
| Kondensat sistemi iyileştirme | %3 - 8 | Düşük |
| Buhar kademeleme optimizasyonu | %5 - 10 | Orta |

## İlgili Dosyalar

- `dryer/formulas.md` — Kurutma exergy hesaplama formülleri
- `dryer/benchmarks.md` — Genel kurutucu benchmark verileri
- `dryer/equipment/drum_dryer.md` — Tambur/silindir kurutucu detayları
- `dryer/equipment/infrared_dryer.md` — IR kurutucu teknik bilgileri
- `dryer/solutions/exhaust_heat_recovery.md` — Egzoz ısı geri kazanım çözümleri
- `dryer/solutions/insulation.md` — İzolasyon iyileştirme çözümleri
- `dryer/solutions/mechanical_dewatering.md` — Mekanik su alma optimizasyonu
- `factory/sector_paper.md` — Kağıt fabrikası genel exergy profili

## Referanslar

1. Karlsson, M. (2000). *Papermaking Part 2: Drying*, Fapet Oy, Finland.
2. EU BREF (2015). *Best Available Techniques Reference Document for the Production of Pulp, Paper and Board*, European Commission.
3. TAPPI TIP 0404-63 (2019). "Energy Cost Reduction in Drying."
4. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press.
5. Stenström, S. (2020). "Drying of Paper: A Review 2000-2018," *Drying Technology*, 38(7), 825-845.
6. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier.
7. Szargut, J. (2005). *Exergy Method: Technical and Ecological Applications*, WIT Press.
8. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*, 2nd Edition, CRC Press.
9. CEPI (2022). *Key Statistics: European Pulp and Paper Industry*.
10. TAPPI (2018). "Best Practices in Paper Machine Drying," *TAPPI Journal*, 17(3).
