# Çözüm: İmpeller Kesme/Değiştirme — Impeller Trimming

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Pompa aşırı boyutlandırılmış (oversized) ve gerçek sistem ihtiyacından fazla head/debi üretiyor. Fazla enerji kısma vanası üzerinde boşa harcanıyor. Pompa BEP (Best Efficiency Point) noktasının uzağında çalışıyor.

**Çözüm:** İmpeller dış çapını tornalayarak (trimming) pompa eğrisini kalıcı olarak düşürmek. Bu sayede pompa gerçek sistem ihtiyacına daha yakın çalışır ve kısma vanası kayıpları azalır.

**Tipik Tasarruf:** %10-25
**Tipik ROI:** 0.5-2 yıl

## Çalışma Prensibi

İmpeller çapı küçültüldüğünde pompa eğrisi aşağı ve sola kayar. Bu etki, çapa bağlı benzerlik yasaları ile tahmin edilir:

### İmpeller Kesme Benzerlik Yasaları
```
Q₂ / Q₁ ≈ D₂ / D₁
H₂ / H₁ ≈ (D₂ / D₁)²
P₂ / P₁ ≈ (D₂ / D₁)³

Burada:
- Q = Debi [m³/h]
- H = Head [m]
- P = Güç [kW]
- D₁ = Orijinal impeller çapı [mm]
- D₂ = Kesilmiş impeller çapı [mm]
```

**Önemli not:** Bu yasalar hız değişimi için kesindir (exact), ancak çap değişimi için yaklaşıktır (approximate). Hydraulic Institute, benzerlik yasalarının %5'e kadar çap azaltmada güvenilir olduğunu kabul eder. Daha büyük kesmelerde pompa üreticisi ile doğrulama yapılmalıdır.

## Kesme Limitleri

| Çap Azaltma Oranı | Benzerlik Yasası Güvenilirliği | Verimlilik Etkisi | Tavsiye |
|-------------------|-------------------------------|-------------------|---------|
| %0-5 | Yüksek (HI onaylı) | Minimal verim kaybı (<%1) | Güvenle uygulanabilir |
| %5-10 | Orta (üretici doğrulaması önerilir) | %1-3 verim kaybı | Dikkatli uygulama |
| %10-15 | Düşük (mutlaka üretici onayı) | %3-5 verim kaybı | Sadece gerekirse |
| %15-20 | Çok düşük | %5-10 verim kaybı | Yeni impeller veya pompa tercih edilmeli |
| >%20 | Geçersiz | Ciddi verim düşüşü | Kesinlikle uygulanmamalı; pompa değiştirilmeli |

**Maksimum kesme kuralı:** İmpeller çapı, pompa gövdesindeki (casing) maksimum impeller çapının %75'inden küçük olmamalıdır (Hydraulic Institute kuralı).

## Verimlilik Etkisi Detay Tablosu

| Çap Azaltma % | Head Azalma % | Güç Azalma % | Verim Değişimi | Net Tasarruf |
|---------------|---------------|--------------|----------------|-------------|
| %5 | ~%10 | ~%14 | -%0.5 puan | %10-14 |
| %10 | ~%19 | ~%27 | -%2 puan | %20-25 |
| %15 | ~%28 | ~%39 | -%4 puan | %25-35 |
| %20 | ~%36 | ~%49 | -%7 puan | %30-40* |

*%20 kesme yalnızca özel durumlarda; verim kaybı önemli.*

## BEP Kayması (Best Efficiency Point Shift)

İmpeller kesildiğinde BEP noktası da değişir:
- BEP debisi düşer (Q_BEP ∝ D)
- BEP head değeri düşer (H_BEP ∝ D²)
- BEP verim değeri biraz düşer (cutwater clearance artar)

**Dikkat:** Kesme sonrası pompa yeni BEP noktasına yakın çalışmalıdır. Eğer sistem gereksinimi kesilmiş impeller'in BEP'inden uzaksa, tasarruf beklenen kadar olmayabilir.

## VSD ile Karşılaştırma

| Faktör | İmpeller Kesme | VSD |
|--------|---------------|-----|
| Yatırım maliyeti | Düşük (€500-5,000) | Orta-Yüksek (€3,000-40,000) |
| Esneklik | Yok — kalıcı değişiklik | Yüksek — gerçek zamanlı ayar |
| Tasarruf (değişken yük) | Sabit; yükte değişime uyum sağlamaz | Yüke göre dinamik tasarruf |
| Tasarruf (sabit yük) | İyi; basit ve etkili | İyi ama VSD kaybı (%2-3) var |
| Bakım | Ek bakım yok | VSD bakımı, fan filtresi, vb. |
| Karmaşıklık | Düşük | Orta (elektrik altyapısı gerekir) |
| En uygun durum | Sabit yük, kalıcı oversizing | Değişken yük, esnek kontrol |

**Tavsiye:** Yük profili sabitse ve pompa kalıcı olarak aşırı boyutlandırılmışsa, impeller kesme en maliyet-etkin çözümdür. Yük değişkense VSD tercih edilmelidir. Bazı durumlarda her ikisi birlikte uygulanabilir (kesilmiş impeller + VSD).

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı
- Pompa sürekli kısılmış vana ile çalışıyorsa
- Bypass hattı sürekli açıksa
- Pompa BEP'in sağında (yüksek debi tarafında) çalışıyorsa
- Sistem gereksinimi sabit veya dar aralıkta değişiyorsa
- Yük profili ölçümü kalıcı oversizing doğruluyorsa

### Ne Zaman Uygulanmamalı
- Yük profili geniş aralıkta değişiyorsa (VSD daha uygun)
- Gerekli kesme oranı >%15-20 ise (yeni impeller veya pompa tercih edilmeli)
- Pompa zaten düşük verimli çalışıyorsa
- Gelecekte kapasite artışı planlanıyorsa

## Yatırım Maliyeti

| İşlem | Maliyet (€) | Süre |
|-------|-------------|------|
| Mevcut impeller tornalama | €500-2,000 | 1-3 gün (pompa sökme/takma dahil) |
| Yeni küçük impeller satın alma | €1,000-5,000 | 2-6 hafta (tedarik süresi) |
| Pompa sökme/takma işçiliği | €500-2,000 | 1-2 gün |
| Toplam (tornalama yolu) | €1,000-4,000 | — |
| Toplam (yeni impeller yolu) | €2,000-7,000 | — |

## ROI Hesabı

### Formül
```
P_mevcut = P_nominal × (Güç%_throttle / 100)
P_yeni = P_nominal × (D₂/D₁)³ × (η_eski / η_yeni)
Yıllık_tasarruf_kWh = (P_mevcut - P_yeni) × Çalışma_saati
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Yıllık_tasarruf_EUR
```

### Örnek Hesap
- 30 kW santrifüj pompa, impeller çapı 250 mm, 6,000 saat/yıl
- Mevcut durum: kısma vanası ile 22 kW ortalama çekim (%73 güç)
- Sistem analizi: 225 mm impeller yeterli (%10 kesme)
- Yeni güç: 30 × (225/250)³ = 30 × 0.729 = 21.9 kW (brüt)
- Verim düzeltmesi ile: ~20 kW (kısma vanası kaybı ortadan kalkar)
- Yıllık tasarruf: (22 - 20) × 6,000 = 12,000 kWh
- Ancak gerçek tasarruf: Vana kaybı eliminasyonu ile birlikte ~18,000 kWh
- Elektrik: €0.15/kWh → Yıllık tasarruf: **€2,700/yıl**
- Tornalama maliyeti: €2,000
- **Geri ödeme: 2,000 / 2,700 = 0.74 yıl (≈9 ay)**

## Uygulama Adımları

1. **Mevcut performans ölçümü:** Debi, head, güç tüketimi ve vana pozisyonunu ölç
2. **Sistem eğrisi belirleme:** Gerçek sistem ihtiyacı (debi ve head) hesapla
3. **Hedef impeller çapı hesabı:** Benzerlik yasaları ile gerekli çapı belirle
4. **Üretici doğrulaması:** Pompa üreticisinden kesilmiş impeller performans eğrisini al
5. **Kesme kararı:** Tornalama mı, yeni impeller mı — maliyet ve tedarik süresine göre karar ver
6. **Uygulama:** Pompayı durdur, impeller'i çıkar, torna/değiştir, geri monte et
7. **Devreye alma ve doğrulama:** Yeni performansı ölç, kısma vanasını tam aç, titreşim kontrolü yap

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Aşırı kesme | Verim düşüşü ve instabilite | Max %15-20 kesme; üretici limitlerini aşma |
| BEP kayması | Çalışma noktası BEP'ten uzaklaşabilir | Sistem eğrisi ile yeni BEP'i doğrula |
| Geri dönüşsüzlük | Kesme kalıcıdır; kapasite geri artırılamaz | Orijinal impeller'i yedek olarak sakla |
| Kavitasyon | Değişen NPSH required | NPSH hesabını yeni koşullar için yenile |
| Dengesizlik | Tornalama sonrası dinamik balans bozulabilir | Kesme sonrası impeller balansını yaptır |

## İlgili Dosyalar
- Pompa boyutlandırma: `solutions/pump_right_sizing.md`
- VSD ile kontrol: `solutions/pump_vsd.md`
- Pompa exergy formülleri: `formulas/pump_exergy.md`
- Sistem optimizasyonu: `solutions/pump_system_optimization.md`

## Referanslar
- Hydraulic Institute, "Trimming Impellers to Reduce Energy Consumption" (2022)
- DOE/AMO, "Trim or Replace Impellers on Oversized Pumps," Energy Tips — Pumping Systems
- Hydraulic Institute, ANSI/HI 14.3-2019, "Rotodynamic Pumps for Design and Application"
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition
- WaterWorld, "Back to Basics Part II — Impact of Impeller Trim on Pump Efficiency"
