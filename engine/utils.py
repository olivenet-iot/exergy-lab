"""
ExergyLab - Utility Functions

Yardımcı fonksiyonlar, birim çevrimleri, validasyon.
"""

from typing import Union, Optional
import json
from datetime import datetime


# Birim çevrim faktörleri
UNIT_CONVERSIONS = {
    'pressure': {
        'bar_to_kpa': 100,
        'psi_to_kpa': 6.89476,
        'atm_to_kpa': 101.325,
    },
    'temperature': {
        'C_to_K': lambda c: c + 273.15,
        'F_to_K': lambda f: (f - 32) * 5/9 + 273.15,
    },
    'flow': {
        'm3_min_to_m3_s': 1/60,
        'cfm_to_m3_min': 0.0283168,
        'l_min_to_m3_min': 0.001,
    },
    'power': {
        'hp_to_kW': 0.7457,
        'btu_hr_to_kW': 0.000293071,
    }
}


def convert_pressure(value: float, from_unit: str, to_unit: str = 'kpa') -> float:
    """Basınç birimi çevirici"""
    # Önce kPa'ya çevir
    to_kpa = {
        'kpa': 1,
        'bar': 100,
        'psi': 6.89476,
        'atm': 101.325,
        'mbar': 0.1,
    }

    from_kpa = {k: 1/v for k, v in to_kpa.items()}

    kpa_value = value * to_kpa.get(from_unit.lower(), 1)
    return kpa_value * from_kpa.get(to_unit.lower(), 1)


def convert_temperature(value: float, from_unit: str, to_unit: str = 'K') -> float:
    """Sıcaklık birimi çevirici"""
    # Önce Kelvin'e çevir
    if from_unit.upper() == 'C':
        kelvin = value + 273.15
    elif from_unit.upper() == 'F':
        kelvin = (value - 32) * 5/9 + 273.15
    elif from_unit.upper() == 'K':
        kelvin = value
    else:
        kelvin = value

    # Hedef birime çevir
    if to_unit.upper() == 'C':
        return kelvin - 273.15
    elif to_unit.upper() == 'F':
        return (kelvin - 273.15) * 9/5 + 32
    else:
        return kelvin


def validate_positive(value: float, name: str) -> None:
    """Pozitif değer kontrolü"""
    if value <= 0:
        raise ValueError(f"{name} pozitif olmalı, verilen: {value}")


def validate_range(value: float, min_val: float, max_val: float, name: str) -> None:
    """Aralık kontrolü"""
    if not min_val <= value <= max_val:
        raise ValueError(f"{name} {min_val}-{max_val} aralığında olmalı, verilen: {value}")


def format_currency(value: float, currency: str = '€') -> str:
    """Para birimi formatla"""
    return f"{currency}{value:,.0f}"


def format_percentage(value: float, decimals: int = 1) -> str:
    """Yüzde formatla"""
    return f"{value:.{decimals}f}%"


def format_power(value_kw: float) -> str:
    """Güç formatla"""
    if value_kw >= 1000:
        return f"{value_kw/1000:.1f} MW"
    else:
        return f"{value_kw:.1f} kW"


def save_analysis_result(result: dict, filepath: str) -> None:
    """Analiz sonucunu JSON olarak kaydet"""
    result['timestamp'] = datetime.now().isoformat()
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


def load_analysis_result(filepath: str) -> dict:
    """Kayıtlı analiz sonucunu yükle"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
