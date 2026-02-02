# ExergyLab Brief: Exergoekonomik Analiz (Exergoeconomic Analysis)

> **Claude Code için:** Bu brief kapsamında exergoekonomik analiz (SPECO metodu) için derinlemesine knowledge base oluştur. Exergy maliyetleme ve ekipman optimizasyonu.

---

## 🎯 OTONOM YETKİ

Bu brief'i uygularken:
1. **Çok derin araştırma yap** — SPECO metodu, exergy costing, Tsatsaronis metodolojisi
2. Mevcut proje yapısını incele (`/home/ubuntu/exergy-lab/`)
3. Mevcut factory ve exergy knowledge dosyalarını referans al
4. Eksik gördüğün bilgileri kendi insiyatifinle ekle
5. Sayısal örnekler mutlaka dahil et

---

## 📋 NEDEN ÖNEMLİ?

**Klasik analiz:** "Kazan exergy yıkımı 1500 kW" (fiziksel bilgi)
**Exergoekonomik:** "Kazan exergy yıkımının maliyeti €180,000/yıl, ama kazanın yatırım maliyeti €50,000/yıl (amortisman). Daha verimli kazan €80,000 ama yıllık exergy maliyeti €120,000'e düşer → Net tasarruf €30,000/yıl" (KARAR bilgisi)

Exergoekonomik analiz, termodinamik ve ekonomiyi birleştirerek **optimum yatırım kararı** verir.

---

## 📋 BÖLÜM 1: Araştırma Konuları

### 1.1 SPECO Metodu (Specific Exergy Costing)

Tsatsaronis'in geliştirdiği sistematik metodoloji:

```
Adım 1: Exergy Analizi
- Her akışkan için exergy hesapla
- Her ekipman için exergy dengesi kur

Adım 2: Ekonomik Analiz
- Ekipman yatırım maliyetleri
- İşletme ve bakım maliyetleri
- Amortisman ve sermaye maliyeti

Adım 3: Exergoekonomik Denge
Her ekipman k için:
Ċ_P,k = Ċ_F,k + Ż_k

Burada:
Ċ_P,k = Ürün exergy maliyet akışı (€/h)
Ċ_F,k = Yakıt exergy maliyet akışı (€/h)
Ż_k = Ekipman sermaye + O&M maliyeti akışı (€/h)

Adım 4: Exergoekonomik Değişkenler
c_P,k = Ürün birim exergy maliyeti (€/GJ veya €/kWh)
c_F,k = Yakıt birim exergy maliyeti (€/GJ)
Ċ_D,k = c_F,k × İ_k = Exergy yıkım maliyeti (€/h)
r_k = (c_P - c_F) / c_F = Göreli maliyet farkı
f_k = Ż_k / (Ż_k + Ċ_D,k) = Exergoekonomik faktör
```

### 1.2 Yakıt-Ürün Tanımları

```
Ekipman            | Yakıt (F)                    | Ürün (P)
-------------------|------------------------------|---------------------------
Kompresör          | W_elektrik                   | Ex_out - Ex_in (hava)
Türbin             | Ex_in - Ex_out (buhar)       | W_mekanik
Kazan              | Ex_yakıt                     | Ex_buhar - Ex_besleme_suyu
Eşanjör (ısıtma)  | Ex_hot_in - Ex_hot_out       | Ex_cold_out - Ex_cold_in
Pompa              | W_elektrik                   | Ex_out - Ex_in (sıvı)
Chiller            | W_kompresör                  | Ex_cold_out - Ex_cold_in
```

### 1.3 Ekipman Maliyet Fonksiyonları

```
Genel form:
Z_PEC = f(kapasite, verim, malzeme, basınç, sıcaklık)

Kompresör:
Z = C₁ × (W_kW)^α × (η_s / (1 - η_s))^β
Tipik: Z = 71.1 × W^0.9 × (0.9 - η_s)^(-1)

Kazan:
Z = C₁ × (Q_kW)^α
Tipik: Z = 130 × (A/0.093)^0.78

Isı eşanjörü:
Z = C₁ × (A_m²)^α
Shell&tube: Z = 8000 + 259 × A^0.81
Plakalı: Z = 4500 + 310 × A^0.65

Türbin:
Z = C₁ × (W_kW)^α × exp(T_in × β)

Pompa:
Z = C₁ × (W_kW)^α × (η / (1-η))^β

CEPCI düzeltmesi:
Z_güncel = Z_referans × (CEPCI_güncel / CEPCI_referans)
```

### 1.4 Sermaye Maliyeti Hesaplama (Levelized Cost)

```
Yıllık sermaye maliyeti:
Ż_CI = Z_PEC × CRF × φ / (N × 3600)  [€/s]

CRF (Capital Recovery Factor):
CRF = i × (1+i)^n / ((1+i)^n - 1)

Burada:
i = faiz oranı (WACC)
n = ekonomik ömür (yıl)
φ = bakım faktörü (tipik 1.06)
N = yıllık çalışma saati

Örnek:
Z_PEC = €100,000
i = 10%, n = 20 yıl
CRF = 0.1175
φ = 1.06
N = 7000 saat

Ż_CI = 100,000 × 0.1175 × 1.06 / (7000 × 3600)
     = €0.000494/s = €1.78/h = €12,454/yıl
```

### 1.5 Exergoekonomik Değerlendirme Kriterleri

```
1. Exergoekonomik faktör (f_k):
   f_k = Ż_k / (Ż_k + Ċ_D,k + Ċ_L,k)

   f_k < 0.25 → Yıkım maliyeti baskın → Ekipmanı iyileştir (daha verimli)
   0.25 < f_k < 0.70 → Dengeli
   f_k > 0.70 → Yatırım maliyeti baskın → Daha ucuz ekipman kullan

2. Göreli maliyet farkı (r_k):
   r_k = (c_P,k - c_F,k) / c_F,k

   Yüksek r_k → Bu ekipman ürün maliyetini çok artırıyor
   → İyileştirme önceliği yüksek

3. Exergy yıkım maliyeti (Ċ_D,k):
   Ċ_D,k = c_F,k × İ_D,k

   Yüksek Ċ_D,k → Para burada kaybediliyor
```

### 1.6 İleri Exergoekonomik Analiz

Kaçınılabilir/kaçınılamaz ayrımını maliyete uygulama:

```
Ċ_D,k = Ċ_D,k_AV + Ċ_D,k_UN

Ż_k = Ż_k_AV + Ż_k_UN

Gerçek optimizasyon potansiyeli:
f_k_AV = Ż_k_AV / (Ż_k_AV + Ċ_D,k_AV)

Sadece kaçınılabilir maliyetlere bakarak karar ver!
```

---

## 📋 BÖLÜM 2: Knowledge Base Oluşturma

### 2.1 Dizin Yapısı

```
knowledge/factory/exergoeconomic/
├── INDEX.md
├── overview.md                # Exergoekonomik analiz genel bakış
├── speco_method.md            # SPECO metodu detay
├── fuel_product_definitions.md # Yakıt-Ürün tanımları
├── cost_equations.md          # Ekipman maliyet fonksiyonları
├── levelized_cost.md          # Sermaye maliyeti hesaplama
├── exergoeconomic_balance.md  # Exergoekonomik denge denklemi
├── evaluation_criteria.md     # f_k, r_k, Ċ_D değerlendirme
├── advanced_exergoeconomic.md # İleri exergoekonomik (AV/UN)
├── cost_databases.md          # Maliyet veri tabanları (CEPCI, endeks)
├── matrix_formulation.md      # Matris formülasyonu (büyük sistemler)
├── auxiliary_equations.md     # Yardımcı denklemler (F/P kuralları)
├── optimization.md            # Exergoekonomik optimizasyon
├── sensitivity_analysis.md    # Duyarlılık analizi
├── worked_examples/
│   ├── simple_cycle.md        # Basit çevrim örneği
│   ├── cogeneration.md        # Kojenerasyon örneği
│   └── industrial_plant.md    # Endüstriyel tesis örneği
└── case_studies.md            # Akademik vaka çalışmaları
```

### 2.2 Dosya Kuralları

- YAML frontmatter
- **Detaylı formüller** (her adım açık)
- **Sayısal örnekler** (worked examples dizininde detaylı)
- **Tablo formatında maliyet veri tabanları**
- Minimum 200 satır
- Akademik referanslar

---

## 📋 BÖLÜM 3: Skill Dosyası

**Dosya:** `/skills/factory/economic_advisor.md` (mevcut güncelle veya yeni oluştur)

```
Exergoekonomik değerlendirme kuralları:

1. f_k < 0.25 → "Exergy yıkım maliyeti baskın, ekipman verimliliğini artır"
2. f_k > 0.70 → "Yatırım maliyeti baskın, daha ekonomik ekipman düşün"
3. Yüksek r_k → "Bu ekipman ürün maliyetini önemli ölçüde artırıyor"
4. Yüksek Ċ_D → "Burada para kaybediliyor — iyileştirme önceliği yüksek"
```

---

## 📋 BÖLÜM 4: Araştırma Kaynakları

### Temel Akademik (MUTLAKA İNCELE)
- **Tsatsaronis, G.** "Thermoeconomic analysis and optimization of energy systems" (1993)
- **Lazzaretto, A., Tsatsaronis, G.** "SPECO: A systematic and general methodology for calculating efficiencies and costs in thermal systems" (2006)
- **Bejan, A., Tsatsaronis, G., Moran, M.** "Thermal Design and Optimization" (Wiley, 1996) — KİTAP
- **Tsatsaronis, G., Morosuk, T.** "Advanced exergoeconomic evaluation and its application" (2014)

### İleri
- Erlach, B. "Combined exergoeconomic and exergoenvironmental analysis"
- Petrakopoulou, F. "Comparative thermodynamic and exergoeconomic studies"
- CEPCI (Chemical Engineering Plant Cost Index) verileri

---

## ✅ Tamamlama Kontrol Listesi

- [ ] knowledge/factory/exergoeconomic/ dizini oluşturuldu (~17 dosya)
- [ ] Her dosya minimum 200 satır
- [ ] SPECO metodu tam açıklanmış
- [ ] Ekipman maliyet fonksiyonları dahil
- [ ] 3+ worked example var
- [ ] Skills güncellendi
- [ ] Cross-reference'lar kuruldu
- [ ] Commit ve push yapıldı

**Hedef: ~17 dosya, her biri minimum 200 satır, akademik derinlikte.**
