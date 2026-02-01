# Santrifüj Kompresör (Centrifugal Compressor)

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Dinamik (kinetik enerji → basınç enerjisi)
- Kapasite aralığı: 150 - 3000+ kW
- Basınç aralığı: 3 - 10 bar (tipik endüstriyel), 40+ bar (proses gazı)
- Doğal olarak yağsız (Class 0)
- Yaygın markalar: Atlas Copco (ZH), Ingersoll Rand (MSG/C), MAN Energy Solutions, Siemens (STC), Hanwha (SM serisi), Elliott

## Çalışma Prensibi
Yüksek hızla dönen çark (impeller) havaya kinetik enerji kazandırır. Difüzörde bu kinetik enerji basınç enerjisine dönüştürülür. Genellikle 2-3 kademeli tasarım kullanılır.

### Temel Bileşenler
- **Impeller (Çark):** 15,000-60,000+ RPM (boyuta bağlı), titanyum veya alüminyum alaşım
- **Difüzör:** Kinetik enerjiyi basınca dönüştürür
- **Volüt (Spiral kasa):** Havanın toplanması
- **Intercooler:** Kademeler arası soğutma
- **IGV (Inlet Guide Vanes):** Kapasite kontrolü için giriş yönlendirme kanatçıkları
- **Yataklar:** Konvansiyonel (yağlı) veya manyetik yatak

### Manyetik Yataklı Tip
- Temassız süspansiyon — mekanik sürtünme yok
- Yağlama sistemi gereksiz (tamamen yağsız)
- Daha yüksek verim (%2-4 yağlı yataklara kıyasla)
- Kompakt tasarım
- Daha düşük bakım maliyeti
- Örnek: Atlas Copco ZH, Danfoss Turbocor, Ingersoll Rand MSG/C (mag-lev)

## Enerji Dağılımı (Tipik — 3 Kademeli)
- Basınçlı hava (faydalı iş): ~10-15%
- Intercooler ve aftercooler ısı kaybı: ~70%
- Aerodinamik kayıplar: ~10%
- Mekanik kayıplar (yatak, conta): ~5%

## Spesifik Güç Tüketimi (SPC)

| Alt Tip | Kapasite | SPC @ 7 bar |
|---------|---------|-------------|
| Konvansiyonel (yağ yataklı) | 150-300 kW | 5.0-5.8 kW/m³/min |
| Konvansiyonel | 300-500 kW | 4.8-5.5 kW/m³/min |
| Konvansiyonel | 500-1000 kW | 4.5-5.2 kW/m³/min |
| Konvansiyonel | >1000 kW | 4.3-5.0 kW/m³/min |
| Manyetik yataklı (mag-lev) | 150-500 kW | 4.3-5.0 kW/m³/min |
| Manyetik yataklı (best-in-class) | >500 kW | ~4.3 kW/m³/min |

Santrifüj kompresörler büyük kapasitelerde en düşük spesifik güce sahip tiptir.

## Kapasite Kontrol Yöntemleri

### 1. IGV (Inlet Guide Vanes) — En Yaygın
- Giriş kanatçıklarının açısı değiştirilerek debi ayarlanır
- %60-100 debi aralığında verimli çalışma
- %60'ın altında surge riski

### 2. VSD (Variable Speed Drive)
- Motor hızı değiştirilerek debi ayarlanır
- IGV ile kombineli kullanılabilir (VSD + IGV)
- Turndown %40-50'ye kadar genişletilebilir

### 3. Blow-off (Basınç Tahliye)
- Surge sınırının altında çalışmayı önlemek için fazla hava atmosfere bırakılır
- Enerji israfı — kaçınılmalı
- Son çare olarak otomatik surge koruma mekanizması

## Surge, Choke ve Turndown Kavramları

### Surge (Pompaj)
- Debi, minimum kararlı çalışma noktasının altına düştüğünde oluşur
- Hava akışı tersine döner — şiddetli titreşim ve mekanik hasar riski
- Tipik surge sınırı: Tam yükün %60-70'i
- **Anti-surge kontrolü zorunlu:** Blow-off valve veya recycle valve

### Choke (Tıkanıklık)
- Debi, maksimum kapasiteyi aştığında oluşur
- Difüzörde sonik hız aşılır
- Basınç düşer, verim çöker
- Pratik üst sınır: Tasarım debisinin %110-115'i

### Turndown Aralığı
| Kontrol Tipi | Minimum Kararlı Debi | Turndown |
|-------------|---------------------|----------|
| Sadece IGV | %60-70 | %30-40 |
| VSD + IGV | %40-50 | %50-60 |
| Manyetik yataklı + VSD | %25-40 | %60-75 |

## Kısmi Yük Davranışı

### Sadece IGV Kontrolü
| Yük % | Güç % | Not |
|--------|-------|-----|
| 100% | 100% | IGV tam açık |
| 90% | 92% | |
| 80% | 85% | |
| 70% | 78% | Surge sınırına yaklaşılıyor |
| 60% | 72% | Surge yakınında, blow-off başlayabilir |
| <60% | 65-80%* | *Blow-off ile: israf, blow-off olmadan: kararsız |

### VSD + IGV (Modern Manyetik Yataklı)
| Yük % | Güç % | Not |
|--------|-------|-----|
| 100% | 100% | |
| 80% | 78% | |
| 60% | 58% | |
| 50% | 50% | Genişletilmiş turndown |
| 40% | 42% | Minimuma yakın |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 150-3000+ | Güç analizörü |
| Çıkış basıncı | bar | 3-10 | Basınç sensörü |
| Hava debisi | m³/min | 25-500+ | Flowmeter |
| Ortam sıcaklığı | °C | 15-40 | Termometre |
| Giriş sıcaklığı | °C | 15-40 | Termometre |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| IGV pozisyonu | % | 0-100 | Kontrol paneli |
| Her kademe çıkış sıcaklığı | °C | 100-200 | Termometre |
| Titreşim | mm/s | <4.5 (ISO 10816) | Titreşim sensörü |
| Yatak sıcaklığı | °C | 50-90 | Sıcaklık sensörü |
| Surge marjini | % | >10% | Kontrol sistemi |
| Yük oranı | % | 0-100 | Kontrol paneli |
| Çalışma saati | saat/yıl | 4000-8760 | Sayaç |

### Nameplate Bilgileri
- Marka ve model (örn. Atlas Copco ZH 630)
- Nominal güç (kW)
- Nominal debi (m³/min veya m³/s)
- Nominal basınç (bar)
- Kademe sayısı
- Yatak tipi (konvansiyonel / manyetik)
- Motor tipi ve devir
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Çıkış sıcaklığı | Ortam + 10°C | Aftercooler sonrası |
| Yük oranı | 80% | Santrifüjler genelde yüksek yükte çalışır |
| Çalışma saati | 7000 saat/yıl | Çok vardiyalı, büyük tesisler |
| Spesifik güç | 5.5 kW/(m³/min) | Orta kapasite ortalama |
| cosφ (güç faktörü) | 0.90 | Büyük motorlarda daha iyi |
| Surge marjini | %15 | Tipik kontrol ayarı |

## Uygulama Alanları
- **Büyük endüstriyel tesisler:** Otomotiv, petrokimya, çelik
- **Enerji santralleri:** Proses havası
- **Çimento fabrikaları:** Taşıma havası
- **Tekstil:** Büyük ölçekli dokuma tesisleri
- **Gıda ve içecek:** Büyük kapasiteli yağsız hava ihtiyacı
- **Atıksu arıtma:** Büyük ölçekli havalandırma (düşük basınçlı santrifüj blower)
- **Gaz işleme:** Doğalgaz sıkıştırma, rafineri gazları

## Vidalı vs Santrifüj Karşılaştırma

| Özellik | Vidalı (Yağsız) | Santrifüj |
|---------|-----------------|-----------|
| Kapasite aralığı | 15-500 kW | 150-3000+ kW |
| SPC @ 7 bar | 6.5-8.5 | 4.3-5.8 |
| Kısmi yük | VSD ile iyi | IGV+VSD ile orta |
| Surge riski | Yok | Var — kritik |
| Bakım maliyeti | Orta | Düşük (mag-lev) |
| Güvenilirlik | Yüksek | Çok yüksek |
| Ömür | 15-20 yıl | 25-30+ yıl |
| Yatırım maliyeti | Orta | Yüksek |

## Dikkat Edilecekler

1. **Surge koruması:** Anti-surge kontrol sistemi zorunlu — surge mekanik hasar verebilir
2. **Sabit yük avantajı:** Tam yükte en verimli kompresör tipi; değişken yükte dikkatli değerlendirilmeli
3. **Minimum kapasite:** Turndown altında blow-off kaçınılmaz — enerji israfı
4. **Manyetik yatak:** Yeni yatırımlarda kesinlikle değerlendirilmeli — verim ve bakım avantajı
5. **Ortam sıcaklığı:** Performans hava yoğunluğuna hassas — sıcak iklimlerde derecelendirme düşer
6. **Yüksek kapasite:** >150 kW uygulamalarda vidalıya göre SPC avantajı belirgindir

## Referanslar
- Atlas Copco Compressed Air Manual, 9th Edition — Centrifugal Compressor Chapter
- ASME PTC-10 — Performance Test Code on Compressors and Exhausters
- CAGI Compressed Air & Gas Handbook, 7th Edition
- MAN Energy Solutions — Centrifugal Compressor Technology
- Schultz (1962), "The Polytropic Analysis of Centrifugal Compressors," ASME J. Eng. Power
