# ExergyLab Engine Modülleri Brief

> **Claude Code için:** Bu dosyayı oku ve boiler, chiller, pump engine modüllerini oluştur.

---

## 🎯 Görev Özeti

Mevcut `engine/compressor.py` referans alınarak 3 yeni engine modülü oluştur:
- `engine/boiler.py`
- `engine/chiller.py`
- `engine/pump.py`

Her modül aynı interface'i sağlamalı ve `equipment_registry.py`'daki `is_engine_ready()` fonksiyonunu güncelleyerek aktif hale getir.

---

## 📚 BÖLÜM 1: Mevcut Yapıyı Anla

### 1.1 Compressor Engine Yapısı

Önce `/engine/compressor.py` dosyasını oku ve yapıyı anla:

```python
# Temel fonksiyonlar:
def analyze_compressor(compressor_type: str, parameters: dict) -> dict
def get_compressor_types() -> list
def _calculate_exergy_metrics(...)
def _get_benchmark(...)
def _calculate_heat_recovery(...)
def _generate_sankey_data(...)
```

### 1.2 Ortak Interface

Her engine modülü şu fonksiyonları sağlamalı:

```python
def analyze_{equipment}(subtype: str, parameters: dict) -> dict:
    """
    Ana analiz fonksiyonu.
    
    Returns:
        {
            "metrics": {...},
            "benchmark": {...},
            "heat_recovery": {...},  # veya eşdeğeri
            "sankey": {...}
        }
    """

def get_{equipment}_types() -> list:
    """Alt tipleri döndür"""
```

---

## 🔥 BÖLÜM 2: Boiler Engine

### 2.1 Dosya: `/engine/boiler.py`

### 2.2 Referans: `/knowledge/boiler/formulas.md`

### 2.3 Parametreler (Input)

```python
BOILER_PARAMETERS = {
    "fuel_type": str,           # "natural_gas", "fuel_oil", "coal", "biomass", "electric"
    "fuel_flow_rate": float,    # kg/h veya m³/h (doğalgaz için)
    "fuel_lhv": float,          # kJ/kg veya kJ/m³ (Lower Heating Value)
    "steam_flow_rate": float,   # kg/h (buhar debisi)
    "steam_pressure": float,    # bar (buhar basıncı)
    "steam_temperature": float, # °C (buhar sıcaklığı, kızgın buhar için)
    "feedwater_temperature": float,  # °C (besleme suyu sıcaklığı)
    "flue_gas_temperature": float,   # °C (baca gazı sıcaklığı)
    "ambient_temperature": float,    # °C (ortam sıcaklığı, default 25)
    "excess_air": float,        # % (fazla hava, default 15)
    "blowdown_rate": float,     # % (blowdown oranı, default 2)
    "operating_hours": int,     # saat/yıl
    "fuel_price": float,        # €/kWh veya €/m³
}
```

### 2.4 Formüller

```python
# 1. Yakıt Exergy Girişi
Ex_fuel = fuel_flow_rate * fuel_lhv * chemical_exergy_factor
# chemical_exergy_factor: doğalgaz ≈ 1.04, fuel oil ≈ 1.06, kömür ≈ 1.09

# 2. Buhar Exergy Çıkışı (CoolProp kullan)
# Buhar entalpisi ve entropisi
h_steam = CP.PropsSI('H', 'P', P_steam*1e5, 'T', T_steam+273.15, 'Water') / 1000  # kJ/kg
s_steam = CP.PropsSI('S', 'P', P_steam*1e5, 'T', T_steam+273.15, 'Water') / 1000  # kJ/kg·K

# Referans durumu (25°C, 1 atm sıvı su)
h_0 = CP.PropsSI('H', 'P', 101325, 'T', 298.15, 'Water') / 1000  # ≈ 104.9 kJ/kg
s_0 = CP.PropsSI('S', 'P', 101325, 'T', 298.15, 'Water') / 1000  # ≈ 0.367 kJ/kg·K
T_0 = 298.15  # K

# Buhar spesifik exergy
ex_steam = (h_steam - h_0) - T_0 * (s_steam - s_0)  # kJ/kg
Ex_steam = steam_flow_rate * ex_steam / 3600  # kW

# 3. Exergy Verimi
eta_ex = Ex_steam / Ex_fuel * 100  # %

# 4. Kayıp Dağılımı
# - Yanma irreversibility (en büyük): ~25-30% yakıt exergy'si
# - Baca gazı kaybı: Q_flue * (1 - T_0/T_flue)
# - Radyasyon kaybı: ~1-2%
# - Blowdown kaybı: m_blowdown * ex_blowdown

# 5. Enerji Verimi (karşılaştırma için)
eta_energy = (steam_flow_rate * (h_steam - h_feedwater)) / (fuel_flow_rate * fuel_lhv) * 100
```

### 2.5 Benchmark Değerleri

```python
BOILER_BENCHMARKS = {
    "exergy_efficiency": {
        "excellent": 45,
        "good": 35,
        "average": 25,
        "poor": 0
    },
    "energy_efficiency": {
        "excellent": 92,
        "good": 88,
        "average": 82,
        "poor": 0
    },
    "flue_gas_temp": {  # °C - düşük daha iyi
        "excellent": 120,
        "good": 150,
        "average": 200,
        "poor": 250
    }
}
```

### 2.6 Sankey Data

```python
def _generate_boiler_sankey(metrics):
    """
    Kazan Sankey diyagramı
    
    Akış:
    Yakıt Exergy → [Kazan] → Buhar Exergy
                          → Yanma Kaybı
                          → Baca Gazı Kaybı
                          → Radyasyon Kaybı
                          → Blowdown Kaybı
    """
    return {
        "nodes": [
            {"name": "Yakıt Exergy"},
            {"name": "Kazan"},
            {"name": "Buhar Exergy"},
            {"name": "Yanma Kaybı"},
            {"name": "Baca Gazı"},
            {"name": "Radyasyon"},
            {"name": "Blowdown"}
        ],
        "links": [
            {"source": 0, "target": 1, "value": metrics["exergy_input_kW"]},
            {"source": 1, "target": 2, "value": metrics["exergy_output_kW"]},
            {"source": 1, "target": 3, "value": metrics["combustion_loss_kW"]},
            {"source": 1, "target": 4, "value": metrics["flue_gas_loss_kW"]},
            {"source": 1, "target": 5, "value": metrics["radiation_loss_kW"]},
            {"source": 1, "target": 6, "value": metrics["blowdown_loss_kW"]}
        ]
    }
```

---

## ❄️ BÖLÜM 3: Chiller Engine

### 3.1 Dosya: `/engine/chiller.py`

### 3.2 Referans: `/knowledge/chiller/formulas.md`

### 3.3 Parametreler (Input)

```python
CHILLER_PARAMETERS = {
    "chiller_type": str,        # "vapor_compression", "absorption"
    "cooling_capacity_kW": float,   # Soğutma kapasitesi (kW)
    "compressor_power_kW": float,   # Kompresör gücü (kW) - VC için
    "heat_input_kW": float,         # Isı girişi (kW) - absorption için
    "chilled_water_supply": float,  # °C (CHW çıkış, tipik 6-7)
    "chilled_water_return": float,  # °C (CHW dönüş, tipik 12-14)
    "condenser_water_supply": float, # °C (CW giriş, tipik 30-32)
    "condenser_water_return": float, # °C (CW çıkış, tipik 35-37)
    "ambient_temperature": float,   # °C (hava soğutmalı için)
    "evaporator_temp": float,       # °C (evaporatör sıcaklığı, tipik 2-4)
    "condenser_temp": float,        # °C (kondenser sıcaklığı, tipik 38-42)
    "operating_hours": int,
    "electricity_price": float,     # €/kWh
}
```

### 3.4 Formüller

```python
# 1. COP Hesabı
COP = cooling_capacity_kW / compressor_power_kW  # Vapor compression
COP_th = cooling_capacity_kW / heat_input_kW     # Absorption

# 2. Carnot COP (teorik maksimum)
T_evap_K = evaporator_temp + 273.15
T_cond_K = condenser_temp + 273.15
COP_carnot = T_evap_K / (T_cond_K - T_evap_K)

# 3. Soğutma Exergy'si
T_0 = 298.15  # K (25°C referans)
T_cool_K = (chilled_water_supply + 273.15)  # Soğutma sıcaklığı

# Soğutma exergy faktörü (Carnot faktörü)
carnot_factor = (T_0 - T_cool_K) / T_cool_K  # veya abs(1 - T_0/T_cool_K)
Ex_cooling = cooling_capacity_kW * carnot_factor

# 4. Exergy Verimi
# Vapor compression: Ex_cooling / W_compressor
# Absorption: Ex_cooling / Ex_heat_input
#   Ex_heat_input = Q_gen * (1 - T_0/T_gen)

eta_ex_vc = Ex_cooling / compressor_power_kW * 100
eta_ex_abs = Ex_cooling / Ex_heat_input * 100

# 5. Second Law Efficiency
eta_II = COP / COP_carnot * 100
```

### 3.5 Benchmark Değerleri

```python
CHILLER_BENCHMARKS = {
    "cop": {
        "centrifugal": {"excellent": 6.5, "good": 5.5, "average": 4.5, "poor": 0},
        "screw": {"excellent": 5.5, "good": 4.5, "average": 3.5, "poor": 0},
        "scroll": {"excellent": 5.0, "good": 4.0, "average": 3.0, "poor": 0},
        "absorption": {"excellent": 1.2, "good": 1.0, "average": 0.7, "poor": 0}
    },
    "exergy_efficiency": {
        "excellent": 45,
        "good": 35,
        "average": 25,
        "poor": 0
    }
}
```

### 3.6 Sankey Data

```python
def _generate_chiller_sankey(metrics, chiller_type):
    """
    Chiller Sankey diyagramı
    
    VC: Elektrik → [Chiller] → Soğutma Exergy + Kondenser Atık
    Absorption: Isı Exergy → [Chiller] → Soğutma Exergy + Kayıplar
    """
    if chiller_type != "absorption":
        return {
            "nodes": [
                {"name": "Elektrik"},
                {"name": "Chiller"},
                {"name": "Soğutma Exergy"},
                {"name": "Kondenser Atık"},
                {"name": "İç Kayıplar"}
            ],
            "links": [
                {"source": 0, "target": 1, "value": metrics["power_input_kW"]},
                {"source": 1, "target": 2, "value": metrics["exergy_output_kW"]},
                {"source": 1, "target": 3, "value": metrics["condenser_loss_kW"]},
                {"source": 1, "target": 4, "value": metrics["internal_loss_kW"]}
            ]
        }
```

---

## 💧 BÖLÜM 4: Pump Engine

### 4.1 Dosya: `/engine/pump.py`

### 4.2 Referans: `/knowledge/pump/formulas.md`

### 4.3 Parametreler (Input)

```python
PUMP_PARAMETERS = {
    "pump_type": str,           # "centrifugal", "positive_displacement", etc.
    "flow_rate_m3h": float,     # Debi (m³/h)
    "head_m": float,            # Toplam head (m)
    "motor_power_kW": float,    # Motor gücü (kW)
    "fluid_density": float,     # kg/m³ (su için 1000)
    "motor_efficiency": float,  # % (motor verimi, default 90)
    "pump_efficiency": float,   # % (pompa verimi - biliniyorsa)
    "operating_hours": int,
    "electricity_price": float,
    "control_method": str,      # "throttle", "vsd", "bypass", "none"
    "throttle_loss_percent": float,  # Throttle kayıp % (varsa)
}
```

### 4.4 Formüller

```python
# 1. Hidrolik Güç
rho = fluid_density  # kg/m³
g = 9.81  # m/s²
Q = flow_rate_m3h / 3600  # m³/s
H = head_m  # m

P_hydraulic = rho * g * Q * H / 1000  # kW

# 2. Pompa Verimi
eta_pump = P_hydraulic / (motor_power_kW * motor_efficiency/100) * 100

# 3. Wire-to-Water Verimi
eta_system = P_hydraulic / motor_power_kW * 100

# 4. Exergy Analizi
# Pompa için exergy = hidrolik güç (basınç enerjisi)
Ex_input = motor_power_kW  # Elektrik exergy ≈ enerji
Ex_output = P_hydraulic    # Faydalı exergy

eta_ex = Ex_output / Ex_input * 100

# 5. Throttle Kaybı (varsa)
if control_method == "throttle":
    throttle_loss_kW = motor_power_kW * (throttle_loss_percent / 100)
    Ex_throttle = throttle_loss_kW  # Tamamen kayıp

# 6. VSD Tasarrufu Potansiyeli (affinity laws)
# %50 debi → %12.5 güç (teorik)
# Gerçekte %15-20 (verim düşüşü)
```

### 4.5 Benchmark Değerleri

```python
PUMP_BENCHMARKS = {
    "pump_efficiency": {
        "large": {"excellent": 88, "good": 80, "average": 70, "poor": 0},    # >50 kW
        "medium": {"excellent": 82, "good": 75, "average": 65, "poor": 0},   # 10-50 kW
        "small": {"excellent": 75, "good": 65, "average": 55, "poor": 0}     # <10 kW
    },
    "system_efficiency": {
        "excellent": 70,
        "good": 55,
        "average": 40,
        "poor": 0
    },
    "exergy_efficiency": {
        "excellent": 65,
        "good": 50,
        "average": 35,
        "poor": 0
    }
}
```

### 4.6 Sankey Data

```python
def _generate_pump_sankey(metrics):
    """
    Pompa Sankey diyagramı
    
    Elektrik → [Motor] → [Pompa] → Hidrolik Güç
                      → Motor Kaybı
                               → Pompa Kaybı
                                         → Throttle Kaybı (varsa)
    """
    return {
        "nodes": [
            {"name": "Elektrik"},
            {"name": "Motor"},
            {"name": "Pompa"},
            {"name": "Hidrolik Güç"},
            {"name": "Motor Kaybı"},
            {"name": "Pompa Kaybı"},
            {"name": "Throttle Kaybı"}
        ],
        "links": [...]
    }
```

---

## 🔧 BÖLÜM 5: Equipment Registry Güncelleme

### 5.1 `is_engine_ready()` Güncelle

`/api/services/equipment_registry.py` dosyasında:

```python
def is_engine_ready(equipment_type: str) -> bool:
    """Engine modülü hazır mı?"""
    ready_engines = ["compressor", "boiler", "chiller", "pump"]  # Hepsini ekle
    return equipment_type in ready_engines
```

### 5.2 Routes Güncelle

`/api/routes/analysis.py` dosyasında analyze fonksiyonunu güncelle:

```python
@router.post("/analyze")
async def analyze(request: AnalysisRequest):
    equipment_type = request.equipment_type or "compressor"
    subtype = request.subtype or request.compressor_type
    
    if equipment_type == "compressor":
        from engine.compressor import analyze_compressor
        result = analyze_compressor(subtype, request.parameters)
    elif equipment_type == "boiler":
        from engine.boiler import analyze_boiler
        result = analyze_boiler(subtype, request.parameters)
    elif equipment_type == "chiller":
        from engine.chiller import analyze_chiller
        result = analyze_chiller(subtype, request.parameters)
    elif equipment_type == "pump":
        from engine.pump import analyze_pump
        result = analyze_pump(subtype, request.parameters)
    else:
        raise HTTPException(501, "Unsupported equipment type")
    
    return result
```

---

## 🎨 BÖLÜM 6: Frontend Güncelleme

### 6.1 ParameterForm Güncelle

Her ekipman tipi için farklı form alanları gerekiyor. `/frontend/src/components/forms/ParameterForm.jsx` güncelle:

```javascript
const EQUIPMENT_FIELDS = {
  compressor: [
    { id: "power_kW", label: "Elektrik Gücü", unit: "kW", ... },
    { id: "flow_rate_m3_min", label: "Hava Debisi", unit: "m³/min", ... },
    // ... mevcut alanlar
  ],
  boiler: [
    { id: "fuel_type", label: "Yakıt Tipi", type: "select", options: [...] },
    { id: "steam_flow_rate", label: "Buhar Debisi", unit: "kg/h", ... },
    { id: "steam_pressure", label: "Buhar Basıncı", unit: "bar", ... },
    { id: "flue_gas_temperature", label: "Baca Gazı Sıcaklığı", unit: "°C", ... },
    // ...
  ],
  chiller: [
    { id: "cooling_capacity_kW", label: "Soğutma Kapasitesi", unit: "kW", ... },
    { id: "compressor_power_kW", label: "Kompresör Gücü", unit: "kW", ... },
    { id: "chilled_water_supply", label: "CHW Çıkış", unit: "°C", ... },
    // ...
  ],
  pump: [
    { id: "flow_rate_m3h", label: "Debi", unit: "m³/h", ... },
    { id: "head_m", label: "Toplam Head", unit: "m", ... },
    { id: "motor_power_kW", label: "Motor Gücü", unit: "kW", ... },
    // ...
  ]
};
```

### 6.2 EquipmentAnalysis Güncelle

`/frontend/src/pages/EquipmentAnalysis.jsx`:
- "Yakında" mesajını kaldır
- Tüm ekipman tipleri için analiz akışını aktif et

---

## ✅ BÖLÜM 7: Tamamlama Kontrol Listesi

### Engine Modülleri
- [ ] `/engine/boiler.py` oluşturuldu
- [ ] `/engine/chiller.py` oluşturuldu
- [ ] `/engine/pump.py` oluşturuldu
- [ ] Her modül CoolProp kullanıyor (gerekirse)
- [ ] Her modül Sankey verisi üretiyor
- [ ] Her modül benchmark karşılaştırması yapıyor

### Backend
- [ ] `equipment_registry.py` güncellendi (is_engine_ready)
- [ ] `routes/analysis.py` tüm tipler için çalışıyor
- [ ] Yeni testler eklendi

### Frontend
- [ ] ParameterForm tüm ekipman tipleri için alan tanımlıyor
- [ ] EquipmentAnalysis "Yakında" mesajı kaldırıldı
- [ ] Tüm ekipman analizleri çalışıyor

### Test
- [ ] Mevcut testler geçiyor
- [ ] Yeni engine testleri geçiyor
- [ ] Frontend build başarılı

---

## 🚀 Uygulama Sırası

1. **Önce** mevcut `/engine/compressor.py` dosyasını oku ve yapıyı anla
2. **Önce** `/knowledge/{equipment}/formulas.md` dosyalarını oku
3. `engine/boiler.py` oluştur ve test et
4. `engine/chiller.py` oluştur ve test et
5. `engine/pump.py` oluştur ve test et
6. `equipment_registry.py` ve `routes/analysis.py` güncelle
7. Frontend ParameterForm ve EquipmentAnalysis güncelle
8. Tüm testleri çalıştır

---

**Bu brief 3 engine modülü için tek kaynak noktasıdır.**
