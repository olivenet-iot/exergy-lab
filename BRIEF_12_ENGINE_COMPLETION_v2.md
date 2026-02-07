# Brief 12 v2: Engine Completion — heat_exchanger.py, steam_turbine.py, dryer.py

> **Claude Code için:** Bu brief'i oku ve uygula. Hata görürsen düzeltme otonomuna sahipsin.

---

## 🎯 Hedef

Mevcut 4 engine'e (compressor, boiler, chiller, pump) 3 yeni engine ekleyerek **7/7 ekipman operasyonel** hale getirmek. Engine'ler + Sankey + testler + tam entegrasyon.

---

## ⚠️ OTONOM YETKİ

Bu brief'i uygularken:
1. Brief'teki görevleri tamamla
2. Mevcut kodu incele — herhangi bir uyumsuzluk veya hata görürsen **kendi insiyatifinle düzelt**
3. Mevcut pattern'la uyumsuz bir şey varsa mevcut kodu referans al (brief'i değil)
4. Eksik gördüğün edge case, validasyon, test ekle
5. Cross-equipment entegrasyon desenleri ekle/güncelle (factory.py)
6. **Mevcut çalışan 243 testi ASLA bozma** — her değişiklikten sonra `pytest tests/ -v` çalıştır

---

## 📋 Adım 0: ÖNCE Mevcut Kodu Anla

Kod yazmaya başlamadan ÖNCE aşağıdaki dosyaları incele. Brief'teki kodun bu dosyalarla uyumlu olması KRİTİK:

```bash
# 1. Mevcut engine pattern'ı
cat engine/core.py                              # DeadState, ExergyResult yapısı
cat engine/compressor.py | head -80             # Import ve class yapısı
grep -n "to_api_dict\|to_dict" engine/*.py      # Doğru method adı (to_api_dict!)
grep -n "def generate_" engine/*.py             # Sankey fonksiyon isimleri
cat engine/__init__.py                          # Public API export'lar

# 2. Factory & Sankey dispatcher
cat engine/factory.py | grep -n "_ANALYZERS" -A 10
cat engine/sankey.py

# 3. API & Registry
cat api/services/equipment_registry.py
cat api/routes/analysis.py | head -150

# 4. Mevcut test yapısı
head -30 tests/test_engine.py
```

**Bu dosyaları incele ve eğer brief'le çelişen bir yapı görürsen, MEVCUT KODU referans al.**

---

## ⚠️ Önemli Kurallar

1. **Mevcut pattern'ı takip et** — boiler.py/pump.py yapısını referans al
2. **Dataclass pattern:** `XxxInput` → `XxxResult(ExergyResult)` → `analyze_xxx()` → `to_api_dict()` → `generate_xxx_sankey_data()` → `get_xxx_recommendations()`
3. **core.py'deki import'ları kullan:** `DeadState`, `ExergyResult`, `heat_exergy`, `celsius_to_kelvin`, `bar_to_kpa`
4. **CoolProp kullanma** — saf Python, ideal gaz/yaklaşık formüller
5. **Tüm fonksiyonlar kW bazlı** — tutarlılık
6. **Türkçe docstring, İngilizce kod** — mevcut proje standardı
7. **Mevcut testleri bozma** — sadece yeni dosyalar ekle, mevcut dosyaları dikkatli güncelle
8. **Method adı `to_api_dict()`** — `to_dict()` DEĞİL
9. **Her engine'de Sankey fonksiyonu ZORUNLU** — `generate_{type}_sankey_data(result)`

---

## Oluşturulacak / Güncellenecek Dosyalar

```
engine/
├── heat_exchanger.py       🆕  (engine + sankey + recommendations)
├── steam_turbine.py        🆕  (engine + sankey + recommendations)
├── dryer.py                🆕  (engine + sankey + recommendations)
├── __init__.py             📝  (yeni import'lar ekle)
├── factory.py              📝  (_ANALYZERS dict'ine 3 ekipman ekle)
└── sankey.py               📝  (dispatcher'a 3 yeni tip ekle)

api/
├── services/
│   └── equipment_registry.py  📝  (engine_ready: True yap)
└── routes/
    └── analysis.py            📝  (yeni engine'leri dispatcher'a ekle)

tests/
├── test_heat_exchanger.py  🆕
├── test_steam_turbine.py   🆕
└── test_dryer.py           🆕
```

---

## 📦 Engine 1: heat_exchanger.py

### Termodinamik Temeli

```
Sıcak taraf exergy değişimi:
  ΔEx_hot = ṁ_h × cp_h × [(T_h_in - T_h_out) - T₀ × ln(T_h_in / T_h_out)]

Soğuk taraf exergy değişimi:
  ΔEx_cold = ṁ_c × cp_c × [(T_c_out - T_c_in) - T₀ × ln(T_c_out / T_c_in)]

Exergy yıkımı:
  Ex_destroyed = ΔEx_hot - ΔEx_cold

Exergy verimi:
  η_ex = ΔEx_cold / ΔEx_hot

Bejan sayısı (entropi ayrıştırma):
  S_gen_ΔT = Q / T_lm_cold - Q / T_lm_hot
  S_gen_ΔP = ṁ_h × R × ΔP/P_avg (hot) + ṁ_c × R × ΔP/P_avg (cold)
  Be = S_gen_ΔT / (S_gen_ΔT + S_gen_ΔP)
```

### Kod

```python
"""
ExergyLab - Heat Exchanger Exergy Analysis

Isı eşanjörü exergy hesaplamaları.
Shell & tube, plakalı, finned tube, ekonomizer tipleri için.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict
import math

from .core import (
    DeadState, ExergyResult,
    celsius_to_kelvin, bar_to_kpa,
    heat_exergy, CP_AIR, R_AIR
)


# Akışkan özgül ısıları (kJ/kg·K)
FLUID_CP = {
    'water': 4.18,
    'steam': 2.01,
    'air': 1.005,
    'flue_gas': 1.10,
    'thermal_oil': 2.10,
    'glycol_30': 3.70,
    'glycol_50': 3.30,
}

# Akışkan R değerleri (kJ/kg·K) — basınç düşüşü entropi hesabı için
FLUID_R = {
    'air': 0.287,
    'flue_gas': 0.287,
    'steam': 0.4615,
    'water': 0.0,
    'thermal_oil': 0.0,
    'glycol_30': 0.0,
    'glycol_50': 0.0,
}


@dataclass
class HeatExchangerInput:
    """Isı eşanjörü analizi için giriş verileri"""

    # Sıcak taraf
    hot_fluid: str = 'water'
    hot_inlet_temp_C: float = 90.0
    hot_outlet_temp_C: float = 70.0
    hot_mass_flow_kg_s: float = 2.0
    hot_pressure_drop_kPa: float = 10.0

    # Soğuk taraf
    cold_fluid: str = 'water'
    cold_inlet_temp_C: float = 20.0
    cold_outlet_temp_C: float = 50.0
    cold_mass_flow_kg_s: float = 1.5
    cold_pressure_drop_kPa: float = 15.0

    # Opsiyonel
    heat_duty_kW: Optional[float] = None
    ambient_temp_C: float = 25.0

    # Operasyonel
    operating_hours: float = 6000
    electricity_price_eur_kwh: float = 0.10
    fuel_price_eur_kwh: float = 0.06

    # Ekipman bilgisi
    hx_type: str = 'shell_tube'    # shell_tube, plate, finned_tube, economizer, air_cooled
    brand: Optional[str] = None
    model: Optional[str] = None
    age_years: Optional[int] = None
    design_heat_duty_kW: Optional[float] = None

    def __post_init__(self):
        """Varsayılan değerleri ayarla ve doğrula"""
        if self.heat_duty_kW is None:
            cp_h = FLUID_CP.get(self.hot_fluid, 4.18)
            self.heat_duty_kW = abs(
                self.hot_mass_flow_kg_s * cp_h * (self.hot_inlet_temp_C - self.hot_outlet_temp_C)
            )


@dataclass
class HeatExchangerResult(ExergyResult):
    """Isı eşanjörü analizi sonuçları"""

    heat_duty_kW: Optional[float] = None
    lmtd_K: Optional[float] = None
    effectiveness: Optional[float] = None
    hot_exergy_decrease_kW: Optional[float] = None
    cold_exergy_increase_kW: Optional[float] = None

    # Bejan analizi
    entropy_gen_total_kW_K: Optional[float] = None
    entropy_gen_heat_transfer_kW_K: Optional[float] = None
    entropy_gen_pressure_drop_kW_K: Optional[float] = None
    bejan_number: Optional[float] = None

    # Benchmark
    benchmark_comparison: Optional[str] = None
    fouling_indicator: Optional[str] = None

    def to_api_dict(self) -> dict:
        """API uyumlu dict çıktısı — mevcut engine pattern'ı ile tutarlı"""
        base = super().to_api_dict()
        base.update({
            'heat_duty_kW': round(self.heat_duty_kW, 2) if self.heat_duty_kW else None,
            'lmtd_K': round(self.lmtd_K, 2) if self.lmtd_K else None,
            'effectiveness': round(self.effectiveness, 3) if self.effectiveness else None,
            'hot_exergy_decrease_kW': round(self.hot_exergy_decrease_kW, 2) if self.hot_exergy_decrease_kW else None,
            'cold_exergy_increase_kW': round(self.cold_exergy_increase_kW, 2) if self.cold_exergy_increase_kW else None,
            'entropy_gen_total_kW_K': round(self.entropy_gen_total_kW_K, 4) if self.entropy_gen_total_kW_K else None,
            'entropy_gen_heat_transfer_kW_K': round(self.entropy_gen_heat_transfer_kW_K, 4) if self.entropy_gen_heat_transfer_kW_K else None,
            'entropy_gen_pressure_drop_kW_K': round(self.entropy_gen_pressure_drop_kW_K, 4) if self.entropy_gen_pressure_drop_kW_K else None,
            'bejan_number': round(self.bejan_number, 3) if self.bejan_number else None,
            'benchmark_comparison': self.benchmark_comparison,
            'fouling_indicator': self.fouling_indicator,
        })
        return base


def analyze_heat_exchanger(input_data: HeatExchangerInput, dead_state: DeadState = None) -> HeatExchangerResult:
    """
    Isı eşanjörü exergy analizi yapar.

    Args:
        input_data: HX giriş verileri
        dead_state: Dead state koşulları (opsiyonel)

    Returns:
        HeatExchangerResult: Analiz sonuçları
    """
    if dead_state is None:
        dead_state = DeadState(T0=celsius_to_kelvin(input_data.ambient_temp_C))

    T0 = dead_state.T0

    # Sıcaklıkları Kelvin'e çevir
    T_h_in = celsius_to_kelvin(input_data.hot_inlet_temp_C)
    T_h_out = celsius_to_kelvin(input_data.hot_outlet_temp_C)
    T_c_in = celsius_to_kelvin(input_data.cold_inlet_temp_C)
    T_c_out = celsius_to_kelvin(input_data.cold_outlet_temp_C)

    # Cp değerleri
    cp_h = FLUID_CP.get(input_data.hot_fluid, 4.18)
    cp_c = FLUID_CP.get(input_data.cold_fluid, 4.18)
    R_h = FLUID_R.get(input_data.hot_fluid, 0.0)
    R_c = FLUID_R.get(input_data.cold_fluid, 0.0)

    m_h = input_data.hot_mass_flow_kg_s
    m_c = input_data.cold_mass_flow_kg_s

    Q = input_data.heat_duty_kW

    # --- LMTD Hesabı (karşı akış varsayımı) ---
    dT1 = T_h_in - T_c_out
    dT2 = T_h_out - T_c_in
    if dT1 > 0 and dT2 > 0 and abs(dT1 - dT2) > 0.01:
        lmtd = (dT1 - dT2) / math.log(dT1 / dT2)
    elif dT1 > 0 and dT2 > 0:
        lmtd = (dT1 + dT2) / 2
    else:
        lmtd = max(abs(dT1), abs(dT2))

    # --- Effectiveness (ε) ---
    C_h = m_h * cp_h
    C_c = m_c * cp_c
    C_min = min(C_h, C_c)
    Q_max = C_min * (T_h_in - T_c_in)
    effectiveness = Q / Q_max if Q_max > 0 else 0

    # --- Exergy Hesapları ---
    delta_ex_hot = m_h * cp_h * (
        (T_h_in - T_h_out) - T0 * math.log(T_h_in / T_h_out)
    )

    delta_ex_cold = m_c * cp_c * (
        (T_c_out - T_c_in) - T0 * math.log(T_c_out / T_c_in)
    )

    Ex_in = delta_ex_hot
    Ex_out = delta_ex_cold

    Ex_destroyed = Ex_in - Ex_out
    if Ex_destroyed < 0:
        Ex_destroyed = 0

    eta_ex = (Ex_out / Ex_in * 100) if Ex_in > 0 else 0

    # --- Entropi Üretimi Ayrıştırma (Bejan) ---
    T_lm_hot = (T_h_in - T_h_out) / math.log(T_h_in / T_h_out) if abs(T_h_in - T_h_out) > 0.1 else T_h_in
    T_lm_cold = (T_c_out - T_c_in) / math.log(T_c_out / T_c_in) if abs(T_c_out - T_c_in) > 0.1 else T_c_in

    S_gen_heat = Q / T_lm_cold - Q / T_lm_hot
    if S_gen_heat < 0:
        S_gen_heat = 0

    S_gen_pressure = 0
    if R_h > 0 and input_data.hot_pressure_drop_kPa > 0:
        P_avg_h = dead_state.P0
        S_gen_pressure += m_h * R_h * input_data.hot_pressure_drop_kPa / P_avg_h
    if R_c > 0 and input_data.cold_pressure_drop_kPa > 0:
        P_avg_c = dead_state.P0
        S_gen_pressure += m_c * R_c * input_data.cold_pressure_drop_kPa / P_avg_c

    S_gen_total = S_gen_heat + S_gen_pressure
    bejan = S_gen_heat / S_gen_total if S_gen_total > 0 else 1.0

    # --- Yıllık Etki ---
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.fuel_price_eur_kwh

    # --- Benchmark ---
    benchmark = _get_hx_benchmark(eta_ex, input_data.hx_type)

    # --- Fouling indicator ---
    fouling = None
    if input_data.design_heat_duty_kW and input_data.design_heat_duty_kW > 0:
        performance_ratio = Q / input_data.design_heat_duty_kW
        if performance_ratio < 0.70:
            fouling = 'severe'
        elif performance_ratio < 0.85:
            fouling = 'moderate'
        elif performance_ratio < 0.95:
            fouling = 'light'
        else:
            fouling = 'clean'

    return HeatExchangerResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        recoverable_heat_kW=None,
        heat_duty_kW=Q,
        lmtd_K=lmtd,
        effectiveness=effectiveness,
        hot_exergy_decrease_kW=delta_ex_hot,
        cold_exergy_increase_kW=delta_ex_cold,
        entropy_gen_total_kW_K=S_gen_total,
        entropy_gen_heat_transfer_kW_K=S_gen_heat,
        entropy_gen_pressure_drop_kW_K=S_gen_pressure,
        bejan_number=bejan,
        benchmark_comparison=benchmark,
        fouling_indicator=fouling,
    )


def _get_hx_benchmark(eta_ex: float, hx_type: str) -> str:
    """Exergy verimine göre benchmark karşılaştırması"""
    benchmarks = {
        'shell_tube':  {'poor': 25, 'average': 40, 'good': 55, 'excellent': 65},
        'plate':       {'poor': 30, 'average': 50, 'good': 65, 'excellent': 75},
        'finned_tube': {'poor': 20, 'average': 35, 'good': 50, 'excellent': 60},
        'economizer':  {'poor': 25, 'average': 40, 'good': 55, 'excellent': 65},
        'air_cooled':  {'poor': 15, 'average': 30, 'good': 45, 'excellent': 55},
    }
    thresholds = benchmarks.get(hx_type, benchmarks['shell_tube'])

    if eta_ex < thresholds['poor']:
        return 'poor'
    elif eta_ex < thresholds['average']:
        return 'below_average'
    elif eta_ex < thresholds['good']:
        return 'average'
    elif eta_ex < thresholds['excellent']:
        return 'good'
    else:
        return 'excellent'


def generate_heat_exchanger_sankey_data(result: HeatExchangerResult) -> dict:
    """
    Isı eşanjörü Sankey diyagram verisi üretir.

    Akış: Sıcak Taraf Exergy → [Soğuk Taraf Kazanımı, ΔT Yıkımı, ΔP Yıkımı]
    """
    Ex_in = result.exergy_in_kW or 0
    Ex_out = result.exergy_out_kW or 0
    Ex_destroyed = result.exergy_destroyed_kW or 0

    # Entropi ayrıştırmasına göre yıkımı böl
    S_heat = result.entropy_gen_heat_transfer_kW_K or 0
    S_pressure = result.entropy_gen_pressure_drop_kW_K or 0
    S_total = S_heat + S_pressure

    if S_total > 0 and Ex_destroyed > 0:
        destruction_heat_transfer = Ex_destroyed * (S_heat / S_total)
        destruction_pressure_drop = Ex_destroyed * (S_pressure / S_total)
    else:
        destruction_heat_transfer = Ex_destroyed
        destruction_pressure_drop = 0

    # Normalize — toplam çıkış = toplam giriş
    total_out = Ex_out + destruction_heat_transfer + destruction_pressure_drop
    if total_out > 0 and abs(total_out - Ex_in) > 0.1:
        scale = Ex_in / total_out
        Ex_out *= scale
        destruction_heat_transfer *= scale
        destruction_pressure_drop *= scale

    nodes = [
        'Sıcak Taraf Exergy',       # 0
        'Soğuk Taraf Kazanımı',      # 1
        'Isı Transferi Kayıp',       # 2
        'Basınç Düşüşü Kayıp',      # 3
    ]

    links = []
    if Ex_out > 0:
        links.append({'source': 0, 'target': 1, 'value': round(Ex_out, 2)})
    if destruction_heat_transfer > 0.01:
        links.append({'source': 0, 'target': 2, 'value': round(destruction_heat_transfer, 2)})
    if destruction_pressure_drop > 0.01:
        links.append({'source': 0, 'target': 3, 'value': round(destruction_pressure_drop, 2)})

    # Basınç düşüşü sıfırsa node'u çıkar
    if destruction_pressure_drop <= 0.01:
        nodes = nodes[:3]

    return {
        'nodes': nodes,
        'links': links,
        'title': 'Isı Eşanjörü Exergy Akışı',
    }


def get_heat_exchanger_recommendations(result: HeatExchangerResult, input_data: HeatExchangerInput) -> list:
    """Analiz sonuçlarına göre iyileştirme önerileri"""
    recommendations = []

    # 1. Fouling — temizlik önerisi
    if result.fouling_indicator in ['severe', 'moderate']:
        savings_pct = 0.15 if result.fouling_indicator == 'severe' else 0.08
        savings = result.annual_loss_EUR * savings_pct if result.annual_loss_EUR else 0
        investment = 2000 if result.fouling_indicator == 'severe' else 1000
        recommendations.append({
            'type': 'cleaning',
            'title': 'Eşanjör Temizliği / Fouling Giderme',
            'description': f'Performans düşüşü tespit edildi ({result.fouling_indicator}). '
                          f'Kimyasal veya mekanik temizlik önerilir.',
            'investment_eur': investment,
            'savings_eur_year': savings,
            'payback_years': investment / savings if savings > 0 else float('inf'),
            'priority': 'high' if result.fouling_indicator == 'severe' else 'medium',
        })

    # 2. Yüksek ΔT — ek ısı geri kazanım
    if input_data.hot_outlet_temp_C > input_data.cold_inlet_temp_C + 30:
        potential_kW = input_data.hot_mass_flow_kg_s * FLUID_CP.get(input_data.hot_fluid, 4.18) * (
            input_data.hot_outlet_temp_C - input_data.cold_inlet_temp_C - 10
        ) * 0.5
        potential_eur = potential_kW * input_data.operating_hours * input_data.fuel_price_eur_kwh
        recommendations.append({
            'type': 'additional_recovery',
            'title': 'Ek Isı Geri Kazanımı',
            'description': f'Sıcak çıkış hâlâ yüksek ({input_data.hot_outlet_temp_C}°C). '
                          f'İkinci kademe eşanjör veya ekonomizer eklenebilir.',
            'investment_eur': 8000,
            'savings_eur_year': potential_eur,
            'payback_years': 8000 / potential_eur if potential_eur > 0 else float('inf'),
            'priority': 'medium',
        })

    # 3. Bejan > 0.9 — ΔT baskın, alan artırma öner
    if result.bejan_number and result.bejan_number > 0.9:
        savings = result.annual_loss_EUR * 0.20 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'area_increase',
            'title': 'Isı Transfer Alanını Artır',
            'description': 'Entropi üretiminin büyük kısmı sıcaklık farkından. '
                          'Daha büyük alan ile ΔT düşürülebilir.',
            'investment_eur': 15000,
            'savings_eur_year': savings,
            'payback_years': 15000 / savings if savings > 0 else float('inf'),
            'priority': 'low',
        })

    # 4. Düşük effectiveness
    if result.effectiveness and result.effectiveness < 0.5:
        savings = result.annual_loss_EUR * 0.30 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'upgrade',
            'title': 'Eşanjör Tip Değişikliği',
            'description': f'Etkinlik düşük (ε={result.effectiveness:.2f}). '
                          f'Plakalı eşanjöre geçiş düşünülebilir.',
            'investment_eur': 12000,
            'savings_eur_year': savings,
            'payback_years': 12000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    return recommendations
```

---

## 📦 Engine 2: steam_turbine.py

### Termodinamik Temeli

```
Giren exergy (buhar):
  Ex_in = ṁ × [cp × ((T_in - T₀) - T₀ × ln(T_in/T₀)) + R × T₀ × ln(P_in/P₀)]

İş çıkışı:
  W_shaft = ṁ × cp × (T_in - T_out)

Çıkan exergy (egzoz):
  Ex_out = ṁ × [cp × ((T_out - T₀) - T₀ × ln(T_out/T₀)) + R × T₀ × ln(P_out/P₀)]

Exergy yıkımı:
  Ex_destroyed = Ex_in - W_shaft - Ex_out

Exergy verimi:
  η_ex = W_shaft / (Ex_in - Ex_out)

CHP: Ex_useful = W_shaft + Ex_heat_recovered
```

### Kod

```python
"""
ExergyLab - Steam Turbine / CHP Exergy Analysis

Buhar türbini ve kojenerasyon sistemi exergy hesaplamaları.
Condensing, backpressure, extraction ve CHP tipleri için.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict
import math

from .core import (
    DeadState, ExergyResult,
    celsius_to_kelvin, bar_to_kpa,
    heat_exergy
)

# Buhar özellikleri (basitleştirilmiş)
CP_STEAM_SUPERHEATED = 2.01     # kJ/kg·K
CP_STEAM_SATURATED = 2.30       # kJ/kg·K
CP_WATER = 4.18                 # kJ/kg·K
R_STEAM = 0.4615                # kJ/kg·K
H_FG_100C = 2257.0              # kJ/kg

# Basınca göre doyma sıcaklıkları [bar → °C]
SATURATION_TEMP = {
    0.05: 32.9,   0.1: 45.8,    0.2: 60.1,   0.5: 81.3,
    1.0: 99.6,    1.5: 111.4,   2.0: 120.2,  3.0: 133.5,
    4.0: 143.6,   5.0: 151.8,   6.0: 158.8,  8.0: 170.4,
    10.0: 179.9,  15.0: 198.3,  20.0: 212.4, 25.0: 224.0,
    30.0: 233.9,  40.0: 250.4,  50.0: 263.9, 60.0: 275.6,
    80.0: 295.0,  100.0: 311.0,
}


def _get_saturation_temp_C(P_bar: float) -> float:
    """Basınca göre doyma sıcaklığı (lineer interpolasyon)"""
    pressures = sorted(SATURATION_TEMP.keys())

    if P_bar <= pressures[0]:
        return SATURATION_TEMP[pressures[0]]
    if P_bar >= pressures[-1]:
        return SATURATION_TEMP[pressures[-1]]

    for i in range(len(pressures) - 1):
        if pressures[i] <= P_bar <= pressures[i + 1]:
            p1, p2 = pressures[i], pressures[i + 1]
            t1, t2 = SATURATION_TEMP[p1], SATURATION_TEMP[p2]
            return t1 + (t2 - t1) * (P_bar - p1) / (p2 - p1)

    return 100.0


@dataclass
class SteamTurbineInput:
    """Buhar türbini analizi için giriş verileri"""

    # Giriş buharı
    inlet_temp_C: float = 400.0
    inlet_pressure_bar: float = 40.0
    mass_flow_kg_s: float = 5.0

    # Çıkış koşulları
    outlet_pressure_bar: float = 0.1
    outlet_temp_C: Optional[float] = None

    # Türbin özellikleri
    isentropic_efficiency: float = 0.80
    mechanical_efficiency: float = 0.98
    generator_efficiency: float = 0.97

    # CHP parametreleri
    is_chp: bool = False
    heat_recovery_temp_C: Optional[float] = None
    heat_recovery_fraction: float = 0.60

    # Ortam
    ambient_temp_C: float = 25.0

    # Operasyonel
    operating_hours: float = 7000
    electricity_price_eur_kwh: float = 0.10
    fuel_price_eur_kwh: float = 0.04

    # Ekipman
    turbine_type: str = 'backpressure'   # condensing, backpressure, extraction
    brand: Optional[str] = None
    model: Optional[str] = None
    age_years: Optional[int] = None
    rated_power_MW: Optional[float] = None

    def __post_init__(self):
        """Çıkış sıcaklığını hesapla (verilmemişse)"""
        if self.outlet_temp_C is None:
            T_sat_out = _get_saturation_temp_C(self.outlet_pressure_bar)

            if self.turbine_type == 'condensing':
                self.outlet_temp_C = T_sat_out
            elif self.turbine_type == 'backpressure':
                T_in_K = self.inlet_temp_C + 273.15
                gamma = 1.3
                T_out_isentropic = T_in_K * (self.outlet_pressure_bar / self.inlet_pressure_bar) ** ((gamma - 1) / gamma)
                T_out_actual = T_in_K - self.isentropic_efficiency * (T_in_K - T_out_isentropic)
                self.outlet_temp_C = max(T_out_actual - 273.15, T_sat_out + 5)
            else:
                T_in_K = self.inlet_temp_C + 273.15
                gamma = 1.3
                T_out_isentropic = T_in_K * (self.outlet_pressure_bar / self.inlet_pressure_bar) ** ((gamma - 1) / gamma)
                T_out_actual = T_in_K - self.isentropic_efficiency * (T_in_K - T_out_isentropic)
                self.outlet_temp_C = max(T_out_actual - 273.15, T_sat_out)


@dataclass
class SteamTurbineResult(ExergyResult):
    """Buhar türbini analizi sonuçları"""

    shaft_power_kW: Optional[float] = None
    electrical_power_kW: Optional[float] = None
    exhaust_exergy_kW: Optional[float] = None
    isentropic_efficiency_actual: Optional[float] = None

    # CHP
    heat_recovered_kW: Optional[float] = None
    heat_recovered_exergy_kW: Optional[float] = None
    total_useful_exergy_kW: Optional[float] = None
    chp_exergy_efficiency_pct: Optional[float] = None

    # Yıllık
    annual_electricity_MWh: Optional[float] = None
    annual_electricity_revenue_EUR: Optional[float] = None

    # Benchmark
    benchmark_comparison: Optional[str] = None

    def to_api_dict(self) -> dict:
        """API uyumlu dict çıktısı"""
        base = super().to_api_dict()
        base.update({
            'shaft_power_kW': round(self.shaft_power_kW, 2) if self.shaft_power_kW else None,
            'electrical_power_kW': round(self.electrical_power_kW, 2) if self.electrical_power_kW else None,
            'exhaust_exergy_kW': round(self.exhaust_exergy_kW, 2) if self.exhaust_exergy_kW else None,
            'isentropic_efficiency_actual': round(self.isentropic_efficiency_actual, 3) if self.isentropic_efficiency_actual else None,
            'heat_recovered_kW': round(self.heat_recovered_kW, 2) if self.heat_recovered_kW else None,
            'heat_recovered_exergy_kW': round(self.heat_recovered_exergy_kW, 2) if self.heat_recovered_exergy_kW else None,
            'total_useful_exergy_kW': round(self.total_useful_exergy_kW, 2) if self.total_useful_exergy_kW else None,
            'chp_exergy_efficiency_pct': round(self.chp_exergy_efficiency_pct, 1) if self.chp_exergy_efficiency_pct else None,
            'annual_electricity_MWh': round(self.annual_electricity_MWh, 1) if self.annual_electricity_MWh else None,
            'annual_electricity_revenue_EUR': round(self.annual_electricity_revenue_EUR, 0) if self.annual_electricity_revenue_EUR else None,
            'benchmark_comparison': self.benchmark_comparison,
        })
        return base


def analyze_steam_turbine(input_data: SteamTurbineInput, dead_state: DeadState = None) -> SteamTurbineResult:
    """
    Buhar türbini exergy analizi yapar.

    Args:
        input_data: Türbin giriş verileri
        dead_state: Dead state koşulları (opsiyonel)

    Returns:
        SteamTurbineResult: Analiz sonuçları
    """
    if dead_state is None:
        dead_state = DeadState(T0=celsius_to_kelvin(input_data.ambient_temp_C))

    T0 = dead_state.T0
    P0_bar = dead_state.P0 / 100  # kPa → bar

    T_in = celsius_to_kelvin(input_data.inlet_temp_C)
    T_out = celsius_to_kelvin(input_data.outlet_temp_C)
    m = input_data.mass_flow_kg_s

    # Uygun cp seçimi
    T_sat_in = celsius_to_kelvin(_get_saturation_temp_C(input_data.inlet_pressure_bar))
    if T_in > T_sat_in + 20:
        cp = CP_STEAM_SUPERHEATED
    else:
        cp = CP_STEAM_SATURATED

    # --- Giren Exergy ---
    ex_in_thermal = cp * ((T_in - T0) - T0 * math.log(T_in / T0))
    ex_in_pressure = R_STEAM * T0 * math.log(input_data.inlet_pressure_bar / P0_bar)
    Ex_in = m * (ex_in_thermal + ex_in_pressure)

    # --- Çıkan Exergy (egzoz) ---
    ex_out_thermal = cp * ((T_out - T0) - T0 * math.log(max(T_out, T0 + 1) / T0))
    ex_out_pressure = R_STEAM * T0 * math.log(max(input_data.outlet_pressure_bar, 0.01) / P0_bar)
    Ex_out_flow = m * (ex_out_thermal + max(ex_out_pressure, 0))

    # --- İş Çıkışı ---
    W_shaft = m * cp * (T_in - T_out)
    W_shaft = max(W_shaft, 0)

    W_electrical = W_shaft * input_data.mechanical_efficiency * input_data.generator_efficiency

    # --- Exergy Yıkımı ---
    Ex_destroyed = Ex_in - W_shaft - Ex_out_flow
    Ex_destroyed = max(Ex_destroyed, 0)

    # --- Exergy Verimi ---
    if Ex_in > Ex_out_flow:
        eta_ex = (W_shaft / (Ex_in - Ex_out_flow)) * 100
    else:
        eta_ex = 0
    eta_ex = min(eta_ex, 100)

    # --- CHP Hesabı ---
    heat_recovered = 0
    heat_recovered_exergy = 0
    total_useful_exergy = W_shaft
    chp_eta_ex = eta_ex

    if input_data.is_chp:
        T_recovery = celsius_to_kelvin(input_data.heat_recovery_temp_C) if input_data.heat_recovery_temp_C else T_out
        Q_exhaust = m * cp * (T_out - T0)
        heat_recovered = Q_exhaust * input_data.heat_recovery_fraction
        heat_recovered = max(heat_recovered, 0)

        if heat_recovered > 0 and T_recovery > T0:
            T_avg_recovery = (T_recovery + T0) / 2
            heat_recovered_exergy = heat_recovered * (1 - T0 / T_avg_recovery)
            heat_recovered_exergy = max(heat_recovered_exergy, 0)

        total_useful_exergy = W_shaft + heat_recovered_exergy
        if Ex_in > 0:
            chp_eta_ex = (total_useful_exergy / Ex_in) * 100
            chp_eta_ex = min(chp_eta_ex, 100)

    # --- Yıllık ---
    annual_elec_MWh = W_electrical * input_data.operating_hours / 1000
    annual_elec_revenue = annual_elec_MWh * 1000 * input_data.electricity_price_eur_kwh
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.fuel_price_eur_kwh

    # --- Benchmark ---
    benchmark = _get_turbine_benchmark(eta_ex, input_data.turbine_type)

    return SteamTurbineResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out_flow,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        recoverable_heat_kW=heat_recovered if input_data.is_chp else None,
        shaft_power_kW=W_shaft,
        electrical_power_kW=W_electrical,
        exhaust_exergy_kW=Ex_out_flow,
        isentropic_efficiency_actual=input_data.isentropic_efficiency,
        heat_recovered_kW=heat_recovered if input_data.is_chp else None,
        heat_recovered_exergy_kW=heat_recovered_exergy if input_data.is_chp else None,
        total_useful_exergy_kW=total_useful_exergy,
        chp_exergy_efficiency_pct=chp_eta_ex if input_data.is_chp else None,
        annual_electricity_MWh=annual_elec_MWh,
        annual_electricity_revenue_EUR=annual_elec_revenue,
        benchmark_comparison=benchmark,
    )


def _get_turbine_benchmark(eta_ex: float, turbine_type: str) -> str:
    """Exergy verimine göre benchmark karşılaştırması"""
    benchmarks = {
        'condensing':   {'poor': 50, 'average': 65, 'good': 75, 'excellent': 82},
        'backpressure': {'poor': 40, 'average': 55, 'good': 70, 'excellent': 80},
        'extraction':   {'poor': 45, 'average': 60, 'good': 72, 'excellent': 80},
    }
    thresholds = benchmarks.get(turbine_type, benchmarks['backpressure'])

    if eta_ex < thresholds['poor']:
        return 'poor'
    elif eta_ex < thresholds['average']:
        return 'below_average'
    elif eta_ex < thresholds['good']:
        return 'average'
    elif eta_ex < thresholds['excellent']:
        return 'good'
    else:
        return 'excellent'


def generate_steam_turbine_sankey_data(result: SteamTurbineResult) -> dict:
    """
    Buhar türbini Sankey diyagram verisi üretir.

    Normal mod: Buhar Exergy → [Shaft Work, Egzoz Exergy, Yıkım]
    CHP modu:   Buhar Exergy → [Elektrik, Isı Geri Kazanım, Egzoz, Yıkım]
    """
    Ex_in = result.exergy_in_kW or 0
    W_shaft = result.shaft_power_kW or 0
    Ex_exhaust = result.exhaust_exergy_kW or 0
    Ex_destroyed = result.exergy_destroyed_kW or 0

    is_chp = result.heat_recovered_kW is not None and result.heat_recovered_kW > 0

    # Normalize
    total_out = W_shaft + Ex_exhaust + Ex_destroyed
    if total_out > 0 and abs(total_out - Ex_in) > 0.1:
        scale = Ex_in / total_out
        W_shaft *= scale
        Ex_exhaust *= scale
        Ex_destroyed *= scale

    if is_chp:
        W_elec = result.electrical_power_kW or 0
        heat_rec_ex = result.heat_recovered_exergy_kW or 0

        nodes = [
            'Buhar Exergy',          # 0
            'Elektrik Üretimi',      # 1
            'Isı Geri Kazanım',      # 2
            'Egzoz Exergy',          # 3
            'Exergy Yıkımı',         # 4
        ]
        links = []
        if W_elec > 0:
            links.append({'source': 0, 'target': 1, 'value': round(W_elec, 2)})
        if heat_rec_ex > 0:
            links.append({'source': 0, 'target': 2, 'value': round(heat_rec_ex, 2)})
        remaining_exhaust = max(Ex_exhaust - heat_rec_ex, 0)
        if remaining_exhaust > 0:
            links.append({'source': 0, 'target': 3, 'value': round(remaining_exhaust, 2)})
        if Ex_destroyed > 0:
            links.append({'source': 0, 'target': 4, 'value': round(Ex_destroyed, 2)})
    else:
        nodes = [
            'Buhar Exergy',     # 0
            'Shaft Work',       # 1
            'Egzoz Exergy',     # 2
            'Exergy Yıkımı',    # 3
        ]
        links = []
        if W_shaft > 0:
            links.append({'source': 0, 'target': 1, 'value': round(W_shaft, 2)})
        if Ex_exhaust > 0:
            links.append({'source': 0, 'target': 2, 'value': round(Ex_exhaust, 2)})
        if Ex_destroyed > 0:
            links.append({'source': 0, 'target': 3, 'value': round(Ex_destroyed, 2)})

    return {
        'nodes': nodes,
        'links': links,
        'title': 'Buhar Türbini Exergy Akışı' + (' (CHP)' if is_chp else ''),
    }


def get_steam_turbine_recommendations(result: SteamTurbineResult, input_data: SteamTurbineInput) -> list:
    """Analiz sonuçlarına göre iyileştirme önerileri"""
    recommendations = []

    # 1. CHP değilse ve egzoz exergy yüksekse → CHP öner
    if not input_data.is_chp and result.exhaust_exergy_kW and result.exhaust_exergy_kW > 100:
        potential_heat = result.exhaust_exergy_kW * 0.6
        savings = potential_heat * input_data.operating_hours * input_data.fuel_price_eur_kwh
        recommendations.append({
            'type': 'chp_conversion',
            'title': 'Kojenerasyon (CHP) Dönüşümü',
            'description': f'Egzoz buharında {result.exhaust_exergy_kW:.0f} kW exergy mevcut. '
                          f'CHP ile ısı geri kazanımı önerilir.',
            'investment_eur': 50000,
            'savings_eur_year': savings,
            'payback_years': 50000 / savings if savings > 0 else float('inf'),
            'priority': 'high' if savings > 20000 else 'medium',
        })

    # 2. Düşük izentropik verim → bakım
    if input_data.isentropic_efficiency < 0.75:
        savings = result.annual_loss_EUR * 0.15 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'overhaul',
            'title': 'Türbin Revizyonu',
            'description': f'İzentropik verim düşük ({input_data.isentropic_efficiency:.0%}). '
                          f'Kanat erozyonu veya sızdırma olabilir.',
            'investment_eur': 30000,
            'savings_eur_year': savings,
            'payback_years': 30000 / savings if savings > 0 else float('inf'),
            'priority': 'high',
        })

    # 3. Düşük superheat → kızgınlık artırma
    T_sat_in = _get_saturation_temp_C(input_data.inlet_pressure_bar)
    superheat = input_data.inlet_temp_C - T_sat_in
    if superheat < 50:
        savings = result.annual_electricity_revenue_EUR * 0.05 if result.annual_electricity_revenue_EUR else 0
        recommendations.append({
            'type': 'superheat_increase',
            'title': 'Buhar Kızgınlığını Artır',
            'description': f'Kızgınlık sadece {superheat:.0f}°C. '
                          f'Daha yüksek kızgınlık ile türbin verimi artar.',
            'investment_eur': 20000,
            'savings_eur_year': savings,
            'payback_years': 20000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # 4. Backpressure — basınç optimizasyonu
    if input_data.turbine_type == 'backpressure' and input_data.outlet_pressure_bar > 5.0:
        savings = result.annual_electricity_revenue_EUR * 0.08 if result.annual_electricity_revenue_EUR else 0
        recommendations.append({
            'type': 'backpressure_optimization',
            'title': 'Karşı Basınç Optimizasyonu',
            'description': f'Çıkış basıncı {input_data.outlet_pressure_bar} bar. '
                          f'Proses gereksinimlerine göre düşürme imkanı araştırılmalı.',
            'investment_eur': 5000,
            'savings_eur_year': savings,
            'payback_years': 5000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    return recommendations
```

---

## 📦 Engine 3: dryer.py

### Termodinamik Temeli

```
Su buharlaştırma: Q_evap = ṁ_water × h_fg
Giren exergy:    Ex_in = Q_fuel × exergy_factor (yakıt) veya P_elec (elektrik)
Faydalı exergy:  Ex_useful = Q_evap × (1 - T₀/T_evap) + Ex_ürün_ısıtma
Egzoz exergy:    Ex_exhaust = ṁ_air × cp × [(T_exh - T₀) - T₀ × ln(T_exh/T₀)]
Exergy yıkımı:   Ex_destroyed = Ex_in - Ex_useful - Ex_exhaust
```

### Kod

```python
"""
ExergyLab - Dryer Exergy Analysis

Kurutma fırını exergy hesaplamaları.
Konveyörlü, döner, spreyli, akışkan yataklı ve raflı kurutucular için.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict
import math

from .core import (
    DeadState, ExergyResult,
    celsius_to_kelvin, bar_to_kpa,
    heat_exergy, CP_AIR
)


# Sabitler
H_FG_100C = 2257.0
CP_WATER_VAPOR = 1.87       # kJ/kg·K
CP_WATER = 4.18             # kJ/kg·K


def _get_hfg(T_C: float) -> float:
    """Buharlaşma entalpisi [kJ/kg] — lineer yaklaşım"""
    return max(2501 - 2.36 * T_C, 1800)


# Kurutucu tip verimi referansları (1. yasa termal verim)
DRYER_THERMAL_EFF = {
    'conveyor': 0.55,
    'rotary': 0.60,
    'spray': 0.40,
    'fluidized_bed': 0.65,
    'tray': 0.50,
    'drum': 0.55,
    'infrared': 0.45,
    'microwave': 0.50,
}


@dataclass
class DryerInput:
    """Kurutma fırını analizi için giriş verileri"""

    # Ürün parametreleri
    product_mass_flow_kg_h: float = 1000.0
    moisture_in_pct: float = 60.0          # yaş bazda
    moisture_out_pct: float = 10.0         # yaş bazda
    product_inlet_temp_C: float = 25.0
    product_outlet_temp_C: float = 60.0

    # Isıtma parametreleri
    heat_source: str = 'natural_gas'       # natural_gas, steam, electrical, hot_air
    supply_temp_C: float = 200.0
    heat_input_kW: Optional[float] = None
    fuel_efficiency: float = 0.85

    # Hava parametreleri
    air_inlet_temp_C: float = 25.0
    air_outlet_temp_C: float = 80.0
    air_mass_flow_kg_h: Optional[float] = None

    # Ortam
    ambient_temp_C: float = 25.0
    ambient_humidity_pct: float = 50.0

    # Operasyonel
    operating_hours: float = 5000
    electricity_price_eur_kwh: float = 0.10
    fuel_price_eur_kwh: float = 0.05

    # Ekipman
    dryer_type: str = 'conveyor'
    brand: Optional[str] = None
    model: Optional[str] = None
    age_years: Optional[int] = None

    def __post_init__(self):
        """Hesaplanan varsayılanlar"""
        self._calc_water_removal()
        if self.heat_input_kW is None:
            self._calc_heat_input()
        if self.air_mass_flow_kg_h is None:
            self._calc_air_flow()

    def _calc_water_removal(self):
        """Buharlaştırılacak su miktarı [kg/h]"""
        m_dry = self.product_mass_flow_kg_h * (1 - self.moisture_in_pct / 100)
        m_wet_in = self.product_mass_flow_kg_h
        m_wet_out = m_dry / (1 - self.moisture_out_pct / 100)
        self.water_removed_kg_h = max(m_wet_in - m_wet_out, 0)

    def _calc_heat_input(self):
        """Minimum ısı girişi tahmini [kW]"""
        h_fg = _get_hfg(self.product_outlet_temp_C)
        Q_evap = self.water_removed_kg_h * h_fg / 3600
        Q_sensible = (self.product_mass_flow_kg_h * CP_WATER * 0.3 *
                      (self.product_outlet_temp_C - self.product_inlet_temp_C)) / 3600
        thermal_eff = DRYER_THERMAL_EFF.get(self.dryer_type, 0.55)
        self.heat_input_kW = (Q_evap + Q_sensible) / thermal_eff

    def _calc_air_flow(self):
        """Hava debisi tahmini [kg/h]"""
        if self.supply_temp_C > self.air_outlet_temp_C:
            dT = self.supply_temp_C - self.air_outlet_temp_C
            self.air_mass_flow_kg_h = self.heat_input_kW * 3600 / (CP_AIR * dT)
        else:
            self.air_mass_flow_kg_h = 5000


@dataclass
class DryerResult(ExergyResult):
    """Kurutma fırını analizi sonuçları"""

    water_removed_kg_h: Optional[float] = None
    heat_input_kW: Optional[float] = None
    evaporation_energy_kW: Optional[float] = None
    exhaust_exergy_kW: Optional[float] = None

    thermal_efficiency_pct: Optional[float] = None
    specific_energy_kJ_kg_water: Optional[float] = None
    specific_exergy_kJ_kg_water: Optional[float] = None

    exhaust_recovery_potential_kW: Optional[float] = None
    exhaust_recovery_savings_eur_year: Optional[float] = None

    benchmark_comparison: Optional[str] = None

    def to_api_dict(self) -> dict:
        """API uyumlu dict çıktısı"""
        base = super().to_api_dict()
        base.update({
            'water_removed_kg_h': round(self.water_removed_kg_h, 1) if self.water_removed_kg_h else None,
            'heat_input_kW': round(self.heat_input_kW, 1) if self.heat_input_kW else None,
            'evaporation_energy_kW': round(self.evaporation_energy_kW, 1) if self.evaporation_energy_kW else None,
            'exhaust_exergy_kW': round(self.exhaust_exergy_kW, 1) if self.exhaust_exergy_kW else None,
            'thermal_efficiency_pct': round(self.thermal_efficiency_pct, 1) if self.thermal_efficiency_pct else None,
            'specific_energy_kJ_kg_water': round(self.specific_energy_kJ_kg_water, 0) if self.specific_energy_kJ_kg_water else None,
            'specific_exergy_kJ_kg_water': round(self.specific_exergy_kJ_kg_water, 0) if self.specific_exergy_kJ_kg_water else None,
            'exhaust_recovery_potential_kW': round(self.exhaust_recovery_potential_kW, 1) if self.exhaust_recovery_potential_kW else None,
            'exhaust_recovery_savings_eur_year': round(self.exhaust_recovery_savings_eur_year, 0) if self.exhaust_recovery_savings_eur_year else None,
            'benchmark_comparison': self.benchmark_comparison,
        })
        return base


def analyze_dryer(input_data: DryerInput, dead_state: DeadState = None) -> DryerResult:
    """
    Kurutma fırını exergy analizi yapar.

    Args:
        input_data: Kurutucu giriş verileri
        dead_state: Dead state koşulları (opsiyonel)

    Returns:
        DryerResult: Analiz sonuçları
    """
    if dead_state is None:
        dead_state = DeadState(T0=celsius_to_kelvin(input_data.ambient_temp_C))

    T0 = dead_state.T0

    T_supply = celsius_to_kelvin(input_data.supply_temp_C)
    T_exhaust = celsius_to_kelvin(input_data.air_outlet_temp_C)
    T_product_in = celsius_to_kelvin(input_data.product_inlet_temp_C)
    T_product_out = celsius_to_kelvin(input_data.product_outlet_temp_C)

    # Su buharlaştırma
    m_water_h = input_data.water_removed_kg_h
    m_water_s = m_water_h / 3600
    h_fg = _get_hfg(input_data.product_outlet_temp_C)
    Q_evap = m_water_s * h_fg

    Q_input = input_data.heat_input_kW

    # --- Giren Exergy ---
    if input_data.heat_source == 'electrical':
        Ex_in = Q_input
    elif input_data.heat_source == 'steam':
        Ex_in = Q_input * (1 - T0 / T_supply)
    else:
        exergy_factor = 1.04  # doğalgaz
        Ex_in = Q_input * exergy_factor

    # --- Faydalı Exergy ---
    T_evap = T_product_out
    if T_evap > T0:
        Ex_useful = Q_evap * (1 - T0 / T_evap)
    else:
        Ex_useful = 0

    m_product_s = input_data.product_mass_flow_kg_h / 3600
    cp_product = CP_WATER * 0.3
    Q_product = m_product_s * cp_product * (T_product_out - T_product_in)
    if T_product_out > T0:
        Ex_product_heating = Q_product * (1 - T0 / ((T_product_out + T_product_in) / 2))
        Ex_product_heating = max(Ex_product_heating, 0)
    else:
        Ex_product_heating = 0

    Ex_total_useful = Ex_useful + Ex_product_heating

    # --- Egzoz Exergy ---
    m_air_s = input_data.air_mass_flow_kg_h / 3600 if input_data.air_mass_flow_kg_h else 0
    if T_exhaust > T0 and m_air_s > 0:
        Ex_exhaust = m_air_s * CP_AIR * (
            (T_exhaust - T0) - T0 * math.log(T_exhaust / T0)
        )
        Ex_exhaust += m_water_s * CP_WATER_VAPOR * (
            (T_exhaust - T0) - T0 * math.log(T_exhaust / T0)
        )
        Ex_exhaust = max(Ex_exhaust, 0)
    else:
        Ex_exhaust = 0

    # --- Exergy Yıkımı ---
    Ex_destroyed = Ex_in - Ex_total_useful - Ex_exhaust
    Ex_destroyed = max(Ex_destroyed, 0)

    # --- Verimler ---
    eta_ex = (Ex_total_useful / Ex_in * 100) if Ex_in > 0 else 0

    Q_useful = Q_evap + Q_product
    thermal_eff = (Q_useful / Q_input * 100) if Q_input > 0 else 0

    specific_energy = (Q_input * 3600 / m_water_h) if m_water_h > 0 else 0
    specific_exergy = (Ex_in * 3600 / m_water_h) if m_water_h > 0 else 0

    # --- Egzoz Geri Kazanım ---
    exhaust_recovery = Ex_exhaust * 0.6
    exhaust_recovery_savings = exhaust_recovery * input_data.operating_hours * input_data.fuel_price_eur_kwh

    # --- Yıllık ---
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.fuel_price_eur_kwh

    benchmark = _get_dryer_benchmark(eta_ex, input_data.dryer_type)

    return DryerResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_total_useful,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        recoverable_heat_kW=exhaust_recovery,
        water_removed_kg_h=m_water_h,
        heat_input_kW=Q_input,
        evaporation_energy_kW=Q_evap,
        exhaust_exergy_kW=Ex_exhaust,
        thermal_efficiency_pct=thermal_eff,
        specific_energy_kJ_kg_water=specific_energy,
        specific_exergy_kJ_kg_water=specific_exergy,
        exhaust_recovery_potential_kW=exhaust_recovery,
        exhaust_recovery_savings_eur_year=exhaust_recovery_savings,
        benchmark_comparison=benchmark,
    )


def _get_dryer_benchmark(eta_ex: float, dryer_type: str) -> str:
    """Exergy verimine göre benchmark karşılaştırması"""
    benchmarks = {
        'conveyor':      {'poor': 8,  'average': 15, 'good': 22, 'excellent': 30},
        'rotary':        {'poor': 10, 'average': 18, 'good': 25, 'excellent': 33},
        'spray':         {'poor': 5,  'average': 10, 'good': 18, 'excellent': 25},
        'fluidized_bed': {'poor': 12, 'average': 20, 'good': 28, 'excellent': 35},
        'tray':          {'poor': 6,  'average': 12, 'good': 20, 'excellent': 28},
        'drum':          {'poor': 8,  'average': 15, 'good': 22, 'excellent': 30},
        'infrared':      {'poor': 10, 'average': 18, 'good': 25, 'excellent': 32},
        'microwave':     {'poor': 15, 'average': 22, 'good': 30, 'excellent': 38},
    }
    thresholds = benchmarks.get(dryer_type, benchmarks['conveyor'])

    if eta_ex < thresholds['poor']:
        return 'poor'
    elif eta_ex < thresholds['average']:
        return 'below_average'
    elif eta_ex < thresholds['good']:
        return 'average'
    elif eta_ex < thresholds['excellent']:
        return 'good'
    else:
        return 'excellent'


def generate_dryer_sankey_data(result: DryerResult) -> dict:
    """
    Kurutma fırını Sankey diyagram verisi üretir.

    Akış: Isı Kaynağı Exergy → [Kurutma İşi, Egzoz Exergy, Exergy Yıkımı]
    """
    Ex_in = result.exergy_in_kW or 0
    Ex_useful = result.exergy_out_kW or 0
    Ex_exhaust = result.exhaust_exergy_kW or 0
    Ex_destroyed = result.exergy_destroyed_kW or 0

    # Normalize
    total_out = Ex_useful + Ex_exhaust + Ex_destroyed
    if total_out > 0 and abs(total_out - Ex_in) > 0.1:
        scale = Ex_in / total_out
        Ex_useful *= scale
        Ex_exhaust *= scale
        Ex_destroyed *= scale

    nodes = [
        'Isı Kaynağı Exergy',     # 0
        'Kurutma İşi',            # 1
        'Egzoz Havası Exergy',    # 2
        'Exergy Yıkımı',          # 3
    ]

    links = []
    if Ex_useful > 0:
        links.append({'source': 0, 'target': 1, 'value': round(Ex_useful, 2)})
    if Ex_exhaust > 0:
        links.append({'source': 0, 'target': 2, 'value': round(Ex_exhaust, 2)})
    if Ex_destroyed > 0:
        links.append({'source': 0, 'target': 3, 'value': round(Ex_destroyed, 2)})

    return {
        'nodes': nodes,
        'links': links,
        'title': 'Kurutma Fırını Exergy Akışı',
    }


def get_dryer_recommendations(result: DryerResult, input_data: DryerInput) -> list:
    """Analiz sonuçlarına göre iyileştirme önerileri"""
    recommendations = []

    # 1. Egzoz ısı geri kazanımı
    if result.exhaust_recovery_potential_kW and result.exhaust_recovery_potential_kW > 5:
        recommendations.append({
            'type': 'exhaust_heat_recovery',
            'title': 'Egzoz Havası Isı Geri Kazanımı',
            'description': f'Egzoz havasında {result.exhaust_exergy_kW:.1f} kW exergy mevcut. '
                          f'Giriş havasını ön ısıtma ile {result.exhaust_recovery_savings_eur_year:.0f} €/yıl tasarruf.',
            'investment_eur': 15000,
            'savings_eur_year': result.exhaust_recovery_savings_eur_year or 0,
            'payback_years': 15000 / result.exhaust_recovery_savings_eur_year if result.exhaust_recovery_savings_eur_year and result.exhaust_recovery_savings_eur_year > 0 else float('inf'),
            'priority': 'high' if result.exhaust_recovery_savings_eur_year and result.exhaust_recovery_savings_eur_year > 5000 else 'medium',
        })

    # 2. Yüksek spesifik enerji → ön susuzlaştırma
    if result.specific_energy_kJ_kg_water and result.specific_energy_kJ_kg_water > 5000:
        savings = result.annual_loss_EUR * 0.20 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'pre_dewatering',
            'title': 'Mekanik Ön Susuzlaştırma',
            'description': 'Spesifik enerji tüketimi yüksek. Presleme veya santrifüj ile '
                          'giriş nem oranını düşürmek önerilir.',
            'investment_eur': 25000,
            'savings_eur_year': savings,
            'payback_years': 25000 / savings if savings > 0 else float('inf'),
            'priority': 'high',
        })

    # 3. Düşük termal verim → izolasyon
    if result.thermal_efficiency_pct and result.thermal_efficiency_pct < 45:
        savings = result.annual_loss_EUR * 0.10 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'insulation',
            'title': 'Kurutucu İzolasyonu İyileştirme',
            'description': f'Termal verim düşük ({result.thermal_efficiency_pct:.0f}%). '
                          f'Duvar ve boru izolasyonu kontrol edilmeli.',
            'investment_eur': 5000,
            'savings_eur_year': savings,
            'payback_years': 5000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # 4. Hava resirkülasyonu
    if input_data.air_outlet_temp_C > 60 and input_data.ambient_humidity_pct < 60:
        savings = result.annual_loss_EUR * 0.12 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'air_recirculation',
            'title': 'Kısmi Hava Resirkülasyonu',
            'description': 'Egzoz havasının bir kısmı geri döndürülerek enerji tasarrufu sağlanabilir. '
                          'Ürün kalitesine dikkat.',
            'investment_eur': 8000,
            'savings_eur_year': savings,
            'payback_years': 8000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # 5. Elektrik → doğalgaz/atık ısı
    if input_data.heat_source == 'electrical':
        savings = result.annual_loss_EUR * 0.40 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'heat_source_change',
            'title': 'Isı Kaynağı Optimizasyonu',
            'description': 'Elektrikli ısıtma yerine doğalgaz veya atık ısı kaynağı kullanımı '
                          'işletme maliyetini düşürebilir.',
            'investment_eur': 20000,
            'savings_eur_year': savings,
            'payback_years': 20000 / savings if savings > 0 else float('inf'),
            'priority': 'high' if result.heat_input_kW and result.heat_input_kW > 50 else 'medium',
        })

    return recommendations
```

---

## 📋 Test Dosyaları

### test_heat_exchanger.py

```python
"""Isı eşanjörü engine testleri"""
import pytest
import math
from engine.heat_exchanger import (
    HeatExchangerInput, HeatExchangerResult,
    analyze_heat_exchanger, get_heat_exchanger_recommendations,
    generate_heat_exchanger_sankey_data,
    FLUID_CP
)
from engine.core import DeadState


class TestHeatExchangerInput:
    """HeatExchangerInput testleri"""

    def test_default_values(self):
        inp = HeatExchangerInput()
        assert inp.hot_fluid == 'water'
        assert inp.cold_fluid == 'water'
        assert inp.hx_type == 'shell_tube'
        assert inp.heat_duty_kW is not None

    def test_heat_duty_auto_calculation(self):
        inp = HeatExchangerInput(
            hot_fluid='water',
            hot_inlet_temp_C=90,
            hot_outlet_temp_C=70,
            hot_mass_flow_kg_s=2.0,
        )
        expected = 2.0 * 4.18 * 20
        assert abs(inp.heat_duty_kW - expected) < 0.1

    def test_custom_heat_duty(self):
        inp = HeatExchangerInput(heat_duty_kW=500.0)
        assert inp.heat_duty_kW == 500.0


class TestAnalyzeHeatExchanger:
    """analyze_heat_exchanger testleri"""

    def test_basic_analysis(self):
        inp = HeatExchangerInput(
            hot_inlet_temp_C=90, hot_outlet_temp_C=70,
            hot_mass_flow_kg_s=2.0,
            cold_inlet_temp_C=20, cold_outlet_temp_C=50,
            cold_mass_flow_kg_s=2.5,
        )
        result = analyze_heat_exchanger(inp)
        assert result.exergy_in_kW > 0
        assert result.exergy_out_kW > 0
        assert result.exergy_destroyed_kW >= 0
        assert 0 < result.exergy_efficiency_pct <= 100
        assert result.heat_duty_kW > 0
        assert result.lmtd_K > 0

    def test_exergy_balance(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        balance = abs(result.exergy_destroyed_kW - (result.exergy_in_kW - result.exergy_out_kW))
        assert balance < 0.01

    def test_effectiveness_range(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        assert 0 <= result.effectiveness <= 1.0

    def test_bejan_number_range(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        assert 0 <= result.bejan_number <= 1.0

    def test_entropy_decomposition(self):
        inp = HeatExchangerInput(
            hot_fluid='air', cold_fluid='air',
            hot_pressure_drop_kPa=5.0, cold_pressure_drop_kPa=8.0,
        )
        result = analyze_heat_exchanger(inp)
        assert result.entropy_gen_heat_transfer_kW_K >= 0
        assert result.entropy_gen_pressure_drop_kW_K >= 0
        total = result.entropy_gen_heat_transfer_kW_K + result.entropy_gen_pressure_drop_kW_K
        assert abs(result.entropy_gen_total_kW_K - total) < 0.001

    def test_fouling_indicator(self):
        inp = HeatExchangerInput(heat_duty_kW=100, design_heat_duty_kW=200)
        result = analyze_heat_exchanger(inp)
        assert result.fouling_indicator == 'severe'

    def test_different_fluids(self):
        for fluid in FLUID_CP.keys():
            inp = HeatExchangerInput(hot_fluid=fluid)
            result = analyze_heat_exchanger(inp)
            assert result.exergy_in_kW > 0

    def test_plate_type(self):
        inp = HeatExchangerInput(hx_type='plate')
        result = analyze_heat_exchanger(inp)
        assert result.benchmark_comparison is not None

    def test_to_api_dict(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        d = result.to_api_dict()
        assert 'heat_duty_kW' in d
        assert 'bejan_number' in d
        assert 'lmtd_K' in d

    def test_annual_values(self):
        inp = HeatExchangerInput(operating_hours=8000, fuel_price_eur_kwh=0.06)
        result = analyze_heat_exchanger(inp)
        assert result.annual_loss_kWh > 0
        assert result.annual_loss_EUR > 0


class TestHeatExchangerSankey:
    """Sankey testleri"""

    def test_sankey_structure(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        sankey = generate_heat_exchanger_sankey_data(result)
        assert 'nodes' in sankey
        assert 'links' in sankey
        assert 'title' in sankey
        assert len(sankey['links']) >= 1

    def test_sankey_energy_balance(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        sankey = generate_heat_exchanger_sankey_data(result)
        total = sum(link['value'] for link in sankey['links'])
        assert abs(total - result.exergy_in_kW) < 1.0

    def test_sankey_bejan_split(self):
        inp = HeatExchangerInput(
            hot_fluid='air', cold_fluid='air',
            hot_pressure_drop_kPa=10.0, cold_pressure_drop_kPa=10.0,
        )
        result = analyze_heat_exchanger(inp)
        sankey = generate_heat_exchanger_sankey_data(result)
        # Basınç düşüşü varsa en az 3 link olmalı
        if result.entropy_gen_pressure_drop_kW_K > 0.01:
            assert len(sankey['links']) >= 3


class TestHeatExchangerRecommendations:
    """Öneri testleri"""

    def test_fouling_recommendation(self):
        inp = HeatExchangerInput(heat_duty_kW=100, design_heat_duty_kW=200)
        result = analyze_heat_exchanger(inp)
        recs = get_heat_exchanger_recommendations(result, inp)
        types = [r['type'] for r in recs]
        assert 'cleaning' in types

    def test_low_effectiveness_recommendation(self):
        inp = HeatExchangerInput(
            hot_inlet_temp_C=200, hot_outlet_temp_C=180,
            cold_inlet_temp_C=20, cold_outlet_temp_C=25,
            hot_mass_flow_kg_s=5.0, cold_mass_flow_kg_s=5.0,
        )
        result = analyze_heat_exchanger(inp)
        recs = get_heat_exchanger_recommendations(result, inp)
        if result.effectiveness < 0.5:
            types = [r['type'] for r in recs]
            assert 'upgrade' in types

    def test_recommendation_structure(self):
        inp = HeatExchangerInput(heat_duty_kW=100, design_heat_duty_kW=200)
        result = analyze_heat_exchanger(inp)
        recs = get_heat_exchanger_recommendations(result, inp)
        for rec in recs:
            assert 'type' in rec
            assert 'title' in rec
            assert 'description' in rec
            assert 'investment_eur' in rec
            assert 'savings_eur_year' in rec
            assert 'payback_years' in rec
            assert 'priority' in rec
```

### test_steam_turbine.py

```python
"""Buhar türbini engine testleri"""
import pytest
import math
from engine.steam_turbine import (
    SteamTurbineInput, SteamTurbineResult,
    analyze_steam_turbine, get_steam_turbine_recommendations,
    generate_steam_turbine_sankey_data,
    _get_saturation_temp_C
)
from engine.core import DeadState


class TestSteamTurbineInput:
    """SteamTurbineInput testleri"""

    def test_default_values(self):
        inp = SteamTurbineInput()
        assert inp.turbine_type == 'backpressure'
        assert inp.inlet_temp_C == 400.0
        assert inp.inlet_pressure_bar == 40.0
        assert inp.outlet_temp_C is not None

    def test_condensing_outlet_temp(self):
        inp = SteamTurbineInput(turbine_type='condensing', outlet_pressure_bar=0.1)
        T_sat = _get_saturation_temp_C(0.1)
        assert abs(inp.outlet_temp_C - T_sat) < 1.0

    def test_backpressure_outlet_temp(self):
        inp = SteamTurbineInput(turbine_type='backpressure', outlet_pressure_bar=5.0)
        T_sat = _get_saturation_temp_C(5.0)
        assert inp.outlet_temp_C >= T_sat


class TestAnalyzeSteamTurbine:
    """analyze_steam_turbine testleri"""

    def test_basic_analysis(self):
        inp = SteamTurbineInput(
            inlet_temp_C=400, inlet_pressure_bar=40,
            mass_flow_kg_s=5.0, outlet_pressure_bar=2.0,
        )
        result = analyze_steam_turbine(inp)
        assert result.exergy_in_kW > 0
        assert result.shaft_power_kW > 0
        assert result.electrical_power_kW > 0
        assert result.exergy_destroyed_kW >= 0
        assert 0 < result.exergy_efficiency_pct <= 100

    def test_exergy_balance(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        balance = abs(result.exergy_in_kW - result.shaft_power_kW - result.exergy_out_kW - result.exergy_destroyed_kW)
        assert balance < 1.0

    def test_electrical_less_than_shaft(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        assert result.electrical_power_kW < result.shaft_power_kW

    def test_chp_mode(self):
        inp = SteamTurbineInput(
            is_chp=True, turbine_type='backpressure',
            outlet_pressure_bar=3.0, heat_recovery_temp_C=130,
        )
        result = analyze_steam_turbine(inp)
        assert result.heat_recovered_kW is not None
        assert result.heat_recovered_kW > 0
        assert result.chp_exergy_efficiency_pct > result.exergy_efficiency_pct

    def test_condensing_vs_backpressure(self):
        inp_cond = SteamTurbineInput(turbine_type='condensing', outlet_pressure_bar=0.1)
        inp_bp = SteamTurbineInput(turbine_type='backpressure', outlet_pressure_bar=3.0)
        r_cond = analyze_steam_turbine(inp_cond)
        r_bp = analyze_steam_turbine(inp_bp)
        assert r_cond.shaft_power_kW > r_bp.shaft_power_kW

    def test_higher_efficiency_more_work(self):
        inp_low = SteamTurbineInput(isentropic_efficiency=0.60)
        inp_high = SteamTurbineInput(isentropic_efficiency=0.90)
        r_low = analyze_steam_turbine(inp_low)
        r_high = analyze_steam_turbine(inp_high)
        assert r_high.shaft_power_kW >= r_low.shaft_power_kW

    def test_annual_values(self):
        inp = SteamTurbineInput(operating_hours=7000)
        result = analyze_steam_turbine(inp)
        assert result.annual_electricity_MWh > 0
        assert result.annual_electricity_revenue_EUR > 0

    def test_to_api_dict(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        d = result.to_api_dict()
        assert 'shaft_power_kW' in d
        assert 'electrical_power_kW' in d
        assert 'benchmark_comparison' in d

    def test_saturation_temp_interpolation(self):
        T_10 = _get_saturation_temp_C(10.0)
        assert abs(T_10 - 179.9) < 0.5
        T_mid = _get_saturation_temp_C(7.0)
        assert 158.8 < T_mid < 170.4


class TestSteamTurbineSankey:
    """Sankey testleri"""

    def test_sankey_structure(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        sankey = generate_steam_turbine_sankey_data(result)
        assert 'nodes' in sankey
        assert 'links' in sankey
        assert len(sankey['links']) >= 2

    def test_sankey_chp_mode(self):
        inp = SteamTurbineInput(
            is_chp=True, turbine_type='backpressure',
            outlet_pressure_bar=3.0, heat_recovery_temp_C=130,
        )
        result = analyze_steam_turbine(inp)
        sankey = generate_steam_turbine_sankey_data(result)
        assert 'CHP' in sankey['title']
        # CHP modunda daha fazla node
        assert len(sankey['nodes']) >= 4


class TestSteamTurbineRecommendations:
    """Öneri testleri"""

    def test_chp_recommendation_for_non_chp(self):
        inp = SteamTurbineInput(is_chp=False, outlet_pressure_bar=3.0)
        result = analyze_steam_turbine(inp)
        recs = get_steam_turbine_recommendations(result, inp)
        if result.exhaust_exergy_kW and result.exhaust_exergy_kW > 100:
            types = [r['type'] for r in recs]
            assert 'chp_conversion' in types

    def test_overhaul_recommendation(self):
        inp = SteamTurbineInput(isentropic_efficiency=0.60)
        result = analyze_steam_turbine(inp)
        recs = get_steam_turbine_recommendations(result, inp)
        types = [r['type'] for r in recs]
        assert 'overhaul' in types

    def test_recommendation_structure(self):
        inp = SteamTurbineInput(isentropic_efficiency=0.60)
        result = analyze_steam_turbine(inp)
        recs = get_steam_turbine_recommendations(result, inp)
        for rec in recs:
            assert 'type' in rec
            assert 'title' in rec
            assert 'investment_eur' in rec
            assert 'savings_eur_year' in rec
            assert 'priority' in rec
```

### test_dryer.py

```python
"""Kurutma fırını engine testleri"""
import pytest
import math
from engine.dryer import (
    DryerInput, DryerResult,
    analyze_dryer, get_dryer_recommendations,
    generate_dryer_sankey_data,
    _get_hfg, DRYER_THERMAL_EFF
)
from engine.core import DeadState


class TestDryerInput:
    """DryerInput testleri"""

    def test_default_values(self):
        inp = DryerInput()
        assert inp.dryer_type == 'conveyor'
        assert inp.moisture_in_pct == 60.0
        assert inp.moisture_out_pct == 10.0
        assert inp.water_removed_kg_h > 0
        assert inp.heat_input_kW > 0

    def test_water_removal_calculation(self):
        inp = DryerInput(
            product_mass_flow_kg_h=1000,
            moisture_in_pct=50,
            moisture_out_pct=10,
        )
        expected_water = 1000 - 500 / 0.9
        assert abs(inp.water_removed_kg_h - expected_water) < 1.0

    def test_zero_moisture_change(self):
        inp = DryerInput(moisture_in_pct=10, moisture_out_pct=10)
        assert inp.water_removed_kg_h == 0 or inp.water_removed_kg_h < 1

    def test_heat_input_auto_calc(self):
        inp = DryerInput(heat_input_kW=None)
        assert inp.heat_input_kW > 0

    def test_custom_heat_input(self):
        inp = DryerInput(heat_input_kW=500.0)
        assert inp.heat_input_kW == 500.0

    def test_hfg_function(self):
        h60 = _get_hfg(60)
        h100 = _get_hfg(100)
        assert h60 > h100
        assert h100 > 2200


class TestAnalyzeDryer:
    """analyze_dryer testleri"""

    def test_basic_analysis(self):
        inp = DryerInput(
            product_mass_flow_kg_h=1000,
            moisture_in_pct=60, moisture_out_pct=10,
            supply_temp_C=200,
        )
        result = analyze_dryer(inp)
        assert result.exergy_in_kW > 0
        assert result.exergy_out_kW >= 0
        assert result.exergy_destroyed_kW >= 0
        assert 0 <= result.exergy_efficiency_pct <= 100
        assert result.water_removed_kg_h > 0

    def test_exergy_balance(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        total = result.exergy_out_kW + result.exhaust_exergy_kW + result.exergy_destroyed_kW
        assert abs(result.exergy_in_kW - total) < 1.0

    def test_electrical_source(self):
        inp = DryerInput(heat_source='electrical', heat_input_kW=100)
        result = analyze_dryer(inp)
        assert result.exergy_in_kW == 100.0

    def test_steam_source(self):
        inp = DryerInput(heat_source='steam', heat_input_kW=100, supply_temp_C=150)
        result = analyze_dryer(inp)
        assert result.exergy_in_kW < 100

    def test_natural_gas_source(self):
        inp = DryerInput(heat_source='natural_gas', heat_input_kW=100)
        result = analyze_dryer(inp)
        assert result.exergy_in_kW > 100

    def test_thermal_efficiency(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        assert 0 < result.thermal_efficiency_pct < 100

    def test_specific_energy(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        assert result.specific_energy_kJ_kg_water > 2000

    def test_different_dryer_types(self):
        for dryer_type in DRYER_THERMAL_EFF.keys():
            inp = DryerInput(dryer_type=dryer_type)
            result = analyze_dryer(inp)
            assert result.exergy_in_kW > 0
            assert result.benchmark_comparison is not None

    def test_exhaust_recovery(self):
        inp = DryerInput(air_outlet_temp_C=120)
        result = analyze_dryer(inp)
        assert result.exhaust_exergy_kW > 0
        assert result.exhaust_recovery_potential_kW > 0

    def test_annual_values(self):
        inp = DryerInput(operating_hours=5000, fuel_price_eur_kwh=0.05)
        result = analyze_dryer(inp)
        assert result.annual_loss_kWh > 0
        assert result.annual_loss_EUR > 0

    def test_to_api_dict(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        d = result.to_api_dict()
        assert 'water_removed_kg_h' in d
        assert 'specific_energy_kJ_kg_water' in d
        assert 'exhaust_exergy_kW' in d


class TestDryerSankey:
    """Sankey testleri"""

    def test_sankey_structure(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        sankey = generate_dryer_sankey_data(result)
        assert 'nodes' in sankey
        assert 'links' in sankey
        assert 'title' in sankey
        assert len(sankey['links']) >= 2

    def test_sankey_energy_balance(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        sankey = generate_dryer_sankey_data(result)
        total = sum(link['value'] for link in sankey['links'])
        assert abs(total - result.exergy_in_kW) < 1.0


class TestDryerRecommendations:
    """Öneri testleri"""

    def test_exhaust_recovery_recommendation(self):
        inp = DryerInput(air_outlet_temp_C=120, operating_hours=6000)
        result = analyze_dryer(inp)
        recs = get_dryer_recommendations(result, inp)
        types = [r['type'] for r in recs]
        assert 'exhaust_heat_recovery' in types

    def test_electrical_source_recommendation(self):
        inp = DryerInput(heat_source='electrical', heat_input_kW=100)
        result = analyze_dryer(inp)
        recs = get_dryer_recommendations(result, inp)
        types = [r['type'] for r in recs]
        assert 'heat_source_change' in types

    def test_recommendation_structure(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        recs = get_dryer_recommendations(result, inp)
        for rec in recs:
            assert 'type' in rec
            assert 'title' in rec
            assert 'description' in rec
            assert 'investment_eur' in rec
            assert 'savings_eur_year' in rec
            assert 'payback_years' in rec
            assert 'priority' in rec
```

---

## 🔧 Entegrasyon Talimatları (KRİTİK)

### 1. `engine/__init__.py` — Yeni export'lar ekle

Mevcut import'ların altına ekle:

```python
from .heat_exchanger import (
    HeatExchangerInput, HeatExchangerResult,
    analyze_heat_exchanger, get_heat_exchanger_recommendations,
    generate_heat_exchanger_sankey_data
)
from .steam_turbine import (
    SteamTurbineInput, SteamTurbineResult,
    analyze_steam_turbine, get_steam_turbine_recommendations,
    generate_steam_turbine_sankey_data
)
from .dryer import (
    DryerInput, DryerResult,
    analyze_dryer, get_dryer_recommendations,
    generate_dryer_sankey_data
)
```

### 2. `engine/sankey.py` — Dispatcher güncelle

Mevcut isinstance zincirine ekle:

```python
from .heat_exchanger import HeatExchangerResult, generate_heat_exchanger_sankey_data
from .steam_turbine import SteamTurbineResult, generate_steam_turbine_sankey_data
from .dryer import DryerResult, generate_dryer_sankey_data

# generate_sankey_data() fonksiyonundaki isinstance zincirine ekle:
#   elif isinstance(result, HeatExchangerResult):
#       return generate_heat_exchanger_sankey_data(result)
#   elif isinstance(result, SteamTurbineResult):
#       return generate_steam_turbine_sankey_data(result)
#   elif isinstance(result, DryerResult):
#       return generate_dryer_sankey_data(result)
```

### 3. `engine/factory.py` — `_ANALYZERS` dict güncelle

```python
# Mevcut dict'e ekle:
from .heat_exchanger import analyze_heat_exchanger, HeatExchangerInput
from .steam_turbine import analyze_steam_turbine, SteamTurbineInput
from .dryer import analyze_dryer, DryerInput

# _ANALYZERS dict'ine:
'heat_exchanger': analyze_heat_exchanger,
'steam_turbine': analyze_steam_turbine,
'dryer': analyze_dryer,
```

Ayrıca yeni cross-equipment entegrasyon desenleri eklemeyi düşün:
- Dryer egzoz → HX ile hava ön ısıtma
- Steam turbine egzoz → absorption chiller beslemesi
- Boiler baca gazı → HX ile feedwater ısıtma (ekonomizer)
- Steam turbine CHP → genel tesis ısıtma

### 4. `api/services/equipment_registry.py` — `engine_ready: True` yap

3 yeni ekipman için `engine_ready: False` → `engine_ready: True` güncelle.

### 5. `api/routes/analysis.py` — Route dispatcher güncelle

Tek ekipman analizi route'unda yeni engine'leri tanıt. Mevcut dispatcher pattern'ını incele ve aynı şekilde ekle.

### 6. DeadState Uyumluluğu (DİKKAT)

Brief'te `DeadState(T0=celsius_to_kelvin(...))` kullanılıyor. Eğer mevcut kodda DeadState farklı oluşturuluyorsa (örn. `DeadState.from_celsius()` veya sadece `DeadState()`) mevcut pattern'ı kullan.

---

## 📋 Test Çalıştırma

```bash
# 1. Sadece yeni testler
pytest tests/test_heat_exchanger.py tests/test_steam_turbine.py tests/test_dryer.py -v

# 2. TÜM testler (regression kontrolü — KRİTİK)
pytest tests/ -v

# 3. Beklenti: ~285+ test, %100 pass
```

---

## 📋 Entegrasyon Doğrulama Scriptleri

Tüm kod bittikten sonra bunları çalıştır:

```bash
# Equipment registry kontrolü
python -c "
from api.services.equipment_registry import get_equipment_types
types = get_equipment_types()
ready = [t for t in types if t.get('engine_ready')]
print(f'Engine ready: {len(ready)}/7')
for t in types:
    print(f'  {t[\"id\"]}: engine_ready={t.get(\"engine_ready\", False)}')
assert len(ready) == 7, f'Expected 7, got {len(ready)}'
print('✅ All 7 equipment types engine_ready')
"

# Factory analyzer kontrolü
python -c "
from engine.factory import _ANALYZERS
print(f'Registered analyzers: {list(_ANALYZERS.keys())}')
assert len(_ANALYZERS) == 7, f'Expected 7 analyzers, got {len(_ANALYZERS)}'
print('✅ All 7 analyzers registered in factory')
"

# Sankey dispatcher kontrolü
python -c "
from engine.sankey import generate_sankey_data
from engine.heat_exchanger import HeatExchangerInput, analyze_heat_exchanger
from engine.steam_turbine import SteamTurbineInput, analyze_steam_turbine
from engine.dryer import DryerInput, analyze_dryer

for name, inp, func in [
    ('HX', HeatExchangerInput(), analyze_heat_exchanger),
    ('ST', SteamTurbineInput(), analyze_steam_turbine),
    ('Dryer', DryerInput(), analyze_dryer),
]:
    result = func(inp)
    sankey = generate_sankey_data(result)
    assert 'nodes' in sankey and 'links' in sankey
    print(f'✅ {name} Sankey works')
print('✅ All 3 new Sankey dispatchers working')
"

# to_api_dict kontrolü
python -c "
from engine.heat_exchanger import HeatExchangerInput, analyze_heat_exchanger
from engine.steam_turbine import SteamTurbineInput, analyze_steam_turbine
from engine.dryer import DryerInput, analyze_dryer

for name, inp, func in [
    ('HX', HeatExchangerInput(), analyze_heat_exchanger),
    ('ST', SteamTurbineInput(), analyze_steam_turbine),
    ('Dryer', DryerInput(), analyze_dryer),
]:
    result = func(inp)
    d = result.to_api_dict()
    assert isinstance(d, dict)
    assert 'exergy_efficiency_pct' in d
    print(f'✅ {name} to_api_dict() works')
print('✅ All to_api_dict() methods working')
"
```

---

## ✅ Tamamlanma Kriterleri

- [ ] `engine/heat_exchanger.py` oluşturuldu, `to_api_dict()` + Sankey fonksiyonu var
- [ ] `engine/steam_turbine.py` oluşturuldu, `to_api_dict()` + Sankey fonksiyonu var
- [ ] `engine/dryer.py` oluşturuldu, `to_api_dict()` + Sankey fonksiyonu var
- [ ] `engine/__init__.py` güncellendi (yeni import + export)
- [ ] `engine/factory.py` `_ANALYZERS` güncellendi (7 ekipman)
- [ ] `engine/sankey.py` dispatcher güncellendi (7 tip)
- [ ] `api/services/equipment_registry.py` → 3 ekipman `engine_ready: True`
- [ ] `api/routes/analysis.py` → yeni engine'ler dispatcher'a eklendi
- [ ] `tests/test_heat_exchanger.py` — tüm testler geçiyor
- [ ] `tests/test_steam_turbine.py` — tüm testler geçiyor
- [ ] `tests/test_dryer.py` — tüm testler geçiyor
- [ ] Mevcut 243 test hâlâ geçiyor (regression yok)
- [ ] Entegrasyon doğrulama scriptleri başarılı
- [ ] Toplam test: ~285+ test, %100 pass

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| Engine modülleri | 4 | 7 |
| Engine ready ekipman | 4/7 | 7/7 |
| Sankey desteği | 4 tip | 7 tip |
| Factory analyzers | 4 | 7 |
| Test sayısı | 243 | ~285+ |
| Test başarı oranı | %100 | %100 |
