# ExergyLab Brief: Buhar Türbini / CHP (Kojenerasyon) Ekipman Modülü

> **Claude Code için:** Bu brief kapsamında buhar türbini ve CHP sistemleri için knowledge base ve skill dosyaları oluştur. Derin araştırma yap, akademik kaynaklara dayan.

---

## 🎯 OTONOM YETKİ

Bu brief'i uygularken:
1. Brief'teki görevleri tamamla
2. Derin araştırma yap — akademik kaynaklar, endüstri standartları, best practice'ler
3. Mevcut proje yapısını incele (`/home/ubuntu/exergy-lab/`) ve tutarlı ol
4. Eksik gördüğün bilgileri kendi insiyatifinle ekle
5. Cross-reference'ları mevcut ekipmanlarla (özellikle kazan) kur
6. Mevcut çalışan işlevselliği bozma

---

## 📋 PROJE BAĞLAMI

ExergyLab endüstriyel exergy analiz platformu. Mevcut: Kompresör, Kazan, Chiller, Pompa.

Önce mevcut yapıyı incele: `knowledge/boiler/` dizinini referans al (buhar türbini kazanla doğrudan ilişkili).

---

## 📋 BÖLÜM 1: Araştırma Konuları

### 1.1 Buhar Türbini Tipleri

- **Back-pressure (Karşı basınçlı):** Çıkış buharı proses kullanımı
- **Condensing (Yoğuşmalı):** Maksimum güç üretimi
- **Extraction (Ara çekişli):** Farklı basınç seviyelerinde buhar çekişi
- **Impulse vs Reaction:** Türbin aerodinamiği
- **Single-stage vs Multi-stage:** Basınç oranına göre

### 1.2 CHP (Kojenerasyon) Sistemleri

- **Buhar türbini CHP:** Kazan + türbin + proses buhar
- **Gaz türbini CHP:** Gaz türbini + HRSG (atık ısı kazanı)
- **Motor CHP:** Gaz/dizel motor + ısı geri kazanım
- **ORC (Organic Rankine Cycle):** Düşük sıcaklık atık ısı → elektrik
- **Micro-CHP:** Küçük ölçek (<50 kWe)
- **Trigeneration (CCHP):** Elektrik + ısı + soğutma

### 1.3 Exergy Analizi

- Buhar türbininde exergy yıkımı mekanizmaları
- İzentropik verim vs exergy verimi
- Rankine çevrimi exergy analizi
- CHP sistemlerinde exergy paylaşımı (elektrik vs ısı)
- Toplam verim vs exergy verimi karşılaştırması
- Karşı basınçlı vs yoğuşmalı exergy karşılaştırması

### 1.4 Formüller

```
Türbin gücü:
W_turbine = m_steam × (h_in - h_out) (kW)

İzentropik verim:
η_s = (h_in - h_out) / (h_in - h_out_s)

Exergy girişi:
Ex_in = m × [(h_in - h₀) - T₀(s_in - s₀)]

Exergy çıkışı:
Ex_out_work = W_turbine (mekanik iş = saf exergy)
Ex_out_steam = m × [(h_out - h₀) - T₀(s_out - s₀)]

Exergy verimi (back-pressure):
η_ex = (W_turbine + Ex_out_steam) / Ex_in_steam

Exergy verimi (condensing):
η_ex = W_turbine / Ex_in_steam

CHP toplam verim (1. yasa):
η_total = (W_net + Q_useful) / Q_fuel

CHP exergy verimi (2. yasa):
η_ex_CHP = (W_net + Ex_useful_heat) / Ex_fuel

Power-to-Heat Ratio (PHR):
PHR = W_electric / Q_thermal

Primer Enerji Tasarrufu (PES):
PES = 1 - 1/(η_e/η_ref_e + η_th/η_ref_th)
```

### 1.5 Benchmark Değerleri

```
Buhar türbini izentropik verim:
- Küçük (<1 MW): %60-70
- Orta (1-10 MW): %70-80
- Büyük (>10 MW): %80-90

CHP toplam verim:
- Buhar türbini CHP: %75-85
- Gaz türbini CHP: %70-85
- Motor CHP: %80-90

CHP exergy verimi:
- Back-pressure: %30-45
- Gas turbine CHP: %35-50
- Engine CHP: %40-55
```

### 1.6 Endüstriyel Uygulamalar

- Kağıt/selüloz: Back-pressure türbin + proses buhar
- Kimya: Extraction türbin + farklı basınç seviyeleri
- Şeker: Bagasse CHP
- Rafineri: Büyük ölçekli buhar türbin sistemleri
- Gıda: Küçük CHP / ORC
- Genel imalat: Motor CHP + atık ısı

---

## 📋 BÖLÜM 2: Knowledge Base Oluşturma

### 2.1 Dizin Yapısı

```
knowledge/steam_turbine/
├── INDEX.md
├── benchmarks.md              # Performans karşılaştırma
├── formulas.md                # Hesaplama formülleri
├── audit.md                   # Enerji denetim prosedürleri
├── equipment/
│   ├── back_pressure.md       # Karşı basınçlı türbinler
│   ├── condensing.md          # Yoğuşmalı türbinler
│   ├── extraction.md          # Ara çekişli türbinler
│   ├── orc.md                 # Organic Rankine Cycle
│   └── micro_turbine.md       # Mikro türbinler
├── systems/
│   ├── steam_turbine_chp.md   # Buhar türbini CHP
│   ├── gas_turbine_chp.md     # Gaz türbini CHP
│   ├── engine_chp.md          # Motor CHP
│   ├── trigeneration.md       # Üçlü üretim (CCHP)
│   └── hrsg.md                # Atık ısı kazanı
├── solutions/
│   ├── efficiency_improvement.md  # Verim iyileştirme
│   ├── load_matching.md       # Yük eşleştirme
│   ├── condensate_optimization.md # Kondensat optimizasyonu
│   ├── maintenance.md         # Bakım ve izleme
│   └── sizing_guide.md        # Boyutlandırma rehberi
├── economics/
│   ├── feasibility.md         # Fizibilite analizi
│   ├── feed_in_tariff.md      # Elektrik satış tarifeleri
│   └── financing.md           # Finansman modelleri
└── case_studies.md            # Uygulama örnekleri
```

### 2.2 Dosya Kuralları

Her dosyada:
- **YAML frontmatter** (title, category, equipment_type, keywords, related_files, priority)
- **Türkçe başlıklar**, teknik terimler İngilizce parantez içinde
- **SI birimleri** (kW, kWe, kWth, MWe, MWth, bar, °C)
- **EUR para birimi**
- **Minimum 150 satır** her dosya
- **## İlgili Dosyalar** ve **## Referanslar** bölümleri

### 2.3 Cross-Reference

- `knowledge/boiler/` → Buhar üretimi bağlantısı
- `knowledge/factory/cogeneration.md` → CHP fabrika entegrasyonu
- `knowledge/factory/cross_equipment.md` → Ekipmanlar arası fırsatlar

---

## 📋 BÖLÜM 3: Skill Dosyası

**Dosya:** `/skills/equipment/steam_turbine_expert.md`

Karar ağacı:

```
BAŞLA: Buhar türbini / CHP analizi
│
├── Türbin tipi?
│   ├── Back-pressure → Proses buhar kalitesi kontrol
│   ├── Condensing → Vakum performansı kontrol
│   └── Extraction → Her basınç seviyesi ayrı değerlendir
│
├── İzentropik verim < benchmark?
│   ├── EVET → OKU: solutions/efficiency_improvement.md
│   └── HAYIR → Performans kabul edilebilir
│
├── CHP mı?
│   ├── EVET → PES > 10%? (EU CHP Directive kriteri)
│   │   ├── EVET → Yüksek verimli CHP
│   │   └── HAYIR → İyileştirme gerekli
│   └── HAYIR → Sadece türbin analizi
│
└── SONUÇ: Öneri listesi
```

---

## 📋 BÖLÜM 4: Araştırma Kaynakları

### Akademik
- Kotas, T.J. "The Exergy Method of Thermal Plant Analysis"
- Horlock, J.H. "Cogeneration - Combined Heat and Power (CHP)"
- Bejan, A. "Advanced Engineering Thermodynamics"
- "Exergy analysis of steam turbine cogeneration systems" (Google Scholar)

### Standartlar ve Düzenlemeler
- EU CHP Directive 2012/27/EU
- EN 50583 (CHP verimliliği)
- API 612 (Special Purpose Steam Turbines)
- ASME PTC 6 (Steam Turbine Performance)

### Endüstri
- US DOE CHP Technical Assistance
- IEA CHP/DHC reports
- COGEN Europe
- Türkiye YEGM kojenerasyon mevzuatı

---

## ✅ Tamamlama Kontrol Listesi

- [ ] knowledge/steam_turbine/ dizini oluşturuldu (~20 dosya)
- [ ] Tüm dosyalarda YAML frontmatter var
- [ ] skills/equipment/steam_turbine_expert.md oluşturuldu
- [ ] Cross-reference'lar kuruldu
- [ ] INDEX dosyaları güncellendi
- [ ] Commit ve push yapıldı

**Hedef: ~20 dosya, her biri minimum 150 satır, akademik kalitede.**
