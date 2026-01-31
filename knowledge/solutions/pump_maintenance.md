# Çözüm: Bakım ve Performans İzleme — Maintenance and Performance Monitoring

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Zamanla pompa verimi düşer; wear ring aşınması, impeller erozyonu, conta bozulması ve rulman arızaları nedeniyle yıllık %1-2 verim kaybı oluşur. Bakımsız bir pompa, 5-10 yıl içinde orijinal veriminin %10-25 altında çalışabilir. Bu durum hem enerji israfına hem de beklenmedik arızalara yol açar.

**Çözüm:** Düzenli bakım programı ve performans izleme sistemi ile pompa verimliliğini koruyan, degradasyonu erken tespit eden sistematik yaklaşım.

**Tipik Tasarruf:** %5-15 (degradasyon önleme ve geri kazanım)
**Tipik ROI:** <1 yıl

## Aşınma Mekanizmaları ve Enerji Etkisi

### 1. Wear Ring Aşınması (Internal Recirculation)

Wear ring (aşınma halkası) impeller ile gövde arasındaki boşluğu minimize eder. Aşınma ile boşluk arttığında yüksek basınçlı sıvı emme tarafına geri sızar:

| Wear Ring Durumu | Tipik Boşluk | Verim Etkisi | Aksiyon |
|-----------------|-------------|-------------|---------|
| Yeni | 0.15-0.25 mm | Referans (%0) | - |
| Hafif aşınmış | 0.30-0.50 mm | -%2-4 | İzle |
| Orta aşınmış | 0.50-0.75 mm | -%4-8 | Planlı değişim |
| Ciddi aşınmış | 0.75-1.05 mm | -%8-15 | Acil değişim |
| Aşırı aşınmış | >1.05 mm | -%15-25 | Acil müdahale + impeller kontrolü |

**Araştırma notu:** Bilimsel çalışmalar, wear ring boşluğunun 0.15 mm'den 0.45 mm'ye artmasıyla verimin %8.2 düştüğünü göstermiştir. Boşluğun 0.75 mm'den 1.05 mm'ye artmasında ise %2.3 ek kayıp oluşur (doğrusal olmayan bozulma).

### 2. İmpeller Aşınması ve Erozyonu

| Aşınma Tipi | Neden | Verim Etkisi | Belirti |
|-------------|-------|-------------|---------|
| Kavitasyon erozyonu | Düşük NPSH, BEP dışı çalışma | -%3-10 | Pitting hasarı, gürültü |
| Abrazif aşınma | Katı partikül içeren sıvı | -%2-8 | Kanat incelmesi, profil bozulması |
| Korozyon | Kimyasal saldırı | -%1-5 | Yüzey pürüzlülüğü artışı |
| Erozyon-korozyon | Kombine etki | -%5-15 | Hızlı malzeme kaybı |

### 3. Conta Aşınması

- Mekanik salmastra veya keçe aşınması → dış sızıntı artışı
- Her sızıntı, pompanın kapasitesinin boşa harcanması demektir
- Ciddi sızıntılarda %1-3 verim kaybı
- Çevresel ve güvenlik riskleri (tehlikeli sıvılarda)

### 4. Rulman Bozulması

- Sürtünme artışı → mekanik kayıplar artışı (%0.5-2)
- Titreşim artışı → tüm bileşenlerde hızlanmış aşınma
- Sıcaklık artışı → yağ bozulması → kötüleşen zincir etki

## Yaşa Göre Verim Düşüşü

| Pompa Yaşı | İyi Bakımlı Pompa | Kötü Bakımlı Pompa | Fark |
|------------|-------------------|---------------------|------|
| 0-1 yıl | %80 (referans) | %80 (referans) | %0 |
| 2-3 yıl | %79.5 | %77 | %2.5 |
| 4-5 yıl | %79 | %74 | %5 |
| 6-8 yıl | %78 | %70 | %8 |
| 9-12 yıl | %77 | %65 | %12 |
| 13-15 yıl | %76 | %60 | %16 |

**Not:** Değerler tipik endüstriyel santrifüj pompa için gösterilmiştir. Başlangıç verimi %80 varsayılmıştır.

## Wear Ring Değişimi Etkisi

Wear ring değişimi en yüksek getirili bakım işlemlerinden biridir:

```
Verim_geri_kazanım = η_yeni_ring - η_aşınmış_ring
Tasarruf_kWh = (P_pompa / η_aşınmış) × t × (1 - η_aşınmış / η_yeni_ring)
```

**Tipik geri kazanım:** %2-8 verim artışı
**Parça maliyeti:** €50-500 (pompa boyutuna bağlı)
**İşçilik:** 4-16 saat (pompanın sökülmesi gerekir)

## Performans İzleme KPI'ları (Key Performance Indicators)

| KPI | Formül | İdeal Değer | Alarm Eşiği |
|-----|--------|-------------|-------------|
| Wire-to-water verimi | η_wtw = (Q × H × ρ × g) / P_elektrik | >%60 (tipik) | <%50 |
| Spesifik enerji tüketimi | SEC = P_elektrik / Q [kWh/m³] | Sistem bazlı | >%15 artış |
| Head vs debi noktası | H-Q eğrisi üzerinde konum | BEP ±%10 | BEP dışı >%20 |
| Motor akım çekişi | I_çalışma / I_nominal | %70-95 | >%100 veya trendi artan |
| Pompa titreşimi | mm/s (rms) | <2.8 mm/s | >4.5 mm/s |
| Rulman sıcaklığı | °C | <70°C | >85°C |

## Titreşim Analizi (ISO 10816 / ISO 20816)

### Titreşim Şiddeti Limitleri (ISO 10816-7: Pompalarda)

| Bölge | Titreşim Hızı (mm/s rms) | Durum | Aksiyon |
|-------|--------------------------|-------|---------|
| Zone A | <2.3 | İyi (yeni pompa) | Normal izleme |
| Zone B | 2.3-4.5 | Kabul edilebilir | İzleme sıklığını artır |
| Zone C | 4.5-7.1 | Yetersiz | Bakım planla |
| Zone D | >7.1 | Tehlikeli | Derhal müdahale |

**Not:** Değerler >15 kW pompalar için geçerlidir. Küçük pompalarda daha düşük limitler uygulanabilir.

### Titreşim Arıza Teşhisi

| Frekans Bileşeni | Olası Arıza | Açıklama |
|-------------------|-------------|----------|
| 1× devir (1×RPM) | Dengesizlik (unbalance) | İmpeller kir birikimi, aşınma |
| 2× devir (2×RPM) | Hizalama hatası (misalignment) | Kaplin hizası bozuk |
| Kanat geçiş frekansı (BPF) | Hidrolik rezonans | Kanat sayısı × RPM |
| Yüksek frekans (>1 kHz) | Rulman hasarı | Zarf analizi ile doğrula |
| Rastgele geniş bant | Kavitasyon | NPSH kontrol et |

## Prediktif Bakım Yöntemleri

| Yöntem | İzlenen Parametre | Tespit Edilen Arıza | Maliyet |
|--------|-------------------|---------------------|---------|
| Titreşim analizi | Titreşim hızı, spektrum | Rulman, hizalama, dengesizlik | €500-2,000/ölçüm noktası |
| Termografi | Yüzey sıcaklığı | Rulman ısınması, elektrik bağlantı | €2,000-8,000 (kamera) |
| Ultrasonik | Yüksek frekans sesi | Kavitasyon, sızıntı, rulman | €1,000-5,000 (cihaz) |
| Motor akım analizi (MCSA) | Stator akımı spektrumu | Motor bar kırığı, eksantriklik | €3,000-10,000 (cihaz) |
| Performans izleme | Q, H, P | Wear ring, impeller aşınma | €1,000-5,000 (sensör seti) |
| Yağ analizi | Viskozite, partikül, su | Yatak aşınma, kontaminasyon | €50-150/numune |

## Yatırım Maliyeti

| Bakım/İzleme Kalemi | Maliyet | Tipik Getiri |
|---------------------|---------|-------------|
| Wear ring değişimi | €200-2,000 | %2-8 verim geri kazanımı |
| Mekanik conta değişimi | €300-3,000 | Sızıntı eliminasyonu |
| Rulman değişimi | €100-1,000 | Mekanik kayıp azalma |
| Portatif titreşim cihazı | €5,000-20,000 | Çoklu pompa izleme |
| Online titreşim sistemi | €500-2,000/nokta | Sürekli izleme |
| Performans izleme sistemi | €2,000-10,000/pompa | Verim trend takibi |

## ROI Hesabı

### Formül
```
Tasarruf_yıllık = P_pompa × t × (1/η_düşük - 1/η_restore) × Elektrik_fiyatı
Yatırım = Parça_maliyeti + İşçilik_maliyeti + Duruş_maliyeti
Geri_ödeme_ay = (Yatırım / Tasarruf_yıllık) × 12
```

### Örnek Hesap — Wear Ring Değişimi
- 30 kW pompa, 7,000 saat/yıl
- Mevcut verim: %68 (aşınmış) → Restorasyon sonrası: %75 (yeni ring)
- Elektrik: €0.15/kWh

```
Tasarruf = 30 × 7,000 × (1/0.68 - 1/0.75) × 0.15
         = 210,000 × (1.4706 - 1.3333) × 0.15
         = 210,000 × 0.1373 × 0.15
         = €4,325/yıl

Yatırım = €300 (ring) + €800 (işçilik) + €500 (duruş) = €1,600
Geri_ödeme = (1,600 / 4,325) × 12 = 4.4 ay
```

## Bakım Programı Takvimi

### Günlük Kontroller
- [ ] Sızıntı kontrolü (görsel)
- [ ] Anormal ses ve titreşim kontrolü (duyusal)
- [ ] Çalışma basıncı ve debisi normal aralıkta
- [ ] Motor sıcaklığı ve akım çekişi normal

### Haftalık Kontroller
- [ ] Rulman sıcaklığı ölçümü
- [ ] Salmastra/conta sızıntı miktarı kontrolü
- [ ] Emme basıncı ve filtre durumu kontrolü
- [ ] Titreşim toplam değer kontrolü (varsa online)

### Aylık Kontroller
- [ ] Detaylı titreşim ölçümü (portatif cihaz ile)
- [ ] Motor akım ve güç ölçümü
- [ ] Kaplin durumu görsel kontrol
- [ ] Temel hizalama kontrolü

### 3 Aylık Kontroller
- [ ] Performans testi (Q, H, P ölçümü)
- [ ] Wire-to-water verimlilik hesabı
- [ ] Yağ numunesi analizi (yağ yağlamalı rulmanlar)
- [ ] Termografik tarama

### Yıllık Kontroller
- [ ] Kapsamlı titreşim analizi (spektrum)
- [ ] Wear ring boşluğu ölçümü
- [ ] Kaplin hizalama kontrolü ve düzeltme
- [ ] Temel/ankraj kontrolü
- [ ] Motor izolasyon direnci testi (megger)
- [ ] Emniyet valfi ve enstrümantasyon kalibrasyonu

## Uygulama Adımları

1. **Mevcut durum tespiti:** Tüm pompaların performans bazlini oluştur (Q, H, P, η)
2. **Kritik pompa belirleme:** Risk matrisine göre kritik pompaları sınıfla
3. **İzleme sistemi kurulumu:** Online veya periyodik ölçüm programı tasarla
4. **Bakım takvimi oluştur:** Yukarıdaki şablonu tesis koşullarına adapte et
5. **Eşik değerleri belirle:** Her pompa için alarm ve aksiyon eşiklerini tanımla
6. **Eğitim:** Operatörlere temel pompa izleme eğitimi ver
7. **Trend takibi:** Aylık performans raporları ile bozulma trendlerini izle
8. **Proaktif müdahale:** Eşik aşımında planlı bakım programla (reaktif değil)

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Aşırı bakım | Gereksiz sık bakım maliyet artırır | Durum bazlı bakım uygula (CBM) |
| Yanlış teşhis | Titreşim kaynağını yanlış belirleme | Eğitimli personel, çoklu yöntem |
| Bakım sırasında hasar | Montaj/demontaj sırasında hasar | Prosedürlere uygun çalışma |
| Yedek parça stoku | Kritik parça yoksa uzun duruş | Min-max stok yönetimi |
| Sensör arızası | Online sistemde yanlış veri | Periyodik kalibrasyon |

## İlgili Dosyalar
- Pompa VSD çözümü: `solutions/pump_vsd.md`
- Pompa kavitasyon önleme: `solutions/pump_cavitation_prevention.md`
- Pompa motor yükseltme: `solutions/pump_motor_upgrade.md`
- Pompa exergy formülleri: `formulas/pump_exergy.md`

## Referanslar
- Hydraulic Institute, "Pump Life Cycle Costs: A Guide to LCC Analysis for Pumping Systems"
- ISO 10816-7 — Mechanical vibration: Evaluation of machine vibration by measurements on non-rotating parts (Rotary pumps)
- ISO 20816-1 — Mechanical vibration: Measurement and evaluation of machine vibration
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- Pumps & Systems, "What Happens to Power & Efficiency When a Pump Wears Out?"
- Pumps & Systems, "The Power of Wear Rings Part Two: Efficiency"
- SKF, "Condition Monitoring for Rotating Equipment" Handbook
