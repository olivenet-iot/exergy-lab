# ExergyLab Brief: Isı Eşanjörü (Heat Exchanger) Ekipman Modülü

> **Claude Code için:** Bu brief kapsamında ısı eşanjörü için knowledge base, engine ve skill dosyaları oluştur. Derin araştırma yap, akademik kaynaklara dayan.

---

## 🎯 OTONOM YETKİ

Bu brief'i uygularken:
1. Brief'teki görevleri tamamla
2. Derin araştırma yap — akademik kaynaklar, endüstri standartları, best practice'ler
3. Mevcut proje yapısını incele ve tutarlı ol
4. Eksik gördüğün bilgileri kendi insiyatifinle ekle
5. Cross-reference'ları mevcut ekipmanlarla (kompresör, kazan, chiller, pompa) kur
6. Mevcut çalışan işlevselliği bozma

---

## 📋 PROJE BAĞLAMI

ExergyLab, endüstriyel ekipmanların exergy analizini yapan bir platformdur.

**Mevcut Ekipmanlar:** Kompresör, Kazan, Chiller, Pompa (4 tip)
**Mevcut Yapı:** `/home/ubuntu/exergy-lab/`

```
knowledge/
├── compressor/ (18 dosya)
├── boiler/ (22 dosya)
├── chiller/ (24 dosya)
├── pump/ (22 dosya)
└── factory/ (33 dosya)

skills/
├── core/
├── equipment/
├── factory/
└── output/
```

Önce mevcut yapıyı incele: `knowledge/compressor/` veya `knowledge/boiler/` dizinlerindeki dosya yapısını referans al.

---

## 📋 BÖLÜM 1: Araştırma Konuları

### 1.1 Isı Eşanjörü Tipleri

Derin araştırma yap:

- **Shell & Tube (Boru Demeti):** En yaygın endüstriyel tip, TEMA standartları
- **Plate (Plakalı):** Kompakt, yüksek verimli, gıda/kimya sektörü
- **Air-cooled (Hava Soğutmalı):** Fan + finned tube
- **Double-pipe (Çift Borulu):** Basit, küçük kapasiteler
- **Spiral:** Kirli akışkanlar, yüksek viskozite
- **Finned tube (Kanatlı boru):** Gaz-sıvı ısı transferi
- **Recuperator / Regenerator:** Baca gazı ısı geri kazanımı
- **Economizer:** Kazan baca gazı → besleme suyu
- **Air preheater:** Baca gazı → yanma havası

### 1.2 Exergy Analizi Temelleri

- Isı eşanjörlerinde exergy yıkımı mekanizmaları
- Sıcaklık farkı (ΔT) ve exergy kaybı ilişkisi
- Basınç düşüşü ve exergy kaybı
- LMTD (Log Mean Temperature Difference) metodu
- ε-NTU (Effectiveness-NTU) metodu
- Minimum ΔT (approach temperature) ve optimum değeri
- Fouling (kirlenme) etkisi

### 1.3 Formüller

```
Isı transferi:
Q = U × A × LMTD (kW)

LMTD:
LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁/ΔT₂)

Eşanjör etkinliği:
ε = Q_gerçek / Q_maksimum

Exergy yıkımı:
I = T₀ × ΔS_toplam
I = T₀ × [m_h × cp_h × ln(T_h_out/T_h_in) + m_c × cp_c × ln(T_c_out/T_c_in)]

NTU:
NTU = U × A / C_min

Basınç düşüşü exergy kaybı:
I_ΔP = m × T₀ × R × ln(P_in/P_out) / M  (gaz için)
I_ΔP = m × v × ΔP × T₀ / T_avg  (sıvı için, yaklaşık)

Fouling etkisi:
1/U_fouled = 1/U_clean + R_f_hot + R_f_cold
```

### 1.4 Benchmark ve Performans Göstergeleri

- U değeri benchmarkları (tip ve akışkan kombinasyonuna göre)
- Approach temperature benchmarkları
- Fouling faktörleri (TEMA standart değerleri)
- Basınç düşüşü limitleri
- Exergy verimi karşılaştırmaları

### 1.5 Yaygın Sorunlar ve Çözümler

- Fouling (kirlenme) → Temizlik programı, CIP
- Düşük ΔT tasarımı → Eşanjör boyutlandırma
- Aşırı basınç düşüşü → Bypass, paralel bağlantı
- Korozyon → Malzeme seçimi
- Vibrasyon → Baffle tasarımı
- Maldistribution → Akış dengeleme

### 1.6 Endüstriyel Uygulamalar

- Kazan economizer
- Kompresör atık ısı geri kazanımı
- Chiller kondenser/evaporatör
- Proses ısıtma/soğutma
- Buhar kondensat geri kazanımı
- CIP ısı geri kazanımı (gıda sektörü)
- Baca gazı ısı geri kazanımı

---

## 📋 BÖLÜM 2: Knowledge Base Oluşturma

### 2.1 Dizin Yapısı

```
knowledge/heat_exchanger/
├── INDEX.md
├── benchmarks.md              # Performans karşılaştırma (U değerleri, verimler)
├── formulas.md                # Hesaplama formülleri (LMTD, NTU, exergy)
├── audit.md                   # Enerji denetim prosedürleri
├── equipment/
│   ├── shell_and_tube.md      # Boru demeti eşanjörler
│   ├── plate.md               # Plakalı eşanjörler
│   ├── air_cooled.md          # Hava soğutmalı
│   ├── double_pipe.md         # Çift borulu
│   ├── spiral.md              # Spiral eşanjörler
│   ├── economizer.md          # Kazan ekonomizerleri
│   ├── air_preheater.md       # Hava ön ısıtıcıları
│   └── recuperator.md         # Rekuperatörler
├── solutions/
│   ├── fouling_management.md  # Kirlenme yönetimi
│   ├── approach_temp.md       # Approach temperature optimizasyonu
│   ├── pressure_drop.md       # Basınç düşüşü azaltma
│   ├── heat_recovery.md       # Isı geri kazanım uygulamaları
│   ├── retrofit.md            # Mevcut eşanjör iyileştirme
│   └── material_selection.md  # Malzeme seçimi (korozyon)
├── standards.md               # TEMA, ASME, API standartları
└── case_studies.md            # Uygulama örnekleri
```

### 2.2 Dosya Kuralları

Her dosyada:
- **YAML frontmatter** (title, category, equipment_type, keywords, related_files, priority)
- **Türkçe başlıklar**, teknik terimler İngilizce parantez içinde
- **SI birimleri** (kW, m², W/m²K, °C, bar, Pa)
- **EUR para birimi**
- **Tablolar** (benchmark, U değerleri, fouling faktörleri)
- **Formüller** (code block içinde)
- **Pratik örnekler** (gerçekçi sayısal değerlerle)
- **## İlgili Dosyalar** bölümü
- **## Referanslar** bölümü (akademik, standart, endüstri)
- **Minimum 150 satır** her dosya

### 2.3 Cross-Reference Gereksinimleri

Bu dosyalar şu mevcut dosyalarla ilişkilendirilmeli:
- `knowledge/boiler/solutions/economizer.md` → Kazan economizer
- `knowledge/compressor/solutions/heat_recovery.md` → Kompresör atık ısı
- `knowledge/chiller/equipment/*.md` → Evaporatör/kondenser
- `knowledge/factory/cross_equipment.md` → Ekipmanlar arası entegrasyon
- `knowledge/factory/heat_integration.md` → Isı entegrasyonu
- `knowledge/factory/waste_heat_recovery.md` → Atık ısı geri kazanımı

---

## 📋 BÖLÜM 3: Skill Dosyası

### 3.1 Equipment Skill

**Dosya:** `/skills/equipment/heat_exchanger_expert.md`

İçermesi gerekenler:
- YAML frontmatter
- Uzmanlık alanı
- Kritik metrikler (U değeri, approach temp, effectiveness, exergy verimi)
- Karar ağacı
- Tip bazlı değerlendirme kuralları
- Tipik öneriler ve ROI
- Yanıt örneği

### 3.2 Karar Ağacı

```
BAŞLA: Isı eşanjörü analizi
│
├── Effectiveness < 60%?
│   ├── EVET → Düşük performans
│   │   ├── Fouling riski? (ΔT artmış, U düşmüş)
│   │   │   └── OKU: solutions/fouling_management.md
│   │   ├── Approach temperature > 15°C?
│   │   │   └── OKU: solutions/approach_temp.md
│   │   └── Eşanjör yaşlı/eskimiş?
│   │       └── OKU: solutions/retrofit.md
│   │
│   └── HAYIR → Kabul edilebilir
│       ├── Basınç düşüşü yüksek?
│       │   └── OKU: solutions/pressure_drop.md
│       └── Ek ısı geri kazanım potansiyeli?
│           └── OKU: solutions/heat_recovery.md
```

---

## 📋 BÖLÜM 4: Mevcut Dosyaları Güncelle

### 4.1 Knowledge INDEX

`/knowledge/INDEX.md` dosyasına heat_exchanger kategorisini ekle.

### 4.2 Factory Cross-References

`/knowledge/factory/cross_equipment.md` dosyasında ısı eşanjörü referanslarını güncelle.

### 4.3 Skills README

`/skills/README.md` dosyasına heat_exchanger_expert skill'ini ekle.

---

## 📋 BÖLÜM 5: Araştırma Kaynakları

Derin araştırma için şu kaynakları kullan:

### Akademik
- Bejan, A. "Entropy Generation Through Heat and Fluid Flow"
- Kakaç, S., Liu, H. "Heat Exchangers: Selection, Rating, and Thermal Design"
- Shah, R.K., Sekulić, D.P. "Fundamentals of Heat Exchanger Design"
- Exergy analysis of heat exchangers (Google Scholar araştır)

### Standartlar
- TEMA (Tubular Exchanger Manufacturers Association)
- ASME Section VIII (basınçlı kaplar)
- API 660/661/662 (eşanjör standartları)
- HTRI/HTFS tasarım metodolojileri

### Endüstri
- US DOE Steam Best Practices
- EU BREF (BAT Reference Documents)
- ASHRAE guidelines

---

## ✅ Tamamlama Kontrol Listesi

- [ ] Araştırma yapıldı
- [ ] knowledge/heat_exchanger/ dizini oluşturuldu
- [ ] INDEX.md oluşturuldu
- [ ] benchmarks.md oluşturuldu
- [ ] formulas.md oluşturuldu
- [ ] audit.md oluşturuldu
- [ ] equipment/ dosyaları oluşturuldu (8 dosya)
- [ ] solutions/ dosyaları oluşturuldu (6 dosya)
- [ ] standards.md oluşturuldu
- [ ] case_studies.md oluşturuldu
- [ ] Tüm dosyalarda YAML frontmatter var
- [ ] Tüm dosyalarda cross-reference var
- [ ] skills/equipment/heat_exchanger_expert.md oluşturuldu
- [ ] Mevcut INDEX dosyaları güncellendi
- [ ] Commit ve push yapıldı

**Hedef: ~20 dosya, her biri minimum 150 satır, akademik kalitede.**
