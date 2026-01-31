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
