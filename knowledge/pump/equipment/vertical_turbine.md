---
title: "Dikey Türbin Pompa — Vertical Turbine Pump"
category: equipment
equipment_type: pump
subtype: "Düşey Türbin"
keywords: [düşey türbin, kuyu pompası, derin kuyu]
related_files: [pump/benchmarks.md, pump/formulas.md, pump/equipment/submersible.md]
use_when: ["Düşey türbin pompa analizi yapılırken", "Derin kuyu pompası değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Dikey Türbin Pompa — Vertical Turbine Pump

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Kinetik (santrifüj), çok kademeli dikey tasarım
- Alt tipler: Lineshaft (uzun şaftlı, motor üstte), submersible motor (motor altta)
- Kapasite aralığı: 10 - 5,000+ m³/h
- Head aralığı: 20 - 300+ m
- Kuyu, sump ve intake uygulamaları için tasarlanmış
- Yaygın markalar: Flowserve (Peerless, Byron Jackson), Sulzer (VMPX, VPC), KSB (UGT), Grundfos (VT), Xylem/Goulds (VIT, VIC), National Pump Company

## Çalışma Prensibi
Dikey türbin pompa, birden fazla kademenin (bowl assembly) dikey olarak sıralı şekilde monte edildiği santrifüj pompa tipidir. Sıvı alttaki emme ağzından girer, her kademede impeller-difüzör çifti tarafından basınç kazanır ve kolon borusu (column pipe) içinden yüzeye iletilir.

### Temel Bileşenler
- **Bowl Assembly (Kademe Grubu):** İmpeller + difüzör (bowl) çiftlerinden oluşan pompa kalbi — basınç burada üretilir
- **Kolon Borusu (Column Pipe):** Bowl assembly'den yüzeye sıvı taşıyan boru; 3-6 m'lik seksiyonlar halinde
- **Lineshaft (Uzun Şaft):** Yüzeydeki motordan bowl assembly'deki impellerlere torku ileten şaft; 3-6 m'lik bağlantılı parçalar
- **Shaft Bearings (Ara Yataklar):** Lineshaft boyunca belirli aralıklarla (tipik her 1.5-3 m) yerleştirilen yataklar
- **Discharge Head (Çıkış Kafası):** Kolon borusunun yüzeydeki bağlantı noktası; motor ile birleşme yeri
- **Motor:** Dikey montajlı, genellikle yüzeyde (lineshaft tip) veya altta (submersible motor tip)
- **Eksenel Yatak (Thrust Bearing):** Motor veya discharge head içinde; impellerlerin eksenel kuvvetini karşılar

### Lineshaft vs Submersible Motor Tipi

| Özellik | Lineshaft (Motor Üstte) | Submersible Motor (Motor Altta) |
|---------|------------------------|-------------------------------|
| Motor konumu | Yüzeyde, discharge head üstünde | Suyun altında, bowl assembly altında |
| Motor verimi | Yüksek (%93-97) — standart motor | Düşük (%85-92) — dalgıç motor |
| Şaft kaybı | Var — uzunluğa bağlı %2-5 | Yok — doğrudan bağlantı |
| Yatak yağlama | Pompalanan su ile veya yağ borusu ile | Pompalanan su ile |
| Bakım | Şaft hizalama ve yatak bakımı gerekli | Motor erişimi zor — çıkarma gerekli |
| Derinlik sınırı | 100-150 m (pratik şaft uzunluğu) | 300+ m (kablo ile sınırlı) |
| İlk yatırım | Düşük-orta | Orta-yüksek |
| Enerji verimi | Sığ kuyu: lineshaft avantajlı | Derin kuyu: submersible avantajlı |

## Bowl Assembly Tasarımı
- Bowl: Döküm demir (ASTM A48 Class 30), vitreous enamel kaplama ile sürtünme azaltma
- İmpeller: Bronz veya paslanmaz çelik, polisajlı yüzey
- Her kademe tipik olarak 5-20 m head üretir
- Kademe sayısı toplam head gereksinimini karşılayacak şekilde seçilir
- Standart bowl çapları: 6", 8", 10", 12", 14", 16", 20", 24", 30"

### İki Farklı Verim Tanımı
- **Bowl Efficiency (Kademe Verimi):** Sadece bowl assembly'deki hidrolik performans
- **Pump Efficiency (Pompa Verimi):** Bowl verimi + şaft sürtünme kaybı + thrust bearing kaybı dahil

```
Total BHP = Bowl BHP + Shaft Friction Loss + Thrust Bearing Loss
Bowl BHP = (ρ × g × H_bowl × Q) / (η_bowl × 3600)
Pump Input = Bowl Input + Lineshaft Loss + Thrust Bearing Loss
η_pump = (ρ × g × H_total × Q) / (Pump Input × 3600)
```

Dikkat: Üreticiler bazen bowl input ve pump input değerlerini karıştırabilir — değerlendirme sırasında hangisinin verildiği doğrulanmalıdır.

## Lineshaft Kayıpları

Lineshaft sürtünme kaybı şaft uzunluğu, yatak sayısı ve devir hızına bağlıdır:

| Şaft Uzunluğu (m) | Yatak Sayısı | Tipik Şaft Kaybı (kW/100 kW) | Not |
|-------------------|-------------|------------------------------|-----|
| 5-15 | 3-8 | 1-2 kW | İhmal edilebilir |
| 15-50 | 8-25 | 2-5 kW | Dikkate alınmalı |
| 50-100 | 25-50 | 5-10 kW | Önemli kayıp |
| >100 | >50 | >10 kW | Submersible motor değerlendirilmeli |

- Şaft malzemesi: Tipik C-1045 karbon çelik, tornalı ve polisajlı
- Şaft doğruluğu: 0.12 mm TIR (3 m'lik seksiyonda), 0.25 mm TIR (6 m'lik seksiyonda)
- Kolon borusu sürtünme kaybı: Max 5 ft/100 ft (nominal debi kapasitesinde)

## Enerji Dağılımı (Tipik — Lineshaft, 50 m Derinlik)
- Faydalı hidrolik iş: ~65-80%
- Hidrolik kayıplar (bowl assembly): ~8-15%
- Lineshaft sürtünme kaybı: ~2-5%
- Thrust bearing kaybı: ~1-2%
- Motor kayıpları: ~5-10%
- Kolon borusu sürtünme: ~1-3%

## Verimlilik Benchmarkları

| Pompa Boyutu | Düşük | Ortalama | İyi | Best-in-class |
|-------------|-------|----------|-----|---------------|
| Küçük (6-8", <30 kW) | <%65 | %65-73 | %73-80 | >%80 |
| Orta (10-14", 30-150 kW) | <%72 | %72-80 | %80-86 | >%86 |
| Büyük (16-24", 150-500 kW) | <%78 | %78-84 | %84-89 | >%89 |
| Çok büyük (>24", >500 kW) | <%80 | %80-86 | %86-90 | >%90 |

Not: Değerler overall pump efficiency (şaft ve yatak kayıpları dahil) olarak verilmiştir.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 5-2000+ | Güç analizörü |
| Basma basıncı (yüzeyde) | bar | 1-30 | Basınç sensörü |
| Debi | m³/h | 10-5000+ | Flowmeter |
| Su seviyesi (statik) | m | 2-150 | Seviye ölçer |
| Su seviyesi (dinamik / pompaj sırasında) | m | 5-200+ | Seviye ölçer |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Motor devri | RPM | 1450-1800 | Takometre |
| Motor akımı | A | Etiket değeri | Pens ampermetre |
| Titreşim (discharge head) | mm/s | <4.5 | Titreşim sensörü |
| Yatak sıcaklığı (thrust) | °C | 40-80 | Sıcaklık sensörü |
| Çalışma saati | saat/yıl | 2000-8760 | Sayaç |
| Bowl set derinliği | m | 5-150 | Montaj kaydı |

### Nameplate Bilgileri
- Marka ve model (örn. Flowserve Peerless 12LCV)
- Nominal güç (kW veya HP)
- Nominal debi (m³/h veya GPM)
- Nominal head (m veya ft)
- Kademe (bowl) sayısı
- Bowl çapı (inç)
- Nominal devir (RPM)
- Motor tipi: Lineshaft veya submersible
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Sıvı yoğunluğu | 1000 kg/m³ | Su varsayımı |
| Bowl verimi | %82 | Orta boy pompa ortalaması |
| Şaft sürtünme kaybı | %3 | 30-50 m derinlik varsayımı |
| Thrust bearing kaybı | %1.5 | Standart yatak |
| Motor verimi | %94 | Lineshaft tip, IE3 motor |
| Overall pump verimi | %77 | Bowl - şaft - yatak kayıpları sonrası |
| Yük oranı | %80 | Sabit debi uygulaması |
| Çalışma saati | 5000 saat/yıl | Su temini uygulaması |
| cosφ (güç faktörü) | 0.87 | Büyük motorlarda daha iyi |

## Exergy Verimi Hesabı

```
η_exergy = P_hydraulic / P_electric
P_hydraulic = ρ × g × H_total × Q / 3600
H_total = Statik seviye + Drawdown + Boru sürtünme kaybı + Çıkış basıncı yüksekliği
P_electric = Ölçülen elektrik gücü (motor girişi)
```

Lineshaft tipte exergy yıkım kaynakları:
1. Motor kayıpları (bakır, demir, mekanik)
2. Thrust bearing sürtünme → ısı
3. Lineshaft yatak sürtünme → ısı
4. Bowl assembly hidrolik kayıpları (impeller, difüzör)
5. Kolon borusu sürtünme → basınç kaybı

## Uygulama Alanları
- **İçme suyu temini:** Kuyu ve göl suyu pompalama, su arıtma tesisi besleme
- **Sulama:** Tarımsal sulama pompa istasyonları
- **Endüstriyel soğutma:** Soğutma kulesi sirkülatör, kondenser suyu
- **Enerji santralleri:** Soğutma suyu, çevrim suyu pompalama
- **Belediye su temini:** Ana su dağıtım pompa istasyonları
- **Yangın suyu:** Yangın pompa sistemleri (NFPA 20 uyumlu)
- **Drenaj ve taşkın kontrolü:** Büyük hacimli su tahliyesi

## Dikey Türbin vs Dalgıç Pompa Karşılaştırma

| Özellik | Dikey Türbin (Lineshaft) | Dalgıç Pompa |
|---------|-------------------------|-------------|
| Motor erişimi | Yüzeyde — kolay bakım | Suyun altında — çıkarma gerekli |
| Motor verimi | Yüksek (%93-97) | Düşük (%85-92) |
| Şaft kaybı | Var (%2-5) | Yok |
| Derinlik sınırı | ~100-150 m (şaft pratik sınır) | 300+ m |
| İlk yatırım | Büyük pompada avantajlı | Küçük pompada avantajlı |
| Güvenilirlik | Şaft/yatak sorunları olası | Motor izolasyon riski |
| Gürültü | Motor yüzeyde — gürültü var | Motor suyun altında — sessiz |
| Kapasite aralığı | Daha yüksek debiler mümkün | Kuyu çapı ile sınırlı |

## Dikkat Edilecekler

1. **Şaft hizalama (Alignment):** Lineshaft tipin en kritik konusu — şaft eğikliği titreşim, yatak aşınması ve erken arızaya neden olur; montajda ve periyodik bakımda hizalama kontrolü zorunlu
2. **Yatak yağlama:** Pompalanan su ile yağlanan yataklar (water lubricated) kumlu suda hızla aşınır; yağ borulu (oil lubricated) alternatif temiz olmayan sularda tercih edilir
3. **Minimum su seviyesi:** Bowl assembly her zaman su altında kalmalı — hava emmesi kavitasyon ve hasara neden olur; seviye koruması gerekli
4. **Eksenel yük (Thrust):** Yüksek head uygulamalarında eksenel yük çok büyük olabilir — thrust bearing boyutlandırma kritik
5. **Başlangıç torku:** Uzun lineshaft ile başlangıçta yüksek tork gerekir — yumuşak kalkış (soft starter) veya VSD önerilir
6. **Bowl verimi vs pompa verimi:** Üreticiden alınan verimlerin bowl mu pump mu olduğu doğrulanmalı — fark %5-10 olabilir
7. **Titreşim:** Uzun şaft ve çoklu yatak yapısı titreşime hassas — ISO 10816'ya göre izleme önerilir

## İlgili Dosyalar
- Dalgıç pompa: `equipment/pump_submersible.md`
- Santrifüj pompa genel: `equipment/pump_centrifugal.md`
- VSD uygulaması: `solutions/pump_vsd.md`
- Benchmark verileri: `benchmarks/pump_benchmarks.md`
- Exergy hesaplamaları: `formulas/pump_exergy.md`

## Referanslar
- Grundfos Deep Well Vertical Turbine Pump Introduction
- Flowserve / Peerless Vertical Turbine Pump Engineering Data
- National Pump Company — Vertical Turbine Deep Well Pump Technical Catalog
- Hydraulic Institute Standards (ANSI/HI 2.1-2.2 — Vertical Turbine Pumps)
- Xylem/Goulds — Turbine Terminology Engineering Data (D200E01)
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- WaterWorld, "Submersible vs. Lineshaft Vertical Turbine Pumps: Advantages and Limitations"
