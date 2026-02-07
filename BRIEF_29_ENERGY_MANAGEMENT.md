# BRIEF_29: Energy Management (ISO 50001) Motor Modülü

> **Tarih:** 2026-02-06
> **Öncelik:** Orta
> **Tahmini Süre:** 3-5 saat
> **Karmaşıklık:** Orta
> **Bağımlılıklar:** Tüm önceki motorlar (exergy, SPECO, AV/UN, pinch, EN/EX, EGM, thermoeconomic)
> **Etkilenen Dosyalar:** Yeni + mevcut toplam ~12 dosya

---

## 1. Bağlam ve Motivasyon

### 1.1 Neden ISO 50001?

Bu ExergyLab'ın **son analiz motoru** ve diğerlerinden farklı bir amacı var. Önceki 5 motor termodinamik hesaplama yapıyordu — bu motor, tüm sonuçları **enerji yönetimi çerçevesinde** sentezler.

ISO 50001, bir kuruluşun enerji performansını sistematik olarak yönetmesi için uluslararası standarttır. ExergyLab bağlamında ISO 50001 modülü:

1. **Energy Performance Indicators (EnPI):** Fabrika geneli performans göstergeleri hesaplar
2. **Olgunluk değerlendirmesi:** Enerji yönetim pratiğinin ne kadar olgun olduğunu skorlar
3. **Enerji denetim raporu:** Tüm analiz sonuçlarını ISO 50001 formatında yapılandırır
4. **İyileştirme eylem planı:** Tüm motorlardan gelen önerileri önceliklendirir ve zaman çizelgesi oluşturur
5. **Uyum boşluk analizi:** ISO 50001 gereksinimlerine karşı mevcut durumu değerlendirir

### 1.2 ExergyLab Motor Özeti ve ISO 50001 Bağlantısı

| Motor | ISO 50001 Maddesi | Katkı |
|-------|-------------------|-------|
| Exergy analizi | 6.3 Enerji gözden geçirmesi | Temel performans verileri |
| SPECO (exergoekonomik) | 6.5 Performans göstergeleri | Maliyet bazlı EnPI'ler |
| AV/UN dekompozisyon | 6.4 İyileştirme fırsatları | İyileştirme potansiyeli |
| Pinch analizi | 6.4 İyileştirme fırsatları | Isı entegrasyonu fırsatları |
| EN/EX dekompozisyon | 6.3 Enerji gözden geçirmesi | Sistem etkileşim analizi |
| EGM | 6.3 Enerji gözden geçirmesi | Tersinmezlik kaynakları |
| Termoekonomik opt. | 6.5 + 6.6 Aksiyon planı | Optimizasyon stratejileri |

### 1.3 Knowledge Base

`knowledge/factory/energy_management/` dizininde ~10 dosya mevcut. Uygulama koşulu: **sistematik yönetim ihtiyacı**.

---

## 2. Teori — ISO 50001 Çerçevesi

### 2.1 Energy Performance Indicators (EnPI)

ExergyLab'ın hesaplayabileceği EnPI'ler (mevcut verilerden türetilen):

```
1. Fabrika Exergy Verimi (η_ex_factory)
   = Σ E_x,out / Σ E_x,in × 100                          (%)
   → Temel performans göstergesi

2. Spesifik Exergy Tüketimi (SEC)
   = Σ E_x,in / Σ E_x,out                                 (kW/kW)
   → Birim ürün başına exergy tüketimi (1'e ne kadar yakınsa o kadar iyi)

3. Exergy Yıkım Oranı (EDR)
   = Σ I_dot / Σ E_x,in × 100                             (%)
   → Ne kadarlık exergy yıkılıyor

4. Kaçınılabilir Kayıp Oranı (ALR — Avoidable Loss Ratio)
   = Σ I_avoidable / Σ I_total × 100                      (%)
   → İyileştirilebilir kayıpların payı

5. Enerji Maliyet Yoğunluğu (ECI — Energy Cost Intensity)
   = Σ C_dot_D / Σ E_x,in                                 (EUR/kWh)
   → Birim exergy girişi başına yıkım maliyeti

6. Isı Geri Kazanım Potansiyeli (HRP)
   = Σ recoverable_heat_kW / Σ I_dot × 100                (%)
   → Yıkılan exerginin ne kadarı ısı olarak geri kazanılabilir

7. Entropi Üretim Yoğunluğu (EGI — Entropy Generation Intensity)
   = S_gen_total × T₀ / Σ E_x,in                          (boyutsuz = N_s_factory)
   → Fabrika seviyesi Bejan sayısı (EGM'den)
```

### 2.2 Olgunluk Değerlendirmesi

ISO 50001 uyumu için 7 boyutta olgunluk skorlaması. Her boyut 0-100 puan, ExergyLab'ın mevcut verilerinden otomatik hesaplanır:

```python
MATURITY_DIMENSIONS = {
    "energy_review": {
        "label": "Enerji Gözden Geçirmesi",
        "iso_clause": "6.3",
        "description": "Enerji kullanımının ve tüketiminin analizi",
        # Skor: ekipman sayısı, analiz tamamlanma oranı
    },
    "performance_indicators": {
        "label": "Performans Göstergeleri",
        "iso_clause": "6.5",
        "description": "EnPI tanımlama ve izleme",
        # Skor: exergoekonomik veri mevcudiyeti, f/r analizi
    },
    "improvement_opportunities": {
        "label": "İyileştirme Fırsatları",
        "iso_clause": "6.4",
        "description": "İyileştirme fırsatlarının belirlenmesi ve önceliklendirilmesi",
        # Skor: AV/UN, pinch, EN/EX analiz mevcudiyeti
    },
    "action_planning": {
        "label": "Aksiyon Planlama",
        "iso_clause": "6.6",
        "description": "Eylem planlarının oluşturulması",
        # Skor: termoekonomik optimizasyon mevcudiyeti
    },
    "monitoring": {
        "label": "İzleme ve Ölçme",
        "iso_clause": "9.1",
        "description": "Performans izleme ve ölçme altyapısı",
        # Skor: ekipman veri kalitesi, EGM analizi
    },
    "heat_integration": {
        "label": "Isı Entegrasyonu",
        "iso_clause": "6.4",
        "description": "Isı geri kazanım ve entegrasyon fırsatları",
        # Skor: pinch analizi mevcudiyeti ve sonuçları
    },
    "cost_optimization": {
        "label": "Maliyet Optimizasyonu",
        "iso_clause": "6.5",
        "description": "Enerji maliyetlerinin optimizasyonu",
        # Skor: SPECO ve termoekonomik analiz mevcudiyeti
    },
}
```

#### Olgunluk Skorlama Mantığı

```python
def _score_energy_review(factory_data: dict) -> int:
    """6.3 - Enerji gözden geçirmesi skoru (0-100)."""
    score = 0
    n_eq = factory_data.get("num_equipment", 0)
    
    # Ekipman sayısı (max 20 puan)
    score += min(20, n_eq * 5)
    
    # Çeşitlilik — kaç farklı ekipman tipi (max 20 puan)
    types = set(r.get("equipment_type") for r in factory_data.get("equipment_results", []))
    score += min(20, len(types) * 5)
    
    # Ortalama exergy verimi > 50% (max 20 puan)
    avg_eta = factory_data.get("avg_exergy_efficiency_pct", 0)
    score += min(20, max(0, int(avg_eta * 0.4)))
    
    # AV/UN analizi mevcut (20 puan)
    has_avun = any(r.get("avoidable_ratio_pct") is not None 
                   for r in factory_data.get("equipment_results", []))
    score += 20 if has_avun else 0
    
    # EGM analizi mevcut (20 puan)
    score += 20 if factory_data.get("entropy_generation") else 0
    
    return min(100, score)
```

Her boyut için benzer skorlama fonksiyonu. Toplam olgunluk skoru:

```
maturity_score = Σ dimension_scores / num_dimensions
maturity_level = {
    90-100: "Lider (Leading)",        → ISO 50001 sertifikasyona hazır
    70-89:  "Olgun (Mature)",         → İleri düzey enerji yönetimi
    50-69:  "Gelişen (Developing)",   → Temel enerji yönetimi mevcut
    30-49:  "Başlangıç (Beginning)",  → Bazı uygulamalar var
    0-29:   "Farkındalık (Aware)",    → Minimum enerji yönetimi
}
```

### 2.3 Boşluk Analizi (Gap Analysis)

Her olgunluk boyutunda skor < 70 ise "boşluk" (gap) olarak işaretlenir:

```python
@dataclass
class MaturityGap:
    dimension: str             # Boyut adı
    label: str                # Türkçe etiket
    iso_clause: str           # ISO maddesi
    current_score: int        # Mevcut skor (0-100)
    target_score: int         # Hedef skor (70 = "olgun")
    gap: int                  # target - current
    recommendations: List[str] # Kapama önerileri
```

### 2.4 İyileştirme Eylem Planı

Tüm motorlardan gelen önerileri birleştirip yapılandırılmış eylem planı oluşturur:

```python
@dataclass
class ActionItem:
    id: str                    # "A-01", "A-02", ...
    source: str                # "thermoeconomic" | "pinch" | "advanced_exergy" | "egm" | "base"
    equipment_id: Optional[str]
    equipment_name: Optional[str]
    action: str                # Aksiyon açıklaması
    category: str              # "quick_win" | "medium_term" | "strategic" | "monitoring"
    estimated_savings_eur: float
    estimated_investment_eur: float
    payback_years: float
    priority: str              # "high" | "medium" | "low"
    timeline: str              # "0-3 ay" | "3-12 ay" | "1-3 yıl" | "sürekli"
```

Kategori belirleme:

```
quick_win:    payback < 1 yıl, investment < 10K EUR  → "0-3 ay"
medium_term:  payback 1-3 yıl, investment 10K-100K   → "3-12 ay"
strategic:    payback > 3 yıl veya investment > 100K  → "1-3 yıl"
monitoring:   savings = 0 (maintain stratejisi)       → "sürekli"
```

---

## 3. Engine Modülü: `engine/energy_management.py`

### 3.1 Dosya Yapısı

Tahmini boyut: **~550-650 satır**

### 3.2 Veri Yapıları

```python
@dataclass
class EnPIMetrics:
    """Energy Performance Indicators."""
    exergy_efficiency_pct: float          # η_ex_factory
    specific_exergy_consumption: float    # SEC (kW/kW)
    exergy_destruction_ratio_pct: float   # EDR (%)
    avoidable_loss_ratio_pct: float       # ALR (%)
    energy_cost_intensity_eur_kWh: float  # ECI (EUR/kWh)
    heat_recovery_potential_pct: float    # HRP (%)
    entropy_generation_intensity: float   # EGI (= N_s_factory)
    
    def to_dict(self) -> dict:
        return {
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "specific_exergy_consumption": round(self.specific_exergy_consumption, 3),
            "exergy_destruction_ratio_pct": round(self.exergy_destruction_ratio_pct, 1),
            "avoidable_loss_ratio_pct": round(self.avoidable_loss_ratio_pct, 1),
            "energy_cost_intensity_eur_kWh": round(self.energy_cost_intensity_eur_kWh, 4),
            "heat_recovery_potential_pct": round(self.heat_recovery_potential_pct, 1),
            "entropy_generation_intensity": round(self.entropy_generation_intensity, 4),
        }


@dataclass
class MaturityDimension:
    """Tek boyut olgunluk skoru."""
    dimension: str
    label: str
    iso_clause: str
    score: int                 # 0-100
    max_score: int             # 100
    findings: List[str]        # Ne bulundu
    gaps: List[str]            # Ne eksik
    
    def to_dict(self) -> dict:
        return {
            "dimension": self.dimension,
            "label": self.label,
            "iso_clause": self.iso_clause,
            "score": self.score,
            "max_score": self.max_score,
            "findings": self.findings,
            "gaps": self.gaps,
        }


@dataclass
class ActionItem:
    """Eylem planı kalemi."""
    id: str
    source: str
    equipment_id: Optional[str]
    equipment_name: Optional[str]
    action: str
    category: str              # quick_win | medium_term | strategic | monitoring
    estimated_savings_eur: float
    estimated_investment_eur: float
    payback_years: float
    priority: str
    timeline: str
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "source": self.source,
            "equipment_id": self.equipment_id,
            "equipment_name": self.equipment_name,
            "action": self.action,
            "category": self.category,
            "estimated_savings_eur": round(self.estimated_savings_eur, 2),
            "estimated_investment_eur": round(self.estimated_investment_eur, 2),
            "payback_years": round(self.payback_years, 1),
            "priority": self.priority,
            "timeline": self.timeline,
        }


@dataclass
class EnergyManagementResult:
    """Fabrika seviyesi ISO 50001 enerji yönetimi sonucu."""
    num_equipment: int
    
    # EnPI'ler
    enpi: EnPIMetrics
    
    # Olgunluk değerlendirmesi
    maturity_score: int                  # Toplam ortalama (0-100)
    maturity_level: str                  # "leading" | "mature" | "developing" | "beginning" | "aware"
    maturity_level_label: str            # Türkçe etiket
    maturity_dimensions: List[MaturityDimension]
    
    # Boşluk analizi
    num_gaps: int
    critical_gaps: List[str]             # Skor < 50 olan boyutlar
    
    # Eylem planı
    action_plan: List[ActionItem]
    action_summary: Dict                 # Kategori bazlı özet
    total_potential_savings_eur: float
    total_estimated_investment_eur: float
    
    # Görselleştirme
    enpi_radar_data: Dict                # Radar chart: 7 EnPI
    maturity_radar_data: Dict            # Radar chart: 7 boyut
    action_timeline_data: Dict           # Gantt/timeline chart verisi
    
    # Uyarılar
    warnings: List[str]
    
    is_valid: bool = True
    error_message: str = ""
    
    def to_dict(self) -> dict:
        # ... standart serializasyon
```

### 3.3 Sabit Veriler

```python
# --- Olgunluk Seviyeleri ---
MATURITY_LEVELS = {
    "leading":    {"min": 90, "label": "Lider (Leading)", "description": "ISO 50001 sertifikasyona hazır"},
    "mature":     {"min": 70, "label": "Olgun (Mature)", "description": "İleri düzey enerji yönetimi"},
    "developing": {"min": 50, "label": "Gelişen (Developing)", "description": "Temel enerji yönetimi mevcut"},
    "beginning":  {"min": 30, "label": "Başlangıç (Beginning)", "description": "Bazı uygulamalar var"},
    "aware":      {"min": 0,  "label": "Farkındalık (Aware)", "description": "Minimum enerji yönetimi"},
}

# --- Olgunluk Boyutları ---
MATURITY_DIMENSIONS = {
    # Bölüm 2.2'deki tam sözlük
}

# --- Aksiyon Kategorileri ---
ACTION_CATEGORIES = {
    "quick_win":    {"label": "Hızlı Kazanım", "timeline": "0-3 ay", "color": "#22c55e"},
    "medium_term":  {"label": "Orta Vadeli", "timeline": "3-12 ay", "color": "#f59e0b"},
    "strategic":    {"label": "Stratejik", "timeline": "1-3 yıl", "color": "#8b5cf6"},
    "monitoring":   {"label": "İzleme", "timeline": "Sürekli", "color": "#3b82f6"},
}

# --- Boşluk Kapama Önerileri ---
GAP_RECOMMENDATIONS = {
    "energy_review": [
        "Tüm enerji tüketen ekipmanları envantere ekleyin",
        "Eksik ekipman tiplerini (pompa, HX, vb.) analiz kapsamına alın",
        "Düzenli enerji gözden geçirmesi prosedürü oluşturun",
    ],
    "performance_indicators": [
        "Exergoekonomik analizi tüm ekipmanlara uygulayın",
        "EnPI hedeflerini belirleyin ve izleme sistemini kurun",
        "Aylık EnPI raporlama prosedürü oluşturun",
    ],
    "improvement_opportunities": [
        "Kaçınılabilir/kaçınılamaz analizi yapın",
        "Endojen/eksojen dekompozisyonu uygulayın",
        "Entropi üretimi analizi ile tersinmezlik kaynaklarını belirleyin",
    ],
    "action_planning": [
        "Termoekonomik optimizasyon analizi çalıştırın",
        "Her ekipman için maliyet-fayda değerlendirmesi yapın",
        "Yıllık enerji iyileştirme hedefleri belirleyin",
    ],
    "monitoring": [
        "Gerçek zamanlı enerji izleme sistemi kurun",
        "Kritik ekipmanlara alt ölçüm cihazları ekleyin",
        "Entropi üretimi bazlı performans takibi uygulayın",
    ],
    "heat_integration": [
        "Pinch analizi ile ısı entegrasyonu fırsatlarını belirleyin",
        "Atık ısı geri kazanım projelerini değerlendirin",
        "Isı eşanjör ağı optimizasyonu yapın",
    ],
    "cost_optimization": [
        "SPECO analizi ile maliyet dağılımını belirleyin",
        "f-faktör/r-faktör bazlı optimizasyon stratejileri uygulayın",
        "Yatırım geri dönüş analizlerini tamamlayın",
    ],
}
```

### 3.4 Ana Fonksiyonlar

#### 3.4.1 `analyze_energy_management()` — Ana Giriş Noktası

```python
def analyze_energy_management(
    factory_data: dict,
) -> EnergyManagementResult:
    """
    ISO 50001 enerji yönetimi değerlendirmesi.
    
    Args:
        factory_data: analyze_factory() çıktısı (to_dict() sonucu).
            Tüm analiz sonuçlarını içerir: base exergy, pinch, advanced_exergy,
            entropy_generation, thermoeconomic_optimization.
    """
    equipment_results = factory_data.get("equipment_results", [])
    if not equipment_results:
        return EnergyManagementResult(is_valid=False, error_message="Ekipman yok", ...)
    
    # 1. EnPI hesapla
    enpi = _calculate_enpi(factory_data)
    
    # 2. Olgunluk değerlendirmesi
    dimensions = _assess_maturity(factory_data)
    maturity_score = sum(d.score for d in dimensions) // len(dimensions) if dimensions else 0
    maturity_level, maturity_label = _determine_maturity_level(maturity_score)
    
    # 3. Boşluk analizi
    gaps = [d for d in dimensions if d.score < 70]
    critical_gaps = [d.label for d in dimensions if d.score < 50]
    
    # 4. Eylem planı
    action_plan = _build_action_plan(factory_data)
    action_summary = _summarize_actions(action_plan)
    
    # 5. Görselleştirme verileri
    enpi_radar = _generate_enpi_radar(enpi)
    maturity_radar = _generate_maturity_radar(dimensions)
    timeline_data = _generate_action_timeline(action_plan)
    
    # 6. Uyarılar
    warnings = _collect_warnings(enpi, maturity_score, action_plan)
    
    return EnergyManagementResult(...)
```

#### 3.4.2 `_calculate_enpi()` — EnPI Hesapla

```python
def _calculate_enpi(factory_data: dict) -> EnPIMetrics:
    """Mevcut fabrika verisinden EnPI'ler hesapla."""
    agg = factory_data.get("aggregates", {})
    eq_results = factory_data.get("equipment_results", [])
    egm = factory_data.get("entropy_generation", {})
    
    E_x_in = agg.get("total_exergy_in_kW", 0)
    E_x_out = agg.get("total_exergy_out_kW", 0)
    I_total = agg.get("total_exergy_destroyed_kW", 0)
    
    # η_ex_factory
    eta_ex = (E_x_out / E_x_in * 100) if E_x_in > 0 else 0
    
    # SEC
    sec = E_x_in / E_x_out if E_x_out > 0 else 0
    
    # EDR
    edr = (I_total / E_x_in * 100) if E_x_in > 0 else 0
    
    # ALR
    I_avoidable = sum(r.get("exergy_destroyed_avoidable_kW", 0) for r in eq_results)
    alr = (I_avoidable / I_total * 100) if I_total > 0 else 0
    
    # ECI
    C_dot_D_total = sum(r.get("exergoeconomic_C_dot_destruction_eur_h", 0) or 0 for r in eq_results)
    eci = C_dot_D_total / E_x_in if E_x_in > 0 else 0
    
    # HRP
    recoverable = sum(r.get("recoverable_heat_kW", 0) or 0 for r in eq_results)
    hrp = (recoverable / I_total * 100) if I_total > 0 else 0
    
    # EGI (= N_s_factory)
    egi = egm.get("N_s_factory", 0) if egm else 0
    
    return EnPIMetrics(
        exergy_efficiency_pct=eta_ex,
        specific_exergy_consumption=sec,
        exergy_destruction_ratio_pct=edr,
        avoidable_loss_ratio_pct=alr,
        energy_cost_intensity_eur_kWh=eci,
        heat_recovery_potential_pct=hrp,
        entropy_generation_intensity=egi,
    )
```

#### 3.4.3 `_assess_maturity()` — Olgunluk Değerlendirmesi

```python
def _assess_maturity(factory_data: dict) -> List[MaturityDimension]:
    """7 boyutta olgunluk skorlaması."""
    dimensions = []
    
    for dim_key, dim_info in MATURITY_DIMENSIONS.items():
        scorer = MATURITY_SCORERS.get(dim_key)
        if scorer:
            score, findings, gaps = scorer(factory_data)
        else:
            score, findings, gaps = 0, [], ["Değerlendirme mevcut değil"]
        
        dimensions.append(MaturityDimension(
            dimension=dim_key,
            label=dim_info["label"],
            iso_clause=dim_info["iso_clause"],
            score=min(100, max(0, score)),
            max_score=100,
            findings=findings,
            gaps=gaps,
        ))
    
    return dimensions
```

Her boyut için ayrı scorer fonksiyonu:

```python
MATURITY_SCORERS = {
    "energy_review": _score_energy_review,
    "performance_indicators": _score_performance_indicators,
    "improvement_opportunities": _score_improvement_opportunities,
    "action_planning": _score_action_planning,
    "monitoring": _score_monitoring,
    "heat_integration": _score_heat_integration,
    "cost_optimization": _score_cost_optimization,
}

def _score_energy_review(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """Enerji gözden geçirmesi skoru."""
    score = 0
    findings = []
    gaps = []
    
    eq_results = factory_data.get("equipment_results", [])
    n_eq = len(eq_results)
    types = set(r.get("equipment_type") for r in eq_results)
    
    # Ekipman sayısı (max 25 puan)
    eq_score = min(25, n_eq * 5)
    score += eq_score
    if n_eq > 0:
        findings.append(f"{n_eq} ekipman analiz edildi")
    if n_eq < 3:
        gaps.append("Daha fazla ekipman analiz kapsamına alınmalı")
    
    # Ekipman çeşitliliği (max 25 puan)
    type_score = min(25, len(types) * 7)
    score += type_score
    if len(types) > 1:
        findings.append(f"{len(types)} farklı ekipman tipi mevcut")
    if len(types) < 3:
        gaps.append("Ekipman tip çeşitliliği artırılmalı")
    
    # AV/UN analizi (25 puan)
    has_avun = any(r.get("avoidable_ratio_pct") is not None for r in eq_results)
    if has_avun:
        score += 25
        findings.append("Kaçınılabilir/kaçınılamaz analizi mevcut")
    else:
        gaps.append("AV/UN analizi yapılmalı")
    
    # EN/EX veya EGM (25 puan)
    has_advanced = (factory_data.get("advanced_exergy") is not None or 
                    factory_data.get("entropy_generation") is not None)
    if has_advanced:
        score += 25
        findings.append("İleri düzey exergy analizi mevcut")
    else:
        gaps.append("İleri düzey analiz (EN/EX veya EGM) yapılmalı")
    
    return score, findings, gaps


def _score_performance_indicators(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """Performans göstergeleri skoru."""
    score = 0
    findings = []
    gaps = []
    eq_results = factory_data.get("equipment_results", [])
    
    # Exergy verimi hesaplanmış (25 puan)
    has_eta = any(r.get("exergy_efficiency_pct") is not None for r in eq_results)
    if has_eta:
        score += 25
        findings.append("Exergy verimlilikleri hesaplanmış")
    else:
        gaps.append("Exergy verimi hesaplanmalı")
    
    # Exergoekonomik analiz (25 puan)
    has_speco = any(r.get("exergoeconomic_f_factor") is not None for r in eq_results)
    if has_speco:
        score += 25
        findings.append("SPECO analizi mevcut")
    else:
        gaps.append("Exergoekonomik analiz yapılmalı")
    
    # Benchmark karşılaştırma (25 puan)
    has_benchmark = any(r.get("benchmark_rating") is not None for r in eq_results)
    if has_benchmark:
        score += 25
        findings.append("Sektör benchmark karşılaştırması mevcut")
    else:
        gaps.append("Benchmark karşılaştırması yapılmalı")
    
    # Çok ekipmanlı izleme (25 puan)
    if len(eq_results) >= 3:
        score += 25
        findings.append(f"{len(eq_results)} ekipman izleniyor")
    else:
        gaps.append("En az 3 ekipman izlenmeli")
    
    return score, findings, gaps


def _score_improvement_opportunities(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """İyileştirme fırsatları skoru."""
    score = 0
    findings = []
    gaps = []
    
    # AV/UN mevcut (25)
    eq_results = factory_data.get("equipment_results", [])
    has_avun = any(r.get("avoidable_ratio_pct") is not None for r in eq_results)
    if has_avun:
        score += 25
        findings.append("Kaçınılabilir kayıp analizi mevcut")
    else:
        gaps.append("AV/UN analizi yapılmalı")
    
    # EN/EX mevcut (25)
    if factory_data.get("advanced_exergy"):
        score += 25
        findings.append("EN/EX dekompozisyon mevcut")
    else:
        gaps.append("Endojen/eksojen analizi yapılmalı")
    
    # EGM mevcut (25)
    if factory_data.get("entropy_generation"):
        score += 25
        findings.append("Entropi üretimi analizi mevcut")
    else:
        gaps.append("EGM analizi yapılmalı")
    
    # Pinch analizi (25)
    if factory_data.get("pinch_analysis"):
        score += 25
        findings.append("Pinch analizi mevcut")
    else:
        gaps.append("Pinch analizi yapılmalı")
    
    return score, findings, gaps


def _score_action_planning(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """Aksiyon planlama skoru."""
    score = 0
    findings = []
    gaps = []
    
    thermo = factory_data.get("thermoeconomic_optimization")
    if thermo and thermo.get("is_valid"):
        score += 50
        findings.append("Termoekonomik optimizasyon mevcut")
        
        # ROI analizi var mı (25)
        ranking = thermo.get("cost_benefit_ranking", [])
        if ranking:
            score += 25
            findings.append(f"{len(ranking)} ekipman için ROI analizi yapılmış")
        else:
            gaps.append("Maliyet-fayda sıralaması oluşturulmalı")
        
        # Çoklu strateji (25)
        dist = thermo.get("strategy_distribution", {})
        if len(dist) > 1:
            score += 25
            findings.append("Çoklu optimizasyon stratejisi belirlenmiş")
        else:
            gaps.append("Farklı ekipmanlar için farklı stratejiler değerlendirilmeli")
    else:
        gaps.append("Termoekonomik optimizasyon analizi yapılmalı")
    
    return score, findings, gaps


def _score_monitoring(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """İzleme skoru."""
    score = 0
    findings = []
    gaps = []
    
    eq_results = factory_data.get("equipment_results", [])
    n_eq = len(eq_results)
    
    # Ekipman verisi var (25)
    if n_eq > 0:
        score += 25
        findings.append(f"{n_eq} ekipman için veri mevcut")
    else:
        gaps.append("Ekipman verileri girilmeli")
    
    # EGM analizi (25) — entropi takibi
    if factory_data.get("entropy_generation"):
        score += 25
        findings.append("Entropi bazlı izleme mevcut")
    else:
        gaps.append("Entropi üretimi izlemesi kurulmalı")
    
    # Veri kalitesi — exergy_in > 0 olanlar oranı (25)
    valid = sum(1 for r in eq_results if (r.get("exergy_in_kW") or 0) > 0)
    quality_ratio = valid / n_eq if n_eq > 0 else 0
    quality_score = int(quality_ratio * 25)
    score += quality_score
    if quality_ratio > 0.8:
        findings.append("Veri kalitesi iyi")
    else:
        gaps.append("Bazı ekipmanların exergy verileri eksik")
    
    # Çoklu analiz katmanı (25) — 3+ motor çalışıyorsa
    motors_available = sum(1 for k in ["pinch_analysis", "advanced_exergy", "entropy_generation", "thermoeconomic_optimization"]
                          if factory_data.get(k) is not None)
    motor_score = min(25, motors_available * 8)
    score += motor_score
    if motors_available >= 3:
        findings.append(f"{motors_available} analiz motoru aktif")
    else:
        gaps.append("Daha fazla analiz motoru etkinleştirilmeli")
    
    return score, findings, gaps


def _score_heat_integration(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """Isı entegrasyonu skoru."""
    score = 0
    findings = []
    gaps = []
    
    pinch = factory_data.get("pinch_analysis")
    if pinch and pinch.get("is_valid"):
        score += 50
        findings.append("Pinch analizi tamamlanmış")
        
        # Isı geri kazanım potansiyeli var (25)
        recovery = pinch.get("max_heat_recovery_kW", 0)
        if recovery > 0:
            score += 25
            findings.append(f"Isı geri kazanım potansiyeli: {recovery:.0f} kW")
        
        # Minimum yardımcı ısıtma/soğutma hesaplanmış (25)
        if pinch.get("hot_utility_kW") is not None:
            score += 25
            findings.append("Minimum yardımcı ısıtma/soğutma belirlenmiş")
    else:
        gaps.append("Pinch analizi yapılmalı")
        
        # Isı eşanjörü var mı (kısmi puan)
        eq_results = factory_data.get("equipment_results", [])
        hx_count = sum(1 for r in eq_results if r.get("equipment_type") == "heat_exchanger")
        if hx_count > 0:
            score += 15
            findings.append(f"{hx_count} ısı eşanjörü mevcut")
        else:
            gaps.append("Isı eşanjörü eklenmeli")
    
    return score, findings, gaps


def _score_cost_optimization(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """Maliyet optimizasyonu skoru."""
    score = 0
    findings = []
    gaps = []
    
    eq_results = factory_data.get("equipment_results", [])
    
    # SPECO mevcut (35)
    has_speco = any(r.get("exergoeconomic_f_factor") is not None for r in eq_results)
    if has_speco:
        score += 35
        findings.append("Exergoekonomik maliyet analizi mevcut")
    else:
        gaps.append("SPECO analizi yapılmalı")
    
    # Termoekonomik optimizasyon (35)
    thermo = factory_data.get("thermoeconomic_optimization")
    if thermo and thermo.get("is_valid"):
        score += 35
        findings.append("Optimizasyon stratejileri belirlenmiş")
        
        savings = thermo.get("total_savings_annual_eur", 0)
        if savings > 0:
            findings.append(f"Toplam tasarruf potansiyeli: {savings:,.0f} EUR/yıl")
    else:
        gaps.append("Termoekonomik optimizasyon yapılmalı")
    
    # Maliyet bazlı sıralama (30)
    if thermo and thermo.get("cost_benefit_ranking"):
        score += 30
        findings.append("Maliyet-fayda sıralaması mevcut")
    else:
        gaps.append("ROI bazlı önceliklendirme yapılmalı")
    
    return score, findings, gaps
```

#### 3.4.4 `_build_action_plan()`

```python
def _build_action_plan(factory_data: dict) -> List[ActionItem]:
    """Tüm motorlardan gelen önerileri birleştirip eylem planı oluştur."""
    actions = []
    counter = 1
    
    # 1. Termoekonomik optimizasyondan aksiyonlar
    thermo = factory_data.get("thermoeconomic_optimization")
    if thermo and thermo.get("is_valid"):
        for rec in thermo.get("recommendations", []):
            if rec.get("strategy") == "maintain":
                category = "monitoring"
                timeline = "Sürekli"
            elif rec.get("simple_payback_years", 99) < 1:
                category = "quick_win"
                timeline = "0-3 ay"
            elif rec.get("simple_payback_years", 99) < 3:
                category = "medium_term"
                timeline = "3-12 ay"
            else:
                category = "strategic"
                timeline = "1-3 yıl"
            
            # İlk aksiyonu al
            action_text = rec.get("recommended_actions", ["Değerlendirme yapın"])[0]
            
            actions.append(ActionItem(
                id=f"A-{counter:02d}",
                source="thermoeconomic",
                equipment_id=rec.get("equipment_id"),
                equipment_name=rec.get("equipment_name"),
                action=action_text,
                category=category,
                estimated_savings_eur=rec.get("C_savings_annual_eur", 0),
                estimated_investment_eur=rec.get("estimated_investment_eur", 0),
                payback_years=rec.get("simple_payback_years", 99.9),
                priority=rec.get("priority", "medium"),
                timeline=timeline,
            ))
            counter += 1
    
    # 2. Pinch analizinden aksiyonlar
    pinch = factory_data.get("pinch_analysis")
    if pinch and pinch.get("is_valid"):
        recovery_kW = pinch.get("max_heat_recovery_kW", 0)
        if recovery_kW > 0:
            # Basit ısı geri kazanım tasarruf tahmini
            savings = recovery_kW * 8000 * 0.05  # 8000h/yıl, 0.05 EUR/kWh
            investment = recovery_kW * 200  # 200 EUR/kW HX maliyeti
            payback = investment / savings if savings > 0 else 99.9
            
            actions.append(ActionItem(
                id=f"A-{counter:02d}",
                source="pinch",
                equipment_id=None,
                equipment_name=None,
                action=f"Pinch analizi sonuçlarına göre ısı entegrasyonu yapın ({recovery_kW:.0f} kW potansiyel)",
                category="medium_term" if payback < 3 else "strategic",
                estimated_savings_eur=savings,
                estimated_investment_eur=investment,
                payback_years=min(payback, 99.9),
                priority="high" if recovery_kW > 100 else "medium",
                timeline="3-12 ay" if payback < 3 else "1-3 yıl",
            ))
            counter += 1
    
    # 3. Boşluk kapama aksiyonları (yatırımsız, izleme kategorisi)
    # Bu kısım _assess_maturity'deki gap'lerden beslenir
    # Basitleştirilmiş: her critical gap için bir monitoring aksiyonu
    
    # Sıralama: quick_win → medium_term → strategic → monitoring, sonra payback
    category_order = {"quick_win": 0, "medium_term": 1, "strategic": 2, "monitoring": 3}
    actions.sort(key=lambda a: (category_order.get(a.category, 4), a.payback_years))
    
    return actions
```

#### 3.4.5 Görselleştirme ve Yardımcı Fonksiyonlar

```python
def _generate_enpi_radar(enpi: EnPIMetrics) -> dict:
    """EnPI radar chart verisi (0-100 normalize)."""
    # Her EnPI'yi 0-100 ölçeğine normalize et
    return {
        "categories": [
            "Exergy Verimi", "SEC", "Yıkım Oranı", "Kaçınılabilir Kayıp",
            "Maliyet Yoğunluğu", "Isı Geri Kazanım", "Entropi Yoğunluğu"
        ],
        "values": [
            min(100, enpi.exergy_efficiency_pct),                    # Yüksek = iyi
            min(100, max(0, (3 - enpi.specific_exergy_consumption) / 3 * 100)),  # Düşük = iyi
            min(100, max(0, 100 - enpi.exergy_destruction_ratio_pct)),           # Düşük = iyi
            min(100, enpi.avoidable_loss_ratio_pct),                 # Yüksek = iyileştirme fırsatı
            min(100, max(0, 100 - enpi.energy_cost_intensity_eur_kWh * 1000)),   # Düşük = iyi
            min(100, enpi.heat_recovery_potential_pct),              # Yüksek = fırsat
            min(100, max(0, 100 - enpi.entropy_generation_intensity * 100)),     # Düşük = iyi
        ],
    }


def _generate_maturity_radar(dimensions: List[MaturityDimension]) -> dict:
    """Olgunluk radar chart verisi."""
    return {
        "categories": [d.label for d in dimensions],
        "values": [d.score for d in dimensions],
        "max_value": 100,
    }


def _generate_action_timeline(actions: List[ActionItem]) -> dict:
    """Eylem planı timeline chart verisi."""
    categories = {"quick_win": [], "medium_term": [], "strategic": [], "monitoring": []}
    for a in actions:
        categories.get(a.category, []).append({
            "id": a.id,
            "action": a.action[:50],
            "equipment": a.equipment_name or "Fabrika",
            "savings": a.estimated_savings_eur,
            "priority": a.priority,
        })
    return {
        "categories": {k: v for k, v in categories.items() if v},
        "category_labels": {k: v["label"] for k, v in ACTION_CATEGORIES.items()},
        "category_colors": {k: v["color"] for k, v in ACTION_CATEGORIES.items()},
    }


def _summarize_actions(actions: List[ActionItem]) -> dict:
    """Eylem planı özeti."""
    summary = {}
    for cat_key, cat_info in ACTION_CATEGORIES.items():
        cat_actions = [a for a in actions if a.category == cat_key]
        summary[cat_key] = {
            "count": len(cat_actions),
            "label": cat_info["label"],
            "total_savings_eur": sum(a.estimated_savings_eur for a in cat_actions),
            "total_investment_eur": sum(a.estimated_investment_eur for a in cat_actions),
        }
    return summary


def _determine_maturity_level(score: int) -> Tuple[str, str]:
    """Olgunluk seviyesini belirle."""
    for level, info in MATURITY_LEVELS.items():
        if score >= info["min"]:
            return level, info["label"]
    return "aware", MATURITY_LEVELS["aware"]["label"]


def _collect_warnings(enpi, maturity_score, actions):
    """Uyarılar."""
    warnings = []
    if maturity_score < 30:
        warnings.append("Enerji yönetim olgunluğu çok düşük — temel adımlarla başlayın")
    if enpi.exergy_destruction_ratio_pct > 60:
        warnings.append(f"Çok yüksek exergy yıkım oranı: %{enpi.exergy_destruction_ratio_pct:.0f}")
    if not actions:
        warnings.append("Aksiyon planı oluşturulamadı — termoekonomik optimizasyon çalıştırın")
    return warnings


def check_energy_management_feasibility(factory_data: dict) -> Tuple[bool, List[str]]:
    """En az 1 ekipman sonucu olmalı."""
    eq = factory_data.get("equipment_results", [])
    if len(eq) < 1:
        return False, ["Ekipman sonucu yok"]
    return True, []
```

---

## 4. API Entegrasyonu

### 4.1 Factory Engine

`engine/factory.py` → `analyze_factory()` içine, step 10:

```python
# 10. Energy Management — ISO 50001 (optional, best-effort)
energy_management = None
try:
    from .energy_management import analyze_energy_management, check_energy_management_feasibility
    factory_dict = result_so_far.to_dict()  # Şu ana kadarki sonuçları dict'e çevir
    feasible, _ = check_energy_management_feasibility(factory_dict)
    if feasible:
        em_result = analyze_energy_management(factory_dict)
        if em_result.is_valid:
            energy_management = em_result.to_dict()
except Exception:
    pass
```

**Önemli mimari fark:** Bu motor, diğerlerinden farklı olarak `factory_data` (yani `to_dict()` sonucu) alır — çünkü tüm önceki motorların sonuçlarını okuması gerekir. Bu yüzden factory.py'de bu motor en sona eklenmeli ve önceki sonuçları (pinch, advanced_exergy, entropy_generation, thermoeconomic_optimization) içeren bir factory_dict oluşturulmalı.

### 4.2 Endpoint + AI Prompt

Standart pattern: endpoint + 400-char prompt formatter.

```python
def _format_energy_management_for_prompt(em_data: dict) -> str:
    """Max ~400 karakter."""
    if not em_data or not em_data.get("is_valid"):
        return ""
    
    enpi = em_data.get("enpi", {})
    lines = [
        "\n## Enerji Yönetimi (ISO 50001)",
        f"- Olgunluk: {em_data.get('maturity_level_label', 'N/A')} ({em_data.get('maturity_score', 0)}/100)",
        f"- EnPI: η_ex={enpi.get('exergy_efficiency_pct', 0):.0f}%, EDR={enpi.get('exergy_destruction_ratio_pct', 0):.0f}%, ALR={enpi.get('avoidable_loss_ratio_pct', 0):.0f}%",
        f"- Boşluk: {em_data.get('num_gaps', 0)} boyut | Aksiyon: {len(em_data.get('action_plan', []))} adet",
    ]
    
    critical = em_data.get("critical_gaps", [])[:2]
    if critical:
        lines.append(f"- Kritik: {', '.join(critical)}")
    
    result = "\n".join(lines)
    return result[:400]
```

---

## 5. Frontend Entegrasyonu

### 5.1 Component Yapısı

```
frontend/src/components/energy-management/
├── EnergyManagementTab.jsx      # Ana bileşen (tek dosya, inline charts)
```

Tek dosya yaklaşımı (ThermoeconomicTab pattern'i).

### 5.2 Wireframe

```
+----------------------------------------------------------+
| Enerji Yönetimi (ISO 50001)                              |
+----------------------------------------------------------+
|                                                          |
| +-- Olgunluk Skoru --+                                  |
| | [  72 / 100  ]  Olgun (Mature)                        |
| | ████████████████████░░░░░░░░░░                        |
| | "İleri düzey enerji yönetimi"                          |
| +--------------------+                                  |
|                                                          |
| +-- EnPI Özet Kartları --+                              |
| | η_ex: 58%  | SEC: 1.72 | EDR: 42% | ALR: 35% |      |
| | ECI: 0.023 | HRP: 28%  | EGI: 0.42            |      |
| +------------------------+                              |
|                                                          |
| +-- Olgunluk Radar -------+  +-- EnPI Radar --------+  |
| |        Enerji Gözd.      |  |     Exergy Verimi     |  |
| |       /    85    \        |  |     /    58     \      |  |
| | Maliyet    İyileş.|      |  | Entropi    SEC   |     |  |
| |   90   ●    75    |      |  |  58    ●    67   |     |  |
| |       \    60    /        |  |      \    42    /      |  |
| |        Isı Entgr.        |  |       HRP              |  |
| +--------------------------+  +------------------------+  |
|                                                          |
| +-- Boşluk Analizi --+                                  |
| | ⚠ İzleme ve Ölçme (9.1): 45/100                      |
| |   → Entropi bazlı izleme kurulmalı                    |
| |   → Bazı ekipmanların exergy verileri eksik            |
| | ⚠ Isı Entegrasyonu (6.4): 50/100                     |
| |   → Pinch analizi yapılmalı                            |
| +---------------------+                                 |
|                                                          |
| +-- Eylem Planı -------+                                |
| | 🟢 Hızlı Kazanım (0-3 ay)                |           |
| | A-01 Kompresör | Basınç oranı opt. | 8K€/yıl | 0.5y |
| |                                                        |
| | 🟠 Orta Vadeli (3-12 ay)                  |           |
| | A-02 Kazan | Economizer ekle | 18K€/yıl | 2.1y      |
| | A-03 Fabrika | Isı entegrasyonu | 12K€/yıl | 1.8y   |
| |                                                        |
| | 🟣 Stratejik (1-3 yıl)                    |           |
| | A-04 Chiller | Absorpsiyon | 6K€/yıl | 4.2y         |
| +-------------------------+                              |
+----------------------------------------------------------+
```

### 5.3 FactoryDashboard Entegrasyonu

```
FactoryDashboard kart sırası:
  1. MetricBar (mevcut)
  2. PriorityList + IntegrationPanel (mevcut)
  3. FactorySankey (mevcut)
  4. PinchTab (BRIEF_24)
  5. AdvancedExergyTab (BRIEF_26)
  6. EntropyGenerationTab (BRIEF_27)
  7. ThermoeconomicTab (BRIEF_28)
  8. EnergyManagementTab (BRIEF_29 — YENİ)
  9. FactoryAIPanel (mevcut)
```

---

## 6. Testler

### 6.1 `tests/test_energy_management.py`

Tahmini: **~400 satır, 35+ test**

```python
class TestEnPI:
    """Energy Performance Indicator testleri."""
    
    def test_exergy_efficiency(self):
        """η_ex = E_out / E_in × 100."""
    def test_sec(self):
        """SEC = E_in / E_out."""
    def test_edr(self):
        """EDR = I_total / E_in × 100."""
    def test_alr(self):
        """ALR = I_avoidable / I_total × 100."""
    def test_eci(self):
        """ECI = C_dot_D / E_in."""
    def test_hrp(self):
        """HRP = recoverable / I_total × 100."""
    def test_egi(self):
        """EGI = N_s_factory."""
    def test_zero_exergy_in_handled(self):
        """E_in = 0 → tüm EnPI'ler 0."""


class TestMaturity:
    """Olgunluk değerlendirmesi testleri."""
    
    def test_all_dimensions_scored(self):
        """7 boyut skorlanmış."""
    def test_scores_0_to_100(self):
        """0 ≤ skor ≤ 100."""
    def test_maturity_level_assignment(self):
        """Skor → doğru seviye."""
    def test_full_data_high_score(self):
        """Tüm motorlar mevcut → yüksek skor."""
    def test_minimal_data_low_score(self):
        """Sadece temel analiz → düşük skor."""
    def test_findings_and_gaps_populated(self):
        """Bulgular ve boşluklar doldurulmuş."""


class TestMaturityScorers:
    """Her boyutun skorlama testleri."""
    
    def test_energy_review_max_score(self):
        """Tam veri → 100."""
    def test_performance_indicators_no_speco(self):
        """SPECO yok → düşük skor."""
    def test_improvement_all_motors(self):
        """Tüm ileri motorlar → 100."""
    def test_action_planning_no_thermo(self):
        """Termoekonomik yok → 0."""
    def test_heat_integration_with_pinch(self):
        """Pinch mevcut → yüksek skor."""
    def test_cost_optimization_with_speco(self):
        """SPECO + thermo → yüksek skor."""


class TestActionPlan:
    """Eylem planı testleri."""
    
    def test_actions_from_thermoeconomic(self):
        """Termoekonomik önerilerden aksiyon üretilir."""
    def test_actions_from_pinch(self):
        """Pinch'ten ısı geri kazanım aksiyonu."""
    def test_category_assignment_quick_win(self):
        """payback < 1y → quick_win."""
    def test_category_assignment_strategic(self):
        """payback > 3y → strategic."""
    def test_maintain_is_monitoring(self):
        """maintain → monitoring."""
    def test_sorted_by_category_then_payback(self):
        """quick_win → medium → strategic → monitoring, sonra payback."""
    def test_action_ids_sequential(self):
        """A-01, A-02, ... sıralı."""


class TestActionSummary:
    """Aksiyon özeti testleri."""
    
    def test_summary_has_all_categories(self):
        """4 kategori mevcut."""
    def test_totals_consistent(self):
        """Kategori toplamları = genel toplam."""


class TestChartData:
    """Görselleştirme testleri."""
    
    def test_enpi_radar_7_categories(self):
        """7 EnPI kategorisi."""
    def test_enpi_radar_values_0_100(self):
        """Değerler 0-100 arasında."""
    def test_maturity_radar_7_dimensions(self):
        """7 olgunluk boyutu."""
    def test_action_timeline_structure(self):
        """Timeline yapısı doğru."""


class TestEdgeCases:
    """Uç durumlar."""
    
    def test_empty_equipment_invalid(self):
        """Ekipman yok → is_valid=False."""
    def test_minimal_factory_data(self):
        """Sadece temel exergy → valid ama düşük skor."""
    def test_no_advanced_motors(self):
        """İleri motor yok → EnPI kısmen dolu, maturity düşük."""
    def test_serialization(self):
        """to_dict() → JSON sorunsuz."""


class TestIntegration:
    """Entegrasyon."""
    
    def test_factory_includes_energy_management(self):
        """analyze_factory() sonucu energy_management var."""
```

---

## 7. Uygulama Planı

### Faz 1: Engine

| Adım | Dosya | İş |
|------|-------|----|
| 1.1 | `engine/energy_management.py` (YENİ) | Veri yapıları: EnPIMetrics, MaturityDimension, ActionItem, EnergyManagementResult |
| 1.2 | aynı | Sabitler: MATURITY_LEVELS, MATURITY_DIMENSIONS, ACTION_CATEGORIES, GAP_RECOMMENDATIONS |
| 1.3 | aynı | `_calculate_enpi()` — 7 EnPI |
| 1.4 | aynı | 7 scorer fonksiyonu (_score_energy_review, ...) |
| 1.5 | aynı | `_assess_maturity()`, `_determine_maturity_level()` |
| 1.6 | aynı | `_build_action_plan()` — thermo + pinch aksiyonları |
| 1.7 | aynı | `_summarize_actions()` |
| 1.8 | aynı | Chart verileri: `_generate_enpi_radar()`, `_generate_maturity_radar()`, `_generate_action_timeline()` |
| 1.9 | aynı | `_collect_warnings()`, `check_energy_management_feasibility()` |
| 1.10 | aynı | `analyze_energy_management()` ana fonksiyon |
| 1.11 | `engine/__init__.py` | Export ekle |

### Faz 2: Testler

| Adım | İş |
|------|----|
| 2.1 | Fixture: tam donanımlı factory_data (tüm motorlar dahil) + minimal factory_data |
| 2.2-2.8 | 7 test sınıfı, 35+ test |
| 2.9 | Regresyon kontrolü |

### Faz 3: API + Fabrika

| Adım | İş |
|------|----|
| 3.1 | factory.py: energy_management alan + step 10 çağrı |
| 3.2 | Schema + route + endpoint |
| 3.3 | AI prompt formatter |

### Faz 4: Frontend

| Adım | İş |
|------|----|
| 4.1 | EnergyManagementTab.jsx (tek dosya, inline charts) |
| 4.2 | FactoryDashboard entegrasyonu |
| 4.3 | factoryApi.js |

---

## 8. Doğrulama

### Invariantlar
- [ ] 0 ≤ EnPI değerleri (negatif olamaz)
- [ ] 0 ≤ maturity skor ≤ 100 (her boyut)
- [ ] Σ boyut skorları / 7 = maturity_score
- [ ] Action plan sıralı: quick_win → medium → strategic → monitoring
- [ ] Radar chart değerleri 0-100 arasında
- [ ] Tüm maturity level aralıkları boşluksuz (0-29, 30-49, 50-69, 70-89, 90-100)

### Testler
- [ ] `pytest tests/test_energy_management.py -v` geçiyor
- [ ] `pytest tests/ -v` regresyon yok

---

## 9. Claude Code Prompt

```
PROJECT_ANALYSIS.md ve BRIEF_29_ENERGY_MANAGEMENT.md dosyalarını oku.

Görev: ExergyLab'a ISO 50001 Enerji Yönetimi motor modülünü ekle. Bu, son analiz motorudur ve tüm önceki motorların sonuçlarını sentezler.

Faz 1 — Engine modülü:
1. engine/energy_management.py dosyasını oluştur (~550-650 satır).
2. Veri yapıları: EnPIMetrics, MaturityDimension, ActionItem, EnergyManagementResult (to_dict). Brief 3.2.
3. Sabitler: MATURITY_LEVELS (5 seviye), MATURITY_DIMENSIONS (7 boyut, ISO maddeleri), ACTION_CATEGORIES (4 kategori + renk + timeline), GAP_RECOMMENDATIONS (7 boyut × 3 öneri). Brief 2.2, 2.3, 3.3.
4. _calculate_enpi(factory_data) → EnPIMetrics: 7 EnPI hesapla. Brief 2.1, 3.4.2. Sıfır bölme koruması.
5. 7 scorer fonksiyonu: _score_energy_review, _score_performance_indicators, _score_improvement_opportunities, _score_action_planning, _score_monitoring, _score_heat_integration, _score_cost_optimization. Her biri (factory_data) → (score, findings, gaps). Brief 3.4.3'teki ayrıntılı mantık.
6. MATURITY_SCORERS dict: scorer fonksiyonlarını boyut key'lerine map et.
7. _assess_maturity(factory_data) → List[MaturityDimension]: MATURITY_SCORERS iterate, clamp 0-100.
8. _determine_maturity_level(score) → (level, label): leading≥90, mature≥70, developing≥50, beginning≥30, aware<30.
9. _build_action_plan(factory_data) → List[ActionItem]: thermoeconomic'ten (recommendations → actions) + pinch'ten (recovery → action). Kategori: payback<1→quick_win, <3→medium_term, else→strategic, maintain→monitoring. Sırala: kategori → payback. Brief 3.4.4.
10. _summarize_actions(actions) → dict: kategori bazlı count + total_savings + total_investment.
11. _generate_enpi_radar(enpi) → dict: 7 kategori, 0-100 normalize. Brief 3.4.5.
12. _generate_maturity_radar(dimensions) → dict: 7 boyut, 0-100.
13. _generate_action_timeline(actions) → dict: kategori bazlı gruplar.
14. _collect_warnings(), check_energy_management_feasibility().
15. analyze_energy_management(factory_data) → EnergyManagementResult: ana fonksiyon.
16. engine/__init__.py güncelle.

Faz 2 — Testler:
17. tests/test_energy_management.py (~400 satır, 35+ test).
18. 2 fixture: full_factory_data (tüm motorlar dahil: pinch_analysis, advanced_exergy, entropy_generation, thermoeconomic_optimization + equipment_results) ve minimal_factory_data (sadece equipment_results).
19. EnPI testleri (8 test): her 7 EnPI formülü + sıfır bölme.
20. Maturity testleri (6 test): 7 boyut, 0-100, level assignment, yüksek/düşük skor.
21. Scorer testleri (6 test): her boyut için spesifik senaryo.
22. Action plan testleri (7 test): thermo kaynak, pinch kaynak, kategori ataması, sıralama, ID'ler.
23. Summary + chart testleri (4 test): 4 kategori, radar boyutları, 0-100.
24. Edge case + entegrasyon (4 test): boş veri, minimal veri, serialization, factory integration.
25. pytest tests/test_energy_management.py -v
26. pytest tests/ -v (regresyon)

Faz 3 — API + Fabrika:
27. engine/factory.py → energy_management: Optional[dict] = None + step 10 çağrı.
    ÖNEMLİ: Bu motor factory_data (to_dict() sonucu) alır. Önceki adımlarda oluşturulan result'ı bir dict'e çevirip gönder. Tüm önceki motor sonuçlarını (pinch, advanced_exergy, entropy_generation, thermoeconomic_optimization) bu dict'e dahil et.
28. api/schemas/factory.py → alan ekle.
29. api/routes/factory.py → response + POST /energy-management endpoint.
30. api/services/claude_code_service.py → _format_energy_management_for_prompt() (max 400 char) + prompt'a ekle.

Faz 4 — Frontend:
31. frontend/src/components/energy-management/EnergyManagementTab.jsx (tek dosya, ~200 satır).
    - Olgunluk skoru bar (progress bar + level label)
    - EnPI özet kartlar
    - 2 Plotly radar chart (olgunluk + EnPI) yan yana
    - Boşluk analizi listesi (skor < 70 olanlar, gap önerileri)
    - Eylem planı: kategoriye göre gruplu, renkli badge, savings/investment/payback
32. FactoryDashboard.jsx → EnergyManagementTab entegrasyonu (ThermoeconomicTab'dan sonra, AI Panel'den önce).
33. factoryApi.js → runEnergyManagement() ekle.

Önemli kurallar:
- Bu motor tüm önceki sonuçları sentezler — factory_data dict alır (equipment_list + analysis_results değil).
- Minimum gereksinim: 1 ekipman sonucu (diğer motorlar opsiyonel).
- Her boyut 0-100, toplam = ortalama.
- EnPI'ler mevcut alanlardan türetilir — sıfır bölme her yerde korunmalı.
- Action plan sıralaması: quick_win → medium_term → strategic → monitoring, sonra payback ascending.
- Pinch'ten gelen savings: recovery_kW × 8000 × 0.05, investment: recovery_kW × 200.
- Tüm metinler (findings, gaps, action descriptions) Türkçe.
```

---

## 10. Bilinen Kısıtlamalar

| Kısıtlama | Açıklama | Gelecek Çözüm |
|-----------|----------|---------------|
| Statik skorlama | Mevcut veri mevcudiyetine dayalı, gerçek ISO denetimine değil | Uzman denetim entegrasyonu |
| Zaman boyutu yok | Tek anlık değerlendirme, trend yok | Periyodik değerlendirme karşılaştırması |
| Action plan basit | Sadece thermo + pinch'ten aksiyon, manuel eklenemiyor | Kullanıcı tanımlı aksiyonlar |
| Pinch savings tahmini | Sabit 0.05 EUR/kWh ve 200 EUR/kW | Gerçek enerji fiyatları ve HX maliyetleri |

---

*BRIEF_29 — Energy Management (ISO 50001) Motor Modülü*
*Bu, ExergyLab'ın 6. ve son analiz motorudur.*
*Tarih: 2026-02-06*
*Bağımlılık: Tüm önceki motorlar (opsiyonel ama skoru etkiler)*
