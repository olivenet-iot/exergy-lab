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
