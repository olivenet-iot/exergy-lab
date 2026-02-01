# Vidalı Kompresör — Yağlı (Oil-Injected Screw Compressor)

> Son güncelleme: 2026-01-31

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

## Spesifik Güç Tüketimi (SPC)

| Alt Tip | SPC @ 7 bar | Not |
|---------|-------------|-----|
| Sabit hızlı (tipik) | 6.0-7.5 kW/m³/min | Piyasa ortalaması |
| Sabit hızlı (best-in-class) | ~5.5 kW/m³/min | Modern, IE4 motor |
| VSD (tipik) | 5.5-7.0 kW/m³/min | Değişken yükte avantajlı |
| VSD (best-in-class) | ~5.5 kW/m³/min | iPM motor, optimize airend |

## Kısmi Yük Davranışı — Load/Unload Kontrol

| Yük % | Güç % | Efektif SPC % |
|--------|-------|--------------|
| 100% | 100% | 100% |
| 75% | ~83% | ~111% |
| 50% | ~67% | ~134% |
| 25% | ~50% | ~200% |
| 0% (boşta) | 25-30% | ∞ |

VSD ile kısmi yük performansı için bkz. `solutions/compressor_vsd.md`

## Dikkat Edilecekler

1. **Yük/boşta çalışma**: Boşta bile %25-30 güç çeker — VSD veya uygun kontrol stratejisi değerlendirilmeli
2. **Basınç kaybı**: Her 1 bar düşüş ≈ %6-7 enerji tasarrufu
3. **Sıcaklık**: Giriş havası her 3°C düşüşü ≈ %1 verim artışı
4. **Kaçaklar**: Tipik tesiste %20-30 hava kaçağı var
5. **Filtre**: Tıkalı filtre basınç düşürür, enerji artar — inlet filter her 2000-4000 saatte kontrol
6. **Isı geri kazanımı**: Giren enerjinin ~%72'si yağ soğutucudan geri kazanılabilir — bkz. `solutions/compressor_heat_recovery.md`
7. **Yaş etkisi**: 10+ yıllık kompresörlerde %10-20 verim kaybı beklenir — düzenli bakım ile azaltılabilir

## İlgili Dosyalar
- Yağsız tip: `equipment/compressor_screw_oilfree.md`
- Benchmark verileri: `benchmarks/compressor_benchmarks.md`
- VSD çözümü: `solutions/compressor_vsd.md`
- Isı geri kazanımı: `solutions/compressor_heat_recovery.md`
- Exergy hesaplamaları: `formulas/compressor_exergy.md`

## Referanslar
- Atlas Copco Compressed Air Manual, 9th Edition
- CAGI Compressed Air & Gas Handbook, 7th Edition
- DOE/AMO, "Improving Compressed Air System Performance: A Sourcebook for Industry"
- Kaeser Compressors Technical Documentation
