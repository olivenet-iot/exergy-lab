# Scroll Kompresör (Scroll Compressor)

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Pozitif deplasmanlı, orbital hareket
- Kapasite aralığı: 2 - 33 kW
- Basınç aralığı: 7 - 10 bar
- Gürültü seviyesi: <65 dB(A) (en sessiz kompresör tipi)
- ISO 8573-1 Class 0 (doğal olarak yağsız)
- Yaygın markalar: Atlas Copco (SF serisi), Ingersoll Rand (WS), ANEST IWATA, Hitachi

## Çalışma Prensibi
İki sarmal (scroll) şekilli eleman — biri sabit (fixed scroll), diğeri orbital hareket eden (orbiting scroll) — arasında hava sıkıştırılır. Orbital scroll, sabit scroll etrafında eksantrik hareketle döner ve hava giriş çevresinden merkeze doğru sıkıştırılır.

### Temel Özellikler
- **Yağsız sıkıştırma:** Scrolllar arasında yağ yoktur — doğal olarak Class 0
- **Sürekli sıkıştırma:** Vidalı kompresöre benzer şekilde neredeyse pulsasyonsuz çıkış
- **Az sayıda hareketli parça:** Valf yok, piston yok — minimal aşınma
- **Modüler yapı:** Birden fazla scroll modülü paralel bağlanarak kapasite artırılabilir (tandem, 4'lü, 6'lı konfigürasyonlar)

## Enerji Dağılımı (Tipik)
- Basınçlı hava (faydalı iş): ~8-10%
- Aftercooler'a atılan ısı: ~60%
- Motor ve mekanik kayıplar: ~15%
- Radyasyon ve diğer kayıplar: ~15%

## Spesifik Güç Tüketimi (SPC)

| Parametre | Değer |
|-----------|-------|
| SPC @ 7 bar (tipik) | 6.5-8.0 kW/m³/min |
| SPC @ 7 bar (best-in-class) | ~6.0 kW/m³/min |
| Karşılaştırma | Vidalı kompresörle yakın, küçük kapasitelerde biraz daha iyi |

## Modüler Konfigürasyon

| Konfigürasyon | Toplam Güç | Toplam Debi (tipik) | Avantaj |
|---------------|-----------|---------------------|---------|
| Tek modül | 2-5.5 kW | 0.2-0.7 m³/min | En küçük boyut |
| Tandem (2 modül) | 4-11 kW | 0.4-1.5 m³/min | Yedeklilik |
| 4 modül | 8-22 kW | 1.0-3.0 m³/min | Kademeli kapasite kontrolü |
| 6 modül | 12-33 kW | 1.5-4.5 m³/min | Maksimum esneklik |

Modüler yapının avantajları:
- Her modül bağımsız olarak açılıp kapatılabilir → mükemmel kısmi yük verimi
- Bir modül arızalansa diğerleri çalışmaya devam eder → yüksek güvenilirlik
- Bakım sırasında kapasite tamamen kaybedilmez

## Kısmi Yük Davranışı

Modüler scroll kompresörlerde kademe kontrolü:

| Yük % | Aktif Modüller (4 modüllü) | Güç % |
|--------|---------------------------|-------|
| 100% | 4/4 | 100% |
| 75% | 3/4 | ~75% |
| 50% | 2/4 | ~50% |
| 25% | 1/4 | ~25% |
| 0% | 0/4 | ~0% (tamamen kapalı) |

Bu kademe kontrolü pistonlu kompresörlere benzer şekilde lineer güç-yük ilişkisi sağlar.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 2-33 | Güç analizörü |
| Çıkış basıncı | bar | 7-10 | Basınç sensörü |
| Hava debisi | m³/min | 0.2-4.5 | Flowmeter veya nameplate |
| Ortam sıcaklığı | °C | 15-35 | Termometre |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Çıkış sıcaklığı | °C | 60-90 | Termometre |
| Aktif modül sayısı | adet | 1-6 | Kontrol paneli |
| Yük oranı | % | 0-100 | Kontrol paneli |
| Çalışma saati | saat/yıl | 2000-8760 | Sayaç |

### Nameplate Bilgileri
- Marka ve model (örn. Atlas Copco SF 22)
- Toplam nominal güç (kW)
- Modül sayısı ve modül başına güç
- Nominal debi (m³/min veya l/s)
- Nominal basınç (bar)
- ISO 8573-1 sınıfı
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Çıkış sıcaklığı | 80°C | Aftercooler öncesi tipik |
| Yük oranı | 70% | Scroll genelde değişken yüklü uygulamalarda |
| Çalışma saati | 4000 saat/yıl | Tek vardiya |
| Spesifik güç | 7.0 kW/(m³/min) | Ortalama |
| cosφ (güç faktörü) | 0.85 | Tipik motor değeri |

## Uygulama Alanları

- **Medikal/Hastane:** Cerrahi hava, dental hava, ventilatör besleme
- **Laboratuvar:** Analitik cihazlar, temiz oda besleme
- **Gıda:** Küçük ölçekli paketleme, POU (point-of-use) uygulamalar
- **Elektronik:** Baskılı devre kartı üretimi, yarı iletken
- **Ofis/bina:** Düşük gürültü gereksinimleri olan ortamlar
- **İlaç:** Küçük-orta ölçekli üretim tesisleri

## Scroll vs Diğer Tipler Karşılaştırma

| Özellik | Scroll | Vidalı (Yağsız) | Pistonlu (Yağsız) |
|---------|--------|-----------------|-------------------|
| Güç aralığı | 2-33 kW | 15-500+ kW | 0.5-500+ kW |
| Gürültü | <65 dB(A) | 70-80 dB(A) | 75-95 dB(A) |
| Titreşim | Çok düşük | Düşük | Yüksek |
| Bakım | Minimal | Orta-Yüksek | Yüksek (valfler) |
| Kısmi yük | Mükemmel (modüler) | Orta | İyi (kademe boşaltma) |
| İlk maliyet | Yüksek (kW başına) | Yüksek | Orta |
| Ömür | 20,000+ saat | 40,000+ saat | 20,000+ saat (valfler arası) |

## Dikkat Edilecekler

1. **Kapasite sınırı:** Maksimum ~33 kW — büyük uygulamalar için uygun değil
2. **Birim maliyet:** kW başına diğer tiplere göre daha pahalı olabilir
3. **Sıcaklık hassasiyeti:** Yüksek ortam sıcaklıklarında (>35°C) verim düşer
4. **Modüler avantaj:** Birden fazla modül = yedeklilik + verimli kısmi yük
5. **Düşük gürültü:** Üretim alanına veya ofis yakınına yerleştirilebilir
6. **Class 0:** Filtrasyon olmadan doğal olarak yağsız hava — medikal ve gıda için ideal

## Referanslar
- Atlas Copco SF Serisi Teknik Dokümantasyonu
- Ingersoll Rand WS Serisi Ürün Kataloğu
- CAGI Compressed Air & Gas Handbook, 7th Edition
- ISO 8573-1:2010 — Compressed Air Quality Classes
