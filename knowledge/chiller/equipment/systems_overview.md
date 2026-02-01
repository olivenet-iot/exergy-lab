---
title: "Soğutma Suyu Sistemleri Genel Bakış — Chilled Water Systems Overview"
category: equipment
equipment_type: chiller
subtype: "Sistem Genel Bakış"
keywords: [soğutma sistemi, chiller, genel bakış]
related_files: [chiller/formulas.md, chiller/benchmarks.md, chiller/audit.md]
use_when: ["Soğutma sistemine genel bakış gerektiğinde", "Chiller sistemi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Soğutma Suyu Sistemleri Genel Bakış — Chilled Water Systems Overview

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Konu: Merkezi soğutma suyu sistemlerinin tasarımı, bileşenleri, kontrol stratejileri ve enerji/ekserji analizi
- Kapasite aralığı: 100 kW - 100+ MW soğutma kapasitesi
- Uygulama: Ticari binalar (ofis, AVM, otel), hastaneler, veri merkezleri, endüstriyel prosesler, bölgesel soğutma (district cooling)
- Referans çevre koşulları: T₀ = 25°C (298.15 K), P₀ = 1 atm (101.325 kPa)
- Tipik soğutma suyu sıcaklıkları: Gidiş 5-9°C, dönüş 10-16°C (konfor soğutma), gidiş 2-7°C (endüstriyel proses)
- Tipik soğutma suyu basıncı: 3-10 bar (kapalı devre)
- Sistem bileşenleri: Chiller(lar), birincil/ikincil pompalar, soğutma kulesi, borulama, kontrol vanaları, enerji depolama (opsiyonel)

## Çalışma Prensibi

Soğutma suyu sistemi, bir veya daha fazla chiller tarafından soğutulan suyun borulama ağı ile terminal ünitelere (fan-coil, AHU, proses ısı değiştiricisi) dağıtıldığı merkezi bir sistemdir. Terminal üniteler ortamdan ısı alarak suyu ısıtır ve ısınan su chiller'a geri döner.

### Temel Enerji Dengesi

```
Q_soğutma = m_su × cp × ΔT = m_su × cp × (T_dönüş - T_gidiş)

Burada:
  Q_soğutma : Toplam soğutma kapasitesi (kW)
  m_su      : Su debisi (kg/s)
  cp        : Suyun özgül ısısı (~4.18 kJ/kg·K)
  T_gidiş   : Gidiş suyu sıcaklığı (°C) — chiller çıkışı
  T_dönüş   : Dönüş suyu sıcaklığı (°C) — terminal ünite çıkışı
  ΔT        : Sıcaklık farkı (°C veya K) — "delta-T"
```

### Soğutma Kapasitesi Birimleri

| Birim | Tanım | Dönüşüm |
|-------|-------|---------|
| kW | Kilowatt (SI) | Referans |
| ton (RT) | Soğutma tonu (US) | 1 ton = 3.517 kW |
| kcal/h | Kilokalori/saat | 1 kW = 860 kcal/h |
| BTU/h | British thermal unit/saat | 1 kW = 3,412 BTU/h |

## Primer-Sekonder (Birincil-İkincil) Pompalama Sistemleri

### Sabit Birincil — Değişken İkincil (Constant Primary — Variable Secondary)

Bu, en yaygın kullanılan soğutma suyu pompalama konfigürasyonudur.

**Birincil (primer) devre:**
- Her chiller'ın kendi sabit devirli pompası vardır
- Sabit debili — chiller tasarım debisinde çalışır
- Chiller açılınca pompası da çalışır, chiller kapanınca pompa durur
- Amaç: Chiller'ın her koşulda tasarım debisini görmesini sağlamak

**İkincil (sekonder) devre:**
- Değişken devirli (VSD) pompalar ile yük talebine göre debi değişir
- Diferansiyel basınç (ΔP) sensörü ile kontrol edilir
- Terminal ünitelerdeki iki yollu vanalar debiyi ayarlar

**Decoupler (bypass) hattı:**
- Birincil ve ikincil devreyi birbirinden ayırır
- Birincil debi > ikincil debi olduğunda fazla su bypass'tan döner
- Birincil debi < ikincil debi olduğunda dönüş suyu bypass'tan gidiş hattına karışır (istenmeyen durum — yüksek gidiş suyu sıcaklığına yol açar)

```
Decoupler akış kuralı:
  Eğer m_primer > m_sekonder → bypass'ta aşağı akış (primer → dönüş)
  Eğer m_primer < m_sekonder → bypass'ta yukarı akış (dönüş → gidiş) — İSTENMEZ
  Eğer m_primer = m_sekonder → bypass'ta akış yok (ideal durum)

Burada:
  m_primer   : Birincil devre toplam debisi (kg/s)
  m_sekonder : İkincil devre toplam debisi (kg/s)
```

### Primer-Sekonder Sistemin Avantaj ve Dezavantajları

| Avantaj | Dezavantaj |
|---------|------------|
| Chiller debisi her zaman sabit — kararlı çalışma | Ek pompa seti (maliyet, enerji) |
| İkincil pompalar VSD ile verimli çalışır | Bypass akışı sıcaklık karışımına yol açabilir |
| Her chiller bağımsız kontrol edilebilir | Daha karmaşık kontrol mantığı |
| Chiller ekleme/çıkarma kolay | Fazladan alan gereksinimi |

## Değişken Birincil Akış (Variable Primary Flow — VPF)

Modern ve daha verimli alternatif — ikincil pompa setini ortadan kaldırır.

**Temel özellikler:**
- Tek pompa seti — VSD ile değişken debili
- Chiller'lar değişken debiye uygun olmalı (minimum debi sınırı: tipik tasarım debisinin %30-50'si)
- Bypass vanası yalnızca minimum akış koruması için — sürekli açık değil
- Daha düşük yatırım ve işletme maliyeti

```
Minimum akış koruması:
  m_bypass = m_min_chiller - m_yük   (eğer m_yük < m_min_chiller)
  m_bypass = 0                        (eğer m_yük ≥ m_min_chiller)

Burada:
  m_min_chiller : Chiller minimum izin verilen debisi (kg/s)
  m_yük         : Sistemin talep ettiği toplam debi (kg/s)
  m_bypass      : Bypass vanasından geçen debi (kg/s)
```

### VPF vs Primer-Sekonder Karşılaştırması

| Kriter | Primer-Sekonder | Değişken Birincil (VPF) |
|--------|-----------------|-------------------------|
| Pompa seti sayısı | 2 (primer + sekonder) | 1 |
| Toplam pompa gücü | Yüksek | Düşük (%15-30 tasarruf) |
| Kontrol karmaşıklığı | Orta | Yüksek (chiller staging kritik) |
| Chiller gereksinimi | Standart | Değişken debiye uygun |
| İlk yatırım | Yüksek (ek pompalar) | Düşük |
| Uygun olduğu kapasite | Tüm kapasiteler | Orta-büyük (>500 kW) |
| Delta-T yönetimi | Primer debiden bağımsız | Kritik öneme sahip |

## Delta-T Yönetimi

### Delta-T'nin Önemi

Soğutma suyu sistemlerinde ΔT (gidiş-dönüş sıcaklık farkı), sistemin verimliliğini doğrudan belirleyen en kritik parametredir.

```
Q = m × cp × ΔT  →  m = Q / (cp × ΔT)

Burada:
  Sabit Q (soğutma yükü) için:
  ΔT düşerse → m artmalı → pompa gücü artar
  ΔT yükselirse → m azalır → pompa gücü azalır

Pompa gücü ilişkisi:
  P_pompa ∝ m × ΔP ∝ (Q / ΔT) × f(m)
```

### Düşük Delta-T Sendromu (Low Delta-T Syndrome)

Soğutma suyu sistemlerinin en yaygın ve maliyetli sorunu. Tasarım ΔT'nin (tipik 5-7°C) altında çalışma durumudur.

**Belirtiler:**
- Dönüş suyu sıcaklığı tasarımdan düşük (örn. tasarım 12°C, gerçek 9°C)
- ΔT: Tasarım 5.5°C, gerçek 3-4°C
- Gereğinden fazla chiller devrede (kapasite karşılanamıyor gibi görünüyor)
- Pompalar fazla enerji tüketiyor
- Chiller'lar düşük verimli çalışıyor

**Nedenleri:**

| Neden | Açıklama | Çözüm |
|-------|----------|-------|
| 3 yollu vana kullanımı | Dönüş suyunu bypass ile karıştırır | 2 yollu vanaya dönüşüm |
| Kontrol vanası arızası | Vana tam kapanamıyor veya aşırı açık | Vana bakım/değişimi |
| Kirli ısı değiştirici | Terminal ünite kapasitesi düşer | Temizlik, yıkama |
| Hava sorunu (air lock) | Isı transferini bozar, debiyi etkiler | Hava atma, otomatik hava tahliye |
| Aşırı debi | Tasarım üstü debi — hız artsa da sıcaklık farkı düşer | VSD ile debi kontrolü, balans |
| Yanlış sıcaklık seti | Gidiş suyu sıcaklığı çok düşük ayarlanmış | Sıcaklık setini optimize etme |

**Maliyet etkisi:**

```
Düşük ΔT'nin enerji etkisi (örnek):
  Tasarım: 1,000 kW, ΔT = 5.5°C, debi = 43.5 L/s
  Gerçek: 1,000 kW, ΔT = 3.5°C, debi = 68.3 L/s

  Debi artışı: %57
  Pompa güç artışı (yaklaşık): %57 × 1.2 ≈ %68 (sürtünme kayıpları ile)
  Ek chiller devreye alınması → düşük yük verimi ile çalışma

Burada:
  Düşük ΔT, hem pompa hem chiller enerji tüketimini artırır
  Toplam enerji artışı: %10-30 (sisteme bağlı)
```

## Chiller Sıralama Stratejileri

### Eşit Yükleme (Equal Loading)

Tüm devredeki chiller'lara eşit yük dağıtımı. En basit kontrol stratejisi.

```
Yük_chiller_i = Q_toplam / n_chiller

Burada:
  Q_toplam     : Sistemin anlık toplam soğutma yükü (kW)
  n_chiller    : Devredeki chiller sayısı
  Yük_chiller_i: Her bir chiller'ın yükü (kW)
```

- Avantaj: Basit kontrol, eşit aşınma
- Dezavantaj: Optimal verimde çalışma garantisi yok

### Verim Bazlı Sıralama (Efficiency-Based Sequencing)

Her chiller'ın kısmi yük verim eğrisine göre en verimli kombinasyonun seçilmesi.

```
Hedef: min(Σ P_elec_i) koşuluyla Σ Q_i ≥ Q_toplam

P_elec_i = Q_i / COP_i(yük_oranı_i, T_cond_i)

Burada:
  P_elec_i    : i. chiller'ın elektrik tüketimi (kW)
  Q_i         : i. chiller'ın soğutma kapasitesi (kW)
  COP_i       : i. chiller'ın COP'u (yük oranı ve kondenser sıcaklığına bağlı)
  yük_oranı_i : Q_i / Q_nominal_i (%)
```

- Avantaj: Minimum enerji tüketimi
- Dezavantaj: Karmaşık kontrol, chiller COP eğrisi verisi gerekli

### Chiller Açma/Kapama Noktaları

| Durum | Koşul | Aksiyon |
|-------|-------|---------|
| Chiller ekleme | Mevcut chiller'lar >%85-90 yükte | Ek chiller devreye al |
| Chiller çıkarma | Toplam yük, (n-1) chiller ile <%80 | Bir chiller'ı devreden çıkar |
| Minimum çalışma süresi | — | ≥15-30 dakika (kısa çevrim önleme) |
| Gecikme süresi | Açma/kapama arası | ≥10-15 dakika |

## Serbest Soğutma (Free Cooling / Economizer)

Dış hava sıcaklığı yeterince düşük olduğunda chiller'ı devre dışı bırakarak soğutma kulesi veya kuru soğutucu ile doğrudan soğutma sağlama.

### Free Cooling Tipleri

| Tip | Çalışma Koşulu | Chiller | Tasarruf Potansiyeli |
|-----|----------------|---------|----------------------|
| Tam serbest soğutma (full free cooling) | T_dış_wb ≤ T_gidiş - (approach + güvenlik) | Kapalı | %100 kompresör tasarrufu |
| Kısmi serbest soğutma (partial free cooling) | T_dış_wb, tam serbest soğutma için yüksek ama yardımcı olabilecek seviyede | Kısmi yükte | %30-70 kompresör tasarrufu |
| Entegre serbest soğutma | Chiller içinde waterside economizer (ısı değiştirici) | Otomatik geçiş | Değişken |

```
Tam serbest soğutma koşulu:
  T_kule_çıkış = T_wb + Approach_kule

  Eğer T_kule_çıkış ≤ T_gidiş_set → chiller gerekmez (tam free cooling)
  Eğer T_kule_çıkış > T_gidiş_set → chiller gerekli (kısmi veya yok)

Burada:
  T_wb           : Dış hava yaş termometre sıcaklığı (°C)
  Approach_kule  : Soğutma kulesi yaklaşma değeri (°C), tipik 3-5°C
  T_gidiş_set    : Soğutma suyu gidiş sıcaklığı set değeri (°C)
```

### Türkiye'de Free Cooling Potansiyeli

| Şehir | Free Cooling Saatleri (saat/yıl, yaklaşık) | Yıl İçindeki Oranı (%) | Tasarruf Potansiyeli |
|-------|---------------------------------------------|------------------------|----------------------|
| İstanbul | 2,500-3,500 | 50-60 | Yüksek |
| Ankara | 3,000-4,000 | 60-70 | Çok yüksek |
| İzmir | 1,500-2,500 | 35-50 | Orta |
| Antalya | 1,000-1,500 | 25-35 | Düşük-orta |
| Erzurum | 4,500-5,500 | 75-85 | Çok yüksek |

Not: Yıl boyu soğutma ihtiyacı olan tesisler (veri merkezi, hastane vb.) için değerler; sadece yaz soğutması yapan binalarda free cooling saatleri mevsimsel çakışma nedeniyle düşebilir.

## Termal Enerji Depolama (TES)

### Buz Depolama (Ice Storage)
- Su yerine buz üretilerek gece tarifesinde enerji depolanır
- Buz oluşum sıcaklığı: -5°C ila -8°C (chiller evaporatör sıcaklığı daha düşük — COP düşer)
- Depolama yoğunluğu: ~334 kJ/kg (buzun erime entalpisi) — suya göre ~4 kat daha yoğun
- Avantaj: Puant yük kaydırma, chiller boyut küçültme, düşük gece tarifesi
- Dezavantaj: Düşük COP (%20-30 COP kaybı), ek ekipman, glikol gereksinimi

### Soğuk Su Depolama (Chilled Water Storage)
- Büyük izoleli tanklarda soğuk su depolanır (tipik 3,000-30,000 m³)
- Katmanlı (stratified) tank tasarımı — sıcak su üstte, soğuk su altta
- Depolama yoğunluğu: ~33 kJ/kg (8°C ΔT varsayımı) — buzdan düşük
- Avantaj: Normal COP ile üretim, basit sistem, düşük bakım
- Dezavantaj: Büyük hacim, alan gereksinimi

### TES Kapasite Hesabı

```
Buz depolama kapasitesi:
  Q_TES = m_buz × h_erime = m_buz × 334 kJ/kg

Soğuk su depolama kapasitesi:
  Q_TES = m_su × cp × ΔT = V × ρ × cp × ΔT

Burada:
  m_buz   : Depolanan buz kütlesi (kg)
  h_erime : Buzun erime entalpisi (~334 kJ/kg)
  V       : Tank hacmi (m³)
  ρ       : Su yoğunluğu (~1,000 kg/m³)
  cp      : Suyun özgül ısısı (~4.18 kJ/kg·K)
  ΔT      : Sıcak-soğuk su sıcaklık farkı (K)
```

## Bölgesel Soğutma (District Cooling)

Büyük ölçekli merkezi soğutma tesisinden birden fazla binaya soğutma suyu dağıtımı.

| Özellik | Değer / Açıklama |
|---------|------------------|
| Kapasite | 5,000 - 500,000+ ton (17.5 MW - 1,750+ MW) |
| Gidiş suyu sıcaklığı | 4-6°C |
| Dönüş suyu sıcaklığı | 12-16°C |
| ΔT | 8-12°C (bireysel binalardan yüksek) |
| Dağıtım mesafesi | 1-10 km |
| Boru malzemesi | Ön izoleli çelik veya PE |
| COP (merkezi tesis) | 5.5-7.5 (büyük ölçek avantajı) |
| Avantaj | Ölçek ekonomisi, yüksek verim, bina içi alan tasarrufu |
| Dezavantaj | Yüksek altyapı yatırımı, boru kayıpları, bağımlılık |

## Sistem Düzeyinde Ekserji Akışı

### Ekserji Akış Diyagramı (Tipik Soğutma Suyu Sistemi)

```
ELEKTRİK GİRİŞİ (saf ekserji) = 100%
|
|=== Chiller kompresör (%70-85 toplam elektrik)
|    |
|    |--- Kompresör tersinmezliği (%10-20) → EKSERJI YIKIMI
|    |--- Kondenser ısı transferi tersinmezliği (%5-10) → EKSERJI YIKIMI
|    |--- Evaporatör ısı transferi tersinmezliği (%3-8) → EKSERJI YIKIMI
|    |--- Genleşme tersinmezliği (%3-5) → EKSERJI YIKIMI
|    |
|    v
|    SOĞUTMA SUYU EKSERJİSİ (%15-30)
|
|=== Pompalar (%10-25 toplam elektrik)
|    |
|    |--- Pompa ve motor tersinmezliği (%3-8) → EKSERJI YIKIMI
|    |--- Boru sürtünme kaybı (%2-5) → EKSERJI YIKIMI
|    |
|    v
|    HİDROLİK İŞ → SUYUN TAŞINMASI
|
|=== Soğutma kulesi (%5-10 toplam elektrik)
|    |
|    |--- Fan ve buharlaşma tersinmezliği (%3-8) → EKSERJI YIKIMI
|    |
|    v
|    ATIK ISI ATIMI
|
FAYDALANMA (terminal ünitelerde soğutma):
  Terminal ünite ekserji verimi: %5-15 (düşük ΔT nedeniyle)
  Toplam sistem ekserji verimi: %5-20

Burada:
  Toplam sistem ekserji verimi = Ex_soğutma_faydalı / Ex_elektrik_toplam
  Ex_soğutma_faydalı: Ortamdan çekilen ısının ekserji değeri
  Ex_elektrik_toplam: Chiller + pompa + kule toplam elektrik (kW)
```

### Soğutma Suyu Ekserji Hesabı

```
Ex_su = m_su × cp × [(T_su - T₀) - T₀ × ln(T_su / T₀)]

Soğutma ekserjisi (soğutulan ortamdan):
  Ex_soğutma = Q_soğutma × (T₀/T_ortam - 1)

Burada:
  T_su     : Su sıcaklığı (K)
  T₀       : Referans çevre sıcaklığı (K) = 298.15 K
  T_ortam  : Soğutulan ortam sıcaklığı (K, genellikle 24°C = 297.15 K)
  Q_soğutma: Soğutma kapasitesi (kW)
```

Not: T_ortam ≈ T₀ olduğunda soğutma ekserjisi çok düşüktür. Bu, soğutma sistemlerinin ekserji veriminin düşük olmasının temel nedenidir.

## Boru Boyutlandırma ve Dağıtım Kayıpları

### Önerilen Su Hızları

| Boru Çapı (mm) | Önerilen Hız (m/s) | Maksimum Hız (m/s) | Basınç Kaybı (Pa/m) |
|-----------------|---------------------|---------------------|----------------------|
| 25-50 | 0.5-1.0 | 1.5 | 100-400 |
| 65-100 | 1.0-1.5 | 2.0 | 100-300 |
| 125-200 | 1.5-2.0 | 2.5 | 100-250 |
| 250-400 | 2.0-2.5 | 3.0 | 80-200 |
| >400 | 2.0-3.0 | 3.5 | 60-150 |

### Boru Isı Kazanımı (Izolasyon Kaybı)

```
Q_kayıp = U × A × (T_ortam - T_su) = U × π × D_dış × L × (T_ortam - T_su)

Burada:
  Q_kayıp : Boru ısı kazanımı (W)
  U       : Toplam ısı geçiş katsayısı (W/m²·K)
  A       : Boru dış yüzey alanı (m²)
  D_dış   : İzolasyonlu boru dış çapı (m)
  L       : Boru uzunluğu (m)
  T_ortam : Boru çevresindeki ortam sıcaklığı (°C)
  T_su    : Soğutma suyu sıcaklığı (°C)
```

| İzolasyon Kalınlığı (mm) | U Değeri (W/m²·K) | Kayıp (W/m, DN100, ΔT=20°C) |
|--------------------------|--------------------|-----------------------------|
| Yok (çıplak boru) | 10-15 | 60-90 |
| 19 mm | 2.0-3.0 | 12-18 |
| 25 mm | 1.5-2.5 | 9-15 |
| 38 mm | 1.0-1.8 | 6-11 |
| 50 mm | 0.7-1.3 | 4-8 |

## Kontrol Stratejileri

### 1. Gidiş Suyu Sıcaklığı Kontrolü

```
Sabit set noktalı kontrol:
  T_gidiş = 7°C (sabit) — en basit, en yaygın

Sıfırlama (reset) kontrollü:
  T_gidiş = f(T_dış) veya f(Yük)

Dış hava sıcaklığına göre reset örneği:
  T_gidiş = 7 + 0.3 × (35 - T_dış)   (T_dış < 35°C iken)
  T_gidiş_max = 12°C, T_gidiş_min = 7°C

Burada:
  T_dış    : Dış hava sıcaklığı (°C)
  Her 1°C gidiş suyu sıcaklığı artışı ≈ %1.5-2 chiller COP artışı
```

### 2. Diferansiyel Basınç Kontrolü

İkincil (veya VPF) pompaların VSD kontrolü — en uzak terminal ünitede minimum ΔP sağlanır.

| Kontrol Yöntemi | Açıklama | Enerji Tasarrufu |
|-----------------|----------|------------------|
| Sabit ΔP (uzak nokta) | Sabit basınç farkı hedefi | Orta |
| Sıfırlamalı ΔP | Yüke göre ΔP hedefi azaltılır | Yüksek |
| Vana pozisyonu bazlı | En açık vana %90-95'te → ΔP azalt | En yüksek |

### 3. Kondenser Suyu Sıcaklığı Optimizasyonu

```
T_kondenser_gidiş = max(T_wb + Approach_kule + Approach_kondenser, T_min_kondenser)

Burada:
  T_wb              : Dış hava yaş termometre sıcaklığı (°C)
  Approach_kule     : Soğutma kulesi yaklaşma değeri (°C)
  Approach_kondenser: Chiller kondenser yaklaşma değeri (°C)
  T_min_kondenser   : Chiller minimum kondenser suyu sıcaklığı (°C, üretici sınırı)
```

Düşük kondenser suyu sıcaklığı, chiller COP'unu artırır ancak soğutma kulesi fan gücünü artırabilir. Optimum nokta, toplam sistem enerjisini minimize eden sıcaklıktır.

## Hidrolik Konular

### Bypass / Decoupler Boyutlandırma

```
Decoupler boru çapı: Ana boru çapı ile aynı veya bir küçük
Decoupler boyu: 4-6 × boru çapı (minimum karışım için)
Akış hızı: <0.3 m/s (minimum karışım)

Decoupler diferansiyel basıncı: ≈ 0 (ihmal edilebilir)

Burada:
  Decoupler, birincil ve ikincil devrelerin birbirini hidrolik olarak
  etkilemesini önler — her devre kendi pompası ile bağımsız çalışır
```

### Hava Yönetimi

| Sorun | Belirti | Çözüm |
|-------|---------|-------|
| Hava birikimi | Düşük debi, gürültü, yetersiz soğutma | Otomatik hava tahliye vanası (yüksek noktalarda) |
| Mikro hava kabarcıkları | Erozyon, pompa kavitasyonu | Degazör (mikro kabarcık ayırıcı) |
| Oksijen korozyonu | Boru iç korozyonu | Kapalı devre, inhibitör, degazör |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Gidiş suyu sıcaklığı | °C | 5-9 | PT100 sensör |
| Dönüş suyu sıcaklığı | °C | 10-16 | PT100 sensör |
| Su debisi (toplam) | m³/h veya L/s | Sisteme bağlı | Ultrasonik / EM debimetre |
| Chiller elektrik tüketimi | kW | Sisteme bağlı | Güç analizörü |
| Pompa elektrik tüketimi | kW | Sisteme bağlı | Güç analizörü |
| Soğutma kulesi fan gücü | kW | Sisteme bağlı | Güç analizörü |
| Dış hava sıcaklığı ve nem | °C, %RH | Mevsime bağlı | Hava istasyonu sensörü |
| Chiller sayısı ve durumu | adet, açık/kapalı | — | BMS veya gözlem |

### Opsiyonel (detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Kondenser giriş/çıkış suyu sıcaklığı | °C | 28-42 | PT100 sensör |
| Kondenser su debisi | m³/h | Sisteme bağlı | Debimetre |
| ΔP (diferansiyel basınç) | kPa veya bar | 50-300 kPa | ΔP sensörü |
| Terminal ünite vana pozisyonları | % | 0-100 | BMS okuma |
| Bypass akışı | m³/h | 0 - birincil debi | Debimetre veya sıcaklık farkı ile hesaplama |
| Bireysel chiller COP | — | 3.0-7.0 | Hesaplama (Q/P) |
| Enerji sayacı (soğutma) | kWh | — | Btu sayacı / enerji ölçer |

### Nameplate Bilgileri
- Her chiller: Marka, model, nominal kapasite (kW/ton), nominal COP/EER, soğutucu akışkan, kompresör tipi
- Pompalar: Marka, model, debi (m³/h), head (m), motor gücü (kW)
- Soğutma kulesi: Marka, model, nominal ısı atım kapasitesi (kW), fan gücü (kW)
- Boru sistemi: Ana boru çapları, toplam boru uzunluğu (yaklaşık)

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Gidiş suyu sıcaklığı | 7°C | Standart konfor soğutma |
| Dönüş suyu sıcaklığı | 12°C | Tasarım ΔT = 5°C |
| ΔT (tasarım) | 5°C | Türkiye HVAC standardı |
| ΔT (gerçek) | 3.5-4.0°C | Düşük ΔT sendromu yaygın |
| Chiller COP (su soğutmalı) | 5.0 | Tam yükte |
| Chiller COP (hava soğutmalı) | 3.0 | Tam yükte, 35°C dış hava |
| Pompa verimi | %70 | Genel endüstriyel ortalama |
| Pompa motor verimi | %92 | IE3 motor |
| Boru ısı kazanımı | %2-5 | Toplam kapasite yüzdesi |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa | Standart ölü durum |
| Yıllık soğutma çalışma saati | 2,500 saat/yıl | Türkiye, ticari bina |
| Elektrik birim fiyatı | 0.10 EUR/kWh | Türkiye sanayi tarifesi (yaklaşık) |

## Performans Tablosu — Sistem Konfigürasyonuna Göre

| Sistem Tipi | Kapasite (kW) | Chiller COP | Pompa Gücü (% soğutma) | Kule Gücü (% soğutma) | Sistem kW/ton | Yaklaşık Sistem Ekserji Verimi (%) |
|-------------|---------------|-------------|------------------------|----------------------|---------------|-------------------------------------|
| Hava soğutmalı, sabit hız | 100-500 | 2.8-3.2 | 5-10 | — | 1.2-1.5 | 5-10 |
| Hava soğutmalı, VSD | 100-500 | 3.0-3.5 | 3-7 | — | 1.0-1.3 | 7-12 |
| Su soğutmalı, P/S sabit primer | 200-5,000 | 4.5-5.5 | 8-15 | 3-6 | 0.65-0.90 | 10-18 |
| Su soğutmalı, VPF | 500-10,000 | 4.8-6.0 | 5-10 | 3-6 | 0.55-0.80 | 12-20 |
| Su soğutmalı, VPF + free cooling | 500-10,000 | 5.0-6.5* | 4-8 | 3-5 | 0.45-0.70* | 15-25 |
| Bölgesel soğutma | 10,000+ | 5.5-7.0 | 5-10 | 2-5 | 0.40-0.65 | 15-25 |

*Yıllık ortalama — free cooling saatlerini içerir.

## Dikkat Edilecekler

1. **Delta-T yönetimi:** Düşük ΔT sendromu, soğutma suyu sistemlerinin en yaygın ve en maliyetli sorunudur — 2 yollu vana kullanımı, düzenli ısı değiştirici temizliği ve debi dengeleme ile önlenmelidir
2. **Chiller sıralama:** Chiller açma/kapama kararları toplam sistem enerjisini dikkate almalıdır — yalnızca chiller yüküne değil, pompa ve kule enerjisine de bakılmalıdır
3. **Gidiş suyu sıcaklığı sıfırlama:** Dış koşullara göre gidiş suyu sıcaklığını yükseltmek büyük tasarruf sağlar — her 1°C artış ≈ %1.5-2 COP iyileşmesi
4. **Kondenser suyu optimizasyonu:** Kondenser suyu sıcaklığını düşürmek chiller verimini artırır ancak kule fan gücünü artırabilir — optimum nokta toplam minimumu verir
5. **Free cooling fırsatı:** Yıl boyu soğutma gereken tesislerde (veri merkezi, hastane) free cooling önemli tasarruf sağlar — özellikle İç Anadolu ve Doğu Anadolu bölgelerinde
6. **Boru izolasyonu:** Soğutma suyu boruları mutlaka yoğuşma önleyici buhar bariyerli izolasyon ile kaplanmalıdır — yetersiz izolasyon hem enerji kaybı hem de tavan/zemin su hasarı yaratır
7. **Hidrolik dengeleme:** Sistem dengesizliği, bazı bölgelerin fazla soğutma alırken bazılarının yetersiz kalmasına neden olur — statik veya dinamik balans vanaları ile dengeleme yapılmalıdır
8. **Su kalitesi:** Kapalı devre soğutma suyunda korozyon inhibitörü ve pH kontrolü yapılmalıdır — korozyon ve biyolojik oluşum ısı transfer verimini düşürür

## İlgili Dosyalar
- Soğutucu akışkanlar: `equipment/chiller_refrigerants.md`
- Soğutma kulesi: `equipment/cooling_tower.md`
- Santrifüj pompa: `equipment/pump_centrifugal.md`
- VSD pompa uygulaması: `solutions/pump_vsd.md`
- Pompa sistemleri genel bakış: `equipment/pumping_systems_overview.md`
- Chiller ekserji hesaplamaları: `formulas/chiller_exergy.md`
- Serbest soğutma (free cooling): `solutions/chiller_free_cooling.md`
- Chiller seçim ve boyutlandırma: `solutions/chiller_selection.md`
- Soğutma benchmark verileri: `benchmarks/chiller_benchmarks.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment (2024), Chapter 13: Hydronic Heating and Cooling.
- ASHRAE Handbook — HVAC Applications (2023), Chapter 42: Supervisory Control Strategies and Optimization.
- Taylor, S.T. (2002). "Primary-Only vs. Primary-Secondary Variable Flow Systems," *ASHRAE Journal*, 44(2), 25-29.
- Taylor, S.T. (2012). "Optimizing Design & Control of Chilled Water Plants," *ASHRAE Journal*, 54 (6-12 serisi).
- Hartman, T.B. (2005). "Designing Efficient Systems with the Equal Marginal Performance Principle," *ASHRAE Journal*, 47(7), 64-70.
- Kirsner, W. (1996). "The Demise of the Primary-Secondary Pumping Paradigm for Chilled Water Plant Design," *Heating/Piping/Air Conditioning Engineering*, 68(11).
- ASHRAE Standard 90.1-2022. *Energy Standard for Buildings Except Low-Rise Residential Buildings*.
- EN 14825:2022. *Air conditioners, liquid chilling packages and heat pumps, with electrically driven compressors, for space heating and cooling — Testing and rating at part load conditions*.
- Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier.
- Bejan, A. (2016). *Advanced Engineering Thermodynamics*, 4th Edition, Wiley.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- CIBSE Guide B2 (2016). *Ventilation and Ductwork*. CIBSE Guide B1 (2016). *Heating and Cooling*.
- Wang, S. (2001). *Handbook of Air Conditioning and Refrigeration*, 2nd Edition, McGraw-Hill.
