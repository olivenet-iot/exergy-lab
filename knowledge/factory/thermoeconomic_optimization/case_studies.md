---
title: "Vaka Çalışmaları (Case Studies)"
category: thermoeconomic_optimization
keywords: [vaka çalışmaları, çimento, CHP, gıda sektörü, tekstil, kimya, CBAM, endüstriyel uygulama]
related_files: [knowledge/factory/thermoeconomic_optimization/practical_guide.md, knowledge/factory/thermoeconomic_optimization/iterative_method.md, knowledge/factory/thermoeconomic_optimization/multi_objective.md]
use_when: ["Sektörel termoekonomik optimizasyon örnekleri arandığında", "Gerçek dünya uygulama sonuçları ve referans veriler gerektiğinde"]
priority: medium
last_updated: 2026-02-02
---

# Vaka Çalışmaları (Case Studies)

## 1. Genel Bakış

Bu bölüm, termoekonomik optimizasyonun hem akademik hem de endüstriyel ortamlarda nasıl
uygulandığını gösteren beş kapsamlı vaka çalışması sunmaktadır. Her vaka, farklı bir sektörü
ve farklı bir optimizasyon yaklaşımını temsil eder:

| # | Vaka | Sektör | Yaklaşım | Ölçek |
|---|------|--------|----------|-------|
| 1 | Çimento fabrikası | Çimento | Exergoekonomik iteratif | 45 MW termal |
| 2 | Doğalgaz CHP | Hizmet (hastane) | Çok amaçlı (NSGA-II) | 2 MWe |
| 3 | Gıda fabrikası | Süt ürünleri | İteratif / faz bazlı | 3 MW termal |
| 4 | Tekstil tesisi | Örme & boyahane | Faz bazlı optimizasyon | 3.5 MW termal |
| 5 | Kimya fabrikası | Gübre (CBAM etkili) | Çok amaçlı + karbon | 15 MW termal |

Vaka çalışmaları, termoekonomik analizin gerçek dünyada karar verme süreçlerini nasıl
yönlendirdiğini, hangi yatırımların önceliklendirildiğini ve elde edilen sonuçları
somut verilerle göstermektedir.

> **Not:** Akademik vakalar (1, 2) yayınlanmış çalışmalardan adapte edilmiştir.
> Endüstriyel vakalar (3, 4, 5) Türk sanayisinden gerçekçi senaryolara dayanmaktadır.

---

## 2. Akademik Vaka: Çimento Fabrikası Exergoekonomik Optimizasyonu

### 2.1. Sistem Tanımı

Çimento üretimi, yüksek sıcaklık süreçleri nedeniyle enerji yoğun sektörlerin başında gelir.
Bu vaka, entegre bir çimento tesisinin exergoekonomik analizini ve optimizasyonunu kapsar.

**Tesis Özellikleri:**

| Parametre | Değer |
|-----------|-------|
| Üretim kapasitesi | 1.2 milyon ton klinker/yıl |
| Toplam termal girdi | ~45 MW (doğalgaz + petcoke) |
| Elektrik tüketimi | ~8.5 MW |
| Çalışma saati | 7,800 h/yıl |
| Fırın tipi | 4 kademeli preheater + kalsiner + döner fırın |
| Soğutucu tipi | Izgaralı klinker soğutucu (grate cooler) |

**Ana Bileşenler:**

1. **Farin değirmeni** (raw mill): Hammadde öğütme, 4.2 MW elektrik
2. **Preheater kulesi** (preheater tower): 4 kademeli siklon, gaz-katı ısı değişimi
3. **Kalsiner** (calciner): CaCO₃ → CaO + CO₂ reaksiyonu, ~900°C
4. **Döner fırın** (rotary kiln): Klinkerleşme, ~1,450°C alev sıcaklığı ~2,000°C
5. **Klinker soğutucu** (clinker cooler): Hava ile soğutma, 1,400°C → 120°C
6. **Çimento değirmeni** (cement mill): Klinker + katkı öğütme, 3.8 MW elektrik

### 2.2. Exergoekonomik Analiz Sonuçları

Tüm bileşenler için SPECO (Specific Exergy Costing) yöntemi uygulanmıştır:

```
Maliyet dengesi: Ċ_P,k = Ċ_F,k + Ż_k

Exergoekonomik faktör: f_k = Ż_k / (Ż_k + Ċ_D,k)
Göreceli maliyet farkı: r_k = (c_P,k - c_F,k) / c_F,k
```

**Bileşen Bazında Sonuçlar:**

| Bileşen | Ėx_D [MW] | ε_k [%] | Ċ_D [€/h] | Ż_k [€/h] | Ċ_D + Ż_k [€/h] | f_k [%] | r_k [%] |
|---------|-----------|---------|-----------|-----------|------------------|---------|---------|
| Döner fırın | 12.8 | 41.2 | 38.4 | 4.2 | 42.6 | 9.9 | 185 |
| Kalsiner | 5.6 | 52.8 | 16.8 | 2.1 | 18.9 | 11.1 | 142 |
| Preheater kulesi | 3.2 | 68.5 | 9.6 | 3.8 | 13.4 | 28.4 | 78 |
| Klinker soğutucu | 4.1 | 55.3 | 12.3 | 1.5 | 13.8 | 10.9 | 120 |
| Farin değirmeni | 1.8 | 22.4 | 5.4 | 2.8 | 8.2 | 34.1 | 245 |
| Çimento değirmeni | 1.6 | 19.8 | 4.8 | 3.2 | 8.0 | 40.0 | 268 |
| **TOPLAM** | **29.1** | — | **87.3** | **17.6** | **104.9** | **16.8** | — |

**Temel Bulgular:**

- Döner fırın en yüksek Ċ_D değerine sahip (38.4 €/h) — toplam yıkım maliyetinin %44'ü
- Düşük f_k değerleri (fırın: %9.9), termodinamik iyileştirme potansiyelini gösterir
- Yüksek r_k değerleri (değirmenler: >%245), yüksek maliyet oluşum oranına işaret eder
- Toplam exergy yıkım maliyeti: ~87 €/h → yıllık ~680,000 €

### 2.3. Optimizasyon ve Sonuçlar

İteratif exergoekonomik optimizasyon (3 iterasyon) uygulanmıştır:

**İterasyon 1 — Döner Fırın Optimizasyonu:**
- Fazla hava oranı (excess air ratio): %15 → %8'e düşürülme
- Alev sıcaklık profili optimizasyonu
- Sonuç: Ėx_D fırın 12.8 → 11.2 MW, Ċ_D 38.4 → 33.6 €/h

**İterasyon 2 — Klinker Soğutucu + Atık Isı Geri Kazanımı:**
- Soğutucu egzoz gazından ORC (Organic Rankine Cycle) sistemi
- Soğutma havası debisi optimizasyonu
- Sonuç: 1.2 MWe elektrik üretimi, Ċ_D soğutucu 12.3 → 8.5 €/h

**İterasyon 3 — Preheater İyileştirmesi:**
- 4 → 5 kademe yükseltme (5th stage cyclone eklenmesi)
- Gaz sızdırmazlığı iyileştirme (air in-leakage azaltma)
- Sonuç: Ėx_D preheater 3.2 → 2.4 MW

**Genel Sonuçlar:**

| Parametre | Önce | Sonra | İyileşme |
|-----------|------|-------|----------|
| Toplam exergy verimi | %32.0 | %37.0 | +5 puan |
| Toplam Ċ_D + Ż | 104.9 €/h | 92.3 €/h | %12.0 azalma |
| Spesifik enerji tüketimi | 3,450 kJ/kg klinker | 3,100 kJ/kg klinker | %10.1 azalma |
| Yıllık maliyet tasarrufu | — | ~98,000 €/yıl | — |
| Yatırım maliyeti | — | 340,000 € | — |
| Basit geri ödeme (SPP) | — | 3.5 yıl | — |
| CO₂ azalma | — | 3,200 ton/yıl | — |

### 2.4. Kaçınılmaz ve Kaçınılabilir Exergy Yıkımı Ayrımı

Çimento fırınında gelişmiş exergy analizi (advanced exergetic analysis) uygulandığında:

```
Ėx_D,fırın = Ėx_D,UN + Ėx_D,AV = 10.0 + 2.8 MW

Ėx_D,UN (unavoidable): %78 — termodinamik sınırlardan kaynaklanır
Ėx_D,AV (avoidable): %22 — iyileştirilebilir kısım
```

Bu bulgu kritiktir: Fırın exergy yıkımı yüksek görünse de, yalnızca %22'si gerçekçi
şekilde azaltılabilir. Bu nedenle yatırım kararları kaçınılabilir kısma odaklanmalıdır.

### 2.5. Çıkarılan Dersler

1. Yüksek sıcaklık süreçlerinde kaçınılmaz exergy yıkımı baskındır — gerçekçi hedef belirleme şarttır
2. Atık ısı geri kazanımı (ORC, WHR) çimento sektöründe en yüksek getirili yatırımdır
3. Değirmenler düşük exergy verimli olsa da (<%25), iyileştirme potansiyeli sınırlıdır (mekanik süreç)
4. Fazla hava optimizasyonu düşük maliyetli ama etkili bir termodinamik iyileştirmedir

---

## 3. Akademik Vaka: Doğalgaz CHP Çok Amaçlı Optimizasyonu

### 3.1. Sistem Tanımı

Hastane yerleşkesi için tasarlanan kojenerasyon (CHP) sistemi, elektrik, ısıtma ve sıcak
su ihtiyacını karşılamaktadır.

**Sistem Özellikleri:**

| Parametre | Değer |
|-----------|-------|
| Gaz türbini kapasitesi | 2 MWe |
| Atık ısı kazanı (HRSG) | 3.2 MW termal |
| Yakıt türü | Doğalgaz (LHV = 47.1 MJ/kg) |
| Elektrik üretimi | 2.0 MWe |
| Isı üretimi (buhar + sıcak su) | 2.8 MW termal |
| Çalışma saati | 7,200 h/yıl |
| Kompresör basınç oranı | 12:1 |
| Türbin giriş sıcaklığı (TIT) | 1,150°C |

**Bileşenler:**
- Hava kompresörü (air compressor)
- Yanma odası (combustion chamber)
- Gaz türbini (gas turbine)
- Atık ısı kazanı / HRSG (heat recovery steam generator)
- Sıcak su ısı değiştiricisi (DHW heat exchanger)

### 3.2. Çok Amaçlı Formülasyon

İki çelişen amaç fonksiyonu tanımlanmıştır:

```
Amaç 1: min C_total = Σ(Ċ_F,k + Ż_k)  [€/h]
         → Toplam sahip olma maliyetini minimize et

Amaç 2: max η_ex = Ėx_P / Ėx_F  [%]
         → Toplam exergy verimini maximize et
         (eşdeğer: min (1 - η_ex))
```

**Karar Değişkenleri:**

| Değişken | Alt sınır | Üst sınır | Birim |
|----------|-----------|-----------|-------|
| Kompresör basınç oranı (r_p) | 8 | 18 | — |
| Türbin giriş sıcaklığı (TIT) | 1,050 | 1,250 | °C |
| Kompresör izentropik verim (η_is,comp) | 0.80 | 0.90 | — |
| Türbin izentropik verim (η_is,turb) | 0.82 | 0.92 | — |
| HRSG pinch sıcaklık farkı (ΔT_pinch) | 10 | 30 | °C |
| Sıcak su çıkış sıcaklığı (T_DHW) | 55 | 75 | °C |

**Kısıtlar:**
- NOx emisyonu ≤ 50 mg/Nm³ (Türk mevzuatı)
- Minimum elektrik üretimi ≥ 1.5 MWe (hastane kritik yük)
- Minimum ısıtma kapasitesi ≥ 2.0 MW termal (kış pik yükü)

**Optimizasyon Yöntemi:** NSGA-II algoritması
- Popülasyon: 100 birey
- Nesil sayısı: 150
- Çaprazlama oranı: 0.9
- Mutasyon oranı: 1/n (n = karar değişken sayısı)

### 3.3. Pareto Front Analizi

150 nesil sonunda elde edilen Pareto cephesinden seçilen temsili noktalar:

| Nokta | C_total [€/h] | η_ex [%] | r_p | TIT [°C] | η_is,comp | η_is,turb | ΔT_pinch [°C] |
|-------|---------------|----------|-----|----------|-----------|-----------|---------------|
| A (min maliyet) | 142.5 | 42.0 | 9.2 | 1,080 | 0.82 | 0.84 | 28 |
| B | 148.3 | 43.5 | 10.1 | 1,105 | 0.83 | 0.85 | 25 |
| C | 155.1 | 45.2 | 11.4 | 1,130 | 0.84 | 0.87 | 22 |
| D | 160.8 | 46.5 | 12.2 | 1,150 | 0.85 | 0.88 | 19 |
| E (TOPSIS) | 163.4 | 47.1 | 12.8 | 1,165 | 0.86 | 0.89 | 17 |
| F | 168.2 | 47.8 | 13.5 | 1,185 | 0.87 | 0.90 | 15 |
| G | 175.6 | 48.4 | 14.8 | 1,210 | 0.88 | 0.91 | 13 |
| H (max verim) | 185.2 | 48.8 | 16.5 | 1,240 | 0.90 | 0.92 | 10 |

**TOPSIS ile Karar Verme:**

Farklı ağırlık senaryoları ile TOPSIS uygulandığında:

| Senaryo | w_maliyet | w_verim | Seçilen Nokta | C_total [€/h] | η_ex [%] |
|---------|-----------|---------|---------------|---------------|----------|
| Maliyet odaklı | 0.7 | 0.3 | B | 148.3 | 43.5 |
| Dengeli | 0.5 | 0.5 | E | 163.4 | 47.1 |
| Verim odaklı | 0.3 | 0.7 | G | 175.6 | 48.4 |

**Temel Ticaret (Trade-off):**

A noktasından H noktasına geçişte:
- Maliyet artışı: 142.5 → 185.2 €/h (%30 artış)
- Verim artışı: 42.0% → 48.8% (+6.8 puan)
- Ancak E noktasından sonra marjinal verim kazanımı hızla düşer

```
A → E: +20.9 €/h maliyet → +5.1 puan verim (0.24 puan/€/h)
E → H: +21.8 €/h maliyet → +1.7 puan verim (0.08 puan/€/h)
```

Bu, azalan getiri (diminishing returns) etkisini açıkça gösterir.

### 3.4. Optimizasyon Sonuçları (Dengeli Senaryo — Nokta E)

| Parametre | Baz durum | Optimize | İyileşme |
|-----------|-----------|----------|----------|
| Exergy verimi | %42.0 | %47.1 | +5.1 puan |
| Toplam maliyet | 155.0 €/h | 163.4 €/h | %5.4 artış |
| Elektrik maliyeti | 0.068 €/kWh | 0.061 €/kWh | %10.3 azalma |
| Isı maliyeti | 0.032 €/kWh | 0.028 €/kWh | %12.5 azalma |
| CO₂ emisyonu | 4,850 ton/yıl | 4,000 ton/yıl | 850 ton/yıl azalma |
| Yatırım artışı | — | 120,000 € | — |
| NPV (15 yıl, %8) | — | 280,000 € | — |
| SPP | — | 4.2 yıl | — |

### 3.5. Çıkarılan Dersler

1. Pareto cephesi, verim-maliyet ticaret dengesini şeffaf biçimde ortaya koyar
2. Azalan getiri etkisi nedeniyle "diz noktası" (knee point) civarındaki çözümler tercih edilmeli
3. Ağırlık seçimi kurumsal önceliklere bağlıdır — hastane için enerji güvenliği verim ağırlığını artırır
4. TIT ve basınç oranı en hassas karar değişkenleridir

---

## 4. Endüstriyel Vaka: Türk Gıda Fabrikası

### 4.1. Fabrika Profili

Konya bölgesinde faaliyet gösteren süt ürünleri işleme tesisi, Türkiye'nin tipik
orta ölçekli gıda üretim tesislerinden biridir.

**Tesis Özellikleri:**

| Parametre | Değer |
|-----------|-------|
| Üretim | Süt ürünleri (peynir, yoğurt, tereyağı) |
| Konum | Konya organize sanayi bölgesi |
| Çalışma saati | 6,000 h/yıl |
| Yıllık enerji maliyeti | ~420,000 € |
| Doğalgaz tüketimi | ~1.8 milyon Nm³/yıl |
| Elektrik tüketimi | ~2.4 GWh/yıl |

**Ekipman Envanteri:**

| Ekipman | Kapasite | Adet | Toplam |
|---------|----------|------|--------|
| Buhar kazanı (steam boiler) | 1,500 kW | 2 | 3,000 kW |
| Soğutma grubu (refrigeration) | 250 kW soğutma | 2 | 500 kW |
| Basınçlı hava kompresörü | 22 kW | 2 | 45 kW (1 yedek) |
| Pompa grubu (process pumps) | 5-15 kW | 8 | 72 kW |
| Pastörizasyon sistemi | — | 1 | — |

### 4.2. Termoekonomik Analiz

**Fabrika Genel Exergy Dengesi:**

```
Ėx_F (toplam yakıt exergisi) = 3,150 kW
Ėx_P (toplam ürün exergisi) = 567 kW
Ėx_D (toplam exergy yıkımı) = 2,583 kW
η_ex,fabrika = 567 / 3,150 = %18.0
```

**Bileşen Bazında Termoekonomik Analiz:**

| Bileşen | Ėx_D [kW] | ε_k [%] | c_F [€/GJ] | c_P [€/GJ] | Ċ_D [€/h] | Ż_k [€/h] | f_k [%] | r_k [%] |
|---------|-----------|---------|-----------|-----------|-----------|-----------|---------|---------|
| Kazan 1 | 820 | 38.5 | 8.2 | 22.4 | 24.2 | 3.1 | 11.4 | 173 |
| Kazan 2 | 790 | 39.2 | 8.2 | 21.8 | 23.3 | 2.9 | 11.1 | 166 |
| Soğutma grubu | 480 | 28.6 | 18.5 | 68.2 | 32.0 | 4.8 | 13.0 | 269 |
| Kompresör | 28 | 12.4 | 18.5 | 152.0 | 1.9 | 0.6 | 24.0 | 722 |
| Pompa grubu | 35 | 48.5 | 18.5 | 40.2 | 2.3 | 1.2 | 34.3 | 117 |
| Pastörizasyon | 180 | 25.3 | 15.4 | 64.5 | 10.0 | 1.8 | 15.3 | 319 |
| Dağıtım kayıpları | 250 | — | — | — | 7.4 | — | — | — |
| **TOPLAM** | **2,583** | **18.0** | — | — | **101.1** | **14.4** | **12.5** | — |

**En Yüksek Maliyet Kaynaklı 3 Bileşen:**
1. Soğutma grubu: Ċ_D + Ż = 36.8 €/h (%31.9 pay)
2. Kazan 1: Ċ_D + Ż = 27.3 €/h (%23.6 pay)
3. Kazan 2: Ċ_D + Ż = 26.2 €/h (%22.7 pay)

### 4.3. Uygulanan İyileştirmeler

Üç fazlı optimizasyon programı uygulanmıştır:

**Faz 1: Kazan Yanma Optimizasyonu + Ekonomizer (Ay 1-3)**

| Uygulama | Detay | Yatırım |
|----------|-------|---------|
| O₂ trim kontrolü | Fazla hava %18 → %10 | 3,500 € |
| Ekonomizer | Baca gazı 220°C → 145°C, besleme suyu ön ısıtma | 7,500 € |
| Kondenstop bakımı | 4 adet arızalı kondenstop değişimi | 1,000 € |
| **Faz 1 Toplam** | | **12,000 €** |

Beklenen tasarruf: Doğalgaz %8 azalma → ~28,800 €/yıl

**Faz 2: Soğutma Sistemi Isı Geri Kazanımı (Ay 4-6)**

| Uygulama | Detay | Yatırım |
|----------|-------|---------|
| Kondenser ısı geri kazanımı | Kondenser atık ısısı → sıcak su (55°C) | 12,000 € |
| Evaporatör temizliği | COP 2.8 → 3.2 iyileşme | 1,500 € |
| Fan VSD uygulaması | Kule fanlarına değişken hız sürücü | 4,500 € |
| **Faz 2 Toplam** | | **18,000 €** |

Beklenen tasarruf: Elektrik %12 + doğalgaz %5 → ~33,600 €/yıl

**Faz 3: Basınçlı Hava Optimizasyonu + VSD (Ay 7-9)**

| Uygulama | Detay | Yatırım |
|----------|-------|---------|
| Kaçak giderme | Ultrasonik tespit, 12 nokta onarım | 2,000 € |
| Basınç düşürme | 7.5 bar → 6.5 bar (yeterli) | 500 € |
| VSD kompresör | Mevcut sabit hızlı → VSD kompresör | 5,500 € |
| **Faz 3 Toplam** | | **8,000 €** |

Beklenen tasarruf: Basınçlı hava elektriği %35 → ~13,200 €/yıl

**Toplam Program:**

| Parametre | Değer |
|-----------|-------|
| Toplam yatırım | 38,000 € |
| Toplam beklenen tasarruf | 75,600 €/yıl |
| Basit geri ödeme (SPP) | 0.50 yıl (6 ay) |
| Hesaplanan SPP (proje öncesi) | 2.3 yıl |

### 4.4. Sonuçlar

Proje tamamlandıktan 12 ay sonra ölçülen gerçek sonuçlar:

| Parametre | Hedef | Gerçekleşen | Sapma |
|-----------|-------|-------------|-------|
| Yıllık tasarruf | 75,600 €/yıl | 82,400 €/yıl | +%9 (enerji fiyat artışı etkisi) |
| Maliyet azalma oranı | %18.0 | %19.6 | +1.6 puan |
| Exergy verimi | %24.0 | %24.3 | +0.3 puan |
| CO₂ azalma | 280 ton/yıl | 295 ton/yıl | +%5.4 |
| Gerçek SPP | 2.3 yıl | 0.46 yıl (5.5 ay) | 6 ay önce geri ödeme |

> **Not:** SPP'nin beklentiden çok daha kısa gerçekleşmesinin ana nedeni, proje süresince
> doğalgaz fiyatlarının %22 artması ve tasarrufun parasal değerinin yükselmesidir. Bu durum,
> enerji fiyat volatilitesinin termoekonomik yatırımların değerini artırdığını gösterir.

### 4.5. Çıkarılan Dersler

1. Gıda sektörü düşük exergy verimine sahiptir (%15-25) — iyileştirme potansiyeli yüksektir
2. Soğutma-ısıtma entegrasyonu (kondenser ısısı → sıcak su) gıda sektöründe anahtar fırsattır
3. Kazan ekonomizeri hemen her tesiste uygulanabilir, düşük riskli yatırımdır
4. Basınçlı hava optimizasyonu düşük maliyetli ancak yüksek getirili bir "hızlı kazanım"dır
5. Enerji fiyat oynaklığı, verimlilik yatırımlarının gerçek geri dönüşünü tahminlerden daha iyi yapabilir

---

## 5. Endüstriyel Vaka: Türk Tekstil Tesisi

### 5.1. Tesis Profili

Denizli bölgesinde faaliyet gösteren örme ve boyahane tesisi, yoğun ısı ve buhar
tüketen tipik bir tekstil işletmesidir.

**Tesis Özellikleri:**

| Parametre | Değer |
|-----------|-------|
| Üretim | Örme kumaş boyama, apre, kurutma |
| Konum | Denizli organize sanayi bölgesi |
| Çalışma saati | 5,500 h/yıl |
| Yıllık enerji maliyeti | ~550,000 € |
| Doğalgaz tüketimi | ~2.5 milyon Nm³/yıl |
| Elektrik tüketimi | ~1.8 GWh/yıl |

**Ekipman Envanteri:**

| Ekipman | Kapasite | Detay |
|---------|----------|-------|
| Buhar kazanı (steam boiler) | 3,000 kW | 10 bar buhar, doğalgaz yakıtlı |
| Kompresör (air compressor) | 100 kW | 2×55 kW vidalı, 7.5 bar |
| Chiller (process cooling) | 400 kW soğutma | Su soğutmalı, boyahane için |
| Stenter (hot air dryer) | 850 kW termal | Direkt doğalgaz yakımlı, 180°C |
| Boyama makineleri | — | 6 adet jet boyama, buhar ısıtmalı |
| Kondenstop + dağıtım | — | 120 m buhar hattı |

### 5.2. Termoekonomik Analiz

**Fabrika Exergy Dengesi:**

```
Ėx_F = 3,850 kW
Ėx_P = 847 kW
Ėx_D = 3,003 kW
η_ex,fabrika = %22.0
```

**Bileşen Bazında Analiz:**

| Bileşen | Ėx_D [kW] | ε_k [%] | Ċ_D [€/h] | Ż_k [€/h] | Ċ_D + Ż_k [€/h] | f_k [%] | r_k [%] |
|---------|-----------|---------|-----------|-----------|------------------|---------|---------|
| Buhar kazanı | 1,080 | 36.0 | 31.9 | 4.5 | 36.4 | 12.4 | 178 |
| Stenter (kurutma) | 520 | 25.8 | 15.4 | 2.8 | 18.2 | 15.4 | 287 |
| Boyama makineleri | 380 | 32.5 | 11.2 | 3.2 | 14.4 | 22.2 | 208 |
| Kompresör | 62 | 14.5 | 4.1 | 1.5 | 5.6 | 26.8 | 590 |
| Chiller | 185 | 30.2 | 12.3 | 2.8 | 15.1 | 18.5 | 231 |
| Dağıtım kayıpları | 776 | — | 22.9 | — | 22.9 | — | — |
| **TOPLAM** | **3,003** | **22.0** | **97.8** | **14.8** | **112.6** | **13.1** | — |

**Kritik Bulgular:**
- Stenter (kurutma fırını), kazandan sonra en büyük 2. exergy yıkım kaynağı
- Dağıtım kayıpları (%25.8) çok yüksek — buhar hattı izolasyonu ve kondenstop arızaları
- Kompresörün r_k değeri (%590) çok yüksek — basınçlı havanın exergy maliyeti fahiş

### 5.3. Optimizasyon Programı

**Faz 1 — Hızlı Kazanımlar (Quick Wins) — Ay 1-2:**

| Uygulama | Tasarruf | Yatırım |
|----------|----------|---------|
| Basınçlı hava kaçak giderme (18 nokta) | 4,200 €/yıl | 1,200 € |
| Buhar hattı izolasyon yenileme (35 m) | 5,800 €/yıl | 2,200 € |
| Kondenstop bakımı (6 adet arızalı) | 3,500 €/yıl | 800 € |
| Kompresör basınç ayarı (7.5 → 6.5 bar) | 1,500 €/yıl | 300 € |
| **Faz 1 Toplam** | **15,000 €/yıl** | **4,500 €** |

SPP Faz 1: 0.3 yıl (3.6 ay)

**Faz 2 — Orta Ölçek Yatırımlar — Ay 3-8:**

| Uygulama | Tasarruf | Yatırım |
|----------|----------|---------|
| Kazan ekonomizeri | 18,000 €/yıl | 8,500 € |
| Stenter egzoz ısı geri kazanımı (exhaust heat recovery) | 22,000 €/yıl | 28,000 € |
| Kompresör VSD retrofit | 6,500 €/yıl | 9,500 € |
| Chiller kondenser ısı geri kazanımı | 5,500 €/yıl | 9,000 € |
| **Faz 2 Toplam** | **52,000 €/yıl** | **55,000 €** |

SPP Faz 2: 1.06 yıl

**Faz 3 — İleri Entegrasyon — Ay 9-14:**

| Uygulama | Tasarruf | Yatırım |
|----------|----------|---------|
| Kondensat geri dönüş optimizasyonu (%65 → %90) | 12,000 €/yıl | 15,000 € |
| Boyama makinesi atık su ısı geri kazanımı | 6,000 €/yıl | 10,000 € |
| **Faz 3 Toplam** | **18,000 €/yıl** | **25,000 €** |

SPP Faz 3: 1.39 yıl

### 5.4. Sonuçlar

**Genel Program Sonuçları:**

| Parametre | Önce | Sonra | İyileşme |
|-----------|------|-------|----------|
| Yıllık enerji maliyeti | 550,000 €/yıl | 465,000 €/yıl | %15.5 azalma |
| Yıllık tasarruf | — | 85,000 €/yıl | — |
| Toplam yatırım | — | 85,000 € | — |
| Basit geri ödeme (SPP) | — | 1.0 yıl | — |
| NPV (15 yıl, %8 iskonto) | — | 350,000 € | — |
| IRR | — | %98 | — |
| Exergy verimi | %22.0 | %31.0 | +9 puan |
| CO₂ emisyonu | 5,100 ton/yıl | 4,680 ton/yıl | 420 ton/yıl azalma |
| Doğalgaz tüketimi | 2.5 M Nm³/yıl | 2.1 M Nm³/yıl | %16 azalma |

### 5.5. Çıkarılan Dersler

1. Tekstilde stenter/kurutma fırını genellikle göz ardı edilir, ancak önemli bir exergy yıkım kaynağıdır
2. Stenter egzoz gazı ısı geri kazanımı (180°C → taze hava ön ısıtma) yüksek getirili yatırımdır
3. Kondensat geri dönüşü her zaman bir "hızlı kazanım" olarak değerlendirilmelidir
4. Ekipmanlar arası ısı entegrasyonu (cross-equipment heat integration) en iyi sonuçları verir
5. Dağıtım kayıplarının toplam exergy yıkımındaki payı (%25+) sıklıkla küçümsenmektedir

---

## 6. Endüstriyel Vaka: Kimya Fabrikası — CBAM Etkili Optimizasyon

### 6.1. Tesis Profili

AB'ye gübre ihraç eden bu kimya tesisi, Sınırda Karbon Düzenleme Mekanizması'nın
(CBAM — Carbon Border Adjustment Mechanism) doğrudan etkisi altındadır.

**Tesis Özellikleri:**

| Parametre | Değer |
|-----------|-------|
| Üretim | Amonyum nitrat gübre |
| Konum | İskenderun, Hatay |
| Çalışma saati | 8,000 h/yıl |
| Yıllık enerji maliyeti | ~1,800,000 € |
| Doğalgaz tüketimi | ~8.5 milyon Nm³/yıl |
| Elektrik tüketimi | ~12 GWh/yıl |
| CO₂ emisyonu | ~12,000 ton/yıl |
| AB ihracat payı | %45 (CBAM kapsamında) |

**Ana Prosesler:**
- Amonyak sentezi (Haber-Bosch): yüksek basınç (150-250 bar), yüksek sıcaklık (400-500°C)
- Nitrik asit üretimi: ekzotermik oksidasyon reaksiyonu
- Nötralizasyon: amonyum nitrat çözeltisi oluşumu
- Granülasyon ve kurutma: son ürün şekillendirme

### 6.2. CBAM Etkisi Analizi

AB'nin CBAM düzenlemesi, ihraç edilen ürünlerin gömülü karbon emisyonlarına maliyet
yüklemektedir. Bu tesis için CBAM etki analizi:

**Senaryo Bazlı CBAM Maliyet Projeksiyonu:**

| Senaryo | Karbon fiyatı [€/tCO₂] | İhracata konu emisyon [ton/yıl] | CBAM maliyeti [€/yıl] |
|---------|------------------------|--------------------------------|----------------------|
| Düşük (2026) | 50 | 5,400 | 270,000 |
| Orta (2028) | 80 | 5,400 | 432,000 |
| Yüksek (2030) | 100 | 5,400 | 540,000 |
| Çok yüksek (2032+) | 120 | 5,400 | 648,000 |

> **Not:** İhracata konu emisyon = Toplam emisyon × AB ihracat payı = 12,000 × 0.45 = 5,400 ton/yıl.

**CBAM dahil toplam enerji maliyeti:**

```
C_total = C_enerji + C_CBAM

Mevcut durum (CBAM yok):    1,800,000 €/yıl
Orta senaryo (80 €/tCO₂):   1,800,000 + 432,000 = 2,232,000 €/yıl (%24 artış)
Yüksek senaryo (100 €/tCO₂): 1,800,000 + 540,000 = 2,340,000 €/yıl (%30 artış)
```

### 6.3. Çok Amaçlı Optimizasyon

**Formülasyon:**

```
Amaç 1: min C_total = C_enerji + C_yatırım + C_CBAM  [€/yıl]
Amaç 2: min E_CO₂  [ton/yıl]

Karar değişkenleri:
- Reaktör atık ısı geri kazanım oranı [%40-%95]
- CHP sistemi kapasitesi [0-5 MWe]
- Proses entegrasyon seviyesi [düşük/orta/yüksek]
- Buhar basınç optimizasyonu [8-16 bar]
- Ekonomizer ve ön ısıtıcı boyutlandırma
```

**Optimizasyon Sonuçları — CBAM'sız vs CBAM'lı Optimal Noktalar:**

| Parametre | CBAM'sız Optimal | CBAM'lı Optimal (80 €/t) | Fark |
|-----------|-----------------|--------------------------|------|
| Exergy verimi (η_ex) | %38 | %44 | +6 puan |
| CO₂ emisyonu | 10,200 ton/yıl | 8,400 ton/yıl | -1,800 ton/yıl |
| Enerji maliyeti | 1,620,000 €/yıl | 1,420,000 €/yıl | -200,000 € |
| CBAM maliyeti | — | 302,400 €/yıl | — |
| Toplam maliyet | 1,620,000 €/yıl | 1,722,400 €/yıl | +102,400 € |
| Gerekli yatırım | 180,000 € | 650,000 € | +470,000 € |

**CBAM'lı Senaryoda Yatırım Dağılımı:**

| Yatırım | Maliyet [€] | Yıllık tasarruf [€/yıl] | Etki |
|---------|-------------|------------------------|------|
| Reaktör atık ısı geri kazanımı (WHR) | 280,000 | 165,000 (enerji) + 85,000 (CBAM) | Ana yatırım |
| CHP sistemi (2.5 MWe gaz motoru) | 220,000 | 140,000 (enerji) + 95,000 (CBAM) | Elektrik + ısı |
| Proses entegrasyonu (pinch analizi) | 95,000 | 75,000 (enerji) + 68,000 (CBAM) | Isı ağı optimizasyonu |
| Buhar sistemi optimizasyonu | 55,000 | 42,000 (enerji) + 22,000 (CBAM) | Basınç + kondensat |
| **TOPLAM** | **650,000 €** | **380,000 + 250,000 = 630,000 €/yıl** | — |

**Ekonomik Değerlendirme (CBAM 80 €/t senaryosu):**

| Parametre | CBAM'sız | CBAM'lı |
|-----------|----------|---------|
| Toplam yatırım | 180,000 € | 650,000 € |
| Yıllık tasarruf | 180,000 €/yıl | 630,000 €/yıl |
| SPP | 1.0 yıl | 1.03 yıl |
| NPV (15 yıl, %10) | 1,100,000 € | 2,100,000 € |
| IRR | %95 | %96 |

### 6.4. Çıkarılan Dersler

1. CBAM, optimal işletme noktasını dramatik biçimde değiştirir — daha verimli çözümler ekonomik olur
2. AB ihracat maruziyeti olan endüstriler karbon maliyetini derhal faktörlemelidir
3. Proses entegrasyonu ve CHP, CBAM altında çok daha cazip hale gelir
4. CBAM tasarrufu (kaçınılan karbon maliyeti), enerji tasarrufuyla neredeyse eşit büyüklüktedir
5. Reaktör atık ısı geri kazanımı, kimya sektöründe en yüksek getirili yatırımdır
6. Erken yatırım yapan tesisler, CBAM geçiş döneminde rekabet avantajı kazanır

---

## 7. Karşılaştırma Tablosu

Beş vakanın temel performans göstergelerinin karşılaştırması:

| Kriter | Çimento | CHP | Gıda | Tekstil | Kimya |
|--------|---------|-----|------|---------|-------|
| **Sektör** | Çimento | Hizmet (hastane) | Gıda (süt) | Tekstil (boyahane) | Kimya (gübre) |
| **Ölçek** | 45 MW | 2 MWe | 3 MW | 3.5 MW | 15 MW |
| **Yöntem** | İteratif exergoekonomik | Çok amaçlı (NSGA-II) | İteratif / faz bazlı | Faz bazlı | Çok amaçlı + CBAM |
| **η_ex önce → sonra** | 32% → 37% | 42% → 47% | 18% → 24% | 22% → 31% | 35% → 44% |
| **Maliyet azalma** | %12 | %15 (birim maliyet) | %18 | %15.5 | %21 (CBAM dahil) |
| **SPP [yıl]** | 3.5 | 4.2 | 2.3 (gerçek: 0.46) | 1.0 | 1.03 (CBAM dahil) |
| **NPV** | N/A | 280,000 € | 450,000 € | 350,000 € | 2,100,000 € |
| **Yatırım** | 340,000 € | 120,000 € | 38,000 € | 85,000 € | 650,000 € |
| **CO₂ azalma [ton/yıl]** | 3,200 | 850 | 280 | 420 | 2,800 |
| **Anahtar bulgu** | %78 kaçınılmaz yıkım | Azalan getiri etkisi | Soğutma-ısıtma entegrasyonu | Stenter ısı geri kazanımı | CBAM optimal noktayı değiştirir |

---

## 8. Genel Çıkarılan Dersler

Beş vaka çalışmasından çıkarılan ortak ve sektörler arası dersler:

1. **Veri kalitesi belirleyicidir:** Termoekonomik analizin güvenilirliği, ölçüm verilerinin
   doğruluğuna bağlıdır. Yanlış debi veya sıcaklık ölçümü, yanlış yatırım kararına yol açar.

2. **Kaçınılmaz vs kaçınılabilir yıkım ayrımı kritiktir:** Özellikle yüksek sıcaklık
   süreçlerinde (çimento fırını, kimya reaktörü) toplam exergy yıkımının büyük kısmı
   termodinamik olarak kaçınılmazdır. Gerçekçi hedefler kaçınılabilir kısma odaklanmalıdır.

3. **Ekipmanlar arası entegrasyon en yüksek değeri üretir:** Her sektörde, tek ekipman
   optimizasyonundan çok daha fazla tasarruf, ekipmanlar arası ısı entegrasyonuyla sağlanmıştır
   (soğutma → ısıtma, egzoz → ön ısıtma, kondensat geri dönüşü).

4. **CBAM oyun değiştiricidir:** AB ihracat maruziyeti olan tesislerde karbon maliyeti,
   optimal işletme noktasını daha verimli çözümlere doğru kaydırır. CBAM'ı dikkate almayan
   analizler eksik kalır.

5. **Sektöre özgü exergy profilleri farklıdır:** Çimento'da yüksek sıcaklık yanma baskındır,
   gıda'da düşük sıcaklık ısı ve soğutma, tekstil'de buhar ve kurutma, kimya'da reaktör
   ve basınç süreçleri ana exergy yıkım kaynaklarıdır. Tek tip yaklaşım işe yaramaz.

6. **Fazlı uygulama riski azaltır:** Hızlı kazanımlarla başlayıp (kaçak giderme, bakım, ayar),
   orta ölçek yatırımlara (ekonomizer, VSD, ısı geri kazanımı), ardından ileri entegrasyona
   (CHP, proses entegrasyonu) geçmek hem nakit akışını hem de kurumsal güveni optimize eder.

7. **Duyarlılık analizi yatırım kararını sağlamlaştırır:** Enerji fiyatları, üretim hacmi,
   faiz oranı ve karbon fiyatı gibi belirsiz parametrelerin sonuçlara etkisini görmek,
   karar vericileri ikna etmenin en etkili yoludur.

8. **Exergoekonomik faktör (f_k) doğru yatırım türünü gösterir:** Düşük f_k → termodinamik
   iyileştirme (süreç değişikliği, ısı geri kazanımı), yüksek f_k → daha ucuz ekipman
   veya bakım odaklı müdahale.

9. **Hızlı geri ödeme güven inşa eder:** Faz 1'deki düşük maliyetli, hızlı geri ödemeli
   projeler yönetimi ikna ederek daha büyük yatırımların önünü açar.

10. **Enerji fiyat volatilitesi, verimlilik yatırımlarını doğal olarak hedge eder:** Gıda
    fabrikası vakasında görüldüğü gibi, enerji fiyatları artınca tasarrufun parasal değeri
    de artar — verimlilik yatırımı bir enerji fiyat sigortası işlevi görür.

---

## İlgili Dosyalar

- [Termoekonomik Optimizasyon Genel Bakış](knowledge/factory/thermoeconomic_optimization/overview.md)
- [İteratif Optimizasyon Yöntemi](knowledge/factory/thermoeconomic_optimization/iterative_method.md)
- [Çok Amaçlı Optimizasyon](knowledge/factory/thermoeconomic_optimization/multi_objective.md)
- [Pratik Uygulama Rehberi](knowledge/factory/thermoeconomic_optimization/practical_guide.md)
- [Çözülmüş Örnek: Kazan Optimizasyonu](knowledge/factory/thermoeconomic_optimization/worked_examples/boiler_optimization.md)
- [Çözülmüş Örnek: CHP Optimizasyonu](knowledge/factory/thermoeconomic_optimization/worked_examples/chp_optimization.md)
- [Çözülmüş Örnek: Fabrika Optimizasyonu](knowledge/factory/thermoeconomic_optimization/worked_examples/factory_optimization.md)
- [Fabrika Vaka Çalışmaları (Genel)](knowledge/factory/case_studies.md)
- [Ekonomik Analiz](knowledge/factory/economic_analysis.md)

## Referanslar

### Akademik Kaynaklar

1. Tsatsaronis, G., & Cziesla, F. (2002). "Thermoeconomics." *Encyclopedia of Physical Science
   and Technology*, 3rd ed., Academic Press.

2. Bejan, A., Tsatsaronis, G., & Moran, M.J. (1996). *Thermal Design and Optimization.*
   Wiley-Interscience.

3. Lazzaretto, A., & Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology for
   calculating efficiencies and costs in thermal systems." *Energy*, 31(8-9), 1257-1289.

4. Açıkkalp, E., Aras, H., & Hepbasli, A. (2014). "Advanced exergoeconomic analysis of a
   trigeneration system using a diesel-gas engine." *Applied Thermal Engineering*, 67, 388-396.

5. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T., & Carassai, A. (2012). "Conventional and
   advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152.

6. Deb, K. (2001). *Multi-Objective Optimization using Evolutionary Algorithms.* Wiley.

### Türk Sanayi Kaynakları

7. YEGM (Yenilenebilir Enerji Genel Müdürlüğü). (2023). "Sanayide Enerji Verimliliği
   Uygulama Rehberi."

8. TSE (Türk Standardları Enstitüsü). "TS EN ISO 50001 Enerji Yönetim Sistemi."

9. TOBB (Türkiye Odalar ve Borsalar Birliği). (2024). "Sınırda Karbon Düzenleme
   Mekanizması (CBAM) Türk İhracatçıları İçin Etki Değerlendirmesi."

10. EİE / YEGM. (2022). "Türkiye Çimento Sektörü Enerji Verimliliği Potansiyel Raporu."

### CBAM ve Karbon Fiyatlandırma

11. European Commission. (2023). "Regulation (EU) 2023/956 — Carbon Border Adjustment Mechanism."

12. EMBER Climate. (2024). "EU ETS Carbon Price Tracker and Projections."
