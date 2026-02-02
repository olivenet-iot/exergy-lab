# ExergyLab Brief: Kurutma Fırını (Industrial Dryer) Ekipman Modülü

> **Claude Code için:** Bu brief kapsamında endüstriyel kurutma fırınları için knowledge base ve skill dosyaları oluştur. Derin araştırma yap, akademik kaynaklara dayan.

---

## 🎯 OTONOM YETKİ

Bu brief'i uygularken:
1. Brief'teki görevleri tamamla
2. Derin araştırma yap — akademik kaynaklar, endüstri standartları
3. Mevcut proje yapısını incele (`/home/ubuntu/exergy-lab/`) ve tutarlı ol
4. Eksik gördüğün bilgileri kendi insiyatifinle ekle
5. Cross-reference'ları mevcut ekipmanlarla kur
6. Mevcut çalışan işlevselliği bozma

---

## 📋 PROJE BAĞLAMI

ExergyLab endüstriyel exergy analiz platformu. Mevcut: Kompresör, Kazan, Chiller, Pompa.

Kurutma fırınları endüstride en büyük enerji tüketicilerden biri:
- Gıda: Toplam enerjinin %30-50'si kurutmaya gider
- Kağıt: %50-70 kurutma
- Tekstil: %30-40 kurutma
- Seramik: %40-60 kurutma/pişirme

Bu ekipman ExergyLab için yüksek değerli bir ekleme.

---

## 📋 BÖLÜM 1: Araştırma Konuları

### 1.1 Kurutma Fırını Tipleri

- **Konvektif kurutuculaer:**
  - Tünnel kurutucu (tunnel dryer)
  - Bant kurutucu (belt/conveyor dryer)
  - Döner kurutucu (rotary dryer)
  - Akışkan yataklı kurutucu (fluidized bed dryer)
  - Sprey kurutucu (spray dryer)
  - Flash kurutucu (pneumatic dryer)
  
- **İletimli (conduction) kurutucular:**
  - Silindir kurutucu (drum dryer)
  - Tray/raf kurutucu
  - Vakum kurutucu
  
- **Radyasyonlu kurutucular:**
  - Infrared kurutucu
  - Mikrodalga kurutucu
  
- **Özel tipler:**
  - Isı pompalı kurutucu (heat pump dryer)
  - Superheated steam dryer (kızgın buhar)
  - Solar kurutucu
  - Freeze dryer (liyofilizatör)

### 1.2 Exergy Analizi Temelleri

- Kurutma prosesinin termodinamik temelleri
- Nemli hava termodinamiği (psikrometri)
- Buharlaşma exergy'si
- Egzoz havası exergy kaybı (en büyük kayıp kaynağı)
- Isıtma/soğutma exergy'si
- Konvektif vs iletimli kurutmada exergy karşılaştırması
- Kurutma hızı eğrileri ve exergy ilişkisi

### 1.3 Formüller

```
Kurutma yükü:
Q_evap = m_water × h_fg (kW)
h_fg ≈ 2,257 kJ/kg (100°C'de)

Kurutma havası:
Q_air = m_air × cp_air × (T_in - T_amb) (kW)

Kurutma verimi (enerji):
η_energy = Q_evap / Q_total

Kurutma verimi (exergy):
η_exergy = Ex_evap / Ex_total

Buharlaşma exergy'si:
Ex_evap = m_water × [(h_fg - T₀ × s_fg)] (kW)
(genellikle düşüktür: ~100°C'de ≈ 167 kJ/kg, cf. h_fg = 2,257 kJ/kg)

Egzoz exergy kaybı:
Ex_exhaust = m_exhaust × cp × [(T_ex - T₀) - T₀ × ln(T_ex/T₀)]

Spesifik enerji tüketimi (SMER):
SMER = kg_water_removed / kWh_energy

Spesifik nem alma oranı (SMER):
- İyi: > 1.0 kg/kWh
- Ortalama: 0.5-1.0 kg/kWh
- Kötü: < 0.5 kg/kWh
```

### 1.4 Benchmark ve Performans

```
Kurutma tipi bazlı enerji verimi:
- Konvektif tünnel: %35-50
- Bant kurutucu: %40-55
- Döner kurutucu: %45-60
- Akışkan yatak: %50-65
- Sprey kurutucu: %40-55
- Isı pompalı: %60-80
- Kızgın buhar: %70-90

Kurutma exergy verimi (tipik):
- Konvektif: %10-25 (çok düşük!)
- İletimli: %15-30
- Isı pompalı: %25-40
- Kızgın buhar: %30-50

Not: Kurutma prosesi inherent olarak exergy-destructive
çünkü yüksek kaliteli enerji (buhar/doğalgaz) düşük kaliteli 
iş için kullanılıyor (suyu buharlaştırma).
```

### 1.5 Yaygın Sorunlar ve Çözümler

- Egzoz havası ısı geri kazanımı (en büyük potansiyel)
- Egzoz havası recirculation (kısmi geri devir)
- Isı pompalı kurutma (özellikle düşük sıcaklık)
- Mekanik ön su alma (pres, santrifüj)
- İzolasyon iyileştirme
- Kurutma hava sıcaklığı optimizasyonu
- Superheated steam kurutma
- Solar ön ısıtma

### 1.6 Sektörel Uygulamalar

- **Gıda:** Sprey kurutma (süt tozu), bant kurutma (meyve, sebze), döner (tahıl)
- **Kağıt/Selüloz:** Silindir kurutucular, IR kurutma
- **Tekstil:** Tenter kurutma, ram fırın, infrared
- **Seramik:** Tünel fırın, roller fırın
- **Ahşap:** Kereste kurutma fırınları
- **Kimya:** Akışkan yatak, sprey, döner
- **Madencilik:** Döner kurutucu, akışkan yatak

---

## 📋 BÖLÜM 2: Knowledge Base Oluşturma

### 2.1 Dizin Yapısı

```
knowledge/dryer/
├── INDEX.md
├── benchmarks.md              # Performans karşılaştırma (SMER, verimler)
├── formulas.md                # Hesaplama formülleri (kurutma, exergy)
├── audit.md                   # Enerji denetim prosedürleri
├── psychrometrics.md          # Nemli hava termodinamiği
├── equipment/
│   ├── tunnel_dryer.md        # Tünel kurutucu
│   ├── belt_dryer.md          # Bant kurutucu
│   ├── rotary_dryer.md        # Döner kurutucu
│   ├── fluidized_bed.md       # Akışkan yataklı
│   ├── spray_dryer.md         # Sprey kurutucu
│   ├── drum_dryer.md          # Silindir kurutucu
│   ├── heat_pump_dryer.md     # Isı pompalı kurutucu
│   └── infrared_dryer.md      # Infrared kurutucu
├── solutions/
│   ├── exhaust_heat_recovery.md   # Egzoz ısı geri kazanımı
│   ├── air_recirculation.md   # Hava geri deviri
│   ├── heat_pump_retrofit.md  # Isı pompası retrofit
│   ├── mechanical_dewatering.md # Mekanik ön su alma
│   ├── insulation.md          # İzolasyon iyileştirme
│   ├── temperature_optimization.md # Sıcaklık optimizasyonu
│   └── solar_preheating.md    # Solar ön ısıtma
├── sectors/
│   ├── food_drying.md         # Gıda kurutma uygulamaları
│   ├── paper_drying.md        # Kağıt kurutma
│   ├── textile_drying.md      # Tekstil kurutma
│   ├── ceramic_drying.md      # Seramik kurutma/pişirme
│   └── wood_drying.md         # Kereste kurutma
└── case_studies.md            # Uygulama örnekleri
```

### 2.2 Dosya Kuralları

Diğer ekipmanlarla aynı:
- YAML frontmatter, Türkçe başlıklar, SI birimleri, EUR
- Cross-reference, referanslar
- Minimum 150 satır
- Tablolar, formüller, pratik örnekler

---

## 📋 BÖLÜM 3: Skill Dosyası

**Dosya:** `/skills/equipment/dryer_expert.md`

Karar ağacı:

```
BAŞLA: Kurutma fırını analizi
│
├── Exergy verimi < 15%?
│   ├── EVET → Kritik düşük (ama kurutma için normal olabilir!)
│   │   ├── Egzoz sıcaklığı > 80°C?
│   │   │   └── OKU: solutions/exhaust_heat_recovery.md
│   │   ├── Egzoz nemi < %60 bağıl nem?
│   │   │   └── OKU: solutions/air_recirculation.md
│   │   └── Düşük sıcaklık kurutma (<80°C)?
│   │       └── OKU: solutions/heat_pump_retrofit.md
│   │
│   └── HAYIR → Kurutma için kabul edilebilir
│       ├── Mekanik ön su alma yapılıyor mu?
│       │   └── HAYIR → OKU: solutions/mechanical_dewatering.md
│       └── İzolasyon durumu?
│           └── Kötü → OKU: solutions/insulation.md
│
├── SMER < 0.5 kg/kWh?
│   └── EVET → Ciddi verim sorunu, kapsamlı analiz gerekli
│
└── SONUÇ: Kurutma inherently exergy-destructive
    → Egzoz geri kazanımı en büyük potansiyel
    → Isı pompası büyük fark yaratabilir
```

**Önemli not:** Kurutma exergy verimi doğal olarak düşüktür (%10-25 konvektif). Bu diğer ekipmanlardan farklı! AI yorumlarken bunu dikkate almalı.

---

## 📋 BÖLÜM 4: Araştırma Kaynakları

### Akademik
- Mujumdar, A.S. "Handbook of Industrial Drying" (ana referans)
- Kemp, I.C. "Fundamentals of Energy Analysis of Dryers"
- "Exergy analysis of industrial drying processes" (Google Scholar)
- Dincer, I. "Exergy Analysis of Drying Processes and Systems"

### Standartlar
- ISO 13579 (Thermal Process Safety)
- ATEX directives (patlama güvenliği)
- EU BREF: Food, Textiles, Pulp & Paper

### Endüstri
- US DOE Process Heating Best Practices
- Carbon Trust drying guides
- IEA Industrial Energy Technology Roadmap

---

## ✅ Tamamlama Kontrol Listesi

- [ ] knowledge/dryer/ dizini oluşturuldu (~22 dosya)
- [ ] Tüm dosyalarda YAML frontmatter var
- [ ] skills/equipment/dryer_expert.md oluşturuldu
- [ ] Cross-reference'lar kuruldu
- [ ] INDEX dosyaları güncellendi
- [ ] Commit ve push yapıldı

**Hedef: ~22 dosya, her biri minimum 150 satır, akademik kalitede.**
