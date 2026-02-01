---
title: "Çözüm: Kavitasyon Önleme — Cavitation Prevention"
category: solutions
equipment_type: pump
keywords: [kavitasyon, NPSH, pompa, hasar]
related_files: [pump/formulas.md, pump/equipment/centrifugal.md, pump/solutions/system_optimization.md]
use_when: ["Kavitasyon önleme önerilirken", "NPSH problemi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Kavitasyon Önleme — Cavitation Prevention

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Kavitasyon (cavitation), pompa içinde sıvının buhar basıncının altına düşmesi sonucu oluşan buhar kabarcıklarının yüksek basınç bölgesinde ani çökmesiyle meydana gelir. Bu durum pompa verimini düşürür, impeller ve gövdede pitting hasarı yaratır, gürültü ve titreşime neden olur. Kavitasyonlu çalışma pompa ömrünü %50-80 kısaltabilir.

**Çözüm:** NPSH (Net Positive Suction Head) marjını artırma, emme koşullarını iyileştirme ve sistem tasarımını optimize etme ile kavitasyonu önleme.

**Tipik Tasarruf:** %5-15 (verim kaybı önleme + ömür uzatma ile bakım maliyeti azalma)
**Tipik ROI:** <1 yıl (önleme bazlı)

## Kavitasyon Mekanizması

### Oluşum Süreci

1. **Basınç düşüşü:** Sıvı, pompa emme bölgesinde ve impeller girişinde hızlanır → basınç düşer
2. **Buharlaşma:** Lokal basınç, sıvının buhar basıncının altına düşerse sıvı buharlaşır → buhar kabarcıkları oluşur
3. **Çökme (implosion):** Kabarcıklar impeller kanallarında yüksek basınç bölgesine geçince ani çöker
4. **Hasar:** Çökme sırasında oluşan mikro-jet'ler ve şok dalgaları metal yüzeyde pitting (çukurcuk) hasarı yaratır

### Kavitasyon Türleri

| Tür | Mekanizma | Belirti | Hasar Seviyesi |
|-----|-----------|---------|---------------|
| Suction cavitation | Düşük NPSHa | Emme tarafında pitting | Yüksek |
| Discharge cavitation | Aşırı yüksek basınç, düşük debi | Basma tarafında pitting | Çok yüksek |
| Recirculation cavitation | BEP'in çok altında çalışma | İmpeller giriş kenarında hasar | Orta-Yüksek |
| Air entrainment | Emme hattında hava girişi | Düzensiz performans | Düşük-Orta |

## NPSH Hesabı

### Temel Kavramlar

- **NPSHa (Available):** Sistem tarafından sağlanan net pozitif emme basıncı — sistem parametresi
- **NPSHr (Required):** Pompanın kavitasyonsuz çalışması için gereken minimum NPSH — pompa parametresi (kataloğdan okunur)
- **NPSH3:** Pompanın toplam head değerinin %3 düştüğü NPSH değeri (Hydraulic Institute standardı)

### NPSHa Hesap Formülü

```
NPSHa = (P_atm - P_buhar) / (ρ × g) + h_s - h_f - h_i

Burada:
  P_atm    = Atmosferik basınç veya tank basıncı [Pa]
  P_buhar  = Sıvının buhar basıncı (sıcaklığa bağlı) [Pa]
  ρ        = Sıvı yoğunluğu [kg/m³]
  g        = Yerçekimi ivmesi (9.81 m/s²)
  h_s      = Statik emme yüksekliği [m] (+ tank pompanın üstünde, - altında)
  h_f      = Emme hattı sürtünme kayıpları [m]
  h_i      = Emme hattı lokal kayıplar (dirsek, vana, filtre) [m]
```

### Güvenlik Marjı

```
NPSHa > NPSHr + Marj

Hydraulic Institute önerileri:
  - Düşük suction energy:   NPSHa ≥ 1.1 × NPSHr
  - Orta suction energy:    NPSHa ≥ 1.3 × NPSHr
  - Yüksek suction energy:  NPSHa ≥ 1.5-2.0 × NPSHr
  - Çok yüksek suction energy: NPSHa ≥ 2.0-5.0 × NPSHr

Genel pratik kural: NPSHa > NPSHr + 0.5-1.0 m (minimum)
```

### NPSHr Tipik Değerleri

| Pompa Tipi | Tipik NPSHr Aralığı | Not |
|-----------|---------------------|-----|
| Küçük santrifüj (<10 kW) | 1.5-3.0 m | Düşük devirli daha iyi |
| Orta santrifüj (10-100 kW) | 2.0-6.0 m | Boyut ve devire bağlı |
| Büyük santrifüj (>100 kW) | 3.0-10.0 m | Yüksek hız → yüksek NPSHr |
| İndüserli pompa | 0.5-1.5 m | Özel tasarım, düşük NPSHr |
| Pozitif deplasmanlı | 0.5-2.0 m | Genelde daha düşük NPSHr |

## Sıcaklığın Buhar Basıncına Etkisi (Su)

| Sıcaklık (°C) | Buhar Basıncı (kPa) | NPSHa Etkisi (m) |
|----------------|---------------------|-------------------|
| 20 | 2.3 | Referans |
| 40 | 7.4 | -0.52 m |
| 60 | 19.9 | -1.79 m |
| 80 | 47.4 | -4.60 m |
| 100 | 101.3 | -10.08 m |
| 120 | 198.5 | -19.99 m |

**Kritik not:** Sıcak sıvı pompalayan sistemlerde NPSHa dramatik şekilde azalır. Her 20°C sıcaklık artışı, NPSHa'yı önemli ölçüde düşürür.

## Kavitasyon Belirtileri

| Belirti | Açıklama | Tespit Yöntemi |
|---------|----------|---------------|
| Gürültü | "Çakıl taşı pompalıyor" sesi | Duyusal muayene |
| Titreşim | Geniş bant yüksek frekanslı titreşim artışı | Titreşim ölçümü |
| Performans düşüşü | Head ve debi beklenenin altında | Performans testi |
| Pitting hasarı | İmpeller ve gövdede çukurcuk oluşumu | Görsel muayene (bakımda) |
| Güç dalgalanması | Motor akımında düzensiz değişimler | Güç/akım izleme |
| Akustik emisyon | Yüksek frekanslı akustik sinyal (>20 kHz) | Ultrasonik cihaz |

## Çözüm Yaklaşımları

| Çözüm | Yöntem | NPSHa Etkisi | Maliyet | Uygulanabilirlik |
|-------|--------|-------------|---------|-----------------|
| Tank yükseltme | Emme tankını pompanın üzerine al (flooded suction) | +2-10 m | €2,000-20,000 | İdeal çözüm, inşaat gerekir |
| Emme borusu büyütme | Daha büyük çaplı boru → sürtünme azalır | +0.5-3 m | €1,000-10,000 | Basit ve etkili |
| Emme hattı kısaltma | Pompa'yı tanka yaklaştır | +0.5-2 m | €500-5,000 | Yerleşime bağlı |
| Dirsek/vana azaltma | Emme hattındaki lokal kayıpları azalt | +0.3-1.5 m | €200-2,000 | Kolay uygulama |
| Sıcaklık düşürme | Sıvı sıcaklığını soğutma ile düşür | Değişken | €2,000-15,000 | Sıcak sıvı uygulamaları |
| Pompa hızı düşürme (VSD) | Düşük hızda NPSHr azalır | NPSHr azalır | €3,000-30,000 | Değişken debi uygulamaları |
| İndüser ekleme | Pompa emişine ön-impeller ekleme | NPSHr %50 azalır | €1,000-5,000 | Retrofit mümkünse |
| Emme basıncı artırma | Kapalı tanka basınç uygula | +belirlenen kadar | €500-5,000 | Kapalı tank gerekli |
| Yeni pompa seçimi | Düşük NPSHr'li pompa seç | NPSHr azalır | €3,000-50,000 | En kalıcı çözüm |

## Kavitasyon Hasarının Maliyet Etkisi

| Etki Alanı | Maliyet Artışı | Açıklama |
|-----------|---------------|----------|
| İmpeller değişimi | €500-10,000/adet | Kavitasyon hasarı → erken impeller değişimi |
| Pompa arıza duruşu | €1,000-50,000/olay | Plansız üretim kaybı |
| Verim kaybı | %5-15 enerji artışı | Sürekli ekstra enerji maliyeti |
| Mekanik conta arızası | €300-3,000/adet | Titreşim kaynaklı erken arıza |
| Rulman arızası | €100-1,000/adet | Titreşim ve dinamik yüklerden |
| Pompa ömür kısalması | Normal ömrün %50-80'i | Toplam sahip olma maliyeti artışı |

### Maliyet Örneği
- 30 kW pompa, kavitasyonlu çalışma
- Yıllık ekstra enerji: 30 × 0.10 × 6,000 × 0.15 = €2,700/yıl (%10 verim kaybı)
- İmpeller değişimi (her 2 yıl yerine 5 yıl): €3,000/3 yıl = €1,000/yıl ek maliyet
- Plansız duruş (yılda 1): €5,000/olay
- **Toplam yıllık kavitasyon maliyeti: ~€8,700**
- **NPSHa iyileştirme yatırımı: €5,000-15,000 → ROI: 6-18 ay**

## Uygulanabilirlik Kriterleri

### Kavitasyon Önleme Ne Zaman Kritik
- Sıcak sıvı uygulamaları (>60°C): Buhar basıncı yüksek
- Negatif emme yüksekliği: Pompa sıvı seviyesinin üzerinde
- Yüksek devirli pompalar: NPSHr yüksek
- Değişken debili sistemler: Farklı çalışma noktalarında NPSH değişir
- Uzun veya karmaşık emme hattı: Sürtünme kayıpları yüksek

## Yatırım Maliyeti

| Çözüm | Maliyet Aralığı | Tipik NPSHa Artışı |
|-------|-----------------|-------------------|
| Emme borusu optimizasyonu | €500-5,000 | +0.5-3 m |
| İndüser ekleme | €1,000-5,000 | NPSHr %50 azalma |
| Tank yükseltme (yapısal) | €5,000-30,000 | +2-10 m |
| VSD (hız düşürme) | €3,000-30,000 | NPSHr azalma |
| Sıvı soğutma sistemi | €3,000-15,000 | Değişken |
| Yeni düşük-NPSHr pompa | €3,000-50,000 | NPSHr azalma |

## ROI Hesabı

### Formül
```
Yıllık_kavitasyon_maliyeti = Enerji_kaybı + Bakım_artışı + Duruş_maliyeti + Ömür_kısalma
Yatırım = Çözüm_maliyeti + Montaj + Mühendislik
Geri_ödeme_yıl = Yatırım / Yıllık_kavitasyon_maliyeti
```

### Örnek Hesap
- 45 kW pompa, kavitasyon nedeniyle %8 verim kaybı
- 6,000 saat/yıl, elektrik €0.15/kWh
- İmpeller her 2 yılda bir değişim (normalde 5 yılda bir)

```
Enerji kaybı = 45 × 0.08 × 6,000 × 0.15 = €3,240/yıl
İmpeller ek maliyeti = €4,000 / 3 yıl (2 yıl vs 5 yıl farkı) = €1,333/yıl
Plansız duruş (0.5 olay/yıl × €5,000) = €2,500/yıl
Toplam yıllık maliyet = €7,073/yıl

Çözüm: Emme borusu büyütme + yerleşim optimizasyonu
Yatırım = €6,000

Geri_ödeme = 6,000 / 7,073 = 0.85 yıl ≈ 10 ay
```

## Uygulama Adımları

1. **NPSH analizi:** NPSHa ve NPSHr değerlerini tüm çalışma noktaları için hesapla
2. **Kavitasyon tespiti:** Gürültü, titreşim ve performans ölçümü ile mevcut kavitasyonu doğrula
3. **Kök neden analizi:** NPSHa neden yetersiz? (düşük seviye, sıcaklık, uzun boru, kayıplar)
4. **Çözüm seçimi:** Maliyet-etkinlik analizine göre en uygun çözümü belirle
5. **Tasarım:** Seçilen çözümün mühendislik tasarımını yap (boru hesabı, tank tasarımı vb.)
6. **Uygulama:** Montaj ve mekanik işleri gerçekleştir
7. **Doğrulama:** Yeni NPSHa hesapla, performans testi yap, kavitasyon belirtilerinin ortadan kalktığını doğrula
8. **İzleme:** Periyodik NPSH marjı kontrolü ve titreşim izleme programı başlat

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Yetersiz marj | NPSHa marjı yeterince artırılmadı | HI önerilerine göre marj hesapla |
| Sıcaklık değişimi | Mevsimsel sıcaklık değişimi NPSHa'yı etkiler | En kötü durum senaryosu ile hesapla |
| Seviye değişimi | Tank seviyesi düştüğünde NPSHa azalır | Minimum seviye senaryosu ile hesapla |
| Hava girişi | Emme hattında sızıntı ile hava girer | Emme hattını basınç testi yap |
| Aşırı önlem | Gereğinden fazla yatırım (over-engineering) | ROI analizi ile optimize et |

## İlgili Dosyalar
- Pompa VSD çözümü: `solutions/pump_vsd.md`
- Pompa bakım çözümü: `solutions/pump_maintenance.md`
- Pompa throttle eliminasyonu: `solutions/pump_throttle_elimination.md`
- Pompa exergy formülleri: `formulas/pump_exergy.md`

## Referanslar
- Hydraulic Institute, ANSI/HI 9.6.1 — "Rotodynamic Pumps: Guideline for NPSH Margin"
- Hydraulic Institute, ANSI/HI 9.6.3 — "Rotodynamic Pumps: Guideline for Allowable Operating Region"
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- Pumps & Systems, "What You Need to Know about NPSH & Cavitation"
- Karassik, I.J., et al., "Pump Handbook" 4th Edition — McGraw-Hill
- ISO 10816-7 — Mechanical vibration: Evaluation of machine vibration (Rotary pumps)
