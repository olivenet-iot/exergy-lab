# Pistonlu Kompresör (Reciprocating / Piston Compressor)

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Pozitif deplasmanlı, ileri-geri hareketli
- Kapasite aralığı: 0.5 - 500+ kW
- Basınç aralığı: 7 - 40+ bar (özel uygulamalarda 400+ bar)
- En eski ve en yaygın kompresör tipi
- Yaygın markalar: Atlas Copco (LE/LT/HX), Ingersoll Rand (T30, PET Star), Boge (SRHV), Sauer Compressors, Burckhardt

## Çalışma Prensibi
Piston, krank mili tarafından silindir içinde ileri-geri hareket ettirilerek hava sıkıştırılır. Emme ve basma valfleri (supaplar) hava akışını yönlendirir.

### Alt Tipler

#### Tek Etkili (Single Acting)
- Sıkıştırma sadece pistonun bir yüzünde gerçekleşir
- Genellikle küçük kapasiteler (<30 kW)
- Daha basit yapı, düşük maliyet
- Atölye ve küçük işletme uygulamaları

#### Çift Etkili (Double Acting)
- Pistonun her iki yüzünde sıkıştırma yapılır
- Daha yüksek kapasite ve verim
- Genellikle >30 kW endüstriyel uygulamalar
- Daha karmaşık yapı (piston kolu contası gerekli)

#### Tek Kademeli (Single Stage)
- Tek silindirde son basınca ulaşılır
- Genellikle 7-8 bar'a kadar
- Yüksek basınç oranı = düşük verim ve yüksek sıcaklık

#### Çok Kademeli (Multi-Stage)
- 2, 3 veya daha fazla kademe ile kademeli sıkıştırma
- Kademeler arası intercooler ile soğutma
- Her kademe tipik olarak 3-4:1 basınç oranında çalışır
- Yüksek basınçlar (40-400+ bar) için zorunlu
- Enerji tasarrufu: 2 kademe → %10-14, 3 kademe → %14-17 (7 bar'da)

## Enerji Dağılımı (Tipik — 2 Kademeli)
- Basınçlı hava (faydalı iş): ~8-12%
- Silindir soğutma (jacket cooling): ~30%
- Intercooler/aftercooler: ~45%
- Radyasyon ve mekanik kayıplar: ~13-17%

## Spesifik Güç Tüketimi (SPC)

| Alt Tip | SPC @ 7 bar | Not |
|---------|-------------|-----|
| Tek kademeli, küçük (<5 kW) | 7.5-10.0 kW/m³/min | Atölye sınıfı |
| Çift kademeli, orta (5-30 kW) | 6.0-7.5 kW/m³/min | Endüstriyel |
| Çift kademeli, büyük (30-200 kW) | 5.5-6.5 kW/m³/min | Ağır hizmet |
| Tipik (genel) | 7.0-9.0+ kW/m³/min | Ortalama piyasa |
| Best-in-class | ~6.5 kW/m³/min | Büyük, çift kademeli |

## Kısmi Yük Davranışı

Pistonlu kompresörlerin kısmi yükteki en önemli avantajı kademe boşaltma (step unloading) özelliğidir:

| Yük % | Güç % | Not |
|--------|-------|-----|
| 100% | 100% | Tüm silindirler yüklü |
| 75% | ~75% | Kademe boşaltma (3/4 silindir) |
| 50% | ~50% | Yarı kapasite |
| 25% | ~25% | Tek silindir yüklü |
| 0% | 10-15% | Boşta çalışma |

Bu neredeyse lineer güç-yük ilişkisi, pistonlu kompresörleri değişken talep uygulamalarında çok verimli kılar.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 0.5-500+ | Güç analizörü veya CT |
| Çıkış basıncı | bar | 7-40+ | Manometre / basınç sensörü |
| Hava debisi | m³/min | 0.1-50+ | Flowmeter veya nameplate |
| Ortam sıcaklığı | °C | 15-40 | Termometre |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Kademe sayısı ve basınçları | bar | Kademe başına 3-4:1 | Ara basınç sensörleri |
| Çıkış sıcaklığı (her kademe) | °C | 120-200 (hava soğutmalı) | Termometre |
| Valf durumu | - | - | Sıcaklık / titreşim analizi |
| Yük oranı | % | 0-100 | Kontrol paneli / akım |
| Çalışma saati | saat/yıl | 1000-8760 | Sayaç |

### Nameplate Bilgileri
- Marka ve model
- Nominal güç (kW veya HP)
- Nominal debi (m³/min, CFM veya l/s)
- Nominal basınç (bar veya PSI)
- Kademe sayısı
- Silindir konfigürasyonu (V, W, L, yatay-karşılıklı)
- Devir (RPM)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Çıkış sıcaklığı | 120°C | 2 kademeli, aftercooler öncesi |
| Yük oranı | 70% | Endüstriyel ortalama |
| Çalışma saati | 4000 saat/yıl | Tek vardiya |
| Spesifik güç | 7.5 kW/(m³/min) | Orta kapasiteli 2 kademeli |
| cosφ (güç faktörü) | 0.85 | Tipik motor değeri |

## Uygulama Alanları

### Standart Basınç (7-10 bar)
- Küçük atölyeler ve garajlar
- Dişçi ve medikal (yağsız pistonlu)
- Endüstriyel yedek kompresör

### Yüksek Basınç (>10 bar)
- **PET şişe şişirme:** 25-40 bar (en yaygın yüksek basınç uygulaması)
- Azot/oksijen üretimi (PSA sistemleri): 10-15 bar
- CNG (sıkıştırılmış doğalgaz): 200-250 bar
- Şişeleme/test: 200-400+ bar
- Endüstriyel gaz sıkıştırma

### PET Şişe Şişirme Detayı
- Tipik basınç: 25-40 bar
- Çok kademeli (3-4 kademe) pistonlu kompresörler kullanılır
- Kritik gereksinim: Yağsız hava (Class 0 veya yüksek kalite filtrasyon)
- Yaygın markalar: Atlas Copco HX/HN, Sauer WP, Ingersoll Rand PET Star

## Vidalı vs Pistonlu Karşılaştırma

| Özellik | Vidalı (Screw) | Pistonlu (Piston) |
|---------|---------------|-------------------|
| Debi kararlılığı | Sürekli, pulsasyonsuz | Pulsasyonlu (tank gerekli) |
| Basınç aralığı | 5-15 bar | 7-400+ bar |
| Kısmi yük verimi | Kötü (load/unload) | Çok iyi (step unload) |
| Bakım aralığı | 4000-8000 saat | 2000-4000 saat (valfler) |
| Gürültü | 65-80 dB(A) | 75-95+ dB(A) |
| Boyut/ağırlık | Kompakt | Daha büyük ve ağır |
| İlk yatırım | Orta | Düşük (küçük) / Yüksek (büyük) |
| Ömür | 15-20 yıl | 20-30+ yıl |

## Dikkat Edilecekler

1. **Valf bakımı:** Her 2000-4000 saatte valf kontrolü, aşınmış valfler %5-15 verim kaybına neden olur
2. **Titreşim:** Pistonlu kompresörler yüksek titreşim üretir — uygun temel ve izolasyon gerekli
3. **Pulsasyon:** Çıkışta basınç dalgalanması olur — yeterli tank hacmi zorunlu
4. **Soğutma:** Hava soğutmalı tiplerde kompresör odası havalandırması kritik
5. **Yağ tüketimi:** Tek etkili tiplerde piston contası yağ geçirebilir — hava kalitesini etkiler
6. **Kademe optimizasyonu:** Yüksek basınçlarda çok kademeli sıkıştırma enerji verimliliği için zorunlu

## Referanslar
- Atlas Copco Compressed Air Manual, 9th Edition
- CAGI Compressed Air & Gas Handbook, 7th Edition
- Cengel & Boles, Thermodynamics: An Engineering Approach, Chapter 7
- DOE/AMO Compressed Air Sourcebook
