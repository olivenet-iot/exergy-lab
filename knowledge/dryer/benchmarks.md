---
title: "Kurutucu Benchmark Verileri"
category: reference
equipment_type: dryer
keywords: [benchmark, kurutucu, SMER, SEC, exergy verimi, enerji verimi, kurutma, endüstriyel kurutucu, egzoz sıcaklığı, egzoz nemi, BAT, BREF, exergy kayıp dağılımı, sektörel benchmark]
related_files: [dryer/formulas.md, dryer/psychrometrics.md, dryer/equipment/tunnel_dryer.md, dryer/equipment/belt_dryer.md, dryer/equipment/rotary_dryer.md, dryer/equipment/fluidized_bed.md, dryer/equipment/spray_dryer.md, dryer/equipment/drum_dryer.md, dryer/equipment/heat_pump_dryer.md, dryer/equipment/infrared_dryer.md, dryer/solutions/exhaust_heat_recovery.md, dryer/solutions/heat_pump_retrofit.md, dryer/solutions/air_recirculation.md, dryer/solutions/insulation.md, dryer/solutions/temperature_optimization.md, dryer/solutions/mechanical_dewatering.md, dryer/solutions/solar_preheating.md, factory/factory_benchmarks.md]
use_when: ["Kurutucu performansı değerlendirilirken", "SMER karşılaştırması yapılırken", "SEC hesaplanırken", "Kurutma verimliliği analiz edilirken", "Exergy kayıp dağılımı incelenirken", "Sektörel kıyaslama yapılırken", "BAT karşılaştırması yapılırken"]
priority: high
last_updated: 2026-02-01
---
# Kurutucu Benchmark Verileri

> Son güncelleme: 2026-02-01

## 1. Kurutucu Tipi Bazlı Benchmarklar (Dryer Type Benchmarks)

Aşağıdaki tablo, her kurutucu tipi için temel performans göstergelerini kapsamlı biçimde sunar. SMER (Specific Moisture Extraction Rate), SEC (Specific Energy Consumption), enerji verimi, exergy verimi, tipik egzoz sıcaklığı ve egzoz bağıl nemi dahildir.

### 1.1 Kapsamlı Kurutucu Tipi Karşılaştırma Tablosu

| Kurutucu Tipi | SMER Aralığı [kg/kWh] | SMER Best Practice [kg/kWh] | SEC Aralığı [kJ/kg su] | Enerji Verimi [%] | Exergy Verimi [%] | Tipik Egzoz Sıcaklığı [°C] | Tipik Egzoz Bağıl Nem [%] |
|---------------|------------------------|------------------------------|-------------------------|--------------------|--------------------|-----------------------------|-----------------------------|
| Tünel (tunnel) | 0.50–1.00 | 1.20 | 3,600–7,200 | 40–65 | 4–12 | 80–130 | 30–60 |
| Bant (belt/conveyor) | 0.80–1.20 | 1.50 | 3,000–4,500 | 45–70 | 6–14 | 70–110 | 40–70 |
| Döner tambur (rotary) | 0.60–1.00 | 1.30 | 3,600–6,000 | 40–65 | 5–13 | 80–140 | 25–55 |
| Akışkan yatak (fluidized bed) | 0.80–1.50 | 2.00 | 2,400–4,500 | 50–75 | 8–16 | 60–100 | 40–70 |
| Püskürtmeli (spray) | 0.30–0.80 | 1.00 | 4,500–12,000 | 30–55 | 3–10 | 80–110 | 20–45 |
| Silindirik tambur (drum) | 1.00–2.00 | 2.50 | 1,800–3,600 | 55–80 | 10–20 | 60–90 | 50–80 |
| Isı pompası (heat pump) | 2.00–4.00 | 5.00 | 900–1,800 | 60–85+ | 15–32 | 30–55 | 60–90 |
| Kızılötesi (infrared — IR) | 0.40–0.80 | 1.00 | 4,500–9,000 | 35–60 | 5–12 | 40–80* | 20–50 |
| Mikrodalga (microwave — MW) | 0.50–1.00 | 1.30 | 3,600–7,200 | 40–65 | 6–14 | 40–80* | 20–50 |
| Kızgın buhar (superheated steam — SSD) | 0.80–1.40 | 1.80 | 2,571–4,500 | 50–75 | 10–20 | 110–150** | N/A*** |

*IR ve MW kurutucularında egzoz, hava bazlı konvektif sisteme bağlıdır; radyan/dielektrik ısıtma doğrudan üründe gerçekleşir.
**Kızgın buhar kurutucularında egzoz, fazla buhar olarak çıkar ve yoğuşturularak ısısı geri kazanılabilir.
***SSD kurutucularında ortam havası yerine kızgın buhar kullanıldığından bağıl nem kavramı geçerli değildir; egzoz doymuş buhar veya fazla buhar olarak çıkar.

Teorik üst sınır (sadece latent ısı): SMER_max ≈ 1.55 kg/kWh (h_fg ≈ 2,257 kJ/kg su @ 100°C).
Isı pompası kurutucularında COP > 1 sayesinde SMER bu teorik sınırı aşabilir.

### 1.2 SEC Dönüşüm ve Referans Değerler

```
SEC [kJ/kg su] = 3,600 / SMER [kg/kWh]

Teorik minimum SEC (sadece latent ısı) = 2,257 kJ/kg su (@ 100°C)
Teorik minimum SEC (70°C'de) ≈ 2,334 kJ/kg su
Pratikte SEC her zaman teorik minimumun üzerindedir (sensible ısı, kayıplar, fan enerjisi dahil).
```

| SEC Aralığı [kJ/kg su] | Sınıflandırma | Açıklama |
|-------------------------|---------------|----------|
| < 2,700 | Mükemmel (Excellent) | Isı pompası veya ileri ısı geri kazanımlı sistem |
| 2,700–3,600 | İyi (Good) | Verimli konvektif/temas kurutucu, iyi izolasyon |
| 3,600–5,000 | Ortalama (Average) | Standart endüstriyel performans |
| 5,000–7,200 | Ortalamanın altı (Below Average) | İyileştirme potansiyeli yüksek |
| > 7,200 | Kötü (Poor) | Ciddi verimsizlik, acil müdahale gerekli |

## 2. Sektör Bazlı Benchmarklar (Industry-Specific Benchmarks)

### 2.1 Gıda Sektörü (Food Industry)

#### Süt ve Süt Ürünleri (Dairy)

| Ürün | Tipik Kurutucu | SMER [kg/kWh] | SEC [kJ/kg su] | Enerji Verimi [%] | Exergy Verimi [%] | Not |
|------|----------------|---------------|-----------------|--------------------|--------------------|-----|
| Süt tozu | Püskürtmeli (spray) | 0.40–0.70 | 5,140–9,000 | 35–50 | 4–9 | Giriş sıcaklığı 180–220°C, yüksek exergy yıkımı |
| Peynir altı suyu tozu | Püskürtmeli | 0.45–0.75 | 4,800–8,000 | 38–52 | 5–10 | Süt tozuna benzer profil |
| Kazein | Akışkan yatak / bant | 0.60–1.00 | 3,600–6,000 | 40–60 | 6–12 | Orta sıcaklıklarda kurutma |
| Yoğurt tozu | Püskürtmeli | 0.35–0.65 | 5,540–10,286 | 30–45 | 3–8 | Isıya duyarlı, düşük sıcaklık |

#### Meyve ve Sebzeler (Fruits & Vegetables)

| Ürün | Tipik Kurutucu | SMER [kg/kWh] | SEC [kJ/kg su] | Enerji Verimi [%] | Exergy Verimi [%] | Not |
|------|----------------|---------------|-----------------|--------------------|--------------------|-----|
| Dilim meyve | Bant / tünel | 0.60–1.00 | 3,600–6,000 | 40–60 | 6–12 | 50–80°C, kalite hassas |
| Domates püresi | Tambur (drum) | 0.80–1.50 | 2,400–4,500 | 50–70 | 8–15 | Temas kurutma, ince film |
| Soğan/sarımsak | Bant | 0.70–1.10 | 3,273–5,143 | 45–65 | 7–13 | Orta sıcaklıklarda |
| Liyofilize meyve | Freeze dryer | 0.10–0.25 | 14,400–36,000 | 10–20 | 2–5 | Çok düşük verim ama yüksek kalite |

#### Tahıl ve Hububat (Grains & Cereals)

| Ürün | Tipik Kurutucu | SMER [kg/kWh] | SEC [kJ/kg su] | Enerji Verimi [%] | Exergy Verimi [%] | Not |
|------|----------------|---------------|-----------------|--------------------|--------------------|-----|
| Buğday / mısır | Akışkan yatak / silo | 0.80–1.50 | 2,400–4,500 | 50–70 | 8–15 | Düşük nem farkı (%22 → %13) |
| Pirinç | Silo / bant | 0.90–1.40 | 2,571–4,000 | 55–70 | 9–15 | Düşük sıcaklıkta uzun kurutma |
| Makarna | Bant (çok bölgeli) | 0.70–1.10 | 3,273–5,143 | 45–65 | 7–13 | Kontrollü nem profili kritik |
| Malt | Akışkan yatak | 0.80–1.30 | 2,769–4,500 | 50–68 | 8–14 | Enzim aktivitesi korunmalı |

### 2.2 Kağıt ve Selüloz Sektörü (Paper & Pulp)

| Proses | Tipik Kurutucu | SMER [kg/kWh] | SEC [kJ/kg su] | Enerji Verimi [%] | Exergy Verimi [%] | Not |
|--------|----------------|---------------|-----------------|--------------------|--------------------|-----|
| Kağıt makinesi kurutma | Çok silindirli (multi-cylinder) | 1.00–1.80 | 2,000–3,600 | 55–75 | 10–18 | Buhar ısıtmalı silindirler |
| Karton kurutma | Silindir + sıcak hava | 0.90–1.50 | 2,400–4,000 | 50–70 | 9–16 | Kombine sistem |
| Selüloz (pulp) kurutma | Akışkan yatak / bant | 0.70–1.20 | 3,000–5,143 | 45–65 | 7–14 | Yüksek başlangıç nemi (%55–60) |
| Tissue kurutma | Yankee silindir + TAD hood | 1.20–2.00 | 1,800–3,000 | 60–78 | 12–20 | Yüksek enerji yoğunluklu |
| Kaplamalı kağıt kurutma | IR + sıcak hava | 0.50–0.90 | 4,000–7,200 | 35–55 | 5–11 | İnce tabaka, hızlı kurutma |

### 2.3 Tekstil Sektörü (Textile Industry)

| Proses | Tipik Kurutucu | SMER [kg/kWh] | SEC [kJ/kg su] | Enerji Verimi [%] | Exergy Verimi [%] | Not |
|--------|----------------|---------------|-----------------|--------------------|--------------------|-----|
| Kumaş kurutma (stenter/ram) | Sıcak hava tünel | 0.50–0.90 | 4,000–7,200 | 35–55 | 5–10 | 160–200°C giriş, yüksek exergy yıkımı |
| İplik kurutma | RF / sıcak hava | 0.40–0.80 | 4,500–9,000 | 30–50 | 4–9 | Hassas sıcaklık kontrolü gerekli |
| Baskı sonrası kurutma | IR / sıcak hava | 0.30–0.70 | 5,143–12,000 | 25–45 | 3–8 | Hızlı kurutma kritik |
| Halı kurutma | Bant / tünel | 0.60–1.00 | 3,600–6,000 | 40–60 | 6–12 | Kalın malzeme, uzun süre |
| Boyama sonrası kurutma | Stenter | 0.45–0.85 | 4,235–8,000 | 32–52 | 4–9 | Renk sabitleme sıcaklığı kritik |

### 2.4 Seramik ve Tuğla Sektörü (Ceramic & Brick)

| Proses | Tipik Kurutucu | SMER [kg/kWh] | SEC [kJ/kg su] | Enerji Verimi [%] | Exergy Verimi [%] | Not |
|--------|----------------|---------------|-----------------|--------------------|--------------------|-----|
| Tuğla / kiremit | Tünel | 0.50–0.90 | 4,000–7,200 | 40–55 | 6–11 | Çatlama riski, kontrollü kuruma |
| Seramik karo (fayans) | Döner / tünel | 0.60–1.00 | 3,600–6,000 | 45–60 | 7–13 | Fırın atık ısısı kullanılabilir |
| Porselen | Tünel (çok bölgeli) | 0.40–0.80 | 4,500–9,000 | 35–50 | 5–10 | Düşük hız, hassas profil |
| Refrakter malzeme | Tünel / oda | 0.50–0.80 | 4,500–7,200 | 35–50 | 6–10 | Çok uzun kurutma süreleri |
| Sıhhi tesisat (sanitaryware) | Tünel | 0.45–0.85 | 4,235–8,000 | 38–52 | 5–10 | Karmaşık geometri, homojen kurutma |

### 2.5 Ahşap ve Kereste Sektörü (Wood & Lumber)

| Proses | Tipik Kurutucu | SMER [kg/kWh] | SEC [kJ/kg su] | Enerji Verimi [%] | Exergy Verimi [%] | Not |
|--------|----------------|---------------|-----------------|--------------------|--------------------|-----|
| Kereste (konvansiyonel kiln) | Oda tipi (kiln) | 0.50–0.90 | 4,000–7,200 | 40–55 | 5–10 | Günler-haftalar süren kurutma |
| Kereste (vakum) | Vakum oda | 0.60–1.00 | 3,600–6,000 | 45–60 | 7–12 | Hızlı, düşük stres |
| Kereste (ısı pompası) | HP + oda | 1.50–3.50 | 1,029–2,400 | 65–80 | 15–28 | En verimli, düşük sıcaklık |
| Talaş / yonga kurutma | Döner tambur | 0.70–1.20 | 3,000–5,143 | 45–65 | 7–14 | Pelet/levha öncesi kurutma |
| MDF / yonga levha hattı | Döner tambur | 0.60–1.00 | 3,600–6,000 | 40–60 | 6–12 | Yüksek kapasite, sürekli |

### 2.6 Kimya ve İlaç Sektörü (Chemical & Pharmaceutical)

| Proses / Ürün | Tipik Kurutucu | SMER [kg/kWh] | SEC [kJ/kg su] | Enerji Verimi [%] | Exergy Verimi [%] | Not |
|---------------|----------------|---------------|-----------------|--------------------|--------------------|-----|
| Kimyasal toz (genel) | Akışkan yatak / püskürtmeli | 0.60–1.20 | 3,000–6,000 | 40–65 | 6–14 | Prosese bağlı geniş aralık |
| Pigment | Püskürtmeli / bant | 0.40–0.80 | 4,500–9,000 | 30–50 | 4–10 | Partikül boyutu kontrol kritik |
| Gübre (fertilizer) | Döner tambur / akışkan yatak | 0.70–1.30 | 2,769–5,143 | 45–68 | 7–14 | Yüksek kapasite, düşük hassasiyet |
| İlaç granül | Akışkan yatak | 0.60–1.00 | 3,600–6,000 | 40–60 | 6–12 | GMP gereksinimi, sıcaklık kontrolü |
| API (aktif farmasötik madde) | Vakum tray / freeze | 0.15–0.50 | 7,200–24,000 | 15–35 | 2–7 | Düşük sıcaklık, hassas malzeme |
| Polimer granül | Akışkan yatak | 0.70–1.20 | 3,000–5,143 | 45–65 | 7–13 | Düşük sıcaklıkta kurutma |
| Boya / kaplama | Bant / IR | 0.40–0.80 | 4,500–9,000 | 30–50 | 4–10 | İnce film kurutma |

## 3. Exergy Verimi Sınıflandırması (Exergy Efficiency Classification)

Kurutucularda exergy verimi genel olarak düşüktür (tipik %5–30). Bunun temel nedeni, yüksek sıcaklıktaki enerji kaynağının (yüksek exergy) düşük sıcaklıktaki buharlaştırma işlemine (düşük exergy) kullanılmasıdır. Sınıflandırma, kurutucu kategorisine göre farklı aralıklara sahiptir.

```
η_ex = Ėx_faydalı / Ėx_giriş
     = (Ėx_ürün_çıkış + Ėx_nem_çıkış - Ėx_ürün_giriş - Ėx_nem_giriş) / Ėx_enerji_kaynağı
```

Detaylı hesaplama: bkz. `dryer/formulas.md`

### 3.1 Konvektif Kurutucular (Convective Dryers)

Kapsamı: Tünel, bant, döner tambur, akışkan yatak, püskürtmeli kurutucular.

| Exergy Verimi [%] | Sınıf | Renk Kodu | Aksiyon |
|--------------------|-------|-----------|---------|
| < 5 | Kritik (Critical) | Kırmızı | Acil müdahale, sistem yenileme değerlendir |
| 5–10 | Düşük (Low) | Turuncu | Kapsamlı iyileştirme planı, ısı geri kazanımı ekle |
| 10–15 | Ortalama (Average) | Sarı | Isı geri kazanımı artır, kontrol optimizasyonu |
| 15–25 | İyi (Good) | Açık yeşil | Küçük optimizasyonlar, izolasyon iyileştirme |
| > 25 | Mükemmel (Excellent) | Koyu yeşil | Performansı koru, izlemeye devam |

### 3.2 Isı Pompası Kurutucular (Heat Pump Dryers)

Kapsamı: Kapalı devre ve açık devre ısı pompası kurutucular.

| Exergy Verimi [%] | Sınıf | Renk Kodu | Aksiyon |
|--------------------|-------|-----------|---------|
| < 15 | Kritik (Critical) | Kırmızı | COP düşük, soğutucu akışkan veya kompresör sorunu |
| 15–22 | Düşük (Low) | Turuncu | COP artışı için bakım, ayar optimizasyonu |
| 22–30 | Ortalama (Average) | Sarı | Standart performans, küçük iyileştirmeler |
| 30–38 | İyi (Good) | Açık yeşil | Verimli çalışma, ince ayar düzeyinde iyileştirme |
| > 38 | Mükemmel (Excellent) | Koyu yeşil | Best-in-class, performansı koru |

### 3.3 Kızılötesi ve Mikrodalga Kurutucular (IR & Microwave Dryers)

Kapsamı: Radyan (IR) ve dielektrik (MW, RF) ısıtmalı kurutucular.

| Exergy Verimi [%] | Sınıf | Renk Kodu | Aksiyon |
|--------------------|-------|-----------|---------|
| < 5 | Kritik (Critical) | Kırmızı | Isıtıcı verimliliği veya uygulama uygunluğu sorgula |
| 5–10 | Düşük (Low) | Turuncu | Reflektör/anten optimizasyonu, dalga boyutu eşleştirme |
| 10–18 | Ortalama (Average) | Sarı | Standart performans, hibrit sistem değerlendir |
| 18–25 | İyi (Good) | Açık yeşil | İyi eşleşme, verimli enerji transferi |
| > 25 | Mükemmel (Excellent) | Koyu yeşil | Optimum çalışma, performansı koru |

### 3.4 Temas Kurutucular (Contact/Conductive Dryers)

Kapsamı: Silindirik tambur (drum), vakum tray, plaka kurutucular.

| Exergy Verimi [%] | Sınıf | Renk Kodu | Aksiyon |
|--------------------|-------|-----------|---------|
| < 8 | Kritik (Critical) | Kırmızı | Isı transfer yüzeyi kontrolü, buhar kalitesi |
| 8–15 | Düşük (Low) | Turuncu | Kondensat tahliye sistemi, izolasyon kontrolü |
| 15–22 | Ortalama (Average) | Sarı | Standart performans, ince ayar |
| 22–30 | İyi (Good) | Açık yeşil | İyi çalışma, kondensat geri kazanımı optimize |
| > 30 | Mükemmel (Excellent) | Koyu yeşil | Best-in-class temas kurutucu |

### 3.5 Kızgın Buhar Kurutucular (Superheated Steam Dryers)

| Exergy Verimi [%] | Sınıf | Renk Kodu | Aksiyon |
|--------------------|-------|-----------|---------|
| < 10 | Kritik (Critical) | Kırmızı | Buhar kalitesi ve basıncı kontrol et |
| 10–15 | Düşük (Low) | Turuncu | Fazla buhar geri kazanımını artır |
| 15–22 | Ortalama (Average) | Sarı | Standart performans |
| 22–30 | İyi (Good) | Açık yeşil | Buhar geri kazanımı iyi çalışıyor |
| > 30 | Mükemmel (Excellent) | Koyu yeşil | Mükemmel buhar yönetimi |

## 4. SMER Sınıflandırması — Kurutucu Tipine Göre (SMER Classification by Dryer Type)

Her kurutucu tipi için SMER değerlendirme eşikleri farklıdır, çünkü her tipin termodinamik sınırları ve çalışma prensipleri farklıdır.

### 4.1 Konvektif Kurutucular — SMER Sınıflandırması

| Kurutucu Tipi | Kötü [kg/kWh] | Ort. Altı [kg/kWh] | Ortalama [kg/kWh] | İyi [kg/kWh] | Mükemmel [kg/kWh] |
|---------------|---------------|---------------------|--------------------|--------------|--------------------|
| Tünel (tunnel) | < 0.40 | 0.40–0.60 | 0.60–0.85 | 0.85–1.10 | > 1.10 |
| Bant (belt) | < 0.60 | 0.60–0.80 | 0.80–1.05 | 1.05–1.30 | > 1.30 |
| Döner tambur (rotary) | < 0.45 | 0.45–0.65 | 0.65–0.85 | 0.85–1.10 | > 1.10 |
| Akışkan yatak (fluidized bed) | < 0.60 | 0.60–0.90 | 0.90–1.20 | 1.20–1.60 | > 1.60 |
| Püskürtmeli (spray) | < 0.25 | 0.25–0.40 | 0.40–0.60 | 0.60–0.85 | > 0.85 |

### 4.2 Temas ve Özel Kurutucular — SMER Sınıflandırması

| Kurutucu Tipi | Kötü [kg/kWh] | Ort. Altı [kg/kWh] | Ortalama [kg/kWh] | İyi [kg/kWh] | Mükemmel [kg/kWh] |
|---------------|---------------|---------------------|--------------------|--------------|--------------------|
| Silindirik tambur (drum) | < 0.70 | 0.70–1.00 | 1.00–1.50 | 1.50–2.10 | > 2.10 |
| Isı pompası (heat pump) | < 1.50 | 1.50–2.20 | 2.20–3.20 | 3.20–4.50 | > 4.50 |
| Kızılötesi (IR) | < 0.30 | 0.30–0.45 | 0.45–0.65 | 0.65–0.85 | > 0.85 |
| Mikrodalga (MW) | < 0.35 | 0.35–0.55 | 0.55–0.80 | 0.80–1.10 | > 1.10 |
| Kızgın buhar (SSD) | < 0.60 | 0.60–0.85 | 0.85–1.15 | 1.15–1.50 | > 1.50 |

### 4.3 Genel SMER Sınıflandırma (Kurutucu Tipinden Bağımsız)

| SMER Aralığı [kg/kWh] | Sınıflandırma | Açıklama | Tipik Kurutucu Grubu |
|------------------------|---------------|----------|----------------------|
| > 2.00 | Mükemmel (Excellent) | Isı pompası veya ileri hibrit sistem | Isı pompası, hibrit HP+konvektif |
| 1.20–2.00 | İyi (Good) | İyi tasarım ve operasyon | Bant, akışkan yatak, tambur, SSD |
| 0.80–1.20 | Ortalama (Average) | Standart endüstriyel performans | Tünel, döner, MW |
| 0.50–0.80 | Ortalamanın altı (Below Average) | İyileştirme potansiyeli yüksek | Eski konvektif, IR |
| < 0.50 | Kötü (Poor) | Ciddi verimsizlik, acil müdahale | Bakımsız/hatalı tasarım, spray |

## 5. Enerji Verimi vs Exergy Verimi Karşılaştırma Tablosu (Energy vs Exergy Efficiency)

Enerji verimi (1. yasa) ve exergy verimi (2. yasa) arasındaki fark, kurutucularda özellikle belirgindir. Yüksek enerji verimine sahip bir kurutucu, düşük exergy verimine sahip olabilir. Bu fark, enerji kalitesinin (sıcaklık seviyesinin) hesaba katılıp katılmamasından kaynaklanır.

### 5.1 Kurutucu Tipine Göre Enerji vs Exergy Verimi

| Kurutucu Tipi | Tipik Enerji Verimi [%] | Tipik Exergy Verimi [%] | Oran (η_en / η_ex) | Fark Açıklaması |
|---------------|-------------------------|-------------------------|---------------------|-----------------|
| Tünel (tunnel) | 45–60 | 5–10 | 6–8× | Yüksek ΔT, büyük egzoz kaybı |
| Bant (belt) | 50–65 | 7–12 | 5–7× | Orta ΔT, düzgün hava dağılımı |
| Döner tambur (rotary) | 45–60 | 6–11 | 6–7× | Yüksek ΔT, karışma kayıpları |
| Akışkan yatak (fluidized bed) | 55–70 | 9–14 | 5–6× | İyi kütle transferi, yüksek fan enerjisi |
| Püskürtmeli (spray) | 35–50 | 4–8 | 7–9× | En yüksek ΔT, çok düşük exergy verimi |
| Silindirik tambur (drum) | 60–75 | 12–18 | 4–5× | Temas kurutma, düşük ΔT |
| Isı pompası (heat pump) | 70–85 | 18–30 | 3–4× | Düşük ΔT, yüksek COP, en iyi oran |
| Kızılötesi (IR) | 40–55 | 6–11 | 5–7× | Elektrik → ısı dönüşüm kaybı |
| Mikrodalga (MW) | 45–60 | 7–12 | 5–6× | Seçici ısıtma avantajı, dönüşüm kaybı |
| Kızgın buhar (SSD) | 55–72 | 12–18 | 4–5× | Buhar geri kazanımı avantajı |

### 5.2 Fark Nedenleri ve Yorumlama

**Neden exergy verimi her zaman enerji veriminden çok düşüktür?**

1. **Sıcaklık seviyesi uyumsuzluğu (temperature mismatch):** Enerji kaynağı sıcaklığı (yakma: 800–1,200°C, buhar: 150–250°C) ile kurutma sıcaklığı (60–150°C) arasında büyük fark vardır. Bu fark doğrudan exergy yıkımına neden olur.

2. **Egzoz kaybının exergy içeriği:** Egzoz havası düşük sıcaklıkta olsa bile, hala önemli exergy taşır. Enerji verimi hesabında bu kayıp abartılırken, exergy verimi hesabında gerçek termodinamik kayıp daha doğru yansıtılır.

3. **Kütle transferi tersinmezlikleri:** Nem difüzyonu ve buharlaşma inherent olarak tersinmez proseslerdir ve exergy üretir (yıkım).

4. **Mekanik enerji tüketimi:** Fan ve konveyör enerjisi saf exergy (iş) olmasına rağmen, düşük kaliteli ısıya dönüşür.

### 5.3 Pratik Kural

```
Konvektif kurutucularda: η_ex ≈ η_en × 0.12–0.20  (yaklaşık)
Temas kurutucularında:   η_ex ≈ η_en × 0.18–0.25  (yaklaşık)
Isı pompası kurutucuda:  η_ex ≈ η_en × 0.25–0.38  (yaklaşık)
```

## 6. Exergy Kayıp Dağılımı — Kurutucu Tipine Göre (Exergy Destruction Distribution)

Exergy kayıp (yıkım) dağılımı, iyileştirme önceliklerini belirlemede kritik öneme sahiptir. Aşağıdaki tablolar, her kurutucu tipi için ana exergy kayıp kalemlerini yüzde olarak gösterir.

### 6.1 Konvektif Kurutucu (Tünel/Bant/Döner Tambur) — Tipik Exergy Kayıp Dağılımı

| Exergy Kayıp Kalemi | Tipik Pay [%] | İyi Tasarım [%] | Açıklama |
|----------------------|---------------|------------------|----------|
| Egzoz havası kaybı (exhaust) | 25–40 | 15–25 | En büyük kayıp; sıcak ve nemli hava atmosfere atılır |
| Yanma/ısı üretim tersinmezliği (combustion) | 20–35 | 18–28 | Yakıtın yanma exergy kaybı (yüksek T → düşük T) |
| Isı transfer tersinmezliği (heat transfer ΔT) | 15–25 | 12–18 | Enerji kaynağı ile kurutma havası arasındaki ΔT |
| Yüzey radyasyon/konveksiyon kaybı (radiation) | 3–8 | 1–3 | Kurutucu yüzeyinden çevreye ısı kaybı |
| Mekanik enerji (fan + konveyör) (mechanical) | 5–12 | 4–8 | Saf exergy (iş) kaybı |
| Kütle transferi tersinmezliği | 5–10 | 5–8 | Nem difüzyonu ve buharlaştırma |
| Diğer (kaçak, kontrol kayıpları) | 2–5 | 1–3 | Hava sızıntısı, aşırı kurutma |

### 6.2 Püskürtmeli Kurutucu (Spray Dryer) — Tipik Exergy Kayıp Dağılımı

| Exergy Kayıp Kalemi | Tipik Pay [%] | İyi Tasarım [%] | Açıklama |
|----------------------|---------------|------------------|----------|
| Egzoz havası kaybı (exhaust) | 30–45 | 20–30 | Düşük egzoz nemi, yüksek sıcaklık |
| Yanma/ısı üretim tersinmezliği (combustion) | 25–35 | 20–28 | Çok yüksek giriş sıcaklığı (180–220°C) |
| Isı transfer tersinmezliği (heat transfer ΔT) | 10–20 | 8–15 | Büyük sıcaklık farkı |
| Yüzey radyasyon kaybı (radiation) | 3–8 | 2–4 | Büyük yüzey alanı |
| Mekanik enerji (fan + atomizör) (mechanical) | 8–15 | 6–10 | Atomizasyon enerjisi dahil |
| Kütle transferi tersinmezliği | 3–8 | 3–6 | Hızlı buharlaştırma |

### 6.3 Isı Pompası Kurutucu (Heat Pump Dryer) — Tipik Exergy Kayıp Dağılımı

| Exergy Kayıp Kalemi | Tipik Pay [%] | İyi Tasarım [%] | Açıklama |
|----------------------|---------------|------------------|----------|
| Kompresör tersinmezliği (compressor) | 25–40 | 20–30 | En büyük kayıp kalemi |
| Kondenser ısı transfer (heat transfer) | 10–20 | 8–15 | Kondenser ΔT |
| Evaporatör ısı transfer (heat transfer) | 10–18 | 8–14 | Evaporatör ΔT |
| Genleşme valfi tersinmezliği (expansion) | 8–15 | 6–12 | Kısma (throttling) kaybı |
| Egzoz kaybı (exhaust) | 5–12 | 3–8 | Kapalı devrede çok düşük |
| Mekanik enerji (fan + konveyör) | 5–10 | 4–8 | Fan enerjisi |
| Yüzey radyasyon kaybı (radiation) | 2–5 | 1–3 | Düşük sıcaklıklarda düşük kayıp |
| Kütle transferi tersinmezliği | 5–10 | 4–8 | Düşük sıcaklıkta daha yavaş |

### 6.4 Kızılötesi (IR) Kurutucu — Tipik Exergy Kayıp Dağılımı

| Exergy Kayıp Kalemi | Tipik Pay [%] | İyi Tasarım [%] | Açıklama |
|----------------------|---------------|------------------|----------|
| Elektrik → IR dönüşüm kaybı | 15–30 | 12–20 | Emitör verimliliğine bağlı |
| Absorpsiyon uyumsuzluğu (spectral mismatch) | 10–25 | 8–15 | Dalga boyu ile malzeme emilimi eşleşmesi |
| Egzoz/konveksiyon kaybı (exhaust) | 15–25 | 10–18 | Hibrit sistemlerde havaya aktarılan ısı |
| Yüzey radyasyon kaybı (radiation) | 5–12 | 3–8 | Isıtıcıdan çevreye yansıma |
| Mekanik enerji (fan) | 3–8 | 2–5 | Egzoz fanı |
| Kütle transferi tersinmezliği | 5–10 | 4–8 | Yüzey kurutma → iç difüzyon |

### 6.5 Kızgın Buhar Kurutucu (Superheated Steam Dryer) — Tipik Exergy Kayıp Dağılımı

| Exergy Kayıp Kalemi | Tipik Pay [%] | İyi Tasarım [%] | Açıklama |
|----------------------|---------------|------------------|----------|
| Isı üretim tersinmezliği (steam generation) | 20–30 | 15–22 | Kazan/ısı kaynağı exergy kaybı |
| Egzoz buharı kaybı (exhaust steam) | 10–20 | 5–12 | Fazla buhar yoğuşturularak geri kazanılabilir |
| Isı transfer tersinmezliği (heat transfer ΔT) | 15–25 | 12–18 | Kızgın buhar → malzeme ΔT |
| Yüzey radyasyon kaybı (radiation) | 5–10 | 2–5 | Yüksek sıcaklık yüzeyleri |
| Mekanik enerji (fan/blower) | 5–12 | 4–8 | Buhar sirkülasyonu |
| Kütle transferi tersinmezliği | 5–10 | 4–8 | Buharlaştırma ve difüzyon |

## 7. En İyi Mevcut Teknikler — BAT Değerleri (Best Available Techniques — EU BREF)

Avrupa Birliği BAT Referans Dokümanları (BREF) sektör bazında kurutma süreçleri için enerji verimliliği hedeflerini belirler.

### 7.1 Genel BAT Prensipleri — Kurutma Prosesleri

| BAT İlkesi | Açıklama | Referans |
|-------------|----------|----------|
| BAT 1: Mekanik ön nem alma | Termal kurutma öncesinde sıkma, santrifüj, filtreleme ile nem azaltma | EU BREF ENE |
| BAT 2: Egzoz ısı geri kazanımı | Egzoz havasından giriş havasına veya diğer proseslere ısı transferi | EU BREF ENE |
| BAT 3: Hava resirkülasyonu | Kısmi egzoz havasını geri devreye alma (nem kapasitesi izin verdiğince) | EU BREF ENE |
| BAT 4: İzolasyon optimizasyonu | Kurutucu yüzeylerinde yeterli termal izolasyon (yüzey T < 50°C) | EU BREF ENE |
| BAT 5: Otomatik nem kontrolü | Çıkış nem ölçümüne dayalı otomatik kurutma kontrolü | EU BREF ENE |
| BAT 6: Düşük sıcaklık kaynağı kullanımı | Mümkün olan en düşük sıcaklık kaynağı ile kurutma (exergy eşleştirme) | EU BREF ENE |
| BAT 7: Atık ısı entegrasyonu | Diğer proseslerden atık ısının kurutma için kullanılması | EU BREF ENE |

### 7.2 Sektörel BAT-AEL Değerleri (BAT Associated Emission/Energy Levels)

#### Gıda, İçecek ve Süt Endüstrisi (EU BREF FDM)

| Proses | BAT-AEL: SEC [kJ/kg su] | BAT-AEL: Enerji Verimi [%] | BAT Tekniği |
|--------|--------------------------|------------------------------|-------------|
| Süt tozu (spray) | 4,000–5,500 | 45–55 | Egzoz ısı geri kazanımı + hava ön ısıtma |
| Tahıl kurutma | 2,500–3,600 | 60–70 | Silo kurutma + düşük sıcaklık |
| Meyve/sebze | 3,000–5,000 | 45–60 | Bant kurutucu + ısı geri kazanımı |
| Şeker (pancar pülpü) | 2,800–3,800 | 55–70 | Döner tambur + buhar entegrasyonu |

#### Kağıt ve Selüloz Endüstrisi (EU BREF PP)

| Proses | BAT-AEL: SEC [kJ/kg su] | BAT-AEL: Enerji Verimi [%] | BAT Tekniği |
|--------|--------------------------|------------------------------|-------------|
| Kağıt makinesi kurutma | 2,000–3,000 | 65–78 | Yüksek verimli silindir, kapalı hood |
| Tissue kurutma (TAD) | 2,200–3,200 | 62–75 | TAD optimizasyonu + ısı geri kazanımı |
| Selüloz kurutma | 2,800–4,000 | 55–68 | Proses entegrasyonu |

#### Seramik Endüstrisi (EU BREF CER)

| Proses | BAT-AEL: SEC [kJ/kg su] | BAT-AEL: Enerji Verimi [%] | BAT Tekniği |
|--------|--------------------------|------------------------------|-------------|
| Tuğla kurutma | 3,200–5,000 | 45–60 | Fırın atık ısısı geri kazanımı |
| Seramik karo kurutma | 3,000–4,500 | 50–65 | Fırın egzoz → kurutucu entegrasyonu |
| Sanitaryware kurutma | 3,500–5,500 | 40–55 | Tünel kurutucu + ısı geri kazanımı |

#### Tekstil Endüstrisi (EU BREF TXT)

| Proses | BAT-AEL: SEC [kJ/kg su] | BAT-AEL: Enerji Verimi [%] | BAT Tekniği |
|--------|--------------------------|------------------------------|-------------|
| Stenter kurutma | 3,500–5,500 | 40–55 | Egzoz ısı geri kazanımı + insulation |
| İplik kurutma | 3,800–6,000 | 35–50 | RF kurutma + konvektif kombine |
| Halı kurutma | 3,200–5,000 | 45–60 | Mekanik ön sıkma + bant kurutucu |

### 7.3 BAT Uygulama Öncelikleri (Maliyet-Etkinliğe Göre)

| Öncelik | BAT Tekniği | Tipik Tasarruf [%] | Yatırım | Geri Dönüş |
|---------|-------------|---------------------|---------|------------|
| 1 | Mekanik ön nem alma (sıkma/pres) | 10–30 | €20,000–100,000 | 0.5–2 yıl |
| 2 | Egzoz havası resirkülasyonu | 10–25 | €10,000–50,000 | 1–2 yıl |
| 3 | İzolasyon iyileştirme | 2–8 | €5,000–20,000 | 0.5–1.5 yıl |
| 4 | Egzoz ısı geri kazanımı (ekonomizer) | 8–18 | €15,000–60,000 | 1–3 yıl |
| 5 | Gelişmiş kontrol sistemi (nem bazlı) | 5–15 | €10,000–40,000 | 1–3 yıl |
| 6 | Fan VSD (değişken hız sürücü) | 10–30 | €5,000–25,000 | 1–2 yıl |
| 7 | Sıcaklık kaynağı kaskadlama | 5–15 | €20,000–80,000 | 2–4 yıl |
| 8 | Isı pompası retrofit | 30–50 | €50,000–200,000 | 2–5 yıl |

## 8. Performans Sınıflandırması Tablosu (Performance Classification)

### 8.1 Genel Performans Matrisi (Tüm Kurutucu Tipleri)

| Gösterge | Birim | Kötü | Ort. Altı | Ortalama | İyi | Mükemmel | Ölçüm Yöntemi |
|----------|-------|------|-----------|----------|-----|----------|---------------|
| SMER | kg/kWh | < 0.50 | 0.50–0.80 | 0.80–1.20 | 1.20–2.00 | > 2.00 | Debi ölçümü + enerji sayacı |
| SEC | kJ/kg su | > 7,200 | 5,000–7,200 | 3,600–5,000 | 2,700–3,600 | < 2,700 | Enerji tüketimi / nem uzaklaştırma |
| Enerji verimi | % | < 35 | 35–45 | 45–60 | 60–75 | > 75 | 1. yasa enerji denetimi |
| Exergy verimi | % | < 5 | 5–8 | 8–15 | 15–25 | > 25 | 2. yasa exergy analizi |
| Egzoz sıcaklığı | °C | > 150 | 120–150 | 100–120 | 80–100 | < 80 | Termokupl / PT100 |
| Egzoz bağıl nem | % | < 25 | 25–40 | 40–55 | 55–70 | > 70 | Higrometre / kapasitif sensör |
| Isı geri kazanım oranı | % | 0 | < 15 | 15–30 | 30–45 | > 45 | Enerji ölçümü (giriş/çıkış) |
| Spesifik fan enerjisi | kW/(kg/h nem) | > 0.15 | 0.12–0.15 | 0.08–0.12 | 0.05–0.08 | < 0.05 | Güç ölçümü / nem debisi |
| Yüzey ısı kaybı | % toplam enerji | > 8 | 5–8 | 3–5 | 1–3 | < 1 | IR termografi |
| Kurutma homojenliği | ΔM (%) | > 3.0 | 2.0–3.0 | 1.5–2.0 | 0.5–1.5 | < 0.5 | Ürün nem ölçümü (çoklu nokta) |
| Çalışma süresi (uptime) | % | < 85 | 85–90 | 90–95 | 95–98 | > 98 | CMMS / üretim kaydı |

### 8.2 Isı Kaynağına Göre Performans Değerlendirmesi

| Enerji Kaynağı | Kaynak Sıcaklığı [°C] | Enerji Maliyeti [€/kWh] | Exergy Faktörü | CO₂ Yoğunluğu [kgCO₂/kWh] | Exergy Eşleşme Notu |
|----------------|------------------------|--------------------------|-----------------|-----------------------------|----------------------|
| Doğalgaz (direkt yanma) | 800–1,200 | 0.03–0.06 | ~1.04 | 0.20 | Kötü — aşırı yüksek sıcaklık |
| Doğalgaz (buhar üzerinden) | 150–250 | 0.04–0.08 | ~0.30–0.45 | 0.25–0.30 | Orta — daha iyi eşleşme |
| Fuel oil | 800–1,200 | 0.04–0.07 | ~1.06 | 0.27 | Kötü — doğalgaza benzer |
| Biyokütle (direkt) | 600–900 | 0.02–0.04 | ~1.05–1.15 | ~0.03* | Kötü — yüksek T, ama düşük karbon |
| Elektrik (rezistans) | — | 0.08–0.15 | 1.00 | 0.30–0.50** | Çok kötü — saf exergy israfı |
| Elektrik (ısı pompası) | — | 0.08–0.15 | 1.00 (COP ile) | 0.10–0.17** | İyi — COP sayesinde |
| Atık ısı (proses) | 80–400 | ~0 | Değişken | ~0 | En iyi — bedava exergy kaynağı |
| Güneş enerjisi (solar) | 60–200 | 0.01–0.03 | Değişken | ~0 | İyi — düşük sıcaklık eşleşmesi |

*Biyokütle sürdürülebilir kaynak ise karbon nötr kabul edilir.
**Şebeke karışımına ve ülkeye bağlıdır.

### 8.3 Egzoz Havası Durumu Sınıflandırması

| Durum | Egzoz Sıcaklığı [°C] | Egzoz Bağıl Nem [%] | Tahmini Kayıp [%] | Aksiyon |
|-------|-----------------------|----------------------|--------------------|---------|
| Best practice | < 80 | > 60 | < 15 | Isı geri kazanımı + resirkülasyon optimal |
| İyi | 80–100 | 50–60 | 15–25 | Isı geri kazanımı mevcut ve çalışıyor |
| Ortalama | 100–120 | 35–50 | 25–35 | Isı geri kazanımı eklenebilir |
| Kötü | 120–150 | 25–35 | 35–50 | Ciddi enerji kaybı, acil önlem |
| Kritik | > 150 | < 25 | > 50 | Büyük enerji israfı, sistem revizyonu |

Genel kural: Her 10°C egzoz sıcaklık düşüşü ≈ %2–3 enerji tasarrufu sağlar.
Genel kural: Her %10 egzoz bağıl nem artışı ≈ %3–5 enerji tasarrufu sağlar.

### 8.4 Yaşa Göre Verimlilik Degradasyonu (Age-Efficiency Model)

| Kurutucu Yaşı | İyi Bakım [% kayıp] | Ortalama Bakım [% kayıp] | Kötü Bakım [% kayıp] |
|---------------|----------------------|---------------------------|------------------------|
| 0–3 yıl | 0–1 | 0–2 | 0–3 |
| 3–5 yıl | 1–2 | 2–4 | 3–6 |
| 5–10 yıl | 2–4 | 4–8 | 6–12 |
| 10–15 yıl | 4–7 | 8–13 | 12–20 |
| 15–20 yıl | 7–10 | 13–18 | 20–28 |
| 20–30 yıl | 10–15 | 18–25 | 28–40 |
| > 30 yıl | 15–20 | 25–35 | 40–55 |

Yenileme kararı pratik kuralları:
- Yıllık enerji israfı maliyeti > yeni kurutucu maliyetinin %12'si ise değiştirmeyi değerlendir
- Bakım maliyeti > yenileme maliyetinin %35'i ise değiştirmeyi değerlendir
- Yaş > 20 yıl VE verim düşüşü > %15 ise yenileme değerlendirmesi yap
- Ürün kalitesi bozulması (düzensiz nem, renk değişimi) ise acil revizyon

### 8.5 Ekonomik Değerlendirme Referansları

| İyileştirme Önlemi | Tipik Enerji Tasarrufu [%] | Yatırım Maliyeti [€] | Geri Dönüş Süresi |
|---------------------|----------------------------|------------------------|---------------------|
| Egzoz havası resirkülasyonu | 10–25 | 10,000–50,000 | 1–2 yıl |
| Hava-hava ısı eşanjörü | 8–15 | 15,000–60,000 | 1–3 yıl |
| İzolasyon iyileştirme | 2–8 | 5,000–20,000 | 0.5–1.5 yıl |
| Fan VSD (değişken hız sürücü) | 10–30 | 5,000–25,000 | 1–2 yıl |
| Gelişmiş kontrol sistemi | 5–15 | 10,000–40,000 | 1–3 yıl |
| Isı pompası retrofit | 30–50 | 50,000–200,000 | 2–5 yıl |
| Mekanik ön nem alma (sıkma/pres) | 10–30 | 20,000–100,000 | 1–3 yıl |
| Hibrit kurutma (IR + konvektif) | 15–25 | 30,000–120,000 | 2–4 yıl |
| Kızgın buhar kurutma dönüşümü | 20–40 | 100,000–500,000 | 3–6 yıl |
| Solar ön ısıtma | 5–15 | 20,000–80,000 | 3–7 yıl |

Hızlı maliyet-fayda hesabı:
```
Tasarruf (€/yıl) = Q̇_kurutucu (kW) × Çalışma_saati (h/yıl) × Tasarruf_oranı (%) × Enerji_maliyeti (€/kWh)

Örnek: 500 kW kurutucu, 6,000 h/yıl, %15 tasarruf, €0.05/kWh
Tasarruf = 500 × 6,000 × 0.15 × 0.05 = €22,500/yıl
```

## İlgili Dosyalar

- `dryer/formulas.md` — Kurutucu exergy analizi hesaplama formülleri ve denklemleri
- `dryer/psychrometrics.md` — Psikrometrik hesaplamalar, nemli hava özellikleri
- `dryer/audit.md` — Kurutucu enerji denetimi prosedürleri ve kontrol listesi
- `dryer/case_studies.md` — Uygulama örnekleri ve vaka çalışmaları
- `dryer/equipment/tunnel_dryer.md` — Tünel kurutucu spesifik bilgileri
- `dryer/equipment/belt_dryer.md` — Bant kurutucu spesifik bilgileri
- `dryer/equipment/rotary_dryer.md` — Döner tambur kurutucu spesifik bilgileri
- `dryer/equipment/fluidized_bed.md` — Akışkan yatak kurutucu spesifik bilgileri
- `dryer/equipment/spray_dryer.md` — Püskürtmeli kurutucu spesifik bilgileri
- `dryer/equipment/drum_dryer.md` — Silindirik tambur kurutucu spesifik bilgileri
- `dryer/equipment/heat_pump_dryer.md` — Isı pompası kurutucu tasarım ve retrofit rehberi
- `dryer/equipment/infrared_dryer.md` — Kızılötesi kurutucu spesifik bilgileri
- `dryer/solutions/exhaust_heat_recovery.md` — Egzoz havası ısı geri kazanım çözümleri
- `dryer/solutions/heat_pump_retrofit.md` — Isı pompası retrofit uygulama rehberi
- `dryer/solutions/air_recirculation.md` — Hava resirkülasyon tasarımı ve optimizasyonu
- `dryer/solutions/insulation.md` — İzolasyon iyileştirme ve yüzey kaybı azaltma
- `dryer/solutions/temperature_optimization.md` — Sıcaklık profili optimizasyonu
- `dryer/solutions/mechanical_dewatering.md` — Mekanik ön nem alma çözümleri
- `dryer/solutions/solar_preheating.md` — Güneş enerjili ön ısıtma sistemleri
- `dryer/sectors/food_drying.md` — Gıda sektörü kurutma detayları
- `dryer/sectors/paper_drying.md` — Kağıt sektörü kurutma detayları
- `dryer/sectors/textile_drying.md` — Tekstil sektörü kurutma detayları
- `dryer/sectors/ceramic_drying.md` — Seramik sektörü kurutma detayları
- `dryer/sectors/wood_drying.md` — Ahşap/kereste sektörü kurutma detayları
- `factory/factory_benchmarks.md` — Fabrika seviyesi genel sektörel benchmarklar
- `factory/cross_equipment.md` — Ekipmanlar arası entegrasyon fırsatları (kurutucu atık ısı)

## Referanslar

- Mujumdar, A.S., "Handbook of Industrial Drying," 4th Edition, CRC Press, 2014
- Kemp, I.C., "Fundamentals of Energy Analysis of Dryers," in Modern Drying Technology, Vol. 4: Energy Savings, Wiley-VCH, 2012
- Kudra, T. & Mujumdar, A.S., "Advanced Drying Technologies," 2nd Edition, CRC Press, 2009
- Dincer, I. & Zamfirescu, C., "Drying Phenomena: Theory and Applications," Wiley, 2016
- EU BREF, "Reference Document on Best Available Techniques for Energy Efficiency," European Commission, 2009
- EU BREF, "Reference Document on BAT in the Food, Drink and Milk Industries (FDM)," European Commission, 2019
- EU BREF, "Reference Document on BAT in the Pulp and Paper Industry (PP)," European Commission, 2015
- EU BREF, "Reference Document on BAT in the Ceramic Manufacturing Industry (CER)," European Commission, 2007
- EU BREF, "Reference Document on BAT in the Textiles Industry (TXT)," European Commission, 2003
- US DOE/AMO, "Improving Process Heating System Performance: A Sourcebook for Industry," 2007
- US DOE, "Waste Heat Recovery: Technology and Opportunities in U.S. Industry," 2008
- Carbon Trust, "Industrial Energy Efficiency Accelerator — Guide to the Drying Sector," CTG058
- Carbon Trust, "Drying — A Guide to Energy-Efficient Drying Technologies," UK
- IEA (International Energy Agency), "Energy Technology Perspectives — Industrial Sector," 2023
- IEA IETS Annex 15/17, "Industrial Excess Heat Recovery"
- Strumillo, C. et al., "Energy Aspects in Drying," in Handbook of Industrial Drying, Chapter 42
- Bahu, R.E., "Energy Considerations in Dryer Design," Drying Technology Journal, 1991
- Chua, K.J. et al., "Heat Pump Drying: Recent Developments and Future Trends," Drying Technology, 2002
- Erbay, Z. & Icier, F., "A Review of Thin-Layer Drying of Foods: Theory, Modeling, and Experimental Results," Critical Reviews in Food Science and Nutrition, 2010
- Aghbashlo, M. et al., "A Review on Exergy Analysis of Drying Processes and Systems," Renewable and Sustainable Energy Reviews, 2013
- ASHRAE Handbook — HVAC Systems and Equipment (Drying and Dehumidification), 2020
- Turkish Energy Efficiency Law (No. 5627) and related regulations
- ETKB (T.C. Enerji ve Tabii Kaynaklar Bakanligi), Enerji Verimliligi Strateji Belgesi
