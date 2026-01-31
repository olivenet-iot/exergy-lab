# ExergyLab

Endüstriyel tesislerde termodinamik performans analizi yapan internal tool. Exergy (kullanılabilir enerji) kavramını kullanarak sistemlerdeki gerçek verimsizlikleri tespit eder, sayısallaştırır ve çözüm önerileri sunar.

**Temel felsefe:** "Entropi avcılığı" — enerji kayıplarını değil, exergy yıkımını (gerçek termodinamik kaybı) bulmak.

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanım

### Kompresör Exergy Analizi

```python
from engine.compressor import CompressorInput, analyze_compressor, get_compressor_recommendations

# Giriş verilerini tanımla
input_data = CompressorInput(
    power_kW=32,                    # Ölçülen elektrik gücü
    flow_rate_m3_min=6.2,           # Hava debisi
    outlet_pressure_bar=7.5,        # Çıkış basıncı
    outlet_temp_C=85,               # Çıkış sıcaklığı (opsiyonel)
    operating_hours=6000,           # Yıllık çalışma saati
    electricity_price_eur_kwh=0.10  # Elektrik birim fiyatı
)

# Analizi çalıştır
result = analyze_compressor(input_data)
print(result.to_dict())

# İyileştirme önerilerini al
recommendations = get_compressor_recommendations(result, input_data)
for rec in recommendations:
    print(f"- {rec['title']}: {rec['description']}")
```

### Dead State Ayarlama

Varsayılan referans koşulları (25°C, 1 atm) değiştirilebilir:

```python
from engine.core import DeadState

dead_state = DeadState.from_celsius(T_celsius=30, P_kPa=101.325)
result = analyze_compressor(input_data, dead_state=dead_state)
```

## Proje Yapısı

```
exergy-lab/
├── knowledge/          # Bilgi tabanı (MD dosyaları)
│   ├── equipment/      # Ekipman tanımları ve ölçüm gereksinimleri
│   ├── benchmarks/     # Sektörel benchmark verileri
│   ├── solutions/      # Çözüm önerileri ve ROI bilgileri
│   ├── formulas/       # Termodinamik denklemler
│   └── methodology/    # Audit süreci ve rehberler
├── engine/             # Python hesaplama motoru
│   ├── core.py         # Temel exergy fonksiyonları
│   ├── compressor.py   # Kompresör hesaplamaları
│   └── utils.py        # Yardımcı fonksiyonlar
├── skills/             # Claude Code skill dosyaları
├── app/                # Web arayüzü (sonraki aşama)
├── data/               # Proje verileri
├── output/             # Raporlar ve grafikler
└── tests/              # Unit testler
```

## Desteklenen Ekipmanlar

| Ekipman | Durum |
|---------|-------|
| Kompresör (vidalı, pistonlu, scroll, santrifüj) | Aktif |
| Kazan | Planlanan |
| Isı eşanjörü | Planlanan |
| Chiller | Planlanan |

## Temel Kavramlar

- **Exergy**: Bir sistemin çevresiyle dengeye gelene kadar yapabileceği maksimum iş
- **Dead State**: Referans çevre koşulları (varsayılan: 25°C, 1 atm)
- **Exergy yıkımı**: Her süreçte kaybedilen kullanılabilir enerji = T₀ × Entropi üretimi
- **Exergy verimi**: Çıkan exergy / Giren exergy × 100
