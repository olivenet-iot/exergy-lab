# Vakum Pompaları — Vacuum Pumps

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Negatif basınç üreten (atmosfer altı) pompa sistemleri
- Kapasite aralığı: 10 - 10,000+ m³/h
- Vakum aralığı: 1013 mbar (atmosfer) - 0.001 mbar (yüksek vakum)
- Yaygın markalar: Busch, Leybold, Edwards, Becker, Atlas Copco, Pfeiffer, Gardner Denver

## Alt Tipler ve Çalışma Prensipleri

### 1. Sıvı Halkalı Pompa (Liquid Ring Pump)
Gövde içinde eksantrik monte edilmiş çark dönerek sıvı (genellikle su) halkası oluşturur. Çark kanatları arasındaki hacim değişimi ile gaz sıkıştırılır ve vakum oluşur. Sızdırmazlık ve soğutma sıvı halkası tarafından sağlanır.
- Vakum aralığı: 33 - 1013 mbar
- Verim: %25-50
- Avantaj: Nemli ve korozif gazlara dayanıklı, basit yapı
- Dezavantaj: Yüksek enerji tüketimi, sıvı tüketimi

### 2. Kuru Vidalı Pompa (Dry Screw Pump)
İki helisel rotor temassız olarak dönerek gazı giriş tarafından çıkış tarafına iter ve sıkıştırır. Yağlama gerektirmez — tamamen kuru çalışır.
- Vakum aralığı: 0.01 - 1013 mbar
- Verim: %50-80
- Avantaj: Yağsız, düşük bakım, geniş vakum aralığı
- Dezavantaj: Yüksek yatırım maliyeti, pulsasyona duyarlı gazlarda dikkat

### 3. Roots Blower (Vakum Tarafı)
İki loblu rotor senkronize dönerek gazı iter. Tek başına derin vakum üretemez — genellikle ön pompa (backing pump) ile kombineli kullanılır.
- Vakum aralığı: 0.01 - 100 mbar (ön pompa ile birlikte)
- Verim: %40-60
- Avantaj: Yüksek debi kapasitesi, hızlı boşaltma
- Dezavantaj: Tek başına kullanılamaz, gürültülü

### 4. Döner Kanatlı Pompa (Rotary Vane Pump)
Eksantrik monteli rotor üzerindeki yay destekli kanatlar gövdeye temas ederek hücre hacimleri oluşturur. Hacim değişimi ile gaz sıkıştırılır. Yağlı tip yaygındır.
- Vakum aralığı: 0.1 - 1013 mbar
- Verim: %50-75
- Avantaj: Kompakt, ucuz, sessiz çalışma
- Dezavantaj: Yağ kontaminasyonu riski, kanat aşınması

### 5. Difüzyon Pompaları (Diffusion Pumps)
Yüksek hızlı yağ veya cıva buharı jetleri ile gaz molekülleri sürüklenerek pompalanır. Mekanik hareketli parçası yoktur.
- Vakum aralığı: 10⁻² - 10⁻⁷ mbar (yüksek ve ultra-yüksek vakum)
- Avantaj: Çok düşük basınçlara ulaşabilir, titreşimsiz
- Dezavantaj: Ön pompaya ihtiyaç, yağ buharı geri difüzyonu riski

## Alt Tip Karşılaştırma

| Özellik | Sıvı Halkalı | Kuru Vidalı | Roots | Döner Kanatlı | Difüzyon |
|---------|-------------|------------|-------|--------------|----------|
| Vakum aralığı (mbar) | 33-1013 | 0.01-1013 | 0.01-100* | 0.1-1013 | 10⁻²-10⁻⁷ |
| Debi aralığı (m³/h) | 25-10,000+ | 10-2,500 | 100-15,000 | 4-630 | 100-50,000 L/s |
| Tipik verim (%) | 25-50 | 50-80 | 40-60 | 50-75 | — |
| Enerji tüketimi | Yüksek | Orta | Orta-yüksek | Orta | Düşük (elektrikli) |
| Bakım | Basit | Düşük | Basit | Orta (kanat) | Düşük |
| Yatırım maliyeti | Orta | Yüksek | Orta | Düşük | Orta-yüksek |

*Roots: ön pompa ile kombineli kullanımda

## Enerji Dağılımı (Tipik)
- Gaz sıkıştırma (faydalı iş — vakum üretimi): %20-40
- Sızdırmazlık/soğutma kayıpları: %15-25 (sıvı halkalıda yüksek)
- Mekanik sürtünme kayıpları: %10-20
- Motor kayıpları: %5-10
- Radyasyon ve diğer kayıplar: %5-10

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 1-500 | Güç analizörü veya CT + voltaj |
| Vakum basıncı (emme) | mbar | 0.001-1013 | Vakum manometresi / transmitter |
| Gaz debisi | m³/h | 10-10,000+ | Flowmeter (termal kütle, pitot) |
| Ortam sıcaklığı | °C | 15-40 | Termometre |

### Opsiyonel (daha detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Çıkış sıcaklığı | °C | 40-120 | Termometre |
| Sızdırmazlık sıvısı sıcaklığı | °C | 15-50 | Termometre (sıvı halkalı) |
| Sızdırmazlık sıvısı debisi | m³/h | 0.5-50 | Debimetre |
| Sızıntı oranı | mbar·L/s | 0.01-10 | Sızıntı dedektörü |
| Yük oranı | % | 0-100 | Kontrol paneli veya akım |
| Çalışma saati | saat/yıl | 2000-8760 | Sayaç veya tahmin |

### Nameplate Bilgileri
- Marka ve model
- Nominal güç (kW)
- Nominal emme kapasitesi (m³/h)
- Nihai vakum basıncı (mbar)
- Pompa tipi (sıvı halkalı, kuru vidalı vb.)
- Sızdırmazlık sıvısı tipi ve debisi (varsa)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Pompa verimi | %40 | Genel ortalama (tipe bağlı) |
| Motor verimi | %90 | IE3 motor varsayımı |
| Çalışma saati | 4000 saat/yıl | Tek vardiya |
| Yük oranı | 75% | Endüstriyel ortalama |
| Sızıntı oranı | Nominal kapasitenin %10'u | Orta bakım seviyesi |
| Vakum basıncı | 100 mbar | Orta vakum uygulaması |
| cosφ (güç faktörü) | 0.85 | Tipik motor değeri |

## Spesifik Enerji Tüketimi

| Pompa Tipi | Spesifik Enerji @ 100 mbar | Not |
|------------|---------------------------|-----|
| Sıvı halkalı (tipik) | 0.03-0.06 kW/(m³/h) | En yüksek tüketim |
| Sıvı halkalı (VSD) | 0.02-0.04 kW/(m³/h) | VSD ile %30-50 tasarruf |
| Kuru vidalı (tipik) | 0.015-0.03 kW/(m³/h) | %20-40 daha verimli |
| Kuru vidalı (best-in-class) | 0.01-0.02 kW/(m³/h) | Modern, VSD kontrollü |
| Döner kanatlı (tipik) | 0.02-0.04 kW/(m³/h) | Orta ölçekli uygulamalar |
| Roots + ön pompa | 0.02-0.05 kW/(m³/h) | Debi ve vakuma bağlı |

## Verimlilik Kıyaslaması (Benchmarks)

| Kategori | Spesifik Enerji Tüketimi | Not |
|----------|--------------------------|-----|
| Düşük | >0.05 kW/(m³/h) | Eski sıvı halkalı, bakımsız |
| Ortalama | 0.03-0.05 kW/(m³/h) | Standart sistem |
| İyi | 0.02-0.03 kW/(m³/h) | VSD, doğru boyutlama |
| Best-in-class | <0.02 kW/(m³/h) | Modern kuru vidalı + VSD + sızıntı kontrolü |

## Exergy Analizi — Vakum Exergysi Hesabı

Vakum ortamında exergy, atmosferik basınçtan sapma ile ilişkilidir. Atmosfer altı basınçlarda da exergy mevcuttur.

```
Vakum exergysi (izothermal, ideal gaz yaklaşımı):

Ex_vakum = n × R × T₀ × ln(P₀ / P_vakum)

Burada:
  Ex_vakum  = Vakum exergysi (kJ/mol veya kW)
  n         = Mol debisi (mol/s)
  R         = Evrensel gaz sabiti (8.314 J/mol·K)
  T₀        = Referans (ortam) sıcaklığı (K)
  P₀        = Atmosfer basıncı (1013 mbar)
  P_vakum   = Vakum basıncı (mbar)

Exergy verimi:
η_ex = Ex_vakum / W_elektrik

Burada:
  W_elektrik = Pompaya verilen elektrik gücü (kW)
```

### Örnek Hesaplama
100 m³/h hava, 100 mbar vakumda, ortam 25°C:
- P₀/P_vakum = 1013/100 = 10.13
- ln(10.13) = 2.315
- n = (100 m³/h × 100/1013) / (0.0224 m³/mol × 3600) ≈ 0.122 mol/s
- Ex_vakum = 0.122 × 8.314 × 298 × 2.315 ≈ 700 W = 0.70 kW

## Endüstriyel Uygulamalar

| Sektör | Tipik Vakum (mbar) | Uygulama | Tercih Edilen Tip |
|--------|-------------------|----------|-------------------|
| Ambalaj | 5-100 | Termoform, MAP, vakumlu paketleme | Döner kanatlı, kuru vidalı |
| Gıda | 10-300 | Kurutma, buharlaştırma, soğutma | Sıvı halkalı, kuru vidalı |
| Kimya | 1-500 | Distilasyon, filtrasyon, kurutma | Sıvı halkalı, kuru vidalı |
| İlaç | 0.1-100 | Liyofilizasyon, kurutma, kaplama | Kuru vidalı, roots + ön pompa |
| Elektronik | 10⁻³-1 | Kaplama, aşındırma, implantasyon | Difüzyon, turbo-moleküler |
| Metalürji | 0.01-10 | Vakum eritme, ısıl işlem | Roots + kuru vidalı |
| Plastik | 100-800 | Ekstrüzyon degassing, kalıplama | Sıvı halkalı, döner kanatlı |
| Kağıt | 300-600 | Su alma (dewatering) | Sıvı halkalı |

## Enerji Tasarrufu Fırsatları

### 1. VSD (Değişken Hız Sürücü) Uygulaması
- Sabit devirli pompaya VSD eklenmesi
- Vakum seviyesine göre otomatik hız ayarı
- Tipik tasarruf: %30-55 (Atlas Copco, Busch verilerine göre)

### 2. Sızıntı Tespiti ve Onarımı
- Tipik sistemlerde vakum sızıntısı kapasitenin %10-30'unu tüketir
- Ultrasonik sızıntı dedektörü ile tespit
- Sızıntı onarımı sonrası pompa daha küçük boyuta veya düşük devire indirilebilir

### 3. Teknoloji Değişikliği
| Mevcut | Yeni Teknoloji | Tipik Tasarruf | Yatırım Geri Dönüşü |
|--------|---------------|---------------|---------------------|
| Sıvı halkalı | Kuru vidalı + VSD | %30-50 | 2-4 yıl |
| Sabit devirli | VSD retrofit | %30-55 | 1-3 yıl |
| Merkezi vakum (oversized) | Dağıtık küçük pompalar | %20-40 | 2-5 yıl |

### 4. Uygun Vakum Seviyesi Seçimi
- Gerekenden daha derin vakum = gereksiz enerji tüketimi
- Her 100 mbar daha derin vakum ≈ %5-15 ek enerji (logaritmik artış)
- Proses ihtiyacı analiz edilmeli ve vakum seviyesi optimize edilmeli

## Dikkat Edilecekler

1. **Sızıntı:** Vakum sistemlerinde sızıntı en büyük enerji kaybı kaynağıdır — düzenli sızıntı testi yapılmalı
2. **Aşırı boyutlama:** Güvenlik marjı ile aşırı büyük pompa seçimi yaygın sorun — %20-30 verim kaybına neden olur
3. **Uygun vakum seviyesi:** Prosesin gerçekten ihtiyacı olan vakum seviyesi belirlenip, gereksiz derin vakumdan kaçınılmalı
4. **Sızdırmazlık sıvısı:** Sıvı halkalı pompalarda sıvı sıcaklığı kontrolü kritik — yüksek sıcaklık kapasite düşürür
5. **Gaz kontaminasyonu:** Proses gazlarının pompa ile uyumluluğu kontrol edilmeli (korozyon, polimerizasyon riski)
6. **Gürültü:** Özellikle roots blower'lar çok gürültülü — ses izolasyonu gerekli
7. **Yaş etkisi:** 10+ yıllık pompalarda %15-25 kapasite kaybı beklenir — performans testi önerilir

## İlgili Dosyalar
- Pompa motorları: `equipment/pump_motors_drives.md`
- Pompa sistemleri genel: `equipment/pumping_systems_overview.md`
- Hidrofor: `equipment/pump_booster.md`
- Roots blower: `equipment/compressor_roots.md`

## Referanslar
- Busch Vacuum Solutions — Vacuum Technology Handbook
- Atlas Copco, "Energy Efficiency in Vacuum Systems"
- Leybold, "Fundamentals of Vacuum Technology"
- Pfeiffer Vacuum, "Vacuum Technology Know-How"
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition
- Oerlikon Leybold Vacuum, "Vacuum Technology: Its Foundations, Formulae, and Tables"
- Edwards, "Vacuum Pump Selection Guide"
