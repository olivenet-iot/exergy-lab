---
title: "Pompa Motorları ve Sürücüler — Pump Motors and Drives"
category: equipment
equipment_type: pump
subtype: "Motor ve Sürücüler"
keywords: [motor, sürücü, pompa, verimlilik]
related_files: [pump/benchmarks.md, pump/solutions/motor_upgrade.md, pump/solutions/vsd.md]
use_when: ["Pompa motoru değerlendirilirken", "Motor verimliliği analiz edilirken"]
priority: medium
last_updated: 2026-01-31
---
# Pompa Motorları ve Sürücüler — Pump Motors and Drives

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Kapsam: Pompa tahrikinde kullanılan elektrik motorları ve hız sürücüleri
- Motor güç aralığı: 0.12 - 1000 kW
- Yaygın motor tipleri: Asenkron (indüksiyon), senkron PM, relüktans
- Yaygın motor markaları: ABB, Siemens, WEG, Nidec (Leroy-Somer), Grundfos MGE, KSB SuPremE
- Yaygın VSD markaları: ABB (ACS), Siemens (SINAMICS), Danfoss (VLT/VACON), Schneider (Altivar)

## Elektrik Motorları — Asenkron (İndüksiyon) Motor

### Çalışma Prensibi
Stator sargıları tarafından oluşturulan döner manyetik alan, rotorda akım indükler ve moment üretir. Rotor hızı her zaman senkron hızın biraz altındadır (kayma — slip). En yaygın endüstriyel motor tipidir.

### Temel Bileşenler
- **Stator:** Sargılı silindik çekirdek — döner manyetik alan oluşturur
- **Rotor:** Sincap kafesi veya sargılı — indüklenen akımla moment üretir
- **Yataklar:** Bilyalı veya makaralı — rotor taşıyıcı
- **Gövde:** Döküm demir veya alüminyum — mekanik koruma ve soğutma
- **Fan:** Motor soğutması — TEFC (Totally Enclosed Fan Cooled) en yaygın

### Kayıp Türleri
- **Bakır kayıpları (I²R):** Stator ve rotor sargılarında ısı — toplam kaybın %35-50'si
- **Demir kayıpları:** Histerezis ve eddy akım — toplam kaybın %15-25'i
- **Mekanik kayıplar:** Yatak sürtünmesi ve fan — toplam kaybın %5-15'i
- **Kaçak kayıplar:** Stray yük kayıpları — toplam kaybın %10-20'si
- **Ventilasyon kayıpları:** Soğutma fanı — toplam kaybın %5-10'u

## Motor Verimlilik Sınıfları (IEC 60034-30-1)

### Sınıf Tanımları

| Sınıf | İsim | Açıklama |
|-------|------|----------|
| IE1 | Standard Efficiency | Eski standart, artık yetersiz |
| IE2 | High Efficiency | Temel verimlilik seviyesi |
| IE3 | Premium Efficiency | EU MEPS zorunlu seviye (0.75-1000 kW) |
| IE4 | Super-Premium Efficiency | EU zorunlu 75-200 kW (Temmuz 2023'ten) |
| IE5 | Ultra-Premium Efficiency | Kayıplarda IE4'e göre %20 azalma hedefi |

### Verimlilik Değerleri — 4 Kutuplu Motor, 50 Hz (Minimum %)

| Güç (kW) | IE1 (%) | IE2 (%) | IE3 (%) | IE4 (%) | IE5 (%) |
|-----------|---------|---------|---------|---------|---------|
| 0.75 | 72.1 | 77.4 | 80.7 | 83.5 | ~86 |
| 1.5 | 77.2 | 81.4 | 84.2 | 86.7 | ~89 |
| 3.0 | 81.5 | 84.6 | 87.0 | 89.2 | ~91 |
| 5.5 | 84.3 | 87.0 | 89.2 | 91.2 | ~93 |
| 7.5 | 85.8 | 88.1 | 90.4 | 92.1 | ~94 |
| 11 | 87.6 | 89.4 | 91.4 | 93.0 | ~94.5 |
| 15 | 88.7 | 90.3 | 92.1 | 93.6 | ~95 |
| 22 | 89.9 | 91.0 | 93.0 | 94.3 | ~95.5 |
| 37 | 91.2 | 92.2 | 93.7 | 95.0 | ~96 |
| 55 | 92.0 | 93.0 | 94.3 | 95.5 | ~96.5 |
| 75 | 92.5 | 93.2 | 94.7 | 95.8 | ~96.8 |
| 110 | 93.2 | 93.8 | 95.0 | 96.0 | ~97 |
| 160 | 93.8 | 94.3 | 95.4 | 96.3 | ~97.2 |
| 200 | 94.0 | 94.6 | 95.6 | 96.5 | ~97.4 |
| 315 | 94.5 | 95.0 | 96.0 | 96.8 | ~97.5 |
| 500 | 95.0 | 95.4 | 96.2 | 97.0 | ~97.7 |

Not: IE5 değerleri henüz IEC standardında resmi olarak tanımlı değildir — tahmini değerlerdir.

## Kısmi Yük Verimi

Motor verimi tam yükte en yüksek değildir — genellikle %75 yükte optimumdur.

### Kısmi Yük Verim Tablosu (Tipik IE3, 15 kW, 4 kutup)

| Yük (%) | Verim (%) | Güç Faktörü (cosφ) | Akım (% nominal) |
|---------|-----------|---------------------|-------------------|
| 100 | 92.1 | 0.86 | 100 |
| 75 | 92.5 | 0.82 | 78 |
| 50 | 91.5 | 0.73 | 60 |
| 25 | 86.0 | 0.52 | 48 |
| 10 | 70.0 | 0.28 | 42 |

**Kritik nokta:** %25'in altında verim hızla düşer ve güç faktörü çok kötüleşir. Aşırı boyutlu motor = düşük verim + düşük güç faktörü.

## VSD (Variable Speed Drive) — Değişken Hız Sürücüsü

### Çalışma Prensibi (AC-DC-AC)
1. **Doğrultucu (Rectifier):** Şebeke AC gerilimini DC'ye çevirir
2. **DC Bus (Ara devre):** Enerji depolama (kondansatör)
3. **Evirici (Inverter):** DC'yi değişken frekanslı AC'ye çevirir (PWM ile)
4. **Kontrol:** PID veya vektörel kontrol ile motor hız ve moment ayarı

### VSD Kayıpları

| Kayıp Kaynağı | Tipik Değer | Not |
|---------------|-------------|-----|
| Doğrultucu | %0.5-1 | Diyot/IGBT kayıpları |
| DC Bus | <%0.5 | Kondansatör ve filtre |
| Evirici | %1-2 | IGBT anahtarlama kayıpları |
| Kontrol elektroniği | <%0.5 | Sabit kayıp |
| **Toplam VSD kaybı** | **%2-5** | Tam yükte %2-3, kısmi yükte %3-5 |

### VSD Avantajları
- **Enerji tasarrufu:** Kübik yasa sayesinde küçük hız düşüşü = büyük güç tasarrufu
- **Yumuşak yol verme:** Yüksek başlangıç akımı yok (DOL'un 6-8 katı yerine nominal akım)
- **Proses kontrolü:** Hassas debi/basınç kontrolü
- **Mekanik koruma:** Düşük mekanik stres, su darbesi azaltma

### VSD Dezavantajları ve Dikkat Noktaları
- **Harmonik etkiler:** 5., 7., 11., 13. harmonikler — THD %30-80 (6 darbeli doğrultucu)
- **Harmonik azaltma:** Giriş reaktörü, DC link choke, aktif front-end (AFE), 12/18-pulse
- **Motor izolasyonu:** PWM gerilim tepe değerleri motor izolasyonunu zorlayabilir — uzun kablo mesafelerinde dU/dt filtre gerekli
- **Yatak akımları:** Yüksek frekanslı ortak mod gerilimi yatak akımlarına neden olabilir — izole yatak veya topraklama halkaları
- **Minimum hız sınırı:** Motor soğutması düşer — tipik minimum %20-30 hız (TEFC motor için)

## Affinity Laws (Benzerlik Yasaları) — Pompa Hız Değişimi

Santrifüj pompalarda hız değişimi ile debi, basınç ve güç arasındaki ilişki:

```
Benzerlik Yasaları (Sabit çark çapında):

1. Debi ∝ Hız:       Q₁/Q₂ = N₁/N₂
2. Basınç ∝ Hız²:    H₁/H₂ = (N₁/N₂)²
3. Güç ∝ Hız³:       P₁/P₂ = (N₁/N₂)³

Burada:
  Q = Debi (m³/h)
  H = Basma yüksekliği (m) veya basınç (bar)
  P = Mil gücü (kW)
  N = Devir sayısı (RPM)

Örnek: Hız %80'e düşürülürse (N₂/N₁ = 0.80):
  Debi:   Q₂ = Q₁ × 0.80 = %80
  Basınç: H₂ = H₁ × 0.64 = %64
  Güç:    P₂ = P₁ × 0.512 = %51.2 → yaklaşık %49 enerji tasarrufu!
```

### Affinity Laws — Pratik Tasarruf Tablosu

| Hız Oranı (%) | Debi (%) | Basınç (%) | Güç (%) | Tasarruf (%) |
|----------------|----------|------------|---------|--------------|
| 100 | 100 | 100 | 100 | 0 |
| 90 | 90 | 81 | 72.9 | 27.1 |
| 80 | 80 | 64 | 51.2 | 48.8 |
| 70 | 70 | 49 | 34.3 | 65.7 |
| 60 | 60 | 36 | 21.6 | 78.4 |
| 50 | 50 | 25 | 12.5 | 87.5 |

**Önemli:** Bu değerler sıfır statik basınçlı sistemler içindir. Statik basınç varsa tasarruf daha düşük olur.

## Affinity Laws — Çark Kesimi (Impeller Trimming)

```
Sabit hızda çark çapı değişimi:

1. Debi ∝ Çap:       Q₁/Q₂ = D₁/D₂
2. Basınç ∝ Çap²:    H₁/H₂ = (D₁/D₂)²
3. Güç ∝ Çap³:       P₁/P₂ = (D₁/D₂)³

Burada:
  D = Çark (impeller) çapı (mm)

Not: ±%10 çap değişiminde doğruluk yüksektir.
     Daha büyük değişimlerde verim kayıpları oluşabilir.
```

## Motor-Pompa Eşleştirme Kuralları

### Motor Boyutlandırma
- Motor gücü, pompa maksimum mil gücünün %10-15 üzerinde seçilir (service factor)
- Service factor (SF): Tipik 1.0-1.15 (IEC), 1.15-1.25 (NEMA)
- **Aşırı boyutlama kaçınılmalı:** Motor verimi ve güç faktörü düşer

### Eşleştirme Tablosu (Tipik)

| Pompa Mil Gücü (kW) | Önerilen Motor (kW) | Service Factor |
|----------------------|---------------------|----------------|
| 2.5 | 3.0 | 1.20 |
| 5.0 | 5.5 | 1.10 |
| 10 | 11 | 1.10 |
| 20 | 22 | 1.10 |
| 45 | 45 veya 55 | 1.0-1.22 |
| 90 | 90 veya 110 | 1.0-1.22 |

## Güç Faktörü ve Düzeltme

```
Güç faktörü:
cosφ = P / S

Burada:
  P = Aktif güç (kW)
  S = Görünür güç (kVA)

Reaktif güç telafisi:
Q_c = P × (tanφ₁ - tanφ₂)

Burada:
  Q_c  = Gerekli kondansatör gücü (kVAr)
  φ₁   = Mevcut güç faktörü açısı
  φ₂   = Hedef güç faktörü açısı (tipik cosφ₂ = 0.95)
```

### Tipik Güç Faktörü Değerleri

| Durum | cosφ | Not |
|-------|------|-----|
| Motor tam yük | 0.82-0.90 | Motor boyutuna bağlı |
| Motor %50 yük | 0.65-0.78 | Düşer |
| Motor %25 yük | 0.40-0.55 | Çok düşük — telafi gerekli |
| VSD ile çalışma | 0.95-0.99 | VSD giriş güç faktörü iyi |
| Hedef (tesiste) | >0.95 | Ceza/prim sınırı |

## Yumuşak Yol Verici (Soft Starter) vs VSD

| Özellik | Soft Starter | VSD |
|---------|-------------|-----|
| Yol verme akımı | 2-4× nominal | 1× nominal |
| Sürekli hız kontrolü | Hayır | Evet |
| Enerji tasarrufu | Sadece yol vermede | Sürekli (kübik yasa) |
| Maliyet | Düşük (%30-50 VSD'nin) | Yüksek |
| Harmonik etki | Düşük (sadece yol verme) | Orta-yüksek (sürekli) |
| Uygulama | Sabit hız, nadir başlatma | Değişken yük, sürekli kontrol |
| Tipik kullanım | Büyük pompalar, fan, konveyör | Pompa, fan, kompresör |

## EU MEPS (Minimum Energy Performance Standards)

### EU Ecodesign Regulation 2019/1781

| Güç Aralığı | Zorunlu Minimum | Yürürlük Tarihi |
|-------------|----------------|-----------------|
| 0.12 - 0.75 kW (3 fazlı) | IE2 | 1 Temmuz 2021 |
| 0.75 - 1000 kW (3 fazlı, 2-8 kutup) | IE3 | 1 Temmuz 2021 |
| 75 - 200 kW (3 fazlı, 2-6 kutup) | IE4 | 1 Temmuz 2023 |
| Ex eb motorlar (0.12 - 1000 kW) | IE2 | 1 Temmuz 2023 |
| Tek fazlı motorlar (≥0.12 kW) | IE2 | 1 Temmuz 2023 |
| VSD'ler (0.12 - 1000 kW) | IE2 (kayıp sınıfı) | 1 Temmuz 2021 |

### Etki
- EU'da 380 milyon motor, toplam elektrik tüketiminin %56'sını oluşturur
- 2030'a kadar yılda 106 TWh tasarruf hedefi
- IE4 zorunluluğu dünyada ilk kez EU tarafından uygulanmıştır

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü (aktif) | kW | 0.12-1000 | Güç analizörü (3 fazlı) |
| Gerilim | V | 380-690 | Voltmetre |
| Akım | A | 0.5-1500 | Pens ampermetre / CT |
| Güç faktörü | - | 0.3-0.99 | Güç analizörü |
| Motor devri | RPM | 300-3600 | Takometre / VSD ekranı |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Motor sıcaklığı (gövde) | °C | 40-120 | Kızılötesi termometre |
| Titreşim | mm/s | <4.5 (ISO 10816) | Titreşim sensörü |
| İzolasyon direnci | MΩ | >5 | Megger testi |
| Harmonik bozulma (THD) | % | 5-80 | Güç kalitesi analizörü |
| VSD çıkış frekansı | Hz | 10-60 | VSD ekranı |

### Nameplate Bilgileri
- Marka ve model
- Nominal güç (kW)
- Nominal gerilim (V) ve akım (A)
- Nominal devir (RPM) ve frekans (Hz)
- Verimlilik sınıfı (IE1/IE2/IE3/IE4/IE5)
- Koruma sınıfı (IP55, IP56 vb.)
- İzolasyon sınıfı (F, H)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Motor verimi | Tablo referans | IE sınıfı ve güce göre yukarıdaki tablodan |
| Motor yük oranı | %75 | Endüstriyel ortalama |
| cosφ (tam yükte) | 0.85 | Tipik asenkron motor |
| VSD verimi | %97 | Modern VSD (>5 kW) |
| VSD harmonik (THD-i) | %35 | 6 darbeli, filtre yok |
| Minimum VSD hızı | %30 nominal | TEFC motor soğutma sınırı |
| Motor ömrü | 20 yıl | İyi bakım koşullarında |
| Service factor | 1.10 | IEC standart |

## Dikkat Edilecekler

1. **Aşırı motor boyutlama:** Pompa motorlarının %60'ından fazlası gereğinden büyük seçilir — verim ve güç faktörü düşer
2. **VSD minimum hız:** TEFC motorlarda %20-30 altında soğutma yetersiz kalır — harici soğutma veya ayrı fan gerekli
3. **Harmonikler:** VSD'ler şebekeye harmonik enjekte eder — hassas ekipmanları etkileyebilir, giriş filtresi değerlendirilmeli
4. **Yatak akımları:** VSD ile uzun kabloda yatak akımları oluşabilir — izole yatak veya shaft grounding ring
5. **Kablo mesafesi:** Motor-VSD arası 100 m'den fazla ise dU/dt filtre veya sinüs filtre gerekli
6. **Motor IE sınıfı yükseltme:** IE1→IE3 motor değişimi %3-8 verim artışı sağlar, geri ödeme 1-3 yıl
7. **Güç faktörü düzeltme:** VSD'siz motorlarda düşük yükte güç faktörü çok düşer — kondansatör bataryası değerlendirilmeli
8. **Yol verme yöntemi:** DOL yol verme büyük pompalarda mekanik stres ve gerilim düşümü yapar — soft starter veya VSD tercih edilmeli

## İlgili Dosyalar
- Pompa sistemleri genel: `equipment/pumping_systems_overview.md`
- Hidrofor: `equipment/pump_booster.md`
- Vakum pompaları: `equipment/pump_vacuum.md`

## Referanslar
- IEC 60034-30-1:2014 — "Rotating electrical machines — Efficiency classes of line operated AC motors"
- EU Regulation 2019/1781 — Ecodesign requirements for electric motors and variable speed drives
- ABB, "Technical Note: IEC 60034-30-1 Standard on Efficiency Classes"
- Siemens, "Motor Efficiency and Variable Speed Drives — Application Guide"
- DOE/AMO, "Improving Motor and Drive System Performance: A Sourcebook for Industry"
- Europump & Hydraulic Institute, "Variable Speed Pumping — A Guide to Successful Applications"
- Bonfiglioli, "Energy Efficiency Standards for Electric Motors and Power Drive Systems"
- NEMA MG 1 — Motors and Generators
- IEEE 519 — Harmonics in Power Systems
