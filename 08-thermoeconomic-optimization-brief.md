# ExergyLab Brief: Termoekonomik Optimizasyon (Thermoeconomic Optimization)

> **Claude Code için:** Bu brief kapsamında termoekonomik optimizasyon yöntemleri için derinlemesine knowledge base oluştur. Maliyet-verim dengesi optimizasyonu.

---

## 🎯 OTONOM YETKİ

Bu brief'i uygularken:
1. **Derin araştırma yap** — Akademik kaynaklar, optimizasyon teorisi, endüstri uygulamaları
2. Mevcut proje yapısını incele (`/home/ubuntu/exergy-lab/`)
3. İleri exergy ve exergoekonomik bilgilerle entegre et
4. Eksik gördüğün bilgileri kendi insiyatifinle ekle
5. Pratik optimizasyon örnekleri mutlaka dahil et

---

## 📋 NEDEN ÖNEMLİ?

**Sorun:** Verimli ekipman pahalı, ucuz ekipman verimsiz. Optimum nerede?

```
Yüksek verimli kazan:
  Yatırım: €200,000
  Exergy yıkımı: 500 kW → Maliyet: €30,000/yıl
  Toplam: €53,500/yıl (amortisman dahil)

Düşük verimli kazan:
  Yatırım: €80,000
  Exergy yıkımı: 1500 kW → Maliyet: €90,000/yıl
  Toplam: €99,400/yıl (amortisman dahil)

Optimum kazan: → ARADA BİR YERDE
  Yatırım: €130,000
  Exergy yıkımı: 800 kW → Maliyet: €48,000/yıl
  Toplam: €63,300/yıl ← MİNİMUM
```

Termoekonomik optimizasyon bu **minimum toplam maliyet noktasını** bulur.

---

## 📋 BÖLÜM 1: Araştırma Konuları

### 1.1 Optimizasyon Temelleri

- **Amaç fonksiyonu:** Minimize C_total = C_fuel + C_investment + C_O&M
- **Karar değişkenleri:** Ekipman verimlilikleri, sıcaklıklar, basınçlar, debiler
- **Kısıtlar:** Termodinamik sınırlar, kapasite gereksinimleri, çevresel limitler
- **Trade-off:** Verim ↑ → Yatırım ↑ ama Yakıt ↓

### 1.2 Termoekonomik Optimizasyon Yöntemleri

#### A) Iteratif Exergoekonomik Yöntem (Tsatsaronis)
```
1. Başlangıç tasarımı yap
2. Exergoekonomik analiz yap
3. f_k ve r_k değerlerini değerlendir
4. Ekipmanları sırala (Ċ_D + Ż büyükten küçüğe)
5. En yüksek maliyetli ekipmanı iyileştir:
   - f_k düşük → Verim artır
   - f_k yüksek → Maliyet düşür
6. Tekrar 2'ye dön, toplam maliyet düşmüyorsa dur
```

#### B) Yapısal Optimizasyon
```
- Süper yapı (superstructure) tanımla
- Tüm olası konfigürasyonları dahil et
- MINLP (Mixed Integer Non-Linear Programming) ile çöz
- En ucuz yapıyı bul
```

#### C) Parametrik Optimizasyon
```
- Yapı sabit, parametreleri optimize et
- Karar değişkenleri: T, P, η, debiler
- NLP (Non-Linear Programming) ile çöz
- Gradient-based veya evolutionary algoritma
```

#### D) Multi-Objective Optimizasyon
```
- Amaç 1: Toplam maliyet minimize
- Amaç 2: Exergy verimi maximize
- Amaç 3: CO₂ emisyonu minimize
- Pareto front oluştur
- Karar verici optimum noktayı seçer
```

### 1.3 Matematiksel Formülasyon

```
Amaç:
min C_total = Σ(Ż_k) + Σ(c_F,k × İ_D,k) + C_fuel_total

Kısıtlar:
- Kütle dengesi: Σm_in = Σm_out (her düğümde)
- Enerji dengesi: Q - W = Σ(m×h)_out - Σ(m×h)_in
- Exergy dengesi: Ex_F = Ex_P + İ_D + Ex_L
- Termodinamik: η < η_max, T > T_min, P < P_max
- Kapasite: Q_demand = Q_supply
- Ekonomik: Yatırım < Bütçe

Karar değişkenleri (örnek CHP sistemi):
x = [P_boiler, T_superheater, P_extraction, P_condenser, η_turbine, ...]

Kısıt:
g(x) ≤ 0  (eşitsizlik kısıtları)
h(x) = 0  (eşitlik kısıtları)
x_L ≤ x ≤ x_U  (sınırlar)
```

### 1.4 Optimizasyon Algoritmaları

```
Gradient-Based:
- SQP (Sequential Quadratic Programming)
- Interior Point
- Avantaj: Hızlı yakınsama
- Dezavantaj: Lokal optimum riski

Evolutionary:
- Genetik Algoritma (GA)
- Particle Swarm Optimization (PSO)
- Differential Evolution (DE)
- NSGA-II (multi-objective)
- Avantaj: Global optimum bulma şansı
- Dezavantaj: Yavaş

Hibrit:
- GA + SQP kombinasyonu
- İlk GA ile bölge bul, sonra SQP ile hassas optimum
```

### 1.5 Duyarlılık Analizi

```
Parametrik duyarlılık:
∂C_total / ∂x_i = ? (her karar değişkeni için)

Senaryo analizi:
- Yakıt fiyatı %20 artarsa → Optimum nasıl değişir?
- Faiz oranı %5 → %15 aralığında
- Çalışma saati 4000 → 8000 saat
- CO₂ vergisi eklenmesi

Break-even analizi:
- Hangi yakıt fiyatında CHP fizibıl?
- Hangi çalışma saatinde VSD fizibıl?
```

### 1.6 Pratik Uygulama Rehberi

```
Endüstriyel optimizasyon adımları:

1. Mevcut sistem tanımlama
   - Ekipman listesi ve parametreleri
   - Enerji tüketimi verileri
   - Maliyet verileri

2. Exergoekonomik analiz (mevcut durum)
   - Her ekipman için f_k, r_k, Ċ_D

3. İyileştirme fırsatları belirleme
   - Yüksek Ċ_D + Ż ekipmanlar
   - Trade-off analizi

4. Optimizasyon
   - Karar değişkenlerini tanımla
   - Kısıtları belirle
   - Çöz (yazılım veya iteratif)

5. Duyarlılık analizi
   - Sonuçların robustluğunu kontrol et

6. Uygulama planı
   - Optimum tasarıma yaklaşma adımları
```

---

## 📋 BÖLÜM 2: Knowledge Base Oluşturma

### 2.1 Dizin Yapısı

```
knowledge/factory/thermoeconomic_optimization/
├── INDEX.md
├── overview.md                # Termoekonomik optimizasyon genel bakış
├── objective_functions.md     # Amaç fonksiyonları
├── decision_variables.md      # Karar değişkenleri ve kısıtlar
├── iterative_method.md        # Tsatsaronis iteratif yöntem
├── structural_optimization.md # Yapısal optimizasyon (süperyapı)
├── parametric_optimization.md # Parametrik optimizasyon
├── multi_objective.md         # Çok amaçlı optimizasyon (Pareto)
├── algorithms.md              # Optimizasyon algoritmaları
├── sensitivity_analysis.md    # Duyarlılık ve senaryo analizi
├── practical_guide.md         # Endüstriyel uygulama rehberi
├── trade_off_curves.md        # Verim-maliyet trade-off eğrileri
├── worked_examples/
│   ├── boiler_optimization.md # Kazan optimizasyonu örneği
│   ├── chp_optimization.md    # CHP optimizasyonu örneği
│   └── factory_optimization.md # Fabrika optimizasyonu örneği
└── case_studies.md            # Akademik ve endüstriyel vakalar
```

### 2.2 Dosya Kuralları

- YAML frontmatter
- Detaylı matematiksel formülasyonlar
- Sayısal örnekler (worked examples)
- Trade-off grafikleri açıklamaları
- Minimum 200 satır
- Cross-reference: exergoeconomic/, advanced_exergy/ dosyalarıyla

---

## 📋 BÖLÜM 3: Skill Güncelleme

Factory analyst ve economic advisor skill'lerine optimizasyon tavsiyeleri ekle:

```
Optimizasyon önerisi koşulları:
1. f_k değerleri dengesiz (çok düşük veya çok yüksek)
2. Toplam maliyet > €100,000/yıl
3. Birden fazla iyileştirme seçeneği var
4. Trade-off açık değil

→ "Termoekonomik optimizasyon ile minimum toplam maliyet noktası belirlenebilir"
```

---

## 📋 BÖLÜM 4: Araştırma Kaynakları

### Temel
- **Bejan, A., Tsatsaronis, G., Moran, M.** "Thermal Design and Optimization"
- **El-Sayed, Y.M.** "The Thermoeconomics of Energy Conversions"
- **Erlach, B., Serra, L., Valero, A.** "Structural theory as standard for thermoeconomics"
- **Lozano, M.A., Valero, A.** "Theory of the exergetic cost"

### Optimizasyon
- Deb, K. "Multi-Objective Optimization using Evolutionary Algorithms" (NSGA-II)
- Boyd, S. "Convex Optimization" (matematiksel temel)

---

## ✅ Tamamlama Kontrol Listesi

- [ ] knowledge/factory/thermoeconomic_optimization/ dizini (~15 dosya)
- [ ] Her dosya minimum 200 satır
- [ ] 3+ worked example var
- [ ] Trade-off analizi örnekleri dahil
- [ ] Skills güncellendi
- [ ] Cross-reference'lar kuruldu
- [ ] Commit ve push yapıldı

**Hedef: ~15 dosya, her biri minimum 200 satır, akademik + pratik derinlikte.**
