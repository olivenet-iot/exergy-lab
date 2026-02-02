---
title: "Isı Entegrasyonu ve Kaynak-Kullanım Eşleştirme (Heat Integration and Source-Sink Matching)"
category: factory
equipment_type: factory
keywords: [ısı entegrasyonu, pinch, fabrika]
related_files: [factory/pinch_analysis.md, factory/waste_heat_recovery.md, factory/cross_equipment.md, factory/pinch/INDEX.md, factory/pinch/fundamentals.md, factory/pinch/composite_curves.md, factory/pinch/hen_design.md, factory/pinch/hen_retrofit.md, factory/pinch/stream_data.md]
use_when: ["Isı entegrasyonu değerlendirilirken", "Proses ısı alışverişi optimize edilirken", "Pinch tabanlı ısı entegrasyon tasarımı yapılırken"]
priority: high
last_updated: 2026-02-01
---
# Isı Entegrasyonu ve Kaynak-Kullanım Eşleştirme (Heat Integration and Source-Sink Matching)

> Son güncelleme: 2026-01-31

## Genel Bakış

Isı entegrasyonu, bir fabrikanın farklı proseslerinden çıkan atık ısının, ısı ihtiyacı olan diğer proseslere yönlendirilmesiyle toplam enerji tüketimini azaltma stratejisidir. Kaynak-kullanım eşleştirme (source-sink matching), mevcut ısı kaynaklarını en uygun ısı tüketicileriyle sistematik olarak eşleştiren metodolojik bir yaklaşımdır. Doğru uygulandığında fabrika seviyesinde %10-30 yakıt tasarrufu sağlanabilir.

## 1. Isı Kaynakları ve Isı Kullanıcıları (Heat Sources and Sinks)

### 1.1 Fabrikadaki Tipik Isı Kaynakları

Endüstriyel tesislerde ısı kayıpları çeşitli noktalarda oluşur. Aşağıdaki tablo, yaygın ısı kaynaklarını sıcaklık seviyelerine göre sınıflandırır:

| Isı Kaynağı | Sıcaklık Aralığı [°C] | Tipik Debi | Elde Edilebilir Güç [kW] | Süreklilik |
|---|---|---|---|---|
| Baca gazı (kazan) | 150–250 | 2,000–10,000 Nm³/h | 50–500 | Sürekli |
| Baca gazı (fırın/kurutma) | 250–600 | 1,000–20,000 Nm³/h | 100–2,000 | Vardiya bazlı |
| Kompresör soğutma suyu | 70–90 | 2–20 m³/h | 20–150 | Sürekli |
| Kompresör soğutma havası | 60–80 | 500–5,000 m³/h | 15–100 | Sürekli |
| Kondenser atık ısısı (chiller) | 35–45 | 5–50 m³/h | 50–500 | Mevsimsel/sürekli |
| Proses soğutma suyu | 40–60 | 5–100 m³/h | 30–500 | Proses bağımlı |
| Kurutma fırını egzozu (konvektif) | 80–150 | 2,000–15,000 m³/h | 50–800 | Vardiya bazlı |
| Kurutma fırını egzozu (sprey) | 70–100 | 5,000–50,000 m³/h | 100–2,000 | Sürekli |
| Buhar kondensat dönüşü | 80–100 | 1–10 m³/h | 20–200 | Sürekli |
| Proses atık suyu | 30–60 | 2–50 m³/h | 10–200 | Proses bağımlı |

### 1.2 Fabrikadaki Tipik Isı Kullanıcıları (Heat Sinks)

| Isı Kullanıcısı | Gerekli Sıcaklık [°C] | Tipik Güç [kW] | Esneklik |
|---|---|---|---|
| Kazan besleme suyu ön ısıtma | 15 → 80 (hedef) | 50–500 | Yüksek |
| Bina ısıtma (radyatör) | 45–70 | 50–500 | Mevsimsel |
| Bina ısıtma (yerden) | 30–45 | 30–300 | Mevsimsel |
| Proses sıcak su | 50–90 | 20–500 | Proses bağımlı |
| Hammadde ön ısıtma | 20–60 | 10–200 | Proses bağımlı |
| Boyama banyosu ısıtma | 60–100 | 100–1,000 | Kesikli |
| Kurutma havası ön ısıtma | 40–150 | 50–2,000 | Vardiya bazlı |
| Yakma havası ön ısıtma | 100–300 | 50–500 | Sürekli |
| Sıcak kullanım suyu (DWH) | 45–60 | 5–50 | Sürekli |

### 1.3 Sıcaklık Seviyesi Sınıflandırması

Isı kaynaklarının ve kullanıcılarının sıcaklık seviyesine göre sınıflandırılması, eşleştirme sürecinin temelidir:

| Sıcaklık Seviyesi | Aralık [°C] | Exergy Kalitesi | Tipik Kaynaklar | Tipik Kullanıcılar |
|---|---|---|---|---|
| Yüksek (High) | >400 | Yüksek (Carnot >0.56) | Fırın baca gazı, yakma odası | Buhar üretimi, güç üretimi |
| Orta-yüksek (Medium-high) | 200–400 | Orta-yüksek | Kazan baca gazı, kurutma | Buhar, yakma havası ön ısıtma |
| Orta (Medium) | 100–200 | Orta (Carnot 0.20–0.40) | Kurutma egzozu, kondenser | Proses ısıtma, buhar (düşük basınç) |
| Düşük (Low) | 50–100 | Düşük | Kompresör, soğutma suyu | Besleme suyu, bina ısıtma |
| Çok düşük (Very low) | <50 | Çok düşük (Carnot <0.08) | Kondenser, atık su | Yerden ısıtma, ısı pompası kaynağı |

## 2. Sıcaklık Kademesi Prensibi (Temperature Cascading)

### 2.1 Temel İlke

Sıcaklık kademesi (cascading), yüksek sıcaklıklı ısının önce yüksek sıcaklık gerektiren proseslere, ardından sıralı olarak daha düşük sıcaklık gerektiren proseslere aktarılmasıdır. Bu yaklaşım exergy yıkımını minimize eder.

```
Temel kural: Isıyı her zaman mümkün olan en yüksek sıcaklık seviyesinde kullanın.
Her sıcaklık düşüşü kademesi en az ΔT_min = 10-20°C olmalıdır.

Exergy tasarrufu:
ΔEx_kurtarılan = Q̇ × (1 - T₀/T_kaynak) - Q̇ × (1 - T₀/T_kullanıcı)
                = Q̇ × T₀ × (1/T_kullanıcı - 1/T_kaynak)

Burada:
- Q̇ = transfer edilen ısı miktarı [kW]
- T₀ = referans sıcaklık [K] (298.15 K)
- T_kaynak = ısı kaynağı sıcaklığı [K]
- T_kullanıcı = ısı kullanıcısı sıcaklığı [K]
```

### 2.2 Sıcaklık Kademesi Diyagramı (ASCII)

```
Sıcaklık [°C]
    |
600 | ████ Fırın baca gazı
    |   ↓
400 | ████ Buhar üretimi (yüksek basınç)
    |   ↓ ......... Kazan baca gazı
250 | ████ Yakma havası ön ısıtma
    |   ↓ ......... Kurutma egzozu
150 | ████ Proses ısıtma / buhar (düşük basınç)
    |   ↓ ......... Kompresör atık ısısı
 90 | ████ Kazan besleme suyu ön ısıtma
    |   ↓
 70 | ████ Bina ısıtma (radyatör)
    |   ↓ ......... Kondenser atık ısısı
 45 | ████ Yerden ısıtma / sıcak su
    |   ↓
 25 | ████ Referans sıcaklık (ölü durum)
    |
    └──────────────────────────────── Kademe
         1     2     3     4     5

████ = Isı kullanıcısı (sink)
..... = Isı kaynağı (source)
  ↓  = Isı akışı yönü (yüksek → düşük sıcaklık)
```

### 2.3 Kademeli Kullanım Verimi

```
Tek kademeli kullanım:
η_cascade,1 = Q̇_kullanılan / Q̇_kaynak

Çok kademeli kullanım:
η_cascade,n = Σᵢ Q̇_kullanılan,i / Q̇_kaynak

Exergy bazlı kademe verimi:
η_ex,cascade = Σᵢ [Q̇ᵢ × (1 - T₀/Tᵢ)] / [Q̇_kaynak × (1 - T₀/T_kaynak)]

Hedef: η_cascade,n > 0.70 (kaynağın %70'inden fazlasını kullanmak)
```

## 3. Kaynak-Kullanım Eşleştirme Metodolojisi (Source-Sink Matching)

### 3.1 Sistematik Eşleştirme Adımları

```
Adım 1: Envanter
├── Tüm ısı kaynaklarını listele (sıcaklık, güç, süreklilik)
├── Tüm ısı kullanıcılarını listele (sıcaklık, güç, zaman profili)
└── Her akış için exergy içeriğini hesapla

Adım 2: Uygunluk analizi
├── Sıcaklık uyumluluğu: T_kaynak > T_kullanıcı + ΔT_min
├── Güç uyumu: Q̇_kaynak ≥ Q̇_kullanıcı (veya kısmi eşleştirme)
├── Zaman uyumu: Eşzamanlı mevcut olma (veya depolama ile)
└── Konum uyumu: Fiziksel mesafe ve boru güzergahı

Adım 3: Eşleştirme matrisi
├── Uyumlu çiftleri puan tablosuyla değerlendir
├── Sıcaklık eşleştirmesini en üst öncelik yap
└── Exergy yıkımını minimize edecek eşleşmeleri seç

Adım 4: Ekonomik değerlendirme
├── Her eşleşme için yatırım maliyetini hesapla
├── Yıllık enerji tasarrufunu belirle
├── Geri ödeme süresini ve NPV'yi hesapla
└── Önceliklendirme yap
```

### 3.2 Kaynak-Kullanım Eşleştirme Matrisi

Aşağıdaki matris, tipik bir fabrikadaki ısı kaynağı-kullanıcı uyumluluğunu gösterir:

| Kaynak ↓ / Kullanıcı → | Kazan Besleme Suyu | Yakma Havası Ön Isıtma | Bina Isıtma | Proses Sıcak Su | Kurutma Ön Isıtma | Yerden Isıtma |
|---|---|---|---|---|---|---|
| Baca gazı (yüksek) | +++ | +++ | ++ | +++ | +++ | + |
| Baca gazı (orta) | +++ | ++ | ++ | +++ | +++ | + |
| Kompresör atık ısı | ++ | - | +++ | ++ | + | +++ |
| Kondenser atık ısı | + | - | ++ | + | - | +++ |
| Kurutma egzozu | ++ | + | ++ | ++ | +++ | + |
| Proses soğutma suyu | + | - | ++ | + | - | ++ |
| Buhar kondensat | +++ | - | ++ | +++ | ++ | + |

```
Uyumluluk puanı:
+++ = Mükemmel uyum (sıcaklık ve güç eşleşmesi ideal)
++  = İyi uyum (uygulanabilir, bazı sınırlamalar)
+   = Sınırlı uyum (özel koşullarda mümkün)
-   = Uyumsuz (sıcaklık yetersiz veya ekonomik değil)
```

## 4. Sıcaklık-Entalpi Eşleştirme (Temperature-Enthalpy Matching)

### 4.1 Bileşik Eğriler (Composite Curves) Basitleştirilmiş Yaklaşım

```
Pinch Analizi Temel Adımları:
1. Tüm sıcak akışları (soğutulacak) listele → Sıcak bileşik eğri
2. Tüm soğuk akışları (ısıtılacak) listele → Soğuk bileşik eğri
3. ΔT_min belirle (genellikle 10-20°C)
4. Eğrileri ΔT_min kadar kaydırarak pinch noktasını bul
5. Pinch noktasının üstü → yalnızca dış ısı kaynağı (utility)
6. Pinch noktasının altı → yalnızca dış soğutma

Minimum dış ısı gereksinimi (Q_H,min):
Sıcak bileşik eğrinin üst ucundaki enerji farkı

Minimum dış soğutma gereksinimi (Q_C,min):
Soğuk bileşik eğrinin alt ucundaki enerji farkı

Maksimum ısı geri kazanım potansiyeli:
Q_geri_kazanım = Q_H,toplam - Q_H,min = Q_C,toplam - Q_C,min
```

### 4.2 Basitleştirilmiş Bileşik Eğri Diyagramı (ASCII)

```
Sıcaklık [°C]
    |
250 |          /
    |         / Sıcak bileşik eğri
200 |        /   (soğutulacak akışlar)
    |  ΔT_min ↔ /
150 |    /    /
    |   /   /
100 |  /   /    ← Pinch noktası
    | /   /
 50 |/   / Soğuk bileşik eğri
    |   /   (ısıtılacak akışlar)
 25 |  /
    |
    └──────────────────────── Entalpi [kW]
    0   200   400   600   800  1000

    |←Q_C,min→|←─ Q_geri_kazanım ─→|←Q_H,min→|
```

## 5. Isı Geri Kazanım Potansiyeli Değerlendirmesi (Heat Recovery Potential)

### 5.1 Kaynak Türüne Göre Geri Kazanım Potansiyeli

| Isı Kaynağı | Mevcut Isı [kW] | Geri Kazanılabilir [%] | Net Kazanım [kW] | Tipik Teknoloji |
|---|---|---|---|---|
| Baca gazı (kazan, 200°C) | 200 | 50–70 | 100–140 | Economizer, kondenserli |
| Baca gazı (fırın, 500°C) | 800 | 40–60 | 320–480 | Atık ısı kazanı, recuperator |
| Kompresör (37 kW) | 26 | 60–80 | 16–21 | Plakalı eşanjör |
| Chiller kondenser (200 kW) | 250 | 30–50 | 75–125 | Desuperheater |
| Kurutma egzozu (120°C) | 300 | 40–60 | 120–180 | Isı tekeri, runaround |
| Proses soğutma suyu | 150 | 50–70 | 75–105 | Plakalı eşanjör |
| Buhar kondensat | 80 | 80–95 | 64–76 | Kondensat tankı + pompa |

### 5.2 Geri Kazanım Hesaplama Formülü

```
Isı geri kazanım miktarı:
Q̇_geri = ṁ × Cp × (T_giriş - T_çıkış) × η_eşanjör [kW]

Burada:
- ṁ = kütle debisi [kg/s]
- Cp = özgül ısı kapasitesi [kJ/(kg·K)]
- T_giriş = kaynak giriş sıcaklığı [°C]
- T_çıkış = kaynak çıkış sıcaklığı [°C]
- η_eşanjör = eşanjör etkinliği [0.60–0.90]

Yıllık enerji tasarrufu:
E_tasarruf = Q̇_geri × t_çalışma / η_kazan [kWh/yıl]

Yıllık maliyet tasarrufu:
C_tasarruf = E_tasarruf × c_yakıt [€/yıl]

Burada:
- t_çalışma = yıllık çalışma süresi [saat]
- η_kazan = mevcut kazan verimi [oran]
- c_yakıt = yakıt birim maliyeti [€/kWh]
```

## 6. Hesaplama Örneği: Tekstil Fabrikası Isı Entegrasyonu

### 6.1 Fabrika Profili

```
Orta ölçekli tekstil fabrikası (boyama ve terbiye):
- Üretim kapasitesi: 15 ton kumaş/gün
- Kazan: 6 ton/h buhar, doğalgaz, η = %88
- Kompresör: 55 kW (vidalı, su soğutmalı)
- Chiller: 150 kW soğutma kapasitesi
- Kurutma makinesi: 3 adet, doğalgaz yakıtlı
- Çalışma: 6,000 saat/yıl, 2 vardiya
- Doğalgaz fiyatı: €0.045/kWh
- Elektrik fiyatı: €0.12/kWh
```

### 6.2 Isı Kaynağı Envanteri

| Kaynak | T_giriş [°C] | T_çıkış [°C] | Q̇ [kW] | t [saat/yıl] | E [MWh/yıl] |
|---|---|---|---|---|---|
| Kazan baca gazı | 210 | 120 (hedef) | 180 | 6,000 | 1,080 |
| Kompresör soğutma suyu | 78 | 55 (hedef) | 32 | 6,000 | 192 |
| Kurutma egzozu (3 adet) | 130 | 70 (hedef) | 250 | 4,500 | 1,125 |
| Boyama atık suyu | 55 | 35 (hedef) | 85 | 4,000 | 340 |
| **Toplam** | | | **547** | | **2,737** |

### 6.3 Isı Kullanıcısı Envanteri

| Kullanıcı | T_giriş [°C] | T_çıkış [°C] | Q̇ [kW] | t [saat/yıl] | E [MWh/yıl] |
|---|---|---|---|---|---|
| Kazan besleme suyu | 15 | 70 | 230 | 6,000 | 1,380 |
| Boyama banyosu ön ısıtma | 20 | 60 | 120 | 4,000 | 480 |
| Bina ısıtma | 25 | 45 | 80 | 3,000 | 240 |
| Sıcak kullanım suyu | 15 | 55 | 25 | 6,000 | 150 |
| **Toplam** | | | **455** | | **2,250** |

### 6.4 Kaynak-Kullanım Eşleştirme Sonuçları

```
Eşleştirme 1: Kazan baca gazı → Kazan besleme suyu ön ısıtma
- Q̇_geri = 180 kW × 0.80 (etkinlik) = 144 kW
- Besleme suyu: 15°C → 55°C (kısmi ön ısıtma)
- Yatırım: Economizer = €22,000
- Yıllık tasarruf: 144 × 6,000 / 0.88 / 1,000 × €0.045 = €44,182/yıl
  → SPP = 22,000 / 44,182 = 0.50 yıl (6 ay)

Eşleştirme 2: Kurutma egzozu → Kurutma havası ön ısıtma (rekuperatif)
- Q̇_geri = 250 kW × 0.55 (kirli gaz, düşük etkinlik) = 138 kW
- Yatırım: Isı tekeri + kanal = €35,000
- Yıllık tasarruf: 138 × 4,500 / 0.88 / 1,000 × €0.045 = €31,761/yıl
  → SPP = 35,000 / 31,761 = 1.10 yıl

Eşleştirme 3: Kompresör atık ısı → Sıcak kullanım suyu + bina ısıtma
- Q̇_geri = 32 kW × 0.70 = 22 kW
- Yatırım: Plakalı eşanjör + boru = €8,000
- Yıllık tasarruf (DWH): 22 × 6,000 / 1,000 × €0.045 = €5,940/yıl
  (kazan yakıtı yerine)
  → SPP = 8,000 / 5,940 = 1.35 yıl

Eşleştirme 4: Boyama atık suyu → Taze su ön ısıtma
- Q̇_geri = 85 kW × 0.60 = 51 kW
- Yatırım: Paslanmaz plakalı eşanjör + filtre = €15,000
- Yıllık tasarruf: 51 × 4,000 / 0.88 / 1,000 × €0.045 = €10,432/yıl
  → SPP = 15,000 / 10,432 = 1.44 yıl
```

### 6.5 Toplam Ekonomik Değerlendirme

| Eşleştirme | Yatırım [€] | Yıllık Tasarruf [€/yıl] | SPP [yıl] | NPV (10 yıl, %10) [€] |
|---|---|---|---|---|
| Baca gazı → Besleme suyu | 22,000 | 44,182 | 0.50 | 249,500 |
| Kurutma → Hava ön ısıtma | 35,000 | 31,761 | 1.10 | 160,200 |
| Kompresör → DWH + bina | 8,000 | 5,940 | 1.35 | 28,500 |
| Atık su → Taze su ön ısıtma | 15,000 | 10,432 | 1.44 | 49,100 |
| **Toplam** | **80,000** | **92,315** | **0.87** | **487,300** |

```
Sonuç:
- Toplam yatırım: €80,000
- Toplam yıllık tasarruf: €92,315/yıl
- Bileşik geri ödeme süresi: 0.87 yıl (10.4 ay)
- Yakıt tasarrufu: ~%18 (kazan + kurutma yakıt tüketiminde)
- CO₂ azaltımı: ~360 ton CO₂/yıl
```

## 7. Engeller ve Çözümler (Barriers and Solutions)

### 7.1 Teknik Engeller

| Engel | Açıklama | Çözüm |
|---|---|---|
| Mesafe | Kaynak ve kullanıcı fiziksel olarak uzak | İzoleli boru hattı, runaround coil sistemi |
| Sıcaklık uyumsuzluğu | Kaynak sıcaklığı kullanıcı için yetersiz | Isı pompası ile sıcaklık yükseltme |
| Zaman uyumsuzluğu | Kaynak ve kullanıcı farklı zamanlarda aktif | Termal enerji depolama (TES) |
| Kirli akışlar | Baca gazı, kurutma egzozu partikül içerir | Ön filtreleme, runaround coil (dolaylı) |
| Korozyon | Baca gazında asit çiğ noktası altına düşme | Korozyona dayanıklı malzeme, çıkış T kontrolü |
| Değişken yükler | Kaynak/kullanıcı debisi dalgalanır | Tampon tankı, kontrol vanaları, bypass |

### 7.2 Ekonomik Engeller

| Engel | Açıklama | Çözüm |
|---|---|---|
| Yüksek yatırım | Özellikle uzun boru hatları | Aşamalı uygulama, ESCO modeli |
| Düşük enerji fiyatı | Tasarruf değeri yetersiz | LCC analizi, gelecek fiyat projeksiyonu |
| Bütçe kısıtı | Yatırım fonlarının sınırlılığı | Devlet teşvikleri (VAP), leasing |
| Belirsizlik | Üretim planı değişkenliği | Duyarlılık analizi, esnek tasarım |

## 8. Tipik Geri Ödeme Süreleri (Typical Payback Periods)

| Isı Geri Kazanım Projesi | Yatırım [€] | SPP [yıl] | Güvenilirlik |
|---|---|---|---|
| Kazan economizer | 15,000–40,000 | 0.5–2.0 | Düşük |
| Kondenserli economizer (baca gazı) | 25,000–60,000 | 1.0–3.0 | Düşük |
| Kompresör ısı geri kazanım | 5,000–15,000 | 1.0–3.0 | Düşük |
| Kurutma egzoz ısı geri kazanım | 20,000–50,000 | 1.0–2.5 | Ortalama |
| Atık su ısı geri kazanım | 10,000–30,000 | 1.5–3.5 | Ortalama |
| Chiller kondenser ısı geri kazanım | 8,000–20,000 | 2.0–4.0 | Ortalama |
| Isı tekeri (rotary heat exchanger) | 15,000–40,000 | 1.5–3.0 | Düşük |
| Runaround coil sistemi | 20,000–50,000 | 2.0–4.0 | Ortalama |
| Termal enerji depolama (TES) | 30,000–100,000 | 3.0–6.0 | İyi |
| Isı pompası (kaynak yükseltme) | 40,000–120,000 | 3.0–7.0 | İyi |

### Performans Sınıflandırması

| SPP [yıl] | Değerlendirme | Öncelik |
|---|---|---|
| <1 | Mükemmel | Hemen uygula |
| 1–2 | İyi | Yüksek öncelik |
| 2–3 | Ortalama | Normal bütçe döngüsünde |
| 3–5 | Düşük | Stratejik planlama |
| >5 | Kritik değerlendirme gerekli | Özel gerekçe ile |

## 9. Isı Entegrasyonu Performans Göstergeleri

| Performans Kriteri | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| Isı geri kazanım oranı | <%10 | %10–25 | %25–40 | >%40 |
| Kaynak-kullanım eşleşme sayısı | 0–1 | 2–3 | 4–5 | >5 |
| Kademe sayısı (cascade) | 1 | 2 | 3 | >3 |
| Exergy verim artışı | <%3 | %3–8 | %8–15 | >%15 |
| Yakıt tasarruf oranı | <%5 | %5–15 | %15–25 | >%25 |

## 10. ExergyLab Platformunda Isı Entegrasyonu

### 10.1 Otomatik Kaynak-Kullanım Eşleştirme

ExergyLab platformu, kullanıcının girdiği ekipman verilerinden otomatik olarak ısı kaynaklarını ve kullanıcılarını tespit eder. Eşleştirme algoritması aşağıdaki adımları izler:

```
1. Veri toplama: Kazan, kompresör, chiller, pompa verilerinden
   atık ısı kaynaklarını ve ısı ihtiyaçlarını çıkar
2. Sıcaklık filtreleme: T_kaynak > T_kullanıcı + ΔT_min (10°C)
3. Güç eşleştirme: Q̇_kaynak ve Q̇_kullanıcı oranını kontrol et
4. Puanlama: Sıcaklık uyumu (%40), güç uyumu (%25),
   mesafe tahmini (%15), ekonomik değer (%20)
5. Öneri listesi: Puan sırasına göre entegrasyon fırsatları
```

### 10.2 Platformda Kullanılan Eşleştirme Kuralları

```
Kural 1: Kompresör atık ısısı (70-90°C)
  → Kazan besleme suyu ön ısıtma (öncelik 1)
  → Bina ısıtma (öncelik 2, kış ayları)
  → Sıcak kullanım suyu (öncelik 3)
  Detay: cross_equipment.md Bölüm 1-2

Kural 2: Kazan baca gazı (150-250°C)
  → Economizer (besleme suyu ön ısıtma, öncelik 1)
  → Yakma havası ön ısıtma (öncelik 2)
  Detay: ../boiler/solutions/ dizini

Kural 3: Chiller kondenser ısısı (35-45°C)
  → Yerden ısıtma (öncelik 1, kış)
  → Düşük sıcaklık ön ısıtma (öncelik 2)
  Detay: ../chiller/solutions/ dizini

Kural 5: Kurutma fırını egzozu (80-150°C)
  → Kazan besleme suyu ön ısıtma (öncelik 1)
  → Kurutma havası ön ısıtma / geri devir (öncelik 2)
  → Bina ısıtma (öncelik 3, kış ayları)
  Detay: ../dryer/solutions/exhaust_heat_recovery.md, cross_equipment.md

Kural 6: Kazan/fırın → Kurutma havası ön ısıtma
  → Kazan baca gazı (150-250°C) → kurutma havası ön ısıtma
  → Kiln/fırın egzozu (250-600°C) → kurutma havası (seramik sektörü)
  Detay: cross_equipment.md (kurutma entegrasyonu), ../dryer/solutions/

Kural 4: Yüksek sıcaklık kaynaklar (>200°C)
  → ORC ile güç üretimi (büyük kapasite)
  → Buhar üretimi (orta kapasite)
  Detay: waste_heat_recovery.md, cogeneration.md
```

## İlgili Dosyalar

### Pinch Analizi Detaylı Bilgi Tabanı (`pinch/`)
- [Pinch Bilgi Tabanı İndeks](pinch/INDEX.md) — 18 dosyalık detaylı pinch analizi bilgi tabanı navigasyonu
- [Pinch Temelleri](pinch/fundamentals.md) — Linnhoff metodolojisi, MER hedefleri, 3 altın kural
- [Bileşik Eğriler](pinch/composite_curves.md) — Hot/Cold composite curve oluşturma
- [HEN Tasarımı](pinch/hen_design.md) — Grid diyagramı, CP kuralları, akış bölme
- [HEN Retrofit](pinch/hen_retrofit.md) — Cross-pinch tespiti, aşamalı retrofit
- [Akış Verisi](pinch/stream_data.md) — Akış verisi çıkarma, ExergyLab entegrasyonu
- [Utility Sistemleri](pinch/utility_systems.md) — Çoklu utility, CHP, ısı pompası yerleştirme

### Diğer İlgili Dosyalar
- [Atık Isı Geri Kazanım Teknolojileri](waste_heat_recovery.md) — WHR teknoloji detayları
- [Kojenerasyon Sistemleri](cogeneration.md) — CHP/CCHP entegrasyonu
- [Proses Entegrasyonu](process_integration.md) — Pinch analizi ve proses düzeyinde entegrasyon
- [Ekipmanlar Arası Optimizasyon](cross_equipment.md) — Çapraz ekipman entegrasyon fırsatları
- [Ekonomik Analiz](economic_analysis.md) — Yatırım analizi metodları
- [Kazan Çözümleri](../boiler/solutions/) — Kazan tarafı ısı geri kazanım
- [Kompresör Benchmarkları](../compressor/benchmarks.md) — Kompresör atık ısı verileri
- [Chiller Çözümleri](../chiller/solutions/) — Chiller tarafı ısı geri kazanım
- [Kurutma Formülleri](../dryer/formulas.md) — Kurutma exergy hesaplamaları
- [Kurutma Egzoz Isı Geri Kazanımı](../dryer/solutions/exhaust_heat_recovery.md) — Kurutma WHR
- [Kurutma Hava Geri Deviri](../dryer/solutions/air_recirculation.md) — Hava geri devir optimizasyonu
- [Kurutma Benchmarkları](../dryer/benchmarks.md) — Kurutma performans referansları
- [Isı Eşanjörü Bilgi Tabanı](../heat_exchanger/INDEX.md) — Eşanjör tipleri, formüller, benchmarklar
- [Fouling Yönetimi](../heat_exchanger/solutions/fouling_management.md) — Kirlenme tespiti ve çözümleri
- [Exergy Temelleri](exergy_fundamentals.md) — Exergy analizi temelleri
- [KPI Tanımları](kpi_definitions.md) — Performans göstergeleri

## Referanslar

- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1982
- Kemp, I.C., "Pinch Analysis and Process Integration," Butterworth-Heinemann, 2nd Edition, 2007
- Klemeš, J.J. (Ed.), "Handbook of Process Integration (PI)," Woodhead Publishing, 2013
- Linnhoff March, "Introduction to Pinch Technology," 1998
- US DOE, "Waste Heat Recovery: Technology and Opportunities in U.S. Industry," 2008
- IEA, "Industrial Heat Pumps — Technology and Applications," 2014
- Dincer, I. & Rosen, M.A., "Thermal Energy Storage: Systems and Applications," Wiley, 2nd Edition, 2011
- Thumann, A. & Mehta, D.P., "Handbook of Energy Engineering," 7th Edition, Fairmont Press, 2013
- European Commission, "Reference Document on Best Available Techniques for Energy Efficiency," 2009
