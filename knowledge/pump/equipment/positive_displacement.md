# Pozitif Deplasmanlı Pompalar — Positive Displacement Pumps

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Pozitif deplasmanlı (sabit hacim ilkesi)
- Alt tipler: Pistonlu (piston), diyafram (diaphragm), vida (screw), dişli (gear), lob (lobe), peristaltik (peristaltic), progresif kavite (progressive cavity)
- Kapasite aralığı: 0.1 - 500 m³/h (tipe bağlı)
- Basınç aralığı: 1 - 1000 bar (tipe bağlı)
- Karakteristik: Sabit debi, değişken basınç üretimi (kompresöre benzer davranış)
- Yaygın markalar: Netzsch (progresif kavite), Grundfos (dozaj — DME/DDA), Flowserve (gear, screw), Bornemann (twin screw), Leistritz (screw), Verder (peristaltik), Lewa (diyafram/piston), Wilden (AODD)

## Çalışma Prensibi
Pozitif deplasmanlı pompalar, sıvının sabit bir hacmini mekanik olarak yakalayıp (trap) basma tarafına iletir. Debisi basınçtan bağımsızdır — sistem basıncı artsa da debi sabit kalır (ideal durumda). Bu özellik santrifüj pompalardan temel farktır.

### İki Ana Kategori

#### 1. Döner (Rotary) Pompalar
- **Vida pompası (Screw Pump):** İkiz veya üçlü vida ile sıvı taşınır. Pulsasyonsuz, sessiz. Yüksek viskozite için ideal.
- **Dişli pompa (Gear Pump):** İç veya dış dişli çiftleri arasında sıvı iletilir. Yağlama, yakıt iletimi.
- **Lob pompa (Lobe Pump):** İki loblu rotor temassız döner. Hijyenik tasarım — gıda, ilaç.
- **Peristaltik pompa (Peristaltic Pump):** Esnek hortum sıkıştırılarak sıvı iletilir. Aşındırıcı, korozif sıvılar.
- **Progresif kavite (Progressive Cavity / Mono Pump):** Helisel rotor + stator. Yüksek katı içerikli sıvılar.

#### 2. İleri-Geri Hareketli (Reciprocating) Pompalar
- **Pistonlu pompa (Piston Pump):** Piston silindir içinde hareket eder. Çok yüksek basınç (1000+ bar).
- **Plunger pompa:** Piston benzeri ama daha küçük çaplı plunger. Yüksek basınç, düşük debi.
- **Diyafram pompa (Diaphragm Pump):** Esnek membran ile sıvı iletilir. Sızdırmazlık garantili — tehlikeli kimyasallar.
- **AODD (Air-Operated Double Diaphragm):** Basınçlı hava ile çalışan çift diyafram. Portatif, çok yönlü.

## Alt Tip Karşılaştırma

| Alt Tip | Debi Aralığı (m³/h) | Basınç (bar) | Verim (%) | Viskozite | Katı Toleransı |
|---------|---------------------|-------------|-----------|-----------|----------------|
| Vida (Screw) | 1-500 | 1-200 | 70-90 | Çok yüksek | Düşük |
| Dişli (Gear) | 0.1-200 | 1-250 | 70-90 | Çok yüksek | Çok düşük |
| Lob (Lobe) | 1-400 | 1-30 | 60-80 | Yüksek | Orta |
| Peristaltik | 0.1-100 | 1-15 | 50-70 | Yüksek | Yüksek |
| Progresif Kavite | 0.5-300 | 1-72 | 60-80 | Yüksek | Çok yüksek |
| Pistonlu (Piston) | 0.1-200 | 10-1000+ | 80-95 | Düşük-orta | Çok düşük |
| Diyafram | 0.01-50 | 1-1000 | 70-90 | Düşük-orta | Orta |
| AODD | 0.1-60 | 1-8 | 30-50 | Orta | Yüksek |

## Enerji Dağılımı (Tipik — Döner Tip, örn. Vida Pompası)
- Faydalı hidrolik iş: ~65-85%
- Mekanik kayıplar (yatak, conta, dişli): ~5-10%
- İç sızıntı (slip) kayıpları: ~5-15% (viskoziteye bağlı)
- Motor kayıpları: ~5-10%

## Viskozite ve Verimlilik İlişkisi
- Düşük viskozite (<10 cSt): İç sızıntı (slip) artar → verim düşer
- Orta viskozite (10-500 cSt): Optimal çalışma aralığı → en yüksek verim
- Yüksek viskozite (>500 cSt): Sürtünme kayıpları artar ama sızıntı azalır → net verim hala iyi
- Santrifüj pompa ile karşılaştırma: >100 cSt'de PD pompa 10-40 puan daha verimli

## Pulsasyon ve Kompanzatörler
- Reciprocating pompalar doğası gereği pulsasyonlu debi üretir
- Pulsasyon giderme yöntemleri:
  - **Pulsasyon damperi (Pulsation Dampener):** Basma hattına monte, basınç dalgalanmalarını sönümler
  - **Çok silindirli tasarım:** Triplex (3 silindir), quintuplex (5 silindir) ile pulsasyon %90+ azaltılır
  - **Akümülatör:** Gaz yastıklı basınç dengeleyici
- Döner tiplerde (vida, dişli) pulsasyon ihmal edilebilir düzeydedir

## Verimlilik Benchmarkları

| Pompa Tipi | Düşük | Ortalama | İyi | Best-in-class |
|-----------|-------|----------|-----|---------------|
| Vida (Screw) | <%65 | %65-75 | %75-85 | >%85 |
| Dişli (Gear) | <%65 | %65-75 | %75-85 | >%85 |
| Pistonlu/Plunger | <%75 | %75-85 | %85-90 | >%90 |
| Diyafram | <%65 | %65-75 | %75-85 | >%85 |
| Progresif Kavite | <%55 | %55-65 | %65-75 | >%75 |
| Lob | <%55 | %55-65 | %65-75 | >%75 |
| Peristaltik | <%45 | %45-55 | %55-65 | >%65 |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 0.1-500 | Güç analizörü |
| Basma basıncı | bar | 1-1000 | Basınç sensörü |
| Emme basıncı | bar | -0.5 ile +5 | Basınç sensörü |
| Debi | m³/h | 0.01-500 | Flowmeter (Coriolis, manyetik, ultrasonik) |
| Sıvı sıcaklığı | °C | 5-300 | Termometre |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Sıvı viskozitesi | cSt | 0.3-1,000,000 | Viskozimetre veya tablo |
| Sıvı yoğunluğu | kg/m³ | 700-1500 | Yoğunluk ölçer |
| Motor devri | RPM | 100-3500 | Takometre |
| Titreşim | mm/s | <4.5 | Titreşim sensörü |
| Pulsasyon (basınç değişimi) | bar | ±%5-20 | Basınç kaydedici |
| Çalışma saati | saat/yıl | 2000-8760 | Sayaç |

### Nameplate Bilgileri
- Marka ve model (örn. Netzsch NEMO NM 063)
- Pompa tipi (vida, dişli, piston vb.)
- Nominal güç (kW)
- Nominal debi (m³/h veya l/h)
- Nominal basınç (bar)
- Maksimum viskozite (cSt)
- Malzeme (rotor, stator, gövde)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Sıvı yoğunluğu | 1000 kg/m³ | Su varsayımı |
| Sıvı viskozitesi | 100 cSt | PD pompa için orta viskozite varsayımı |
| Pompa verimi | %75 | Vida/dişli pompa ortalaması |
| Motor verimi | %90 | IE3 motor varsayımı |
| Yük oranı | %80 | PD pompalar genelde yüksek yükte çalışır |
| Çalışma saati | 4000 saat/yıl | Tek vardiya |
| cosφ (güç faktörü) | 0.85 | Tipik motor değeri |
| İç sızıntı (slip) | %5 | Orta viskozitede tipik değer |

## Exergy Analizi Farklılıkları
PD pompalarda sabit debi özelliği nedeniyle exergy analizi santrifüj pompalardan farklılık gösterir:

```
η_exergy = Ė_hydraulic / Ė_electric
Ė_hydraulic = ΔP × Q_actual
Q_actual = Q_theoretical - Q_slip
```

- Sabit debi → basınç bazlı kayıp hesabı ön plana çıkar
- İç sızıntı (slip) exergy kaybı olarak değerlendirilir
- Viskoz sıvılarda sürtünme kayıpları irreversibilite kaynağıdır
- Pulsasyonlu akışta ortalama debi ve basınç kullanılmalıdır

## Tipik Uygulama Alanları

| Uygulama | Önerilen Tip | Neden |
|----------|-------------|-------|
| Kimya endüstrisi (dozaj) | Diyafram, pistonlu | Hassas dozajlama, korozif sıvılar |
| Gıda ve içecek | Lob, peristaltik | Hijyenik tasarım, düşük kesme kuvveti |
| Petrol ve gaz | Vida (twin screw), pistonlu | Yüksek viskozite, yüksek basınç |
| Atıksu ve çamur | Progresif kavite, peristaltik | Katı toleransı |
| Boya ve mürekkep | Dişli, diyafram | Viskoz sıvılar, hassas debi |
| Yağlama sistemleri | Dişli, vida | Yağ iletimi, sabit basınç |
| Su arıtma (kimyasal dozaj) | Diyafram (solenoid/motor) | Hassas dozajlama |
| Yüksek basınç temizlik | Pistonlu (plunger) | 100-1000+ bar su jeti |

## Santrifüj vs PD Pompa Karşılaştırma

| Özellik | Santrifüj | Pozitif Deplasmanlı |
|---------|-----------|-------------------|
| Debi-basınç ilişkisi | Basınç artar → debi düşer | Basınç değişir → debi sabit |
| Verim (düşük viskozite) | Yüksek (%75-93) | Orta-yüksek (%70-90) |
| Verim (yüksek viskozite) | Düşük (>100 cSt'de kötü) | Yüksek (viskozite avantajı) |
| Kendi kendine emme | Hayır (priming gerekli) | Evet (self-priming) |
| Debi kontrolü | Vana veya VSD | Devir veya strok ayarı |
| Kuru çalışma toleransı | Hayır (hasar riski) | Tipe bağlı (peristaltik evet) |
| Pulsasyon | Yok | Var (reciprocating tiplerde) |
| İlk yatırım maliyeti | Düşük-orta | Orta-yüksek |

## Dikkat Edilecekler

1. **İç sızıntı (Slip):** Düşük viskoziteli sıvılarda iç sızıntı artar — debi ve verim düşer; pompa tipi ve boşluk (clearance) uygun seçilmeli
2. **Basınç tahliye vanası (Relief Valve):** PD pompalar kapalı vanaya karşı çalışırsa basınç sınırsız artar — emniyet vanası zorunlu
3. **Pulsasyon:** Reciprocating tiplerde pulsasyon boru sistemi yorulmasına neden olabilir — dampener kullanılmalı
4. **Aşınma:** Aşındırıcı sıvılarda rotor/stator aşınması verim kaybının ana nedenidir — malzeme seçimi kritik
5. **Kuru çalışma:** Döner tiplerde (vida, dişli) kuru çalışma ciddi hasara yol açar — koruma gerekli
6. **Viskozite değişimi:** Proses sıcaklığı ile viskozite değişir — tasarımda en kötü senaryo dikkate alınmalı
7. **Enerji karşılaştırması:** Düşük viskoziteli ve yüksek debili uygulamalarda santrifüj pompa daha verimlidir

## İlgili Dosyalar
- Santrifüj pompa: `equipment/pump_centrifugal.md`
- VSD uygulaması: `solutions/pump_vsd.md`
- Benchmark verileri: `benchmarks/pump_benchmarks.md`
- Exergy hesaplamaları: `formulas/pump_exergy.md`

## Referanslar
- Hydraulic Institute Standards (ANSI/HI 3.1-3.5 — Rotary Pumps, ANSI/HI 6.1-6.5 — Reciprocating Pumps)
- Karassik, I.J. et al., "Pump Handbook," McGraw-Hill, 4th Edition
- Netzsch Progressive Cavity Pump Engineering Manual
- Bornemann Twin Screw Pump Technical Documentation
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- Europump Guide to Pump Selection and Energy Assessment
- Nelik, L., "Centrifugal & Rotary Pumps: Fundamentals with Applications," CRC Press
