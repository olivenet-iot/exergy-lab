# ExergyLab Brief: Pinch Analizi Detay (Isı Entegrasyonu)

> **Claude Code için:** Bu brief kapsamında pinch analizi ve ısı entegrasyonu için derinlemesine knowledge base oluştur. Bu mevcut factory/ knowledge base'ini genişleten bir çalışmadır.

---

## 🎯 OTONOM YETKİ

Bu brief'i uygularken:
1. Derin araştırma yap — akademik kaynaklar, Linnhoff metodolojisi, endüstri uygulamaları
2. Mevcut proje yapısını incele (`/home/ubuntu/exergy-lab/`) ve tutarlı ol
3. Mevcut `knowledge/factory/pinch_analysis.md` dosyasını incele ve genişlet
4. Mevcut `knowledge/factory/heat_integration.md` dosyasını referans al
5. Eksik gördüğün bilgileri kendi insiyatifinle ekle
6. Mevcut dosyaları silme, sadece yeni dosyalar ekle veya mevcut içeriği zenginleştir

---

## 📋 BÖLÜM 1: Araştırma Konuları

### 1.1 Pinch Analizi Temelleri

- **Linnhoff metodolojisi** (Manchester Üniversitesi)
- **Minimum enerji hedefleri** (MER - Minimum Energy Requirements)
- **ΔT_min seçimi** ve optimum değeri
- **Grand Composite Curve (GCC)**
- **Hot/Cold Composite Curves**
- **Problem Table Algorithm**
- **Shifted Temperature Diagram**
- **Pinch noktası ve altın kurallar:**
  1. Pinch üzerinden ısı transferi yapma
  2. Pinch üzerine soğutma yardımcısı koyma
  3. Pinch altına ısıtma yardımcısı koyma

### 1.2 Isı Eşanjör Ağı (HEN) Tasarımı

- **Stream data extraction** — akışkan verileri çıkarma
- **Targeting** — minimum yardımcı ihtiyacı belirleme
- **HEN design** — eşanjör ağı tasarımı
  - Pinch Design Method
  - Grid diagram
  - Stream splitting
  - Matching rules (CP inequality)
- **HEN optimization** — loop breaking, path shifting
- **Retrofit** — mevcut sisteme uyarlama
- **Area targeting** — minimum eşanjör alanı

### 1.3 İleri Pinch Konuları

- **Total Site Analysis:** Birden fazla proses birimi
- **Column Targeting:** Distilasyon kolonları
- **Batch Process Integration:** Kesikli prosesler
- **Heat Storage:** Isı depolama (batch için)
- **Water Pinch:** Su tüketimi minimizasyonu
- **Hydrogen Pinch:** H₂ ağı optimizasyonu (rafineri)
- **Carbon Pinch:** CO₂ emisyon minimizasyonu
- **Exergy-based Pinch:** Carnot-bazlı composite curves

### 1.4 Pratik Uygulama

- **Veri toplama:** Akışkan sıcaklıkları, debiler, ısı kapasiteleri
- **Software araçları:** HINT, PinchExpress, Aspen Energy Analyzer
- **Maliyet hedefleme:** Bath formula (eşanjör maliyet tahmini)
- **Payback hedefleme:** Enerji tasarrufu vs yatırım dengesi
- **Proses kısıtları:** Korozyon, fouling, güvenlik, mesafe
- **Retrofit tasarım:** Mevcut eşanjörleri koruma

### 1.5 Sektörel Uygulamalar

```
Sektör          | Tipik Tasarruf | ΔT_min Önerisi
----------------|----------------|----------------
Petrokimya      | %20-40         | 10-20°C
Kimya           | %15-30         | 10-15°C
Kağıt/selüloz   | %10-25         | 10-20°C
Gıda            | %10-20         | 5-10°C
Tekstil         | %10-15         | 5-10°C
Çimento         | %5-15          | 20-30°C
Metal           | %10-20         | 15-25°C
```

---

## 📋 BÖLÜM 2: Knowledge Base Genişletme

### 2.1 Yeni Dosyalar

```
knowledge/factory/pinch/
├── INDEX.md
├── fundamentals.md            # Pinch analizi temelleri
├── composite_curves.md        # Composite curve oluşturma
├── grand_composite.md         # Grand Composite Curve (GCC)
├── problem_table.md           # Problem Table Algorithm
├── hen_design.md              # Isı eşanjör ağı tasarımı
├── hen_retrofit.md            # Mevcut sisteme uygulama
├── targeting.md               # Minimum enerji/alan/maliyet hedefleme
├── delta_t_min.md             # ΔT_min seçimi ve optimizasyonu
├── stream_data.md             # Akışkan veri çıkarma kuralları
├── total_site.md              # Total Site Analysis
├── batch_integration.md       # Kesikli proses entegrasyonu
├── utility_systems.md         # Yardımcı sistem optimizasyonu
├── cost_estimation.md         # HEN maliyet tahmini (Bath formula)
├── software_tools.md          # Pinch analizi yazılım araçları
├── practical_guide.md         # Sahada uygulama rehberi
├── common_mistakes.md         # Yaygın hatalar ve kaçınılacaklar
└── case_studies.md            # Sektörel uygulama örnekleri
```

### 2.2 Mevcut Dosya Güncellemeleri

- `knowledge/factory/pinch_analysis.md` → Detay referanslarını ekle
- `knowledge/factory/heat_integration.md` → Pinch bağlantılarını güncelle

### 2.3 Dosya Kuralları

Her dosyada:
- YAML frontmatter
- Türkçe başlıklar (teknik terimler İngilizce parantez)
- Diyagram açıklamaları (ASCII art veya detaylı text)
- Sayısal örnekler (step-by-step hesaplama)
- Pratik ipuçları (sahada ne işe yarar)
- Cross-reference
- Minimum 200 satır (bu konu detay gerektiriyor)

---

## 📋 BÖLÜM 3: Skill Güncelleme

### 3.1 Factory Skills

`/skills/factory/factory_analyst.md` dosyasına pinch analizi karar kuralları ekle:

```
Pinch Analizi Önerisi Koşulları:
1. Fabrikada 3+ ekipman varsa
2. Hem ısıtma hem soğutma ihtiyacı varsa
3. Farklı sıcaklık seviyelerinde akışkanlar varsa
4. Toplam ısı yükü > 500 kW ise

→ "Detaylı pinch analizi ile %10-30 ek tasarruf mümkün" öner
```

### 3.2 Integration Expert

`/skills/factory/integration_expert.md` dosyasında pinch bazlı eşleştirme kurallarını genişlet.

---

## 📋 BÖLÜM 4: Araştırma Kaynakları

### Akademik
- Linnhoff, B. et al. "User Guide on Process Integration for the Efficient Use of Energy" (orijinal kitap)
- Kemp, I.C. "Pinch Analysis and Process Integration" (en güncel referans)
- Smith, R. "Chemical Process Design and Integration"
- Klemeš, J.J. "Handbook of Process Integration"
- Townsend, D.W., Linnhoff, B. "Surface Area Targets for Heat Exchanger Networks"

### Endüstri
- IEA Industrial Energy-Related Technologies and Systems
- US DOE Pinch Analysis for Process Industries
- EU BREF documents (sektörel)
- Carbon Trust Process Integration guides

---

## ✅ Tamamlama Kontrol Listesi

- [ ] knowledge/factory/pinch/ dizini oluşturuldu (~18 dosya)
- [ ] Her dosya minimum 200 satır
- [ ] Sayısal örnekler dahil
- [ ] Mevcut factory dosyaları güncellendi
- [ ] Skills güncellendi
- [ ] Cross-reference'lar kuruldu
- [ ] Commit ve push yapıldı

**Hedef: ~18 dosya, her biri minimum 200 satır, akademik derinlikte.**
