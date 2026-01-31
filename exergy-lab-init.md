# ExergyLab — Project Initialization Document

> **Bu dosyayı Claude Code'a ver. "Bu dosyayı oku ve projeyi oluştur" de.**

---

## 🎯 Proje Özeti

**ExergyLab**, endüstriyel tesislerde termodinamik performans analizi yapan bir internal tool'dur. Exergy (kullanılabilir enerji) kavramını kullanarak sistemlerdeki gerçek verimsizlikleri tespit eder, sayısallaştırır ve çözüm önerileri sunar.

**Temel felsefe:** "Entropi avcılığı" — enerji kayıplarını değil, exergy yıkımını (gerçek termodinamik kaybı) bulmak.

---

## 👤 Kullanıcı Profili

- **Kim:** Kemal — Kimya mühendisi, termodinamik ve ısı transferinde güçlü, IoT/LoRaWAN deneyimli
- **Kullanım:** Internal tool, sahada veri toplama ve analiz
- **Amaç:** Fabrikalara/tesislere gidip exergy analizi yapmak, raporlamak, danışmanlık vermek

---

## 🏗️ Mimari Genel Bakış

```
/exergy-lab
│
├── /knowledge                    # Bilgi tabanı (MD dosyaları)
│   ├── /equipment                # Ekipman tanımları ve ölçüm gereksinimleri
│   ├── /benchmarks               # Sektörel benchmark verileri
│   ├── /solutions                # Çözüm önerileri ve ROI bilgileri
│   ├── /formulas                 # Termodinamik denklemler ve açıklamalar
│   └── /methodology              # Audit süreci ve rehberler
│
├── /skills                       # Claude Code skill dosyaları
│   ├── SKILL_exergy_calculator.md
│   ├── SKILL_benchmark_analyzer.md
│   ├── SKILL_solution_recommender.md
│   └── SKILL_report_generator.md
│
├── /engine                       # Python hesaplama motoru (deterministik)
│   ├── __init__.py
│   ├── core.py                   # Temel exergy fonksiyonları
│   ├── compressor.py             # Kompresör hesaplamaları
│   ├── boiler.py                 # Kazan hesaplamaları
│   ├── heat_exchanger.py         # Isı eşanjörü hesaplamaları
│   ├── chiller.py                # Chiller hesaplamaları
│   ├── utils.py                  # Yardımcı fonksiyonlar, birim çevrimleri
│   └── fluids.py                 # CoolProp wrapper
│
├── /app                          # Web arayüzü (Streamlit veya FastAPI + React)
│   └── (sonraki aşama)
│
├── /data                         # Proje verileri
│   ├── /projects                 # Kayıtlı projeler (JSON)
│   └── /templates                # Form şablonları
│
├── /output                       # Çıktılar
│   ├── /reports                  # PDF raporlar
│   └── /charts                   # Grafikler, diyagramlar
│
├── /tests                        # Unit testler
│   └── test_compressor.py
│
├── requirements.txt              # Python bağımlılıkları
├── README.md                     # Proje açıklaması
└── PROJECT.md                    # Bu dosya
```

---

## 🔬 Temel Kavramlar

### Exergy Nedir?

Exergy = Bir sistemin çevresiyle dengeye gelene kadar yapabileceği maksimum iş.

- **Enerji korunur** (1. yasa) — kaybolmaz, dönüşür
- **Exergy korunmaz** (2. yasa) — her süreçte bir miktar yok edilir
- **Exergy yıkımı = Entropi üretimi × T₀**

### Dead State (Ölü Durum)

Referans çevre koşulları:
- T₀ = 298.15 K (25°C) — ayarlanabilir
- P₀ = 101.325 kPa (1 atm)

### Temel Denklemler

**Fiziksel exergy (akışkan):**
```
Ex = ṁ × [(h - h₀) - T₀ × (s - s₀)]
```

**Isı transferi exergy'si:**
```
Ex_Q = Q̇ × (1 - T₀/T)
```

**Exergy verimi:**
```
η_ex = Ex_out / Ex_in
```

**Exergy yıkımı:**
```
Ex_destroyed = Ex_in - Ex_out = T₀ × Ṡ_gen
```

---

## 📦 İlk Sprint: Kompresör Modülü

İlk olarak **kompresör** için tam bir modül oluşturulacak. Bu template olacak, diğer ekipmanlar buna göre yapılacak.

### 1. Knowledge Base Dosyaları

#### `/knowledge/equipment/compressor_screw.md`

```markdown
# Vidalı Kompresör (Screw Compressor)

## Genel Bilgiler
- Tip: Pozitif deplasmanlı, döner
- Kapasite aralığı: 3 - 500 kW
- Basınç aralığı: 5 - 15 bar (tipik 7-10 bar)
- Yaygın markalar: Atlas Copco, Kaeser, Ingersoll Rand, Boge, CompAir

## Çalışma Prensibi
İki helisel rotor arasında hava sıkıştırılır. Yağlı tip (oil-injected) 
en yaygınıdır — yağ hem sızdırmazlık hem soğutma sağlar.

## Enerji Dağılımı (Tipik)
- Basınçlı hava (faydalı iş): ~8-10%
- Yağ soğutucuya atılan ısı: ~72%
- Aftercooler'a atılan ısı: ~13%
- Radyasyon ve diğer kayıplar: ~5%

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 3-500 | Güç analizörü veya CT + voltaj |
| Çıkış basıncı | bar | 5-15 | Manometre veya basınç sensörü |
| Hava debisi | m³/min | 0.3-80 | Flowmeter veya nameplate + yük |
| Ortam sıcaklığı | °C | 15-40 | Termometre |

### Opsiyonel (daha detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Giriş sıcaklığı | °C | 15-40 | Termometre |
| Çıkış sıcaklığı | °C | 70-100 | Termometre |
| Yağ sıcaklığı | °C | 60-90 | Termometre |
| Yük oranı | % | 0-100 | Kontrol paneli veya akım |
| Çalışma saati | saat/yıl | 2000-8760 | Sayaç veya tahmin |

### Nameplate Bilgileri
- Marka ve model
- Nominal güç (kW)
- Nominal debi (m³/min veya CFM)
- Nominal basınç (bar veya PSI)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Giriş sıcaklığı | Ortam sıcaklığı | |
| Çıkış sıcaklığı | 85°C | Yağlı vidalı için tipik |
| Yük oranı | 75% | Endüstriyel ortalama |
| Çalışma saati | 4000 saat/yıl | Tek vardiya |
| cosφ (güç faktörü) | 0.85 | Tipik motor değeri |
| Spesifik güç | 6.5 kW/(m³/min) | Ortalama verimli kompresör |

## Dikkat Edilecekler

1. **Yük/boşta çalışma**: Boşta bile %25-30 güç çeker
2. **Basınç kaybı**: Her 1 bar düşüş ≈ %7 enerji tasarrufu
3. **Sıcaklık**: Giriş havası her 5°C düşüşü ≈ %2 verim artışı
4. **Kaçaklar**: Tipik tesiste %20-30 hava kaçağı var
5. **Filtre**: Tıkalı filtre basınç düşürür, enerji artar
```

#### `/knowledge/formulas/compressor_exergy.md`

```markdown
# Kompresör Exergy Hesaplamaları

## Temel İlkeler

Kompresör elektrik enerjisini (saf exergy) basınçlı hava exergy'sine dönüştürür.
Dönüşüm sırasında entropi üretilir ve exergy yok edilir.

## Hesaplama Adımları

### 1. Giren Exergy (Elektrik)

Elektrik saf exergy'dir:
```
Ex_in = P_electric [kW]
```

### 2. Kütle Debisi

Hacimsel debiden kütle debisine:
```
ṁ = V̇ × ρ_air

Burada:
- V̇ = Hacimsel debi [m³/s]
- ρ_air = Hava yoğunluğu ≈ 1.2 kg/m³ (25°C, 1 atm'de)
```

### 3. Çıkan Exergy (Basınçlı Hava)

İdeal gaz kabulüyle basınçlı havanın exergy'si:
```
Ex_air = ṁ × R × T₀ × ln(P₂/P₁)

Burada:
- R = 0.287 kJ/kg·K (kuru hava için gaz sabiti)
- T₀ = 298.15 K (dead state sıcaklığı)
- P₂ = Çıkış basıncı [kPa]
- P₁ = Giriş basıncı = 101.325 kPa
```

### 4. Exergy Yıkımı

```
Ex_destroyed = Ex_in - Ex_air [kW]
```

### 5. Exergy Verimi

```
η_ex = Ex_air / Ex_in × 100 [%]
```

### 6. Atık Isı Exergy Potansiyeli

Kompresör atık ısısı aftercooler ve yağ soğutucudan atılır:
```
Q_waste ≈ Ex_destroyed [kW]  (büyük kısmı ısı olarak)

Ex_heat_recoverable = Q_waste × (1 - T₀/T_exhaust)

Burada:
- T_exhaust = Çıkış sıcaklığı [K]
```

### 7. Yıllık Maliyet

```
Yıllık_kayıp_kWh = Ex_destroyed × çalışma_saati
Yıllık_kayıp_EUR = Yıllık_kayıp_kWh × elektrik_fiyatı
```

## Örnek Hesaplama

**Girdiler:**
- P_electric = 32 kW
- V̇ = 6.2 m³/min = 0.103 m³/s
- P₂ = 7.5 bar = 750 kPa
- T_exhaust = 85°C = 358 K
- Çalışma = 6000 saat/yıl
- Elektrik = 0.10 €/kWh

**Hesap:**
```
ṁ = 0.103 × 1.2 = 0.124 kg/s

Ex_air = 0.124 × 0.287 × 298.15 × ln(750/101.325)
       = 0.124 × 0.287 × 298.15 × 2.002
       = 21.25 kW

Ex_destroyed = 32 - 21.25 = 10.75 kW

η_ex = 21.25 / 32 × 100 = 66.4%

Ex_heat = 10.75 × (1 - 298.15/358) = 1.80 kW

Yıllık_kayıp = 10.75 × 6000 = 64,500 kWh
Maliyet = 64,500 × 0.10 = 6,450 €/yıl
```

## Sınırlamalar

1. İdeal gaz kabulü yapılmıştır (yüksek basınçlarda sapma olabilir)
2. Nem etkisi ihmal edilmiştir
3. Yük değişimi dinamikleri dahil değildir
```

#### `/knowledge/benchmarks/compressor_benchmarks.md`

```markdown
# Kompresör Benchmark Verileri

## Exergy Verimi Aralıkları

| Kompresör Tipi | Düşük | Ortalama | İyi | Best-in-class |
|----------------|-------|----------|-----|---------------|
| Vidalı (yağlı) | <30% | 35-45% | 45-55% | >60% |
| Vidalı (yağsız) | <25% | 30-40% | 40-50% | >55% |
| Pistonlu | <25% | 30-40% | 40-50% | >55% |
| Scroll | <30% | 35-45% | 45-55% | >60% |
| Santrifüj | <35% | 40-50% | 50-60% | >65% |

## Spesifik Güç Tüketimi

Verimlilik için alternatif metrik: kW / (m³/min) @ 7 bar

| Sınıf | Spesifik Güç | Açıklama |
|-------|--------------|----------|
| Çok iyi | < 5.5 | Modern, VSD, optimize |
| İyi | 5.5 - 6.5 | Standart verimli |
| Ortalama | 6.5 - 7.5 | Eski veya bakımsız |
| Kötü | > 7.5 | Acil müdahale gerekli |

## Yaşa Göre Verim Düşüşü

| Yaş | Beklenen Verim Kaybı |
|-----|---------------------|
| 0-5 yıl | 0-5% |
| 5-10 yıl | 5-10% |
| 10-15 yıl | 10-20% |
| >15 yıl | 20-35% |

Not: Düzenli bakım ile verim kaybı minimize edilebilir.

## Sektörel Karşılaştırma

| Sektör | Tipik Exergy Verimi | Not |
|--------|---------------------|-----|
| Otomotiv | 40-50% | Yüksek kalite gereksinimleri |
| Gıda | 35-45% | Hijyen öncelikli |
| Tekstil | 30-40% | Genelde eski sistemler |
| Metal işleme | 35-45% | Ağır kullanım |
| Genel üretim | 35-45% | Karma |

## Kaçak Oranları

| Durum | Kaçak Oranı | Aksiyon |
|-------|-------------|---------|
| Çok iyi | < 10% | Koruyucu bakım yeterli |
| Kabul edilebilir | 10-20% | Yıllık kaçak tespiti |
| Kötü | 20-30% | Acil kaçak onarımı |
| Kritik | > 30% | Kapsamlı sistem revizyonu |

## Isı Geri Kazanım Potansiyeli

| Kompresör Gücü | Geri Kazanılabilir Isı | Tipik Kullanım |
|----------------|------------------------|----------------|
| 15-30 kW | 10-20 kW | Küçük ölçekli ısıtma |
| 30-75 kW | 20-50 kW | Proses suyu, bina ısıtma |
| 75-150 kW | 50-100 kW | Merkezi ısıtma sistemi |
| >150 kW | >100 kW | Endüstriyel proses |
```

#### `/knowledge/solutions/compressor_heat_recovery.md`

```markdown
# Çözüm: Kompresör Atık Isı Geri Kazanımı

## Özet

**Problem:** Kompresör elektrik enerjisinin ~%90'ını ısıya dönüştürür. Bu ısı genellikle atmosfere atılır.

**Çözüm:** Heat Recovery Unit (HRU) ile atık ısıyı proses suyu, bina ısıtma veya başka amaçlarla kullanmak.

**Tipik ROI:** 1-3 yıl

## Uygulanabilirlik Kriterleri

| Kriter | Minimum | İdeal |
|--------|---------|-------|
| Kompresör gücü | 15 kW | >30 kW |
| Çalışma saati | 3000 saat/yıl | >5000 saat/yıl |
| Isı kullanım mesafesi | <50 m | <20 m |
| Isı ihtiyacı sürekliliği | Sezonluk | Yıl boyu |

## Teknik Açıklama

### Isı Kaynakları
1. **Yağ soğutucu:** ~72% (en büyük kaynak, 60-80°C)
2. **Aftercooler:** ~13% (70-90°C basınçlı hava)
3. **Motor:** ~5% (genelde geri kazanılmaz)

### Geri Kazanım Yöntemleri

**Tip A: Hava-Hava (Direkt)**
- Sıcak egzoz havası kanalla yönlendirilir
- Bina ısıtma için kullanılır
- Maliyet: €500-2,000
- Sınırlama: Sadece ısıtma sezonu, mesafe kısıtı

**Tip B: Hava-Su (HRU)**
- Plakalı ısı eşanjörü ile su ısıtılır
- 50-70°C sıcak su üretilir
- Maliyet: €3,000-15,000
- Avantaj: Esnek kullanım, depolama imkanı

**Tip C: Entegre Sistem**
- OEM heat recovery paketi
- Kompresör ile birlikte tasarlanmış
- Maliyet: %10-20 ek (yeni kompresör alımında)
- Avantaj: Garanti, optimize performans

## Yatırım Maliyeti

| Kompresör Gücü | HRU Maliyeti | Kurulum | Toplam |
|----------------|--------------|---------|--------|
| 15-30 kW | €2,000-4,000 | €500-1,000 | €2,500-5,000 |
| 30-75 kW | €4,000-8,000 | €1,000-2,000 | €5,000-10,000 |
| 75-150 kW | €8,000-15,000 | €2,000-4,000 | €10,000-19,000 |
| >150 kW | €15,000-30,000 | €4,000-8,000 | €19,000-38,000 |

## Tasarruf Hesabı

```
Geri kazanılabilir ısı (kW):
Q_recovery = P_compressor × 0.70 × η_HRU

Burada:
- P_compressor = Kompresör gücü [kW]
- 0.70 = Isıya dönüşen oran
- η_HRU = HRU verimi (tipik 0.80-0.90)

Yıllık tasarruf (kWh):
E_saved = Q_recovery × kullanım_saati × eşzamanlılık_faktörü

Parasal tasarruf (€/yıl):
Savings = E_saved × alternatif_ısı_maliyeti

Alternatif ısı maliyetleri:
- Doğalgaz kazan: €0.05-0.08/kWh
- LPG kazan: €0.08-0.12/kWh
- Elektrikli ısıtma: €0.10-0.15/kWh
- Mazot kazan: €0.07-0.10/kWh
```

## Örnek ROI Hesabı

**Senaryo:** 55 kW vidalı kompresör, 5000 saat/yıl, doğalgaz alternatif

```
Q_recovery = 55 × 0.70 × 0.85 = 32.7 kW
E_saved = 32.7 × 5000 × 0.70 = 114,450 kWh/yıl
Savings = 114,450 × 0.06 = €6,867/yıl

Yatırım = €8,000 (HRU + kurulum)
Geri ödeme = 8,000 / 6,867 = 1.17 yıl
```

## Tedarikçiler

| Marka | Ürün | Özellik |
|-------|------|---------|
| Atlas Copco | ER serisi | Entegre, yüksek verim |
| Kaeser | KRAT | Modüler, retrofit uygun |
| Boge | DUOTHERM | Çift sıcaklık çıkışı |
| Bowman | EC serisi | Aftermarket, ekonomik |
| Alfa Laval | CB serisi | Yüksek kapasiteli |

## Uygulama Adımları

1. Isı tüketim noktalarını ve miktarlarını belirle
2. Kompresörden uzaklığı ve boru güzergahını planla
3. Eşzamanlılık faktörünü hesapla (ısı ihtiyacı vs kompresör çalışması)
4. HRU kapasitesi belirle (kompresör gücünün %60-70'i)
5. Minimum 3 tedarikçiden teklif al
6. Kurulum yaptır (genelde 1-2 gün)
7. Devreye alma ve performans doğrulama

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Düşük kullanım | Yaz aylarında ısı gerekmez | Absorpsiyonlu soğutma değerlendir |
| Mesafe kaybı | Uzun boruda ısı kaybı | İzolasyon, maksimum 30m |
| Legionella | Durgun sıcak suda bakteri | Su >60°C tut, sirkülasyon |
| Geri basınç | HRU kompresöre yük bindirir | OEM onaylı ürün kullan |

## Karar Matrisi

| Koşul | Öneri |
|-------|-------|
| Yıl boyu ısı ihtiyacı + >30kW | Kesinlikle uygula |
| Sezonluk ısı + >50kW | Uygula, ROI hesapla |
| Sezonluk ısı + <30kW | Dikkatli değerlendir |
| Isı ihtiyacı yok | Uygulanmaz |
```

### 2. Engine (Python Hesaplama)

#### `/engine/core.py`

```python
"""
ExergyLab - Core Thermodynamic Functions

Temel exergy hesaplama fonksiyonları.
Dead state ve yardımcı fonksiyonlar.
"""

from dataclasses import dataclass
from typing import Optional
import math

# Sabitler
R_AIR = 0.287  # kJ/kg·K - Kuru hava gaz sabiti
R_UNIVERSAL = 8.314  # J/mol·K
CP_AIR = 1.005  # kJ/kg·K - Havanın sabit basınçta özgül ısısı

@dataclass
class DeadState:
    """Referans çevre koşulları (dead state)"""
    T0: float = 298.15  # K (25°C)
    P0: float = 101.325  # kPa (1 atm)
    
    def T0_celsius(self) -> float:
        return self.T0 - 273.15
    
    @classmethod
    def from_celsius(cls, T_celsius: float, P_kPa: float = 101.325):
        return cls(T0=T_celsius + 273.15, P0=P_kPa)


@dataclass
class ExergyResult:
    """Exergy analizi sonuç yapısı"""
    exergy_in_kW: float
    exergy_out_kW: float
    exergy_destroyed_kW: float
    exergy_efficiency_pct: float
    annual_loss_kWh: Optional[float] = None
    annual_loss_EUR: Optional[float] = None
    recoverable_heat_kW: Optional[float] = None
    
    def to_dict(self) -> dict:
        return {
            'exergy_in_kW': round(self.exergy_in_kW, 2),
            'exergy_out_kW': round(self.exergy_out_kW, 2),
            'exergy_destroyed_kW': round(self.exergy_destroyed_kW, 2),
            'exergy_efficiency_pct': round(self.exergy_efficiency_pct, 1),
            'annual_loss_kWh': round(self.annual_loss_kWh, 0) if self.annual_loss_kWh else None,
            'annual_loss_EUR': round(self.annual_loss_EUR, 0) if self.annual_loss_EUR else None,
            'recoverable_heat_kW': round(self.recoverable_heat_kW, 2) if self.recoverable_heat_kW else None,
        }


def heat_exergy(Q_kW: float, T_K: float, dead_state: DeadState = None) -> float:
    """
    Isı transferinin exergy'sini hesaplar.
    
    Ex_Q = Q × (1 - T₀/T)
    
    Args:
        Q_kW: Isı transfer hızı [kW]
        T_K: Isı transferi sıcaklığı [K]
        dead_state: Dead state koşulları
        
    Returns:
        Exergy [kW]
    """
    if dead_state is None:
        dead_state = DeadState()
    
    if T_K <= dead_state.T0:
        # Soğutma durumu - Carnot çarpanı negatif
        return Q_kW * (dead_state.T0 / T_K - 1)
    else:
        # Isıtma durumu
        return Q_kW * (1 - dead_state.T0 / T_K)


def carnot_factor(T_hot_K: float, T_cold_K: float) -> float:
    """
    Carnot faktörü (maksimum teorik verim)
    
    η_carnot = 1 - T_cold / T_hot
    """
    return 1 - T_cold_K / T_hot_K


def celsius_to_kelvin(T_C: float) -> float:
    """Celsius'u Kelvin'e çevirir"""
    return T_C + 273.15


def kelvin_to_celsius(T_K: float) -> float:
    """Kelvin'i Celsius'a çevirir"""
    return T_K - 273.15


def bar_to_kpa(P_bar: float) -> float:
    """Bar'ı kPa'ya çevirir"""
    return P_bar * 100


def kpa_to_bar(P_kPa: float) -> float:
    """kPa'yı bar'a çevirir"""
    return P_kPa / 100


def m3_min_to_m3_s(V_m3_min: float) -> float:
    """m³/min'i m³/s'ye çevirir"""
    return V_m3_min / 60


def air_density(T_K: float, P_kPa: float) -> float:
    """
    İdeal gaz yasasıyla hava yoğunluğu
    
    ρ = P / (R × T)
    """
    return P_kPa / (R_AIR * T_K)
```

#### `/engine/compressor.py`

```python
"""
ExergyLab - Compressor Exergy Analysis

Kompresör exergy hesaplamaları.
Vidalı, pistonlu ve diğer kompresör tipleri için.
"""

from dataclasses import dataclass
from typing import Optional
import math

from .core import (
    DeadState, ExergyResult, 
    R_AIR, celsius_to_kelvin, bar_to_kpa, 
    m3_min_to_m3_s, air_density, heat_exergy
)


@dataclass
class CompressorInput:
    """Kompresör analizi için giriş verileri"""
    
    # Zorunlu
    power_kW: float              # Elektrik gücü [kW]
    flow_rate_m3_min: float      # Hava debisi [m³/min]
    outlet_pressure_bar: float   # Çıkış basıncı [bar]
    
    # Opsiyonel - ölçülen
    inlet_temp_C: Optional[float] = None    # Giriş sıcaklığı [°C]
    outlet_temp_C: Optional[float] = None   # Çıkış sıcaklığı [°C]
    ambient_temp_C: Optional[float] = None  # Ortam sıcaklığı [°C]
    
    # Operasyonel
    operating_hours: float = 4000           # Yıllık çalışma [saat]
    load_factor: float = 0.75               # Yük faktörü [0-1]
    
    # Ekonomik
    electricity_price_eur_kwh: float = 0.10  # Elektrik fiyatı [€/kWh]
    
    # Ekipman bilgisi
    compressor_type: str = "screw"          # screw, piston, scroll, centrifugal
    brand: Optional[str] = None
    model: Optional[str] = None
    age_years: Optional[int] = None
    
    def __post_init__(self):
        """Varsayılan değerleri ayarla"""
        if self.ambient_temp_C is None:
            self.ambient_temp_C = 25.0
        if self.inlet_temp_C is None:
            self.inlet_temp_C = self.ambient_temp_C
        if self.outlet_temp_C is None:
            # Tip bazlı varsayılan çıkış sıcaklığı
            defaults = {
                'screw': 85,
                'piston': 140,
                'scroll': 90,
                'centrifugal': 120
            }
            self.outlet_temp_C = defaults.get(self.compressor_type, 85)


@dataclass 
class CompressorResult(ExergyResult):
    """Kompresör analizi sonuçları"""
    
    # Ek kompresör-spesifik sonuçlar
    mass_flow_kg_s: Optional[float] = None
    specific_power_kW_m3min: Optional[float] = None
    heat_recovery_potential_kW: Optional[float] = None
    heat_recovery_savings_eur_year: Optional[float] = None
    benchmark_comparison: Optional[str] = None  # "poor", "average", "good", "excellent"
    
    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            'mass_flow_kg_s': round(self.mass_flow_kg_s, 4) if self.mass_flow_kg_s else None,
            'specific_power_kW_m3min': round(self.specific_power_kW_m3min, 2) if self.specific_power_kW_m3min else None,
            'heat_recovery_potential_kW': round(self.heat_recovery_potential_kW, 2) if self.heat_recovery_potential_kW else None,
            'heat_recovery_savings_eur_year': round(self.heat_recovery_savings_eur_year, 0) if self.heat_recovery_savings_eur_year else None,
            'benchmark_comparison': self.benchmark_comparison,
        })
        return base


def analyze_compressor(input_data: CompressorInput, dead_state: DeadState = None) -> CompressorResult:
    """
    Kompresör exergy analizi yapar.
    
    Args:
        input_data: Kompresör giriş verileri
        dead_state: Dead state koşulları (opsiyonel)
        
    Returns:
        CompressorResult: Analiz sonuçları
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)
    
    # Birim dönüşümleri
    T_in_K = celsius_to_kelvin(input_data.inlet_temp_C)
    T_out_K = celsius_to_kelvin(input_data.outlet_temp_C)
    P_out_kPa = bar_to_kpa(input_data.outlet_pressure_bar)
    V_dot_m3_s = m3_min_to_m3_s(input_data.flow_rate_m3_min)
    
    # Kütle debisi
    rho = air_density(T_in_K, dead_state.P0)
    m_dot = V_dot_m3_s * rho  # kg/s
    
    # 1. Giren exergy (elektrik)
    Ex_in = input_data.power_kW
    
    # 2. Çıkan exergy (basınçlı hava)
    # İdeal gaz için: Ex_air = ṁ × R × T₀ × ln(P₂/P₁)
    pressure_ratio = P_out_kPa / dead_state.P0
    Ex_out = m_dot * R_AIR * dead_state.T0 * math.log(pressure_ratio)
    
    # 3. Exergy yıkımı
    Ex_destroyed = Ex_in - Ex_out
    
    # 4. Exergy verimi
    eta_ex = (Ex_out / Ex_in) * 100 if Ex_in > 0 else 0
    
    # 5. Yıllık kayıp
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.electricity_price_eur_kwh
    
    # 6. Isı geri kazanım potansiyeli
    # Atık ısının exergy değeri
    heat_recovery_potential = heat_exergy(Ex_destroyed, T_out_K, dead_state)
    
    # Termal tasarruf (doğalgaz alternatifi varsayımıyla)
    gas_price_eur_kwh = 0.06  # Yaklaşık doğalgaz fiyatı
    recoverable_thermal = Ex_destroyed * 0.70 * 0.85  # %70 ısıya, %85 HRU verimi
    heat_recovery_savings = recoverable_thermal * input_data.operating_hours * 0.70 * gas_price_eur_kwh
    
    # 7. Spesifik güç
    specific_power = input_data.power_kW / input_data.flow_rate_m3_min
    
    # 8. Benchmark karşılaştırma
    benchmark = _get_benchmark_comparison(eta_ex, input_data.compressor_type)
    
    return CompressorResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        recoverable_heat_kW=heat_recovery_potential,
        mass_flow_kg_s=m_dot,
        specific_power_kW_m3min=specific_power,
        heat_recovery_potential_kW=recoverable_thermal,
        heat_recovery_savings_eur_year=heat_recovery_savings,
        benchmark_comparison=benchmark
    )


def _get_benchmark_comparison(eta_ex: float, compressor_type: str) -> str:
    """
    Exergy verimine göre benchmark karşılaştırması yapar.
    """
    # Tip bazlı benchmark aralıkları
    benchmarks = {
        'screw': {'poor': 30, 'average': 45, 'good': 55, 'excellent': 60},
        'piston': {'poor': 25, 'average': 40, 'good': 50, 'excellent': 55},
        'scroll': {'poor': 30, 'average': 45, 'good': 55, 'excellent': 60},
        'centrifugal': {'poor': 35, 'average': 50, 'good': 60, 'excellent': 65},
    }
    
    thresholds = benchmarks.get(compressor_type, benchmarks['screw'])
    
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


def get_compressor_recommendations(result: CompressorResult, input_data: CompressorInput) -> list:
    """
    Analiz sonuçlarına göre iyileştirme önerileri üretir.
    
    Returns:
        List of recommendation dictionaries
    """
    recommendations = []
    
    # 1. Isı geri kazanımı değerlendirmesi
    if input_data.power_kW >= 15 and result.heat_recovery_savings_eur_year > 1000:
        investment = _estimate_hru_cost(input_data.power_kW)
        payback = investment / result.heat_recovery_savings_eur_year if result.heat_recovery_savings_eur_year > 0 else float('inf')
        
        recommendations.append({
            'type': 'heat_recovery',
            'title': 'Atık Isı Geri Kazanımı',
            'description': f'Kompresör atık ısısından yılda {result.heat_recovery_savings_eur_year:.0f} € tasarruf potansiyeli',
            'investment_eur': investment,
            'savings_eur_year': result.heat_recovery_savings_eur_year,
            'payback_years': payback,
            'priority': 'high' if payback < 2 else 'medium' if payback < 4 else 'low'
        })
    
    # 2. Verim düşükse genel öneriler
    if result.benchmark_comparison in ['poor', 'below_average']:
        recommendations.append({
            'type': 'maintenance',
            'title': 'Bakım ve Kontrol',
            'description': 'Exergy verimi düşük. Filtre, yağ, conta kontrolü önerilir.',
            'investment_eur': 500,
            'savings_eur_year': result.annual_loss_EUR * 0.10,  # %10 iyileşme varsayımı
            'payback_years': 500 / (result.annual_loss_EUR * 0.10) if result.annual_loss_EUR > 0 else float('inf'),
            'priority': 'high'
        })
    
    # 3. Spesifik güç yüksekse
    if result.specific_power_kW_m3min > 7.0:
        recommendations.append({
            'type': 'pressure_optimization',
            'title': 'Basınç Optimizasyonu',
            'description': 'Spesifik güç yüksek. Sistem basıncını düşürme imkanı araştırılmalı.',
            'investment_eur': 0,
            'savings_eur_year': result.annual_loss_EUR * 0.07,  # Her 1 bar = %7 tasarruf
            'payback_years': 0,
            'priority': 'high'
        })
    
    return recommendations


def _estimate_hru_cost(power_kW: float) -> float:
    """HRU yatırım maliyeti tahmini"""
    if power_kW < 30:
        return 3500
    elif power_kW < 75:
        return 7000
    elif power_kW < 150:
        return 12000
    else:
        return 25000
```

#### `/engine/utils.py`

```python
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
```

### 3. Skill Dosyası (Claude Code için)

#### `/skills/SKILL_exergy_calculator.md`

```markdown
# SKILL: Exergy Calculator

## Bu skill ne yapar?

Bu skill, endüstriyel ekipmanların exergy analizini yapar. Kullanıcıdan ekipman bilgilerini ve ölçüm verilerini alır, Python engine kullanarak hesaplama yapar, sonuçları yorumlar ve öneriler sunar.

## Ne zaman kullanılır?

- Kullanıcı bir ekipmanın exergy analizi istediğinde
- Kullanıcı enerji verimliliği veya kayıp hesabı istediğinde
- "Kompresör analizi yap", "Kazan verimliliğini hesapla" gibi isteklerde

## Çalışma adımları

### 1. Ekipman tipini belirle

Kullanıcıdan ekipman tipini öğren:
- Kompresör (vidalı, pistonlu, scroll, santrifüj)
- Kazan (buhar, kızgın su)
- Isı eşanjörü
- Chiller
- Pompa
- Motor

### 2. Gerekli verileri topla

`/knowledge/equipment/` altındaki ilgili MD dosyasını oku.
Zorunlu ve opsiyonel parametreleri kullanıcıya sor.

Örnek (kompresör için):
- Elektrik gücü (kW) - zorunlu
- Hava debisi (m³/min) - zorunlu
- Çıkış basıncı (bar) - zorunlu
- Giriş/çıkış sıcaklıkları (°C) - opsiyonel
- Çalışma saati (saat/yıl) - varsayılan 4000
- Elektrik fiyatı (€/kWh) - varsayılan 0.10

### 3. Hesaplamayı çalıştır

`/engine/` altındaki Python modüllerini kullan.

```python
from engine.compressor import CompressorInput, analyze_compressor

input_data = CompressorInput(
    power_kW=32,
    flow_rate_m3_min=6.2,
    outlet_pressure_bar=7.5,
    # ... diğer parametreler
)

result = analyze_compressor(input_data)
```

### 4. Sonuçları yorumla

`/knowledge/benchmarks/` dosyalarını kullanarak:
- Exergy verimini sektör ortalamasıyla karşılaştır
- İyi/kötü/ortalama değerlendirmesi yap

### 5. Çözüm önerileri sun

`/knowledge/solutions/` dosyalarını tarayarak:
- Uygun çözümleri belirle
- ROI hesabı yap
- Önceliklendirme yap

### 6. Sonuçları raporla

Kullanıcıya şu formatta sun:

```
## Exergy Analizi Sonuçları

**Ekipman:** [Tip] - [Marka/Model]

### Temel Metrikler
| Metrik | Değer |
|--------|-------|
| Giren Exergy | XX.X kW |
| Çıkan Exergy | XX.X kW |
| Exergy Yıkımı | XX.X kW |
| Exergy Verimi | XX.X% |

### Benchmark Karşılaştırma
[Sektör ortalamasına göre değerlendirme]

### Yıllık Etki
- Kayıp: XX,XXX kWh/yıl
- Maliyet: €X,XXX/yıl

### İyileştirme Önerileri
1. [Öneri 1] - ROI: X.X yıl
2. [Öneri 2] - ROI: X.X yıl
```

## Dikkat edilecekler

1. **Birim tutarlılığı:** Kullanıcı farklı birimler kullanabilir (PSI, CFM, °F). Dönüşüm yap.

2. **Eksik veri:** Zorunlu veri yoksa sor. Opsiyonel veri yoksa varsayılan kullan ve belirt.

3. **Doğrulama:** Mantıksız değerleri sorgula (örn: %150 verim, negatif sıcaklık Kelvin'de)

4. **Hesaplama vs Yorum:** Hesaplama deterministik (engine). Yorum ve öneri AI (sen).

## Örnek diyalog

**Kullanıcı:** Fabrikamızdaki kompresörü analiz etmek istiyorum.

**AI:** Kompresör exergy analizi için bilgilere ihtiyacım var.

Kompresör tipi nedir?
- Vidalı
- Pistonlu
- Scroll
- Santrifüj

**Kullanıcı:** Vidalı, Atlas Copco GA37

**AI:** GA37 için şu bilgileri girebilir misin?

Zorunlu:
- Ölçülen elektrik gücü (kW): [nameplate 37 kW, ama ölçülen değer daha doğru]
- Hava debisi (m³/min): [nameplate'te yazar, veya ölçüm]
- Çıkış basıncı (bar): [manometreden oku]

Opsiyonel (daha detaylı analiz için):
- Çıkış havası sıcaklığı (°C)
- Yıllık çalışma saati
- Elektrik fiyatı (€/kWh)

**Kullanıcı:** Güç 32 kW ölçtüm, debi 6.2 m³/min, basınç 7.5 bar. Çıkış sıcaklığı 85°C. Yılda 6000 saat çalışıyor.

**AI:** [Hesaplama çalıştırır, sonuçları sunar, öneriler verir]
```

### 4. Requirements

#### `/requirements.txt`

```
# ExergyLab Dependencies

# Termodinamik hesaplamalar
CoolProp>=6.4.0

# Veri işleme
numpy>=1.21.0
pandas>=1.3.0

# Görselleştirme
plotly>=5.0.0
matplotlib>=3.4.0

# Web arayüzü (opsiyonel, sonraki aşama)
streamlit>=1.20.0
# fastapi>=0.95.0
# uvicorn>=0.21.0

# Rapor üretimi
reportlab>=3.6.0
python-docx>=0.8.11

# Yardımcı
python-dotenv>=0.19.0
pydantic>=1.9.0

# Test
pytest>=7.0.0
```

---

## 🚀 Claude Code İçin Başlangıç Talimatları

Bu dosyayı okuduktan sonra şu adımları izle:

### Adım 1: Proje yapısını oluştur

```bash
mkdir -p exergy-lab/{knowledge/{equipment,benchmarks,solutions,formulas,methodology},skills,engine,data/{projects,templates},output/{reports,charts},tests}
```

### Adım 2: Knowledge base dosyalarını oluştur

Yukarıdaki MD içeriklerini ilgili dosyalara yaz:
- `/knowledge/equipment/compressor_screw.md`
- `/knowledge/formulas/compressor_exergy.md`
- `/knowledge/benchmarks/compressor_benchmarks.md`
- `/knowledge/solutions/compressor_heat_recovery.md`

### Adım 3: Engine modüllerini oluştur

Python dosyalarını yaz:
- `/engine/__init__.py`
- `/engine/core.py`
- `/engine/compressor.py`
- `/engine/utils.py`

### Adım 4: Skill dosyasını oluştur

- `/skills/SKILL_exergy_calculator.md`

### Adım 5: Test et

```python
# Test scripti
from engine.compressor import CompressorInput, analyze_compressor

# Örnek veri
input_data = CompressorInput(
    power_kW=32,
    flow_rate_m3_min=6.2,
    outlet_pressure_bar=7.5,
    outlet_temp_C=85,
    operating_hours=6000,
    electricity_price_eur_kwh=0.10
)

result = analyze_compressor(input_data)
print(result.to_dict())
```

### Adım 6: Bana sonuçları göster

Projeyi oluşturduktan sonra:
1. Klasör yapısını göster
2. Test sonuçlarını göster
3. Varsa hataları bildir

---

## 📝 Notlar

- Bu internal bir tool, kullanıcı sadece Kemal
- Hesaplamalar deterministik, yorumlamalar AI
- Knowledge base genişletilebilir yapıda
- İlk sprint sadece kompresör, sonra diğer ekipmanlar eklenecek
- Web arayüzü sonraki aşamada

---

**Bu doküman ExergyLab projesinin tek kaynak noktasıdır (single source of truth).**
