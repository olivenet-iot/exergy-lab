---
title: "Çözüm: Motor Yükseltme — Motor Upgrade (IE2 → IE3/IE4)"
category: solutions
equipment_type: pump
keywords: [motor, IE3, IE4, verimlilik]
related_files: [pump/equipment/motors_drives.md, pump/benchmarks.md, pump/solutions/vsd.md]
use_when: ["Motor yükseltme önerilirken", "IE3/IE4 motor değişimi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Motor Yükseltme — Motor Upgrade (IE2 → IE3/IE4)

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Eski, düşük verimli motorlar (IE1/IE2) gereksiz enerji tüketiyor. Pompa sistemlerinde motorlar toplam enerji tüketiminin büyük bölümünü oluşturur ve motor verimliliği doğrudan işletme maliyetini etkiler. IE1 sınıfı bir motor, IE4 sınıfına göre %3-8 daha fazla kayıp üretir; bu kayıp büyük motorlarda ve uzun çalışma sürelerinde ciddi mali yük oluşturur.

**Çözüm:** Mevcut IE1 veya IE2 sınıfı motorun IE3 (Premium Efficiency) veya IE4 (Super Premium Efficiency) sınıfı motor ile değiştirilmesi.

**Tipik Tasarruf:** %2-8
**Tipik ROI:** 2-5 yıl (büyük motorlarda ve sürekli çalışmada daha kısa)

## Çalışma Prensibi

Motor verimlilik sınıfları IEC 60034-30-1 standardı ile tanımlanır. Verim farkı şu kayıp mekanizmalarındaki iyileştirmelerden gelir:

- **Bakır kayıpları (I²R):** Daha kalın iletken, daha düşük direnç → azaltılmış stator ve rotor kayıpları
- **Demir kayıpları:** Daha ince ve kaliteli elektrik çelik sacları → histerezis ve eddy akımı kayıplarında azalma
- **Mekanik kayıplar:** Daha iyi rulmanlar, optimize fan tasarımı → sürtünme kayıplarında azalma
- **Kaçak kayıplar:** Optimize manyetik devre tasarımı → sapan akı kayıplarında azalma

Yüksek verimli motorlar aynı mekanik gücü daha az elektrik girdisi ile üretir:

```
P_elektrik = P_mekanik / η_motor
Tasarruf = P_mekanik × (1/η_eski - 1/η_yeni)
```

## Motor Verimlilik Sınıfları (IEC 60034-30-1)

4 kutuplu (1500 rpm @ 50 Hz) motorlar için nominal verim değerleri:

| Motor Gücü | IE1 (Standard) | IE2 (High) | IE3 (Premium) | IE4 (Super Premium) | IE5 (Ultra Premium) |
|------------|----------------|------------|---------------|---------------------|---------------------|
| 0.75 kW | 72.1% | 77.4% | 80.7% | 83.5% | 86.0% |
| 1.1 kW | 75.0% | 79.6% | 82.7% | 85.2% | 87.5% |
| 2.2 kW | 79.7% | 83.2% | 86.0% | 88.0% | 90.0% |
| 4 kW | 82.6% | 85.8% | 88.6% | 90.2% | 91.8% |
| 7.5 kW | 85.7% | 88.7% | 90.4% | 92.1% | 93.5% |
| 11 kW | 87.6% | 89.8% | 91.4% | 93.0% | 94.0% |
| 22 kW | 90.0% | 91.6% | 93.0% | 94.5% | 95.4% |
| 37 kW | 91.2% | 92.7% | 93.7% | 95.0% | 95.8% |
| 55 kW | 92.0% | 93.2% | 94.3% | 95.5% | 96.2% |
| 75 kW | 92.5% | 93.6% | 94.7% | 95.8% | 96.5% |
| 110 kW | 93.0% | 94.0% | 95.0% | 96.0% | 96.8% |
| 160 kW | 93.5% | 94.5% | 95.4% | 96.3% | 97.0% |
| 250 kW | 94.0% | 95.0% | 95.8% | 96.6% | 97.1% |

## Yeni Motor vs Rewinding (Sarım Yenileme) Karşılaştırması

| Faktör | Yeni IE3/IE4 Motor | Rewinding (Sarım Yenileme) |
|--------|-------------------|---------------------------|
| Verim etkisi | Orijinal veya daha yüksek | Genelde -%1-2 kayıp (kötü rewinding ile -%5'e kadar) |
| Maliyet | Tam motor fiyatı | Motor fiyatının %40-60'ı |
| Ömür | 15-20+ yıl | 5-10 yıl (kaliteye bağlı) |
| Güvenilirlik | Fabrika garantili | Sarım kalitesine bağlı |
| Zaman | Stok varsa 1-2 hafta | 3-7 gün |
| Tavsiye | Motor >10 yaş veya <15 kW ise | Çok büyük motor veya acil durum |

**Genel kural:** 15 kW'ın altındaki motorları sarım yenilemek yerine yeni IE3/IE4 motor ile değiştirmek ekonomik olarak daha avantajlıdır. Büyük motorlarda (>75 kW) rewinding hala ekonomik olabilir ancak kaliteli bir atölyede yapılmalıdır.

## EU MEPS (Minimum Energy Performance Standards) Zorunlulukları

| Tarih | Kapsam | Minimum Verimlilik Sınıfı |
|-------|--------|--------------------------|
| 2011 | 0.75-375 kW (EU) | IE2 |
| 2015 | 7.5-375 kW (EU) | IE3 (veya IE2 + VSD) |
| 2021 (EU 2019/1781) | 0.75-1000 kW, 2-6 kutuplu | IE3 |
| 2023 (EU 2019/1781) | 75-200 kW, 2-6 kutuplu | IE4 |
| Gelecek | >0.12 kW genişleme beklentisi | IE4 yaygınlaşması |

**Not:** Ex-proof (patlama korumalı) motorlar için farklı geçiş tarihleri geçerlidir.

## Uygulanabilirlik Kriterleri

### Motor Yükseltme Ne Zaman Uygulanmalı
- Motor IE1 veya IE2 sınıfında ve >5,000 saat/yıl çalışıyorsa
- Motor gücü >7.5 kW ise (daha büyük motorlarda fayda/maliyet oranı artar)
- Elektrik fiyatı yüksekse (>€0.10/kWh)
- Motor arızalanmış ve rewinding kararı verilecekse (rewinding yerine yükseltme)
- Motor >15 yaşında ise (verim bozulması + eski teknoloji)

### Motor Yükseltme Ne Zaman Uygulanmamalı
- Motor zaten IE3+ sınıfında ve sağlıklı ise
- Motor çalışma saati düşükse (<2,000 saat/yıl)
- Motor gücü çok küçükse (<1 kW): ROI çok uzun
- Sistemde daha büyük tasarruf fırsatları varsa (önce VSD, throttle eliminasyonu vb.)

## Yatırım Maliyeti

| Motor Gücü | IE3 Motor Fiyatı | IE4 Motor Fiyatı | Fark (IE2 → IE3) | Fark (IE2 → IE4) |
|------------|-----------------|-----------------|-------------------|-------------------|
| 1.1 kW | €200-350 | €300-500 | €50-100 | €150-250 |
| 4 kW | €400-650 | €550-900 | €100-200 | €250-450 |
| 7.5 kW | €550-900 | €750-1,200 | €150-300 | €350-600 |
| 15 kW | €800-1,300 | €1,100-1,800 | €250-450 | €500-900 |
| 22 kW | €1,000-1,600 | €1,400-2,200 | €300-550 | €600-1,100 |
| 37 kW | €1,400-2,200 | €1,900-3,000 | €400-700 | €800-1,500 |
| 55 kW | €1,900-3,000 | €2,500-4,000 | €500-900 | €1,100-2,000 |
| 75 kW | €2,400-3,800 | €3,200-5,000 | €600-1,100 | €1,400-2,500 |
| 110 kW | €3,200-5,000 | €4,200-6,500 | €800-1,400 | €1,800-3,200 |

**Not:** Fiyatlar montaj ve devreye alma dahil değildir. Montaj maliyeti genellikle €500-2,000 ekler.

## ROI Hesabı

### Formül
```
Tasarruf_kWh = P_mil × t × (1/η_eski - 1/η_yeni)
Tasarruf_EUR = Tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = (Motor_fiyatı + Montaj_maliyeti) / Tasarruf_EUR
```

### Örnek Hesap
- 22 kW pompa motoru, IE2 (η = 91.6%) → IE4 (η = 94.5%)
- Çalışma: 6,000 saat/yıl, sürekli %85 yük
- Elektrik fiyatı: €0.15/kWh
- Mil gücü: 22 × 0.85 = 18.7 kW

```
Tasarruf_kWh = 18.7 × 6,000 × (1/0.916 - 1/0.945)
             = 112,200 × (1.0917 - 1.0582)
             = 112,200 × 0.0335
             = 3,759 kWh/yıl

Tasarruf_EUR = 3,759 × 0.15 = €564/yıl

Yatırım = €1,800 (IE4 motor) + €800 (montaj) = €2,600
Geri_ödeme = 2,600 / 564 = 4.6 yıl
```

**Not:** 55 kW ve üzeri motorlarda geri ödeme genellikle 2-3 yıla düşer. VSD ile kombine edildiğinde toplam tasarruf çok daha yüksek olur.

## Uygulama Adımları

1. **Motor envanteri:** Tüm pompa motorlarının güç, yaş, verim sınıfı ve çalışma saatlerini listele
2. **Önceliklendirme:** En yüksek çalışma saati × güç çarpımına sahip motorları belirle
3. **ROI hesabı:** Her motor için tasarruf ve geri ödeme hesapla
4. **Motor seçimi:** Mekanik uyumluluk (montaj boyutu, mil çapı, devir) kontrol et
5. **Tedarik:** IE3/IE4 motor sipariş et (IEC frame boyutu uyumu doğrula)
6. **Montaj:** Eski motor sökümü, yeni motor montajı, kaplin hizalama
7. **Devreye alma:** Motor yönü, akım, titreşim kontrolü
8. **Doğrulama:** Kurulum öncesi/sonrası güç ölçümü ile tasarrufu doğrula

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Mekanik uyumsuzluk | Farklı frame boyutu veya mil çapı | IEC standart frame boyutlarını kontrol et |
| Kısa devre akımı | IE3/IE4 motorlar daha yüksek kısa devre akımı çekebilir | Koruma röle ayarlarını güncelle |
| Atalet momenti farkı | Farklı rotor ataleti kaplin ve şaft üzerinde stres | Başlangıç akımı ve atalet hesabı yap |
| VSD uyumu | IE4 motorlar genellikle inverter-duty değildir | Inverter-duty sertifikalı motor seç |
| Yetersiz tasarruf | Küçük motorlarda (%<4 kW) tasarruf çok düşük | Önce büyük motorları hedefle |

## İlgili Dosyalar
- Pompa VSD çözümü: `solutions/pump_vsd.md`
- Pompa bakım çözümü: `solutions/pump_maintenance.md`
- Pompa kontrol optimizasyonu: `solutions/pump_control_optimization.md`
- Pompa exergy formülleri: `formulas/pump_exergy.md`

## Referanslar
- IEC 60034-30-1:2014 — Rotating electrical machines — Efficiency classes of line operated AC motors
- EU Ecodesign Regulation 2019/1781 — Electric motors and variable speed drives
- DOE/AMO, "Improving Motor and Drive System Performance: A Sourcebook for Industry"
- DOE MotorMaster+ (motor efficiency database and analysis tool)
- Europump & Hydraulic Institute, "Pump Life Cycle Costs: LCC Analysis for Pumping Systems"
- MDPI Applied Sciences, "Comparative Study of Induction Motors of IE2, IE3 and IE4 Efficiency Classes in Pump Applications" (2020)
