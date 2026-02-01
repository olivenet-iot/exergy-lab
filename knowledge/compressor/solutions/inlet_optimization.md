# Çözüm: Giriş Havası Optimizasyonu

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Kompresörler sıcak iç ortam havasını emerek verimsiz çalışır. Kompresör odası sıcaklığı 40-50°C'ye ulaşabilir.

**Çözüm:** Dış ortam havasının doğrudan kompresör girişine kanalize edilmesi, yeterli oda havalandırması ve filtre bakımı.

**Temel Kural:** Her 3°C giriş sıcaklığı düşüşü ≈ %1 verim artışı

**Tipik Tasarruf:** %1-7
**Tipik ROI:** 3-12 ay

## Sıcaklık Etkisi

### Neden Önemli?
Kompresörler sabit hacimde hava sıkıştırır. Soğuk hava daha yoğundur → aynı hacimde daha fazla kütle → birim kütle başına daha az enerji.

### Sıcaklık-Verim Tablosu

| Giriş Sıcaklığı | Bağıl Verim | Bağıl Güç Tüketimi |
|-----------------|------------|-------------------|
| 15°C (referans) | %100 | %100 |
| 20°C | %98.3 | %101.7 |
| 25°C | %96.6 | %103.5 |
| 30°C | %95.0 | %105.3 |
| 35°C | %93.3 | %107.2 |
| 40°C | %91.7 | %109.1 |
| 45°C | %90.0 | %111.1 |

**Örnek:** Kompresör odası 40°C, dış ortam 20°C → 20°C fark → **%6-7 enerji tasarrufu** dış hava kanalı ile.

## Çözüm 1: Doğrudan Dış Hava Kanalı (Tercih Edilen)

Dış ortamdan kompresör giriş filtresine izoleli kanal:

### Teknik Gereksinimler
- Kanal çapı: Kompresör giriş filtresine uygun, basınç düşüşü <50 Pa
- İzolasyon: Kompresör odası içindeki bölümde yoğuşmayı önlemek için
- Hava koruma: Yağmur siperi, böcek filtresi, kaba ön filtre
- Kanal uzunluğu: Kısa tutulmalı (<5 m ideal)

### Maliyet ve Tasarruf
- **Yatırım:** €500-3,000 (kanal, bağlantı parçaları, hava siperi)
- **Tasarruf:** Sıcaklık farkına bağlı olarak %1-7

### Dikkat
- Minimum giriş sıcaklığı: 5°C (altında donma riski — nem donabilir)
- Tozlu veya korozif dış ortamda ek filtrasyon gerekebilir
- Kompresörün izin verdiği giriş sıcaklığı aralığını kontrol et

## Çözüm 2: Kompresör Odası Havalandırma İyileştirme

Kompresör atık ısısını uzaklaştırmak için yeterli havalandırma:

### Havalandırma Hesabı
```
Havalandırma_debisi (m³/saat) = Q_atık (kW) × 3,600 / (ρ × Cp × ΔT)

Pratik kural:
~150 m³/saat havalandırma havası / kW kompresör gücü (ΔT = 10°C için)
```

**Örnek:** 100 kW kompresör → ~15,000 m³/saat havalandırma gerekli

### Uygulama
- Termostat kontrollü fanlar + büyük giriş panjurları
- Yazın otomatik açılma, kışta kontrollü çalışma
- Kışın kompresör odası sıcak havası bina ısıtmada kullanılabilir (en basit ısı geri kazanım)

### Maliyet
- €2,000-10,000 (oda boyutu ve konfigürasyona bağlı)

## Çözüm 3: Mevsimsel Hava Kaynağı Geçişi

- **Kış:** Dış ortam havası (soğuk = daha verimli)
- **Yaz:** Dış ortam sıcaklığı oda sıcaklığına yakınsa fayda azalır
- Otomatik damper + sıcaklık sensörü ile geçiş

## Filtre Bakımı

### Giriş (Inlet) Filtresi

| Parametre | Değer |
|-----------|-------|
| Temiz filtre basınç düşüşü | 10-30 mbar |
| Kirli filtre basınç düşüşü | 50-100+ mbar |
| Enerji etkisi | Her 10 mbar artış ≈ +%0.1 enerji |
| Ciddi tıkanma etkisi | +%0.5-1.0 enerji artışı |
| Değişim aralığı | 2,000-4,000 saat veya ΔP göstergesine göre |
| Filtre eleman maliyeti | €20-100 |

### Filtre İhmalinin Riskleri
- Enerji artışı (basınç düşüşü)
- **Filtre yırtılması:** Aşırı tıkanmada filtre yırtılabilir → kontaminantlar airend'e girer → katastrofik hasar
- Kompresör kapasitesinde düşüş

### En İyi Uygulamalar
- Filtre diferansiyel basınç göstergesini düzenli kontrol et
- Tozlu ortamlarda ön filtre (panel filtre veya siklon separatör) kullan
- Daha düşük dirençli, yüksek kaliteli filtre elemanları değerlendir
- Filtreleri önerilen aralıkta veya ΔP eşiğinde değiştir — asla "biraz daha" çalıştırma

## Nem Etkisi

- Nemli hava kuru havadan biraz daha az yoğundur (su buharı N₂/O₂'den hafiftir)
- Kompresör gücüne etkisi minimal (<%0.5)
- **Ana etki:** Daha fazla kondansat → kurutucu yükü artar, drenaj kaybı artar, korozyon riski artar
- Önlem: Dış hava girişinde nem kontrolü gerekmez, ancak kurutucu kapasitesi yeterli olmalı

## ROI Hesabı

### Örnek: Dış Hava Kanalı
- 75 kW kompresör, 6,000 saat/yıl, €0.12/kWh
- Kompresör odası: 38°C, Dış ortam (yıllık ortalama): 18°C
- Sıcaklık farkı: 20°C → Tasarruf: ~%6.7
- Yıllık enerji maliyeti: 75 × 6,000 × 0.12 = €54,000
- Yıllık tasarruf: €54,000 × 0.067 = **€3,618/yıl**
- Yatırım: €1,500 (kanal + kurulum)
- **Geri ödeme: 5 ay**

## İlgili Dosyalar
- Vidalı kompresör: `equipment/compressor_screw.md`
- Bakım çözümleri: `solutions/compressor_maintenance.md`
- Isı geri kazanımı: `solutions/compressor_heat_recovery.md`

## Referanslar
- DOE/AMO, "Improving Compressed Air System Performance," Section 8
- Atlas Copco, "Compressed Air Manual" — Installation Chapter
- Kaeser, "Compressed Air Engineering" — Compressor Room Design
- CAGI, "Compressed Air & Gas Handbook"
