---
title: "Kompresör Benchmark Verileri"
category: reference
equipment_type: compressor
keywords: [benchmark, kompresör, özgül enerji, SEC]
related_files: [compressor/formulas.md, compressor/audit.md, compressor/solutions/vsd.md]
use_when: ["Kompresör performansı değerlendirilirken", "SEC karşılaştırması yapılırken"]
priority: high
last_updated: 2026-01-31
---
# Kompresör Benchmark Verileri

> Son güncelleme: 2026-01-31

## 1. Exergy Verimi Aralıkları

| Kompresör Tipi | Düşük | Ortalama | İyi | Best-in-class |
|----------------|-------|----------|-----|---------------|
| Vidalı (yağlı) | <30% | 35-45% | 45-55% | >60% |
| Vidalı (yağsız) | <25% | 30-40% | 40-50% | >55% |
| Pistonlu | <25% | 30-40% | 40-50% | >55% |
| Scroll | <30% | 35-45% | 45-55% | >60% |
| Santrifüj | <35% | 40-50% | 50-60% | >65% |

## 2. Spesifik Güç Tüketimi (SPC) — Tip ve Kapasiteye Göre

### 2.1 Vidalı Yağlı Kompresörler (7 bar)

| Nominal Güç (kW) | Debi (m³/min) | SPC [kW/(m³/min)] | Not |
|-------------------|--------------|-------------------|-----|
| 4-7 | 0.5-1.0 | 7.0-8.5 | Küçük, sabit hız |
| 7-15 | 1.0-2.5 | 6.5-7.5 | Küçük-orta |
| 15-30 | 2.5-5.0 | 6.0-7.0 | Orta |
| 30-55 | 5.0-9.5 | 5.5-6.5 | Orta-büyük |
| 55-90 | 9.5-16 | 5.2-6.2 | Büyük |
| 90-160 | 16-28 | 5.0-6.0 | Çok büyük |
| 160-250 | 28-43 | 4.8-5.8 | Endüstriyel |
| 250-355 | 43-62 | 4.7-5.7 | Ağır endüstriyel |

### 2.2 Vidalı Yağsız Kompresörler (7 bar)

Yağlı vidalı değerlere %10-15 eklenmelidir.
- Tipik aralık: 5.5-8.0 kW/(m³/min) (kapasiteye bağlı)
- Kuru tip: 6.5-8.5 kW/(m³/min)
- Su enjeksiyonlu: 6.0-7.5 kW/(m³/min)

### 2.3 Pistonlu Kompresörler (7 bar)

| Alt Tip | SPC Aralığı | Not |
|---------|-------------|-----|
| Tek kademeli, küçük (<5 kW) | 7.5-10.0 | Atölye sınıfı |
| Çift kademeli, orta (5-30 kW) | 6.0-7.5 | Endüstriyel |
| Çift kademeli, büyük (30-200 kW) | 5.5-6.5 | Ağır hizmet |
| Çok kademeli, yüksek basınç | Değişken | Son basınca bağlı |

### 2.4 Santrifüj Kompresörler (7 bar)

| Kapasite | SPC Aralığı | Not |
|----------|-------------|-----|
| 150-300 kW | 5.0-5.8 | Tek kademe, IGV |
| 300-500 kW | 4.8-5.5 | Çok kademe |
| 500-1000 kW | 4.5-5.2 | Büyük endüstriyel |
| >1000 kW | 4.3-5.0 | Tesis ölçeği |
| Manyetik yataklı (best) | ~4.3 | En düşük SPC |

### 2.5 Genel SPC Sınıflandırması (7 bar, tüm tipler)

| Sınıf | Spesifik Güç | Açıklama |
|-------|--------------|----------|
| En iyi uygulama | < 5.0 | Modern santrifüj/büyük vidalı, VSD, optimize |
| Çok iyi | 5.0-5.5 | İyi bakımlı modern sistem |
| İyi | 5.5-6.5 | Standart verimli |
| Ortalama | 6.5-7.5 | Eski veya bakımsız |
| Ortalamanın altı | 7.5-8.5 | Önemli tasarruf potansiyeli |
| Kötü | > 8.5 | Acil müdahale gerekli |

### 2.6 Motor Verimlilik Sınıfı Etkisi

| Motor Sınıfı | Tipik Verim (30-75 kW) | SPC Etkisi (IE3 bazlı) |
|-------------|----------------------|----------------------|
| IE1 (Standart) | %90.0-91.5 | %3-4 daha yüksek SPC |
| IE2 (Yüksek) | %91.5-93.0 | %1.5-2 daha yüksek SPC |
| IE3 (Premium) | %93.0-94.5 | Baz değer |
| IE4 (Süper Premium) | %94.5-95.5 | %1-1.5 daha düşük SPC |
| IE5 (Ultra Premium) | %95.5-96.5 | %2-2.5 daha düşük SPC |

Not: AB'de 2021'den itibaren 0.75-1000 kW motorlarda IE3 minimum zorunlu.

## 3. Kısmi Yük Verimliliği

### 3.1 Vidalı Kompresör — Load/Unload Kontrol

| Yük % | Güç % | Efektif SPC % | Not |
|--------|-------|--------------|-----|
| 100% | 100% | 100% | Tam yük |
| 90% | 93% | 103% | |
| 80% | 87% | 109% | |
| 75% | 83% | 111% | |
| 70% | 80% | 114% | |
| 60% | 73% | 122% | |
| 50% | 67% | 134% | Belirgin israf |
| 40% | 60% | 150% | |
| 30% | 53% | 177% | Çok verimsiz |
| 25% | 50% | 200% | |
| 0% | 25-30% | ∞ | Boşta çalışma |

### 3.2 Vidalı Kompresör — VSD Kontrol

| Yük % | Güç % | Efektif SPC % | Not |
|--------|-------|--------------|-----|
| 100% | 100% | 100% | Tam hız |
| 90% | 90% | 100% | Lineer ilişki |
| 80% | 80% | 100% | |
| 75% | 75% | 100% | |
| 70% | 70% | 100% | |
| 60% | 61% | 102% | |
| 50% | 52% | 104% | |
| 40% | 44% | 110% | Hafif artış |
| 30% | 37% | 123% | Optimal aralık altı |
| 25% | 34% | 136% | Minimum hıza yakın |

### 3.3 VSD vs Load/Unload Tasarruf Karşılaştırması

| Yük % | Load/Unload Güç % | VSD Güç % | VSD Tasarrufu |
|--------|-------------------|-----------|--------------|
| 100% | 100% | 100% | %0 (VSD biraz dezavantajlı) |
| 75% | ~83% | ~75% | ~%10 |
| 50% | ~67% | ~52% | ~%22 |
| 25% | ~50% | ~34% | ~%32 |

### 3.4 Pistonlu Kompresör — Kademe Boşaltma

| Yük % | Güç % | Not |
|--------|-------|-----|
| 100% | 100% | Tüm silindirler yüklü |
| 75% | ~75% | 3/4 silindir |
| 50% | ~50% | 2/4 silindir |
| 25% | ~25% | 1/4 silindir |
| 0% | 10-15% | Boşta |

Pistonlu kompresörler, kademe kontrolü sayesinde en iyi kısmi yük verimine sahiptir.

### 3.5 Santrifüj Kompresör — IGV Kontrol

| Yük % | Güç % (sadece IGV) | Güç % (VSD+IGV) |
|--------|-------------------|-----------------|
| 100% | 100% | 100% |
| 90% | 92% | 90% |
| 80% | 85% | 78% |
| 70% | 78% | 68% |
| 60% | 72% | 58% |
| 50% | 65-80%* | 50% |
| 40% | N/A (surge) | 42% |

*Blow-off ile %80, blow-off olmadan kararsız. Surge sınırı tipik %60-70.

## 4. Kaçak Oranları Benchmark

### 4.1 Sistem Kaçak Durumu

| Durum | Kaçak Oranı | Aksiyon |
|-------|-------------|---------|
| Çok iyi (en iyi uygulama) | < 5% | Koruyucu bakım devam |
| İyi | 5-10% | Yıllık kaçak tespiti yeterli |
| Kabul edilebilir | 10-20% | 6 ayda bir kaçak tespiti |
| Kötü | 20-30% | Acil kaçak onarımı |
| Kritik | > 30% | Kapsamlı sistem revizyonu |

### 4.2 Kaçak Maliyeti Benchmark (7 bar, 8000 saat, €0.10/kWh)

| Delik Çapı | Kaçak Debisi (l/s) | Yıllık Maliyet |
|------------|-------------------|----------------|
| 1 mm | ~0.8 | ~€400 |
| 3 mm | ~7.0 | ~€3,400 |
| 5 mm | ~19.5 | ~€9,500 |
| 10 mm | ~78.0 | ~€38,000 |

### 4.3 Kaçağın Zaman İçindeki Artışı

| Sistem Yaşı | Beklenen Kaçak Oranı (bakımsız) |
|-------------|-------------------------------|
| Yeni (0-2 yıl) | %5 |
| 2-5 yıl | %10-15 |
| 5-10 yıl | %20-25 |
| >10 yıl | %25-40 |

## 5. Yaşa Göre Verim Düşüşü

### 5.1 Bakım Kalitesine Göre Detaylı Model

| Yaş | İyi Bakım | Ortalama Bakım | Kötü Bakım |
|-----|-----------|----------------|------------|
| 0-3 yıl | %0-2 | %0-2 | %0-3 |
| 3-5 yıl | %1-3 | %2-5 | %3-8 |
| 5-8 yıl | %2-5 | %5-10 | %8-15 |
| 8-10 yıl | %3-7 | %8-15 | %15-25 |
| 10-15 yıl | %5-10 | %12-20 | %20-35 |
| 15-20 yıl | %8-15 | %18-30 | %30-50 |
| >20 yıl | %12-20 | %25-40 | %40-60+ |

### 5.2 Bozulma Mekanizmaları (Kompresör Tipine Göre)

**Vidalı kompresör:**
- Rotor aşınması (iç kaçak artışı): ~%1-2 / 10,000 saat
- Yatak aşınması (titreşim, hizalama): Kademeli
- Valf aşınması (emme, minimum basınç): Periyodik değişim
- Yağ bozulması: Rotor aşınmasını hızlandırır
- Soğutucu kirlenmesi: Çıkış sıcaklığı artışı

**Pistonlu kompresör:**
- Piston segman aşınması: En önemli faktör
- Valf aşınması/kırılması: 2000-4000 saat aralıkla değişim
- Silindir boşluk aşınması: Uzun vadeli
- Paking aşınması (çift etkili): Kaçak artışı

**Santrifüj kompresör:**
- Impeller erozyonu/kirlenmesi: Verim düşüşü
- Conta aşınması: İç resirkülasyon artışı
- Yatak bozulması: Yağ yataklarda; manyetik yatakta aşınma yok
- IGV mekanizma aşınması: Modülasyon hassasiyeti düşer

### 5.3 Bakım Etkisi Tablosu

| Bakım Kalemi | İhmal Cezası | Önerilen Aralık |
|-------------|-------------|----------------|
| Hava giriş filtresi | +%0.5-1.0 enerji / 25 mbar ΔP artışı | Her 2000-4000 saat |
| Yağ filtresi | Aşırı ısınma, hızlanan aşınma | Her 2000-4000 saat |
| Yağ separatörü | +%1-5 enerji, yağ taşınması | Her 4000-8000 saat |
| Yağ değişimi | Hızlanan aşınma, verim düşüşü | Her 4000-8000 saat |
| Soğutucu temizliği | +2-5°C çıkış sıcaklığı artışı | Yılda bir veya sıcaklığa göre |
| Kayış gerginliği | -%2-5 kapasite (kayma) | Her 1000-2000 saat |
| Valf kontrolü (pistonlu) | -%5-15 kapasite | Her 2000-4000 saat |
| Kondansat drenaj | Hava kaybı veya su hasarı | Haftalık kontrol |

### 5.4 Yenileme Kararı — Pratik Kurallar

- Yıllık verimsizlik enerji maliyeti > yeni kompresör maliyetinin %15'i → değiştirmeyi değerlendir
- Bakım maliyeti > yenileme maliyetinin %40'ı → değiştirmeyi değerlendir
- Yaş >15 yıl VE verim düşüşü >%15 → yenileme değerlendirmesi yap

## 6. Sektörel Karşılaştırma

### 6.1 Sektöre Göre Tipik Exergy Verimi

| Sektör | Tipik Exergy Verimi | Not |
|--------|---------------------|-----|
| Otomotiv | %40-50 | Yüksek kalite gereksinimleri, iyi bakım |
| Gıda | %35-45 | Hijyen öncelikli, yağsız sistemler |
| Tekstil | %30-40 | Genelde eski sistemler |
| Metal işleme | %35-45 | Ağır kullanım |
| İlaç | %35-45 | Class 0 gereksinimi, yağsız |
| Genel üretim | %35-45 | Karma |
| Atölye / KOBİ | %25-35 | Genelde küçük, eski, bakımsız |

### 6.2 Sektöre Göre Tipik SPC

| Sektör | Tipik SPC [kW/(m³/min)] | Açıklama |
|--------|------------------------|----------|
| Büyük endüstri (>500 kW) | 5.0-6.0 | Santrifüj veya büyük vidalı |
| Orta endüstri (100-500 kW) | 5.5-7.0 | Vidalı, genelde iyi bakımlı |
| Küçük endüstri (<100 kW) | 6.5-8.5 | Vidalı/pistonlu, değişken bakım |
| Atölye (<30 kW) | 7.5-10.0 | Pistonlu veya küçük vidalı |

## 7. Isı Geri Kazanım Potansiyeli

| Kompresör Gücü | Geri Kazanılabilir Isı | Tipik Kullanım |
|----------------|------------------------|----------------|
| 15-30 kW | 10-20 kW | Küçük ölçekli ısıtma |
| 30-75 kW | 20-50 kW | Proses suyu, bina ısıtma |
| 75-150 kW | 50-100 kW | Merkezi ısıtma sistemi |
| >150 kW | >100 kW | Endüstriyel proses |

Geri kazanılabilir ısı ≈ Kompresör gücü × %70 × HRU verimi (%80-90)

## 8. Kurutucu Enerji Tüketimi Benchmark

| Kurutucu Tipi | Enerji Tüketimi | PDP | Tipik Uygulama |
|--------------|-----------------|-----|---------------|
| Soğutmalı (cycling) | %0.5-1.0 | +3°C | Genel endüstri |
| Soğutmalı (non-cycling) | %1.0-2.0 | +3°C | Genel endüstri |
| Adsorpsiyon (ısıtmasız) | %15-20 purge | -40°C | Gıda, ilaç |
| Adsorpsiyon (ısıtmalı) | %5-10 purge + ısıtıcı | -40°C | Büyük tesisler |
| Adsorpsiyon (blower purge) | %0 CA + 2-4 kW | -40°C | Enerji bilincli tesisler |
| HOC (Heat of Compression) | ~%0 ek enerji | -20 ile -40°C | Yağsız, büyük sistemler |
| Membran | %15-20 purge | -20 ile -40°C | POU, küçük debiler |

## Referanslar
- DOE/AMO, "Improving Compressed Air System Performance: A Sourcebook for Industry"
- Compressed Air Challenge, "Best Practices for Compressed Air Systems"
- Atlas Copco, "Compressed Air Manual," 9th Edition
- Carbon Trust, "Compressed Air — Opportunities for Businesses" (CTG027)
- CAGI, "Compressed Air & Gas Handbook," 7th Edition
- Kaeser Compressors Technical Documentation
- CAGI Performance Verification Data Sheets
