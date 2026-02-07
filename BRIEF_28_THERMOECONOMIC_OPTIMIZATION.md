# BRIEF_28: Thermoeconomic Optimization Motor Modülü

> **Tarih:** 2026-02-06
> **Öncelik:** Orta-Yüksek
> **Tahmini Süre:** 3-5 saat
> **Karmaşıklık:** Orta-Yüksek
> **Bağımlılıklar:** Exergoekonomik (exergoeconomic.py), AV/UN (core.py), fabrika (factory.py)
> **Etkilenen Dosyalar:** Yeni + mevcut toplam ~12 dosya

---

## 1. Bağlam ve Motivasyon

### 1.1 Neden Termoekonomik Optimizasyon?

ExergyLab şu an 4 analiz katmanına sahip:
1. **Exergy analizi** — ne kadar kayıp var?
2. **AV/UN + EN/EX** — kayıp kaçınılabilir mi, nereden geliyor?
3. **Exergoekonomik (SPECO)** — kaybın maliyeti nedir? (Z_dot, C_dot_D, f, r)
4. **EGM** — tersinmezlik hangi mekanizmadan?

Eksik olan: **bu bilgileri kullanarak optimizasyon önerileri üretmek.** Termoekonomik optimizasyon, SPECO sonuçlarını (özellikle f-faktör ve r-faktör) kullanarak her ekipman için **ne yapılması gerektiğini** sistematik olarak belirler.

### 1.2 Tsatsaronis'in Optimizasyon Karar Kuralları

SPECO'dan gelen f-faktör ve r-faktör, optimizasyon yönünü belirler:

```
f-faktör = Z_dot / (Z_dot + C_dot_D)
  → Yatırım maliyetinin toplam maliyet oranındaki payı

r-faktör = (c_product - c_fuel) / c_fuel
  → Birim ürün exergy maliyetindeki göreli artış
```

**Karar matrisi:**

| f-faktör | r-faktör | Yorum | Strateji |
|----------|----------|-------|----------|
| Düşük (<0.25) | Yüksek | Exergy yıkım maliyeti baskın | Verim artır (daha iyi ekipman) → C_dot_D düşer |
| Yüksek (>0.65) | Düşük | Yatırım maliyeti baskın | Daha ucuz/basit ekipman → Z_dot düşer |
| Yüksek (>0.65) | Yüksek | Her ikisi de yüksek | Sistem tasarımını değiştir (yapısal optimizasyon) |
| Orta (0.25-0.65) | Düşük | Dengeli | İnce ayar (parametrik optimizasyon) |
| Orta (0.25-0.65) | Orta | Dengeli | Sürdür, izle |

### 1.3 Parametrik vs. Yapısal Optimizasyon

**Parametrik optimizasyon:** Mevcut ekipmanın çalışma koşullarını değiştir
- Kompresör: basınç oranını, ara soğutma sıcaklığını optimize et
- Kazan: fazla hava oranını, baca sıcaklığını optimize et
- Isı eşanjörü: akış hızlarını, ΔT yaklaşımını optimize et

**Yapısal optimizasyon:** Sistem konfigürasyonunu değiştir
- Ekipman ekle/çıkar (economizer, preheater)
- Akış düzenini değiştir (seri/paralel)
- Farklı teknoloji seç (absorpsiyon vs. kompresyon chiller)

### 1.4 Knowledge Base

`knowledge/factory/thermoeconomic_optimization/` dizininde ~16 dosya mevcut. Uygulama koşulu: **C_D > 50,000 EUR/yıl**.

---

## 2. Teori — Termoekonomik Optimizasyon

### 2.1 Ekipman Bazlı Optimizasyon Değerlendirmesi

Her ekipman için aşağıdaki metrikler hesaplanır:

```
Toplam maliyet oranı:
  C_total_dot = Z_dot + C_dot_D                (EUR/h)

Yıllık toplam maliyet:
  C_total_annual = C_total_dot × operating_hours  (EUR/yıl)

Optimizasyon potansiyeli:
  C_savings_potential = C_dot_D × avoidable_ratio  (EUR/h)
  → Kaçınılabilir exergy yıkımının maliyeti

Yıllık tasarruf potansiyeli:
  C_savings_annual = C_savings_potential × operating_hours  (EUR/yıl)
```

### 2.2 Optimizasyon Stratejisi Belirleme

```python
def determine_optimization_strategy(f_factor, r_factor, avoidable_ratio):
    """
    f-faktör ve r-faktör bazında optimizasyon stratejisi.
    
    Returns:
        strategy: "parametric" | "structural" | "invest" | "downsize" | "maintain"
        action: Kısa açıklama
        priority: "high" | "medium" | "low"
    """
    if f_factor < 0.25:
        if r_factor > 0.50:
            # Düşük f, yüksek r → verim artır
            return "invest", "Daha verimli ekipmana yatırım yapın", "high"
        else:
            return "parametric", "Çalışma parametrelerini optimize edin", "medium"
    
    elif f_factor > 0.65:
        if r_factor > 0.50:
            # Yüksek f, yüksek r → sistem değişikliği
            return "structural", "Sistem konfigürasyonunu değiştirin", "high"
        else:
            # Yüksek f, düşük r → maliyet azalt
            return "downsize", "Daha ekonomik alternatif değerlendirin", "medium"
    
    else:  # 0.25 ≤ f ≤ 0.65
        if avoidable_ratio > 0.30:
            return "parametric", "Parametrik iyileştirme potansiyeli var", "medium"
        else:
            return "maintain", "Mevcut durumu sürdürün", "low"
```

### 2.3 Ekipman Tipine Özel Optimizasyon Önerileri

```python
OPTIMIZATION_ACTIONS = {
    "compressor": {
        "invest": [
            "Yüksek verimli motor ve VSD (değişken hız sürücüsü) ekleyin",
            "İzentropik verimi yüksek kompresör tipine geçin",
            "Çok kademeli kompresyon ile ara soğutma ekleyin",
        ],
        "parametric": [
            "Basınç oranını optimize edin (kaçak testi yapın)",
            "Emme havası sıcaklığını düşürün (aftercooler bakımı)",
            "Yük profilini analiz edin — kısmi yükte VSD kullanın",
        ],
        "structural": [
            "Kompresyon kademesi ekleyin (2→3 kademe)",
            "Isı geri kazanımlı kompresör sistemine geçin",
            "Merkezi sistemi bölgesel ünitelere ayırın",
        ],
        "downsize": [
            "Aşırı boyutlandırma analizi yapın",
            "Sabit hızlı yerine VSD'li daha küçük ünite değerlendirin",
        ],
    },
    "boiler": {
        "invest": [
            "Yoğuşmalı kazan teknolojisine geçin",
            "Economizer / hava ön ısıtıcı ekleyin",
            "Atık ısı geri kazanım sistemi kurun",
        ],
        "parametric": [
            "Fazla hava oranını optimize edin (O₂ trim kontrol)",
            "Baca gazı sıcaklığını düşürün (economizer bakımı)",
            "Blöf oranını optimize edin",
        ],
        "structural": [
            "Bölgesel ısıtma ağı kurun (birden fazla kazan)",
            "Kojenerasyon (CHP) sistemi değerlendirin",
            "Yakıt tipini değiştirin (doğalgaz → biyokütle/atık ısı)",
        ],
        "downsize": [
            "Kazan kapasitesini yeniden boyutlandırın",
            "Modüler kazan sistemi değerlendirin",
        ],
    },
    "chiller": {
        "invest": [
            "Yüksek COP'lu chiller'a geçin",
            "Serbest soğutma (free cooling) sistemi ekleyin",
            "Soğuk akü (thermal storage) değerlendirin",
        ],
        "parametric": [
            "Evaporatör/kondenser yaklaşım sıcaklığını optimize edin",
            "Soğutma kulesi bakımını artırın (kondenser sıcaklığı)",
            "Set noktasını mevsime göre ayarlayın",
        ],
        "structural": [
            "Absorpsiyon chiller ile atık ısı kullanın",
            "Kaskad soğutma sistemi değerlendirin",
            "Bölgesel soğutma ağı kurun",
        ],
        "downsize": [
            "Soğutma yükünü yeniden hesaplayın",
            "Değişken debili pompalama sistemi kurun",
        ],
    },
    "pump": {
        "invest": [
            "Yüksek verimli motor ve VSD ekleyin",
            "Pompa tipini optimize edin (spesifik hız uyumu)",
        ],
        "parametric": [
            "Çalışma noktasını BEP'e (en iyi verimlilik noktası) yaklaştırın",
            "Boru hattı kayıplarını azaltın (vana, dirsek)",
            "İmpeller çapını optimize edin",
        ],
        "structural": [
            "Paralel pompa konfigürasyonu değerlendirin",
            "Booster pompa ekleyerek ana pompa boyutunu küçültün",
        ],
        "downsize": [
            "Aşırı boyutlanmış pompayı değiştirin",
            "İmpeller kırpma (trimming) uygulayın",
        ],
    },
    "heat_exchanger": {
        "invest": [
            "Daha büyük ısı transfer alanı ile ΔT yaklaşımını düşürün",
            "Plakalı eşanjöre geçin (daha yüksek U değeri)",
            "Fouling direncini azaltan yüzey kaplaması uygulayın",
        ],
        "parametric": [
            "Temizlik programını optimize edin (fouling kontrolü)",
            "Akış hızlarını optimize edin (ΔP vs. ΔT dengesi)",
            "Bypass ayarını kontrol edin",
        ],
        "structural": [
            "Çok akışlı eşanjör ağı tasarlayın (pinch analizi)",
            "Isı pompalı geri kazanım sistemi ekleyin",
            "Kondensasyon ekonomizeri ekleyin",
        ],
        "downsize": [
            "Aşırı boyutlanmış eşanjörü küçültün",
            "Paralel bağlantıyı seri bağlantıya çevirin",
        ],
    },
    "steam_turbine": {
        "invest": [
            "Daha yüksek izentropik verimli türbine geçin",
            "Çok kademeli türbin değerlendirin",
            "Kanatçık yükseltme/değiştirme yapın",
        ],
        "parametric": [
            "Giriş buharı koşullarını optimize edin (kazan ile koordine)",
            "Çıkış basıncını optimize edin",
            "Sızıntı kontrolü yapın (şaft contası)",
        ],
        "structural": [
            "Ekstraksiyon türbine geçin (CHP)",
            "ORC (Organik Rankine Çevrimi) ekleyin",
            "Kondens sistemi iyileştirin (vakum)",
        ],
        "downsize": [
            "Türbin kapasitesini yeniden değerlendirin",
            "Kısmi yük performansını analiz edin",
        ],
    },
    "dryer": {
        "invest": [
            "Isı pompalı kurutma sistemine geçin",
            "Egzoz havası ısı geri kazanımı ekleyin",
            "Mekanik ön-susuzlaştırma ile termal yükü azaltın",
        ],
        "parametric": [
            "Kurutma havası sıcaklık ve debisini optimize edin",
            "Çıkış nem kontrol stratejisini iyileştirin",
            "Ürün giriş nem oranını düşürün (ön işlem)",
        ],
        "structural": [
            "Çok kademeli kurutma sistemi değerlendirin",
            "Güneş enerjili ön ısıtma ekleyin",
            "Atık ısı kaynağından besleme yapın",
        ],
        "downsize": [
            "Kurutma kapasitesini üretim hızına göre ayarlayın",
            "Kesikli/sürekli mod seçimini optimize edin",
        ],
    },
}
```

### 2.4 Fabrika Seviyesi Optimizasyon

```
Toplam optimizasyon potansiyeli:
  C_savings_total = Σ_k C_dot_D_k × avoidable_ratio_k × operating_hours

Strateji dağılımı:
  n_invest, n_parametric, n_structural, n_downsize, n_maintain

Yatırım geri dönüş tahmini (basitleştirilmiş):
  Parametrik: ~0 yatırım, 6-12 ay geri dönüş (bakım maliyeti)
  İnvest: yüksek yatırım, 2-5 yıl geri dönüş
  Yapısal: çok yüksek yatırım, 3-7 yıl geri dönüş
  
Basitleştirilmiş ROI tahmini:
  payback_years = estimated_investment / C_savings_annual
```

### 2.5 Yatırım Maliyet Tahminleri (Kapasite Bazlı)

```python
# Optimizasyon tipi başına tahmini yatırım maliyeti (EUR)
# capacity = ekipmanın nominal gücü (kW)
INVESTMENT_ESTIMATES = {
    "compressor": {
        "invest": lambda cap: 500 * cap**0.7,       # VSD + yüksek verim motor
        "parametric": lambda cap: 50 * cap**0.5,     # Kontrol optimizasyonu
        "structural": lambda cap: 800 * cap**0.7,    # Kademe ekleme
        "downsize": lambda cap: 300 * cap**0.7,      # Yeni küçük ünite
    },
    "boiler": {
        "invest": lambda cap: 400 * cap**0.75,       # Economizer + kontrol
        "parametric": lambda cap: 30 * cap**0.5,     # O₂ trim
        "structural": lambda cap: 1200 * cap**0.75,  # CHP sistemi
        "downsize": lambda cap: 250 * cap**0.75,     # Modüler kazan
    },
    "chiller": {
        "invest": lambda cap: 350 * cap**0.8,        # Yüksek COP chiller
        "parametric": lambda cap: 40 * cap**0.5,     # Optimizasyon
        "structural": lambda cap: 600 * cap**0.8,    # Absorpsiyon ekleme
        "downsize": lambda cap: 200 * cap**0.8,      # Küçültme
    },
    "pump": {
        "invest": lambda cap: 300 * cap**0.65,       # VSD + verimli motor
        "parametric": lambda cap: 20 * cap**0.5,     # İmpeller trim
        "structural": lambda cap: 400 * cap**0.65,   # Paralel pompa
        "downsize": lambda cap: 150 * cap**0.65,     # Küçük pompa
    },
    "heat_exchanger": {
        "invest": lambda cap: 250 * cap**0.7,        # Büyük alan / plakalı
        "parametric": lambda cap: 15 * cap**0.5,     # Temizlik programı
        "structural": lambda cap: 500 * cap**0.7,    # HEN yeniden tasarım
        "downsize": lambda cap: 100 * cap**0.7,      # Küçültme
    },
    "steam_turbine": {
        "invest": lambda cap: 600 * cap**0.7,        # Kanatçık yükseltme
        "parametric": lambda cap: 40 * cap**0.5,     # Sızıntı kontrolü
        "structural": lambda cap: 1500 * cap**0.7,   # ORC ekleme
        "downsize": lambda cap: 400 * cap**0.7,      # Yeniden boyutlama
    },
    "dryer": {
        "invest": lambda cap: 450 * cap**0.7,        # Isı geri kazanım
        "parametric": lambda cap: 35 * cap**0.5,     # Kontrol iyileştirme
        "structural": lambda cap: 700 * cap**0.7,    # Çok kademeli
        "downsize": lambda cap: 200 * cap**0.7,      # Kapasite azaltma
    },
}
```

---

## 3. Engine Modülü: `engine/thermoeconomic_optimization.py`

### 3.1 Dosya Yapısı

Tahmini boyut: **~550-650 satır**

### 3.2 Veri Yapıları

```python
@dataclass
class OptimizationRecommendation:
    """Tek ekipman için termoekonomik optimizasyon önerisi."""
    equipment_id: str
    equipment_name: str
    equipment_type: str
    subtype: str
    
    # SPECO metrikleri (mevcut sonuçlardan)
    f_factor: float                      # Z_dot / (Z_dot + C_dot_D)
    r_factor: float                      # (c_product - c_fuel) / c_fuel
    Z_dot_eur_h: float                   # Yatırım maliyet oranı
    C_dot_D_eur_h: float                 # Yıkım maliyet oranı
    C_total_dot_eur_h: float             # Z_dot + C_dot_D
    
    # AV/UN
    avoidable_ratio: float               # 0-1
    
    # Optimizasyon stratejisi
    strategy: str                        # "invest" | "parametric" | "structural" | "downsize" | "maintain"
    strategy_label: str                  # İnsan-okunur etiket
    priority: str                        # "high" | "medium" | "low"
    
    # Aksiyonlar (ekipman tipine özel)
    recommended_actions: List[str]
    
    # Ekonomik potansiyel
    C_savings_potential_eur_h: float     # C_dot_D × avoidable_ratio
    C_savings_annual_eur: float          # Yıllık tasarruf
    estimated_investment_eur: float      # Tahmini yatırım maliyeti
    simple_payback_years: float          # Basit geri ödeme süresi
    
    def to_dict(self) -> dict:
        return {
            "equipment_id": self.equipment_id,
            "equipment_name": self.equipment_name,
            "equipment_type": self.equipment_type,
            "subtype": self.subtype,
            "f_factor": round(self.f_factor, 3),
            "r_factor": round(self.r_factor, 3),
            "Z_dot_eur_h": round(self.Z_dot_eur_h, 4),
            "C_dot_D_eur_h": round(self.C_dot_D_eur_h, 4),
            "C_total_dot_eur_h": round(self.C_total_dot_eur_h, 4),
            "avoidable_ratio": round(self.avoidable_ratio, 3),
            "strategy": self.strategy,
            "strategy_label": self.strategy_label,
            "priority": self.priority,
            "recommended_actions": self.recommended_actions,
            "C_savings_potential_eur_h": round(self.C_savings_potential_eur_h, 4),
            "C_savings_annual_eur": round(self.C_savings_annual_eur, 2),
            "estimated_investment_eur": round(self.estimated_investment_eur, 2),
            "simple_payback_years": round(self.simple_payback_years, 1),
        }


@dataclass
class ThermoeconomicOptimizationResult:
    """Fabrika seviyesi termoekonomik optimizasyon sonucu."""
    num_equipment: int
    operating_hours: int
    
    # Toplam maliyetler
    total_Z_dot_eur_h: float
    total_C_dot_D_eur_h: float
    total_C_total_dot_eur_h: float
    factory_f_factor: float              # Fabrika geneli f-faktör
    
    # Toplam optimizasyon potansiyeli
    total_savings_potential_eur_h: float
    total_savings_annual_eur: float
    total_estimated_investment_eur: float
    factory_payback_years: float
    
    # Strateji dağılımı
    strategy_distribution: Dict[str, int]  # {"invest": 2, "parametric": 3, ...}
    
    # Öncelik dağılımı
    priority_distribution: Dict[str, int]  # {"high": 2, "medium": 3, "low": 1}
    
    # Ekipman önerileri (C_savings_annual bazlı sıralı)
    recommendations: List[OptimizationRecommendation]
    
    # Cost-benefit sıralaması
    cost_benefit_ranking: List[Dict]     # ROI bazlı sıralama
    
    # Görselleştirme
    f_r_scatter_data: Dict               # f-r scatter plot verisi
    savings_waterfall_data: Dict         # Tasarruf waterfall chart verisi
    
    # Uyarılar
    warnings: List[str]
    
    is_valid: bool = True
    error_message: str = ""
    
    def to_dict(self) -> dict:
        return {
            "is_valid": self.is_valid,
            "error_message": self.error_message,
            "num_equipment": self.num_equipment,
            "operating_hours": self.operating_hours,
            "total_Z_dot_eur_h": round(self.total_Z_dot_eur_h, 4),
            "total_C_dot_D_eur_h": round(self.total_C_dot_D_eur_h, 4),
            "total_C_total_dot_eur_h": round(self.total_C_total_dot_eur_h, 4),
            "factory_f_factor": round(self.factory_f_factor, 3),
            "total_savings_potential_eur_h": round(self.total_savings_potential_eur_h, 4),
            "total_savings_annual_eur": round(self.total_savings_annual_eur, 2),
            "total_estimated_investment_eur": round(self.total_estimated_investment_eur, 2),
            "factory_payback_years": round(self.factory_payback_years, 1),
            "strategy_distribution": self.strategy_distribution,
            "priority_distribution": self.priority_distribution,
            "recommendations": [r.to_dict() for r in self.recommendations],
            "cost_benefit_ranking": self.cost_benefit_ranking,
            "f_r_scatter_data": self.f_r_scatter_data,
            "savings_waterfall_data": self.savings_waterfall_data,
            "warnings": self.warnings,
        }
```

### 3.3 Sabit Veriler

```python
# Strateji etiketleri (Türkçe)
STRATEGY_LABELS = {
    "invest": "Verimli ekipmana yatırım",
    "parametric": "Parametrik optimizasyon",
    "structural": "Yapısal değişiklik",
    "downsize": "Boyut küçültme",
    "maintain": "Mevcut durumu sürdür",
}

# Strateji renkleri (frontend için)
STRATEGY_COLORS = {
    "invest": "#ef4444",       # Kırmızı — yüksek yatırım
    "parametric": "#f59e0b",   # Turuncu — orta efor
    "structural": "#8b5cf6",   # Mor — sistem değişikliği
    "downsize": "#3b82f6",     # Mavi — maliyet azaltma
    "maintain": "#22c55e",     # Yeşil — sorun yok
}

# OPTIMIZATION_ACTIONS — Bölüm 2.3'teki tam sözlük
# INVESTMENT_ESTIMATES — Bölüm 2.5'teki tam sözlük
```

### 3.4 Ana Fonksiyonlar

#### 3.4.1 `analyze_thermoeconomic_optimization()`

```python
def analyze_thermoeconomic_optimization(
    equipment_list: List[dict],
    analysis_results: Dict[str, dict],
    operating_hours: int = 8000,
) -> ThermoeconomicOptimizationResult:
    """
    Fabrika ekipmanları için termoekonomik optimizasyon.
    
    Args:
        equipment_list: Fabrika ekipman listesi
        analysis_results: Her ekipmanın analiz sonuçları {id: result_dict}
        operating_hours: Yıllık çalışma saati (varsayılan 8000)
    """
    # 1. Exergoekonomik verisi olan ekipmanları filtrele
    valid = _filter_valid_equipment(equipment_list, analysis_results)
    if len(valid) < 1:
        return ThermoeconomicOptimizationResult(
            is_valid=False,
            error_message="Exergoekonomik verisi olan ekipman yok",
            # ... boş değerler
        )
    
    # 2. Her ekipman için optimizasyon önerisi
    recommendations = []
    for item in valid:
        result = analysis_results[item["id"]]
        rec = _generate_recommendation(item, result, operating_hours)
        recommendations.append(rec)
    
    # 3. C_savings_annual bazlı sırala (büyükten küçüğe)
    recommendations.sort(key=lambda r: r.C_savings_annual_eur, reverse=True)
    
    # 4. Fabrika metrikleri
    factory_metrics = _calculate_factory_metrics(recommendations, operating_hours)
    
    # 5. Cost-benefit sıralaması
    cost_benefit = _create_cost_benefit_ranking(recommendations)
    
    # 6. f-r scatter plot verisi
    f_r_data = _generate_f_r_scatter(recommendations)
    
    # 7. Tasarruf waterfall verisi
    waterfall_data = _generate_savings_waterfall(recommendations)
    
    # 8. Uyarılar
    warnings = _collect_warnings(recommendations, factory_metrics)
    
    return ThermoeconomicOptimizationResult(
        num_equipment=len(recommendations),
        operating_hours=operating_hours,
        recommendations=recommendations,
        cost_benefit_ranking=cost_benefit,
        f_r_scatter_data=f_r_data,
        savings_waterfall_data=waterfall_data,
        warnings=warnings,
        **factory_metrics,
    )
```

#### 3.4.2 `_filter_valid_equipment()`

```python
def _filter_valid_equipment(equipment_list, analysis_results):
    """Exergoekonomik verisi olan ekipmanları filtrele."""
    valid = []
    for item in equipment_list:
        result = analysis_results.get(item.get("id", ""))
        if not result:
            continue
        # Exergoekonomik alanlar mevcut olmalı
        f = result.get("exergoeconomic_f_factor")
        if f is not None and f >= 0:
            valid.append(item)
    return valid
```

#### 3.4.3 `_generate_recommendation()`

```python
def _generate_recommendation(item, result, operating_hours):
    """Tek ekipman için optimizasyon önerisi üret."""
    eq_type = item["equipment_type"]
    subtype = item.get("subtype", "_default")
    
    # SPECO verileri
    f = result.get("exergoeconomic_f_factor", 0.5)
    r = result.get("exergoeconomic_r_factor", 0.5)
    Z_dot = result.get("exergoeconomic_Z_dot_eur_h", 0)
    C_dot_D = result.get("exergoeconomic_C_dot_destruction_eur_h", 0)
    avoidable_ratio = result.get("avoidable_ratio_pct", 0) / 100.0
    
    C_total_dot = Z_dot + C_dot_D
    
    # Strateji belirleme
    strategy, action, priority = _determine_strategy(f, r, avoidable_ratio)
    
    # Ekipman tipine özel aksiyonlar
    actions = _get_equipment_actions(eq_type, strategy)
    
    # Tasarruf potansiyeli
    C_savings_h = C_dot_D * avoidable_ratio
    C_savings_annual = C_savings_h * operating_hours
    
    # Yatırım tahmini
    capacity = result.get("exergy_in_kW", 100)  # Kapasite yaklaşımı
    investment = _estimate_investment(eq_type, strategy, capacity)
    
    # Geri ödeme
    payback = investment / C_savings_annual if C_savings_annual > 0 else 99.9
    payback = min(payback, 99.9)  # Üst sınır
    
    return OptimizationRecommendation(
        equipment_id=item["id"],
        equipment_name=item.get("name", eq_type),
        equipment_type=eq_type,
        subtype=subtype,
        f_factor=f,
        r_factor=r,
        Z_dot_eur_h=Z_dot,
        C_dot_D_eur_h=C_dot_D,
        C_total_dot_eur_h=C_total_dot,
        avoidable_ratio=avoidable_ratio,
        strategy=strategy,
        strategy_label=STRATEGY_LABELS.get(strategy, strategy),
        priority=priority,
        recommended_actions=actions,
        C_savings_potential_eur_h=C_savings_h,
        C_savings_annual_eur=C_savings_annual,
        estimated_investment_eur=investment,
        simple_payback_years=payback,
    )
```

#### 3.4.4 `_determine_strategy()`

```python
def _determine_strategy(f_factor, r_factor, avoidable_ratio):
    """f/r bazlı optimizasyon stratejisi — Bölüm 2.2 karar matrisi."""
    if f_factor < 0.25:
        if r_factor > 0.50:
            return "invest", STRATEGY_LABELS["invest"], "high"
        else:
            return "parametric", STRATEGY_LABELS["parametric"], "medium"
    elif f_factor > 0.65:
        if r_factor > 0.50:
            return "structural", STRATEGY_LABELS["structural"], "high"
        else:
            return "downsize", STRATEGY_LABELS["downsize"], "medium"
    else:
        if avoidable_ratio > 0.30:
            return "parametric", STRATEGY_LABELS["parametric"], "medium"
        else:
            return "maintain", STRATEGY_LABELS["maintain"], "low"
```

#### 3.4.5 `_get_equipment_actions()`

```python
def _get_equipment_actions(eq_type, strategy):
    """Ekipman tipine özel optimizasyon aksiyonları."""
    type_actions = OPTIMIZATION_ACTIONS.get(eq_type, {})
    actions = type_actions.get(strategy, [])
    if not actions:
        # Genel fallback aksiyonlar
        fallback = {
            "invest": ["Daha verimli ekipmana yatırım yapın"],
            "parametric": ["Çalışma parametrelerini optimize edin"],
            "structural": ["Sistem konfigürasyonunu değiştirin"],
            "downsize": ["Ekipman boyutunu küçültün"],
            "maintain": ["Mevcut bakım programını sürdürün"],
        }
        actions = fallback.get(strategy, ["Değerlendirme yapın"])
    return actions
```

#### 3.4.6 `_estimate_investment()`

```python
def _estimate_investment(eq_type, strategy, capacity_kW):
    """Optimizasyon yatırım maliyeti tahmini."""
    if strategy == "maintain":
        return 0.0
    
    type_estimates = INVESTMENT_ESTIMATES.get(eq_type, {})
    estimator = type_estimates.get(strategy)
    
    if estimator and capacity_kW > 0:
        return estimator(max(capacity_kW, 10))  # Min 10 kW
    
    # Genel fallback
    fallback = {
        "invest": 300 * capacity_kW**0.7,
        "parametric": 30 * capacity_kW**0.5,
        "structural": 600 * capacity_kW**0.7,
        "downsize": 150 * capacity_kW**0.7,
    }
    return fallback.get(strategy, 0)
```

#### 3.4.7 `_calculate_factory_metrics()`

```python
def _calculate_factory_metrics(recommendations, operating_hours):
    """Fabrika seviyesi metrikleri."""
    total_Z = sum(r.Z_dot_eur_h for r in recommendations)
    total_CD = sum(r.C_dot_D_eur_h for r in recommendations)
    total_C = total_Z + total_CD
    total_savings_h = sum(r.C_savings_potential_eur_h for r in recommendations)
    total_savings_yr = sum(r.C_savings_annual_eur for r in recommendations)
    total_invest = sum(r.estimated_investment_eur for r in recommendations)
    
    factory_f = total_Z / total_C if total_C > 0 else 0.5
    factory_payback = total_invest / total_savings_yr if total_savings_yr > 0 else 99.9
    factory_payback = min(factory_payback, 99.9)
    
    # Dağılımlar
    strategy_dist = {}
    priority_dist = {}
    for r in recommendations:
        strategy_dist[r.strategy] = strategy_dist.get(r.strategy, 0) + 1
        priority_dist[r.priority] = priority_dist.get(r.priority, 0) + 1
    
    return {
        "total_Z_dot_eur_h": total_Z,
        "total_C_dot_D_eur_h": total_CD,
        "total_C_total_dot_eur_h": total_C,
        "factory_f_factor": factory_f,
        "total_savings_potential_eur_h": total_savings_h,
        "total_savings_annual_eur": total_savings_yr,
        "total_estimated_investment_eur": total_invest,
        "factory_payback_years": factory_payback,
        "strategy_distribution": strategy_dist,
        "priority_distribution": priority_dist,
    }
```

#### 3.4.8 `_create_cost_benefit_ranking()`

```python
def _create_cost_benefit_ranking(recommendations):
    """ROI bazlı sıralama (en kısa geri ödeme ilk)."""
    # maintain olanları hariç tut
    actionable = [r for r in recommendations if r.strategy != "maintain"]
    ranked = sorted(actionable, key=lambda r: r.simple_payback_years)
    return [
        {
            "equipment_id": r.equipment_id,
            "equipment_name": r.equipment_name,
            "strategy": r.strategy,
            "strategy_label": r.strategy_label,
            "C_savings_annual_eur": round(r.C_savings_annual_eur, 2),
            "estimated_investment_eur": round(r.estimated_investment_eur, 2),
            "simple_payback_years": round(r.simple_payback_years, 1),
            "priority": r.priority,
        }
        for r in ranked
    ]
```

#### 3.4.9 `_generate_f_r_scatter()`

```python
def _generate_f_r_scatter(recommendations):
    """f-faktör vs r-faktör scatter plot verisi."""
    return {
        "equipment_names": [r.equipment_name for r in recommendations],
        "f_factors": [round(r.f_factor, 3) for r in recommendations],
        "r_factors": [round(r.r_factor, 3) for r in recommendations],
        "strategies": [r.strategy for r in recommendations],
        "colors": [STRATEGY_COLORS.get(r.strategy, "#9ca3af") for r in recommendations],
        "sizes": [max(8, min(30, r.C_savings_annual_eur / 1000)) for r in recommendations],
        # Karar bölgeleri (frontend'de çizilecek)
        "zones": {
            "invest": {"f_range": [0, 0.25], "r_range": [0.5, 2.0], "label": "Verim artır"},
            "downsize": {"f_range": [0.65, 1.0], "r_range": [0, 0.5], "label": "Maliyet azalt"},
            "structural": {"f_range": [0.65, 1.0], "r_range": [0.5, 2.0], "label": "Sistem değiştir"},
            "parametric": {"f_range": [0.25, 0.65], "r_range": [0, 2.0], "label": "İnce ayar"},
        },
    }
```

#### 3.4.10 `_generate_savings_waterfall()`

```python
def _generate_savings_waterfall(recommendations):
    """Tasarruf waterfall chart verisi (büyükten küçüğe)."""
    # Sadece tasarrufu > 0 olanlar
    actionable = [r for r in recommendations if r.C_savings_annual_eur > 0]
    actionable.sort(key=lambda r: r.C_savings_annual_eur, reverse=True)
    
    names = [r.equipment_name for r in actionable]
    values = [round(r.C_savings_annual_eur, 2) for r in actionable]
    strategies = [r.strategy for r in actionable]
    colors = [STRATEGY_COLORS.get(r.strategy, "#9ca3af") for r in actionable]
    
    # Kümülatif toplam
    cumulative = []
    running = 0
    for v in values:
        running += v
        cumulative.append(round(running, 2))
    
    return {
        "equipment_names": names,
        "savings_eur": values,
        "cumulative_eur": cumulative,
        "strategies": strategies,
        "colors": colors,
        "total_savings_eur": round(sum(values), 2),
    }
```

#### 3.4.11 `check_thermoeconomic_feasibility()`

```python
def check_thermoeconomic_feasibility(equipment_list, analysis_results):
    """
    Termoekonomik optimizasyonun anlamlı olup olmadığını kontrol et.
    
    Gereksinimler:
    - En az 1 ekipmanda exergoekonomik veri var (f_factor mevcut)
    """
    valid = _filter_valid_equipment(equipment_list, analysis_results)
    if len(valid) < 1:
        return False, ["Exergoekonomik verisi olan ekipman yok"]
    return True, []
```

---

## 4. API Entegrasyonu

### 4.1 Factory Engine

`engine/factory.py` → `analyze_factory()` içine, EGM'den sonra:

```python
# 9. Thermoeconomic Optimization (optional, best-effort)
thermoeconomic_optimization = None
try:
    from .thermoeconomic_optimization import analyze_thermoeconomic_optimization, check_thermoeconomic_feasibility
    # ... eq_list_dicts ve results_dict oluştur ...
    feasible, _ = check_thermoeconomic_feasibility(eq_list_dicts, results_dict)
    if feasible:
        thermo_result = analyze_thermoeconomic_optimization(
            eq_list_dicts, results_dict, operating_hours=8000
        )
        if thermo_result.is_valid:
            thermoeconomic_optimization = thermo_result.to_dict()
except Exception:
    pass
```

`FactoryAnalysisResult`'a: `thermoeconomic_optimization: Optional[dict] = None`

### 4.2 Endpoint

```python
@router.post("/factory/projects/{project_id}/thermoeconomic-optimization")
```

### 4.3 AI Prompt

```python
def _format_thermoeconomic_for_prompt(thermo_data: dict) -> str:
    """Max ~400 karakter."""
    if not thermo_data or not thermo_data.get("is_valid"):
        return ""
    
    lines = [
        "\n## Termoekonomik Optimizasyon",
        f"- Fabrika f-faktör: {thermo_data.get('factory_f_factor', 0):.2f}",
        f"- Toplam tasarruf potansiyeli: {thermo_data.get('total_savings_annual_eur', 0):,.0f} EUR/yıl",
        f"- Tahmini yatırım: {thermo_data.get('total_estimated_investment_eur', 0):,.0f} EUR | Geri ödeme: {thermo_data.get('factory_payback_years', 0):.1f} yıl",
    ]
    
    ranking = thermo_data.get("cost_benefit_ranking", [])[:3]
    if ranking:
        lines.append("- Öncelik: " + ", ".join(
            f"{r['equipment_name']}({r['strategy_label'][:10]},{r['simple_payback_years']}y)" for r in ranking
        ))
    
    result = "\n".join(lines)
    return result[:400] if len(result) > 400 else result
```

---

## 5. Frontend Entegrasyonu

### 5.1 Component Yapısı

```
frontend/src/components/thermoeconomic/
├── FRScatterChart.jsx          # f vs r scatter plot (strateji bölgeleri)
├── SavingsWaterfallChart.jsx   # Tasarruf waterfall
├── ThermoMetricBar.jsx         # Özet kartlar
├── OptimizationRankingList.jsx # ROI bazlı sıralama
├── ThermoeconomicTab.jsx       # Ana bileşen
```

### 5.2 Wireframe

```
+----------------------------------------------------------+
| Termoekonomik Optimizasyon                               |
+----------------------------------------------------------+
|                                                          |
| +-- Özet Kartlar --+                                    |
| | Tasarruf: 45,200€/yıl | Yatırım: 125K€ |            |
| | Geri Ödeme: 2.8 yıl   | f: 0.42        |            |
| | Yüksek: 2  | Orta: 3  | Düşük: 1       |            |
| +------------------+                                    |
|                                                          |
| +-- f-r Scatter Plot -----+                             |
| |   r ↑                   |                              |
| | 1.0 |  ● invest    ● struct                           |
| |     |     zone        zone                             |
| | 0.5 |··············●·····                              |
| |     |  param zone  ● downsize                          |
| |   0 +──────────────┼──── f →                           |
| |     0   0.25  0.50 0.65  1.0                           |
| +-------------------------+                              |
|                                                          |
| +-- Tasarruf Waterfall ---+                              |
| | Kazan-1    [████████████████] 18,500€                  |
| | Kompresör  [██████████]       12,300€                  |
| | HX-1       [███████]          8,200€                   |
| | Chiller    [████]             4,100€                   |
| | Toplam ────────── 45,200€/yıl                          |
| +-------------------------+                              |
|                                                          |
| +-- Optimizasyon Sıralaması --+                         |
| | 1. Kompresör | Parametrik | 12.3K€/yıl | 1.2y ★     |
| |    → Basınç oranını optimize edin                      |
| |    → Emme havası sıcaklığını düşürün                   |
| | 2. Kazan-1   | Yatırım    | 18.5K€/yıl | 3.1y       |
| |    → Economizer ekleyin                                |
| |    → Fazla hava oranını optimize edin                  |
| +-----------------------------+                         |
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
  7. ThermoeconomicTab (BRIEF_28 — YENİ)
  8. FactoryAIPanel (mevcut)
```

---

## 6. Testler

### 6.1 `tests/test_thermoeconomic_optimization.py`

Tahmini: **~400 satır, 32+ test**

```python
class TestStrategyDetermination:
    """f/r karar matrisi testleri."""
    
    def test_low_f_high_r_gives_invest(self):
        """f<0.25, r>0.50 → invest."""
    def test_low_f_low_r_gives_parametric(self):
        """f<0.25, r≤0.50 → parametric."""
    def test_high_f_high_r_gives_structural(self):
        """f>0.65, r>0.50 → structural."""
    def test_high_f_low_r_gives_downsize(self):
        """f>0.65, r≤0.50 → downsize."""
    def test_mid_f_high_avoidable_gives_parametric(self):
        """0.25≤f≤0.65, avoidable>0.30 → parametric."""
    def test_mid_f_low_avoidable_gives_maintain(self):
        """0.25≤f≤0.65, avoidable≤0.30 → maintain."""
    def test_boundary_f_025(self):
        """f=0.25 sınır durumu."""
    def test_boundary_f_065(self):
        """f=0.65 sınır durumu."""


class TestEquipmentActions:
    """Ekipman tipine özel aksiyon testleri."""
    
    def test_all_equipment_types_have_actions(self):
        """7 ekipman tipi × 4 strateji → aksiyonlar var."""
    def test_actions_non_empty(self):
        """Tüm aksiyon listeleri boş değil."""
    def test_unknown_type_gets_fallback(self):
        """Bilinmeyen tip → fallback aksiyon."""


class TestInvestmentEstimates:
    """Yatırım maliyet tahmini testleri."""
    
    def test_maintain_zero_investment(self):
        """maintain → 0 yatırım."""
    def test_investment_increases_with_capacity(self):
        """Kapasite arttıkça yatırım artar."""
    def test_structural_more_expensive_than_parametric(self):
        """Yapısal > parametrik yatırım."""
    def test_unknown_type_gets_fallback(self):
        """Bilinmeyen tip → fallback tahmin."""


class TestSavingsCalculation:
    """Tasarruf hesaplama testleri."""
    
    def test_savings_equals_CD_times_avoidable(self):
        """C_savings = C_dot_D × avoidable_ratio."""
    def test_annual_savings_uses_operating_hours(self):
        """Yıllık = saatlik × operating_hours."""
    def test_payback_calculation(self):
        """payback = investment / savings_annual."""
    def test_payback_capped_at_99(self):
        """Sıfır tasarruf → payback = 99.9."""
    def test_zero_avoidable_zero_savings(self):
        """avoidable_ratio = 0 → savings = 0."""


class TestFactoryMetrics:
    """Fabrika metrikleri testleri."""
    
    def test_factory_f_factor(self):
        """factory_f = Σ Z_dot / (Σ Z_dot + Σ C_dot_D)."""
    def test_totals_consistent(self):
        """Toplam C = Σ individual."""
    def test_strategy_distribution_counts(self):
        """Strateji sayıları doğru."""
    def test_priority_distribution_counts(self):
        """Öncelik sayıları doğru."""


class TestCostBenefitRanking:
    """ROI sıralaması testleri."""
    
    def test_sorted_by_payback_ascending(self):
        """En kısa geri ödeme ilk."""
    def test_maintain_excluded(self):
        """maintain stratejisi hariç."""


class TestChartData:
    """Görselleştirme verisi testleri."""
    
    def test_f_r_scatter_structure(self):
        """Scatter data yapısı doğru."""
    def test_waterfall_cumulative_ascending(self):
        """Waterfall kümülatif artan."""
    def test_waterfall_total_matches_sum(self):
        """Waterfall toplamı = tek tek toplam."""


class TestEdgeCases:
    """Uç durumlar."""
    
    def test_no_exergoeconomic_data_invalid(self):
        """Exergoekonomik veri yok → is_valid=False."""
    def test_single_equipment_valid(self):
        """Tek ekipman → is_valid=True."""
    def test_all_maintain_zero_savings(self):
        """Hepsi maintain → toplam savings = 0."""
    def test_serialization(self):
        """to_dict() → JSON sorunsuz."""


class TestIntegration:
    """Entegrasyon testleri."""
    
    def test_factory_includes_thermoeconomic(self):
        """analyze_factory() sonucu thermoeconomic_optimization alanı var."""
```

---

## 7. Uygulama Planı

### Faz 1: Engine

| Adım | Dosya | İş |
|------|-------|----|
| 1.1 | `engine/thermoeconomic_optimization.py` (YENİ) | Veri yapıları |
| 1.2 | aynı | Sabitler: STRATEGY_LABELS, STRATEGY_COLORS, OPTIMIZATION_ACTIONS (7 tip × 4 strateji), INVESTMENT_ESTIMATES |
| 1.3 | aynı | `_filter_valid_equipment()` — f_factor mevcut olanlar |
| 1.4 | aynı | `_determine_strategy()` — f/r karar matrisi |
| 1.5 | aynı | `_get_equipment_actions()`, `_estimate_investment()` |
| 1.6 | aynı | `_generate_recommendation()` — tek ekipman |
| 1.7 | aynı | `_calculate_factory_metrics()` |
| 1.8 | aynı | `_create_cost_benefit_ranking()` |
| 1.9 | aynı | `_generate_f_r_scatter()`, `_generate_savings_waterfall()` |
| 1.10 | aynı | `_collect_warnings()`, `check_thermoeconomic_feasibility()` |
| 1.11 | aynı | `analyze_thermoeconomic_optimization()` ana fonksiyon |
| 1.12 | `engine/__init__.py` | Export ekle |

### Faz 2: Testler

| Adım | Dosya | İş |
|------|-------|----|
| 2.1 | `tests/test_thermoeconomic_optimization.py` (YENİ) | Fixture'lar |
| 2.2-2.9 | aynı | 8 test sınıfı, 32+ test |
| 2.10 | Tüm | `pytest tests/ -v` regresyon |

### Faz 3: API + Fabrika

| Adım | Dosya | İş |
|------|-------|----|
| 3.1 | `engine/factory.py` | Alan + çağrı |
| 3.2 | `api/schemas/factory.py` | Alan |
| 3.3 | `api/routes/factory.py` | Response + endpoint |
| 3.4 | `api/services/claude_code_service.py` | Prompt formatter |

### Faz 4: Frontend

| Adım | Dosya | İş |
|------|-------|----|
| 4.1 | `components/thermoeconomic/` | Dizin |
| 4.2 | `FRScatterChart.jsx` | Plotly scatter (strateji bölgeleri) |
| 4.3 | `SavingsWaterfallChart.jsx` | Plotly bar (kümülatif çizgi) |
| 4.4 | `ThermoMetricBar.jsx` | Özet kartlar |
| 4.5 | `OptimizationRankingList.jsx` | ROI sıralaması + aksiyonlar |
| 4.6 | `ThermoeconomicTab.jsx` | Ana bileşen |
| 4.7 | `FactoryDashboard.jsx` | Entegrasyon |
| 4.8 | `factoryApi.js` | API call |

---

## 8. Doğrulama

### Invariantlar
- [ ] C_total_dot = Z_dot + C_dot_D (her ekipman)
- [ ] C_savings = C_dot_D × avoidable_ratio
- [ ] payback = investment / savings (savings > 0 ise)
- [ ] 0 ≤ f_factor ≤ 1
- [ ] Σ strategy_distribution = num_equipment
- [ ] Waterfall cumulative[-1] = total_savings

### Testler
- [ ] `pytest tests/test_thermoeconomic_optimization.py -v` geçiyor
- [ ] `pytest tests/ -v` regresyon yok

---

## 9. Claude Code Prompt

```
PROJECT_ANALYSIS.md ve BRIEF_28_THERMOECONOMIC_OPTIMIZATION.md dosyalarını oku.

Görev: ExergyLab'a termoekonomik optimizasyon motor modülünü ekle. Bu modül mevcut SPECO (exergoekonomik) sonuçlarını kullanarak her ekipman için optimizasyon stratejisi belirler.

Faz 1 — Engine modülü:
1. engine/thermoeconomic_optimization.py dosyasını oluştur (~550-650 satır).
2. Veri yapıları: OptimizationRecommendation ve ThermoeconomicOptimizationResult (to_dict). Brief 3.2.
3. Sabitler: STRATEGY_LABELS, STRATEGY_COLORS (5 strateji), OPTIMIZATION_ACTIONS (7 ekipman tipi × 4+1 strateji, her biri 2-3 Türkçe aksiyon), INVESTMENT_ESTIMATES (7 ekipman tipi × 4 strateji, lambda fonksiyonları). Brief 2.3, 2.5, 3.3.
4. _filter_valid_equipment(): exergoeconomic_f_factor mevcut ve ≥ 0 olanları filtrele.
5. _determine_strategy(f, r, avoidable_ratio): Brief 2.2 karar matrisi. f<0.25 → r>0.50? invest : parametric. f>0.65 → r>0.50? structural : downsize. Else → avoidable>0.30? parametric : maintain.
6. _get_equipment_actions(eq_type, strategy): OPTIMIZATION_ACTIONS lookup + fallback.
7. _estimate_investment(eq_type, strategy, capacity_kW): INVESTMENT_ESTIMATES lambda + fallback. maintain → 0.
8. _generate_recommendation(item, result, operating_hours): SPECO verileri, strateji, aksiyonlar, tasarruf, yatırım, payback. Brief 3.4.3.
9. _calculate_factory_metrics(): toplamlar, f_factory, dağılımlar. Brief 3.4.7.
10. _create_cost_benefit_ranking(): payback ascending, maintain hariç. Brief 3.4.8.
11. _generate_f_r_scatter(): scatter data + zone tanımları. Brief 3.4.9.
12. _generate_savings_waterfall(): büyükten küçüğe, kümülatif. Brief 3.4.10.
13. _collect_warnings(), check_thermoeconomic_feasibility().
14. analyze_thermoeconomic_optimization(equipment_list, analysis_results, operating_hours=8000): ana fonksiyon.
15. engine/__init__.py güncelle.

Faz 2 — Testler:
16. tests/test_thermoeconomic_optimization.py (~400 satır, 32+ test).
17. Fixture: 4-5 ekipman, farklı f/r değerleri ve avoidable_ratio.
18. Strateji testleri (8 test): tüm karar matrisi dalları + sınır değerleri (f=0.25, f=0.65).
19. Aksiyon testleri (3 test): 7 tip × 4 strateji hepsinde aksiyon var, fallback çalışıyor.
20. Yatırım testleri (4 test): maintain=0, kapasite arttıkça artar, structural>parametric, fallback.
21. Tasarruf testleri (5 test): C_savings=CD×avoidable, yıllık hesap, payback, cap 99.9, zero.
22. Fabrika testleri (4 test): f_factory, toplamlar, strateji dağılımı, öncelik dağılımı.
23. Sıralama + chart testleri (4 test): payback ascending, maintain hariç, waterfall cumulative, scatter yapısı.
24. Edge case + entegrasyon (4 test): no exergoeconomic→invalid, single valid, serialization, factory integration.
25. pytest tests/test_thermoeconomic_optimization.py -v
26. pytest tests/ -v (regresyon)

Faz 3 — API + Fabrika:
27. engine/factory.py → thermoeconomic_optimization: Optional[dict] = None + best-effort çağrı.
28. api/schemas/factory.py → alan ekle.
29. api/routes/factory.py → response + POST /thermoeconomic-optimization endpoint.
30. api/services/claude_code_service.py → _format_thermoeconomic_for_prompt() (max 400 char) + prompt'a ekle.

Faz 4 — Frontend:
31. frontend/src/components/thermoeconomic/ dizini oluştur.
32. FRScatterChart.jsx — Plotly scatter, karar bölgeleri (dikdörtgen shapes), strateji renkleri.
33. SavingsWaterfallChart.jsx — Plotly bar (strateji renkleri) + kümülatif çizgi.
34. ThermoMetricBar.jsx — Toplam tasarruf, yatırım, geri ödeme, f_factory, strateji dağılımı kartları.
35. OptimizationRankingList.jsx — ROI sıralı, strateji badge, aksiyonlar listesi.
36. ThermoeconomicTab.jsx — Ana bileşen.
37. FactoryDashboard.jsx → ThermoeconomicTab entegrasyonu (EntropyGenerationTab'dan sonra).
38. factoryApi.js → runThermoeconomicOptimization() ekle.

Önemli kurallar:
- SPECO verileri yoksa (f_factor None) → ekipmanı hariç tut.
- Strateji karar matrisi Brief 2.2'yi birebir uygula.
- OPTIMIZATION_ACTIONS Türkçe olacak.
- payback üst sınır 99.9 yıl.
- maintain stratejisi → savings = 0, investment = 0.
- Mevcut alanlar: exergoeconomic_f_factor, exergoeconomic_r_factor, exergoeconomic_Z_dot_eur_h, exergoeconomic_C_dot_destruction_eur_h, avoidable_ratio_pct, exergy_in_kW.
```

---

*BRIEF_28 — Thermoeconomic Optimization Motor Modülü*
*Tarih: 2026-02-06*
*Bağımlılık: Exergoekonomik (BRIEF_23), AV/UN (core.py)*
