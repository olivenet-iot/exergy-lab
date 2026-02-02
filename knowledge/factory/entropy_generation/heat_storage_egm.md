---
title: "Isı Depolama Optimizasyonu — EGM (Thermal Energy Storage Optimization via EGM)"
category: factory
equipment_type: factory
keywords: [ısı depolama, termal depolama, sensible heat, latent heat, PCM, tank optimizasyonu, izolasyon]
related_files: [factory/entropy_generation/fundamentals.md, factory/entropy_generation/heat_transfer_egm.md, chiller/solutions/thermal_storage.md]
use_when: ["Isı depolama sistemi optimizasyonu yapılacakken", "PCM seçimi ve EGM analizi gerektiğinde", "Tank boyutlandırma kararı verilecekken"]
priority: medium
last_updated: 2026-02-01
---

# Isı Depolama Optimizasyonu — EGM (Thermal Energy Storage Optimization via EGM)

> Son güncelleme: 2026-02-01

## Genel Bakış

Termal enerji depolama (Thermal Energy Storage — TES), endüstriyel sistemlerde enerji arz-talep uyumsuzluğunu gidermek, pik yük yonetimi yapmak ve atık ısıyı değerlendirmek icin kullanılan temel stratejilerden biridir. Ancak her depolama süreci — şarj, bekleme, deşarj — kaçınılmaz olarak entropi üretir ve exergy yıkımına neden olur. Bu dosya, Entropi Üretim Minimizasyonu (EGM) perspektifinden termal depolama sistemlerinin analiz ve optimizasyonunu kapsamlı biçimde ele alır.

**Temel mesaj:** Isı depolamak bedava değildir — her adımda termodinamik kalite kaybedilir. EGM, bu kalite kaybını minimize eden tasarım kararlarını verir: depolama sıcaklığı, tank boyutu, PCM secimi, izolasyon kalınlığı.

---

## 1. Isı Depolamada Entropi Üretimi — Genel Çerçeve

### 1.1 Neden Isı Depolama Entropi Üretir?

**Fiziksel Sezgi:** Isı depolamanın her aşaması bir sıcaklık farkı (ΔT) içerir. Kaynaktan depolama ortamına ısı aktarırken kaynak daha sıcaktır; depolama ortamından talep noktasına ısı verirken depolama daha sıcaktır. Bu sıcaklık farkları, sonlu ΔT üzerinden ısı transferi tersinmezliğinin doğrudan kaynağıdır. Buna ek olarak, bekleme süresi boyunca çevreye kaybedilen ısı da entropi üretir. Bir anlamda, ısı depolama süreci enerjiyi "termodinamik vergiye" tabi tutar — ve bu vergi entropi üretimidir.

Isı depolama sürecindeki üç temel entropi üretim kaynağı:

**1. Şarj Aşaması (Charging):** Kaynak sıcaklığı T_kaynak'tan depolama ortamına (T_depolama < T_kaynak) ısı transfer edilir. Bu sonlu ΔT, entropi üretir.

**2. Bekleme/Depolama Aşaması (Storage Period):** Depolama ortamı çevre sıcaklığından (T₀) daha sıcak veya soğuktur. Izolasyona rağmen çevreye ısı kaybı (veya soğuk depolamada çevreden ısı kazanımı) olur. Bu kayıp entropi üretir.

**3. Deşarj Aşaması (Discharging):** Depolama ortamından (T_depolama) talep sıcaklığına (T_talep < T_depolama) ısı transfer edilir. Yine sonlu ΔT, entropi üretir.

```
Toplam Entropi Üretimi — Isı Depolama Çevrimi:

  S_gen,toplam = S_gen,şarj + S_gen,bekleme + S_gen,deşarj

Burada:
  S_gen,şarj    = şarj sırasında sonlu ΔT'den kaynaklanan entropi üretimi [kJ/K]
  S_gen,bekleme = bekleme süresinde ısı kaybından kaynaklanan entropi üretimi [kJ/K]
  S_gen,deşarj  = deşarj sırasında sonlu ΔT'den kaynaklanan entropi üretimi [kJ/K]

Exergy yıkımı (Gouy-Stodola):
  İ_toplam = T₀ × S_gen,toplam  [kJ]

Burada:
  T₀ = referans ortam sıcaklığı [K]
```

Bu üç terimin göreli büyüklüğü, depolama süresine ve izolasyon kalitesine bağlı olarak değişir:

| Depolama Süresi | S_gen,şarj Payı | S_gen,bekleme Payı | S_gen,deşarj Payı |
|---|---|---|---|
| Kısa süreli (<4 saat) | %35-45 | %5-15 | %35-45 |
| Günlük (8-16 saat) | %25-35 | %15-30 | %25-35 |
| Haftalık (>48 saat) | %15-25 | %40-60 | %15-25 |
| Mevsimsel (>3 ay) | %5-10 | %70-85 | %5-10 |

> **Mühendislik Çıkarımı:** Kısa süreli depolamada şarj/deşarj ΔT'sini azaltmak önceliklidir; uzun süreli depolamada izolasyon iyileştirmesi çok daha kritiktir.

### 1.2 Depolama Türleri

Termal enerji depolama üç temel mekanizmaya dayanır:

**1. Duyulur Isı Depolama (Sensible Heat Storage):**
Depolama ortamının sıcaklığını değiştirerek enerji depolama. Ortam faz değiştirmez.
- Örnekler: Su tankları, kaya yatakları (rock beds), kum tankları, beton bloklar
- Enerji yoğunluğu: Düşük-orta (20-80 kWh/m³)
- Avantaj: Basit, ucuz, kanıtlanmış teknoloji
- Entropi perspektifi: Sıcaklık sürekli değişir → değişken ΔT → entropi hesabı logaritmik

**2. Gizli Isı Depolama (Latent Heat Storage):**
Faz değişim malzemelerinin (Phase Change Materials — PCM) katı-sıvı geçişindeki latent ısıyı kullanma.
- Örnekler: Buz, parafin, tuz hidratlar, erythritol
- Enerji yoğunluğu: Yüksek (50-200 kWh/m³)
- Avantaj: Sabit sıcaklıkta yüksek yoğunluklu depolama
- Entropi perspektifi: Sabit sıcaklık → sabit ΔT → entropi hesabı basitleşir

**3. Termokimyasal Depolama (Thermochemical Storage):**
Tersinir kimyasal reaksiyonlar aracılığıyla enerji depolama.
- Örnekler: Metal hidritler, amonyak ayrışması, kalsiyum oksit/hidroksit
- Enerji yoğunluğu: Çok yüksek (100-500 kWh/m³)
- Bu dosyanın kapsamı dışında; ileri bir konu olarak not edilmiştir

---

## 2. Sensible Heat Storage — EGM Analizi

### 2.1 Entropi Üretimi Formülasyonu

**Fiziksel Sezgi:** Bir su tankını sabit sıcaklıktaki bir kaynakla (örneğin buhar, sıcak yağ) ısıttığımızı düşünelim. Tank sıcaklığı T_i'den T_f'ye yükselir. Tank sıcaklığı arttıkça kaynak ile tank arasındaki sıcaklık farkı azalır — dolayısıyla ısı transferi başına entropi üretimi de azalır. Ancak toplam entropi üretimi, tüm süreç boyunca (T_i → T_f) entegre edilmelidir. Logaritmik terim, sıcaklık değişimi boyunca entropinin kümülatif birikimini temsil eder.

```
Sensible Heat Storage — Şarj Entropi Üretimi:

  Problem: m kg su, T_i'den T_f'ye sabit sıcaklıktaki kaynak (T_kaynak) ile ısıtılıyor.

  Adım 1 — Depolama ortamının entropi kazanımı:
    Depolama ortamı ısı alarak entropisini artırır. Sıcaklık sürekli değiştiği
    için entropi değişimi logaritmik bir ifadedir:

    ΔS_depolama = m × c_p × ln(T_f / T_i)

  Adım 2 — Kaynağın entropi kaybı:
    Kaynak sabit sıcaklıkta (T_kaynak) ısı verir. Kaynağın kaybettiği
    ısı miktarı Q = m × c_p × (T_f - T_i) olup, bu ısı T_kaynak sıcaklığında
    verildiğinden entropi kaybı:

    ΔS_kaynak = -Q / T_kaynak = -m × c_p × (T_f - T_i) / T_kaynak

  Adım 3 — Toplam entropi üretimi:
    S_gen = ΔS_depolama + ΔS_kaynak
    S_gen = m × c_p × [ln(T_f / T_i) - (T_f - T_i) / T_kaynak]

Burada:
  m         = depolama ortamı kütlesi [kg]
  c_p       = özgül ısı kapasitesi [kJ/(kg·K)]
  T_i       = başlangıç sıcaklığı [K]
  T_f       = son sıcaklık [K]
  T_kaynak  = kaynak sıcaklığı (sabit) [K]
  S_gen     = toplam entropi üretimi [kJ/K]

Birim kontrolü:
  [kg] × [kJ/(kg·K)] × [-] = [kJ/K]  ✓

Matematiksel Not:
  ln(T_f/T_i) her zaman < (T_f - T_i)/T_i  (Jensen eşitsizliği)
  T_kaynak > T_f > T_i olduğundan (T_f - T_i)/T_kaynak < (T_f - T_i)/T_i
  Dolayısıyla S_gen > 0 her zaman sağlanır ✓
```

**Sayısal Örnek — Sıcak Su Tankı Şarjı:**

```
Veri:
  m = 5,000 kg (5 m³ su tankı)
  c_p = 4.18 kJ/(kg·K)
  T_i = 30°C = 303.15 K (başlangıç — ortam sıcaklığına yakın)
  T_f = 80°C = 353.15 K (hedef depolama sıcaklığı)
  T_kaynak = 120°C = 393.15 K (buhar veya sıcak yağ)
  T₀ = 25°C = 298.15 K

Adım 1 — Depolanan enerji:
  Q = m × c_p × (T_f - T_i)
    = 5,000 × 4.18 × (80 - 30)
    = 1,045,000 kJ = 1,045 MJ ≈ 290 kWh

Adım 2 — Entropi üretimi:
  ΔS_depolama = 5,000 × 4.18 × ln(353.15 / 303.15)
              = 20,900 × ln(1.1649)
              = 20,900 × 0.15270
              = 3,191.4 kJ/K

  ΔS_kaynak = -5,000 × 4.18 × (353.15 - 303.15) / 393.15
            = -20,900 × 50 / 393.15
            = -1,045,000 / 393.15
            = -2,658.3 kJ/K

  S_gen = 3,191.4 + (-2,658.3) = 533.1 kJ/K

Adım 3 — Exergy yıkımı:
  İ = T₀ × S_gen = 298.15 × 533.1 = 158,904 kJ ≈ 159 MJ ≈ 44.1 kWh

Adım 4 — Exergy verimi:
  Depolanan enerjinin exergisi:
  Ex_depolanan = m × c_p × [(T_f - T_i) - T₀ × ln(T_f / T_i)]
               = 5,000 × 4.18 × [50 - 298.15 × 0.15270]
               = 20,900 × [50 - 45.51]
               = 20,900 × 4.49
               = 93,841 kJ ≈ 26.1 kWh

  Kaynaktan alınan exergy:
  Ex_kaynak = Q × (1 - T₀/T_kaynak)
            = 1,045,000 × (1 - 298.15/393.15)
            = 1,045,000 × 0.2416
            = 252,472 kJ ≈ 70.1 kWh

  η_ex,şarj = Ex_depolanan / Ex_kaynak = 93,841 / 252,472 = 0.372 = %37.2

Yorum:
  290 kWh enerji depolamak için kaynak 70.1 kWh exergy sağladı.
  Bunun yalnızca 26.1 kWh'ı depolama ortamında kaldı (%37.2).
  44.1 kWh exergy (entropi üretimi nedeniyle) kalıcı olarak yok edildi.
  Kaynak-depolama arasındaki 40°C sıcaklık farkı bu kaybın ana nedenidir.
```

### 2.2 Stratifiye Tank vs Karışık Tank (Stratified vs Fully Mixed)

**Fiziksel Sezgi:** Bir su tankında sıcak su üstte, soğuk su altta doğal olarak katmanlaşır (stratification) — çünkü sıcak suyun yoğunluğu düşüktür. Bu katmanlaşma, deşarj sırasında büyük termodinamik avantaj sağlar: tankın üst katmanından alınan su, depolama sıcaklığına yakındır ve talep noktasına yüksek sıcaklıkta ulaşır. Karışık tankta ise tüm su ortalama sıcaklıktadır — deşarj ilerledikçe su sıcaklığı düşer ve talep sıcaklığının altına inebilir.

```
Stratifiye Tank — Entropi Avantajı:

  Karışık tank (Fully mixed):
    Deşarj boyunca tank sıcaklığı: T_karışık = (m_sıcak × T_sıcak + m_soğuk × T_soğuk) / m_toplam
    ΔT_deşarj(t) değişken → entropi üretimi daha yüksek

  Stratifiye tank:
    Deşarj boyunca çıkış sıcaklığı: T_çıkış ≈ T_sıcak (termoklin bozulana kadar sabit)
    Sabit ve yüksek T_çıkış → daha düşük ΔT → daha düşük S_gen

  Entropi karşılaştırması (tipik):
    S_gen,karışık / S_gen,stratifiye = 1.15 - 1.30

  Yani stratifiye tank, karışık tanka göre %15-30 daha az entropi üretir.
```

**Stratifikasyon İçin Tasarım Önerileri:**

| Parametre | Önerilen Değer | Açıklama |
|---|---|---|
| Tank yükseklik/çap oranı (H/D) | ≥ 2.5 (ideal: 3.0-4.0) | Uzun tank daha iyi katmanlaşma sağlar |
| Giriş/çıkış difüzör hızı | < 0.15 m/s | Düşük hız türbülansı önler |
| Froude sayısı (Fr) | < 1.0 (ideal: < 0.5) | Termoklin stabilitesini sağlar |
| Termoklin kalınlığı hedefi | < tank yüksekliğinin %10'u | İnce termoklin = yüksek exergy verimi |
| İç baffle/engel | Uygulanabilir ise | Dikey karışmayı azaltır |

**Froude Sayısı Hesabı:**

**Fiziksel Sezgi:** Froude sayısı, giriş akışının momentumunun (karışma eğilimi) ile yerçekimi kaynaklı yoğunluk farkının (katmanlaşma eğilimi) oranını ölçer. Düşük Froude sayısı, yerçekimi kuvvetlerinin baskın olduğunu ve sıcaklık katmanlarının korunacağını gösterir.

```
Fr = v / √(g × d × Δρ/ρ)

Burada:
  v  = difüzör çıkış hızı [m/s]
  g  = yerçekimi ivmesi = 9.81 [m/s²]
  d  = difüzör çapı [m]
  Δρ = sıcak ve soğuk su arasındaki yoğunluk farkı [kg/m³]
  ρ  = ortalama yoğunluk [kg/m³]

Hedef: Fr < 1.0, tercihen Fr < 0.5
```

### 2.3 Tank Boyutu Optimizasyonu — EGM Perspektifi

**Fiziksel Sezgi:** Büyük tank daha fazla termal kütle barındırır — şarj/deşarj sırasında sıcaklık daha az değişir (daha düşük ΔT), dolayısıyla çevrimsel (cyclic) entropi üretimi azalır. Ancak büyük tankın yüzey alanı fazladır; bekleme süresinde çevreye ısı kaybı artar. Ayrıca büyük tank, daha yüksek yatırım maliyeti ve daha fazla yer gerektirir. EGM, bu trade-off'un minimum entropi üretimi noktasını bulur.

```
Tank Boyutu — Entropi Trade-off:

  S_gen,çevrim(V) = S_gen,şarj(V) + S_gen,bekleme(V) + S_gen,deşarj(V)

  V arttıkça:
    S_gen,şarj   ↓  (ΔT_şarj azalır çünkü termal kütle artar)
    S_gen,bekleme ↑  (yüzey alanı ∝ V^(2/3) artar → ısı kaybı artar)
    S_gen,deşarj  ↓  (ΔT_deşarj azalır)

  Optimum:
    dS_gen,çevrim / dV = 0  →  V_opt

  Basitleştirilmiş yaklaşım (küresel tank varsayımı):
    S_gen,çevrim ≈ α/V + β × V^(2/3) × t_bekleme

  Burada:
    α = şarj/deşarj entropi katsayısı (sabit yüke bağlı)
    β = izolasyon ve ortam koşullarına bağlı katsayı
    t_bekleme = bekleme süresi [s]
    V = tank hacmi [m³]

  Türev alındığında:
    dS_gen/dV = -α/V² + (2/3) × β × V^(-1/3) × t_bekleme = 0

  Bu denklem analitik veya numerik olarak çözülerek V_opt bulunur.
```

**Pratik Boyutlandırma Rehberi:**

| Uygulama | Depolama Süresi | Önerilen V/Q Oranı | Not |
|---|---|---|---|
| Proses ısı tamponlama | 1-4 saat | 0.5-1.5 m³/MWh | Hızlı çevrim, izolasyon ikincil |
| Günlük pik kaydırma | 8-16 saat | 1.5-3.0 m³/MWh | Stratifikasyon kritik |
| Hafta sonu depolama | 48-72 saat | 3.0-5.0 m³/MWh | İzolasyon kalınlığı artırılmalı |
| Mevsimsel depolama | >3 ay | Büyük yer altı tankları | Zemin izolasyonu baskın |

---

## 3. Latent Heat Storage — EGM Analizi

### 3.1 PCM Entropi Üretimi

**Fiziksel Sezgi:** Faz değişim malzemesi (PCM), erime sıcaklığı T_pcm'de sabit sıcaklıkta büyük miktarda enerji (latent ısı, h_fg) depolar. Kaynak T_kaynak sıcaklığında ısı verirken, PCM T_pcm'de bu ısıyı alır. Her iki taraf da sabit sıcaklıkta olduğu için entropi hesabı önemli ölçüde basitleşir. Entropi üretimi, yalnızca bu iki sıcaklık arasındaki farktan kaynaklanır — fark ne kadar küçükse, entropi üretimi o kadar azdır.

```
PCM Şarj Entropi Üretimi:

  Fiziksel süreç: Kaynak (T_kaynak) → PCM (T_pcm), faz değişimi sırasında

  Aktarılan ısı:
    Q = m × h_fg  [kJ]

  Entropi üretimi:
    S_gen,şarj = Q × (1/T_pcm - 1/T_kaynak)
               = m × h_fg × (1/T_pcm - 1/T_kaynak)

  Burada:
    m        = PCM kütlesi [kg]
    h_fg     = özgül latent ısı (erime/donma entalpisi) [kJ/kg]
    T_pcm    = PCM erime/donma sıcaklığı [K]
    T_kaynak = ısı kaynağı sıcaklığı [K]

  S_gen > 0 olması için T_kaynak > T_pcm gereklidir ✓

  Benzer şekilde deşarj:
    S_gen,deşarj = m × h_fg × (1/T_talep - 1/T_pcm)

  Burada:
    T_talep = ısı talebi sıcaklığı [K], T_talep < T_pcm

  Toplam çevrim entropi üretimi:
    S_gen,toplam = m × h_fg × (1/T_talep - 1/T_kaynak)

  Dikkat: Toplam entropi üretimi, PCM sıcaklığından BAĞIMSIZ gibi görünür!
  Ancak bu sadece şarj+deşarj toplamıdır. Bekleme süresindeki ısı kaybı
  ve sensible heat bileşeni (faz değişimi öncesi/sonrası ΔT) PCM
  sıcaklığına bağlıdır. Bu nedenle T_pcm optimizasyonu hala önemlidir.
```

### 3.2 Optimum PCM Sıcaklığı

**Fiziksel Sezgi:** Şarj sırasında kaynak ile PCM arasındaki ΔT entropi üretir; deşarj sırasında PCM ile talep arasındaki ΔT entropi üretir. PCM sıcaklığını yükseltirsen şarj entropisi azalır ama deşarj entropisi artar — ve tam tersi. Bu iki karşıt etkinin dengelenmesi, toplam entropi üretiminin minimumu olan **optimum PCM sıcaklığını** verir. Matematiksel olarak bu optimum, kaynak ve talep sıcaklıklarının **geometrik ortalamasıdır** — termodinamiğin zarif sonuçlarından biri.

```
Optimum PCM Sıcaklığı Türetmesi:

  Toplam entropi üretimi (şarj + deşarj):
    S_gen = m × h_fg × (1/T_pcm - 1/T_kaynak) + m × h_fg × (1/T_talep - 1/T_pcm)

  Sensible heat bileşenini de dahil ettiğimizde (PCM'in duyulur ısı katkısı
  faz değişimine kıyasla küçükse, dominant terim latent ısıdır):

    S_gen ≈ m × h_fg × [(1/T_pcm - 1/T_kaynak) + (1/T_talep - 1/T_pcm)]

  Not: Yukarıdaki toplam T_pcm'den bağımsızdır. Ancak gerçekte:
  - Sensible heat bileşeni T_pcm'ye bağlıdır
  - Bekleme kayıpları T_pcm'ye bağlıdır
  - Isı transfer katsayıları T_pcm'ye bağlıdır

  Daha gerçekçi formülasyon (bekleme kaybı dahil):
    S_gen,toplam = m × h_fg × (1/T_pcm - 1/T_kaynak)
                 + Q_kayıp × (1/T₀ - 1/T_pcm)
                 + m × h_fg × (1/T_talep - 1/T_pcm)

  Optimum koşul: dS_gen,toplam / dT_pcm = 0

  Sadece şarj + deşarj terimi (bekleme ihmal edildiğinde):
    d/dT_pcm [m × h_fg × (1/T_pcm - 1/T_kaynak + 1/T_talep - 1/T_pcm)] = 0

  Sensible heat terimi dahil edildiğinde optimum:

    ┌─────────────────────────────────────────────┐
    │                                             │
    │   T_pcm,opt = √(T_kaynak × T_talep)        │
    │                                             │
    │   Geometrik Ortalama!                       │
    │                                             │
    └─────────────────────────────────────────────┘

  Bu sonuç, T_pcm,opt'un kaynak ve talep sıcaklıklarının geometrik
  ortalaması olduğunu gösterir. Geometrik ortalama, entropi üretimini
  şarj ve deşarj arasında EŞİT DAĞITIR — termodinamik denge noktası.
```

**Sayısal Örnek — Optimum PCM Sıcaklığı:**

```
Veri:
  T_kaynak = 90°C = 363.15 K (atık sıcak su veya buhar kondensatı)
  T_talep  = 40°C = 313.15 K (bina ısıtma veya sıcak kullanma suyu)

Hesap:
  T_pcm,opt = √(363.15 × 313.15)
            = √(113,709)
            = 337.2 K
            = 64.1°C

Yorum:
  Optimal PCM erime sıcaklığı ≈ 64°C olmalıdır.

  Entropi dağılımı kontrolü:
    ΔT_şarj  = T_kaynak - T_pcm,opt = 90 - 64 = 26°C
    ΔT_deşarj = T_pcm,opt - T_talep = 64 - 40 = 24°C

  Sıcaklık farkları yaklaşık eşittir — geometrik ortalamanın
  özelliği budur: entropi üretimini iki tarafa dengeli dağıtır.

  Karşılaştırma — Yanlış PCM seçimi (T_pcm = 80°C):
    ΔT_şarj  = 90 - 80 = 10°C  (düşük entropi)
    ΔT_deşarj = 80 - 40 = 40°C  (yüksek entropi!)
    Toplam entropi üretimi daha yüksek olur.
```

### 3.3 PCM Seçimi Kriterleri — Entropi Perspektifinden

**Fiziksel Sezgi:** EGM perspektifinden PCM seçiminde dört kriter öne çıkar: (1) Erime sıcaklığı T_opt'a yakın olmalı — bu, şarj/deşarj entropi üretimini minimize eder. (2) Yüksek latent ısı (h_fg) — aynı enerji daha az kütle ile depolanır, sensible heat geçiş fazındaki ΔT-kaynaklı entropi azalır. (3) Yüksek termal iletkenlik (k) — ısı transferi daha düşük ΔT ile gerçekleşir, dolayısıyla daha az entropi üretilir. (4) Düşük aşırı soğuma (supercooling) eğilimi — aşırı soğuma ekstra ΔT yaratır ve ek entropi üretir.

**Endüstriyel PCM Tablosu — EGM-İlgili Özellikler:**

| PCM Malzeme | T_erime (°C) | h_fg (kJ/kg) | k (W/(m·K)) | ρ (kg/m³) | En Uygun Uygulama | EGM Notu |
|---|---|---|---|---|---|---|
| Buz (Ice) | 0 | 334 | 2.2 | 917 | Soğutma depolama | Yüksek k → düşük ΔT → düşük S_gen |
| Na₂SO₄·10H₂O (Glauber tuzu) | 32 | 252 | 0.5 | 1,485 | Bina ısıtma/soğutma | Ucuz, bol; aşırı soğuma sorunu |
| Parafin RT42 | 42 | 165 | 0.2 | 820 | Düşük sıcaklık depolama | Düşük k → yüksek ΔT → yüksek S_gen |
| Parafin RT60 | 60 | 160 | 0.2 | 780 | Sıcak su ön ısıtma | T_opt yakınında iyi performans |
| Erythritol | 118 | 340 | 0.7 | 1,480 | Buhar sistemi, orta sıcaklık | Yüksek h_fg + iyi k → EGM avantajı |
| D-Mannitol | 167 | 294 | 0.2 | 1,520 | Endüstriyel proses ısı | Yüksek T_erime, düşük k dezavantaj |
| KNO₃/NaNO₃ ötektiği | 222 | 100 | 0.5 | 1,950 | Yoğunlaştırılmış güneş enerjisi | Yüksek sıcaklık uygulamaları |

**PCM Termal İletkenlik İyileştirme — EGM Etkisi:**

PCM'lerin çoğu düşük termal iletkenliğe (k < 0.5 W/(m·K)) sahiptir. Bu durum, şarj/deşarj sırasında PCM içinde büyük sıcaklık gradyanlarına neden olur ve ek entropi üretir. İyileştirme yöntemleri:

| Yöntem | k Artışı | S_gen Azalması | Maliyet |
|---|---|---|---|
| Grafit köpük ekleme | 5-30× | %25-50 | Orta |
| Metal kanatçıklar (fins) | 3-10× | %15-35 | Düşük-Orta |
| Karbon nanotüp katkı | 2-5× | %10-20 | Yüksek |
| Metal köpük matris | 10-50× | %30-55 | Yüksek |
| Nano-partikül katkı | 1.5-3× | %5-15 | Orta |

---

## 4. İzolasyon Optimizasyonu — EGM

### 4.1 Isı Kaybı Kaynaklı Entropi Üretimi

**Fiziksel Sezgi:** Depolama ortamı çevreden farklı sıcaklıkta olduğu sürece, izolasyona rağmen bir miktar ısı kaybı (veya kazanımı) olur. Bu ısı, depolama ortamından (yüksek sıcaklık) çevreye (düşük sıcaklık) akar — tipik bir sonlu ΔT ısı transferi tersinmezliği. Uzun süreli depolamada bu terim, toplam entropi üretiminin baskın bileşeni haline gelir.

```
Bekleme Süresinde Isı Kaybı Entropi Üretimi:

  Isı kaybı hızı:
    Q̇_kayıp = U × A × (T_depolama - T₀)  [kW]

  Burada:
    U = toplam ısı geçiş katsayısı (izolasyon dahil) [kW/(m²·K)]
    A = tank dış yüzey alanı [m²]
    T_depolama = depolama ortamı sıcaklığı [K]
    T₀ = çevre sıcaklığı [K]

  Entropi üretim hızı:
    Ṡ_gen,kayıp = Q̇_kayıp × (1/T₀ - 1/T_depolama)  [kW/K]

  Bu formülün türetmesi:
    Çevre T₀'da Q̇_kayıp kadar ısı alır → entropi artışı = Q̇_kayıp / T₀
    Depolama T_depolama'da Q̇_kayıp kadar ısı verir → entropi azalması = Q̇_kayıp / T_depolama
    Ṡ_gen = Q̇_kayıp / T₀ - Q̇_kayıp / T_depolama = Q̇_kayıp × (1/T₀ - 1/T_depolama)

  Toplam bekleme entropi üretimi (t_bekleme süresi boyunca):
    S_gen,bekleme = ∫₀^t Ṡ_gen,kayıp dt

  Sabit sıcaklık varsayımıyla (büyük tank, kısa süre):
    S_gen,bekleme ≈ Q̇_kayıp × (1/T₀ - 1/T_depolama) × t_bekleme  [kJ/K]

  Exergy yıkımı:
    İ_bekleme = T₀ × S_gen,bekleme  [kJ]
```

**Sayısal Örnek:**

```
Veri:
  Tank: 10 m³ silindirik, D = 2.0 m, H = 3.2 m
  A = π × D × H + 2 × π × (D/2)² ≈ 20.1 + 6.3 = 26.4 m²
  İzolasyon: 80 mm taş yünü, k_iz = 0.04 W/(m·K)
  U ≈ k_iz / L_iz = 0.04 / 0.08 = 0.5 W/(m²·K) = 0.0005 kW/(m²·K)
  T_depolama = 80°C = 353.15 K
  T₀ = 25°C = 298.15 K
  t_bekleme = 16 saat = 57,600 s

Hesap:
  Q̇_kayıp = 0.0005 × 26.4 × (353.15 - 298.15)
           = 0.0132 × 55 = 0.726 kW

  Ṡ_gen,kayıp = 0.726 × (1/298.15 - 1/353.15)
              = 0.726 × (0.003354 - 0.002832)
              = 0.726 × 0.000522
              = 0.000379 kW/K

  S_gen,bekleme = 0.000379 × 57,600 = 21.8 kJ/K

  İ_bekleme = 298.15 × 21.8 = 6,500 kJ ≈ 1.8 kWh

  16 saatlik bekleme süresinde kaybedilen enerji:
  Q_kayıp = 0.726 × 16 = 11.6 kWh

  Kaybedilen exergy: 1.8 kWh
  (Kaybedilen enerjinin %15.5'i exergy olarak yok edilmiştir)
```

### 4.2 Optimum İzolasyon Kalınlığı

**Fiziksel Sezgi:** İzolasyonu kalınlaştırmak ısı kaybını ve dolayısıyla bekleme entropi üretimini azaltır. Ancak izolasyon malzemesinin kendisi de bir enerji ve maliyet gerektirir — hem üretim sürecindeki gömülü enerji (embodied energy) hem de satın alma maliyeti. EGM optimumu, izolasyon kalınlığı artırıldığında azalan ısı kaybı entropisi ile artan maliyet/gömülü enerji arasındaki dengeyi bulur. EGM optimumu, ekonomik optimumdan genellikle %10-20 daha kalın izolasyon önerir — çünkü EGM, exergy değerini ekonomik analizden daha yüksek fiyatlandırır.

```
İzolasyon Kalınlığı Optimizasyonu:

  Isı kaybından entropi üretimi (kalınlık L'nin fonksiyonu olarak):
    Ṡ_gen,kayıp(L) = [k_iz × A × (T_dep - T₀) / L] × (1/T₀ - 1/T_dep)

  L arttıkça:
    Ṡ_gen,kayıp ↓ (ısı kaybı azalır)
    Ama: İzolasyon maliyeti ∝ L × A
         Gömülü enerji ∝ L × A

  Ekonomik optimum:
    d/dL [C_enerji × Q̇_kayıp(L) × t_çalışma + C_iz × L × A] = 0

  EGM optimum:
    d/dL [T₀ × Ṡ_gen,kayıp(L) × t_çalışma] = 0
    (Maliyet kısıtı Lagrange çarpanı ile dahil edilir)
```

### 4.3 Endüstriyel İzolasyon Standartları — EGM Perspektifi

| Depolama Sıcaklığı | Ekonomik Optimum İzolasyon | EGM Optimum İzolasyon | Malzeme Önerisi |
|---|---|---|---|
| 0-10°C (soğuk depolama) | 40-60 mm | 50-80 mm | Kapalı hücre köpük, XPS |
| 10-40°C (düşük sıcaklık) | 30-50 mm | 40-70 mm | EPS, XPS |
| 40-60°C (ılık depolama) | 50-80 mm | 60-100 mm | Taş yünü, cam yünü |
| 60-90°C (sıcak su) | 80-120 mm | 100-150 mm | Taş yünü, kalsiyum silikat |
| 90-150°C (kızgın su / yağ) | 100-150 mm | 120-180 mm | Kalsiyum silikat, seramik elyaf |
| >150°C (endüstriyel proses) | 150-250 mm | 180-300 mm | Seramik elyaf, perlit |

> **Önemli:** Soğuk depolama sistemlerinde buğulanma önleyici buhar bariyeri (vapor barrier) izolasyonun DIŞINDA olmalıdır. Aksi takdirde izolasyon nemlenip termal performansını kaybeder — bu da S_gen'i dramatik biçimde artırır.

---

## 5. Soğuk Depolama (Ice/Chilled Water Storage) — EGM

### 5.1 Buz Depolama (Ice Storage)

**Fiziksel Sezgi:** Buz depolama, gece saatlerinde (ucuz elektrik) buz üretip gündüz pik saatlerinde eriterek soğutma sağlar. Ancak buz üretmek için chiller evaporatör sıcaklığı -5°C ile -7°C'ye düşürülmelidir (normal soğuk su üretiminde +5°C ile +7°C). Bu daha düşük evaporatör sıcaklığı, Carnot COP'unu düşürür ve kompresörde daha fazla entropi üretilir. EGM analizi, bu ek entropi üretiminin maliyet tasarrufuyla ne ölçüde dengelendiğini değerlendirir.

```
Buz Depolama — Entropi Analizi:

  Normal soğutma (chilled water, CHW):
    T_evap = 5°C = 278.15 K
    T_kond = 35°C = 308.15 K
    COP_Carnot = T_evap / (T_kond - T_evap) = 278.15 / 30 = 9.27
    COP_gerçek ≈ 0.55 × COP_Carnot = 5.1

  Buz üretimi:
    T_evap = -7°C = 266.15 K
    T_kond = 35°C = 308.15 K
    COP_Carnot = 266.15 / (308.15 - 266.15) = 266.15 / 42 = 6.34
    COP_gerçek ≈ 0.55 × COP_Carnot = 3.5

  COP cezası:
    ΔCOP = 5.1 - 3.5 = 1.6 → %31 düşüş

  Entropi üretim karşılaştırması (1 kWh soğutma için):
    CHW: W_kompresör = 1.0 / 5.1 = 0.196 kWh = 706 kJ
    Buz: W_kompresör = 1.0 / 3.5 = 0.286 kWh = 1,029 kJ

    Ek iş = 1,029 - 706 = 323 kJ
    Ek entropi üretimi ≈ 323 / T₀ = 323 / 298.15 = 1.08 kJ/K

  Bu ek entropi üretimi, tarifeler arası maliyet farkı ile
  ekonomik olarak haklı çıkarılabilir — ancak termodinamik
  açıdan buz depolama her zaman daha fazla entropi üretir.
```

### 5.2 Soğuk Su Depolama (Chilled Water Storage)

**Fiziksel Sezgi:** Stratifiye soğuk su tankı, sıcak ve soğuk katmanları yoğunluk farkıyla ayırır. Chiller normal evaporatör sıcaklığında çalışır (COP cezası yok), ancak depolama yoğunluğu buza göre çok düşüktür (yaklaşık 7-10 kat daha fazla hacim gerekir). EGM açısından soğuk su depolama, buz depolamadan üstündür — çünkü chiller COP cezası yoktur ve stratifikasyon sayesinde deşarj sırasında düşük entropi üretilir.

```
Soğuk Su Stratifiye Tank — S_gen Hesabı:

  Şarj: Chiller 5°C su üretir → tankın alt katmanına gönderilir
    T_evap = 5°C → COP = 5.1 (normal)
    S_gen,şarj ≈ standart chiller entropi üretimi (ek yok)

  Bekleme: Termoklin bozulması + ısı kazanımı
    S_gen,bekleme = Q̇_kazanım × (1/T_soğuk_su - 1/T₀)
    Not: T_soğuk_su < T₀ olduğundan, çevreden ısı AKAR → entropi üretilir

  Deşarj: Soğuk su 5°C'den bina soğutma devresine (12°C dönüş)
    S_gen,deşarj = ṁ_su × c_p × ln(T_dönüş / T_gidiş)
                 - Q̇_soğutma / T_ort_bina

  Stratifiye tankta termoklin kalitesi kritiktir:
    İyi termoklin → T_gidiş ≈ 5°C (sabit) → düşük S_gen
    Kötü termoklin → T_gidiş yükselir → ΔT azalır → S_gen artar
```

### 5.3 Buz vs Soğuk Su Karşılaştırması — EGM Tablosu

| Parametre | Buz Depolama | Soğuk Su Depolama | EGM Yorumu |
|---|---|---|---|
| Depolama yoğunluğu | Yüksek (~50-70 kWh/m³) | Düşük (~7-10 kWh/m³) | Buz: daha az yüzey → daha az bekleme S_gen |
| Chiller COP etkisi | Düşük (COP ≈ 3.0-3.5) | Normal (COP ≈ 5.0-5.5) | CHW: %30 daha az kompresör S_gen |
| S_gen,şarj (kWh soğutma başına) | ~1.08 kJ/K | ~0.66 kJ/K | CHW: %39 daha düşük |
| S_gen,bekleme (16 saat) | Düşük (küçük tank) | Orta (büyük tank) | Buz avantajlı (küçük yüzey) |
| S_gen,deşarj | Düşük (0°C sabit) | Orta (termoklin bağımlı) | Buz: sabit T → öngörülebilir |
| S_gen,toplam (kWh başına) | Daha yüksek | Daha düşük | **CHW termodinamik olarak üstün** |
| Yer gereksinimi | Küçük | Büyük | Buz: 5-7× daha az alan |
| En uygun uygulama | Sınırlı alan, yüksek pik kesme | Büyük tesisler, yeterli alan | Alan kısıtı yoksa CHW tercih edilmeli |

> **EGM Sonucu:** Termodinamik açıdan soğuk su depolama her zaman buz depolamadan daha az entropi üretir. Buz depolama ancak alan kısıtı veya çok yüksek tarife farkı durumunda ekonomik olarak haklı çıkarılabilir.

---

## 6. Endüstriyel Atık Isı Depolama

### 6.1 Atık Isı Kaynakları ve Depolama Stratejisi

**Fiziksel Sezgi:** Endüstriyel atık ısı genellikle kesikli (intermittent) veya sürekli (continuous) olabilir. Kesikli atık ısı — fırın çıkışları, batch prosesler, güneş enerjisi — zaman içinde büyük dalgalanmalar gösterir. Sürekli düşük sıcaklıktaki atık ısı — kompresör soğutma suyu, chiller kondenser ısısı — daha kararlıdır ama exergy değeri düşüktür. EGM, her durum için farklı depolama stratejisi önerir.

```
Atık Isı Depolama — EGM Optimal Sıcaklık:

  Durum 1: Kesikli yüksek sıcaklık atık ısı
    T_atık = 200-400°C (fırın çıkışı, baca gazı)
    T_talep = 60-90°C (proses ısıtma, sıcak su)

    T_depolama,opt = √(T_atık × T_talep)
    Örnek: T_atık = 300°C = 573 K, T_talep = 80°C = 353 K
           T_depolama,opt = √(573 × 353) = 450 K = 177°C
    Uygun depolama: Termal yağ, kızgın su, yüksek sıcaklık PCM

  Durum 2: Sürekli düşük sıcaklık atık ısı
    T_atık = 30-60°C (kompresör, chiller kondenser)
    T_talep = 20-40°C (ön ısıtma, bina ısıtma)

    T_depolama,opt = √(T_atık × T_talep)
    Örnek: T_atık = 50°C = 323 K, T_talep = 30°C = 303 K
           T_depolama,opt = √(323 × 303) = 313 K = 40°C
    Uygun depolama: Su tankı, düşük sıcaklık PCM

  Durum 3: Güneş enerjisi (solar thermal)
    T_atık = 60-200°C (düz plakalı kolektör → vakum tüplü)
    T_talep = 40-60°C (sıcak su, mevsimsel depolama)

    Değişken T_atık nedeniyle EGM optimumu dinamik hesap gerektirir.
    Mevsimsel depolamada izolasyon S_gen baskın terimdir.
```

### 6.2 Kaskad Depolama (Cascaded Storage)

**Fiziksel Sezgi:** Tek bir depolama sıcaklığı yerine, birden fazla kademede depolama yapmak toplam entropi üretimini azaltır. Tıpkı Carnot çevriminin sonsuz kademeye bölünerek tersinir hale getirilmesi gibi, kaskad depolama da sıcaklık atlama boşluklarını küçülterek her adımdaki ΔT'yi — ve dolayısıyla entropi üretimini — düşürür. Bu prensip, Bejan'ın "constructal" tasarım felsefesiyle de uyumludur: akışı (burada ısı akışını) kolaylaştıran tasarım, doğal olarak daha az entropi üretir.

```
Kaskad Depolama — Entropi Avantajı:

  Tek kademeli depolama:
    T_kaynak (yüksek) → T_depolama → T_talep (düşük)
    S_gen,tek = Q × (1/T_talep - 1/T_kaynak)

  İki kademeli kaskad:
    T_kaynak → T_dep,1 → T_dep,2 → T_talep
    S_gen,kaskad = Q × [(1/T_dep,1 - 1/T_kaynak) + (1/T_dep,2 - 1/T_dep,1)
                       + (1/T_talep - 1/T_dep,2)]
                = Q × (1/T_talep - 1/T_kaynak)    ← AYNI toplam!

  Görünüşte toplam aynı — peki avantaj nerede?

  Avantaj şu durumlarda ortaya çıkar:
    1. Farklı talep noktaları farklı sıcaklıklarda ise:
       T_dep,1 → yüksek sıcaklık talebi, T_dep,2 → düşük sıcaklık talebi
       Her talep, kendi sıcaklığına en yakın depolamadan beslenir → düşük ΔT

    2. Bekleme kayıpları azalır:
       Yüksek sıcaklık deposu daha küçük → daha az yüzey → daha az kayıp
       Düşük sıcaklık deposu düşük ΔT → daha az kayıp

    3. PCM kaskadında:
       Her PCM kendi optimum sıcaklığında çalışır
       Toplam exergy verimi %10-25 artar

  Pratik kaskad örneği (3 kademe):
    Kademe 1: PCM @ 100°C (endüstriyel proses ısıtma)
    Kademe 2: PCM @ 60°C  (sıcak kullanma suyu)
    Kademe 3: Su tank @ 35°C (bina ön ısıtma)
```

**Kaskad Depolama Karşılaştırması:**

| Parametre | Tek Kademe | 2-Kademe Kaskad | 3-Kademe Kaskad |
|---|---|---|---|
| Exergy verimi | %30-40 | %40-55 | %50-65 |
| Entropi üretimi (göreceli) | 1.00 | 0.70-0.85 | 0.55-0.70 |
| Sistem karmaşıklığı | Düşük | Orta | Yüksek |
| Yatırım maliyeti (göreceli) | 1.00 | 1.3-1.6 | 1.6-2.2 |
| En uygun durum | Tek talep sıcaklığı | 2 farklı talep | 3+ farklı talep |

---

## 7. Pratik Mühendislik Kuralları

EGM tabanlı termal depolama tasarımında hızlı karar vermeye yardımcı olan temel kurallar:

### 7.1 Depolama Sıcaklığı Kuralları

```
Kural 1: Optimal depolama sıcaklığı = kaynak ve talep sıcaklıklarının
         geometrik ortalaması.

         T_depolama,opt = √(T_kaynak × T_talep)    [K cinsinden!]

         Bu kural, hem sensible hem latent depolama için geçerlidir.

Kural 2: PCM seçiminde erime sıcaklığı, T_opt değerinin ±5-10°C
         aralığında olmalıdır. Bu aralık dışına çıkıldığında entropi
         üretimi hızla artar.

         |T_pcm - T_opt| < 10°C  →  EGM performansı kabul edilebilir
         |T_pcm - T_opt| < 5°C   →  EGM performansı iyi
```

### 7.2 Stratifikasyon Kuralları

```
Kural 3: Stratifiye tanklar, karışık tanklara göre %15-30 daha az
         entropi üretir. Su depolamada HER ZAMAN stratifikasyonu
         hedefleyin.

Kural 4: Tank yükseklik/çap oranı (H/D) ≥ 2.5 olmalıdır.
         H/D = 3.0-4.0 aralığı optimal stratifikasyon sağlar.
         H/D < 2.0 durumunda stratifikasyon bozulma riski yüksektir.

Kural 5: Difüzör hızı 0.15 m/s'yi geçmemelidir. Yüksek hız
         türbülans yaratır ve termoklini bozar → S_gen artar.
```

### 7.3 Buz ve Soğuk Su Depolama Kuralları

```
Kural 6: Buz depolamada chiller COP cezası %20-30 arasındadır.
         Bu ceza, gece/gündüz tarife farkı ile kısmen telafi edilir,
         ancak termodinamik olarak soğuk su depolama her zaman
         daha az entropi üretir.

Kural 7: Soğuk su depolamasında termoklin kalitesi exergy veriminin
         %70'ini belirler. Froude sayısı (Fr) < 1.0 olmalıdır;
         ideal tasarımda Fr < 0.5 hedeflenmelidir.
```

### 7.4 İzolasyon Kuralları

```
Kural 8: Sıcak depolama (>60°C) için minimum 100 mm izolasyon
         gereklidir. EGM optimumu genellikle 120-180 mm arasındadır.

Kural 9: Soğuk depolama (<10°C) için minimum 50 mm izolasyon
         ve buhar bariyeri zorunludur.

Kural 10: Depolama süresi >24 saat ise, izolasyon entropi üretimi
          baskın terim haline gelir. Bu durumda izolasyon kalınlığını
          %50 artırmak ekonomik olarak haklıdır.
```

### 7.5 Hızlı Karşılaştırma Tablosu

| Depolama Tipi | Tipik Exergy Verimi | S_gen (kWh soğutma/ısıtma başına) | En İyi Uygulama |
|---|---|---|---|
| Stratifiye sıcak su tankı | %35-55 | 0.5-1.2 kJ/K | Endüstriyel proses tampon |
| Karışık sıcak su tankı | %25-40 | 0.8-1.8 kJ/K | Basit uygulamalar |
| PCM (optimum T_pcm) | %40-60 | 0.4-0.9 kJ/K | Kompakt, sabit T uygulamaları |
| PCM (yanlış T_pcm) | %20-35 | 0.9-2.0 kJ/K | Kaçınılmalı! |
| Buz depolama | %15-25 | 1.5-3.0 kJ/K | Alan kısıtı, yüksek tarife farkı |
| Soğuk su (stratifiye) | %30-45 | 0.6-1.4 kJ/K | Büyük soğutma tesisleri |
| Kaskad PCM (3-kademe) | %50-65 | 0.3-0.7 kJ/K | Çoklu talep sıcaklıkları |
| Kaya yatağı | %25-40 | 0.8-2.0 kJ/K | Düşük maliyetli, büyük ölçek |

### 7.6 Tasarım Karar Ağacı

```
Depolama sistemi tasarımı → EGM tabanlı karar akışı:

  1. Kaynak ve talep sıcaklıklarını belirle
     └─→ T_opt = √(T_kaynak × T_talep) hesapla

  2. Depolama süresi nedir?
     ├─ < 4 saat → Şarj/deşarj ΔT optimizasyonuna odaklan
     ├─ 4-24 saat → ΔT + izolasyon dengesi kur
     └─ > 24 saat → İzolasyon optimizasyonuna öncelik ver

  3. Alan kısıtı var mı?
     ├─ Evet → PCM veya buz depolama (yüksek yoğunluk)
     └─ Hayır → Stratifiye su tankı (düşük S_gen)

  4. Birden fazla talep sıcaklığı var mı?
     ├─ Evet → Kaskad depolama değerlendir
     └─ Hayır → Tek kademe yeterli

  5. PCM seçilecekse:
     └─→ T_erime ≈ T_opt ±5°C olan PCM seç
         └─→ Yüksek h_fg ve yüksek k tercih et
```

---

## 8. Sayısal Uygulama — Tam Çevrim EGM Analizi

**Problem:** Bir fabrikada 120°C buhar kondensatından (T_kaynak = 393.15 K) gelen atık ısı, PCM sisteminde depolanıp gece boyunca beklettikten sonra ertesi gün sıcak kullanma suyu (T_talep = 45°C = 318.15 K) üretmek için kullanılacaktır. Tam çevrim EGM analizini yapınız.

```
Adım 1 — Optimum PCM Sıcaklığı:
  T_pcm,opt = √(393.15 × 318.15) = √(125,071) = 353.7 K = 80.5°C
  Seçilen PCM: Parafin RT82 (T_erime = 82°C, h_fg = 170 kJ/kg, k = 0.2 W/(m·K))
  T_pcm = 355.15 K (yaklaşık, T_opt'a çok yakın ✓)

Adım 2 — Gerekli PCM Kütlesi:
  Depolanacak enerji: Q = 500 kWh = 1,800,000 kJ
  m_pcm = Q / h_fg = 1,800,000 / 170 = 10,588 kg ≈ 10.6 ton
  Hacim ≈ 10,588 / 800 ≈ 13.2 m³

Adım 3 — Şarj Entropi Üretimi:
  S_gen,şarj = m × h_fg × (1/T_pcm - 1/T_kaynak)
             = 10,588 × 170 × (1/355.15 - 1/393.15)
             = 1,799,960 × (0.002816 - 0.002544)
             = 1,799,960 × 0.000272
             = 489.6 kJ/K

Adım 4 — Bekleme Entropi Üretimi (12 saat bekleme):
  Tank yüzey alanı ≈ 35 m² (varsayım, 13 m³ tank)
  İzolasyon: 120 mm taş yünü, U ≈ 0.33 W/(m²·K)
  Q̇_kayıp = 0.00033 × 35 × (355.15 - 298.15) = 0.659 kW
  Ṡ_gen,bekleme = 0.659 × (1/298.15 - 1/355.15) = 0.659 × 0.000538 = 0.000354 kW/K
  S_gen,bekleme = 0.000354 × 43,200 = 15.3 kJ/K

Adım 5 — Deşarj Entropi Üretimi:
  S_gen,deşarj = m × h_fg × (1/T_talep - 1/T_pcm)
               = 1,799,960 × (1/318.15 - 1/355.15)
               = 1,799,960 × (0.003143 - 0.002816)
               = 1,799,960 × 0.000327
               = 588.6 kJ/K

Adım 6 — Toplam Entropi Üretimi:
  S_gen,toplam = 489.6 + 15.3 + 588.6 = 1,093.5 kJ/K

  Exergy yıkımı:
  İ_toplam = 298.15 × 1,093.5 = 326,029 kJ ≈ 90.6 kWh

Adım 7 — Exergy Verimi:
  Talep noktasına ulaşan exergy:
  Ex_talep ≈ Q × (1 - T₀/T_pcm) × η_deşarj
           ≈ 1,800,000 × (1 - 298.15/355.15) × 0.90
           ≈ 1,800,000 × 0.1605 × 0.90
           ≈ 260,010 kJ ≈ 72.2 kWh

  Kaynak exergisi:
  Ex_kaynak = Q × (1 - T₀/T_kaynak)
            = 1,800,000 × (1 - 298.15/393.15)
            = 1,800,000 × 0.2416
            = 434,880 kJ ≈ 120.8 kWh

  η_ex = Ex_talep / Ex_kaynak = 72.2 / 120.8 = 0.598 ≈ %59.8

Sonuç Özeti:
  ┌──────────────────────────────────────────────────────┐
  │ Depolanan enerji:              500 kWh               │
  │ Kaynak exergisi:               120.8 kWh             │
  │ Talep exergisi:                72.2 kWh              │
  │ Toplam exergy yıkımı:         90.6 kWh              │
  │ Exergy verimi:                 %59.8                 │
  │                                                      │
  │ Entropi dağılımı:                                    │
  │   Şarj:    489.6 kJ/K  (%44.8)                      │
  │   Bekleme:  15.3 kJ/K  (%1.4)                       │
  │   Deşarj:  588.6 kJ/K  (%53.8)                      │
  │                                                      │
  │ Bekleme kaybı çok düşük → izolasyon yeterli ✓        │
  │ Deşarj S_gen > Şarj S_gen → T_pcm hafif yüksek      │
  │   olabilir (T_opt = 80.5°C, PCM = 82°C → kabul)     │
  └──────────────────────────────────────────────────────┘
```

---

## İlgili Dosyalar

| Dosya | İlişki |
|---|---|
| `factory/entropy_generation/fundamentals.md` | EGM temel formülasyonları, Gouy-Stodola teoremi |
| `factory/entropy_generation/heat_transfer_egm.md` | Isı transferi EGM analizi (şarj/deşarj ΔT detayları) |
| `factory/entropy_generation/overview.md` | EGM genel bakış, metodoloji ve felsefe |
| `factory/entropy_generation/bejan_number.md` | Bejan sayısı — ısı transferi vs sürtünme payı |
| `chiller/solutions/thermal_storage.md` | Soğuk depolama uygulama detayları ve ekonomik analiz |
| `factory/cross_equipment.md` | Ekipmanlar arası exergy entegrasyonu — depolama ile sinerji |
| `factory/waste_heat_recovery.md` | Atık ısı geri kazanımı stratejileri |
| `factory/economic_analysis.md` | EGM sonuçlarının ekonomik değerlendirmesi |

---

## Referanslar

1. **Bejan, A.** (1982). *Entropy Generation Through Heat and Fluid Flow*. Wiley, New York. — Depolama sistemleri EGM analizi temelleri.

2. **Bejan, A.** (1996). *Entropy Generation Minimization*. CRC Press, Boca Raton. — Termal depolama optimizasyonu bölümü.

3. **Dincer, I. & Rosen, M.A.** (2021). *Thermal Energy Storage: Systems and Applications* (3rd Ed.). Wiley. — Kapsamlı TES referansı, exergy analizi bölümleri.

4. **Dincer, I. & Rosen, M.A.** (2013). *Exergy: Energy, Environment and Sustainable Development* (2nd Ed.). Elsevier. — TES exergy değerlendirmesi.

5. **Krane, R.J.** (1987). "A second law analysis of the optimum design and operation of thermal energy storage systems." *International Journal of Heat and Mass Transfer*, 30(1), 43-57. — TES ikinci yasa optimizasyonu.

6. **Agyenim, F., Hewitt, N., Eames, P., & Smyth, M.** (2010). "A review of materials, heat transfer and phase change problem formulation for latent heat thermal energy storage systems." *Renewable and Sustainable Energy Reviews*, 14(2), 615-628. — PCM ısı transferi ve entropi analizi.

7. **Hauer, A.** (2007). "Sorption theory for thermal energy storage design." *Thermal Energy Storage for Sustainable Energy Consumption*, NATO ASI Series. — Termokimyasal depolama temelleri.

8. **ASHRAE Handbook — HVAC Applications** (2023). Chapter 51: "Thermal Storage." — Pratik tasarım standartları.

9. **Zalba, B., Marín, J.M., Cabeza, L.F., & Mehling, H.** (2003). "Review on thermal energy storage with phase change: materials, heat transfer analysis and applications." *Applied Thermal Engineering*, 23(3), 251-283. — PCM kapsamlı derleme.

10. **Rosen, M.A. & Dincer, I.** (2003). "Exergy methods for assessing and comparing thermal storage systems." *International Journal of Energy Research*, 27(4), 415-430. — TES exergy karşılaştırma metodolojisi.

11. **Domanski, R. & Fellah, G.** (1998). "Thermoeconomic analysis of sensible heat, thermal energy storage systems." *Applied Thermal Engineering*, 18(6), 465-482. — Duyulur ısı depolama ekonomik optimizasyonu.

12. **Jegadheeswaran, S. & Pohekar, S.D.** (2009). "Performance enhancement in latent heat thermal storage system: a review." *Renewable and Sustainable Energy Reviews*, 13(9), 2225-2244. — PCM performans iyileştirme yöntemleri.

---

> **ExergyLab Notu:** Bu dosya, ısı depolama sistemlerinin EGM perspektifinden analiz ve optimizasyonu için kullanılır. Pratik uygulama detayları (boru bağlantıları, kontrol stratejileri, ekonomik analiz) için `chiller/solutions/thermal_storage.md` ve `factory/economic_analysis.md` dosyalarına başvurunuz. Temel EGM formülasyonları için `factory/entropy_generation/fundamentals.md` dosyası referans alınmalıdır.
