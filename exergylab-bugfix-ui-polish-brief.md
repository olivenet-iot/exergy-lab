# ExergyLab Bug Fix & UI Polish Brief (v2)

> **Claude Code için:** Bu brief'teki bug'ları düzelt ve UI iyileştirmelerini yap. Tek prompt'ta tamamla.

---

## 🐛 BÖLÜM 1: Bug Fixes

### 1.1 Cross-Equipment Hesaplama Hatası

**Dosya:** `/engine/factory.py`

**Sorun:** `_detect_integration_opportunities()` fonksiyonunda kompresör → kazan ısı geri kazanım hesabı yanlış.

**Mevcut (yanlış):**
```
37 kW kompresör → 1.5 kW geri kazanım, €464/yıl, 32.3 yıl ROI
```

**Olması gereken:**
```
37 kW kompresör → ~24 kW atık ısı (gücün %65'i)
Geri kazanılabilir: ~15-20 kW (atık ısının %70-80'i)
Tasarruf: 15 kW × 6000 saat × €0.05/kWh termal = €4,500/yıl
Yatırım: ~€10,000-15,000 (HRU + piping)
ROI: 2-3 yıl
```

**Düzeltme:**

```python
def _detect_integration_opportunities(
    equipment_list: List[EquipmentItem],
    equipment_results: List[Dict]
) -> List[Dict]:
    """Ekipmanlar arası entegrasyon fırsatlarını tespit et."""
    opportunities = []
    
    # Ekipman tiplerini grupla
    equipment_by_type = {}
    results_by_id = {}
    
    for item in equipment_list:
        eq_type = item.equipment_type.value
        if eq_type not in equipment_by_type:
            equipment_by_type[eq_type] = []
        equipment_by_type[eq_type].append(item)
    
    for eq in equipment_results:
        results_by_id[eq["id"]] = eq
    
    has_compressor = "compressor" in equipment_by_type
    has_boiler = "boiler" in equipment_by_type
    has_chiller = "chiller" in equipment_by_type
    has_pump = "pump" in equipment_by_type
    
    # Fırsat 1: Kompresör atık ısısı → Kazan besleme suyu
    if has_compressor and has_boiler:
        for comp_item in equipment_by_type["compressor"]:
            comp_result = results_by_id.get(comp_item.id, {})
            if "error" in comp_result:
                continue
            
            metrics = comp_result.get("result", {}).get("metrics", {})
            
            # Kompresör gücünü al - DOĞRU ALAN
            power_kW = (
                metrics.get("power_input_kW") or 
                metrics.get("exergy_input_kW") or 
                comp_item.parameters.get("power_kW") or
                comp_item.parameters.get("motor_power_kW") or
                0
            )
            
            if power_kW < 5:  # Çok küçük kompresörler için skip
                continue
            
            # Atık ısı hesabı
            # Kompresör elektrik gücünün ~90-95%'i ısıya dönüşür
            # Bunun ~70-80%'i geri kazanılabilir (su soğutmalı sistemde)
            heat_to_oil_water = power_kW * 0.90  # Isıya dönüşen
            recoverable_heat_kW = heat_to_oil_water * 0.75  # Geri kazanılabilir
            
            # Yıllık çalışma saati
            operating_hours = comp_item.parameters.get("operating_hours", 6000)
            
            # Tasarruf hesabı
            # Geri kazanılan ısı, kazan yakıt tasarrufu sağlar
            # Doğalgaz fiyatı ~€0.04-0.06/kWh termal
            thermal_energy_price = 0.05  # €/kWh
            annual_savings = recoverable_heat_kW * operating_hours * thermal_energy_price
            
            # Yatırım tahmini
            # Heat recovery unit: ~€200-400/kW
            investment = recoverable_heat_kW * 300 + 5000  # Base cost + per kW
            
            # ROI
            roi_years = investment / annual_savings if annual_savings > 0 else 99
            
            # Her kazan için fırsat ekle
            for boiler_item in equipment_by_type["boiler"]:
                opportunities.append({
                    "id": f"comp_to_boiler_{comp_item.id}_{boiler_item.id}",
                    "title": "Kompresör Atık Isısı → Kazan Besleme Suyu",
                    "description": f"{comp_item.name} atık ısısının {boiler_item.name} besleme suyu ön ısıtmada kullanımı. Tahmini geri kazanılabilir ısı: {recoverable_heat_kW:.1f} kW.",
                    "source_equipment": comp_item.id,
                    "target_equipment": boiler_item.id,
                    "source_type": "compressor",
                    "target_type": "boiler",
                    "potential_recovery_kW": round(recoverable_heat_kW, 1),
                    "estimated_savings_eur": round(annual_savings, 0),
                    "estimated_investment_eur": round(investment, 0),
                    "estimated_roi_years": round(roi_years, 1),
                    "complexity": "medium",
                    "reference": "knowledge/factory/cross_equipment.md"
                })
                break  # İlk kazan için bir kez ekle
    
    # Fırsat 2: Kompresör atık ısısı → Bina ısıtma (kazan yoksa)
    if has_compressor and not has_boiler:
        for comp_item in equipment_by_type["compressor"]:
            comp_result = results_by_id.get(comp_item.id, {})
            if "error" in comp_result:
                continue
            
            metrics = comp_result.get("result", {}).get("metrics", {})
            power_kW = (
                metrics.get("power_input_kW") or 
                metrics.get("exergy_input_kW") or 
                comp_item.parameters.get("power_kW") or
                0
            )
            
            if power_kW < 10:
                continue
            
            recoverable_heat_kW = power_kW * 0.90 * 0.70
            operating_hours = comp_item.parameters.get("operating_hours", 6000)
            heating_season_hours = min(operating_hours, 3000)  # Kış ayları
            
            annual_savings = recoverable_heat_kW * heating_season_hours * 0.08
            investment = recoverable_heat_kW * 200 + 3000
            roi_years = investment / annual_savings if annual_savings > 0 else 99
            
            opportunities.append({
                "id": f"comp_to_hvac_{comp_item.id}",
                "title": "Kompresör Atık Isısı → Bina Isıtma",
                "description": f"{comp_item.name}'den {recoverable_heat_kW:.1f} kW atık ısı kış aylarında bina ısıtması için kullanılabilir.",
                "source_equipment": comp_item.id,
                "target_equipment": "HVAC",
                "source_type": "compressor",
                "target_type": "hvac",
                "potential_recovery_kW": round(recoverable_heat_kW, 1),
                "estimated_savings_eur": round(annual_savings, 0),
                "estimated_investment_eur": round(investment, 0),
                "estimated_roi_years": round(roi_years, 1),
                "complexity": "low",
                "reference": "knowledge/factory/cross_equipment.md"
            })
    
    # Fırsat 3: Chiller kondenser ısısı → Sıcak su
    if has_chiller:
        for chiller_item in equipment_by_type["chiller"]:
            chiller_result = results_by_id.get(chiller_item.id, {})
            if "error" in chiller_result:
                continue
            
            metrics = chiller_result.get("result", {}).get("metrics", {})
            cooling_kW = (
                metrics.get("cooling_capacity_kW") or
                chiller_item.parameters.get("cooling_capacity_kW") or
                0
            )
            
            if cooling_kW < 50:
                continue
            
            # Kondenser ısısı = soğutma + kompresör gücü (COP ~4)
            condenser_heat_kW = cooling_kW * 1.25
            
            # Desuperheater ile geri kazanım (~15% kondenser ısısı)
            recoverable_kW = condenser_heat_kW * 0.15
            
            operating_hours = chiller_item.parameters.get("operating_hours", 4000)
            annual_savings = recoverable_kW * operating_hours * 0.06
            investment = recoverable_kW * 300 + 5000
            roi_years = investment / annual_savings if annual_savings > 0 else 99
            
            opportunities.append({
                "id": f"chiller_heat_recovery_{chiller_item.id}",
                "title": "Chiller Kondenser Isısı → Sıcak Su",
                "description": f"{chiller_item.name} kondenserinden {recoverable_kW:.1f} kW ısı desuperheater ile geri kazanılarak sıcak su üretilebilir.",
                "source_equipment": chiller_item.id,
                "target_equipment": "hot_water",
                "source_type": "chiller",
                "target_type": "hot_water",
                "potential_recovery_kW": round(recoverable_kW, 1),
                "estimated_savings_eur": round(annual_savings, 0),
                "estimated_investment_eur": round(investment, 0),
                "estimated_roi_years": round(roi_years, 1),
                "complexity": "medium",
                "reference": "knowledge/factory/cross_equipment.md"
            })
    
    # Fırsat 4: Pompa VSD retrofit (throttle kontrolü varsa)
    if has_pump:
        for pump_item in equipment_by_type["pump"]:
            pump_result = results_by_id.get(pump_item.id, {})
            if "error" in pump_result:
                continue
            
            control_method = pump_item.parameters.get("control_method", "none")
            has_vsd = pump_item.parameters.get("has_vsd", False)
            
            if control_method == "throttle" and not has_vsd:
                metrics = pump_result.get("result", {}).get("metrics", {})
                power_kW = (
                    metrics.get("motor_power_kW") or
                    metrics.get("power_input_kW") or
                    pump_item.parameters.get("motor_power_kW") or
                    0
                )
                
                if power_kW < 5:
                    continue
                
                operating_hours = pump_item.parameters.get("operating_hours", 6000)
                electricity_price = pump_item.parameters.get("electricity_price", 0.12)
                
                # VSD tasarruf potansiyeli %30-50
                savings_ratio = 0.35
                annual_savings = power_kW * operating_hours * electricity_price * savings_ratio
                
                investment = power_kW * 300 + 2000  # VSD cost
                roi_years = investment / annual_savings if annual_savings > 0 else 99
                
                opportunities.append({
                    "id": f"pump_vsd_{pump_item.id}",
                    "title": f"Pompa VSD Retrofit: {pump_item.name}",
                    "description": f"{pump_item.name} pompası throttle kontrolünden VSD'ye geçirilerek %30-50 enerji tasarrufu sağlanabilir.",
                    "source_equipment": pump_item.id,
                    "target_equipment": None,
                    "source_type": "pump",
                    "target_type": None,
                    "power_kW": round(power_kW, 1),
                    "estimated_savings_eur": round(annual_savings, 0),
                    "estimated_investment_eur": round(investment, 0),
                    "estimated_roi_years": round(roi_years, 1),
                    "complexity": "low",
                    "reference": "knowledge/pump/solutions/vsd.md"
                })
    
    # Tasarruf büyüklüğüne göre sırala
    opportunities.sort(key=lambda x: x.get("estimated_savings_eur", 0), reverse=True)
    
    return opportunities
```

### 1.2 Hotspot Öncelik Tutarlılığı

**Dosya:** `/engine/factory.py`

**Sorun:** `_get_priority()` fonksiyonu hem verimliliği hem de mutlak kaybı değerlendirmeli.

**Düzeltme:**

```python
def _get_priority(efficiency: float, loss_kW: float, total_loss_kW: float = None) -> str:
    """
    Öncelik belirleme.
    
    Kriterler:
    1. Exergy verimi çok düşükse → high
    2. Kayıp mutlak olarak yüksekse → high
    3. Kayıp toplam kaybın büyük kısmıysa → high
    """
    # Verimlilik bazlı
    if efficiency < 25:
        return "high"
    
    # Mutlak kayıp bazlı
    if loss_kW > 100:
        return "high"
    elif loss_kW > 30:
        return "medium"
    
    # Toplam kayıptaki pay bazlı (varsa)
    if total_loss_kW and total_loss_kW > 0:
        loss_ratio = loss_kW / total_loss_kW
        if loss_ratio > 0.5:  # %50'den fazla
            return "high"
        elif loss_ratio > 0.2:  # %20'den fazla
            return "medium"
    
    # Verimlilik orta seviye
    if efficiency < 45:
        return "medium"
    
    return "low"
```

Ve `_identify_hotspots()` fonksiyonunda kullan:

```python
def _identify_hotspots(equipment_results: List[Dict]) -> List[Dict]:
    """Exergy kayıp sıralaması"""
    hotspots = []
    
    # Önce toplam kaybı hesapla
    total_loss = 0
    for eq in equipment_results:
        if "error" in eq:
            continue
        result = eq.get("result", {})
        metrics = result.get("metrics", {})
        exergy_input = metrics.get("exergy_input_kW", 0) or metrics.get("power_input_kW", 0) or 0
        exergy_output = metrics.get("exergy_output_kW", 0) or metrics.get("useful_exergy_kW", 0) or 0
        total_loss += (exergy_input - exergy_output)
    
    for eq in equipment_results:
        if "error" in eq:
            continue
        
        result = eq.get("result", {})
        metrics = result.get("metrics", {})
        
        exergy_input = metrics.get("exergy_input_kW", 0) or metrics.get("power_input_kW", 0) or 0
        exergy_output = metrics.get("exergy_output_kW", 0) or metrics.get("useful_exergy_kW", 0) or 0
        exergy_destroyed = exergy_input - exergy_output
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
            "priority": _get_priority(exergy_efficiency, exergy_destroyed, total_loss)
        })
    
    # Kayıp büyüklüğüne göre sırala
    hotspots.sort(key=lambda x: x["exergy_destroyed_kW"], reverse=True)
    
    return hotspots
```

---

## 🎨 BÖLÜM 2: UI Polish

### 2.1 Yakıt Tipi Dropdown Styling

**Dosya:** `/frontend/src/components/forms/FormField.jsx`

**Sorun:** Select dropdown seçenekleri düzgün görünmüyor.

**Düzeltme:** Select field için proper styling:

```jsx
// FormField.jsx içinde select tipi için
if (field.type === 'select') {
  return (
    <div key={field.id} className="space-y-1">
      <label className="block text-sm font-medium text-gray-700">
        {field.label}
        {field.required && <span className="text-red-500">*</span>}
      </label>
      <select
        value={value || field.default || ''}
        onChange={(e) => onChange(field.id, e.target.value)}
        className="w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm 
                   focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500
                   bg-white text-gray-900"
        required={field.required}
      >
        <option value="" disabled>Seçiniz...</option>
        {field.options?.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      {field.unit && (
        <span className="text-sm text-gray-500">{field.unit}</span>
      )}
    </div>
  );
}
```

### 2.2 Ekipman Form Alanları - Varsayılan Değerler ve Birimler

**Dosya:** `/api/routes/analysis.py` veya ilgili config endpoint

Boiler için form field tanımlarını güncelle:

```python
BOILER_FIELDS = [
    {
        "id": "name",
        "label": "Ekipman Adı",
        "type": "text",
        "required": True,
        "default": "Kazan #1"
    },
    {
        "id": "fuel_type",
        "label": "Yakıt Tipi",
        "type": "select",
        "required": True,
        "default": "natural_gas",
        "options": [
            {"value": "natural_gas", "label": "Doğalgaz"},
            {"value": "fuel_oil", "label": "Fuel Oil"},
            {"value": "coal", "label": "Kömür"},
            {"value": "biomass", "label": "Biyokütle"},
            {"value": "lpg", "label": "LPG"},
            {"value": "diesel", "label": "Dizel"}
        ]
    },
    {
        "id": "fuel_flow_rate",
        "label": "Yakıt Debisi",
        "type": "number",
        "required": True,
        "unit": "kg/h",  # veya m³/h for natural gas
        "min": 1,
        "default": 100,
        "hint": "Doğalgaz için m³/h, diğerleri için kg/h"
    },
    {
        "id": "steam_flow_rate",
        "label": "Buhar Debisi",
        "type": "number",
        "required": True,
        "unit": "kg/h",
        "min": 100,
        "default": 2000
    },
    {
        "id": "steam_pressure",
        "label": "Buhar Basıncı",
        "type": "number",
        "required": True,
        "unit": "bar",
        "min": 1,
        "max": 50,
        "default": 10
    },
    {
        "id": "steam_temperature",
        "label": "Buhar Sıcaklığı",
        "type": "number",
        "required": False,
        "unit": "°C",
        "default": 184,
        "hint": "Boş bırakılırsa doymuş buhar varsayılır"
    },
    {
        "id": "feedwater_temperature",
        "label": "Besleme Suyu Sıcaklığı",
        "type": "number",
        "required": False,
        "unit": "°C",
        "min": 10,
        "max": 105,
        "default": 80
    },
    {
        "id": "flue_gas_temperature",
        "label": "Baca Gazı Sıcaklığı",
        "type": "number",
        "required": False,
        "unit": "°C",
        "min": 100,
        "max": 400,
        "default": 180
    },
    {
        "id": "excess_air",
        "label": "Fazla Hava",
        "type": "number",
        "required": False,
        "unit": "%",
        "min": 5,
        "max": 50,
        "default": 15
    },
    {
        "id": "blowdown_rate",
        "label": "Blowdown Oranı",
        "type": "number",
        "required": False,
        "unit": "%",
        "min": 0,
        "max": 10,
        "default": 3
    },
    {
        "id": "operating_hours",
        "label": "Yıllık Çalışma Saati",
        "type": "number",
        "required": False,
        "unit": "saat/yıl",
        "min": 1000,
        "max": 8760,
        "default": 6000
    },
    {
        "id": "fuel_price",
        "label": "Yakıt Fiyatı",
        "type": "number",
        "required": False,
        "unit": "€/kWh",  # Normalize edilmiş birim
        "min": 0.01,
        "max": 1,
        "default": 0.04,
        "hint": "Doğalgaz ~€0.04/kWh, Fuel oil ~€0.05/kWh"
    }
]
```

### 2.3 Kompresör Form Varsayılan Değerleri

```python
COMPRESSOR_FIELDS = [
    {
        "id": "name",
        "label": "Ekipman Adı",
        "type": "text",
        "required": True,
        "default": "Kompresör #1"
    },
    {
        "id": "power_kW",
        "label": "Motor Gücü",
        "type": "number",
        "required": True,
        "unit": "kW",
        "min": 1,
        "max": 1000,
        "default": 37
    },
    {
        "id": "flow_rate_m3_min",
        "label": "Hava Debisi",
        "type": "number",
        "required": True,
        "unit": "m³/min",
        "min": 0.1,
        "max": 200,
        "default": 6.2
    },
    {
        "id": "discharge_pressure_bar",
        "label": "Çıkış Basıncı",
        "type": "number",
        "required": True,
        "unit": "bar",
        "min": 4,
        "max": 15,
        "default": 7.5
    },
    {
        "id": "inlet_temperature",
        "label": "Giriş Havası Sıcaklığı",
        "type": "number",
        "required": False,
        "unit": "°C",
        "min": -10,
        "max": 50,
        "default": 25
    },
    {
        "id": "operating_hours",
        "label": "Yıllık Çalışma Saati",
        "type": "number",
        "required": False,
        "unit": "saat/yıl",
        "min": 1000,
        "max": 8760,
        "default": 6000
    },
    {
        "id": "electricity_price",
        "label": "Elektrik Fiyatı",
        "type": "number",
        "required": False,
        "unit": "€/kWh",
        "min": 0.01,
        "max": 0.5,
        "default": 0.12
    },
    {
        "id": "load_factor",
        "label": "Yük Faktörü",
        "type": "number",
        "required": False,
        "unit": "%",
        "min": 20,
        "max": 100,
        "default": 75,
        "hint": "Ortalama yüklenme oranı"
    }
]
```

### 2.4 Chiller Form Varsayılan Değerleri

```python
CHILLER_FIELDS = [
    {
        "id": "name",
        "label": "Ekipman Adı",
        "type": "text",
        "required": True,
        "default": "Chiller #1"
    },
    {
        "id": "cooling_capacity_kW",
        "label": "Soğutma Kapasitesi",
        "type": "number",
        "required": True,
        "unit": "kW",
        "min": 10,
        "max": 10000,
        "default": 350
    },
    {
        "id": "compressor_power_kW",
        "label": "Kompresör Gücü",
        "type": "number",
        "required": True,
        "unit": "kW",
        "min": 5,
        "max": 3000,
        "default": 70
    },
    {
        "id": "chilled_water_supply_temp",
        "label": "Soğutma Suyu Çıkış",
        "type": "number",
        "required": False,
        "unit": "°C",
        "min": 2,
        "max": 15,
        "default": 7
    },
    {
        "id": "chilled_water_return_temp",
        "label": "Soğutma Suyu Dönüş",
        "type": "number",
        "required": False,
        "unit": "°C",
        "min": 8,
        "max": 20,
        "default": 12
    },
    {
        "id": "condenser_water_supply_temp",
        "label": "Kondenser Suyu Giriş",
        "type": "number",
        "required": False,
        "unit": "°C",
        "min": 20,
        "max": 40,
        "default": 30
    },
    {
        "id": "condenser_water_return_temp",
        "label": "Kondenser Suyu Çıkış",
        "type": "number",
        "required": False,
        "unit": "°C",
        "min": 25,
        "max": 45,
        "default": 35
    },
    {
        "id": "operating_hours",
        "label": "Yıllık Çalışma Saati",
        "type": "number",
        "required": False,
        "unit": "saat/yıl",
        "default": 4000
    },
    {
        "id": "electricity_price",
        "label": "Elektrik Fiyatı",
        "type": "number",
        "required": False,
        "unit": "€/kWh",
        "default": 0.12
    }
]
```

### 2.5 Pompa Form Varsayılan Değerleri

```python
PUMP_FIELDS = [
    {
        "id": "name",
        "label": "Ekipman Adı",
        "type": "text",
        "required": True,
        "default": "Pompa #1"
    },
    {
        "id": "motor_power_kW",
        "label": "Motor Gücü",
        "type": "number",
        "required": True,
        "unit": "kW",
        "min": 0.5,
        "max": 500,
        "default": 15
    },
    {
        "id": "flow_rate_m3h",
        "label": "Debi",
        "type": "number",
        "required": True,
        "unit": "m³/h",
        "min": 1,
        "max": 5000,
        "default": 50
    },
    {
        "id": "head_m",
        "label": "Toplam Basma Yüksekliği",
        "type": "number",
        "required": True,
        "unit": "m",
        "min": 5,
        "max": 500,
        "default": 40
    },
    {
        "id": "fluid_density",
        "label": "Akışkan Yoğunluğu",
        "type": "number",
        "required": False,
        "unit": "kg/m³",
        "default": 1000,
        "hint": "Su için 1000"
    },
    {
        "id": "control_method",
        "label": "Kontrol Yöntemi",
        "type": "select",
        "required": False,
        "default": "none",
        "options": [
            {"value": "none", "label": "Kontrol Yok"},
            {"value": "throttle", "label": "Vana ile Kısma"},
            {"value": "bypass", "label": "Bypass"},
            {"value": "on_off", "label": "On/Off"}
        ]
    },
    {
        "id": "throttle_loss_percent",
        "label": "Vana Kaybı",
        "type": "number",
        "required": False,
        "unit": "%",
        "default": 0,
        "hint": "Kısma vanası varsa kayıp yüzdesi"
    },
    {
        "id": "has_vsd",
        "label": "VSD Var mı?",
        "type": "boolean",
        "required": False,
        "default": false
    },
    {
        "id": "motor_efficiency",
        "label": "Motor Verimi",
        "type": "number",
        "required": False,
        "unit": "%",
        "min": 70,
        "max": 98,
        "default": 92
    },
    {
        "id": "pump_efficiency",
        "label": "Pompa Verimi",
        "type": "number",
        "required": False,
        "unit": "%",
        "min": 40,
        "max": 95,
        "default": 75,
        "hint": "Bilinmiyorsa boş bırakın, tahmin edilir"
    },
    {
        "id": "operating_hours",
        "label": "Yıllık Çalışma Saati",
        "type": "number",
        "required": False,
        "unit": "saat/yıl",
        "default": 6000
    },
    {
        "id": "electricity_price",
        "label": "Elektrik Fiyatı",
        "type": "number",
        "required": False,
        "unit": "€/kWh",
        "default": 0.12
    }
]
```

### 2.6 Form Field Hint Gösterimi

**Dosya:** `/frontend/src/components/forms/FormField.jsx`

Hint text ekle:

```jsx
{field.hint && (
  <p className="text-xs text-gray-400 mt-1">{field.hint}</p>
)}
```

### 2.7 AddEquipmentModal'da Varsayılan Değerleri Uygula

**Dosya:** `/frontend/src/components/factory/AddEquipmentModal.jsx`

Form açıldığında varsayılan değerleri set et:

```jsx
useEffect(() => {
  if (config?.fields) {
    const defaults = {};
    config.fields.forEach(field => {
      if (field.default !== undefined) {
        defaults[field.id] = field.default;
      }
    });
    setParameters(prev => ({ ...defaults, ...prev }));
  }
}, [config]);
```

---

## 🧪 BÖLÜM 3: Test Senaryoları

### Test 1: Cross-Equipment Hesaplama
```
Kompresör: 37 kW vidalı
Kazan: 2 ton/h buhar

Beklenen entegrasyon fırsatı:
- Geri kazanım: ~20-25 kW
- Tasarruf: €4,000-6,000/yıl
- ROI: 1.5-3 yıl
```

### Test 2: Hotspot Önceliklendirme
```
Kazan: %22 verim, 1500 kW kayıp → high
Kompresör: %58 verim, 15 kW kayıp → low (toplam kaybın %1'i)
```

### Test 3: Form Varsayılan Değerler
```
Yeni kazan eklerken:
- Buhar basıncı: 10 bar (otomatik)
- Yakıt tipi: Doğalgaz (otomatik)
- Çalışma saati: 6000 (otomatik)
```

---

## ✅ Tamamlama Kontrol Listesi

### Bug Fixes
- [ ] Cross-equipment hesaplama düzeltildi
- [ ] Hotspot öncelik mantığı güncellendi
- [ ] Testler geçiyor

### UI Polish
- [ ] Select dropdown styling düzeltildi
- [ ] Boiler form varsayılan değerleri eklendi
- [ ] Kompresör form varsayılan değerleri eklendi
- [ ] Chiller form varsayılan değerleri eklendi
- [ ] Pompa form varsayılan değerleri eklendi
- [ ] Hint text gösterimi eklendi
- [ ] Modal'da varsayılan değerler yükleniyor
- [ ] Frontend build başarılı

---

**Bu brief bug fix ve UI polish için tek kaynak noktasıdır.**
