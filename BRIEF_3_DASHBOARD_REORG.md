# BRIEF 3: Dashboard Reorganizasyonu — 9 Tab → 6 Tab + Gap Analysis

> **Tarih:** 2026-02-07
> **Öncelik:** Yüksek — Brief 1 + Brief 2 tamamlandıktan sonra
> **Bağımlılık:** Brief 1 (gap_analysis verisi), Brief 2 (proses tanımı UI)
> **Dokunduğu Dosyalar:** frontend/ + knowledge/ + skills/
> **Tahmini:** ~1200 satır değişiklik

---

## 1. Amaç

Fabrika dashboard'unu bir "analiz hikayesi" anlatacak şekilde yeniden yapılandırmak.
Mevcut 9 bağımsız tab'ı 6 anlamlı bölüme indirmek. Gap Analysis görselleştirmesi eklemek.

---

## 2. Tab Dönüşüm Planı

### Mevcut (9 tab):
```
AI Yorum · Öncelikler · Sankey · Pinch · İleri Exergy · EGM · Termoekonomik · Enerji Yönetimi · Envanter
```

### Yeni (6 tab):
```
🎯 Proses · 📊 Genel Bakış · 🔥 Exergy Akışı · 🔬 Derin Analiz · 💡 Aksiyon Planı · 📋 Yönetim
```

### Dönüşüm Detayı:

| Yeni Tab | İçerik | Eski Karşılık |
|----------|--------|---------------|
| **Proses Analizi** | Gap Analysis görselleştirme (waterfall, bar, pie, ESI) | ⭐ YENİ |
| **Genel Bakış** | AI Yorum + Hotspot/Öncelik listesi + Envanter özeti | AI Yorum + Öncelikler + Envanter birleşimi |
| **Exergy Akışı** | Factory Sankey V2 (3 mod) | Sankey tab'ı (aynen) |
| **Derin Analiz** | Alt sekmeli: Pinch \| İleri Exergy \| EGM | Pinch + İleri Exergy + EGM birleşimi |
| **Aksiyon Planı** | Termoekonomik f/r matrisi + Entegrasyon fırsatları + AI öneriler | Termoekonomik + AI entegrasyon |
| **Enerji Yönetimi** | ISO 50001 olgunluk + Envanter (tam liste) | Enerji Yönetimi + Envanter birleşimi |

---

## 3. Hikaye Akışı

Dashboard şu hikayeyi anlatacak:

```
1. PROSES    → "Bu fabrika ne yapıyor ve idealden ne kadar uzak?"
2. GENEL     → "Ana sorunlar ne, hangi ekipmanlar problematik?"
3. AKIŞ      → "Exergy fabrikada nasıl akıyor, nerede kayboluyor?"
4. DERİN     → "Kayıpların kök nedeni ne? (Pinch, AV/UN, Bejan)"
5. AKSİYON   → "Ne yapmalıyız? Maliyet-fayda analizi?"
6. YÖNETİM   → "Organizasyonel olgunluğumuz ne seviyede?"
```

---

## 4. Tab 1: Proses Analizi (YENİ)

### 4.1 Yeni Bileşen: `GapAnalysisTab.jsx` (~350 satır)

**Proses tanımı varsa:**

```
┌─────────────────────────────────────────────────────────────────────┐
│ PROSES ANALİZİ                                                      │
│                                                                     │
│ ┌─ Proses Kartı ─────────────────────────────────────────────────┐  │
│ │ 🔥 Kurutma — Tahıl Kurutma                                    │  │
│ │ Malzeme: 1000 kg/h, %20 → %5 nem, 150 kg/h su uzaklaştırma   │  │
│ │ Çalışma: 6000 saat/yıl | Enerji fiyatı: €0.08/kWh  [✏️ Düzenle]│  │
│ └────────────────────────────────────────────────────────────────┘  │
│                                                                     │
│ ┌─ ESI Skoru ──────┐  ┌─ İdeal Mesafe ─┐  ┌─ BAT Mesafe ──┐      │
│ │    F              │  │  İdealin       │  │  BAT'ın       │      │
│ │   0.0015          │  │  667x          │  │  52x          │      │
│ │ Kritik — büyük    │  │  fazlası       │  │  fazlası      │      │
│ │ dönüşüm gerekli   │  │               │  │               │      │
│ └──────────────────┘  └────────────────┘  └───────────────┘      │
│                                                                     │
│ ┌─ 3 Katman Karşılaştırma ──────────────────────────────────────┐  │
│ │                                                                │  │
│ │  Minimum   ██  2.1 kW                                         │  │
│ │  BAT       ████████████  27.0 kW                              │  │
│ │  Mevcut    ████████████████████████████████████████  1,400 kW  │  │
│ │                                                                │  │
│ │  Plotly horizontal bar chart (logaritmik ölçek)                │  │
│ └────────────────────────────────────────────────────────────────┘  │
│                                                                     │
│ ┌─ Gap Waterfall ───────────────────────────────────────────────┐  │
│ │                                                                │  │
│ │  Min → Tek.Limit → Kazan → Kurutma → Diğer → Mevcut          │  │
│ │  Plotly waterfall chart                                        │  │
│ │                                                                │  │
│ └────────────────────────────────────────────────────────────────┘  │
│                                                                     │
│ ┌─ Gap Dağılımı ──────────────┐  ┌─ Ekonomik Etki ──────────┐     │
│ │                              │  │                           │     │
│ │  Plotly donut chart          │  │ Toplam Gap: €659,040/yıl  │     │
│ │  Kazan: %46                  │  │ BAT Gap:    €629,760/yıl  │     │
│ │  Kurutma: %26                │  │                           │     │
│ │  Dağıtım: %18               │  │ BAT Teknoloji:            │     │
│ │  Diğer: %10                  │  │ Isı pompalı kurutucu +    │     │
│ │                              │  │ atık ısı geri kazanımı    │     │
│ └──────────────────────────────┘  │                           │     │
│                                    │ Kaynak: EU BREF (2019)   │     │
│                                    └───────────────────────────┘     │
│                                                                     │
│ ┌─ Hesaplama Detayları ─────────────────────────────────────────┐  │
│ │ Metot: Chemical exergy of water removal (Dincer & Rosen)      │  │
│ │ Varsayımlar:                                                   │  │
│ │ • Buharlaştırma exergisi: 50 kJ/kg su @25°C                   │  │
│ │ • Ortam bağıl nemi %60 varsayılmış                             │  │
│ └────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

**Proses tanımı yoksa:**

```
┌──────────────────────────────────────────────────────┐
│  ℹ️ Proses tanımı eklenmemiş.                        │
│                                                      │
│  Proses tanımı ekleyerek şunları öğrenebilirsiniz:   │
│  • Fabrikanız termodinamik ideale ne kadar uzak      │
│  • En iyi teknoloji ile kıyaslama                    │
│  • Ürün başına spesifik exergy tüketimi              │
│  • Gerçekçi yıllık tasarruf potansiyeli              │
│                                                      │
│  [+ Proses Tanımı Ekle]                              │
└──────────────────────────────────────────────────────┘
```

### 4.2 Plotly Chart Spesifikasyonları

#### 3 Katman Bar Chart
```javascript
// Horizontal bar, logaritmik ölçek
const trace = {
  type: 'bar',
  orientation: 'h',
  x: [minimum, bat, actual],
  y: ['Termodinamik\nMinimum', 'BAT\nReferans', 'Mevcut\nTesis'],
  marker: { color: ['#10B981', '#F59E0B', '#EF4444'] },
  text: [formatKW(minimum), formatKW(bat), formatKW(actual)],
  textposition: 'outside',
};
const layout = {
  xaxis: { type: 'log', title: 'Exergy (kW)' },
  height: 200,
  margin: { l: 100, r: 60, t: 20, b: 40 },
};
```

#### Waterfall Chart
```javascript
const trace = {
  type: 'waterfall',
  x: data.labels,
  y: data.values,
  measure: data.types,  // "absolute", "relative", "total"
  connector: { line: { color: '#cbd5e1' } },
  increasing: { marker: { color: '#EF4444' } },
  decreasing: { marker: { color: '#10B981' } },
  totals: { marker: { color: '#6366F1' } },
};
```

#### Gap Donut Chart
```javascript
const trace = {
  type: 'pie',
  labels: data.labels,
  values: data.values,
  hole: 0.5,
  textinfo: 'label+percent',
  marker: {
    colors: ['#EF4444', '#F59E0B', '#3B82F6', '#10B981', '#8B5CF6', '#EC4899', '#6B7280'],
  },
};
```

---

## 5. Tab 2: Genel Bakış (AI + Öncelikler + Envanter Özeti Birleşimi)

### 5.1 Yapı

```
┌─────────────────────────────────────────────────────────────────┐
│ GENEL BAKIŞ                                                     │
│                                                                 │
│ ┌─ AI Yorumu ──────────────────────────────────────────────────┐│
│ │ [Mevcut FactoryAIPanel — aynen]                              ││
│ │ + Proses konteksti varsa gap analysis bilgisi de dahil       ││
│ └──────────────────────────────────────────────────────────────┘│
│                                                                 │
│ ┌─ Kritik Noktalar ───────────────────────────────────────────┐│
│ │ [Mevcut PriorityList — hotspot sıralı]                      ││
│ │ + IntegrationPanel (entegrasyon fırsatları)                  ││
│ └──────────────────────────────────────────────────────────────┘│
│                                                                 │
│ ┌─ Ekipman Özeti ─────────────────────────────────────────────┐│
│ │ 4 ekipman: Kazan-1, Kurutma-1, Kompresör-1, Pompa-1        ││
│ │ [Envantere Git →]                                            ││
│ └──────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

Mevcut bileşenler taşınıyor, yeni bileşen yazılmıyor. Sadece layout değişikliği.

---

## 6. Tab 3: Exergy Akışı (Sankey — Aynen)

Mevcut FactorySankeyV2 aynen kalıyor. Tab adı "Sankey" → "Exergy Akışı" olarak değişir.

---

## 7. Tab 4: Derin Analiz (Pinch + İleri Exergy + EGM Birleşimi)

### 7.1 Alt Sekme Yapısı

```
┌─────────────────────────────────────────────────────────────────┐
│ DERİN ANALİZ                                                    │
│                                                                 │
│ ┌──────────┐ ┌──────────────┐ ┌─────────────────┐              │
│ │  Pinch   │ │ İleri Exergy │ │ Entropi Üretimi │              │
│ └──────────┘ └──────────────┘ └─────────────────┘              │
│                                                                 │
│ [Seçili alt sekmenin içeriği]                                   │
│ Pinch → PinchTab (mevcut, aynen)                                │
│ İleri Exergy → AdvancedExergyTab (mevcut, aynen)                │
│ Entropi Üretimi → EntropyGenerationTab (mevcut, aynen)          │
└─────────────────────────────────────────────────────────────────┘
```

Alt sekme navigasyonu basit button group (Tailwind). Mevcut 3 bileşen aynen kullanılır.

---

## 8. Tab 5: Aksiyon Planı (Termoekonomik + Entegrasyon + AI Öneriler)

### 8.1 Yapı

```
┌─────────────────────────────────────────────────────────────────┐
│ AKSİYON PLANI                                                   │
│                                                                 │
│ ┌─ f/r Karar Matrisi ─────────────────────────────────────────┐│
│ │ [Mevcut ThermoeconomicTab f/r matrisi]                      ││
│ │ Scatter plot + aksiyon kutu renklendirmesi                   ││
│ └──────────────────────────────────────────────────────────────┘│
│                                                                 │
│ ┌─ Entegrasyon Fırsatları ────────────────────────────────────┐│
│ │ [Mevcut IntegrationPanel — Öncelikler tab'ından taşınıyor]  ││
│ │ (Gap analysis varsa: gerçek tasarruf değerleri ile)          ││
│ └──────────────────────────────────────────────────────────────┘│
│                                                                 │
│ ┌─ SPECO Sonuçları ───────────────────────────────────────────┐│
│ │ [Mevcut ThermoeconomicTab SPECO tablosu]                    ││
│ └──────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

Mevcut ThermoeconomicTab içerisindeki bileşenler burada yeniden düzenleniyor. Ana bileşenler aynı, layout farklı.

---

## 9. Tab 6: Enerji Yönetimi (ISO 50001 + Tam Envanter)

### 9.1 Yapı

```
┌─────────────────────────────────────────────────────────────────┐
│ ENERJİ YÖNETİMİ                                                │
│                                                                 │
│ ┌─ ISO 50001 Olgunluk ───────────────────────────────────────┐ │
│ │ [Mevcut EnergyManagementTab — aynen]                        │ │
│ └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│ ┌─ Ekipman Envanteri ────────────────────────────────────────┐ │
│ │ [Mevcut EquipmentInventory + AddEquipmentModal — aynen]     │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 10. FactoryMetricBar Güncellemesi

Proses tanımı varsa, mevcut KPI kartlarına ek kartlar:

```javascript
// Mevcut kartlar (korunuyor):
// - Toplam Exergy Girişi
// - Toplam Exergy Yıkımı  
// - Fabrika Exergy Verimi
// - Ekipman Sayısı

// Proses varsa EK kartlar:
if (gapAnalysis) {
  // ESI Skoru kartı (grade badge ile)
  // BAT Gap kartı (€/yıl)
  // veya: mevcut 4 karttan 2'si gap bilgisiyle değişir
}
```

**Not:** MetricBar'ı çok kalabalıklaştırma. Proses varsa en çarpıcı 1-2 KPI ekle, detaylar Proses tab'ında.

---

## 11. AI Prompt Güncelleme

### 11.1 `api/services/claude_code_service.py`

Fabrika AI yorumlama prompt'una proses konteksti ekle:

```python
# Mevcut prompt'un sonuna ekle (eğer gap_analysis varsa):

if factory_analysis.gap_analysis:
    gap = factory_analysis.gap_analysis
    process_context = f"""

## Proses Tanımı ve Gap Analizi

Bu fabrika bir **{gap['process_label']}** tesisidir.
Proses tipi: {gap['process_type']}

### Exergetic Gap Analysis Sonuçları:
- Termodinamik minimum exergy: {gap['minimum_exergy_kW']:.1f} kW
- BAT (en iyi teknoloji) referansı: {gap['bat_exergy_kW']:.1f} kW  
- Mevcut tesis tüketimi: {gap['actual_exergy_kW']:.1f} kW
- İdealin {gap['actual_to_minimum_ratio']:.0f} katı tüketim
- BAT'ın {gap['actual_to_bat_ratio']:.1f} katı tüketim
- ESI Skoru: {gap['exergetic_sustainability_index']:.4f} (Not: {gap['grade']})
- Gerçekçi tasarruf potansiyeli: {gap['bat_gap_kW']:.1f} kW (€{gap['annual_bat_gap_cost_eur']:,.0f}/yıl)
- BAT teknolojisi: {gap['bat_technology']}

Bu bilgileri AI yorumuna entegre et. Özellikle:
1. Büyük resmi açıkla (idealden ne kadar uzak)
2. Gerçekçi iyileştirme potansiyelini vurgula
3. BAT teknolojisine geçiş önerisi ver
"""
    prompt += process_context
```

### 11.2 Knowledge Dosyası Referansı

AI yorumlama sırasında `knowledge/factory/process/` dosyaları da context'e eklenebilir (proses tipine göre ilgili dosya).

---

## 12. Tab Durum İndikatörleri

Mevcut yeşil nokta sistemi korunuyor ama yeni tab yapısına uyarlanıyor:

```javascript
const TABS = [
  { 
    key: "process", 
    label: "Proses Analizi", 
    icon: Target,
    hasData: (data) => !!data.gapAnalysis,
    // Proses tanımı yoksa sarı nokta (uyarı), varsa yeşil
    statusColor: (data) => data.project.process_type 
      ? (data.gapAnalysis ? "green" : "yellow") 
      : "gray"
  },
  { 
    key: "overview", 
    label: "Genel Bakış", 
    icon: BarChart3,
    hasData: (data) => !!data.aiInterpretation || !!data.hotspots?.length,
  },
  { 
    key: "flow", 
    label: "Exergy Akışı", 
    icon: GitBranch,  // veya Workflow
    hasData: (data) => !!data.sankeyData,
  },
  { 
    key: "deep", 
    label: "Derin Analiz", 
    icon: Microscope,
    hasData: (data) => !!(data.pinchData || data.advancedExergy || data.egmData),
  },
  { 
    key: "action", 
    label: "Aksiyon Planı", 
    icon: Lightbulb,
    hasData: (data) => !!data.thermoeconomicData,
  },
  { 
    key: "management", 
    label: "Enerji Yönetimi", 
    icon: ClipboardList,
    hasData: (data) => !!data.energyManagement,
  },
];
```

---

## 13. Dosya Değişiklikleri

| Dosya | İşlem | Tahmin |
|-------|-------|--------|
| `frontend/src/components/factory/GapAnalysisTab.jsx` | **YENİ** | ~350 satır |
| `frontend/src/components/factory/DeepAnalysisTab.jsx` | **YENİ** (wrapper) | ~60 satır |
| `frontend/src/components/factory/ActionPlanTab.jsx` | **YENİ** (wrapper) | ~80 satır |
| `frontend/src/components/factory/OverviewTab.jsx` | **YENİ** (wrapper) | ~80 satır |
| `frontend/src/components/factory/ManagementTab.jsx` | **YENİ** (wrapper) | ~60 satır |
| `frontend/src/pages/FactoryDashboard.jsx` | **GÜNCELLE** | ~200 satır değişiklik (9→6 tab) |
| `frontend/src/components/factory/FactoryMetricBar.jsx` | **GÜNCELLE** | +30 satır |
| `api/services/claude_code_service.py` | **GÜNCELLE** | +30 satır (prompt context) |
| `knowledge/factory/process/*.md` | Brief 0'da oluşturulmuş olmalı | — |
| `skills/factory/process_analyst.md` | Brief 0'da oluşturulmuş olmalı | — |

**Toplam: ~890 satır yeni + ~230 satır değişiklik ≈ 1,120 satır**

---

## 14. Migration Stratejisi

Eski tab bileşenleri silinMEYECEK — wrapper'lar içinde kullanılmaya devam edecek:

```
ESKİ                          → YENİ
FactoryAIPanel               → OverviewTab içinde
PriorityList                 → OverviewTab içinde
IntegrationPanel             → ActionPlanTab içinde
FactorySankeyV2              → Aynen (tab adı değişir)
PinchTab                     → DeepAnalysisTab alt sekmesi
AdvancedExergyTab            → DeepAnalysisTab alt sekmesi
EntropyGenerationTab         → DeepAnalysisTab alt sekmesi
ThermoeconomicTab            → ActionPlanTab içinde
EnergyManagementTab          → ManagementTab içinde
EquipmentInventory           → ManagementTab içinde
```

Hiçbir mevcut bileşen silinmiyor. Sadece layout ve gruplama değişiyor.

---

## 15. UYARILAR

1. **Mevcut bileşenleri silme** — Sadece wrapper'la ve yeniden grupla
2. **engine/ klasörüne DOKUNMA** (prompt güncellemesi hariç — o api/ içinde)
3. **Tab geçiş animasyonu** — Mevcut transition mekanizması korunsun
4. **URL hash** — Mevcut tab hash sistemi varsa uyarla (?tab=process, ?tab=overview, vb.)
5. **Responsive** — Mobilde tab'lar scroll olabilmeli
6. **Proses tanımı yoksa** — Proses tab'ı "Ekle" CTA gösterir, diğer tab'lar eskisi gibi çalışır
7. **Testler** — Frontend testleri varsa güncellenmalı

---

*Bu brief ExergyLab dashboard'unu "ekipman listesi"nden "analiz hikayesi"ne dönüştürür. 
Tüm 4 brief'in son adımıdır.*
