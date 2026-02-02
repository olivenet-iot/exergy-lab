---
title: "Isı Eşanjörleri Genel Bakış — Heat Exchanger Systems Overview"
category: equipment
equipment_type: heat_exchanger
subtype: "Sistem Genel Bakış"
keywords: [eşanjör, ısı değiştirici, heat exchanger, sınıflandırma, seçim kriterleri, akış düzeni]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/equipment/shell_and_tube.md, heat_exchanger/equipment/plate.md, heat_exchanger/equipment/air_cooled.md]
use_when: ["Isı eşanjörü sistemine genel bakış gerektiğinde", "Eşanjör tipi seçimi yapılırken", "Akış düzeni karşılaştırması istendiğinde"]
priority: high
last_updated: 2026-02-01
---
# Isı Eşanjörleri Genel Bakış — Heat Exchanger Systems Overview

> Son güncelleme: 2026-02-01

## Genel Bilgiler

Isı eşanjörleri (heat exchangers), iki veya daha fazla akışkan arasında ısı transferi sağlayan cihazlardır. Endüstriyel tesislerde enerji geri kazanımı, proses ısıtma/soğutma, buhar üretimi ve atık ısı değerlendirme gibi kritik görevleri üstlenirler. Tipik bir endüstriyel tesisin toplam enerji tüketiminin %15-40'ı ısı eşanjörlerindeki verimsizliklerden etkilenir.

- Uygulama alanları: Petrokimya, gıda, ilaç, enerji santralleri, HVAC, kağıt, çimento
- Kapasite aralığı: 1 kW - 1,000+ MW
- Çalışma sıcaklığı: -200°C ile 1,400°C arası (malzemeye bağlı)
- Çalışma basıncı: Vakum - 500+ bar
- Referans çevre koşulları: T₀ = 25°C (298.15 K), P₀ = 101.325 kPa

## Isı Eşanjörü Sınıflandırması

### Yapısal Sınıflandırma (By Construction)

| Tip | Alt Tipler | Kapasite Aralığı | Tipik Uygulama |
|-----|-----------|-------------------|----------------|
| Gövde-Boru (Shell & Tube) | Sabit tüp plakası, U-boru, yüzen kafa | 10 kW - 500 MW | Petrokimya, enerji, proses |
| Plakalı (Plate) | Contalı (GPHE), lehimli (BPHE), kaynaklı | 1 kW - 50 MW | HVAC, gıda, kimya |
| Hava Soğutmalı (Air-Cooled) | Cebri çekiş, indüklenmiş çekiş | 50 kW - 200 MW | Rafineri, santral, doğalgaz |
| Çift Borulu (Double Pipe) | Düz, saç tokası (hairpin), kanatlı | 1 kW - 5 MW | Yüksek basınç, küçük kapasite |
| Spiral | Tek geçişli, çift geçişli | 10 kW - 30 MW | Yüksek viskozite, çamurlu akışkan |
| Ekonomizer | Yoğuşmalı, yoğuşmasız | 50 kW - 50 MW | Kazan baca gazı geri kazanım |
| Hava Ön Isıtıcı | Döner (Ljungström), borulu, plakalı | 100 kW - 100 MW | Yanma havası ön ısıtma |
| Reküperatör/Rejeneratör | Metalik, seramik | 10 kW - 50 MW | Fırın, fırın, cam sanayi |

### Akış Düzenine Göre Sınıflandırma (By Flow Arrangement)

| Akış Düzeni | Tanım | Termal Etkinlik (ε) | Kullanım Alanı |
|-------------|-------|---------------------|----------------|
| Karşı akış (Counterflow) | Akışkanlar zıt yönde akar | En yüksek (0.75-0.98) | Gövde-boru, çift borulu, spiral |
| Paralel akış (Parallel flow) | Akışkanlar aynı yönde akar | Düşük (0.40-0.65) | Sıcaklık kontrolü gereken uygulamalar |
| Çapraz akış (Crossflow) | Akışkanlar birbirine dik akar | Orta (0.50-0.85) | Hava soğutmalı eşanjörler, radyatörler |
| Karışık akış (Multi-pass) | Birden fazla geçiş ile karşı/paralel kombinasyonu | Orta-yüksek (0.60-0.92) | Çok geçişli gövde-boru |

### Isı Transfer Mekanizmasına Göre Sınıflandırma

| Mekanizma | Açıklama | U Aralığı (W/(m²·K)) | Örnek |
|-----------|----------|----------------------|-------|
| Tek fazlı konveksiyon | Her iki akışkan da tek fazda | 50-1,500 | Yağ/su, gaz/gaz |
| Yoğuşma (Condensation) | Bir taraf yoğuşuyor | 1,000-10,000 | Buhar/su, soğutucu yoğuşma |
| Kaynama (Boiling) | Bir taraf kaynıyor | 500-8,000 | Reboiler, evaporatör |
| Radyasyon | Yüksek sıcaklıkta ışınım ile transfer | 20-200 | Fırın reküperatörü |
| Kombine | İki veya daha fazla mekanizma birlikte | Değişken | Buhar jeneratörü |

## Tüm Eşanjör Tiplerinin Karşılaştırma Tablosu

| Tip | U Aralığı (W/(m²·K)) | Basınç (bar) | Sıcaklık (°C) | Göreceli Maliyet | Kirlenme Eğilimi | Kompaktlık |
|-----|----------------------|-------------|---------------|------------------|-------------------|------------|
| Gövde-Boru (S&T) | 150-5,000 | 0.1-300+ | -200 ile 600+ | Orta | Orta-Yüksek | Düşük |
| Contalı Plaka (GPHE) | 1,000-8,000 | 0.1-25 | -35 ile 200 | Düşük-Orta | Düşük (kolay temizlik) | Yüksek |
| Lehimli Plaka (BPHE) | 1,000-7,000 | 0.1-45 | -195 ile 225 | Düşük | Düşük | Çok Yüksek |
| Kaynaklı Plaka | 1,000-7,500 | 0.1-40 | -50 ile 350 | Orta-Yüksek | Orta | Yüksek |
| Hava Soğutmalı | 20-300 | 0.1-200 | -50 ile 400 | Yüksek | Yüksek (hava tarafı) | Düşük |
| Çift Borulu | 100-3,000 | 0.1-500+ | -200 ile 600 | Düşük (küçük) | Düşük-Orta | Düşük |
| Spiral | 500-4,000 | 0.1-25 | -50 ile 400 | Orta-Yüksek | Çok Düşük (öz temizleme) | Orta |
| Ekonomizer | 30-200 | Baca gazı tarafı: atmosfer | 80-450 | Orta | Yüksek (kurum, asit) | Orta |
| Hava Ön Isıtıcı (döner) | 15-100 | Atmosfer | 80-500 | Yüksek | Yüksek | Orta |
| Reküperatör (metalik) | 20-150 | Atmosfer-10 | 200-1,100 | Yüksek | Orta | Düşük |
| Reküperatör (seramik) | 10-80 | Atmosfer | 200-1,400 | Çok Yüksek | Düşük | Düşük |

## Seçim Kriterleri ve Karar Matrisi

### Birincil Seçim Kriterleri

| Kriter | Açıklama | Etkisi |
|--------|----------|--------|
| Çalışma sıcaklığı | Malzeme ve conta sınırlamaları | GPHE < 200°C; S&T < 600°C; seramik < 1,400°C |
| Çalışma basıncı | Mekanik dayanım gereksinimleri | GPHE < 25 bar; S&T < 300+ bar |
| Kirlenme eğilimi (fouling) | Temizlik gereksinimleri | Spiral: öz temizleme; GPHE: kolay temizlik; S&T: mekanik temizlik |
| Akışkan uyumluluğu | Korozyon, viskozite, fazı | Agresif akışkan: kaynaklı veya S&T; viskoz: spiral |
| Maliyet (yatırım + işletme) | Toplam sahip olma maliyeti | BPHE en ucuz (küçük), S&T orta, seramik en pahalı |
| Bakım erişimi | Mekanik temizlik imkanı | S&T: tüp çekme; GPHE: plaka sökme; BPHE: erişim yok |
| Alan kısıtı | Yerleşim planı | Plaka: en kompakt (S&T'nin %20-30 alanı) |
| Isı geri kazanım oranı | NTU ve etkinlik gereksinimi | Karşı akış > çapraz akış > paralel akış |

### Karar Matrisi (Puanlama: 1-5, yüksek = iyi)

| Kriter | Ağırlık | S&T | GPHE | BPHE | Hava Soğutmalı | Çift Boru | Spiral |
|--------|---------|-----|------|------|----------------|-----------|--------|
| Yüksek basınç | 0.15 | 5 | 2 | 3 | 4 | 5 | 2 |
| Yüksek sıcaklık | 0.15 | 5 | 2 | 2 | 4 | 5 | 3 |
| Kirlenme direnci | 0.15 | 3 | 4 | 2 | 2 | 3 | 5 |
| Kompaktlık | 0.10 | 2 | 5 | 5 | 1 | 2 | 3 |
| Düşük maliyet | 0.15 | 3 | 4 | 5 | 2 | 4 | 3 |
| Bakım kolaylığı | 0.10 | 4 | 5 | 1 | 3 | 3 | 3 |
| Büyük kapasite | 0.10 | 5 | 3 | 2 | 4 | 1 | 3 |
| Exergy verimi | 0.10 | 4 | 5 | 5 | 2 | 4 | 4 |

## Akış Düzenleri Detaylı Karşılaştırma

### Karşı Akış (Counterflow)

En yüksek termal etkinlik sağlayan düzendir. Soğuk akışkan çıkışı, sıcak akışkan girişine yaklaşabilir.

```
Karşı akış sıcaklık profili:

Sıcak akışkan: T_h,in ----→ T_h,out
                  ←----
Soğuk akışkan: T_c,out ←---- T_c,in

T_c,out > T_h,out olabilir (sıcaklık çaprazlaması mümkün)

LMTD (Logaritmik Ortalama Sıcaklık Farkı):
  ΔT₁ = T_h,in - T_c,out
  ΔT₂ = T_h,out - T_c,in
  LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁ / ΔT₂)
```

### Paralel Akış (Parallel Flow)

Her iki akışkan da aynı yönde akar. Soğuk akışkan çıkışı asla sıcak akışkan çıkışını aşamaz.

```
Paralel akış sıcaklık profili:

Sıcak akışkan: T_h,in ----→ T_h,out
                ----→
Soğuk akışkan: T_c,in ----→ T_c,out

T_c,out < T_h,out her zaman (sıcaklık çaprazlaması mümkün değil)

LMTD:
  ΔT₁ = T_h,in - T_c,in
  ΔT₂ = T_h,out - T_c,out
  LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁ / ΔT₂)
```

**Not:** Paralel akış, hassas sıcaklık kontrolü gerektiren uygulamalarda tercih edilir (sıcaklık ani değişim yerine kademeli yaklaşma).

### Çapraz Akış (Crossflow)

Akışkanlar birbirine dik akar. Hava soğutmalı eşanjörlerde ve kompakt eşanjörlerde yaygındır.

```
Çapraz akış düzeni:

  Hava (soğuk akışkan) →→→→→→
                        ↑↑↑↑↑↑
  Sıcak akışkan         ||||||
  (borular içinde)       ↑↑↑↑↑↑

LMTD düzeltme faktörü: F = 0.80-0.95 (karışıklık durumuna göre)
Q = U × A × F × LMTD_karşıakış
```

### Çok Geçişli Düzenler (Multi-Pass)

Gövde-boru eşanjörlerde tüp tarafında birden fazla geçiş yapılarak ısı transfer katsayısı artırılır.

```
Tipik geçiş sayıları ve LMTD düzeltme faktörü (F):

| Gövde Geçişi | Tüp Geçişi | F Faktörü | Not |
|--------------|------------|-----------|-----|
| 1 | 1 | 1.00 | Saf karşı akış |
| 1 | 2 | 0.80-0.95 | En yaygın konfigürasyon |
| 1 | 4 | 0.75-0.92 | Yüksek ısı transfer katsayısı |
| 2 | 4 | 0.90-0.98 | Yüksek etkinlik gereken uygulamalar |
| 2 | 6 | 0.88-0.97 | Uzun ünite boyundan kaçınma |

Kural: F < 0.75 ise gövde geçiş sayısı artırılmalıdır.
```

## Endüstriyel Uygulamalar

### Tipik Uygulama Tablosu

| Sektör | Uygulama | Eşanjör Tipi | Tipik Kapasite | Akışkanlar |
|--------|----------|-------------|---------------|------------|
| Petrokimya | Ham petrol ön ısıtma | S&T, çift borulu | 5-100 MW | Ham petrol / Proses akımı |
| Petrokimya | Kondenser | S&T | 10-200 MW | Hidrokarbon buharı / Soğutma suyu |
| Enerji santralı | Baca gazı ekonomizer | Kanatlı borulu | 1-50 MW | Baca gazı / Besleme suyu |
| Enerji santralı | Kondenser | S&T | 100-1,000 MW | Buhar / Soğutma suyu |
| Gıda ve süt | Pastörizasyon | GPHE | 50-5,000 kW | Süt / Sıcak su |
| Gıda ve süt | CIP ısıtma | BPHE | 10-500 kW | Buhar / Su |
| HVAC | Chiller evaporatör | BPHE, S&T | 50-10,000 kW | Soğutucu / Su |
| HVAC | Serbest soğutma | GPHE | 100-5,000 kW | Soğutma suyu / Kule suyu |
| Kimya | Reaktör soğutma | S&T, spiral | 100-50,000 kW | Proses / Soğutma suyu |
| Kağıt | Siyah çözelti ısıtma | Spiral | 500-10,000 kW | Siyah çözelti / Buhar |
| Çelik | Fırın atık ısı geri kazanım | Reküperatör | 1-50 MW | Baca gazı / Hava |
| Cam | Fırın geri kazanım | Seramik rejeneratör | 5-100 MW | Baca gazı / Yanma havası |

## Exergy Perspektifinden Eşanjör Seçimi

### Exergy Yıkımının Temel Kaynakları

```
Eşanjör exergy yıkımı bileşenleri:

Ex_yıkım = Ex_ΔT + Ex_ΔP + Ex_sızıntı + Ex_çevre

Burada:
  Ex_ΔT     : Sonlu sıcaklık farkından kaynaklanan exergy yıkımı (kW)
  Ex_ΔP     : Basınç düşüşünden kaynaklanan exergy yıkımı (kW)
  Ex_sızıntı: Akışkan sızıntısından kaynaklanan exergy kaybı (kW)
  Ex_çevre  : Çevreye ısı kaybından kaynaklanan exergy kaybı (kW)

Sıcaklık farkından exergy yıkımı:
  Ex_ΔT = T₀ × ΔS_üretilen = T₀ × [m_c × cp_c × ln(T_c,out/T_c,in) + m_h × cp_h × ln(T_h,out/T_h,in)]

Basınç düşüşünden exergy yıkımı:
  Ex_ΔP ≈ m × v × ΔP / η_pompa   (sıvılar için)
  Ex_ΔP ≈ m × R × T₀ × ln(P_in/P_out) / M   (gazlar için)
```

### Exergy Verimi Tanımları

```
Eşanjör exergy verimi:

  η_ex = Ex_çıkış / Ex_giriş

Veya daha spesifik olarak:

  η_ex = (Ex_soğuk,çıkış - Ex_soğuk,giriş) / (Ex_sıcak,giriş - Ex_sıcak,çıkış)

Burada:
  Ex = m × [(h - h₀) - T₀ × (s - s₀)]
```

### Exergy Verimini Etkileyen Faktörler

| Faktör | Exergy Üzerindeki Etkisi | Tasarım Önerisi |
|--------|--------------------------|-----------------|
| Sıcaklık farkı (ΔT_lm) | ΔT artarsa exergy yıkımı artar | Minimum pratik ΔT hedefle (pinch analizi) |
| Akış düzeni | Karşı akış en düşük exergy yıkımı | Mümkünse karşı akış tercih et |
| Basınç düşüşü | Pompa/fan gücü ile doğrudan ilişkili | Optimal hız ve kanat tasarımı |
| Isı transfer alanı | Büyük alan = düşük ΔT = düşük exergy yıkımı | Ekonomik optimum bul |
| Kirlenme | Etkin ΔT'yi artırır, exergy yıkımını artırır | Düzenli temizlik programı |

### Tipik Exergy Verimleri

| Eşanjör Tipi | Tipik Exergy Verimi (%) | En İyi Uygulama (%) | Not |
|-------------|------------------------|--------------------|-----|
| Gövde-Boru (gaz/gaz) | 25-50 | 50-70 | Düşük U değeri, büyük ΔT |
| Gövde-Boru (sıvı/sıvı) | 50-75 | 75-90 | Orta U değeri |
| Gövde-Boru (yoğuşma) | 40-65 | 65-85 | Yüksek U, faz değişimi |
| Plakalı (GPHE) | 60-85 | 85-95 | Yüksek U, düşük ΔT |
| Hava soğutmalı | 20-40 | 40-55 | Düşük hava tarafı U |
| Çift borulu | 50-75 | 75-90 | Saf karşı akış |
| Spiral | 55-80 | 80-90 | Karşı akış, yüksek U |
| Ekonomizer | 30-55 | 55-70 | Gaz/sıvı, kirlenme etkisi |
| Reküperatör | 35-60 | 60-80 | Yüksek sıcaklıkta yüksek exergy kalitesi |

## Isı Transfer Temel Formülleri

```
Genel ısı transfer denklemi:
  Q = U × A × ΔT_m

Burada:
  Q     : Isı transfer hızı (kW)
  U     : Toplam ısı geçiş katsayısı (W/(m²·K))
  A     : Isı transfer alanı (m²)
  ΔT_m  : Ortalama sıcaklık farkı (°C veya K)

Toplam ısı geçiş direnci (düz duvar için):
  1/U = 1/h_i + R_f,i + t_w/k_w + R_f,o + 1/h_o

Burada:
  h_i   : İç taraf konveksiyon katsayısı (W/(m²·K))
  h_o   : Dış taraf konveksiyon katsayısı (W/(m²·K))
  R_f,i : İç taraf kirlenme direnci (m²·K/W)
  R_f,o : Dış taraf kirlenme direnci (m²·K/W)
  t_w   : Duvar kalınlığı (m)
  k_w   : Duvar malzemesinin ısı iletim katsayısı (W/(m·K))

NTU-Etkinlik yöntemi:
  NTU = U × A / C_min
  C_min = min(m_h × cp_h, m_c × cp_c)
  ε = f(NTU, C_r)   burada C_r = C_min / C_max

Karşı akış etkinliği:
  ε = [1 - exp(-NTU × (1 - C_r))] / [1 - C_r × exp(-NTU × (1 - C_r))]
  C_r = 1 ise: ε = NTU / (1 + NTU)
```

## Kirlenme (Fouling)

### TEMA Kirlenme Direnci Değerleri

| Akışkan | R_f (m²·K/W) | Not |
|---------|-------------|-----|
| Arıtılmış soğutma suyu (açık devre) | 0.000176 | T < 50°C |
| Arıtılmamış soğutma suyu | 0.000352 | T < 50°C |
| Buhar (temiz) | 0.000088 | Kondenser tarafı |
| Hafif hidrokarbon (sıvı) | 0.000176 | Benzin, nafta |
| Ağır hidrokarbon (sıvı) | 0.000352-0.000528 | Fuel oil, asfalt |
| Baca gazı | 0.000880-0.001760 | Kurum ve kül birikimi |
| Hava (temiz) | 0.000176 | Endüstriyel hava |
| Süt, gıda ürünleri | 0.000176-0.000352 | Düzenli CIP gerekli |

### Kirlenme ve Exergy İlişkisi

```
Kirlenmenin exergy etkisi:

  U_kirli = 1 / (1/U_temiz + R_f,i + R_f,o)

  ΔT_m,kirli > ΔT_m,temiz  (aynı Q için daha büyük sıcaklık farkı gerekir)

  Ex_yıkım,kirli > Ex_yıkım,temiz

Kirlenme nedeniyle ek exergy yıkımı:
  ΔEx_kirlenme = T₀ × Q × (1/T_m,kirli - 1/T_m,temiz)

Burada:
  T_m : Logaritmik ortalama sıcaklık (K)
```

## Eşanjör Performans İzleme

### Anahtar Performans Göstergeleri (KPI)

| KPI | Tanım | Hedef | Alarm Seviyesi |
|-----|-------|-------|----------------|
| Etkinlik (ε) | Gerçek ısı transferi / maksimum mümkün | >0.70 | <0.60 |
| Kirlenme faktörü (Cleanliness Factor — CF) | U_gerçek / U_tasarım | >0.80 | <0.70 |
| Basınç düşüşü oranı | ΔP_gerçek / ΔP_tasarım | <1.30 | >1.50 |
| Yaklaşma sıcaklığı (Approach) | T_sıcak,çıkış - T_soğuk,giriş | Tasarıma uygun | >150% tasarım değeri |
| Exergy verimi | η_ex = Ex_çıkış / Ex_giriş | >0.65 | <0.50 |

## Maliyet Tahmini (Bütçe Seviyesi)

| Eşanjör Tipi | Spesifik Maliyet (EUR/m²) | Montaj Faktörü | Not |
|-------------|--------------------------|----------------|-----|
| S&T (karbon çelik) | 200-600 | 2.5-3.5 | Basınç ve malzemeye bağlı |
| S&T (paslanmaz çelik) | 500-1,500 | 2.5-3.5 | Korozif servisler |
| GPHE (AISI 316) | 150-400 | 1.5-2.0 | En düşük alan başına maliyet |
| BPHE | 50-200 | 1.2-1.5 | Küçük kapasiteler |
| Hava soğutmalı | 300-1,000 | 2.0-3.0 | Fan ve yapı dahil |
| Spiral | 400-1,200 | 2.0-2.5 | Özel imalat |
| Ekonomizer | 100-400 | 2.0-3.0 | Kanatlı boru |
| Reküperatör (metalik) | 500-2,000 | 2.5-3.5 | Yüksek sıcaklık alaşımı |
| Reküperatör (seramik) | 1,000-5,000 | 3.0-4.0 | Çok yüksek sıcaklık |

## Dikkat Edilecekler

1. **Exergy optimizasyonu:** Eşanjör seçiminde sadece birinci yasa verimi (enerji) değil, ikinci yasa verimi (exergy) de dikkate alınmalıdır. Düşük sıcaklık farkı ile çalışan eşanjörler daha yüksek exergy verimine sahiptir.
2. **Pinch analizi entegrasyonu:** Fabrika düzeyinde eşanjör ağı tasarımında pinch analizi kullanılmalı, minimum yaklaşma sıcaklığı (ΔT_min) optimum olarak belirlenmelidir.
3. **Kirlenme yönetimi:** Kirlenme, exergy verimini doğrudan düşürür. Düzenli temizlik programı hem enerji hem exergy performansını korur.
4. **Basınç düşüşü dengesi:** Yüksek akış hızı = yüksek U değeri = küçük alan, ancak yüksek ΔP = yüksek pompa gücü. Optimum, toplam exergy yıkımını minimize eder.
5. **Malzeme seçimi:** Yüksek ısı iletkenlikli malzemeler (bakır, alüminyum) düşük duvar direnci sağlar ancak korozyon ve maliyet dikkate alınmalıdır.

## İlgili Dosyalar

- Gövde-boru eşanjör: `heat_exchanger/equipment/shell_and_tube.md`
- Plakalı eşanjör: `heat_exchanger/equipment/plate.md`
- Hava soğutmalı eşanjör: `heat_exchanger/equipment/air_cooled.md`
- Çift borulu eşanjör: `heat_exchanger/equipment/double_pipe.md`
- Spiral eşanjör: `heat_exchanger/equipment/spiral.md`
- Ekonomizer: `heat_exchanger/equipment/economizer.md`
- Hava ön ısıtıcı: `heat_exchanger/equipment/air_preheater.md`
- Reküperatör: `heat_exchanger/equipment/recuperator.md`
- Formüller: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Pinch analizi: `factory/pinch_analysis.md`
- Isı entegrasyonu: `factory/heat_integration.md`

## Referanslar

- Kakaç, S., Liu, H., Pramuanjaroenkij, A. (2020). *Heat Exchangers: Selection, Rating, and Thermal Design*, 4th Edition, CRC Press.
- Shah, R.K. & Sekulić, D.P. (2003). *Fundamentals of Heat Exchanger Design*, John Wiley & Sons.
- TEMA (Tubular Exchanger Manufacturers Association) (2019). *Standards of the Tubular Exchanger Manufacturers Association*, 10th Edition.
- Hewitt, G.F., Shires, G.L., Bott, T.R. (1994). *Process Heat Transfer*, CRC Press.
- Bejan, A. (2013). *Convection Heat Transfer*, 4th Edition, Wiley.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*, Krieger Publishing.
- Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*, Wiley.
- Linnhoff, B. et al. (1994). *A User Guide on Process Integration for the Efficient Use of Energy*, IChemE.
- HEDH — Heat Exchanger Design Handbook, Begell House.
- Perry, R.H. & Green, D.W. (2019). *Perry's Chemical Engineers' Handbook*, 9th Edition, McGraw-Hill.
