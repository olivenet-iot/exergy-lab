# Yağsız Vidalı Kompresör (Oil-Free Screw Compressor)

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Pozitif deplasmanlı, döner, yağsız
- Kapasite aralığı: 15 - 500+ kW
- Basınç aralığı: 7 - 10 bar (tipik), 13 bar'a kadar
- ISO 8573-1 Class 0 sertifikalı (yağsız hava garantisi)
- Yaygın markalar: Atlas Copco (ZR/ZT serisi), Ingersoll Rand (Sierra), Kaeser (CSG/DSG), Boge (SO/SLF)

## Çalışma Prensibi
Yağlı vidalı kompresörlerden farklı olarak sıkıştırma odasına yağ enjekte edilmez. Rotorlar birbirine temas etmeden, hassas toleranslarla döner. İki ana alt tip vardır:

### Kuru Tip (Dry Screw)
- Rotor yüzeyleri PTFE veya özel kaplama ile kaplanır
- Yağ yerine zamanlama dişlileri (timing gears) ile rotor senkronizasyonu sağlanır
- Genellikle 2 kademeli sıkıştırma kullanılır (her kademe ~3 bar)
- Çıkış sıcaklığı: 150-250°C (yağlı tipe göre çok daha yüksek)
- Ara soğutucu (intercooler) ile kademeler arası soğutma yapılır

### Su Enjeksiyonlu Tip (Water-Injected)
- Sıkıştırma odasına su enjekte edilir (sızdırmazlık + soğutma)
- Tek kademede 7-10 bar basınç üretilebilir
- Çıkış sıcaklığı: 50-60°C (kuru tipe göre çok daha düşük)
- Daha yüksek verim (izotermale daha yakın sıkıştırma)
- Örnek: Atlas Copco AQ serisi

## Enerji Dağılımı (Tipik — Kuru Tip, 2 Kademeli)
- Basınçlı hava (faydalı iş): ~6-8%
- Aftercooler'a atılan ısı: ~50%
- Intercooler'a atılan ısı: ~30%
- Radyasyon ve diğer kayıplar: ~10-12%

## Spesifik Güç Tüketimi (SPC)

| Parametre | Kuru Tip | Su Enjeksiyonlu |
|-----------|----------|-----------------|
| SPC @ 7 bar (tipik) | 6.5-8.5 kW/m³/min | 6.0-7.5 kW/m³/min |
| SPC @ 7 bar (best-in-class) | ~6.0 kW/m³/min | ~5.5 kW/m³/min |
| Yağlı vidalıya kıyasla | %10-15 daha fazla enerji | %5-10 daha fazla enerji |

## Yağlı vs Yağsız Karşılaştırma

| Özellik | Yağlı Vidalı | Yağsız (Kuru) | Yağsız (Su Enjeksiyonlu) |
|---------|-------------|---------------|--------------------------|
| Hava kalitesi | Class 1-2 (filtre ile) | Class 0 | Class 0 |
| SPC @ 7 bar | 5.5-7.0 | 6.5-8.5 | 6.0-7.5 |
| Çıkış sıcaklığı | 70-100°C | 150-250°C | 50-60°C |
| Bakım maliyeti | Düşük-Orta | Yüksek | Orta |
| Yağ değişimi | Gerekli | Yok | Yok |
| İlk yatırım maliyeti | Baz | %30-50 daha pahalı | %20-40 daha pahalı |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 15-500+ | Güç analizörü |
| Çıkış basıncı | bar | 7-10 | Basınç sensörü |
| Hava debisi | m³/min | 2-80+ | Flowmeter veya nameplate |
| Ortam sıcaklığı | °C | 15-40 | Termometre |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| 1. kademe çıkış sıcaklığı | °C | 150-250 (kuru) | Termometre |
| 2. kademe çıkış sıcaklığı | °C | 150-250 (kuru) | Termometre |
| Intercooler çıkış sıcaklığı | °C | 25-40 | Termometre |
| Yük oranı | % | 0-100 | Kontrol paneli |
| Çalışma saati | saat/yıl | 2000-8760 | Sayaç |

### Nameplate Bilgileri
- Marka ve model (örn. Atlas Copco ZR 110)
- Nominal güç (kW)
- Nominal debi (m³/min veya l/s)
- Nominal basınç (bar)
- Kademe sayısı
- ISO 8573-1 sınıfı
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Çıkış sıcaklığı (aftercooler sonrası) | Ortam + 10°C | Aftercooler çıkışı |
| Yük oranı | 75% | Endüstriyel ortalama |
| Çalışma saati | 6000 saat/yıl | Yağsız genelde çok vardiyalı |
| Spesifik güç | 7.5 kW/(m³/min) | Kuru tip ortalama |
| cosφ (güç faktörü) | 0.85 | Tipik motor değeri |

## Uygulama Alanları
- **Gıda ve içecek:** Ürünle doğrudan temas eden hava (paketleme, taşıma)
- **İlaç:** GMP gereksinimleri, Class 0 zorunlu
- **Elektronik:** Yarı iletken üretimi, temiz oda
- **Tekstil:** Dokuma makineleri (yağ kontaminasyonu kabul edilemez)
- **Otomotiv boyama:** Boya kabini besleme havası
- **Medikal:** Nefes havası, cerrahi aletler

## Isı Geri Kazanım Potansiyeli
- Kuru tipte 2 kademeli yapı nedeniyle yüksek sıcaklıkta ısı mevcuttur
- Intercooler ve aftercooler'dan ısı geri kazanımı mümkün
- HOC (Heat of Compression) kurutucu entegrasyonu özellikle verimlidir
  - Yüksek çıkış sıcaklığı (~200°C) doğrudan desiccant rejenerasyonu için kullanılır
  - Ek enerji tüketimi: ~%0

## Dikkat Edilecekler

1. **Enerji maliyeti:** Yağlı tipe göre %10-15 daha fazla — TCO analizi yapılmalı
2. **Bakım kritikliği:** Rotor kaplaması ve timing gear bakımı ihmal edilmemeli
3. **Kademeler arası soğutma:** Intercooler performansı toplam verimi doğrudan etkiler
4. **Sıcaklık:** Yüksek çıkış sıcaklığı nedeniyle aftercooler boyutlandırması önemli
5. **Alternatif değerlendirmesi:** Class 0 gerekli değilse, yağlı + filtrasyon daha ekonomik olabilir
6. **Su enjeksiyonlu tip:** Kuru tipe göre daha verimli ancak su arıtma sistemi gerektirir

## Referanslar
- Atlas Copco Compressed Air Manual, 9th Edition
- ISO 8573-1:2010 — Compressed Air Quality Classes
- CAGI (Compressed Air & Gas Institute) Performance Verification Data Sheets
- Kaeser Technical Documentation — Oil-Free Compressor Series
