# ExergyLab Factory Analysis - Engine, API, Frontend Brief

> **Claude Code için:** Bu brief factory analiz sisteminin tamamını kapsar: knowledge navigation, engine, API, frontend ve AI entegrasyonu.

---

## 🎯 Genel Amaç

Fabrika seviyesi exergy analizi:
1. Çoklu ekipman yönetimi (envanter)
2. Her ekipmanın ayrı analizi
3. Fabrika geneli aggregation
4. Ekipmanlar arası optimizasyon fırsatları
5. Fabrika Sankey diyagramı
6. AI fabrika yorumu

---

## 📚 BÖLÜM 1: Knowledge Base Navigation (ÖNCELİKLİ)

### 1.1 Sorun

119 MD dosyası var. AI hangi dosyalara bakacağını bilmeli.

### 1.2 Çözüm: Index Dosyaları

**Ana Index:** `/knowledge/INDEX.md`

```markdown
# ExergyLab Knowledge Base Index

> Bu dosya tüm knowledge base'in haritasıdır. AI yorumlama yaparken bu dosyayı referans alır.

## Yapı Özeti

| Klasör | Dosya Sayısı | Kapsam |
|--------|--------------|--------|
| compressor/ | 18 | Basınçlı hava sistemleri |
| boiler/ | 22 | Buhar ve sıcak su kazanları |
| chiller/ | 24 | Soğutma sistemleri |
| pump/ | 22 | Pompalama sistemleri |
| factory/ | 33 | Fabrika seviyesi analiz |

## Ekipman Analizi İçin

Her ekipman klasöründe:
- `equipment/*.md` - Ekipman tipleri ve özellikleri
- `solutions/*.md` - İyileştirme çözümleri
- `benchmarks.md` - Karşılaştırma değerleri
- `formulas.md` - Hesaplama formülleri
- `audit.md` - Ölçüm ve doğrulama metodolojisi

### Kompresör Yorumlarken
1. `compressor/benchmarks.md` → Verimlilik karşılaştırması
2. `compressor/formulas.md` → Exergy hesaplama doğrulaması
3. `compressor/solutions/` → Öneri seçenekleri
4. `compressor/equipment/{subtype}.md` → Tipe özel bilgi

### Kazan Yorumlarken
1. `boiler/benchmarks.md` → Verimlilik karşılaştırması
2. `boiler/formulas.md` → Yanma ve exergy hesaplama
3. `boiler/solutions/` → Ekonomizer, O2 trim, vb.
4. `boiler/equipment/{subtype}.md` → Kazan tipine özel

### Chiller Yorumlarken
1. `chiller/benchmarks.md` → COP, IPLV karşılaştırması
2. `chiller/formulas.md` → Soğutma exergy hesaplama
3. `chiller/solutions/` → VSD, free cooling, vb.
4. `chiller/equipment/{subtype}.md` → Chiller tipine özel

### Pompa Yorumlarken
1. `pump/benchmarks.md` → Verimlilik karşılaştırması
2. `pump/formulas.md` → Hidrolik güç, exergy
3. `pump/solutions/` → VSD, impeller trim, vb.
4. `pump/equipment/{subtype}.md` → Pompa tipine özel

## Fabrika Analizi İçin

### Metodoloji ve Temel
- `factory/methodology.md` - Audit yaklaşımı
- `factory/energy_management.md` - ISO 50001
- `factory/exergy_fundamentals.md` - Fabrika exergy dengesi
- `factory/system_boundaries.md` - Sistem sınırları

### Analiz Teknikleri
- `factory/energy_flow_analysis.md` - Enerji akış (Sankey)
- `factory/exergy_flow_analysis.md` - Exergy akış
- `factory/pinch_analysis.md` - Isı entegrasyonu
- `factory/utility_analysis.md` - Utilities analizi

### Entegrasyon ve Optimizasyon
- `factory/cross_equipment.md` - **Ekipmanlar arası fırsatlar (ÖNEMLİ)**
- `factory/heat_integration.md` - Isı entegrasyonu
- `factory/waste_heat_recovery.md` - Atık ısı teknolojileri
- `factory/cogeneration.md` - Kojenerasyon

### Ekonomik Analiz
- `factory/economic_analysis.md` - NPV, IRR, ROI
- `factory/prioritization.md` - **Proje önceliklendirme (ÖNEMLİ)**
- `factory/life_cycle_cost.md` - LCC analizi

### Sektörel Bilgi
- `factory/sector_textile.md` - Tekstil
- `factory/sector_food.md` - Gıda
- `factory/sector_chemical.md` - Kimya
- `factory/sector_metal.md` - Metal
- `factory/sector_cement.md` - Çimento
- `factory/sector_paper.md` - Kağıt
- `factory/sector_automotive.md` - Otomotiv

### Benchmark
- `factory/factory_benchmarks.md` - **Sektörel SEC değerleri (ÖNEMLİ)**
- `factory/kpi_definitions.md` - EnPI tanımları
- `factory/performance_indicators.md` - Performans göstergeleri

### Vaka Çalışmaları
- `factory/case_studies.md` - Gerçek örnekler

## Navigasyon Kuralları

### Tek Ekipman Yorumu
```
1. knowledge/{equipment_type}/benchmarks.md
2. knowledge/{equipment_type}/formulas.md
3. knowledge/{equipment_type}/solutions/*.md (ilgili olanlar)
4. knowledge/{equipment_type}/equipment/{subtype}.md
```

### Fabrika Yorumu
```
1. knowledge/factory/cross_equipment.md (MUTLAKA)
2. knowledge/factory/prioritization.md (MUTLAKA)
3. knowledge/factory/factory_benchmarks.md
4. knowledge/factory/sector_{sector}.md (sektör biliniyorsa)
5. Her ekipman için ilgili benchmark dosyası
```
```

### 1.3 SKILL Dosyası Güncelleme

`/skills/SKILL_exergy_interpreter.md` dosyasına ekle:

```markdown
## Knowledge Base Navigasyonu

### Dosya Yapısı
Knowledge base 5 ana klasörden oluşur:
- `knowledge/compressor/` - Basınçlı hava sistemleri
- `knowledge/boiler/` - Kazan sistemleri
- `knowledge/chiller/` - Soğutma sistemleri
- `knowledge/pump/` - Pompa sistemleri
- `knowledge/factory/` - Fabrika seviyesi analiz

### Tek Ekipman Yorumlarken

**MUTLAKA OKU:**
1. `knowledge/{equipment_type}/benchmarks.md` - Verimlilik karşılaştırması için
2. `knowledge/{equipment_type}/formulas.md` - Hesaplama doğrulaması için

**GEREKTİĞİNDE OKU:**
3. `knowledge/{equipment_type}/solutions/{solution}.md` - Öneri detayları için
4. `knowledge/{equipment_type}/equipment/{subtype}.md` - Tipe özel bilgi için

### Fabrika Yorumlarken

**MUTLAKA OKU:**
1. `knowledge/factory/cross_equipment.md` - Ekipmanlar arası optimizasyon fırsatları
2. `knowledge/factory/prioritization.md` - Proje önceliklendirme
3. `knowledge/factory/factory_benchmarks.md` - Sektörel karşılaştırma

**SEKTÖR BİLİNİYORSA OKU:**
4. `knowledge/factory/sector_{sector}.md` - Sektöre özel enerji profili ve fırsatlar

**EKONOMİK ANALİZ İÇİN OKU:**
5. `knowledge/factory/economic_analysis.md` - NPV, IRR, ROI metodları

**ENTEGRASYON ÖNERİLERİ İÇİN OKU:**
6. `knowledge/factory/heat_integration.md` - Isı entegrasyonu
7. `knowledge/factory/waste_heat_recovery.md` - Atık ısı teknolojileri
8. `knowledge/factory/cogeneration.md` - Kojenerasyon (büyük tesisler için)

### Yorumlama Öncelikleri

**Fabrika Analizi Yorumunda Şunları İçer:**
1. Toplam fabrika exergy verimi değerlendirmesi
2. Hotspot analizi (en çok kayıp nerede)
3. Ekipmanlar arası entegrasyon fırsatları (cross_equipment.md'den)
4. Önceliklendirilmiş aksiyon planı (prioritization.md metoduyla)
5. Sektörel benchmark karşılaştırması
6. Quick wins ve stratejik projeler ayrımı
```

---

## 🔧 BÖLÜM 2: Factory Engine

### 2.1 Dosya: `/engine/factory.py`

```python
"""
Fabrika seviyesi exergy analizi motoru.

Bu modül:
1. Çoklu ekipman analizini koordine eder
2. Fabrika geneli aggregation yapar
3. Hotspot analizi yapar
4. Cross-equipment fırsatları tespit eder
5. Fabrika Sankey verisi üretir
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

# Mevcut engine'leri import et
from engine.compressor import analyze_compressor
from engine.boiler import analyze_boiler
from engine.chiller import analyze_chiller
from engine.pump import analyze_pump


class EquipmentType(str, Enum):
    COMPRESSOR = "compressor"
    BOILER = "boiler"
    CHILLER = "chiller"
    PUMP = "pump"


@dataclass
class EquipmentItem:
    """Fabrikadaki tek bir ekipman"""
    id: str
    name: str
    equipment_type: EquipmentType
    subtype: str
    parameters: Dict[str, Any]
    analysis_result: Optional[Dict] = None


@dataclass
class FactoryAnalysisResult:
    """Fabrika analiz sonucu"""
    # Aggregated metrics
    total_energy_input_kW: float
    total_exergy_input_kW: float
    total_useful_exergy_kW: float
    total_exergy_destroyed_kW: float
    factory_exergy_efficiency: float
    
    # Financials
    total_annual_energy_cost_eur: float
    total_annual_exergy_loss_cost_eur: float
    total_potential_savings_eur: float
    
    # Equipment results
    equipment_results: List[Dict]
    
    # Hotspots (sorted by loss)
    hotspots: List[Dict]
    
    # Cross-equipment opportunities
    integration_opportunities: List[Dict]
    
    # Sankey data
    sankey_data: Dict


def analyze_equipment_item(item: EquipmentItem) -> Dict:
    """Tek bir ekipmanı analiz et"""
    if item.equipment_type == EquipmentType.COMPRESSOR:
        return analyze_compressor(item.subtype, item.parameters)
    elif item.equipment_type == EquipmentType.BOILER:
        return analyze_boiler(item.subtype, item.parameters)
    elif item.equipment_type == EquipmentType.CHILLER:
        return analyze_chiller(item.subtype, item.parameters)
    elif item.equipment_type == EquipmentType.PUMP:
        return analyze_pump(item.subtype, item.parameters)
    else:
        raise ValueError(f"Unknown equipment type: {item.equipment_type}")


def analyze_factory(
    factory_name: str,
    sector: Optional[str],
    equipment_list: List[EquipmentItem]
) -> FactoryAnalysisResult:
    """
    Fabrika seviyesi analiz.
    
    Args:
        factory_name: Fabrika adı
        sector: Sektör (textile, food, chemical, metal, cement, paper, automotive)
        equipment_list: Ekipman listesi
    
    Returns:
        FactoryAnalysisResult
    """
    # 1. Her ekipmanı analiz et
    equipment_results = []
    for item in equipment_list:
        try:
            result = analyze_equipment_item(item)
            item.analysis_result = result
            equipment_results.append({
                "id": item.id,
                "name": item.name,
                "type": item.equipment_type.value,
                "subtype": item.subtype,
                "result": result
            })
        except Exception as e:
            equipment_results.append({
                "id": item.id,
                "name": item.name,
                "type": item.equipment_type.value,
                "subtype": item.subtype,
                "error": str(e)
            })
    
    # 2. Aggregation
    aggregates = _calculate_aggregates(equipment_results)
    
    # 3. Hotspot analizi
    hotspots = _identify_hotspots(equipment_results)
    
    # 4. Cross-equipment fırsatları
    opportunities = _detect_integration_opportunities(equipment_list, equipment_results)
    
    # 5. Fabrika Sankey
    sankey = _generate_factory_sankey(equipment_results, aggregates)
    
    return FactoryAnalysisResult(
        total_energy_input_kW=aggregates["total_energy_input_kW"],
        total_exergy_input_kW=aggregates["total_exergy_input_kW"],
        total_useful_exergy_kW=aggregates["total_useful_exergy_kW"],
        total_exergy_destroyed_kW=aggregates["total_exergy_destroyed_kW"],
        factory_exergy_efficiency=aggregates["factory_exergy_efficiency"],
        total_annual_energy_cost_eur=aggregates["total_annual_energy_cost_eur"],
        total_annual_exergy_loss_cost_eur=aggregates["total_annual_exergy_loss_cost_eur"],
        total_potential_savings_eur=aggregates["total_potential_savings_eur"],
        equipment_results=equipment_results,
        hotspots=hotspots,
        integration_opportunities=opportunities,
        sankey_data=sankey
    )


def _calculate_aggregates(equipment_results: List[Dict]) -> Dict:
    """Fabrika geneli toplamları hesapla"""
    total_energy_input = 0
    total_exergy_input = 0
    total_useful_exergy = 0
    total_exergy_destroyed = 0
    total_annual_cost = 0
    total_potential_savings = 0
    
    for eq in equipment_results:
        if "error" in eq:
            continue
        
        result = eq.get("result", {})
        metrics = result.get("metrics", {})
        
        # Exergy metrikleri
        exergy_input = metrics.get("exergy_input_kW", 0) or metrics.get("power_input_kW", 0) or 0
        exergy_output = metrics.get("exergy_output_kW", 0) or metrics.get("useful_exergy_kW", 0) or 0
        exergy_destroyed = metrics.get("exergy_destroyed_kW", 0) or (exergy_input - exergy_output)
        
        total_exergy_input += exergy_input
        total_useful_exergy += exergy_output
        total_exergy_destroyed += exergy_destroyed
        
        # Enerji girişi (yakıt dahil)
        energy_input = metrics.get("energy_input_kW", 0) or exergy_input
        total_energy_input += energy_input
        
        # Finansal
        annual_cost = metrics.get("annual_cost_eur", 0) or metrics.get("annual_energy_cost_eur", 0) or 0
        total_annual_cost += annual_cost
        
        # Potansiyel tasarruf (önerilerden)
        recommendations = result.get("recommendations", [])
        for rec in recommendations:
            savings = rec.get("annual_savings_eur", 0) or 0
            total_potential_savings += savings
    
    # Fabrika exergy verimi
    factory_efficiency = 0
    if total_exergy_input > 0:
        factory_efficiency = (total_useful_exergy / total_exergy_input) * 100
    
    # Exergy kaybının mali değeri (yaklaşık)
    exergy_loss_cost = 0
    if total_exergy_input > 0 and total_annual_cost > 0:
        exergy_loss_cost = total_annual_cost * (total_exergy_destroyed / total_exergy_input)
    
    return {
        "total_energy_input_kW": round(total_energy_input, 2),
        "total_exergy_input_kW": round(total_exergy_input, 2),
        "total_useful_exergy_kW": round(total_useful_exergy, 2),
        "total_exergy_destroyed_kW": round(total_exergy_destroyed, 2),
        "factory_exergy_efficiency": round(factory_efficiency, 1),
        "total_annual_energy_cost_eur": round(total_annual_cost, 0),
        "total_annual_exergy_loss_cost_eur": round(exergy_loss_cost, 0),
        "total_potential_savings_eur": round(total_potential_savings, 0)
    }


def _identify_hotspots(equipment_results: List[Dict]) -> List[Dict]:
    """Exergy kayıp sıralaması"""
    hotspots = []
    
    for eq in equipment_results:
        if "error" in eq:
            continue
        
        result = eq.get("result", {})
        metrics = result.get("metrics", {})
        
        exergy_input = metrics.get("exergy_input_kW", 0) or metrics.get("power_input_kW", 0) or 0
        exergy_output = metrics.get("exergy_output_kW", 0) or metrics.get("useful_exergy_kW", 0) or 0
        exergy_destroyed = metrics.get("exergy_destroyed_kW", 0) or (exergy_input - exergy_output)
        exergy_efficiency = metrics.get("exergy_efficiency", 0) or 0
        annual_cost = metrics.get("annual_cost_eur", 0) or metrics.get("annual_energy_cost_eur", 0) or 0
        
        # Kayıp maliyeti tahmini
        loss_cost = 0
        if exergy_input > 0:
            loss_cost = annual_cost * (exergy_destroyed / exergy_input)
        
        hotspots.append({
            "equipment_id": eq["id"],
            "equipment_name": eq["name"],
            "equipment_type": eq["type"],
            "exergy_destroyed_kW": round(exergy_destroyed, 2),
            "exergy_efficiency": round(exergy_efficiency, 1),
            "estimated_annual_loss_eur": round(loss_cost, 0),
            "priority": _get_priority(exergy_efficiency, exergy_destroyed)
        })
    
    # Kayıp büyüklüğüne göre sırala (büyükten küçüğe)
    hotspots.sort(key=lambda x: x["exergy_destroyed_kW"], reverse=True)
    
    return hotspots


def _get_priority(efficiency: float, loss_kW: float) -> str:
    """Öncelik belirleme"""
    if efficiency < 30 or loss_kW > 50:
        return "high"
    elif efficiency < 50 or loss_kW > 20:
        return "medium"
    else:
        return "low"


def _detect_integration_opportunities(
    equipment_list: List[EquipmentItem],
    equipment_results: List[Dict]
) -> List[Dict]:
    """
    Ekipmanlar arası entegrasyon fırsatlarını tespit et.
    
    Bu fonksiyon knowledge/factory/cross_equipment.md içeriğine dayanır.
    """
    opportunities = []
    
    # Ekipman tiplerini grupla
    equipment_by_type = {}
    for item in equipment_list:
        eq_type = item.equipment_type.value
        if eq_type not in equipment_by_type:
            equipment_by_type[eq_type] = []
        equipment_by_type[eq_type].append(item)
    
    has_compressor = "compressor" in equipment_by_type
    has_boiler = "boiler" in equipment_by_type
    has_chiller = "chiller" in equipment_by_type
    has_pump = "pump" in equipment_by_type
    
    # Fırsat 1: Kompresör atık ısısı → Kazan besleme suyu
    if has_compressor and has_boiler:
        # Kompresör kapasitelerini topla
        total_compressor_kW = 0
        for item in equipment_by_type["compressor"]:
            if item.analysis_result:
                metrics = item.analysis_result.get("metrics", {})
                total_compressor_kW += metrics.get("power_input_kW", 0) or metrics.get("exergy_input_kW", 0) or 0
        
        # Geri kazanılabilir ısı (kompresör gücünün ~60-70%'i ısıya dönüşür)
        recoverable_heat_kW = total_compressor_kW * 0.65
        
        # Tahmini tasarruf (yakıt tasarrufu olarak)
        # Besleme suyu 15°C → 45°C ısıtılırsa, kazan yakıt tasarrufu ~2-4%
        estimated_savings = recoverable_heat_kW * 6000 * 0.05  # €0.05/kWh termal değer
        
        opportunities.append({
            "id": "comp_to_boiler_heat_recovery",
            "title": "Kompresör Atık Isısı → Kazan Besleme Suyu",
            "description": f"Kompresörlerden {recoverable_heat_kW:.0f} kW atık ısı geri kazanılarak kazan besleme suyu ön ısıtılabilir. Bu, kazan yakıt tüketimini %2-4 azaltabilir.",
            "source_equipment": "compressor",
            "target_equipment": "boiler",
            "potential_recovery_kW": round(recoverable_heat_kW, 1),
            "estimated_savings_eur": round(estimated_savings, 0),
            "estimated_investment_eur": round(recoverable_heat_kW * 200, 0),  # ~€200/kW için heat recovery unit
            "estimated_roi_years": round((recoverable_heat_kW * 200) / estimated_savings, 1) if estimated_savings > 0 else 0,
            "complexity": "medium",
            "reference": "knowledge/factory/cross_equipment.md"
        })
    
    # Fırsat 2: Kompresör atık ısısı → Bina/proses ısıtma
    if has_compressor:
        total_compressor_kW = 0
        for item in equipment_by_type["compressor"]:
            if item.analysis_result:
                metrics = item.analysis_result.get("metrics", {})
                total_compressor_kW += metrics.get("power_input_kW", 0) or metrics.get("exergy_input_kW", 0) or 0
        
        recoverable_heat_kW = total_compressor_kW * 0.65
        
        # Eğer kazan yoksa bu ısı bina ısıtma için kullanılabilir
        if not has_boiler and recoverable_heat_kW > 10:
            estimated_savings = recoverable_heat_kW * 3000 * 0.08  # Kış ayları, €0.08/kWh
            
            opportunities.append({
                "id": "comp_to_space_heating",
                "title": "Kompresör Atık Isısı → Bina Isıtma",
                "description": f"Kompresörlerden {recoverable_heat_kW:.0f} kW atık ısı kış aylarında bina ısıtması için kullanılabilir.",
                "source_equipment": "compressor",
                "target_equipment": "HVAC",
                "potential_recovery_kW": round(recoverable_heat_kW, 1),
                "estimated_savings_eur": round(estimated_savings, 0),
                "estimated_investment_eur": round(recoverable_heat_kW * 150, 0),
                "estimated_roi_years": round((recoverable_heat_kW * 150) / estimated_savings, 1) if estimated_savings > 0 else 0,
                "complexity": "low",
                "reference": "knowledge/factory/cross_equipment.md"
            })
    
    # Fırsat 3: Kazan atık ısısı → Absorption chiller
    if has_boiler and has_chiller:
        # Kazan baca gazı ısısı ile absorption chiller çalıştırma
        total_boiler_kW = 0
        for item in equipment_by_type["boiler"]:
            if item.analysis_result:
                metrics = item.analysis_result.get("metrics", {})
                total_boiler_kW += metrics.get("fuel_input_kW", 0) or metrics.get("exergy_input_kW", 0) or 0
        
        # Baca gazı kaybı ~%15-20
        flue_gas_heat_kW = total_boiler_kW * 0.15
        
        # Absorption chiller COP ~0.7
        cooling_capacity_kW = flue_gas_heat_kW * 0.7
        
        if cooling_capacity_kW > 50:  # Minimum ekonomik boyut
            # Elektrikli chiller yerine tasarruf
            estimated_savings = cooling_capacity_kW * 4000 * 0.12 / 4  # COP 4 varsayımı, €0.12/kWh
            
            opportunities.append({
                "id": "boiler_to_absorption_chiller",
                "title": "Kazan Atık Isısı → Absorption Chiller",
                "description": f"Kazan baca gazından {flue_gas_heat_kW:.0f} kW ısı ile {cooling_capacity_kW:.0f} kW soğutma kapasiteli absorption chiller çalıştırılabilir.",
                "source_equipment": "boiler",
                "target_equipment": "chiller",
                "potential_recovery_kW": round(flue_gas_heat_kW, 1),
                "cooling_capacity_kW": round(cooling_capacity_kW, 1),
                "estimated_savings_eur": round(estimated_savings, 0),
                "estimated_investment_eur": round(cooling_capacity_kW * 400, 0),  # Absorption chiller ~€400/kW
                "estimated_roi_years": round((cooling_capacity_kW * 400) / estimated_savings, 1) if estimated_savings > 0 else 0,
                "complexity": "high",
                "reference": "knowledge/factory/cross_equipment.md"
            })
    
    # Fırsat 4: Chiller kondenser ısısı → Sıcak su
    if has_chiller:
        total_chiller_kW = 0
        for item in equipment_by_type["chiller"]:
            if item.analysis_result:
                metrics = item.analysis_result.get("metrics", {})
                total_chiller_kW += metrics.get("cooling_capacity_kW", 0) or 0
        
        # Kondenser ısısı = soğutma + kompresör gücü
        condenser_heat_kW = total_chiller_kW * 1.25  # COP ~4 varsayımı
        
        if condenser_heat_kW > 20:
            # Desuperheater ile sıcak su üretimi
            recoverable_kW = condenser_heat_kW * 0.15  # Desuperheater ~%15 geri kazanır
            estimated_savings = recoverable_kW * 6000 * 0.06
            
            opportunities.append({
                "id": "chiller_heat_recovery",
                "title": "Chiller Kondenser Isısı → Sıcak Su",
                "description": f"Chiller kondenserinden {recoverable_kW:.0f} kW ısı desuperheater ile geri kazanılarak sıcak su üretilebilir.",
                "source_equipment": "chiller",
                "target_equipment": "hot_water",
                "potential_recovery_kW": round(recoverable_kW, 1),
                "estimated_savings_eur": round(estimated_savings, 0),
                "estimated_investment_eur": round(recoverable_kW * 250, 0),
                "estimated_roi_years": round((recoverable_kW * 250) / estimated_savings, 1) if estimated_savings > 0 else 0,
                "complexity": "medium",
                "reference": "knowledge/factory/cross_equipment.md"
            })
    
    # Fırsat 5: Pompa VSD retrofit (throttle kontrolü varsa)
    if has_pump:
        for item in equipment_by_type["pump"]:
            if item.analysis_result:
                metrics = item.analysis_result.get("metrics", {})
                control_method = item.parameters.get("control_method", "none")
                has_vsd = item.parameters.get("has_vsd", False)
                
                if control_method == "throttle" and not has_vsd:
                    power_kW = metrics.get("motor_power_kW", 0) or metrics.get("power_input_kW", 0) or 0
                    
                    if power_kW > 5:
                        # Throttle → VSD tasarruf potansiyeli %30-50
                        estimated_savings = power_kW * 6000 * 0.12 * 0.35
                        
                        opportunities.append({
                            "id": f"pump_vsd_{item.id}",
                            "title": f"Pompa VSD Retrofit: {item.name}",
                            "description": f"{item.name} pompası throttle kontrolünden VSD'ye geçirilerek %30-50 enerji tasarrufu sağlanabilir.",
                            "source_equipment": "pump",
                            "target_equipment": None,
                            "power_kW": round(power_kW, 1),
                            "estimated_savings_eur": round(estimated_savings, 0),
                            "estimated_investment_eur": round(power_kW * 300, 0),  # VSD ~€300/kW
                            "estimated_roi_years": round((power_kW * 300) / estimated_savings, 1) if estimated_savings > 0 else 0,
                            "complexity": "low",
                            "reference": "knowledge/pump/solutions/vsd.md"
                        })
    
    # Tasarruf büyüklüğüne göre sırala
    opportunities.sort(key=lambda x: x.get("estimated_savings_eur", 0), reverse=True)
    
    return opportunities


def _generate_factory_sankey(equipment_results: List[Dict], aggregates: Dict) -> Dict:
    """
    Fabrika geneli Sankey diyagramı verisi üret.
    
    Yapı:
    Enerji Girişi → [Her Ekipman] → Faydalı Çıktı
                                 → Kayıplar
    """
    nodes = [
        {"name": "Enerji Girişi", "color": "#3B82F6"},  # Mavi
    ]
    links = []
    
    node_index = 1  # 0 = Enerji Girişi
    
    total_useful = 0
    total_loss = 0
    
    for eq in equipment_results:
        if "error" in eq:
            continue
        
        result = eq.get("result", {})
        metrics = result.get("metrics", {})
        
        eq_name = eq.get("name", eq.get("id"))
        eq_type = eq.get("type")
        
        # Ekipman rengi
        color_map = {
            "compressor": "#60A5FA",  # Açık mavi
            "boiler": "#F87171",      # Kırmızı
            "chiller": "#34D399",     # Yeşil
            "pump": "#A78BFA"         # Mor
        }
        eq_color = color_map.get(eq_type, "#9CA3AF")
        
        # Exergy değerleri
        exergy_input = metrics.get("exergy_input_kW", 0) or metrics.get("power_input_kW", 0) or 0
        exergy_output = metrics.get("exergy_output_kW", 0) or metrics.get("useful_exergy_kW", 0) or 0
        exergy_destroyed = exergy_input - exergy_output
        
        if exergy_input <= 0:
            continue
        
        # Ekipman node'u
        nodes.append({"name": eq_name, "color": eq_color})
        eq_node_idx = node_index
        node_index += 1
        
        # Giriş → Ekipman
        links.append({
            "source": 0,  # Enerji Girişi
            "target": eq_node_idx,
            "value": round(exergy_input, 2)
        })
        
        total_useful += exergy_output
        total_loss += exergy_destroyed
    
    # Çıktı node'ları
    nodes.append({"name": "Faydalı Exergy", "color": "#10B981"})  # Yeşil
    useful_node_idx = node_index
    node_index += 1
    
    nodes.append({"name": "Exergy Kaybı", "color": "#EF4444"})  # Kırmızı
    loss_node_idx = node_index
    
    # Her ekipmandan çıkışlar
    eq_idx = 1
    for eq in equipment_results:
        if "error" in eq:
            continue
        
        result = eq.get("result", {})
        metrics = result.get("metrics", {})
        
        exergy_input = metrics.get("exergy_input_kW", 0) or metrics.get("power_input_kW", 0) or 0
        exergy_output = metrics.get("exergy_output_kW", 0) or metrics.get("useful_exergy_kW", 0) or 0
        exergy_destroyed = exergy_input - exergy_output
        
        if exergy_input <= 0:
            continue
        
        # Ekipman → Faydalı
        if exergy_output > 0:
            links.append({
                "source": eq_idx,
                "target": useful_node_idx,
                "value": round(exergy_output, 2)
            })
        
        # Ekipman → Kayıp
        if exergy_destroyed > 0:
            links.append({
                "source": eq_idx,
                "target": loss_node_idx,
                "value": round(exergy_destroyed, 2)
            })
        
        eq_idx += 1
    
    return {
        "nodes": nodes,
        "links": links,
        "summary": {
            "total_input_kW": aggregates["total_exergy_input_kW"],
            "total_useful_kW": round(total_useful, 2),
            "total_loss_kW": round(total_loss, 2),
            "efficiency_percent": aggregates["factory_exergy_efficiency"]
        }
    }


# Export
__all__ = [
    "analyze_factory",
    "EquipmentItem",
    "EquipmentType",
    "FactoryAnalysisResult"
]
```

---

## 🌐 BÖLÜM 3: Factory API

### 3.1 Schemas: `/api/schemas/factory.py`

```python
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from enum import Enum


class EquipmentTypeEnum(str, Enum):
    compressor = "compressor"
    boiler = "boiler"
    chiller = "chiller"
    pump = "pump"


class EquipmentItemRequest(BaseModel):
    id: str
    name: str
    equipment_type: EquipmentTypeEnum
    subtype: str
    parameters: Dict[str, Any]


class CreateFactoryProjectRequest(BaseModel):
    name: str
    sector: Optional[str] = None  # textile, food, chemical, metal, cement, paper, automotive
    description: Optional[str] = None


class AddEquipmentRequest(BaseModel):
    equipment: EquipmentItemRequest


class FactoryProjectResponse(BaseModel):
    id: str
    name: str
    sector: Optional[str]
    description: Optional[str]
    equipment_count: int
    created_at: str
    updated_at: str


class FactoryAnalysisResponse(BaseModel):
    factory_id: str
    factory_name: str
    sector: Optional[str]
    
    # Aggregates
    total_energy_input_kW: float
    total_exergy_input_kW: float
    total_useful_exergy_kW: float
    total_exergy_destroyed_kW: float
    factory_exergy_efficiency: float
    
    # Financials
    total_annual_energy_cost_eur: float
    total_annual_exergy_loss_cost_eur: float
    total_potential_savings_eur: float
    
    # Details
    equipment_results: List[Dict]
    hotspots: List[Dict]
    integration_opportunities: List[Dict]
    sankey_data: Dict
```

### 3.2 Routes: `/api/routes/factory.py` (güncelle)

```python
from fastapi import APIRouter, HTTPException
from typing import Dict, List
from datetime import datetime
import uuid

from api.schemas.factory import (
    CreateFactoryProjectRequest,
    AddEquipmentRequest,
    FactoryProjectResponse,
    FactoryAnalysisResponse,
    EquipmentItemRequest
)
from engine.factory import analyze_factory, EquipmentItem, EquipmentType

router = APIRouter()

# In-memory storage (sonra database)
factory_projects: Dict[str, Dict] = {}


@router.post("/factory/projects", response_model=FactoryProjectResponse)
def create_project(request: CreateFactoryProjectRequest):
    """Yeni fabrika projesi oluştur"""
    project_id = str(uuid.uuid4())[:8]
    now = datetime.now().isoformat()
    
    project = {
        "id": project_id,
        "name": request.name,
        "sector": request.sector,
        "description": request.description,
        "equipment": [],
        "created_at": now,
        "updated_at": now
    }
    
    factory_projects[project_id] = project
    
    return FactoryProjectResponse(
        id=project_id,
        name=request.name,
        sector=request.sector,
        description=request.description,
        equipment_count=0,
        created_at=now,
        updated_at=now
    )


@router.get("/factory/projects/{project_id}")
def get_project(project_id: str):
    """Fabrika projesini getir"""
    if project_id not in factory_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project = factory_projects[project_id]
    return {
        "success": True,
        "project": project
    }


@router.get("/factory/projects")
def list_projects():
    """Tüm projeleri listele"""
    projects = [
        {
            "id": p["id"],
            "name": p["name"],
            "sector": p["sector"],
            "equipment_count": len(p["equipment"]),
            "created_at": p["created_at"],
            "updated_at": p["updated_at"]
        }
        for p in factory_projects.values()
    ]
    return {"projects": projects}


@router.post("/factory/projects/{project_id}/equipment")
def add_equipment(project_id: str, request: AddEquipmentRequest):
    """Projeye ekipman ekle"""
    if project_id not in factory_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project = factory_projects[project_id]
    
    # Ekipmanı ekle
    equipment_data = request.equipment.dict()
    project["equipment"].append(equipment_data)
    project["updated_at"] = datetime.now().isoformat()
    
    return {
        "success": True,
        "equipment_count": len(project["equipment"]),
        "equipment_id": equipment_data["id"]
    }


@router.delete("/factory/projects/{project_id}/equipment/{equipment_id}")
def remove_equipment(project_id: str, equipment_id: str):
    """Projeden ekipman sil"""
    if project_id not in factory_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project = factory_projects[project_id]
    
    # Ekipmanı bul ve sil
    original_count = len(project["equipment"])
    project["equipment"] = [
        eq for eq in project["equipment"] if eq["id"] != equipment_id
    ]
    
    if len(project["equipment"]) == original_count:
        raise HTTPException(status_code=404, detail="Equipment not found")
    
    project["updated_at"] = datetime.now().isoformat()
    
    return {
        "success": True,
        "equipment_count": len(project["equipment"])
    }


@router.post("/factory/projects/{project_id}/analyze")
def analyze_factory_project(project_id: str):
    """Fabrika analizi çalıştır"""
    if project_id not in factory_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project = factory_projects[project_id]
    
    if not project["equipment"]:
        raise HTTPException(status_code=400, detail="No equipment in project")
    
    # Equipment listesini dönüştür
    equipment_list = []
    for eq_data in project["equipment"]:
        item = EquipmentItem(
            id=eq_data["id"],
            name=eq_data["name"],
            equipment_type=EquipmentType(eq_data["equipment_type"]),
            subtype=eq_data["subtype"],
            parameters=eq_data["parameters"]
        )
        equipment_list.append(item)
    
    # Analiz
    result = analyze_factory(
        factory_name=project["name"],
        sector=project.get("sector"),
        equipment_list=equipment_list
    )
    
    # Sonucu kaydet
    project["analysis_result"] = {
        "total_energy_input_kW": result.total_energy_input_kW,
        "total_exergy_input_kW": result.total_exergy_input_kW,
        "total_useful_exergy_kW": result.total_useful_exergy_kW,
        "total_exergy_destroyed_kW": result.total_exergy_destroyed_kW,
        "factory_exergy_efficiency": result.factory_exergy_efficiency,
        "total_annual_energy_cost_eur": result.total_annual_energy_cost_eur,
        "total_annual_exergy_loss_cost_eur": result.total_annual_exergy_loss_cost_eur,
        "total_potential_savings_eur": result.total_potential_savings_eur,
        "equipment_results": result.equipment_results,
        "hotspots": result.hotspots,
        "integration_opportunities": result.integration_opportunities,
        "sankey_data": result.sankey_data
    }
    project["updated_at"] = datetime.now().isoformat()
    
    return {
        "success": True,
        "analysis": project["analysis_result"]
    }


@router.post("/factory/projects/{project_id}/interpret")
async def interpret_factory(project_id: str):
    """AI fabrika yorumu"""
    if project_id not in factory_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project = factory_projects[project_id]
    
    if "analysis_result" not in project:
        raise HTTPException(status_code=400, detail="Run analysis first")
    
    # Claude Code ile fabrika yorumu
    from api.services.claude_code_service import interpret_factory_analysis
    
    interpretation = await interpret_factory_analysis(
        factory_name=project["name"],
        sector=project.get("sector"),
        analysis_result=project["analysis_result"]
    )
    
    return {
        "success": True,
        "interpretation": interpretation
    }
```

### 3.3 Claude Code Service Güncelleme

`/api/services/claude_code_service.py` dosyasına ekle:

```python
async def interpret_factory_analysis(
    factory_name: str,
    sector: Optional[str],
    analysis_result: Dict
) -> Dict:
    """
    Claude Code ile fabrika analizi yorumlama.
    
    Fabrika yorumu için SKILL dosyası ve knowledge/factory/ kullanılır.
    """
    # SKILL dosyasını oku
    skill_content = _load_skill_file()
    
    # Analiz verisini formatlı string'e dönüştür
    analysis_text = _format_factory_analysis(factory_name, sector, analysis_result)
    
    # Prompt oluştur
    prompt = f"""
{skill_content}

---

## Fabrika Analiz Verisi

{analysis_text}

---

## Görev

Yukarıdaki fabrika exergy analiz sonuçlarını yorumla.

MUTLAKA şu knowledge dosyalarını referans al:
1. knowledge/factory/cross_equipment.md - Ekipmanlar arası fırsatlar
2. knowledge/factory/prioritization.md - Önceliklendirme
3. knowledge/factory/factory_benchmarks.md - Sektörel benchmark
{f'4. knowledge/factory/sector_{sector}.md - Sektöre özel bilgi' if sector else ''}

Yanıtını şu JSON formatında ver:
{{
    "summary": "Fabrika genel değerlendirmesi (2-3 cümle)",
    "factory_efficiency_assessment": "Fabrika exergy verimi değerlendirmesi",
    "hotspot_analysis": "En kritik kayıp noktaları analizi",
    "integration_opportunities": [
        {{
            "title": "Fırsat başlığı",
            "description": "Detaylı açıklama",
            "potential_savings_eur": 0,
            "priority": "high/medium/low"
        }}
    ],
    "prioritized_actions": [
        {{
            "timeframe": "immediate/short_term/medium_term",
            "action": "Yapılacak iş",
            "expected_benefit": "Beklenen fayda"
        }}
    ],
    "sector_specific_insights": "Sektöre özel öneriler (varsa)",
    "warnings": ["Dikkat edilmesi gerekenler"]
}}
"""
    
    # Claude Code çağır
    result = await _call_claude_code(prompt)
    
    return result


def _format_factory_analysis(factory_name: str, sector: Optional[str], result: Dict) -> str:
    """Analiz sonucunu okunabilir formata dönüştür"""
    lines = [
        f"Fabrika: {factory_name}",
        f"Sektör: {sector or 'Belirtilmemiş'}",
        "",
        "## Toplam Metrikler",
        f"- Toplam Exergy Girişi: {result['total_exergy_input_kW']:.1f} kW",
        f"- Faydalı Exergy: {result['total_useful_exergy_kW']:.1f} kW",
        f"- Exergy Kaybı: {result['total_exergy_destroyed_kW']:.1f} kW",
        f"- Fabrika Exergy Verimi: %{result['factory_exergy_efficiency']:.1f}",
        f"- Yıllık Enerji Maliyeti: €{result['total_annual_energy_cost_eur']:,.0f}",
        f"- Potansiyel Tasarruf: €{result['total_potential_savings_eur']:,.0f}",
        "",
        "## Ekipman Sonuçları",
    ]
    
    for eq in result.get("equipment_results", []):
        if "error" not in eq:
            metrics = eq.get("result", {}).get("metrics", {})
            lines.append(f"- {eq['name']} ({eq['type']}/{eq['subtype']}): "
                        f"Exergy verimi %{metrics.get('exergy_efficiency', 0):.1f}")
    
    lines.append("")
    lines.append("## Hotspots (Kayıp Sıralaması)")
    
    for hs in result.get("hotspots", [])[:5]:
        lines.append(f"- {hs['equipment_name']}: {hs['exergy_destroyed_kW']:.1f} kW kayıp, "
                    f"€{hs['estimated_annual_loss_eur']:,.0f}/yıl, öncelik: {hs['priority']}")
    
    lines.append("")
    lines.append("## Tespit Edilen Entegrasyon Fırsatları")
    
    for opp in result.get("integration_opportunities", []):
        lines.append(f"- {opp['title']}: €{opp.get('estimated_savings_eur', 0):,.0f}/yıl tasarruf, "
                    f"{opp.get('estimated_roi_years', 0):.1f} yıl ROI")
    
    return "\n".join(lines)
```

---

## 🎨 BÖLÜM 4: Frontend

### 4.1 Yeni Dosyalar

```
frontend/src/
├── pages/
│   ├── FactoryList.jsx          # Proje listesi
│   ├── FactoryWizard.jsx        # Yeni proje oluşturma
│   └── FactoryDashboard.jsx     # Proje detay ve sonuçlar
│
├── components/factory/
│   ├── EquipmentInventory.jsx   # Ekipman listesi
│   ├── AddEquipmentModal.jsx    # Ekipman ekleme modal
│   ├── FactorySankey.jsx        # Fabrika Sankey diyagramı
│   ├── HotspotList.jsx          # Kayıp sıralaması
│   ├── IntegrationOpportunities.jsx  # Cross-equipment fırsatlar
│   └── FactoryAIInterpretation.jsx   # AI fabrika yorumu
│
└── services/
    └── factoryApi.js            # Factory API fonksiyonları
```

### 4.2 API Service: `/frontend/src/services/factoryApi.js`

```javascript
import api from './api';

export const createFactoryProject = async (data) => {
  const response = await api.post('/factory/projects', data);
  return response.data;
};

export const getFactoryProjects = async () => {
  const response = await api.get('/factory/projects');
  return response.data;
};

export const getFactoryProject = async (projectId) => {
  const response = await api.get(`/factory/projects/${projectId}`);
  return response.data;
};

export const addEquipmentToProject = async (projectId, equipment) => {
  const response = await api.post(`/factory/projects/${projectId}/equipment`, {
    equipment
  });
  return response.data;
};

export const removeEquipmentFromProject = async (projectId, equipmentId) => {
  const response = await api.delete(`/factory/projects/${projectId}/equipment/${equipmentId}`);
  return response.data;
};

export const analyzeFactory = async (projectId) => {
  const response = await api.post(`/factory/projects/${projectId}/analyze`);
  return response.data;
};

export const interpretFactory = async (projectId) => {
  const response = await api.post(`/factory/projects/${projectId}/interpret`);
  return response.data;
};
```

### 4.3 Factory Wizard Akışı

```
Step 1: Proje Bilgileri
┌─────────────────────────────────────────────────────────────┐
│  Yeni Fabrika Projesi                                       │
│                                                              │
│  Fabrika Adı: [________________________]                    │
│                                                              │
│  Sektör:      [Tekstil                    ▼]               │
│               • Tekstil                                      │
│               • Gıda ve İçecek                              │
│               • Kimya                                        │
│               • Metal                                        │
│               • Çimento                                      │
│               • Kağıt                                        │
│               • Otomotiv                                     │
│                                                              │
│  Açıklama:    [________________________]                    │
│               [________________________]                    │
│                                                              │
│                                    [İptal]  [Devam →]       │
└─────────────────────────────────────────────────────────────┘

Step 2: Ekipman Ekleme
┌─────────────────────────────────────────────────────────────┐
│  Ekipman Envanteri                      [+ Ekipman Ekle]    │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ # │ Tip        │ Alt Tip    │ Ad           │ Durum │   │
│  ├───┼────────────┼────────────┼──────────────┼───────┤   │
│  │ 1 │ Kompresör  │ Vidalı     │ Ana Komp.    │ ✓     │   │
│  │ 2 │ Kazan      │ Ateş Borulu│ Buhar Kazanı │ ✓     │   │
│  │ 3 │ Chiller    │ Santrifüj  │ Merkezi Sog. │ ✓     │   │
│  │ 4 │ Pompa      │ Santrifüj  │ Soğutma Pomp.│ ✓     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  Minimum 2 ekipman gerekli.                                 │
│                                                              │
│                          [← Geri]  [Analiz Çalıştır →]     │
└─────────────────────────────────────────────────────────────┘

Step 3: Sonuçlar
┌─────────────────────────────────────────────────────────────┐
│  Fabrika Analiz Sonuçları                                   │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Toplam Güç   │  │ Exergy Kaybı │  │ Fabrika      │      │
│  │   245 kW     │  │   142 kW     │  │ Verimi: %42  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
│  [=============== FABRİKA SANKEY ===============]           │
│                                                              │
│  Hotspots:                                                   │
│  1. 🔥 Buhar Kazanı - 85 kW kayıp - €18,500/yıl            │
│  2. 💨 Ana Kompresör - 32 kW kayıp - €6,200/yıl            │
│  3. ❄️ Merkezi Soğutma - 18 kW kayıp - €3,800/yıl          │
│                                                              │
│  Entegrasyon Fırsatları:                                    │
│  • Kompresör → Kazan: €4,500/yıl tasarruf                  │
│  • Chiller → Sıcak Su: €2,200/yıl tasarruf                 │
│                                                              │
│  [AI Fabrika Yorumu]                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Bu tekstil fabrikası %42 exergy verimi ile sektör   │   │
│  │ ortalamasının (%35) üzerinde performans gösteriyor. │   │
│  │ En büyük iyileştirme fırsatı kazan sisteminde...    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│                     [PDF Rapor]  [Projeyi Kaydet]          │
└─────────────────────────────────────────────────────────────┘
```

### 4.4 Routing Güncelleme

`App.jsx`'e ekle:

```jsx
import FactoryList from './pages/FactoryList';
import FactoryWizard from './pages/FactoryWizard';
import FactoryDashboard from './pages/FactoryDashboard';

// Routes içinde:
<Route path="/factory" element={<FactoryList />} />
<Route path="/factory/new" element={<FactoryWizard />} />
<Route path="/factory/:projectId" element={<FactoryDashboard />} />
```

---

## ✅ BÖLÜM 5: Uygulama Sırası

### Adım 1: Knowledge Index ve SKILL Güncelleme
1. `/knowledge/INDEX.md` oluştur
2. `/skills/SKILL_exergy_interpreter.md` güncelle - fabrika navigasyonu ekle

### Adım 2: Backend
1. `/api/schemas/factory.py` oluştur
2. `/engine/factory.py` oluştur
3. `/api/routes/factory.py` güncelle
4. `/api/services/claude_code_service.py` güncelle - `interpret_factory_analysis` ekle
5. `/api/main.py` kontrol et
6. Testler ekle

### Adım 3: Frontend
1. `/frontend/src/services/factoryApi.js` oluştur
2. `/frontend/src/pages/FactoryList.jsx` oluştur
3. `/frontend/src/pages/FactoryWizard.jsx` oluştur
4. `/frontend/src/pages/FactoryDashboard.jsx` oluştur
5. `/frontend/src/components/factory/*.jsx` oluştur
6. Routing güncelle
7. Sidebar'daki factory linklerini aktif et

### Adım 4: Test
1. Backend testleri çalıştır
2. Frontend build kontrol
3. Manual test:
   - Proje oluştur
   - Ekipman ekle (minimum 2)
   - Analiz çalıştır
   - AI yorumu al
   - Sankey görüntüle

---

## 🧪 Test Senaryoları

### Senaryo 1: Basit Fabrika
```
Fabrika: Test Fabrikası
Sektör: Tekstil

Ekipmanlar:
1. Kompresör (vidalı, 37 kW)
2. Kazan (ateş borulu, 2 ton/h buhar)

Beklenen:
- Fabrika exergy verimi ~%30-40
- Kompresör → Kazan ısı geri kazanım fırsatı tespit edilmeli
```

### Senaryo 2: Tam Fabrika
```
Fabrika: Endüstriyel Tesis
Sektör: Gıda

Ekipmanlar:
1. Kompresör #1 (vidalı, 55 kW)
2. Kompresör #2 (vidalı, 37 kW)
3. Kazan (su borulu, 4 ton/h)
4. Chiller (santrifüj, 350 kW soğutma)
5. Pompa #1 (santrifüj, 15 kW, throttle)
6. Pompa #2 (santrifüj, 7.5 kW, VSD)

Beklenen:
- Hotspot sıralaması
- Çoklu entegrasyon fırsatı
- Pompa VSD retrofit önerisi
- Sektörel karşılaştırma
```

---

**Bu brief factory analysis sisteminin tamamı için tek kaynak noktasıdır.**
