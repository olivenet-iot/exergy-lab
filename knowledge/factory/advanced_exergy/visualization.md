---
title: "Gelişmiş Exergy Analizi — Görselleştirme Yöntemleri"
category: factory/advanced_exergy
keywords:
  - exergy wheel
  - stacked bar chart
  - waterfall chart
  - grassmann diyagramı
  - radar chart
  - heatmap
  - görselleştirme
  - kaçınılabilir exergy yıkımı
  - endojen ekzojen
related_files:
  - knowledge/factory/advanced_exergy/splitting.md
  - knowledge/factory/advanced_exergy/interactions.md
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/prioritization.md
  - engine/sankey.py
  - frontend/src/components/SankeyDiagram.jsx
use_when: "Gelişmiş exergy analizi sonuçlarını görselleştirmek, karar vericilere sunmak veya frontend bileşenleri tasarlamak gerektiğinde"
priority: high
last_updated: 2025-05-15
---

# Gelişmiş Exergy Analizi — Görselleştirme Yöntemleri

Gelişmiş exergy analizinin ürettiği dört yollu ayrıştırma (endojen-kaçınılabilir, endojen-kaçınılamaz, ekzojen-kaçınılabilir, ekzojen-kaçınılamaz) sonuçlarının etkili bir şekilde görselleştirilmesi, mühendislik kararlarının hızlı ve doğru alınmasını sağlar. Bu dosya, ExergyLab platformunda kullanılabilecek tüm görselleştirme yöntemlerini, veri formatlarını ve uygulama detaylarını kapsar.

## 1. Renk Kodlama Standardı (Color Coding Standard)

Tüm görselleştirmelerde tutarlılık sağlamak için aşağıdaki renk paleti kullanılır:

| Kategori | Kod | Renk | HEX | Anlamı |
|----------|-----|------|-----|--------|
| I_EN_AV | Endojen-Kaçınılabilir | Kırmızı | `#DC2626` | Bileşenin kendisinde iyileştirilebilir |
| I_EX_AV | Ekzojen-Kaçınılabilir | Turuncu | `#F97316` | Sistem etkileşimiyle iyileştirilebilir |
| I_EN_UN | Endojen-Kaçınılamaz | Koyu gri | `#6B7280` | Bileşen teknoloji limiti |
| I_EX_UN | Ekzojen-Kaçınılamaz | Açık gri | `#D1D5DB` | Sistem yapısal limiti |

> **Kural:** Kırmızı her zaman "aksiyon gerekli" anlamına gelir. Gri tonları "mevcut teknoloji ile değiştirilemez" anlamındadır. Turuncu "başka bileşeni iyileştirerek azaltılabilir" mesajını verir.

## 2. Exergy Wheel Diyagramı (Exergy Wheel Diagram)

### 2.1 Kavram

Exergy Wheel, dairesel bir diyagramdır. Her bileşen (kompresör, kazan, chiller, pompa vb.) bir dilim olarak temsil edilir. İç çember kaçınılamaz exergy yıkımını, dış çember ise kaçınılabilir exergy yıkımını gösterir. Bu sayede hem bileşenler arası karşılaştırma hem de her bileşenin iç yapısı tek bir görselde sunulur.

### 2.2 Yapı

```
              Exergy Wheel — Fabrika Toplamı

                    Kazan
                  ╱────────╲
               ╱   I_EN_UN    ╲
            ╱   ┌────────────┐   ╲
         ╱      │  I_EN_AV   │      ╲
Pompa  ╱   ─────┤            ├─────   ╲  Kompresör
       ╲        │  I_EX_AV   │        ╱
         ╲      └────────────┘      ╱
            ╲   I_EX_UN           ╱
               ╲                ╱
                  ╲────────╱
                    Chiller

  İç Çember: Kaçınılamaz (UN) — Gri tonları
  Dış Çember: Kaçınılabilir (AV) — Kırmızı/Turuncu
```

### 2.3 Tek Bileşen Wheel Detayı

Her bileşen için ayrı bir wheel oluşturulabilir:

```
        ┌──────────────┐
       │   I_EN_UN     │  (Koyu gri — kaçınılamaz, endojen)
      ┌┤              ├┐
     │ │   I_EN_AV    │ │ (Kırmızı — kaçınılabilir, endojen)
     │ ├──────────────┤ │
     │ │   I_EX_AV    │ │ (Turuncu — kaçınılabilir, ekzojen)
      └┤              ├┘
       │   I_EX_UN     │  (Açık gri — kaçınılamaz, ekzojen)
        └──────────────┘
```

### 2.4 Sayısal Örnek

Bir buhar kazanı için gelişmiş exergy analizi sonuçları:

```
Toplam exergy yıkımı (I_total) = 850 kW

I_EN_UN = 340 kW  (%40.0)  →  İç çember, koyu gri dilim
I_EN_AV = 255 kW  (%30.0)  →  Dış çember, kırmızı dilim
I_EX_AV = 127.5 kW (%15.0) →  Dış çember, turuncu dilim
I_EX_UN = 127.5 kW (%15.0) →  İç çember, açık gri dilim

Wheel açıları (360° üzerinden):
  I_EN_UN dilimi: 0°   — 144°  (144°)
  I_EN_AV dilimi: 144° — 252°  (108°)
  I_EX_AV dilimi: 252° — 306°  (54°)
  I_EX_UN dilimi: 306° — 360°  (54°)
```

### 2.5 Veri Formatı

```json
{
  "chart_type": "exergy_wheel",
  "component": "boiler_01",
  "unit": "kW",
  "segments": [
    { "category": "I_EN_UN", "value": 340, "color": "#6B7280", "label": "Endojen Kaçınılamaz" },
    { "category": "I_EN_AV", "value": 255, "color": "#DC2626", "label": "Endojen Kaçınılabilir" },
    { "category": "I_EX_AV", "value": 127.5, "color": "#F97316", "label": "Ekzojen Kaçınılabilir" },
    { "category": "I_EX_UN", "value": 127.5, "color": "#D1D5DB", "label": "Ekzojen Kaçınılamaz" }
  ],
  "total_destruction": 850
}
```

## 3. Stacked Bar Chart (4-Yollu Renk Kodlaması)

### 3.1 Kavram

Yatay veya dikey çubuk grafik ile tüm bileşenlerin exergy yıkım dağılımını yan yana karşılaştırma imkanı sağlar. Her çubuk dört renkli bölüme ayrılır.

### 3.2 Eksen Düzeni

- **X ekseni:** Bileşenler (kompresör, kazan, chiller, pompa vb.)
- **Y ekseni:** Exergy yıkımı (kW)
- **Çubuk katmanları (alttan üste):**
  1. Kırmızı (`#DC2626`): I_EN_AV — Endojen kaçınılabilir (en altta, aksiyon gerekli)
  2. Turuncu (`#F97316`): I_EX_AV — Ekzojen kaçınılabilir (sistem etkileşimi)
  3. Koyu gri (`#6B7280`): I_EN_UN — Endojen kaçınılamaz (bileşen limiti)
  4. Açık gri (`#D1D5DB`): I_EX_UN — Ekzojen kaçınılamaz (sistem limiti)

> **Tasarım Kararı:** I_EN_AV en alta yerleştirilir çünkü karar vericinin ilk göreceği ve en çok ilgileneceği kategoridir. Aksiyon alınabilir değerler tabandan başlar.

### 3.3 Sayısal Örnek — Fabrika Karşılaştırması

| Bileşen | I_EN_AV (kW) | I_EX_AV (kW) | I_EN_UN (kW) | I_EX_UN (kW) | I_total (kW) |
|---------|---------------|---------------|---------------|---------------|---------------|
| Kazan | 255.0 | 127.5 | 340.0 | 127.5 | 850.0 |
| Kompresör | 45.0 | 22.5 | 90.0 | 22.5 | 180.0 |
| Chiller | 38.0 | 19.0 | 57.0 | 16.0 | 130.0 |
| Pompa | 8.0 | 4.0 | 18.0 | 5.0 | 35.0 |
| **Toplam** | **346.0** | **173.0** | **505.0** | **171.0** | **1195.0** |

```
Kaçınılabilir oran = (I_EN_AV + I_EX_AV) / I_total
                   = (346 + 173) / 1195
                   = 519 / 1195
                   = %43.4
```

Bu, fabrikadaki toplam exergy yıkımının %43.4'ünün iyileştirilebilir olduğu anlamına gelir.

### 3.4 Recharts Implementasyon Referansı

```jsx
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const COLORS = {
  I_EN_AV: '#DC2626',
  I_EX_AV: '#F97316',
  I_EN_UN: '#6B7280',
  I_EX_UN: '#D1D5DB'
};

const data = [
  { name: 'Kazan', I_EN_AV: 255, I_EX_AV: 127.5, I_EN_UN: 340, I_EX_UN: 127.5 },
  { name: 'Kompresör', I_EN_AV: 45, I_EX_AV: 22.5, I_EN_UN: 90, I_EX_UN: 22.5 },
  { name: 'Chiller', I_EN_AV: 38, I_EX_AV: 19, I_EN_UN: 57, I_EX_UN: 16 },
  { name: 'Pompa', I_EN_AV: 8, I_EX_AV: 4, I_EN_UN: 18, I_EX_UN: 5 }
];

<ResponsiveContainer width="100%" height={400}>
  <BarChart data={data}>
    <XAxis dataKey="name" />
    <YAxis label={{ value: 'Exergy Yıkımı (kW)', angle: -90 }} />
    <Tooltip />
    <Legend />
    <Bar dataKey="I_EN_AV" stackId="a" fill={COLORS.I_EN_AV} name="Endojen Kaçınılabilir" />
    <Bar dataKey="I_EX_AV" stackId="a" fill={COLORS.I_EX_AV} name="Ekzojen Kaçınılabilir" />
    <Bar dataKey="I_EN_UN" stackId="a" fill={COLORS.I_EN_UN} name="Endojen Kaçınılamaz" />
    <Bar dataKey="I_EX_UN" stackId="a" fill={COLORS.I_EX_UN} name="Ekzojen Kaçınılamaz" />
  </BarChart>
</ResponsiveContainer>
```

### 3.5 Veri Formatı (JSON Schema)

```json
{
  "chart_type": "stacked_bar",
  "unit": "kW",
  "components": [
    {
      "name": "string",
      "equipment_type": "boiler | compressor | chiller | pump",
      "I_EN_AV": "number",
      "I_EX_AV": "number",
      "I_EN_UN": "number",
      "I_EX_UN": "number"
    }
  ],
  "totals": {
    "I_EN_AV": "number",
    "I_EX_AV": "number",
    "I_EN_UN": "number",
    "I_EX_UN": "number"
  }
}
```

## 4. Waterfall Chart (Şelale Diyagramı)

### 4.1 Kavram

Waterfall chart, toplam exergy yıkımından başlayarak kaçınılamaz kısımları adım adım çıkarır ve gerçek iyileştirme potansiyelini ortaya koyar. Karar vericiye "elimdeki toplamdan ne kadarı gerçekten iyileştirilebilir" sorusunu görsel olarak yanıtlar.

### 4.2 Temel Akış

```
Başlangıç:  I_total = 1195 kW
  │
  ├─ Adım 1:  -I_EN_UN = -505 kW    (Bileşen teknoloji limitleri çıkar)
  │            Kalan: 690 kW
  │
  ├─ Adım 2:  -I_EX_UN = -171 kW    (Sistem yapısal limitleri çıkar)
  │            Kalan: 519 kW
  │
  ├─ Adım 3:  Sonuç → I_AV = 519 kW (Toplam kaçınılabilir yıkım)
  │
  ├─ Adım 4:  Ayrıştırma:
  │            I_EX_AV = 173 kW      (Sistem etkileşimi ile azaltılabilir)
  │            I_EN_AV = 346 kW      (Doğrudan bileşen iyileştirmesi)
  │
  └─ Son:     Öncelik sırası netleşir
```

### 4.3 Alternatif Detaylı Akış

Daha detaylı bir waterfall için bileşen bazlı adımlar eklenebilir:

```
I_total (1195 kW)
  │
  ├── -Kazan I_UN (467.5 kW)     → Kalan: 727.5 kW
  ├── -Kompresör I_UN (112.5 kW) → Kalan: 615.0 kW
  ├── -Chiller I_UN (73.0 kW)    → Kalan: 542.0 kW
  ├── -Pompa I_UN (23.0 kW)      → Kalan: 519.0 kW
  │
  = I_AV_total (519.0 kW)
  │
  ├── -Kazan I_AV (382.5 kW)     → Kalan: 136.5 kW
  ├── -Kompresör I_AV (67.5 kW)  → Kalan: 69.0 kW
  ├── -Chiller I_AV (57.0 kW)    → Kalan: 12.0 kW
  ├── -Pompa I_AV (12.0 kW)      → Kalan: 0.0 kW
  │
  = 0 kW (tüm yıkım hesaplanmış)
```

### 4.4 Renk Kodlama ve Etiketleme Kuralları

| Adım Türü | Renk | Çubuk Yönü | Etiket Formatı |
|-----------|------|-----------|----------------|
| Başlangıç değeri | Mavi (`#3B82F6`) | Yukarı | "Toplam: X kW" |
| Kaçınılamaz çıkarma | Gri (`#9CA3AF`) | Aşağı | "-I_UN: X kW" |
| Ara toplam | Sarı (`#EAB308`) | Yukarı | "Kaçınılabilir: X kW" |
| Ekzojen kaçınılabilir | Turuncu (`#F97316`) | Aşağı | "-I_EX_AV: X kW" |
| Endojen kaçınılabilir | Kırmızı (`#DC2626`) | Yukarı | "I_EN_AV: X kW" |

### 4.5 Veri Formatı

```json
{
  "chart_type": "waterfall",
  "unit": "kW",
  "steps": [
    { "label": "Toplam Exergy Yıkımı", "value": 1195, "type": "total", "color": "#3B82F6" },
    { "label": "Endojen Kaçınılamaz", "value": -505, "type": "subtract", "color": "#6B7280" },
    { "label": "Ekzojen Kaçınılamaz", "value": -171, "type": "subtract", "color": "#D1D5DB" },
    { "label": "Kaçınılabilir Toplam", "value": 519, "type": "subtotal", "color": "#EAB308" },
    { "label": "Ekzojen Kaçınılabilir", "value": -173, "type": "subtract", "color": "#F97316" },
    { "label": "Endojen Kaçınılabilir", "value": 346, "type": "result", "color": "#DC2626" }
  ]
}
```

## 5. Grassmann Diyagramı Uzantısı (Extended Grassmann/Sankey)

### 5.1 Kavram

ExergyLab'ın mevcut `engine/sankey.py` modülü, standart exergy Sankey diyagramı üretir. Gelişmiş exergy analizi sonuçları ile bu diyagramı zenginleştirmek, kaçınılabilir ve kaçınılamaz kayıpları akış diyagramı üzerinde görmek mümkün olur.

### 5.2 Mevcut Sankey Yapısı

```
Yakıt Exergysi (F) ───────────────────► Ürün Exergysi (P)
                     │
                     ├──► Exergy Yıkımı (I)
                     └──► Exergy Kaybı (L)
```

### 5.3 Gelişmiş Sankey Uzantısı

Kaçınılabilir/kaçınılamaz ayrıştırma ile zenginleştirilmiş akış:

```
Yakıt Exergysi (F) ══════════════════════════► Ürün Exergysi (P)
                     │
                     ├──►  I_EN_AV  ─── (Kırmızı düz ok)
                     ├──►  I_EX_AV  ─── (Turuncu düz ok)
                     ├─ ─► I_EN_UN  ─── (Koyu gri kesikli ok)
                     ├─ ─► I_EX_UN  ─── (Açık gri kesikli ok)
                     └──►  Exergy Kaybı (L)
```

### 5.4 Ok Stilleri

| Akış | Çizgi Stili | Renk | Kalınlık (px) |
|------|------------|------|---------------|
| Yakıt (F) | Düz | Mavi (`#3B82F6`) | Orantılı |
| Ürün (P) | Düz | Yeşil (`#22C55E`) | Orantılı |
| I_EN_AV | Düz | Kırmızı (`#DC2626`) | Orantılı |
| I_EX_AV | Düz | Turuncu (`#F97316`) | Orantılı |
| I_EN_UN | Kesikli (dashed) | Koyu gri (`#6B7280`) | Orantılı |
| I_EX_UN | Kesikli (dashed) | Açık gri (`#D1D5DB`) | Orantılı |
| Kayıp (L) | Noktalı (dotted) | Mor (`#A855F7`) | Orantılı |

### 5.5 ExergyLab Entegrasyon Önerisi

Mevcut `engine/sankey.py` dosyasındaki `generate_sankey_data()` fonksiyonuna ek parametre olarak `advanced=True` bayrağı eklenebilir:

```python
def generate_sankey_data(results: dict, advanced: bool = False) -> dict:
    """
    Sankey diyagramı verisi üretir.

    Args:
        results: Exergy analizi sonuçları
        advanced: True ise 4-yollu ayrıştırma ile zenginleştirilmiş veri

    Returns:
        Sankey node ve link verileri
    """
    base_data = _generate_base_sankey(results)

    if advanced and "splitting" in results:
        splitting = results["splitting"]
        base_data["links"].extend([
            {"source": "Fuel", "target": "I_EN_AV", "value": splitting["I_EN_AV"], "color": "#DC2626", "style": "solid"},
            {"source": "Fuel", "target": "I_EX_AV", "value": splitting["I_EX_AV"], "color": "#F97316", "style": "solid"},
            {"source": "Fuel", "target": "I_EN_UN", "value": splitting["I_EN_UN"], "color": "#6B7280", "style": "dashed"},
            {"source": "Fuel", "target": "I_EX_UN", "value": splitting["I_EX_UN"], "color": "#D1D5DB", "style": "dashed"},
        ])

    return base_data
```

## 6. Radar/Spider Chart (Performans Poligonu)

### 6.1 Kavram

Her ekipman için birden fazla gelişmiş exergy göstergesini tek bir çokgen üzerinde göstererek hızlı karşılaştırma sağlar. Çokgenin alanı büyükse iyileştirme potansiyeli yüksektir.

### 6.2 Eksenler (5 Boyut)

1. **theta (avoidability ratio):** Kaçınılabilir oran = I_AV / I_total

```
theta = (I_EN_AV + I_EX_AV) / I_total
```

2. **IPN (Improvement Priority Number):** İyileştirme öncelik sayısı

```
IPN = (I_EN_AV / I_total) * (1 - epsilon) * CF
```
Burada CF = maliyet faktörü (cost factor), epsilon = exergy verimi.

3. **epsilon_star (gelişmiş exergy verimi):** Kaçınılamaz yıkım dikkate alınmış verim

```
epsilon_star = P / (F - I_UN)
```

4. **r_EN_AV:** Endojen kaçınılabilir oran

```
r_EN_AV = I_EN_AV / I_total
```

5. **r_EX_AV:** Ekzojen kaçınılabilir oran

```
r_EX_AV = I_EX_AV / I_total
```

### 6.3 Sayısal Örnek

| Metrik | Kazan | Kompresör | Chiller | Pompa |
|--------|-------|-----------|---------|-------|
| theta | 0.450 | 0.375 | 0.438 | 0.343 |
| IPN | 0.82 | 0.45 | 0.51 | 0.18 |
| epsilon_star | 0.68 | 0.79 | 0.72 | 0.88 |
| r_EN_AV | 0.300 | 0.250 | 0.292 | 0.229 |
| r_EX_AV | 0.150 | 0.125 | 0.146 | 0.114 |

> **Yorum:** Kazan en büyük çokgen alanına sahiptir, dolayısıyla iyileştirme önceliği en yüksek bileşendir. Pompa en küçük alan ile sınırlı iyileştirme potansiyeli gösterir.

### 6.4 Alan Hesabı (Polygon Area)

Radar chart'taki çokgen alanı, Shoelace formülü ile hesaplanabilir. Normalleştirilmiş alan (0-1 arası) kullanılarak bileşenler sıralanır:

```
A_normalized = A_polygon / A_max_polygon
```

Burada A_max_polygon tüm eksenlerde 1.0 olduğunda elde edilen alandır.

### 6.5 Veri Formatı

```json
{
  "chart_type": "radar",
  "axes": ["theta", "IPN", "epsilon_star", "r_EN_AV", "r_EX_AV"],
  "axis_labels": [
    "Kaçınılabilir Oran",
    "İyileştirme Önceliği",
    "Gelişmiş Verim",
    "Endojen Kaçınılabilir",
    "Ekzojen Kaçınılabilir"
  ],
  "components": [
    {
      "name": "Kazan",
      "values": [0.450, 0.82, 0.68, 0.300, 0.150],
      "color": "#EF4444",
      "polygon_area": 0.72
    },
    {
      "name": "Kompresör",
      "values": [0.375, 0.45, 0.79, 0.250, 0.125],
      "color": "#3B82F6",
      "polygon_area": 0.41
    }
  ]
}
```

## 7. Heatmap (Isı Haritası)

### 7.1 Kavram

Satırlarda bileşenler, sütunlarda dört kategori yer alır. Renk yoğunluğu exergy yıkımı miktarını temsil eder. Büyük sistemlerde (10+ bileşen) hızlı görsel hotspot tespiti için idealdir.

### 7.2 Matris Yapısı

```
              │ I_EN_AV │ I_EX_AV │ I_EN_UN │ I_EX_UN │
─────────────┼─────────┼─────────┼─────────┼─────────┤
 Kazan       │  ████   │  ██     │  █████  │  ██     │
 Kompresör   │  ██     │  █      │  ███    │  █      │
 Chiller     │  ██     │  █      │  ██     │  █      │
 Pompa       │  ░      │  ░      │  █      │  ░      │
─────────────┴─────────┴─────────┴─────────┴─────────┘

Yoğunluk: ░ = düşük,  █ = orta,  ██ = yüksek,  ████ = çok yüksek
```

### 7.3 Renk Skalası

Her sütun kendi renk ailesinde gradient kullanır:

- **I_EN_AV sütunu:** Beyaz → Açık kırmızı → Koyu kırmızı (`#FEE2E2` → `#DC2626`)
- **I_EX_AV sütunu:** Beyaz → Açık turuncu → Koyu turuncu (`#FED7AA` → `#F97316`)
- **I_EN_UN sütunu:** Beyaz → Açık gri → Koyu gri (`#F3F4F6` → `#6B7280`)
- **I_EX_UN sütunu:** Beyaz → Çok açık gri → Orta gri (`#F9FAFB` → `#D1D5DB`)

### 7.4 Veri Formatı

```json
{
  "chart_type": "heatmap",
  "unit": "kW",
  "rows": ["Kazan", "Kompresör", "Chiller", "Pompa"],
  "columns": ["I_EN_AV", "I_EX_AV", "I_EN_UN", "I_EX_UN"],
  "values": [
    [255.0, 127.5, 340.0, 127.5],
    [45.0, 22.5, 90.0, 22.5],
    [38.0, 19.0, 57.0, 16.0],
    [8.0, 4.0, 18.0, 5.0]
  ],
  "max_value": 340.0,
  "highlight_threshold": 100.0
}
```

### 7.5 Hotspot Tespiti

Heatmap üzerinde otomatik hotspot tespiti için eşik değeri kullanılır:

```
Eşik = ortalama + 1 * standart_sapma

Ortalama = toplam_değerler / hücre_sayısı
         = (255 + 127.5 + 340 + 127.5 + 45 + 22.5 + 90 + 22.5 + 38 + 19 + 57 + 16 + 8 + 4 + 18 + 5) / 16
         = 1195 / 16
         = 74.7 kW

Standart sapma ≈ 96.3 kW

Eşik = 74.7 + 96.3 = 171.0 kW

Hotspot hücreler (>171 kW):
  - Kazan I_EN_AV: 255 kW  ← BİRİNCİ ÖNCELİK
  - Kazan I_EN_UN: 340 kW  ← Teknoloji limiti (bilgi amaçlı)
```

## 8. Veri Format Spesifikasyonları — Genel API Yanıtı

Tüm görselleştirme verilerini kapsayan birleşik API yanıt formatı:

```json
{
  "factory_id": "factory_001",
  "analysis_timestamp": "2025-05-15T10:30:00Z",
  "visualization_data": {
    "exergy_wheel": { "...wheel formatı..." },
    "stacked_bar": { "...stacked bar formatı..." },
    "waterfall": { "...waterfall formatı..." },
    "sankey_advanced": { "...Grassmann formatı..." },
    "radar": { "...radar formatı..." },
    "heatmap": { "...heatmap formatı..." }
  },
  "summary": {
    "total_destruction_kW": 1195,
    "avoidable_ratio": 0.434,
    "top_hotspot": "Kazan — I_EN_AV (255 kW)",
    "recommended_chart": "stacked_bar"
  }
}
```

## 9. Frontend Uygulama Notları (React / Recharts)

### 9.1 Bileşen Mimarisi

```
AdvancedExergyVisualizations/
├── ExergyWheel.jsx          — PieChart tabanlı dairesel diyagram
├── StackedDestructionBar.jsx — StackedBarChart tabanlı çubuk grafik
├── WaterfallChart.jsx       — Özel waterfall bileşeni
├── AdvancedSankey.jsx       — Mevcut SankeyDiagram genişletmesi
├── PerformanceRadar.jsx     — RadarChart tabanlı spider diyagram
├── DestructionHeatmap.jsx   — Özel heatmap bileşeni
└── ChartSelector.jsx        — Kullanıcıya grafik seçimi sunar
```

### 9.2 Recharts Bileşen Eşleştirmesi

| Görselleştirme | Recharts Bileşeni | Notlar |
|---------------|-------------------|--------|
| Exergy Wheel | `<PieChart>` + `<Pie>` | İki iç içe Pie: iç=UN, dış=AV |
| Stacked Bar | `<BarChart>` + `<Bar stackId>` | 4 adet `<Bar>` bileşeni |
| Waterfall | Özel (`<BarChart>` + invisible base) | Negatif değerler için özel hesaplama |
| Radar | `<RadarChart>` + `<Radar>` | Birden fazla Radar overlay |
| Heatmap | Özel (`<svg>` veya `<canvas>`) | Recharts'ta native heatmap yok |

### 9.3 Responsive Tasarım

- Mobilde: Tek grafik, kaydırmalı seçim (ChartSelector)
- Tablette: 2x2 grid düzeni
- Masaüstünde: Dashboard düzeni, tüm grafikler aynı anda

### 9.4 Tooltip Standardı

Tüm grafiklerde ortak tooltip formatı:

```
┌──────────────────────────────────┐
│ Kazan — Endojen Kaçınılabilir    │
│ Değer: 255.0 kW                 │
│ Toplam İçindeki Pay: %21.3      │
│ Aksiyon: Bileşen iyileştirmesi  │
└──────────────────────────────────┘
```

## İlgili Dosyalar

- `knowledge/factory/advanced_exergy/splitting.md` — Dört yollu exergy yıkımı ayrıştırma metodolojisi
- `knowledge/factory/advanced_exergy/interactions.md` — Bileşenler arası ekzojen etkileşim analizi
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arası exergy fırsatları
- `knowledge/factory/prioritization.md` — İyileştirme önceliklendirme mantığı
- `engine/sankey.py` — Mevcut Sankey diyagramı veri üreteci
- `frontend/src/components/SankeyDiagram.jsx` — Mevcut Sankey frontend bileşeni

## Referanslar

1. Tsatsaronis, G. & Park, M.H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270.

2. Morosuk, T. & Tsatsaronis, G. (2009). "Advanced exergy analysis for chemically reacting systems — Application to a simple open gas-turbine system." *International Journal of Thermodynamics*, 12(3), 105-111.

3. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T. & Carassai, A. (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152.

4. Bejan, A., Tsatsaronis, G. & Moran, M. (1996). *Thermal Design and Optimization*. John Wiley & Sons, New York.

5. Kelly, S., Tsatsaronis, G. & Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391.
