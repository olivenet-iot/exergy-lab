# BRIEF: Ekipman Analizi Sayfası Kapsamlı Redesign

> **Tarih:** 2026-02-06
> **Kapsam:** EquipmentAnalysis.jsx + tüm alt componentler (dashboard/, results/, chat/, whatif/)
> **Hedef:** Görsel hiyerarşi, bilgi yoğunluğu kontrolü, profesyonel SaaS estetiği
> **Etkilenen dosyalar:** ~25 component, ~2,500 satır JSX/CSS

---

## 1. Problem Analizi

### 1.1 Mevcut Sorunlar (Ekran Görüntülerinden)

| # | Sorun | Nerede | Etki |
|---|-------|--------|------|
| P1 | Görsel hiyerarşi yok | Tüm sayfa | Her kart aynı ağırlıkta, göz nereye bakacağını bilmiyor |
| P2 | Beyaz kutu monotonluğu | Tüm kartlar | `bg-white border border-gray-200 rounded` tekrarı, derinlik yok |
| P3 | Radar chart küçük, legend kesilmiş | Overview tab | "Exergy V...", "Isı Geri K..." okunamıyor |
| P4 | Temel Metrikler kartı gereksiz | Overview tab | Sadece 3 satır — MetricBar zaten aynı bilgiyi gösteriyor |
| P5 | Sankey taşma/kaybolma | Akış tab | Sürüklenince label'lar kesiliyor, container overflow sorunu |
| P6 | AI tab dikey scroll cehennem | AI Danışman tab | ~3 ekran scroll: özet→analiz→bulgular→4 öneri→aksiyon→chat |
| P7 | Chat en altta gömülü | AI Danışman tab | Sohbet özelliğine ulaşmak için tüm AI metnini scroll etmek lazım |
| P8 | Öneri kartları metin duvarı | AI Danışman tab | Yıllık Tasarruf/Yatırım/Geri Ödeme bilgisi metin içinde kayboluyor |
| P9 | Senaryo tab'da tek slider | Senaryo tab | Sadece 1 parametre değiştirilebilir gibi görünüyor |
| P10 | Karşılaştırma tablosu sıkıcı | Senaryo tab | Düz tablo, yeşil/kırmızı vurgusu zayıf |
| P11 | Font/spacing tutarsızlığı | Genel | Başlıklar, gövde metni, etiketler arasında tutarlı hiyerarşi yok |
| P12 | Detaylı Metrikler tablosu düz | Akış tab altı | Uzun tablo, gruplama yok, değerler renksiz |

### 1.2 Kök Neden

**"Her şeyi göster" felsefesi.** Platform 6 motor ve çok sayıda metrik üretiyor. Mevcut UI hepsini eşit ağırlıkta listeliyor. Eksik olan: **bilgi katmanlama** (progressive disclosure) ve **görsel ağırlık farklılaştırma** (visual hierarchy).

---

## 2. Tasarım Felsefesi

### 2.1 Temel Prensipler

1. **"Skor önce, detay sonra"** — İlk bakışta büyük skor/durum, detaylar tıklamayla
2. **"3-saniye kuralı"** — Kullanıcı 3 saniyede en kritik bilgiyi görmeli
3. **"Endüstriyel profesyonellik"** — Fabrika müdürünün ciddiye alacağı estetik, oyuncak değil
4. **"Nefes alan layout"** — Kartlar arası spacing, gruplama, görsel mola noktaları

### 2.2 Estetik Yön: "Endüstriyel Kontrol Paneli"

Referans dünya: SCADA/HMI dashboard estetiği + modern SaaS rafineliği.

- **Renk sistemi:** Koyu üst bar (slate-800/900) + açık arka plan (slate-50) + renkli aksan (performans bazlı)
- **Tipografi:** Sayılar büyük ve bold (tabular-nums), etiketler küçük ve muted
- **Kartlar:** Subtle shadow (shadow-sm), sol kenarda renk çizgisi (performance indicator), rounded-lg
- **Performans renkleri:** Yeşil (iyi, ≥70%), Amber (orta, 40-70%), Kırmızı (kötü, <40%)

### 2.3 Renk Sistemi (CSS Variables)

```css
:root {
  /* Ana renkler */
  --color-surface: #f8fafc;        /* slate-50, sayfa arka planı */
  --color-card: #ffffff;            /* kart arka planı */
  --color-card-elevated: #ffffff;   /* öne çıkan kart, daha güçlü shadow */

  /* Performans renkleri */
  --color-perf-excellent: #059669;  /* emerald-600 (≥80%) */
  --color-perf-good: #10b981;      /* emerald-500 (60-80%) */
  --color-perf-average: #f59e0b;   /* amber-500 (40-60%) */
  --color-perf-poor: #ef4444;      /* red-500 (<40%) */

  /* Aksan renkler */
  --color-primary: #2563eb;        /* blue-600 */
  --color-primary-soft: #dbeafe;   /* blue-100 */
  --color-ai-accent: #7c3aed;     /* violet-600, AI özellik vurgusu */
  --color-ai-soft: #ede9fe;       /* violet-100 */

  /* Metin hiyerarşisi */
  --text-primary: #0f172a;         /* slate-900 */
  --text-secondary: #475569;       /* slate-600 */
  --text-muted: #94a3b8;           /* slate-400 */
}
```

---

## 3. Sayfa Genel Yapısı (Yeni Layout)

### 3.1 Analiz Öncesi (Form Sayfası)

Mevcut form iyi çalışıyor. Minimal değişiklikler:

```
┌─────────────────────────────────────────────────────────────────┐
│ [Kompresör ikonu]  Kompresör Ekserji Analizi                    │
│ Kompresör tipini seçin ve parametreleri girin                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Kompresör Tipi                                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │  Vidalı   │ │ Pistonlu │ │  Scroll  │ │Santrifüj │          │
│  │    ✓      │ │          │ │          │ │          │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
│  2. Parametreler                                                │
│  ┌─────────────┐ ┌─────────────┐                               │
│  │ Elektrik     │ │ Hava Debisi  │                               │
│  │ Gücü (kW)   │ │ (m³/min)    │                               │
│  │ [37       ]  │ │ [6.2      ]  │                               │
│  └─────────────┘ └─────────────┘                               │
│  ...                                                            │
│                                                                 │
│  ┌──────────────────────────────────────┐                      │
│  │        🔬 Ekserji Analizi Yap        │                      │
│  └──────────────────────────────────────┘                      │
│                                                                 │
│  ┌ · · · · · · · · · · · · · · · · · · ┐ ← YENİ               │
│  │ ℹ Bu analiz size şunları verecek:    │                      │
│  │ • Ekserji verimliliği ve sektörel    │                      │
│  │   kıyaslama (A-F not)               │                      │
│  │ • Yıkım ayrıştırması (AV/UN)        │                      │
│  │ • Yapay zeka destekli iyileştirme    │                      │
│  │   önerileri ve ROI hesabı            │                      │
│  │ • What-if senaryo karşılaştırması    │                      │
│  └ · · · · · · · · · · · · · · · · · · ┘                      │
└─────────────────────────────────────────────────────────────────┘
```

**Değişiklikler:**
- Butonun altına hafif bir "Bu analiz size şunları verecek" bilgi kutusu (ilk kez kullanan için)
- Tip seçim kartlarına küçük ikon eklenebilir (opsiyonel)

### 3.2 Analiz Sonrası (Dashboard) — ANA REDESİGN

Mevcut 4-tab yapısı korunuyor ama her tab'ın içeriği yeniden düzenleniyor.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ SIDEBAR (mevcut)  │  ANA İÇERİK ALANI                                      │
│                   │                                                          │
│                   │ ┌── HERO SCORE BANNER ──────────────────────────────────┐│
│                   │ │ [Gauge]  %58.4   C  │  15.4 kW  │  €6,154  │ %36.2  ││
│                   │ │ Ekserji  Verim  Not │  Yıkım    │  Kayıp   │ Kaçınıl ││
│                   │ └──────────────────────────────────────────────────────┘│
│                   │                                                          │
│                   │ ┌─ TABS ───────────────────────────────────────────────┐│
│                   │ │ [Genel Bakış] [Akış] [AI Danışman] [Senaryo]        ││
│                   │ └─────────────────────────────────────────────────────┘│
│                   │                                                          │
│                   │ ┌── TAB İÇERİĞİ ─────────────────────────────────────┐│
│                   │ │                                                      ││
│                   │ │  (tab'a göre değişen içerik)                        ││
│                   │ │                                                      ││
│                   │ └─────────────────────────────────────────────────────┘│
│                   │                                                          │
│                   │ ┌── FLOATING CHAT (opsiyonel, her tab'da erişilebilir)─┐│
│                   │ │ 💬 AI Danışmanı (tıkla)                              ││
│                   │ └──────────────────────────────────────────────────────┘│
└───────────────────┴──────────────────────────────────────────────────────────┘
```

**Yapısal değişiklikler:**
1. **MetricBar → Hero Score Banner:** Daha büyük, daha cesur, performans renginde
2. **Parameter Sidebar korunuyor** (sol panel, collapsible)
3. **4 Tab korunuyor** ama içerikleri yeniden düzenleniyor
4. **Chat → Floating panel** (tab'lardan bağımsız, her zaman erişilebilir)

---

## 4. Hero Score Banner (Yeni MetricBar)

Mevcut MetricBar iyi bir başlangıç ama çok "düz". Yeni tasarım:

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│  ┌──────────────┐                                                      │
│  │   ████████   │   Kompresör — Vidalı Kompresör                       │
│  │   ██ 58 ██   │   ──────────────────────────────────────────         │
│  │   ██  .4 █   │                                                      │
│  │   ████████   │   YIKIM          YILLIK KAYIP     KAÇINILABİLİR     │
│  │    %58.4     │   15.4 kW        €6,154/yıl       %36.2             │
│  │   C Orta     │   ▪ 9.8 kaçınılmaz               ▪ 5.6 kW potansiyel│
│  └──────────────┘   ▪ 5.6 kaçınılabilir                               │
│                                                                        │
│  [← Tekrar Analiz]                          [📄 PDF] [📋 Kopyala]     │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Detaylı Tasarım

**Sol: Verimlilik Gauge (hero element)**
- Büyük yarım daire (semi-circle) gauge — performans renginde
- Ortasında büyük sayı: `%58.4`
- Altında harf notu: `C — Orta` (renk kodlu badge)
- `120x120px` minimum boyut

**Sağ: 3 KPI bloğu**
- Her biri: büyük sayı + küçük etiket + opsiyonel alt detay
- Yıkım: `15.4 kW` — altında AV/UN mini breakdown
- Yıllık Kayıp: `€6,154/yıl` — kırmızı renk
- Kaçınılabilir: `%36.2` — altında `5.6 kW potansiyel`

**Implementasyon: `HeroScoreBanner.jsx`**

```jsx
// Props
{
  equipmentName: string,
  subtype: string,
  efficiency: number,        // 0-100
  grade: string,             // A-F
  gradeLabel: string,        // "Mükemmel", "İyi", "Orta", "Zayıf", "Kritik"
  destructionKW: number,
  avoidableKW: number,
  unavoidableKW: number,
  annualLossEUR: number,
  avoidableRatio: number,    // 0-100
  avoidableKWPotential: number
}
```

**Renk mantığı:**
```js
const getPerformanceColor = (efficiency) => {
  if (efficiency >= 80) return 'emerald';   // excellent
  if (efficiency >= 60) return 'blue';      // good
  if (efficiency >= 40) return 'amber';     // average
  return 'red';                              // poor
};
```

**Gauge implementasyonu:** SVG semi-circle arc (CSS conic-gradient veya SVG path). Plotly KULLANMIYORUZ — lightweight olmalı.

```jsx
// SVG Gauge Component (inline, hafif)
const GaugeChart = ({ value, maxValue = 100, color }) => {
  const percentage = Math.min(value / maxValue, 1);
  const angle = percentage * 180;
  // SVG arc path hesaplama...
  return (
    <svg viewBox="0 0 120 70" className="w-32 h-20">
      {/* Arka plan arc (gri) */}
      <path d="..." stroke="#e2e8f0" strokeWidth="10" fill="none" />
      {/* Değer arc (renkli) */}
      <path d="..." stroke={color} strokeWidth="10" fill="none" />
      {/* Merkez metin */}
      <text x="60" y="62" textAnchor="middle" className="text-2xl font-bold">
        %{value.toFixed(1)}
      </text>
    </svg>
  );
};
```

---

## 5. Tab 1: Genel Bakış (Overview) — Redesign

### 5.1 Mevcut Sorunlar
- Radar küçük, legend kesilmiş
- AV/UN sağda izole
- Temel Metrikler gereksiz tekrar
- AI özeti scroll'un altında kayıp

### 5.2 Yeni Layout

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│  ┌─── AI Özet (Hero AI Insight) ──────────────────────────────────┐   │
│  │ 🤖 37 kW vidalı kompresör iyi seviyede çalışıyor.             │   │
│  │    Yıllık €1,538 tasarruf potansiyeli mevcut.                  │   │
│  │    → En yüksek ROI: Atık ısı geri kazanımı (2.6 yıl)         │   │
│  │                                        [Detaylı Analiz →]     │   │
│  └────────────────────────────────────────────────────────────────┘   │
│                                                                        │
│  ┌─── Benchmark Radar ─────────────┐ ┌─── Yıkım Ayrıştırması ───┐   │
│  │                                  │ │                            │   │
│  │      (BÜYÜK radar chart)         │ │  Kaçınılabilir (AV)       │   │
│  │      6 eksen, legend altında     │ │  ██████████░░░░░░  36.2%  │   │
│  │      tam yazılmış                │ │  5.6 kW                   │   │
│  │                                  │ │                            │   │
│  │      min 350x350px              │ │  Kaçınılamaz (UN)          │   │
│  │                                  │ │  ░░░░░░░░░░██████  63.8%  │   │
│  │                                  │ │  9.8 kW                   │   │
│  │                                  │ │                            │   │
│  │  [Exergy Ver. 58] [İyileş. 64] │ │  ─────────────────         │   │
│  │  [Sektör 66] [Isı Geri K. 60]  │ │  Toplam Yıkım: 15.4 kW   │   │
│  │  [Yıkım Or. 58] [Maliyet 58]   │ │  Yıkım Oranı: %41.6      │   │
│  │                                  │ │                            │   │
│  └──────────────────────────────────┘ └────────────────────────────┘   │
│                                                                        │
│  ┌─── Exergoekonomik Özet ─────────────────────────────────────────┐  │
│  │                                                                  │  │
│  │  f = 0.62        r = 1.9        Ż = 2.5 EUR/h    Ċ_D = 1.5    │  │
│  │  ████████████░   ████░░░░░░░░   Yatırım ağırlıklı  EUR/h       │  │
│  │  Yatırım baskın  Düşük artış    ─────────────────  Yıkım mal.  │  │
│  │                                                                  │  │
│  │  Yorum: Yatırım maliyeti baskın (f>0.5). Parametrik             │  │
│  │  optimizasyon öncelikli — ekipman değişimi gerekmez.             │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 5.3 Component Yapısı

**Kaldırılan componentler:**
- `MetricBar.jsx` → `HeroScoreBanner.jsx` ile değiştirildi (tab dışına taşındı)
- `MetricsCard.jsx` → gereksiz, banner zaten gösteriyor

**Değiştirilen componentler:**
- `OverviewTab.jsx` — tamamen yeniden yazılacak

**Yeni componentler:**
- `AIInsightCard.jsx` — Kısa AI özet kartı (3-4 cümle max)
- `ExergoeconomicSummary.jsx` — f/r faktör görsel özeti
- `DestructionBreakdown.jsx` — AV/UN yeni görsel (horizontal stacked bar yerine)

**Mevcut korunan:**
- `RadarBenchmark.jsx` — ama boyut büyütülecek, legend düzeltilecek

### 5.4 Radar Chart Düzeltmeleri

```jsx
// RadarBenchmark.jsx değişiklikleri

// 1. Layout boyutu artırılacak
const layout = {
  width: 400,   // eski: ~300
  height: 400,  // eski: ~300
  polar: {
    radialaxis: {
      range: [0, 100],
      tickvals: [25, 50, 75, 100],
      tickfont: { size: 11 }
    },
    angularaxis: {
      // TAM İSİMLER, kısaltma yok
      tickfont: { size: 12 },
    }
  },
  showlegend: false,  // legend yerine altında badge'ler
  margin: { t: 30, b: 30, l: 60, r: 60 }
};

// 2. Eksen isimleri kısaltılmayacak
const AXIS_LABELS = {
  exergy_efficiency: 'Ekserji Verimi',
  improvement_status: 'İyileştirme',
  sector_ranking: 'Sektör Sırası',
  heat_recovery: 'Isı Geri Kaz.',    // max 14 karakter
  destruction_ratio: 'Yıkım Oranı',
  cost_efficiency: 'Maliyet Ver.'
};

// 3. Legend yerine altında 6 mini badge
// Her badge: [renkli nokta] [isim] [puan]
// 3x2 grid layout
```

### 5.5 AI Insight Card

```jsx
// AIInsightCard.jsx
// Konum: Overview tab'ın EN ÜSTÜnde
// Kaynak: interpretation.summary (AI'ın ilk paragrafı)

const AIInsightCard = ({ summary, topRecommendation, onViewDetails }) => (
  <div className="bg-gradient-to-r from-violet-50 to-blue-50 border border-violet-200
                  rounded-xl p-5 mb-6">
    <div className="flex items-start gap-3">
      <div className="w-8 h-8 bg-violet-100 rounded-lg flex items-center justify-center
                      flex-shrink-0 mt-0.5">
        <Sparkles className="w-4 h-4 text-violet-600" />
      </div>
      <div className="flex-1">
        <p className="text-slate-700 text-sm leading-relaxed">{summary}</p>
        {topRecommendation && (
          <p className="text-violet-700 text-sm font-medium mt-2">
            → En yüksek ROI: {topRecommendation.title} ({topRecommendation.payback})
          </p>
        )}
      </div>
      <button onClick={onViewDetails}
              className="text-violet-600 text-sm font-medium whitespace-nowrap
                         hover:text-violet-800 transition-colors">
        Detaylı Analiz →
      </button>
    </div>
  </div>
);
```

---

## 6. Tab 2: Akış Analizi — Redesign

### 6.1 Mevcut Sorunlar
- Sankey taşma/kaybolma
- Label kesme ("Exe...")
- Detaylı Metrikler ve Yıllık Etki alt kısımda sıkıcı

### 6.2 Yeni Layout

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│  ┌─── Ekserji Akış Diyagramı ──────────────────────────────────────┐  │
│  │                                                   [🔍+] [🔍-]   │  │
│  │                                                   [↺ Sıfırla]   │  │
│  │                                                                  │  │
│  │   ┌────────────┐    ┌─────────────┐    ┌────────────────────┐   │  │
│  │   │  Elektrik   │───→│  Kompresör  │───→│  Basınçlı Hava     │   │  │
│  │   │  Enerjisi   │    │             │    │  (Faydalı)         │   │  │
│  │   │  37 kW      │    │             │───→│  Yıkım — Kaçınılmaz│  │  │
│  │   └────────────┘    └─────────────┘    │  Yıkım — Kaçınıla. │   │  │
│  │                                        │  Isı (Geri Kaz.)    │   │  │
│  │                                        └────────────────────┘   │  │
│  │                                                                  │  │
│  │  Container: overflow-hidden, fixed height, zoom/pan controls     │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  ┌─── Benchmark ────────────┐ ┌─── Detaylı Metrikler ──────────────┐  │
│  │                           │ │                                     │  │
│  │  Sektör: İlk %34         │ │  ┌ Ekserji Dengesi ──────────────┐ │  │
│  │  ████████████████▎░░░░░░  │ │  │ Giriş   37.0 kW              │ │  │
│  │  0%    58.4%        70%   │ │  │ Faydalı 21.6 kW  ███████░░   │ │  │
│  │                           │ │  │ Yıkım   15.4 kW  █████░░░░   │ │  │
│  │  İyi seviye. Sınırlı      │ │  └───────────────────────────────┘ │  │
│  │  iyileştirme potansiyeli.  │ │                                     │  │
│  │                           │ │  ┌ Ekonomik Göstergeler ─────────┐ │  │
│  └───────────────────────────┘ │  │ f-faktör    0.6               │ │  │
│                                 │  │ r-faktör    1.9               │ │  │
│                                 │  │ Ż           2.5  EUR/h       │ │  │
│                                 │  │ Ċ_D         1.5  EUR/h       │ │  │
│                                 │  │ c_P         0.3  EUR/kWh     │ │  │
│                                 │  │ Toplam      4.0  EUR/h       │ │  │
│                                 │  └───────────────────────────────┘ │  │
│                                 │                                     │  │
│                                 │  ┌ Yıllık Etki ────────────────┐  │  │
│                                 │  │ Kayıp  61,542 kWh  €6,154   │  │  │
│                                 │  │ Kaz.    9.2 kW  →  €1,538/yıl│ │  │
│                                 │  └───────────────────────────────┘ │  │
│                                 └─────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

### 6.3 Sankey Fix

```jsx
// SankeyDiagram.jsx değişiklikleri

// 1. Container: sabit yükseklik + overflow hidden
<div className="relative" style={{ height: '400px', overflow: 'hidden' }}>
  <Plot
    data={sankeyData}
    layout={{
      ...layout,
      dragmode: false,        // Sürüklemeyi kapat
      // VEYA
      dragmode: 'pan',        // Sadece pan, node sürükleme değil
    }}
    config={{
      displayModeBar: false,  // Plotly toolbar gizle
      scrollZoom: false,      // Scroll zoom kapat
      staticPlot: false,      // Hover tooltip çalışsın
    }}
  />
  {/* Zoom kontrolleri */}
  <div className="absolute top-3 right-3 flex gap-1">
    <button className="p-1.5 bg-white/80 rounded shadow-sm hover:bg-white">
      <ZoomIn size={16} />
    </button>
    <button className="p-1.5 bg-white/80 rounded shadow-sm hover:bg-white">
      <ZoomOut size={16} />
    </button>
    <button className="p-1.5 bg-white/80 rounded shadow-sm hover:bg-white">
      <RotateCcw size={16} />
    </button>
  </div>
</div>

// 2. Label kısaltma yerine tooltip
// Sankey node labels: kısa isim göster, hover'da tam isim + değer
const sankeyTrace = {
  node: {
    label: shortLabels,       // "Basınçlı Hava", "Yıkım (AV)"
    customdata: fullLabels,   // Tooltip için tam veri
    hovertemplate: '%{customdata}<extra></extra>'
  }
};
```

### 6.4 Detaylı Metrikler — Gruplu Kart

Mevcut düz tablo yerine **3 gruplanmış kart**:

```jsx
// DetailedMetrics.jsx (YENİ)
// Mevcut uzun tabloyu 3 gruba ayır:

const MetricGroup = ({ title, icon, metrics }) => (
  <div className="bg-white rounded-lg border border-slate-200 p-4">
    <h4 className="text-sm font-medium text-slate-500 flex items-center gap-2 mb-3">
      {icon} {title}
    </h4>
    <div className="space-y-2">
      {metrics.map(m => (
        <div key={m.label} className="flex justify-between items-center">
          <span className="text-sm text-slate-600">{m.label}</span>
          <span className={`text-sm font-semibold tabular-nums ${m.colorClass}`}>
            {m.value} <span className="text-slate-400 font-normal">{m.unit}</span>
          </span>
        </div>
      ))}
    </div>
  </div>
);

// Gruplar:
// 1. Ekserji Dengesi: Giriş, Faydalı, Yıkım, AV, UN, Oran
// 2. Ekonomik Göstergeler: f, r, Ż, Ċ_D, c_P, Toplam
// 3. Yıllık Etki: Kayıp kWh, Kayıp EUR, Geri Kazanım, Potansiyel Tasarruf
```

---

## 7. Tab 3: AI Danışman — BÜYÜK Redesign

Bu tab en çok değişecek alan. Mevcut: 3 ekran scroll metin duvarı. Hedef: taranabilir, aksiyonlanabilir dashboard.

### 7.1 Yeni Mimari: Chat Ayrılıyor

**KRİTİK KARAR:** Chat, AI tab'dan ayrılıp **floating panel** oluyor. AI tab sadece analiz sonuçlarını gösterir.

### 7.2 Yeni Layout

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│  ┌─── AI Analiz Özeti ───────────────────────────────────────────┐    │
│  │  [Kopyala 📋] [PDF 📄]                        Claude Code     │    │
│  │                                                                │    │
│  │  37 kW vidalı kompresör %58.4 ekserji verimi ile iyi          │    │
│  │  seviyede çalışmaktadır...                                    │    │
│  │  (2-3 paragraf MAX, expand butonu ile devamı)                 │    │
│  │                                           [Devamını oku ▼]    │    │
│  └────────────────────────────────────────────────────────────────┘    │
│                                                                        │
│  ┌─── Önemli Bulgular ───────────────────────────────────────────┐    │
│  │  ✓ Verim %58.4 — iyi kategorisi, best-in-class'a yakın       │    │
│  │  ⚠ Yıkımın %63.8'i kaçınılamaz — gerçek potansiyel 5.56 kW  │    │
│  │  ↑ 9.15 kW atık ısı geri kazanım potansiyeli                 │    │
│  │  ◉ θ = 0.362 — anlamlı tasarruf marjı mevcut                 │    │
│  └────────────────────────────────────────────────────────────────┘    │
│                                                                        │
│  ┌─── İyileştirme Önerileri ─────────────────────────────────────┐    │
│  │                                                                │    │
│  │  ┌ 1. Atık Isı Geri Kazanımı (HRU) ─── Yüksek Öncelik ────┐ │    │
│  │  │                                                           │ │    │
│  │  │  ┌─────────┐  ┌──────────┐  ┌────────────┐              │ │    │
│  │  │  │ €1,538  │  │  €4,000  │  │  2.6 yıl   │              │ │    │
│  │  │  │ Tasarruf │  │  Yatırım │  │  Geri Ödeme│              │ │    │
│  │  │  └─────────┘  └──────────┘  └────────────┘              │ │    │
│  │  │                                                           │ │    │
│  │  │  Kompresör atık ısısından 9.15 kW termal enerji...       │ │    │
│  │  │                                      [Detay ▼]           │ │    │
│  │  └───────────────────────────────────────────────────────────┘ │    │
│  │                                                                │    │
│  │  ┌ 2. Kaçak Tespit ve Onarım ─── Yüksek Öncelik ───────────┐│    │
│  │  │  €615 / €500 / 0.8 yıl                                   ││    │
│  │  │  (varsayılan: kapalı — tıkla aç)              [Detay ▼]  ││    │
│  │  └───────────────────────────────────────────────────────────┘│    │
│  │                                                                │    │
│  │  ┌ 3. Sistem Basıncı Opt. ─── Orta Öncelik ─────────────────┐│    │
│  │  │  €430 / €200 / 0.5 yıl                       [Detay ▼]   ││    │
│  │  └───────────────────────────────────────────────────────────┘│    │
│  │                                                                │    │
│  │  ┌ 4. Periyodik Bakım ─── Orta Öncelik ─────────────────────┐│    │
│  │  │  €300 / €500 / 1.7 yıl                       [Detay ▼]   ││    │
│  │  └───────────────────────────────────────────────────────────┘│    │
│  └────────────────────────────────────────────────────────────────┘    │
│                                                                        │
│  ┌─── Önerilmeyen Çözümler (collapse) ──────── [Aç/Kapat ▼] ────┐   │
│  │  (varsayılan: kapalı)                                          │   │
│  └────────────────────────────────────────────────────────────────┘   │
│                                                                        │
│  ┌─── Aksiyon Planı (collapse) ──────────────── [Aç/Kapat ▼] ────┐  │
│  │  (varsayılan: kapalı — timeline görünümü)                       │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 7.3 Öneri Kartı Yeni Tasarım

Her öneri kartı: **kolayca taranabilir, sayılar öne çıkıyor**

```jsx
// RecommendationCard.jsx (YENİ)

const RecommendationCard = ({ rec, index, defaultOpen = false }) => {
  const [isOpen, setIsOpen] = useState(defaultOpen);

  return (
    <div className="border border-slate-200 rounded-lg overflow-hidden">
      {/* Header — her zaman görünür */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex items-center justify-between p-4 hover:bg-slate-50
                   transition-colors text-left"
      >
        <div className="flex items-center gap-3">
          <span className="text-sm font-bold text-slate-400">
            {index + 1}.
          </span>
          <span className="font-medium text-slate-800">
            {rec.title}
          </span>
          <PriorityBadge priority={rec.priority} />
        </div>

        {/* Mini KPI'lar — kapalıyken bile görünür */}
        <div className="flex items-center gap-4 mr-4">
          <KPIMini label="Tasarruf" value={`€${rec.savings}`} color="emerald" />
          <KPIMini label="Yatırım" value={`€${rec.investment}`} color="slate" />
          <KPIMini label="Geri Ödeme" value={rec.payback} color="blue" />
          <ChevronDown className={`w-4 h-4 transition-transform
                       ${isOpen ? 'rotate-180' : ''}`} />
        </div>
      </button>

      {/* Detail — açılır/kapanır */}
      {isOpen && (
        <div className="px-4 pb-4 pt-0 border-t border-slate-100">
          <p className="text-sm text-slate-600 leading-relaxed mt-3">
            {rec.description}
          </p>
        </div>
      )}
    </div>
  );
};

// İlk öneri varsayılan açık, kalanlar kapalı
```

### 7.4 Aksiyon Planı — Timeline Görünümü

Mevcut bullet-list yerine horizontal timeline:

```
  ○ Hemen           ○ Kısa Vade (1-3 ay)      ○ Orta Vade (3-12 ay)
  │                  │                           │
  ├─ Kaçak tarama    ├─ Kaçak onarım            ├─ HRU montajı
  ├─ Basınç tespiti  ├─ Basınç optimizasyonu    ├─ Kaçak tarama programı
  ├─ Filtre kontrol  ├─ Fizibilite hazırlığı    ├─ Sensör sistemi kurulumu
```

Implementasyon: 3 sütunlu grid, her sütun bir zaman dilimi.

```jsx
const ActionTimeline = ({ actions }) => {
  const groups = {
    immediate: actions.filter(a => a.timeframe === 'immediate'),
    short: actions.filter(a => a.timeframe === 'short_term'),
    medium: actions.filter(a => a.timeframe === 'medium_term')
  };

  return (
    <div className="grid grid-cols-3 gap-4">
      <TimelineColumn title="Hemen" icon={Zap} items={groups.immediate}
                      color="red" />
      <TimelineColumn title="1-3 Ay" icon={Calendar} items={groups.short}
                      color="amber" />
      <TimelineColumn title="3-12 Ay" icon={Target} items={groups.medium}
                      color="blue" />
    </div>
  );
};
```

---

## 8. Floating Chat Panel

### 8.1 Konsept

Chat, AI tab'ına gömülü olmak yerine **her tab'dan erişilebilir floating panel** olacak.

```
                                                    ┌─────────────────────┐
                                                    │ 💬 AI Danışmanı     │
                                                    │ ──────────────────  │
                                                    │ Merhaba! Bu komp.   │
                                                    │ analizi hakkında     │
                                                    │ sorularınızı         │
                                                    │ yanıtlayabilirim.   │
                                                    │                     │
                                                    │ [Exergy verimini    │
                                                    │  nasıl artırabili.] │
                                                    │                     │
                                                    │ [Bu sonuçlar sekt.  │
                                                    │  benchmark ile...]  │
                                                    │                     │
                                                    │ ┌─────────────────┐ │
                                                    │ │ Sorunuzu yazın  │ │
                                                    │ └─────────────────┘ │
                                                    └─────────────────────┘

  Kapalı hali: Sağ alt köşede FAB (Floating Action Button)
  ┌──────┐
  │  💬  │  ← tıkla → panel açılır
  │      │
  └──────┘
```

### 8.2 Implementasyon

```jsx
// FloatingChat.jsx (YENİ)
// Konum: EquipmentAnalysis.jsx seviyesinde, tab'ların dışında

const FloatingChat = ({ analysisResult, equipmentType }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      {/* FAB Button */}
      {!isOpen && (
        <button
          onClick={() => setIsOpen(true)}
          className="fixed bottom-6 right-6 w-14 h-14 bg-violet-600 text-white
                     rounded-full shadow-lg hover:bg-violet-700 transition-all
                     hover:scale-105 flex items-center justify-center z-50"
        >
          <MessageCircle size={24} />
        </button>
      )}

      {/* Chat Panel */}
      {isOpen && (
        <div className="fixed bottom-6 right-6 w-96 h-[500px] bg-white rounded-2xl
                        shadow-2xl border border-slate-200 flex flex-col z-50
                        animate-in slide-in-from-bottom-4">
          {/* Header */}
          <div className="flex items-center justify-between p-4 border-b
                          bg-gradient-to-r from-violet-600 to-blue-600
                          rounded-t-2xl">
            <div className="flex items-center gap-2 text-white">
              <Bot size={20} />
              <span className="font-medium">AI Danışmanı</span>
            </div>
            <button onClick={() => setIsOpen(false)}
                    className="text-white/80 hover:text-white">
              <X size={18} />
            </button>
          </div>

          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-4">
            {/* Mevcut ChatPanel.jsx mantığı buraya taşınır */}
          </div>

          {/* Input */}
          <div className="p-3 border-t">
            <div className="flex gap-2">
              <input className="flex-1 border rounded-lg px-3 py-2 text-sm"
                     placeholder="Sorunuzu yazın..." />
              <button className="p-2 bg-violet-600 text-white rounded-lg">
                <Send size={16} />
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};
```

---

## 9. Tab 4: Senaryo — Redesign

### 9.1 Mevcut Sorunlar
- Tek slider görünüyor
- Karşılaştırma tablosu düz
- Radar karşılaştırma küçük

### 9.2 Yeni Layout

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│  ┌─── What-If Senaryo Modu ──────────────────────────────────────┐    │
│  │                                                                │    │
│  │  Parametreleri değiştirerek alternatif senaryoları test edin.  │    │
│  │                                                                │    │
│  │  ┌ Çıkış Sıcaklığı (°C) ─────────────────────────────────┐   │    │
│  │  │  [===●==========] 85 → 61    Mevcut: 85 │ Senaryo: 61 │   │    │
│  │  └────────────────────────────────────────────────────────┘   │    │
│  │                                                                │    │
│  │  ┌ Çıkış Basıncı (bar) ──────────────────────────────────┐   │    │
│  │  │  [===========●===] 7.5 → 7.5   (değişmedi)            │   │    │
│  │  └────────────────────────────────────────────────────────┘   │    │
│  │  ... (tüm değiştirilebilir parametreler slider ile)           │    │
│  │                                                                │    │
│  │  [🔄 Karşılaştır]  [↺ Sıfırla]                               │    │
│  └────────────────────────────────────────────────────────────────┘    │
│                                                                        │
│  ┌─── Sonuç: Etki Özeti ────────────────────────────────────────┐     │
│  │                                                                │    │
│  │   Ekserji Tasarrufu     Yıllık Tasarruf     Maliyet Tasarrufu │    │
│  │   ┌─────────────┐      ┌─────────────┐     ┌─────────────┐   │    │
│  │   │   +0.4 kW   │      │  +240 kWh   │     │  +€164/yıl  │   │    │
│  │   │     ↑ 2.6%  │      │              │     │             │   │    │
│  │   └─────────────┘      └─────────────┘     └─────────────┘   │    │
│  │                                                                │    │
│  └────────────────────────────────────────────────────────────────┘    │
│                                                                        │
│  ┌── Metrik Karşılaştırma ─────┐  ┌── Radar Karşılaştırma ───────┐   │
│  │                              │  │                               │   │
│  │  Metrik     Mevcut  Senaryo  │  │     (Büyük radar — 2 layer)  │   │
│  │  ─────────────────────────── │  │                               │   │
│  │  Verim(%)   58.4   57.3 ▼   │  │     ── Mevcut (60.7)         │   │
│  │  Yıkım(kW) 15.39  15.79 ▲  │  │     ── Senaryo (60.2)        │   │
│  │  ...                         │  │                               │   │
│  │                              │  │                               │   │
│  │  ▲ = kötüleşme (kırmızı)    │  │                               │   │
│  │  ▼ = iyileşme (yeşil)       │  │                               │   │
│  └──────────────────────────────┘  └───────────────────────────────┘   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 9.3 Değişiklikler

1. **Tüm parametreler slider ile gösterilecek** (sadece değiştirilebilir olanlar)
2. **Sonuç kartları renkli** — iyileşme yeşil, kötüleşme kırmızı, nötr gri
3. **Karşılaştırma tablosunda ok ve renk kodu** — ▲ kırmızı (kötü yönde), ▼ yeşil (iyi yönde)
4. **Radar chart büyük** — yan yana yerine tablo + radar aynı satırda
5. **İyileşme/kötüleşme delta'ları büyük ve renkli**

```jsx
// DeltaCard.jsx
const DeltaCard = ({ label, value, unit, isImprovement }) => (
  <div className={`rounded-xl p-4 text-center ${
    isImprovement
      ? 'bg-emerald-50 border border-emerald-200'
      : 'bg-red-50 border border-red-200'
  }`}>
    <div className={`text-2xl font-bold tabular-nums ${
      isImprovement ? 'text-emerald-700' : 'text-red-700'
    }`}>
      {value > 0 ? '+' : ''}{value} {unit}
    </div>
    <div className="text-sm text-slate-500 mt-1">{label}</div>
  </div>
);
```

---

## 10. Ortak Stil ve Component Kararları

### 10.1 Kart Stili (Tutarlı)

```jsx
// 3 kart seviyesi:

// Level 1: Yüzey kartı (temel container)
const SurfaceCard = "bg-white rounded-xl border border-slate-200"

// Level 2: Öne çıkan kart (hero elements)
const ElevatedCard = "bg-white rounded-xl shadow-md border border-slate-100"

// Level 3: Vurgulu kart (AI, uyarı, sonuç)
const AccentCard = "rounded-xl border-l-4"  // + border-l rengi dinamik
```

### 10.2 Başlık Hiyerarşisi

```css
/* H1: Sayfa başlığı */
.page-title { @apply text-2xl font-bold text-slate-900; }

/* H2: Bölüm başlığı (kart başlığı) */
.section-title { @apply text-lg font-semibold text-slate-800; }

/* H3: Alt bölüm */
.subsection-title { @apply text-base font-medium text-slate-700; }

/* Label: Metrik etiketi */
.metric-label { @apply text-xs font-medium text-slate-500 uppercase tracking-wide; }

/* Value: Metrik değeri */
.metric-value { @apply text-xl font-bold text-slate-900 tabular-nums; }
```

### 10.3 Spacing Sistemi

```
Sayfa padding: p-6
Kart arası: space-y-6
Kart iç padding: p-5
İçerik grupları arası: space-y-4
İçerik satırları arası: space-y-2
```

### 10.4 Animasyonlar

```css
/* Sayfa geçişi */
.tab-content-enter { animation: fadeIn 200ms ease-out; }

/* Kart açılma (accordion) */
.accordion-content {
  overflow: hidden;
  transition: max-height 300ms ease-out, opacity 200ms ease-out;
}

/* Gauge animasyonu */
.gauge-arc {
  transition: stroke-dashoffset 800ms cubic-bezier(0.4, 0, 0.2, 1);
}

/* Sayı değişimi */
.metric-value {
  transition: color 200ms ease;
}
```

---

## 11. Dosya Yapısı Değişiklikleri

### 11.1 Yeni/Değişen Dosyalar

```
components/
│
├── dashboard/
│   ├── HeroScoreBanner.jsx      ← YENİ (MetricBar.jsx yerine)
│   ├── GaugeChart.jsx            ← YENİ (SVG gauge)
│   ├── OverviewTab.jsx           ← TAM YENİDEN YAZIM
│   ├── FlowTab.jsx               ← GÜNCELLEME (Sankey fix + layout)
│   ├── AITab.jsx                 ← TAM YENİDEN YAZIM
│   ├── ScenarioTab.jsx           ← GÜNCELLEME (slider'lar, renkli delta)
│   ├── TabContainer.jsx          ← KORUNUYOR
│   ├── DashboardLayout.jsx       ← GÜNCELLEME (floating chat ekleme)
│   ├── ParameterSidebar.jsx      ← KORUNUYOR
│   ├── MetricBar.jsx             ← SİLİNECEK (HeroScoreBanner ile değişti)
│   └── AIActionBar.jsx           ← SİLİNECEK (AI tab'a gömüldü)
│
├── results/
│   ├── AIInsightCard.jsx         ← YENİ
│   ├── RecommendationCard.jsx    ← YENİ
│   ├── ActionTimeline.jsx        ← YENİ
│   ├── DestructionBreakdown.jsx  ← YENİ (AV/UN yeni görsel)
│   ├── ExergoeconomicSummary.jsx ← YENİ
│   ├── DetailedMetrics.jsx       ← YENİ (gruplu metrikler)
│   ├── DeltaCard.jsx             ← YENİ
│   ├── AIInterpretation.jsx      ← SİLİNECEK (parçalanıp yeni comp'lara)
│   ├── RadarBenchmark.jsx        ← GÜNCELLEME (boyut, legend)
│   ├── SankeyDiagram.jsx         ← GÜNCELLEME (overflow fix, kontroller)
│   ├── BenchmarkChart.jsx        ← KORUNUYOR
│   ├── MetricsCard.jsx           ← SİLİNECEK (DetailedMetrics ile değişti)
│   └── SolutionsList.jsx         ← KORUNUYOR
│
├── chat/
│   ├── FloatingChat.jsx          ← YENİ (ChatPanel.jsx wrap + FAB)
│   └── ChatPanel.jsx             ← GÜNCELLEME (floating panel uyumu)
│
├── whatif/
│   ├── ScenarioEditor.jsx        ← GÜNCELLEME (tüm parametreler)
│   ├── ComparisonPanel.jsx       ← GÜNCELLEME (renkli delta)
│   └── RadarComparison.jsx       ← GÜNCELLEME (büyük boyut)
```

### 11.2 Silinen Dosyalar (4)
- `dashboard/MetricBar.jsx` → HeroScoreBanner
- `dashboard/AIActionBar.jsx` → AI tab'a gömüldü
- `results/AIInterpretation.jsx` → Parçalandı (AIInsightCard + RecommendationCard + ActionTimeline)
- `results/MetricsCard.jsx` → DetailedMetrics

### 11.3 Yeni Dosyalar (9)
- `dashboard/HeroScoreBanner.jsx`
- `dashboard/GaugeChart.jsx`
- `results/AIInsightCard.jsx`
- `results/RecommendationCard.jsx`
- `results/ActionTimeline.jsx`
- `results/DestructionBreakdown.jsx`
- `results/ExergoeconomicSummary.jsx`
- `results/DetailedMetrics.jsx`
- `chat/FloatingChat.jsx`

---

## 12. Test Planı

### 12.1 Mevcut Testler — Regresyon Kontrolü

Tüm mevcut 671 test geçmeye devam etmeli. Frontend değişiklikleri backend'i ETKİLEMEZ.

### 12.2 Manuel Test Senaryoları

| # | Senaryo | Kontrol Noktası |
|---|---------|-----------------|
| T1 | 7 ekipman tipi analiz çalıştır | HeroScoreBanner doğru metrikler, renk kodu |
| T2 | Kompresör — Overview tab | Radar 6 eksen okunabilir, legend tam |
| T3 | Kompresör — Akış tab | Sankey taşmıyor, zoom kontrolleri çalışıyor |
| T4 | Kompresör — AI tab | Öneriler accordion açılıyor/kapanıyor, KPI görünür |
| T5 | Kompresör — Senaryo tab | Tüm parametreler slider ile değiştirilebilir |
| T6 | Floating chat açılıyor/kapanıyor | FAB tıkla → panel açılır, X tıkla → kapanır |
| T7 | Chat tab dışında çalışıyor | Overview'deyken chat açıp soru sorabilme |
| T8 | AI yorumu olmadan dashboard | AI bölümleri graceful degradation (loading/yok) |
| T9 | Küçük ekran (1366x768) | Layout bozulmuyor, scroll çalışıyor |
| T10 | Büyük ekran (1920x1080) | Content max-width ile ortalanıyor |

---

## 13. Implementasyon Sırası

Önerilen uygulama sırası (incremental, her adımda çalışır halde):

### Faz 1: Temel Yapı (En az risk)
1. `GaugeChart.jsx` oluştur (bağımsız SVG component)
2. `HeroScoreBanner.jsx` oluştur (GaugeChart kullan)
3. `EquipmentAnalysis.jsx` güncelle: MetricBar → HeroScoreBanner
4. Test: 7 ekipman tipi doğru metrik gösteriyor mu

### Faz 2: Overview Tab
5. `AIInsightCard.jsx` oluştur
6. `DestructionBreakdown.jsx` oluştur
7. `ExergoeconomicSummary.jsx` oluştur
8. `RadarBenchmark.jsx` güncelle (boyut, legend)
9. `OverviewTab.jsx` yeniden yaz
10. Test: Overview doğru veriyi gösteriyor, radar okunabilir

### Faz 3: Akış Tab
11. `SankeyDiagram.jsx` güncelle (overflow fix, kontroller)
12. `DetailedMetrics.jsx` oluştur (gruplu)
13. `FlowTab.jsx` güncelle (yeni layout)
14. Test: Sankey taşmıyor, metrikler gruplu

### Faz 4: AI Tab
15. `RecommendationCard.jsx` oluştur
16. `ActionTimeline.jsx` oluştur
17. `AITab.jsx` yeniden yaz
18. Test: Accordion çalışıyor, KPI'lar görünür

### Faz 5: Chat + Senaryo
19. `FloatingChat.jsx` oluştur (ChatPanel'i wrap et)
20. `DashboardLayout.jsx` güncelle (floating chat ekle)
21. `AITab.jsx` güncelle (chat bölümünü kaldır)
22. `ScenarioTab.jsx` güncelle (slider'lar, renkli delta)
23. Test: Chat her tab'da çalışıyor

### Faz 6: Temizlik
24. `MetricBar.jsx` sil
25. `AIActionBar.jsx` sil (dashboard/)
26. `AIInterpretation.jsx` sil
27. `MetricsCard.jsx` sil
28. Import referanslarını temizle
29. Son regression test: 671+ test geçiyor

---

## 14. Başarı Kriterleri

| Kriter | Ölçüm |
|--------|-------|
| 3-saniye kuralı | Verimlilik skoru 3 saniyede görülebilir |
| Scroll azaltma | AI tab max 1.5 ekran scroll (eskiden 3+) |
| Chat erişilebilirlik | Her tab'dan 1 tıkla chat açılabilir |
| Sankey stabil | Taşma/kaybolma yok, zoom çalışıyor |
| Radar okunabilir | 6 eksen ismi tam okunabiliyor |
| Tutarlı estetik | Tüm kartlar aynı stil sistemi |
| Regresyon yok | 671 test hâlâ geçiyor |

---

*Bu BRIEF, Claude Code implementasyonu için hazırlanmıştır.*
*Tahmini effort: 5 Faz, ~25 dosya, ~2,000 satır net değişiklik.*
*Mevcut test sayısı etkilenmez (frontend-only değişiklik).*
