# BRIEF: Fabrika Sankey v2 — Grassmann Stili Çok Katmanlı Exergy Akış Diyagramı

> **Tarih:** 2026-02-07
> **Öncelik:** Yüksek
> **Tahmini Etki:** Fabrika analiz dashboardunun görsel gücünü 10x artırır
> **Bağımlılıklar:** Mevcut factory.py pipeline, sankey.py, FactorySankey.jsx

---

## 1. Amaç

Mevcut basit fabrika Sankey diyagramını, Grassmann tarzı çok katmanlı bir exergy akış diyagramına dönüştürmek. Bu diyagram fabrikanın tüm exergy akışını tek bir görselde anlatmalı: enerji kaynağından (yakıt, elektrik) ekipmanlara dağılım, her ekipmandaki exergy yıkımı, ekipmanlar arası ısı geri kazanım fırsatları ve nihai faydalı çıktılar vs kayıplar.

**Hedef:** Bir fabrika müdürü bu diyagrama bakıp 5 saniyede "para nerede yanıyor" sorusunun cevabını görebilmeli.

---

## 2. Mevcut Durum (Neler Var)

### 2.1 Backend
- `engine/sankey.py` (158 satır): Tek ekipman bazlı Sankey verisi üretiyor
  - `generate_sankey_data(result, equipment_subtype)` → dispatcher
  - Her ekipman tipi için ayrı `_generate_{type}_sankey_data()` fonksiyonu
  - Çıktı: `{ nodes: [...], links: [...], summary: {...} }`
- `engine/factory.py` Adım 5: `_generate_factory_sankey()` — Basit fabrika seviyesi Sankey
  - Ekipman bazlı node'lar ve toplam exergy in/out/destroyed linkleri
  - Entegrasyon fırsatlarını göstermiyor
  - Katmanlama (layering) yok — tüm ekipmanlar aynı seviyede

### 2.2 Frontend
- `components/results/SankeyDiagram.jsx` (70 satır): Tek ekipman Plotly sankey
- `components/factory/FactorySankey.jsx` (53 satır): Fabrika Plotly sankey — temel render

### 2.3 Mevcut Veri Yapısı
```json
{
  "nodes": [
    { "label": "Elektrik Girişi" },
    { "label": "Kompresör-1" },
    { "label": "Faydalı Çıktı" },
    { "label": "Exergy Yıkımı" }
  ],
  "links": [
    { "source": 0, "target": 1, "value": 100 },
    { "source": 1, "target": 2, "value": 65 },
    { "source": 1, "target": 3, "value": 35 }
  ],
  "summary": { "total_in": 100, "total_out": 65, "total_destroyed": 35 }
}
```

---

## 3. Hedef Tasarım: Grassmann Stili Çok Katmanlı Sankey

### 3.1 Katman Mimarisi (Soldan Sağa)

Diyagram 5 dikey katmandan oluşacak:

```
KATMAN 0          KATMAN 1           KATMAN 2          KATMAN 3         KATMAN 4
(Kaynaklar)       (Dağıtım)         (Ekipmanlar)      (Çıktılar)       (Sonuç)
                                                        
┌──────────┐                        ┌─────────────┐   ┌───────────┐    
│          │───────────────────────▶│ Kompresör-1  │──▶│ Basınçlı  │──┐ 
│ Elektrik │                        │   ██ 35 kW   │   │ Hava      │  │ ┌──────────┐
│ (400 kW) │───────────────────────▶│             │   └───────────┘  ├▶│ Faydalı  │
│          │                        └──────┬──────┘                   │ │ Çıktı    │
│          │───────┐                       │                          │ │ (620 kW) │
└──────────┘       │                       ▼                          │ └──────────┘
                   │                ┌─────────────┐                   │
                   │                │  Yıkım      │                   │
┌──────────┐       │                │  (exergy    │                   │
│          │───────┤                │  destroyed) │                   │ ┌──────────┐
│ Doğalgaz │       │                └─────────────┘                   │ │ Toplam   │
│ (800 kW) │───────┤                                                  │ │ Exergy   │
│          │       │                ┌─────────────┐   ┌───────────┐  │ │ Yıkımı   │
│          │───────┴───────────────▶│  Kazan-1    │──▶│ Buhar     │──┤ │ (380 kW) │
└──────────┘                        │   ██ 120 kW  │   └───────────┘  │ └──────────┘
                                    └──────┬──────┘                   │
┌──────────┐                               │          ┌───────────┐  │ ┌──────────┐
│ Atık Isı │                               ▼          │ Geri      │  │ │ Geri     │
│ (Geri    │◀─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│ Kazanım   │──┘ │ Kazanım  │
│ Kazanım) │   (entegrasyon fırsatı)       │          │ Potansiyel│    │ (200 kW) │
└──────────┘                               │          └───────────┘    └──────────┘
                                    ┌─────────────┐
                                    │  Chiller-1  │
                                    │   ██ 45 kW   │
                                    └─────────────┘
```

### 3.2 Node Tipleri ve Renk Şeması

| Node Tipi | Renk | Açıklama |
|-----------|------|----------|
| `source_electricity` | `#3b82f6` (blue-500) | Elektrik kaynağı |
| `source_fuel` | `#f97316` (orange-500) | Yakıt kaynağı (doğalgaz, LPG, vb.) |
| `source_thermal` | `#ef4444` (red-500) | Termal kaynak (buhar, sıcak su girişi) |
| `equipment` | Performansa göre dinamik renk | Her ekipman node'u |
| `product` | `#10b981` (green-500) | Faydalı çıktı (basınçlı hava, buhar, soğutma vb.) |
| `destroyed` | `#ef4444` (red-500), opaklık 0.6 | Exergy yıkımı |
| `destroyed_avoidable` | `#ef4444` (red-500), opaklık 0.8 | Kaçınılabilir exergy yıkımı |
| `destroyed_unavoidable` | `#9ca3af` (gray-400) | Kaçınılamaz exergy yıkımı |
| `recovery` | `#8b5cf6` (violet-500) | Isı geri kazanım potansiyeli |
| `integration` | `#8b5cf6` (violet-500), kesikli | Entegrasyon fırsatı (mevcut olmayan ama potansiyel) |

### 3.3 Link Tipleri ve Kalınlık

| Link Tipi | Renk | Opaklık | Açıklama |
|-----------|------|---------|----------|
| `fuel_flow` | `#f97316` | 0.5 | Yakıt → Ekipman |
| `electricity_flow` | `#3b82f6` | 0.5 | Elektrik → Ekipman |
| `thermal_flow` | `#ef4444` | 0.4 | Termal → Ekipman |
| `product_flow` | `#10b981` | 0.5 | Ekipman → Faydalı Çıktı |
| `destruction_avoidable` | `#ef4444` | 0.6 | Ekipman → Kaçınılabilir Yıkım |
| `destruction_unavoidable` | `#9ca3af` | 0.4 | Ekipman → Kaçınılamaz Yıkım |
| `recovery_potential` | `#8b5cf6` | 0.5 | Ekipman → Geri Kazanım |
| `integration_opportunity` | `#8b5cf6` | 0.3, dashed | Ekipmanlar arası fırsat |

Link kalınlığı: kW değerine doğrusal orantılı (minimum 2px, maksimum görsele göre).

### 3.4 Ekipman Node'u İç Detayı

Her ekipman node'u hover'da tooltip ile detay gösterecek:

```
┌─────────────────────────────┐
│ Kompresör-1 (Vidalı)        │
│ ─────────────────────────── │
│ Exergy Giriş:    100.0 kW   │
│ Exergy Çıkış:     65.0 kW   │
│ Exergy Yıkım:     35.0 kW   │
│ Verimlilik:        65.0 %    │
│ AV Yıkım:         22.0 kW   │
│ UN Yıkım:         13.0 kW   │
│ f-faktör:          0.35      │
│ Yıllık Kayıp:   €12,400     │
│ Öncelik:           YÜKSEK   │
└─────────────────────────────┘
```

### 3.5 Görünüm Modları

Kullanıcı 3 farklı görünüm modu arasında geçiş yapabilecek (toggle butonları):

| Mod | Açıklama | Varsayılan |
|-----|----------|------------|
| `exergy_flow` | Tam exergy akışı (kaynak → ekipman → çıktı/yıkım) | ✅ Varsayılan |
| `destruction_focus` | Sadece yıkımı vurgula: AV vs UN ayrımı, küçük akışları gizle | |
| `cost_flow` | Exergoekonomik akış: €/h cinsinden maliyet akışı (C_dot) | |

---

## 4. Backend Değişiklikleri

### 4.1 Yeni Dosya: `engine/factory_sankey_v2.py`

Mevcut `sankey.py`'ye dokunma — yeni dosya oluştur. Tek ekipman Sankey'leri olduğu gibi kalacak.

```python
# engine/factory_sankey_v2.py

def generate_factory_sankey_v2(
    equipment_results: list[dict],
    aggregates: dict,
    hotspots: list[dict],
    integration_opportunities: list[dict],
    advanced_exergy: dict | None = None,
    view_mode: str = "exergy_flow"  # exergy_flow | destruction_focus | cost_flow
) -> dict:
    """
    Grassmann tarzı çok katmanlı fabrika Sankey verisi üretir.
    
    Returns:
        {
            "nodes": [...],
            "links": [...],
            "layers": {...},
            "summary": {...},
            "view_mode": str,
            "metadata": {...}
        }
    """
```

#### 4.1.1 Node Oluşturma Mantığı

```python
def _build_nodes(equipment_results, aggregates, integration_opportunities):
    """
    5 katmanlı node yapısı oluşturur.
    
    Katman 0 - Kaynaklar:
      - Ekipman parametrelerinden enerji kaynağını çıkar
      - Elektrik kullanan ekipmanlar: kompresör, chiller, pompa
      - Yakıt kullanan ekipmanlar: kazan, kurutma fırını
      - Buhar kullanan ekipmanlar: buhar türbini (girişi buhar)
      - Aynı kaynağı kullanan ekipmanlar tek source node'a bağlanır
    
    Katman 1 - Dağıtım (opsiyonel):
      - Eğer 4+ ekipman aynı kaynağı kullanıyorsa, ara dağıtım node'u ekle
      - Aksi halde doğrudan kaynak → ekipman
    
    Katman 2 - Ekipmanlar:
      - Her ekipman bir node
      - Node rengi exergy verimliliğine göre (performanceColors mantığı)
      - Node boyutu exergy_in_kW'a orantılı
    
    Katman 3 - Çıktılar:
      - Her ekipmanın faydalı çıktısı (basınçlı hava, buhar, soğutma, vb.)
      - Exergy yıkımı (AV ve UN ayrımı)
      - Isı geri kazanım potansiyeli
    
    Katman 4 - Sonuç (Agregasyon):
      - Toplam faydalı exergy
      - Toplam exergy yıkımı
      - Toplam geri kazanım potansiyeli
    
    Returns:
        nodes: list[dict] — her node:
            {
                "id": str,           # benzersiz tanımlayıcı
                "label": str,        # görünen isim (Türkçe)
                "layer": int,        # 0-4 arası katman
                "node_type": str,    # source_electricity, equipment, destroyed, vb.
                "color": str,        # hex renk kodu
                "value_kw": float,   # kW değeri (boyut hesabı için)
                "metadata": dict     # tooltip için ek bilgi
            }
    """
```

#### 4.1.2 Link Oluşturma Mantığı

```python
def _build_links(nodes, equipment_results, integration_opportunities, view_mode):
    """
    Node'lar arası bağlantıları oluşturur.
    
    Temel Akışlar (her zaman):
      - Kaynak → Ekipman: exergy_in_kW değerinde
      - Ekipman → Faydalı Çıktı: exergy_out_kW değerinde
      - Ekipman → Exergy Yıkımı: exergy_destroyed_kW değerinde
    
    AV/UN Ayrımı (destruction_focus modunda veya her zaman):
      - Ekipman → Kaçınılabilir Yıkım: exergy_destroyed_avoidable_kW
      - Ekipman → Kaçınılamaz Yıkım: exergy_destroyed_unavoidable_kW
    
    Isı Geri Kazanım (varsa):
      - Ekipman → Geri Kazanım: recoverable_heat_kW (veya heat_recovery_potential_kW)
    
    Entegrasyon Fırsatları (integration_opportunities listesinden):
      - Ekipman-A → Ekipman-B: entegrasyon potansiyeli kW
      - Bu linkler kesikli (dashed) stil ile gösterilecek
      - Sadece exergy_flow modunda göster
    
    Maliyet Akışı (cost_flow modunda):
      - Değerler kW yerine €/h cinsinden: C_dot_destruction, Z_dot
      - Kaynak maliyeti: c_fuel * exergy_in olarak hesapla
    
    Returns:
        links: list[dict] — her link:
            {
                "source": str,       # kaynak node id
                "target": str,       # hedef node id
                "value": float,      # kW veya €/h
                "link_type": str,    # fuel_flow, destruction_avoidable, vb.
                "color": str,        # rgba renk
                "label": str,        # hover label
                "is_opportunity": bool  # entegrasyon fırsatı mı?
            }
    """
```

#### 4.1.3 Kaynak Tespiti Yardımcı Fonksiyonu

```python
# Ekipman tipine göre enerji kaynağını belirle
EQUIPMENT_ENERGY_SOURCE = {
    "compressor": "electricity",
    "chiller": "electricity",
    "pump": "electricity",
    "boiler": "fuel",          # parametrelerden yakıt tipi çıkarılabilir
    "dryer": "fuel",           # veya elektrik olabilir (heat_pump subtype)
    "steam_turbine": "thermal", # giriş buharı
    "heat_exchanger": "thermal" # sıcak akışkan girişi
}

# Dryer alt tip istisnası
DRYER_ELECTRIC_SUBTYPES = ["heat_pump", "infrared", "microwave"]

def _determine_energy_source(equipment_type: str, subtype: str, parameters: dict) -> str:
    """Ekipman tipine ve alt tipine göre enerji kaynağını belirler."""
```

#### 4.1.4 Ürün Tipi Yardımcı Fonksiyonu

```python
# Ekipman tipine göre faydalı çıktı adı (Türkçe)
EQUIPMENT_PRODUCT_LABELS = {
    "compressor": "Basınçlı Hava",
    "boiler": "Buhar / Sıcak Su",
    "chiller": "Soğutma",
    "pump": "Hidrolik İş",
    "heat_exchanger": "Isı Transferi",
    "steam_turbine": "Mekanik / Elektrik",
    "dryer": "Kurutma"
}
```

#### 4.1.5 Plotly Formatına Dönüştürme

```python
def to_plotly_format(sankey_data: dict) -> dict:
    """
    Kendi veri yapımızı Plotly Sankey trace formatına dönüştürür.
    
    Plotly Sankey trace yapısı:
    {
        "type": "sankey",
        "arrangement": "snap",
        "node": {
            "label": [...],
            "color": [...],
            "x": [...],        # katman pozisyonu (0.0 - 1.0)
            "y": [...],        # dikey pozisyon (0.0 - 1.0)
            "pad": 20,
            "thickness": 25,
            "line": { "color": "white", "width": 1 },
            "customdata": [...],  # tooltip metadata
            "hovertemplate": "..."
        },
        "link": {
            "source": [...],
            "target": [...],
            "value": [...],
            "color": [...],
            "label": [...],
            "customdata": [...],
            "hovertemplate": "..."
        }
    }
    
    Kritik: Plotly'de node x/y pozisyonları 0-1 arası.
    Katman → x eşlemesi:
      - Katman 0 (Kaynaklar):  x = 0.01
      - Katman 1 (Dağıtım):   x = 0.20
      - Katman 2 (Ekipmanlar): x = 0.45
      - Katman 3 (Çıktılar):  x = 0.75
      - Katman 4 (Sonuç):     x = 0.99
    
    y pozisyonu: node'ları dikey olarak ekipman tipine göre grupla
    (elektrikli üstte, yakıtlı ortada, termal altta)
    """
```

#### 4.1.6 Summary Hesaplaması

```python
def _build_summary(equipment_results, aggregates) -> dict:
    """
    Sankey diyagramının altında/yanında gösterilecek özet metrikleri.
    
    Returns:
        {
            "total_exergy_in_kw": float,
            "total_exergy_out_kw": float,
            "total_destroyed_kw": float,
            "total_destroyed_avoidable_kw": float,
            "total_destroyed_unavoidable_kw": float,
            "total_recovery_potential_kw": float,
            "factory_exergy_efficiency_pct": float,
            "biggest_loss_equipment": str,
            "biggest_loss_kw": float,
            "source_breakdown": {
                "electricity_kw": float,
                "fuel_kw": float,
                "thermal_kw": float
            },
            "num_integration_opportunities": int,
            "integration_potential_kw": float
        }
    """
```

### 4.2 factory.py Değişikliği

`_generate_factory_sankey()` fonksiyonunu güncelle — yeni `factory_sankey_v2` modülünü çağırsın:

```python
# factory.py içinde, Adım 5'i güncelle:
from engine.factory_sankey_v2 import generate_factory_sankey_v2

def _generate_factory_sankey(equipment_results, aggregates, hotspots, integration_opportunities, advanced_exergy=None):
    """Eski fonksiyonu yeni v2 ile değiştir."""
    return generate_factory_sankey_v2(
        equipment_results=equipment_results,
        aggregates=aggregates,
        hotspots=hotspots,
        integration_opportunities=integration_opportunities,
        advanced_exergy=advanced_exergy,
        view_mode="exergy_flow"
    )
```

### 4.3 API Route Değişikliği (Opsiyonel)

Eğer frontend'den view_mode değiştirmek istenirse, factory.py route'una query parameter ekle:

```python
# api/routes/factory.py — analyze endpoint'inde
# view_mode parametresi: FactoryAnalysisResult.sankey içine gömülecek
# Frontend farklı mod istediğinde yeni istek atacak veya
# frontend tarafında client-side mod değişimi yapılacak (tercih edilen)
```

**ÖNEMLİ:** view_mode değişimi tercihen frontend'de yapılmalı. Backend her zaman tam veriyi dönsün (tüm AV/UN, cost verileri dahil), frontend hangi linkleri gösterip gizleyeceğine karar versin. Bu şekilde mod değişiminde yeni API isteği gerekmez.

---

## 5. Frontend Değişiklikleri

### 5.1 Yeni Component: `components/factory/FactorySankeyV2.jsx`

Mevcut `FactorySankey.jsx`'i (53 satır) **değiştir** (yeniden yaz veya yeni dosya + import güncelle).

```
FactorySankeyV2.jsx yapısı:
├── ViewModeToggle (3 buton: Exergy Akışı / Yıkım Odaklı / Maliyet)
├── SankeyChart (Plotly.js trace)
├── SankeySummaryBar (alt kısımda özet metrikler)
└── SankeyLegend (renk açıklamaları)
```

#### 5.1.1 ViewModeToggle

```jsx
// 3 butonlu toggle grubu
// Aktif mod: bg-blue-600 text-white
// Pasif mod: bg-gray-100 text-gray-600
// Buton metinleri (Türkçe):
//   - "Exergy Akışı" (exergy_flow)
//   - "Yıkım Analizi" (destruction_focus)
//   - "Maliyet Akışı" (cost_flow)

// State: const [viewMode, setViewMode] = useState("exergy_flow");
```

#### 5.1.2 Plotly Sankey Konfigürasyonu

```jsx
// Layout ayarları
const layout = {
  font: { family: "system-ui, sans-serif", size: 13 },
  margin: { l: 10, r: 10, t: 40, b: 10 },
  paper_bgcolor: "transparent",
  plot_bgcolor: "transparent",
  title: {
    text: viewMode === "cost_flow" 
      ? "Fabrika Exergoekonomik Maliyet Akışı (€/h)" 
      : "Fabrika Exergy Akış Diyagramı (kW)",
    font: { size: 16, color: "#374151" }
  }
};

// Config
const config = {
  displayModeBar: false,
  responsive: true,
  staticPlot: false  // hover aktif olsun
};
```

#### 5.1.3 Client-Side View Mode Filtreleme

```jsx
// Backend'den gelen tam veriyi view mode'a göre filtrele
function filterByViewMode(sankeyData, viewMode) {
  if (viewMode === "exergy_flow") {
    // Tüm linkleri göster, AV/UN'u birleştir (tek "yıkım" linki)
    // Entegrasyon fırsatlarını göster (kesikli)
  } else if (viewMode === "destruction_focus") {
    // AV ve UN'u ayrı linkler olarak göster
    // Küçük akışları gizle (< toplam exergy'nin %2'si)
    // Entegrasyon fırsatlarını gizle
    // Yıkım linklerini kalınlaştır
  } else if (viewMode === "cost_flow") {
    // Değerleri kW'dan €/h'ye çevir
    // Exergoekonomik verisi olmayan ekipmanları grileştir
    // f-faktör ve r-faktör bilgisini tooltip'e ekle
  }
}
```

#### 5.1.4 Tooltip Formatı (Türkçe)

```jsx
// Node hover template
const nodeHoverTemplate = `
<b>%{customdata[0]}</b><br>
Tip: %{customdata[1]}<br>
Exergy Giriş: %{customdata[2]} kW<br>
Exergy Çıkış: %{customdata[3]} kW<br>
Exergy Yıkım: %{customdata[4]} kW<br>
Verimlilik: %{customdata[5]}%<br>
Öncelik: %{customdata[6]}<br>
<extra></extra>
`;

// Link hover template
const linkHoverTemplate = `
<b>%{customdata[0]}</b><br>
%{value:.1f} %{customdata[1]}<br>
<extra></extra>
`;
```

#### 5.1.5 SankeySummaryBar

Diyagramın altında yatay özet çubuğu:

```
┌────────────┬────────────┬────────────┬────────────┬────────────┐
│ Toplam     │ Faydalı    │ Toplam     │ Kaçınılabir│ Geri       │
│ Giriş      │ Çıktı      │ Yıkım      │ Yıkım      │ Kazanım    │
│ 1,200 kW   │ 620 kW     │ 380 kW     │ 245 kW     │ 200 kW     │
│             │ %51.7      │ %31.7      │ %64.5      │             │
└────────────┴────────────┴────────────┴────────────┴────────────┘
```

Her kutucukta: değer (kW veya €/h) + yüzde. Renk kodlu (faydalı=yeşil, yıkım=kırmızı, geri kazanım=mor).

#### 5.1.6 SankeyLegend

Diyagramın sağ üstünde veya altında küçük renk açıklamaları:

```
● Elektrik   ● Yakıt   ● Faydalı Çıktı   ● Kaçınılabilir Yıkım   ● Kaçınılamaz Yıkım   ● Geri Kazanım   ┄ Entegrasyon Fırsatı
```

### 5.2 FactoryDashboard.jsx Güncellemesi

Sankey tab'ında `FactorySankey` yerine `FactorySankeyV2` kullan. Componente geçirilecek props:

```jsx
<FactorySankeyV2
  sankeyData={analysisResult.sankey}
  equipmentResults={analysisResult.equipment_results}
  aggregates={analysisResult.aggregates}
  hotspots={analysisResult.hotspots}
  integrationOpportunities={analysisResult.integration_opportunities}
  advancedExergy={analysisResult.advanced_exergy}
/>
```

---

## 6. Entegrasyon Fırsatlarının Sankey'e Yansıması

Mevcut 9 entegrasyon pattern'i Sankey'de şu şekilde gösterilecek:

| Pattern | Sankey'deki Görünüm |
|---------|---------------------|
| Kompresör atık ısısı → Kazan ön ısıtma | Kompresör yıkım node'undan Kazan'a kesikli mor link |
| Kompresör atık ısısı → Mekân ısıtma | Kompresör yıkım node'undan yeni "Mekân Isıtma" node'una |
| Kazan baca gazı → Absorption chiller | Kazan yıkımından Chiller'a kesikli mor link |
| Chiller kondansör ısısı → Sıcak su | Chiller yıkımından yeni "Sıcak Su" node'una |
| Pompa VSD retrofiti | Pompa node'unda yıldız/vurgu (link yok) |
| Kurutma egzozu → HX ön ısıtma | Kurutma yıkımından HX'e kesikli mor link |
| Buhar türbini egzozu → Absorption chiller | Türbin yıkımından Chiller'a kesikli mor link |
| Kazan baca gazı → HX ekonomizer | Kazan yıkımından HX'e kesikli mor link |
| Buhar türbini CHP → Tesis ısıtma | Türbin çıktısından yeni "Tesis Isıtma" node'una |

Bu entegrasyon linkleri `is_opportunity: true` olarak işaretlenecek ve frontend'de:
- Kesikli (dashed) çizgi stili
- Mor renk (#8b5cf6)
- Düşük opaklık (0.3)
- Hover'da "⚡ Entegrasyon Fırsatı: [açıklama]" + tahmini tasarruf

---

## 7. Test Gereksinimleri

### 7.1 Yeni Test Dosyası: `tests/test_factory_sankey_v2.py`

```python
# Minimum test senaryoları:

# 1. Tek ekipman fabrika (en basit durum)
def test_single_equipment_sankey():
    """1 kompresör ile sankey: 1 kaynak, 1 ekipman, 2 çıktı (ürün + yıkım)"""

# 2. Karışık kaynaklı fabrika
def test_mixed_source_sankey():
    """Elektrik (kompresör, pompa) + yakıt (kazan) + termal (HX) karışımı"""

# 3. AV/UN ayrımı
def test_avoidable_unavoidable_split():
    """destruction_focus modunda AV ve UN ayrı node/link olarak görünmeli"""

# 4. Entegrasyon fırsatları
def test_integration_opportunities_links():
    """Entegrasyon fırsatları kesikli linkler olarak Sankey'de görünmeli"""

# 5. Maliyet modu
def test_cost_flow_mode():
    """cost_flow modunda değerler €/h cinsinden olmalı"""

# 6. Node katman doğrulaması
def test_node_layers():
    """Her node doğru katmanda (0-4) olmalı"""

# 7. Enerji korunumu doğrulaması (KRİTİK)
def test_energy_conservation():
    """Her ekipman node'unda: giren link toplamı = çıkan link toplamı"""
    
# 8. Plotly format dönüşümü
def test_plotly_format_conversion():
    """to_plotly_format() geçerli Plotly trace üretmeli"""

# 9. Boş fabrika
def test_empty_factory():
    """Ekipman yokken hata vermemeli, boş sankey dönmeli"""

# 10. Büyük fabrika (7+ ekipman)
def test_large_factory_layout():
    """Çok ekipmalı fabrikada node'lar üst üste binmemeli"""
```

---

## 8. Plotly Sankey Teknik Notlar

### 8.1 Plotly'de Katman Kontrolü

Plotly Sankey'de node pozisyonunu kontrol etmek için `x` ve `y` kullan:

```python
node = dict(
    label=[...],
    x=[0.01, 0.01, 0.45, 0.45, 0.75, 0.99, ...],  # katman pozisyonu
    y=[0.1, 0.5, 0.2, 0.6, 0.3, 0.5, ...],         # dikey pozisyon
    pad=20,
    thickness=25
)
```

**DİKKAT:** x ve y değerleri 0.0 ile 1.0 arasında olmalı. Tam 0.0 veya tam 1.0 kullanmaktan kaçın (Plotly'de rendering sorunları olabilir), 0.001 ve 0.999 tercih et.

### 8.2 Renk ve Opaklık

Plotly Sankey linklerinde rgba formatı kullan:

```python
# Link renk örnekleri
"rgba(239, 68, 68, 0.6)"   # kırmızı, yıkım
"rgba(16, 185, 129, 0.5)"  # yeşil, faydalı çıktı
"rgba(139, 92, 246, 0.3)"  # mor, entegrasyon fırsatı
```

### 8.3 Minimum Ekipman Sayısı

Bu özellik 1 ekipmanla bile çalışmalı ama gerçek gücünü 3+ ekipmanla gösterir. 1-2 ekipman durumunda daha basit bir layout kullan (dağıtım katmanını atla).

### 8.4 Performans

Plotly Sankey 50+ node'da yavaşlayabilir. Fabrikalar genellikle 3-15 ekipman arasında olacak, bu da ~30-60 node (kaynak + ekipman + çıktı + yıkım) demek. Bu aralık sorunsuz çalışır.

---

## 9. Dosya Değişiklikleri Özeti

| Dosya | İşlem | Açıklama |
|-------|-------|----------|
| `engine/factory_sankey_v2.py` | **YENİ** | Çok katmanlı Sankey veri üretimi (~400-500 satır) |
| `engine/factory.py` | **GÜNCELLE** | `_generate_factory_sankey()` → v2 çağrısı |
| `engine/__init__.py` | **GÜNCELLE** | Yeni modül export |
| `frontend/src/components/factory/FactorySankeyV2.jsx` | **YENİ** | Yeni Sankey component (~250-350 satır) |
| `frontend/src/components/factory/FactorySankey.jsx` | **SİL/DEĞİŞTİR** | V2 ile değiştirilecek |
| `frontend/src/pages/FactoryDashboard.jsx` | **GÜNCELLE** | Import değişikliği |
| `tests/test_factory_sankey_v2.py` | **YENİ** | Yeni test dosyası (~200-300 satır) |

**Tahmini toplam yeni kod:** ~900-1,200 satır (engine ~500 + frontend ~350 + tests ~250)

---

## 10. Kabul Kriterleri

1. ✅ 5 katmanlı Grassmann tarzı Sankey doğru render ediliyor
2. ✅ 3 görünüm modu (exergy_flow, destruction_focus, cost_flow) çalışıyor
3. ✅ Ekipman node'ları hover'da detaylı tooltip gösteriyor
4. ✅ Entegrasyon fırsatları kesikli mor linklerle gösteriliyor
5. ✅ AV/UN yıkım ayrımı destruction_focus modunda görünüyor
6. ✅ Enerji korunumu sağlanıyor (giren = çıkan, her node'da)
7. ✅ 1 ekipman ile de, 10 ekipman ile de düzgün çalışıyor
8. ✅ SankeySummaryBar özet metrikleri doğru gösteriyor
9. ✅ Mevcut testler kırılmıyor (671 test hâlâ geçiyor)
10. ✅ Yeni testler yazılmış ve geçiyor
11. ✅ Türkçe etiketler ve tooltip'ler doğru

---

## 11. ÖNEMLİ UYARILAR

1. **Mevcut `sankey.py`'ye DOKUNMA** — Tek ekipman Sankey'leri ayrı kalacak
2. **`engine/factory.py`'deki pipeline sırasını BOZMA** — Sadece Adım 5'in iç implementasyonunu değiştir
3. **Plotly versiyonu:** Mevcut `plotly.js ^3.3.1` — uyumluluğu kontrol et
4. **Node x/y pozisyonlarında 0.0 ve 1.0 KULLANMA** — Plotly rendering sorunları olur
5. **Maliyet akışında exergoekonomik verisi olmayan ekipmanlar olabilir** — Fallback: 0 değerli gri link
6. **Büyük fabrikalarda (10+ ekipman) y pozisyonlarını dinamik hesapla** — Üst üste binme olmasın

---

*Bu brief ExergyLab v3.2 için Grassmann tarzı fabrika Sankey geliştirmesi kapsamındadır.*
