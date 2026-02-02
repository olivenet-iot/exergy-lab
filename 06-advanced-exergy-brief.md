# ExergyLab Brief: İleri Exergy Analizi (Advanced Exergy Analysis)

> **Claude Code için:** Bu brief kapsamında ileri exergy analizi (advanced exergy analysis) için derinlemesine knowledge base oluştur. Bu ExergyLab'ın en önemli farklılaştırıcı özelliği olacak.

---

## 🎯 OTONOM YETKİ

Bu brief'i uygularken:
1. **Çok derin araştırma yap** — Bu konu ExergyLab'ın temel farklılaştırıcısı
2. Akademik kaynakları detaylı incele (Tsatsaronis, Morosuk, Bejan)
3. Mevcut proje yapısını incele (`/home/ubuntu/exergy-lab/`)
4. Mevcut `knowledge/factory/exergy_fundamentals.md` dosyasını referans al
5. Mevcut `skills/core/exergy_fundamentals.md` dosyasını zenginleştir
6. Yeni kavramları mevcut analiz sistemine entegre et

---

## 📋 NEDEN ÖNEMLİ?

**Klasik exergy analizi:** "Kazanın exergy verimi %32"
**İleri exergy analizi:** "Kazanın exergy yıkımının %65'i KAÇINILAMAZ (yanma irreversibility), ama %35'i KAÇINILABİLİR (economizer, hava ön ısıtma). Kaçınılabilir kısmın %80'i ENDOJEN (kazanın kendisi), %20'si EKZOJEN (diğer ekipmanlardan kaynaklanan)."

**Bu bilgi neden değerli?**
- Hangi ekipmana yatırım yapılmalı → kaçınılabilir exergy'si yüksek olan
- Hangi iyileştirme gerçekçi → kaçınılamaz kısım zaten yapılamaz
- Ekipmanlar arası etkileşim → ekzojen yıkım cross-equipment optimizasyonu

---

## 📋 BÖLÜM 1: Araştırma Konuları

### 1.1 Kaçınılabilir vs Kaçınılamaz (Avoidable / Unavoidable)

```
Geleneksel exergy yıkımı:
I_total = I_avoidable + I_unavoidable

Kaçınılamaz (Unavoidable):
- Teknolojik ve ekonomik sınırlar dahilinde azaltılamayan yıkım
- "İdeal ama gerçekçi" çalışma koşullarında bile oluşacak yıkım
- Termodinamiğin 2. yasasının kaçınılamaz sonucu

Kaçınılabilir (Avoidable):
- Mevcut teknolojiyle azaltılabilecek yıkım
- İyileştirme potansiyelini gösterir
- YATIRIM KARARI için temel bilgi
```

**Her ekipman için kaçınılamaz exergy yıkımı tahmini:**

```
Kompresör:
- Kaçınılamaz: İzentropik verim üst sınırı (%92-95)
- Kaçınılabilir: Mevcut verim ile üst sınır arasındaki fark

Kazan (yanma):
- Kaçınılamaz: Yanma irreversibility (~%25-30 exergy girdisinin)
  → Doğalgaz yanmasının termodinamik sınırı
  → Adiabatik alev sıcaklığı vs buhar sıcaklığı farkı
- Kaçınılabilir: Baca gazı kaybı, fazla hava, izolasyon

Isı eşanjörü:
- Kaçınılamaz: Minimum ΔT_min (~5-10°C) gerektiren yıkım
- Kaçınılabilir: Fouling, aşırı ΔT, tasarım hataları

Pompa:
- Kaçınılamaz: Hidrolik kayıplar minimum seviyede (%85-90)
- Kaçınılabilir: Throttle, aşırı boyut, eski motor
```

### 1.2 Endojen vs Ekzojen (Endogenous / Exogenous)

```
I_total = I_endogenous + I_exogenous

Endojen (Endogenous):
- Ekipmanın KENDİ iç irreversibility'sinden kaynaklanan
- Diğer ekipmanlar ideal çalışsa bile bu ekipmanda oluşacak yıkım
- Ekipman tasarımı/işletmesine bağlı

Ekzojen (Exogenous):
- DİĞER ekipmanlardaki yetersizliklerden kaynaklanan
- Bu ekipman ideal olsa bile, besleme koşulları kötüyse oluşan yıkım
- SİSTEM OPTİMİZASYONU için kritik bilgi
```

**Örnek:**
```
Kazan besleme suyu pompası düşük verimli çalışıyor:
→ Pompa daha sıcak su veriyor (sürtünme ısısı)
→ Ama pompa debisi yetersiz olabilir
→ Kazan besleme suyu sıcaklığı düşük
→ Kazan baca gazı sıcaklığı yükseliyor
→ Kazandaki ek exergy yıkımı = EKZOJEN (pompadan kaynaklanan)
```

### 1.3 Dörtlü Ayrıştırma (4-Way Splitting)

```
I_total = I_EN_AV + I_EN_UN + I_EX_AV + I_EX_UN

I_EN_AV: Endojen-Kaçınılabilir → BU EKİPMANI İYİLEŞTİR
I_EN_UN: Endojen-Kaçınılamaz → Yapılacak bir şey yok
I_EX_AV: Ekzojen-Kaçınılabilir → DİĞER EKİPMANI İYİLEŞTİR
I_EX_UN: Ekzojen-Kaçınılamaz → Yapılacak bir şey yok

GERÇEK İYİLEŞTİRME POTANSİYELİ = I_EN_AV + I_EX_AV
```

### 1.4 Hesaplama Metodolojisi

```
Adım 1: Gerçek Analiz (Real Analysis)
- Gerçek çalışma koşullarında tüm ekipmanları analiz et
- Her ekipman için I_total hesapla

Adım 2: Kaçınılamaz Koşullar Belirleme
- Her ekipman için "en iyi teknolojik/ekonomik" parametreleri belirle
  Örnek kazan: η_max = 95%, baca gazı min = 130°C
  Örnek kompresör: η_s_max = 92%, ΔP_min = ...
  Örnek eşanjör: ΔT_min = 5°C, ΔP_min = ...

Adım 3: Endojen Hesaplama
- Her ekipmanı teker teker "gerçek" koşulda çalıştır
- Diğer tüm ekipmanları "ideal" koşulda çalıştır
- Bu ekipmandaki yıkım = endojen yıkım

Adım 4: Dörtlü Ayrıştırma
- I_UN hesapla (unavoidable koşullarda)
- I_EN hesapla (endogenous koşullarda)
- I_EN_UN = Endojen + Kaçınılamaz koşullarda
- I_EN_AV = I_EN - I_EN_UN
- I_EX_AV = I_AV - I_EN_AV
- I_EX_UN = I_UN - I_EN_UN
```

### 1.5 Analiz Sonuçlarının Yorumlanması

```
Önceliklendirme:
1. I_EN_AV yüksek olan ekipman → Kendi iyileştirmesi öncelikli
2. I_EX_AV yüksek olan ekipman → Besleyen ekipmanı iyileştir
3. I_EN_UN + I_EX_UN yüksek → Yapısal sınır, mevcut teknolojiyle çözülemez
```

### 1.6 İleri Exergy Metotları

- **Exergy wheel:** Görselleştirme aracı
- **Functional exergy efficiency:** Ürün/yakıt tanımları
- **Exergy destruction ratio:** y*_D,k = I_k / I_total
- **Relative avoidability:** I_AV / I_total oranı
- **Improvement priority number:** IPN = I_AV × cost_factor

---

## 📋 BÖLÜM 2: Knowledge Base Oluşturma

### 2.1 Yeni Dosyalar

```
knowledge/factory/advanced_exergy/
├── INDEX.md
├── overview.md                # İleri exergy analizi genel bakış
├── avoidable_unavoidable.md   # Kaçınılabilir vs kaçınılamaz
├── endogenous_exogenous.md    # Endojen vs ekzojen
├── four_way_splitting.md      # Dörtlü ayrıştırma
├── methodology.md             # Hesaplama metodolojisi (adım adım)
├── ideal_conditions.md        # İdeal/kaçınılamaz koşul tanımlama
├── equipment_specific/
│   ├── compressor_advanced.md # Kompresör ileri exergy
│   ├── boiler_advanced.md     # Kazan ileri exergy
│   ├── heat_exchanger_advanced.md # Eşanjör ileri exergy
│   ├── turbine_advanced.md    # Türbin ileri exergy
│   ├── pump_advanced.md       # Pompa ileri exergy
│   └── chiller_advanced.md    # Chiller ileri exergy
├── interpretation_guide.md    # Sonuç yorumlama rehberi
├── improvement_priority.md    # İyileştirme önceliklendirme
├── visualization.md           # Görselleştirme (exergy wheel, bar chart)
├── limitations.md             # Yöntemin sınırlamaları
└── case_studies.md            # Akademik vaka çalışmaları
```

### 2.2 Dosya Kuralları

- YAML frontmatter
- **Detaylı formüller** (code block içinde)
- **Sayısal örnekler** (her dosyada en az 1 worked example)
- **Her ekipman için ideal/kaçınılamaz parametre tabloları**
- Minimum 200 satır (bu çok detaylı bir konu)
- Akademik referanslar (Tsatsaronis grubu makaleleri)

---

## 📋 BÖLÜM 3: Skill Güncellemeleri

### 3.1 Core Skill

`/skills/core/exergy_fundamentals.md` dosyasına ileri exergy kavramlarını ekle:

```
İleri exergy analizi kullanılabilir koşullar:
1. Fabrika analizi (3+ ekipman)
2. Cross-equipment optimizasyon
3. Yatırım önceliklendirme

Yorum kuralları:
- Kaçınılabilir exergy yıkımı > toplam yıkımın %30'u ise → "Önemli iyileştirme potansiyeli"
- Ekzojen yıkım > %20 ise → "Sistem seviyesi optimizasyon gerekli"
- Endojen-kaçınılamaz > %60 ise → "Ekipman değişimi düşünülmeli"
```

### 3.2 Equipment Skills

Her ekipman skill'ine kaçınılabilir/kaçınılamaz referans değerleri ekle.

### 3.3 Factory Skills

Factory analyst skill'ine dörtlü ayrıştırma bazlı önceliklendirme ekle.

---

## 📋 BÖLÜM 4: Araştırma Kaynakları

### Temel Akademik (MUTLAKA İNCELE)
- **Tsatsaronis, G., Morosuk, T.** "Advanced exergy-based methods used to understand and improve energy-conversion systems" (2016)
- **Tsatsaronis, G.** "Definitions and nomenclature in exergy analysis and exergoeconomics" (2007)
- **Kelly, S., Tsatsaronis, G., Morosuk, T.** "Advanced exergetic analysis: Approaches for splitting the exergy destruction" (2009)
- **Morosuk, T., Tsatsaronis, G.** "Advanced exergy-based analyses applied to a system of an air-conditioning machine" (2011)
- **Petrakopoulou, F., Tsatsaronis, G., Morosuk, T., Carassai, A.** "Conventional and advanced exergetic analyses applied to a combined cycle power plant" (2012)

### İleri Kaynak
- Bejan, A. "Advanced Engineering Thermodynamics"
- Szargut, J. "Exergy Method: Technical and Ecological Applications"
- Dincer, I., Rosen, M. "Exergy: Energy, Environment and Sustainable Development"

---

## ✅ Tamamlama Kontrol Listesi

- [ ] knowledge/factory/advanced_exergy/ dizini oluşturuldu (~18 dosya)
- [ ] Her dosya minimum 200 satır
- [ ] Dörtlü ayrıştırma metodolojisi tam açıklanmış
- [ ] Her ekipman için ideal koşul tablosu var
- [ ] Sayısal örnekler dahil (en az 3 worked example)
- [ ] Skills güncellendi (core + equipment + factory)
- [ ] Cross-reference'lar kuruldu
- [ ] Commit ve push yapıldı

**Hedef: ~18 dosya, her biri minimum 200 satır, akademik derinlikte. Bu ExergyLab'ın TEMEL farklılaştırıcısı.**
