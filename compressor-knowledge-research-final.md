# ExergyLab: Kompresör Knowledge Base Araştırma Brief (Final)

> **Claude Code için talimat:** Bu dosyayı oku, web araştırması yap, ExergyLab projesinin `/knowledge` dizinini doldur. Araştırma sırasında bu brief'te olmayan ama faydalı olacağını düşündüğün bilgiler bulursan, uygun dosyalara ekle veya yeni dosya oluştur.

---

## 🎯 Görev Özeti

ExergyLab projesinin `/knowledge` dizinindeki kompresör bilgilerini genişlet.

**Mevcut durum:** Sadece `compressor_screw.md` (vidalı kompresör) var.
**Hedef:** Tüm kompresör tipleri, sistem bilgisi, çözüm önerileri, benchmark verileri ve audit metodolojisi.

**Önemli:** Mevcut dosyaları bozmadan genişlet.

---

## 📁 Oluşturulacak Dosya Yapısı

```
knowledge/
├── equipment/
│   ├── compressor_screw.md              (mevcut, gerekirse güncelle)
│   ├── compressor_screw_oilfree.md      (yeni)
│   ├── compressor_piston.md             (yeni)
│   ├── compressor_scroll.md             (yeni)
│   ├── compressor_centrifugal.md        (yeni)
│   ├── compressor_roots.md              (yeni, opsiyonel)
│   └── compressed_air_systems.md        (yeni)
│
├── benchmarks/
│   └── compressor_benchmarks.md         (mevcut, genişlet)
│
├── solutions/
│   ├── compressor_heat_recovery.md      (mevcut, genişlet)
│   ├── compressor_vsd.md                (yeni)
│   ├── compressor_air_leaks.md          (yeni)
│   ├── compressor_pressure_optimization.md (yeni)
│   ├── compressor_dryer_optimization.md (yeni)
│   ├── compressor_inlet_optimization.md (yeni)
│   ├── compressor_system_design.md      (yeni)
│   └── compressor_maintenance.md        (yeni)
│
├── formulas/
│   └── compressor_exergy.md             (mevcut, genişlet)
│
└── methodology/
    └── compressed_air_audit.md          (yeni)

Toplam: ~17 dosya
```

---

## 📋 BÖLÜM 1: Equipment (Ekipman Tanımları)

Her dosya için aşağıdaki template'i kullan. Mevcut `compressor_screw.md` referans alınabilir.

### Equipment Dosyası Template

```markdown
# [Kompresör Tipi]

> Son güncelleme: [Tarih]

## Genel Bilgiler
- Tip ve sınıflandırma
- Kapasite aralığı (kW)
- Basınç aralığı (bar)
- Yaygın markalar ve modeller
- Tipik uygulama alanları

## Çalışma Prensibi
[Kısa teknik açıklama, şematik varsa belirt]

## Enerji Dağılımı (Tipik)
| Bileşen | Oran |
|---------|------|
| Basınçlı hava (faydalı iş) | X% |
| Yağ/su soğutucuya atılan ısı | X% |
| Aftercooler'a atılan ısı | X% |
| Radyasyon ve diğer kayıplar | X% |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|

### Nameplate Bilgileri
- Toplanacak bilgiler listesi

## Varsayılan Değerler (Ölçüm Yoksa)
| Parametre | Varsayılan | Not |
|-----------|------------|-----|

## Bu Tipe Özgü Özellikler
[Exergy analizi yaparken dikkat edilecekler]

## Tipik Arızalar ve Verimsizlik Nedenleri
[Sahada dikkat edilecek noktalar]

## Kısmi Yük Performansı
[Yük değişimine tepki, verim düşüşü]
```

---

### 1.1 Vidalı Kompresör - Yağsız (Oil-Free Screw)
**Dosya:** `/knowledge/equipment/compressor_screw_oilfree.md`

Araştır:
- Çalışma prensibi (kuru sıkıştırma, water-injected vs dry)
- Kapasite aralığı: 15-350 kW
- Kullanım alanları: Gıda, ilaç, elektronik, tekstil (Class 0 gerektiren)
- ISO 8573-1 Class 0 sertifikasyonu
- Yağlı tipe göre farklar:
  - Daha düşük verim (%10-15 daha fazla enerji)
  - Daha yüksek ilk yatırım
  - Daha düşük bakım maliyeti (yağ yok)
  - Daha yüksek çıkış sıcaklığı
- Exergy verimi karakteristiği
- Yaygın markalar: Atlas Copco ZR/ZT, Kaeser FSG, Ingersoll Rand Sierra

### 1.2 Pistonlu Kompresör (Reciprocating)
**Dosya:** `/knowledge/equipment/compressor_piston.md`

Araştır:
- Çalışma prensibi:
  - Tek etkili vs çift etkili
  - Tek kademeli vs çok kademeli
  - Hava soğutmalı vs su soğutmalı
- Kapasite aralığı: 0.5-50 kW (küçük), 50-500+ kW (büyük endüstriyel)
- Basınç aralığı: 7-40+ bar (yüksek basınç uygulamaları)
- Tipik uygulamalar:
  - Küçük atölyeler
  - Yüksek basınç (PET şişirme, 30-40 bar)
  - Aralıklı kullanım
- Enerji dağılımı
- Pulsasyonlu akış karakteristiği
- Bakım gereksinimleri (valf, piston segmanı, vb.)
- Exergy verimi (vidalıya göre genelde düşük sürekli çalışmada)
- Yaygın markalar: Bauer, Sauer, Ingersoll Rand T30

### 1.3 Scroll Kompresör
**Dosya:** `/knowledge/equipment/compressor_scroll.md`

Araştır:
- Çalışma prensibi (orbital scroll hareketi, sabit + hareketli spiral)
- Kapasite aralığı: 1-15 kW (genelde küçük-orta)
- Avantajlar:
  - Sessiz çalışma (<65 dB)
  - Titreşimsiz
  - Oil-free seçenekler mevcut
  - Kompakt boyut
  - Düşük bakım
- Sınırlamalar:
  - Kapasite sınırlı
  - Büyük sistemler için uygun değil
- Tipik uygulamalar: HVAC, medikal hava, laboratuvar, gıda
- Exergy verimi karakteristiği
- Yaygın markalar: Atlas Copco SF, Anest Iwata, GAST

### 1.4 Santrifüj Kompresör (Centrifugal)
**Dosya:** `/knowledge/equipment/compressor_centrifugal.md`

Araştır:
- Çalışma prensibi:
  - Dinamik sıkıştırma (kinetik → basınç)
  - Tek vs çok kademeli
  - Interstage cooling
  - Inlet guide vanes (IGV)
- Kapasite aralığı: 150-3000+ kW
- Basınç: 3-10 bar (tek kademe), 10-40+ bar (çok kademe)
- Önemli kavramlar:
  - **Surge:** Minimum akış sınırı, sistem instabilitesi
  - **Choke/Stonewall:** Maximum akış sınırı
  - **Turndown:** Kısmi yük kapasitesi (%50-100 aralığı)
- VSD kontrolü (manyetik yataklar ile 30,000+ RPM)
- Yağsız çalışma (manyetik yatak sistemleri)
- Exergy verimi: Genelde en yüksek (>65% mümkün)
- Tipik uygulamalar: Büyük fabrikalar, petrokimya, enerji santralleri
- Yaygın markalar: Atlas Copco ZH, Ingersoll Rand Centac, Cameron/Sullair

### 1.5 Roots Blower / Lobe Kompresör (Opsiyonel)
**Dosya:** `/knowledge/equipment/compressor_roots.md`

Araştır:
- Çalışma prensibi (pozitif deplasman, döner loblar)
- Kapasite: Yüksek debi, düşük basınç (0.3-1.0 bar gauge)
- Tipik uygulamalar:
  - Atıksu arıtma (havalandırma)
  - Pnömatik taşıma
  - Vakum sistemleri
- Verim karakteristiği
- Exergy analizi yaklaşımı (düşük basınç farkı)

### 1.6 Basınçlı Hava Sistemleri — Genel Bakış
**Dosya:** `/knowledge/equipment/compressed_air_systems.md`

**Bu dosya çok önemli — sistem seviyesi düşünce için temel.**

Araştır:
- **Sistem bileşenleri:**
  - Kompresör (supply side)
  - Hava alma ve filtrasyon
  - Aftercooler ve nem ayırıcı
  - Hava kurutucu (dryer)
  - Depolama tankı (receiver)
  - Dağıtım hattı (piping)
  - Kullanım noktaları (demand side)
  
- **Çoklu kompresör konfigürasyonları:**
  - Lead/Lag sıralama
  - VSD + sabit hız kombinasyonu
  - Yedekleme stratejileri
  - Master controller sistemleri
  
- **Basınç kavramları:**
  - Kompresör çıkış basıncı
  - Sistem basıncı (header pressure)
  - Nokta basıncı (point-of-use pressure)
  - Basınç düşüşü kaynakları
  
- **Kapasite hesaplama:**
  - Toplam talep hesabı
  - Diversity factor (eşzamanlılık)
  - Gelecek büyüme payı
  
- **Tipik sistem verimsizlikleri:**
  - Kaçaklar (%20-30)
  - Yanlış uygulama (blow-off, açık üfleme)
  - Aşırı basınç
  - Kısmi yük kayıpları
  - Kontrol sistemi uyumsuzluğu
  
- **Demand-side vs Supply-side optimizasyon:**
  - Önce demand-side (kaçak, yanlış kullanım)
  - Sonra supply-side (kompresör verimi)
  
- **Merkezi vs Dağıtık sistemler:**
  - Ne zaman hangisi tercih edilir
  - Hibrit yaklaşımlar

---

## 📊 BÖLÜM 2: Benchmarks

**Dosya:** `/knowledge/benchmarks/compressor_benchmarks.md` — GÜNCELLE/GENİŞLET

### Eklenecek İçerik:

#### 2.1 Tip Bazlı Exergy Verimi
```markdown
| Kompresör Tipi | Düşük | Ortalama | İyi | Best-in-class |
|----------------|-------|----------|-----|---------------|
| Vidalı (yağlı) | <30%  | 35-45%   | 45-55% | >60% |
| Vidalı (yağsız)| <25%  | 30-40%   | 40-50% | >55% |
| Pistonlu       | <25%  | 30-40%   | 40-50% | >55% |
| Scroll         | <30%  | 35-45%   | 45-55% | >60% |
| Santrifüj      | <35%  | 40-50%   | 50-60% | >65% |
```

#### 2.2 Spesifik Güç Tüketimi (kW per m³/min @ 7 bar)
- Tip bazlı karşılaştırma
- Kapasite sınıflarına göre (küçük/orta/büyük)
- Motor verimlilik sınıfları etkisi (IE2, IE3, IE4)

#### 2.3 Kısmi Yük Verimliliği
| Yük (%) | Vidalı Load/Unload | Vidalı VSD | Pistonlu | Santrifüj IGV |
|---------|-------------------|------------|----------|---------------|
| 100%    | 100%              | 100%       | 100%     | 100% |
| 75%     | 85%               | 97%        | 75%      | 90% |
| 50%     | 65%               | 93%        | 50%      | 75% |
| 25%     | 45%               | 85%        | 25%      | — |

#### 2.4 Kaçak Oranları Benchmark
| Durum | Kaçak Oranı | Açıklama |
|-------|-------------|----------|
| Mükemmel | <5% | Aktif kaçak yönetim programı |
| İyi | 5-10% | Düzenli tarama |
| Ortalama | 10-20% | Ara sıra tarama |
| Kötü | 20-30% | Tarama yok |
| Çok kötü | >30% | İhmal edilmiş sistem |

#### 2.5 Yaşa Göre Verim Düşüşü
- İlk 5 yıl, 5-10 yıl, 10+ yıl
- Bakım kalitesine göre varyasyon

#### 2.6 Sektörel Ortalamalar
Mevcut tabloya ekle/genişlet:
- Tipik kompresör tipleri (sektöre göre)
- Ortalama sistem verimi
- İyileştirme potansiyeli

---

## 💡 BÖLÜM 3: Solutions (Çözüm Önerileri)

Her çözüm dosyası için bu template'i kullan:

### Solution Dosyası Template

```markdown
# [Çözüm Adı]

> Son güncelleme: [Tarih]

## Özet
[1-2 cümle: Ne, neden, ne kadar tasarruf]

## Problem Tanımı
[Bu çözümün hedeflediği verimsizlik]

## Çalışma Prensibi
[Teknik açıklama]

## Ne Zaman Uygulanır?
- Uygunluk kriterleri
- Kontrol edilecek parametreler
- Karar matrisi

## Ne Zaman Uygulanmaz?
- Kontraendikasyonlar
- Dikkat edilecek durumlar

## Tipik Tasarruf Potansiyeli
| Durum | Tasarruf |
|-------|----------|
| ... | X-Y% |

## Yatırım Maliyeti
| Kapasite/Kapsam | Maliyet Aralığı |
|-----------------|-----------------|
| ... | €X - €Y |

## ROI Hesaplama

### Formül
```
[Açık formül]
```

### Örnek Hesaplama
[Somut numerik örnek]

## Uygulama Adımları
1. ...
2. ...
3. ...

## Dikkat Edilecekler / Riskler
- ...

## Tedarikçi/Ekipman Önerileri (varsa)
- ...

## Vaka Çalışması
[Gerçek dünya örneği, kaynak belirt]

## Kaynaklar
- [Referanslar]
```

---

### 3.1 VSD (Variable Speed Drive) Retrofit
**Dosya:** `/knowledge/solutions/compressor_vsd.md`

Araştır:
- VSD nasıl çalışır (frekans kontrolü → hız kontrolü → debi kontrolü)
- Tasarruf mekanizması (Affinity Laws: Güç ∝ Hız³)
- **Ne zaman uygulanır:**
  - Değişken yük profili (%30-80 aralığında dalgalanma)
  - Load/unload kayıpları yüksek
  - Trim kompresör ihtiyacı
- **Ne zaman uygulanmaz:**
  - Sabit yük (%90+ sürekli)
  - Çok küçük kompresörler (<4 kW, maliyet/fayda)
  - Eski motor (retrofit uyumsuz)
- **Retrofit vs Yeni VSD kompresör:**
  - Retrofit: Mevcut kompresöre harici VSD
  - Yeni: Fabrika entegre (Atlas Copco GA VSD+, Kaeser SFC)
  - Maliyet/performans karşılaştırması
- **Sistem tasarımı:**
  - VSD + sabit hız kombinasyonu (base load + trim)
  - Sequencing stratejisi
- Yatırım maliyeti aralıkları
- ROI: Tipik 1-3 yıl
- Marka/model önerileri

### 3.2 Kaçak Tespiti ve Giderme
**Dosya:** `/knowledge/solutions/compressor_air_leaks.md`

Araştır:
- **Problem boyutu:**
  - Tipik kaçak oranları (%20-30 ortalama tesis)
  - Kaçak = para kaybı (somut rakamlar)
- **Kaçak maliyeti formülü:**
  ```
  Kaçak_debisi (l/s) = C × d² × √P
  Maliyet (€/yıl) = Kaçak_debisi × SEC × Çalışma_saati × Elektrik_fiyatı
  
  Burada:
  - C = 0.067 (katsayı)
  - d = delik çapı (mm)
  - P = basınç (bar)
  - SEC = spesifik enerji tüketimi (kW per l/s)
  ```
- **Kaçak maliyet tablosu:**
  | Delik Çapı | 7 bar'da Kaçak | Yıllık Maliyet (@0.10€/kWh, 8000h) |
  |------------|----------------|-----------------------------------|
  | 1 mm       | X l/s          | €Y |
  | 3 mm       | X l/s          | €Y |
  | 5 mm       | X l/s          | €Y |
  | 10 mm      | X l/s          | €Y |
- **Tespit yöntemleri:**
  - **Ultrasonik dedektör:** En etkili, 40 kHz frekans
    - Ekipman: SDT, UE Systems, Fluke ii900
    - Fiyat aralığı: €2,000-15,000
  - **Akustik görüntüleme kamerası:** Fluke ii910, Teledyne FLIR Si124
    - Hızlı tarama, görsel
    - Fiyat: €15,000-30,000
  - **Sabunlu su:** Basit, yavaş, sınırlı
  - **Sistem seviyesi:** Tank drop testi, debi ölçümü
- **Yaygın kaçak noktaları (öncelik sırası):**
  1. Hızlı bağlantılar (quick couplings)
  2. Hortum bağlantıları
  3. Vana/valf sızıntıları
  4. Regülatörler
  5. Silindir contaları
  6. Boru bağlantıları (flanş, dişli)
  7. Filtre gövdeleri
  8. Drenaj noktaları
- **Onarım maliyetleri:**
  - Basit (bağlantı sıkma): €0-10
  - Orta (conta değişimi): €10-50
  - Büyük (valf değişimi): €50-200
- **Kaçak yönetim programı:**
  - Periyodik tarama (3-6 ayda bir)
  - Etiketleme sistemi (tespit → onarım takibi)
  - KPI takibi (kaçak oranı trendi)
- ROI: Genellikle 3-12 ay

### 3.3 Basınç Optimizasyonu
**Dosya:** `/knowledge/solutions/compressor_pressure_optimization.md`

Araştır:
- **Temel kural:** Her 1 bar düşüş ≈ %6-7 enerji tasarrufu
- **Neden aşırı basınç:**
  - "Güvenlik marjı" yaklaşımı
  - Hat kayıplarını kompanse etme
  - Tüm noktaların ihtiyacını karşılama
- **Analiz adımları:**
  1. Tüm kullanım noktalarının gerçek basınç ihtiyacını belirle
  2. Kritik noktayı bul (en yüksek basınç gereksinimi)
  3. Dağıtım hattı basınç düşüşlerini ölç/hesapla
  4. Minimum sistem basıncını belirle
- **Basınç düşürme stratejileri:**
  - Doğrudan kompresör set basıncını düşür
  - Hat kayıplarını azalt (boru çapı, layout)
  - Basınç/akış kontrolörü (flow controller)
  - Bölgesel basınç (zone pressure) - yüksek basınç gereken noktalara booster
- **Dikkat:**
  - Kademeli düşür, ani değil
  - Operasyonu izle
  - Uç noktaları kontrol et
- Yatırım: Genellikle düşük veya sıfır (sadece ayar)
- ROI formülü ve örnek

### 3.4 Kurutucu Optimizasyonu
**Dosya:** `/knowledge/solutions/compressor_dryer_optimization.md`

Araştır:
- **Kurutucu tipleri ve enerji tüketimi:**
  | Tip | Enerji Tüketimi | Dewpoint |
  |-----|-----------------|----------|
  | Soğutmalı (refrigerated) | 0.5-2% kompresör gücü | +3°C PDP |
  | Adsorpsiyon (heatless) | 15-20% purge kaybı | -40°C PDP |
  | Adsorpsiyon (heated) | 5-10% + ısıtıcı | -40°C PDP |
  | HOC (heat of compression) | ~0% | -40°C PDP |
  | Membran | 15-20% purge | -40°C PDP |
  
- **Optimizasyon fırsatları:**
  - Gereğinden düşük dewpoint (overspecification)
  - Dewpoint talep kontrolü (load-dependent drying)
  - Purge kaybını azaltma (adsorpsiyon tip)
  - HOC sistemine geçiş (yeni sistem için)
  - Soğutmalı kurutucu enerji tasarrufu modları
- **Heat of Compression (HOC) kurutucular:**
  - Kompresör atık ısısını kullanır
  - Ek enerji tüketimi yok
  - Yatırım maliyeti yüksek ama opex düşük
- ROI hesaplama

### 3.5 Isı Geri Kazanımı
**Dosya:** `/knowledge/solutions/compressor_heat_recovery.md` — MEVCUT, GENİŞLET

Eklenecek:
- Farklı sistem tipleri detayı:
  - Hava-hava (mekan ısıtma)
  - Hava-su (proses su, kazan besleme)
  - Direkt entegrasyon
- Mevsimsel kullanım faktörü (Türkiye iklim bölgeleri için)
- Entegrasyon maliyetleri detayı
- Uygulama örnekleri (sektörel)
- ROI hassasiyeti (kullanım faktörüne göre)

### 3.6 Giriş Havası Optimizasyonu
**Dosya:** `/knowledge/solutions/compressor_inlet_optimization.md`

Araştır:
- **Sıcaklık etkisi:**
  - Her 3°C düşüş ≈ %1 verim artışı
  - Yazın en büyük etkisi
- **Dış ortamdan hava çekme:**
  - Kompresör odasından vs dışarıdan
  - Kanal tasarımı, filtre
  - Yatırım ve tasarruf
- **Filtre bakımı:**
  - Tıkalı filtre = basınç düşüşü = enerji artışı
  - Değişim periyodları
  - Diferansiyel basınç izleme
- **Nem kontrolü:**
  - Yüksek nem bölgelerinde dikkat
- ROI hesaplama

### 3.7 Sistem Tasarımı İyileştirmeleri
**Dosya:** `/knowledge/solutions/compressor_system_design.md`

Araştır:
- **Depolama tankı:**
  - Boyutlandırma kuralları
  - VSD ile tank boyutu ilişkisi
  - Lokasyon (kompresör sonrası, kullanım noktası)
- **Boru hattı:**
  - Çap hesabı (hız < 6 m/s kuralı)
  - Ring vs linear layout
  - Basınç düşüşü hesabı
- **Kondenstop ve drenaj:**
  - Timer vs demand drains
  - No-loss drains
- **Çoklu kompresör sıralama:**
  - Master controller
  - Sequencing stratejileri
  - VSD + sabit hız optimizasyonu
- Yatırım/tasarruf analizi

### 3.8 Bakım Bazlı Verimlilik
**Dosya:** `/knowledge/solutions/compressor_maintenance.md`

Araştır:
- **Filtre bakımı:**
  - Hava giriş filtresi: Tıkanma = basınç düşüşü
  - Yağ filtresi: Tıkanma = aşırı ısınma
  - Değişim periyotları ve kriterleri
- **Yağ kalitesi:**
  - Analiz periyodu
  - Değişim kriterleri
  - Yağ tipi seçimi
- **Soğutucu temizliği:**
  - Aftercooler, oil cooler
  - Kirli soğutucu = düşük verim
- **Valf bakımı:**
  - Giriş/çıkış valfleri (pistonlu)
  - Minimum basınç valfi
- **Kontrol sistemi:**
  - Kalibrasyon
  - Sensör kontrolü
- **Prediktif bakım:**
  - Vibrasyon analizi
  - Sıcaklık trendi
  - Yağ analizi
- Bakım maliyeti vs enerji tasarrufu karşılaştırması

---

## 📐 BÖLÜM 4: Formulas

**Dosya:** `/knowledge/formulas/compressor_exergy.md` — GÜNCELLE/GENİŞLET

### Eklenecek İçerik:

#### 4.1 Çok Kademeli Sıkıştırma
```
W_total = n × W_stage
W_stage = (n/(n-1)) × P₁ × V̇ × [(P₂/P₁)^((n-1)/n) - 1]

Ara soğutma ile:
P_intermediate = √(P₁ × P₂)  (iki kademe için)
```

#### 4.2 Politropik Verim
```
η_polytropic = ln(P₂/P₁) / ln(T₂/T₁) × (k-1)/k

Burada k = Cp/Cv = 1.4 (hava için)
```

#### 4.3 İzentropik → Exergy Verim Dönüşümü
```
η_exergy ≈ η_isentropic × [T₀ × ln(P₂/P₁)] / [(T₂ - T₁)]

Yaklaşık ilişki, ideal gaz kabulü ile
```

#### 4.4 Kaçak Kaynaklı Exergy Kaybı
```
Ex_leak = V̇_leak × R × T₀ × ln(P_system/P₀)

Maliyet = Ex_leak × Çalışma_saati × (Elektrik_fiyatı / η_overall)
```

#### 4.5 Sistem Seviyesi Exergy Analizi
```
Ex_input = Σ W_compressors (elektrik)
Ex_useful = Σ V̇_use_points × R × T₀ × ln(P_use/P₀)
Ex_loss = Ex_leak + Ex_waste_heat + Ex_pressure_drop + Ex_control_losses

η_system = Ex_useful / Ex_input
```

---

## 📖 BÖLÜM 5: Methodology

**Dosya:** `/knowledge/methodology/compressed_air_audit.md`

### Tam Audit Rehberi Yaz:

#### 5.1 Audit Öncesi Hazırlık
- **Toplanacak bilgiler:**
  - Son 12 ay enerji faturaları
  - Ekipman listesi (kompresör, kurutucu, tank)
  - Sistem şemaları / P&ID
  - Üretim takvimi
  - Bilinen sorunlar
- **Ön görüşme soruları**
- **Ekipman listesi:**
  | Ekipman | Marka/Model | Amaç |
  |---------|-------------|------|
  | Power analyzer | Fluke 435-II, Hioki | Güç profili |
  | Clamp meter | Fluke 376 | Anlık güç |
  | Manometre | Dijital, 0-16 bar | Basınç |
  | IR termometre | Fluke 62 MAX | Sıcaklık |
  | Ultrasonik dedektör | SDT270, UE UP100 | Kaçak |
  | Data logger | — | Uzun süreli kayıt |

#### 5.2 Saha Çalışması

**A. Sistem Envanteri**
- Tüm kompresörlerin nameplate verileri
- Kurutucu, tank, filtre bilgileri
- Dağıtım hattı layout'u
- Kullanım noktaları

**B. Ölçümler**
- Güç profili (min 24 saat, ideal 1 hafta)
- Basınç profili (kompresör çıkış, sistem, uç noktalar)
- Sıcaklıklar (giriş, çıkış, yağ, aftercooler)
- Debi (varsa flowmeter, yoksa tank drop testi)

**C. Kaçak Taraması**
- Ultrasonik ile sistematik tarama
- Kaçak noktalarını etiketle ve kaydet
- Kaçak büyüklüğü tahmini

**D. Gözlemsel Kontroller**
- Filtre durumu
- Drenaj çalışması
- Kompresör odası sıcaklığı
- Yanlış kullanımlar (açık üfleme, vb.)

**E. Operatör Görüşmesi**
- Çalışma paterni
- Bilinen sorunlar
- Bakım geçmişi

#### 5.3 Veri Analizi
- Yük profili analizi (load/unload oranları)
- Spesifik güç hesabı (kW per m³/min)
- Exergy analizi (ExergyLab engine kullan)
- Kaçak oranı hesabı
- Benchmark karşılaştırma

#### 5.4 Raporlama Yapısı
1. Yönetici Özeti (1 sayfa)
2. Sistem Tanımı
3. Mevcut Durum Değerlendirmesi
4. Bulgular ve Analiz
5. İyileştirme Önerileri (öncelikli sıra)
6. ROI Hesapları
7. Uygulama Yol Haritası
8. Ekler (ölçüm verileri, fotoğraflar)

#### 5.5 Saha Kontrol Listesi (Checklist)

```markdown
## Kompresör Odası
- [ ] Ortam sıcaklığı ölçüldü
- [ ] Giriş havası kaynağı kontrol edildi
- [ ] Havalandırma yeterliliği kontrol edildi
- [ ] Nameplate verileri kaydedildi
- [ ] Güç ölçümü yapıldı
- [ ] Basınç ölçümü yapıldı
- [ ] Çıkış sıcaklığı ölçüldü
- [ ] Kontrol paneli bilgileri kaydedildi
- [ ] Filtre durumu kontrol edildi
- [ ] Kurutucu tipi ve durumu kaydedildi
- [ ] Tank boyutu ve durumu kaydedildi
- [ ] Yağ seviyesi / durumu kontrol edildi
- [ ] Drenaj çalışması kontrol edildi

## Dağıtım Sistemi
- [ ] Ana hat basıncı ölçüldü
- [ ] Kritik uç nokta basınçları ölçüldü
- [ ] Kaçak taraması yapıldı
- [ ] Kaçak noktaları etiketlendi/kaydedildi
- [ ] Boru çapları not edildi
- [ ] Basınç düşüşü noktaları belirlendi

## Kullanım Noktaları
- [ ] Ana tüketiciler belirlendi
- [ ] Basınç gereksinimleri sorgulandı
- [ ] Yanlış kullanımlar tespit edildi
- [ ] Demand profili hakkında bilgi alındı
```

---

## 🔍 Araştırma Kaynakları

Web search ile öncelikli kaynaklar:

1. **Resmi/Kurumsal:**
   - U.S. DOE — Compressed Air Challenge, Best Practices
   - European Commission — BAT Reference Documents
   - Carbon Trust (UK) — Compressed Air guides
   - ISO 11011 — Compressed air energy efficiency assessment
   - ISO 1217 — Displacement compressors acceptance tests

2. **Üretici Teknik Dökümanları:**
   - Atlas Copco — Compressed Air Manual (online)
   - Kaeser — Kompendium, Application guides
   - Ingersoll Rand — Energy efficiency resources
   - Gardner Denver — Technical literature

3. **Endüstri Kaynakları:**
   - Compressed Air & Gas Institute (CAGI)
   - ENERGY STAR for Industry
   - Plant Engineering magazine

---

## ⚠️ Önemli Kurallar

1. **Veri doğruluğu:** Sayısal değerler için kaynak belirt. Kesin değilse "tipik", "yaklaşık" kullan.

2. **Birim tutarlılığı:** SI birimleri (kW, bar, m³/min, °C). Gerekirse dönüşüm tablosu ekle.

3. **Pratiklik:** Akademik detay değil, sahada kullanılabilir bilgi. "Bu veriyle ne yaparım?" sorusuna cevap ver.

4. **Türkçe:** Tüm içerik Türkçe. Teknik terimler (VSD, aftercooler, surge) İngilizce kalabilir.

5. **Tarih:** Her dosyanın başına oluşturma/güncelleme tarihi ekle.

---

## 🚀 Ek Yönerge: Keşif Modu

Bu brief kapsamı dışında, araştırma sırasında şunları bulursan:

- **Yeni çözüm önerileri** (brief'te olmayan)
- **İlginç vaka çalışmaları** (gerçek dünya ROI verileri)
- **Güncel teknolojiler** (örn: AI-based leak detection, IoT monitoring)
- **Bölgesel/sektörel spesifik bilgiler** (Türkiye elektrik fiyatları, vb.)

→ **Uygun dosyaya ekle veya yeni dosya oluştur.**

Yeni dosya oluşturursan, dosya adını ve kısa açıklamasını final raporunda belirt.

---

## ✅ Tamamlama Kontrolü

Tüm dosyaları oluşturduktan sonra:

1. **Klasör yapısını göster:**
   ```bash
   tree knowledge/
   ```

2. **Her dosyanın durumunu raporla:**
   | Dosya | Durum | Bölüm Sayısı | Not |
   |-------|-------|--------------|-----|
   | compressor_screw.md | Mevcut | X | — |
   | compressor_piston.md | Yeni | X | — |
   | ... | ... | ... | ... |

3. **Eklediğin ekstra içerikleri listele** (brief dışı keşifler)

4. **Eksik kalan veya sorunlu bir şey varsa belirt**

---
## 🚀 Ek Yönerge: Keşif Modu

Bu brief kapsamı dışında, araştırma sırasında şunları bulursan:
- Yeni çözüm önerileri (brief'te olmayan)
- İlginç vaka çalışmaları (gerçek dünya ROI verileri)
- Güncel teknolojiler (AI-based leak detection, IoT monitoring)
- Bölgesel/sektörel spesifik bilgiler (Türkiye elektrik fiyatları, vb.)

→ Uygun dosyaya ekle veya yeni dosya oluştur.

**Bu brief ExergyLab kompresör modülünün knowledge base'i için tek kaynak noktasıdır.**

*Tahmini çalışma: ~15-20 MD dosyası, detaylı web araştırması gerektirir.*
