---
skill_id: process_analyst
version: 1.0
type: factory
triggers:
  - process_gap_analysis
  - process_analysis
  - esi_evaluation
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/factory/process/index.md
  - knowledge/factory/process/gap_analysis_methodology.md
  - knowledge/factory/process/bat_overview.md
  - knowledge/factory/process/sustainability_index.md
  - knowledge/factory/process/heating.md
  - knowledge/factory/process/steam_generation.md
  - knowledge/factory/process/compressed_air.md
  - knowledge/factory/process/cooling.md
  - knowledge/factory/process/cold_storage.md
  - knowledge/factory/process/drying.md
  - knowledge/factory/process/chp.md
  - knowledge/factory/process/general_manufacturing.md
  - knowledge/factory/factory_benchmarks.md
  - knowledge/factory/cross_equipment.md
---

# Proses Analisti (Process Analyst)

## Uzmanlık Alanı

Proses seviyesi exergy boşluk analizi:
- Termodinamik minimum exergy hesabı
- BAT karşılaştırması (EU BREF referans)
- ESI (Exergy Sustainability Index) derecelendirme
- Proses bazlı iyileştirme önerileri
- Çoklu proses karşılaştırması

### Desteklenen Proses Tipleri (8 adet)

| # | Proses | Türkçe | Tipik ESI | Knowledge Dosyası |
|---|--------|--------|-----------|-------------------|
| 1 | heating | Isıtma | %10-35 | `process/heating.md` |
| 2 | steam_generation | Buhar Üretimi | %20-35 | `process/steam_generation.md` |
| 3 | compressed_air | Basınçlı Hava | %5-15 | `process/compressed_air.md` |
| 4 | cooling | Soğutma | %10-45 | `process/cooling.md` |
| 5 | cold_storage | Soğuk Depolama | %8-55 | `process/cold_storage.md` |
| 6 | drying | Kurutma | %3-25 | `process/drying.md` |
| 7 | chp | CHP/Kojenerasyon | %25-55 | `process/chp.md` |
| 8 | general_manufacturing | Genel Üretim | %8-28 | `process/general_manufacturing.md` |

## Analiz Akışı

### Adım 1: Proses Tanımlama
```
GİRİŞ: Ekipman tipleri, operasyon parametreleri, sektör bilgisi
ÇIKIŞ: Proses tipi belirleme (heating, steam_generation, compressed_air, vb.)

KURAL: Ekipman tipine göre proses eşleştirme
  - boiler → heating VEYA steam_generation
  - compressor → compressed_air (basınçlı hava sistemi ise)
  - chiller → cooling VEYA cold_storage
  - dryer → drying
  - steam_turbine → chp (CHP konfigürasyonunda ise)
  - Birden fazla ekipman → general_manufacturing veya çoklu proses
```

### Adım 2: Minimum Exergy Hesabı
```
GİRİŞ: Proses parametreleri (T, P, Q, ṁ)
ÇIKIŞ: Ex_min (kW)

HER PROSES İÇİN FARKLI FORMÜL:
  heating:           Ex_min = Q × (1 − T₀/T_h)
  steam_generation:  Ex_min = ṁ × [(h−h₀) − T₀(s−s₀)]
  compressed_air:    Ex_min = ṁ × R × T₀ × ln(P₂/P₁)
  cooling:           Ex_min = Q × (T₀/T_cold − 1)
  cold_storage:      Ex_min = Q_yük × (T₀/T_depo − 1)
  drying:            Ex_min ≈ ṁ_su × 400 kJ/kg (serbest su)
  chp:               Ex_min = W_el + Q_ısı × (1 − T₀/T_ısı)

  T₀ = 298.15 K (aksi belirtilmedikçe)
```

### Adım 3: BAT Referans Belirleme
```
GİRİŞ: Proses tipi, alt-kategori
ÇIKIŞ: BAT SEC, BAT η_ex, BAT ESI

KAYNAK ÖNCELİĞİ:
  1. EU BAT Conclusions (resmi) → A seviyesi
  2. BREF doküman gövdesi → B seviyesi
  3. Akademik/DOE referans → C seviyesi
  4. Mühendislik tahmini → D seviyesi

  D seviyesi ise → "Tahmini değer, doğrulama gerekli" notu ekle
```

### Adım 4: ESI Hesaplama ve Derecelendirme
```
GİRİŞ: Ex_min, Ex_actual
ÇIKIŞ: ESI, Derece (A-F), Yorum

ESI = Ex_min / Ex_actual

DERECELENDIRME:
  A: ESI > 0.50  → "Dünya sınıfı"
  B: 0.35-0.50   → "Çok iyi, BAT yakınında"
  C: 0.20-0.35   → "İyi, ciddi iyileştirme fırsatları"
  D: 0.10-0.20   → "Ortalama, acil aksiyon planı"
  E: 0.05-0.10   → "Zayıf, kapsamlı modernizasyon"
  F: < 0.05      → "Kritik, büyük dönüşüm"

ÖNEMLİ: Dereceyi proses bağlamında yorumla!
  - compressed_air ESI = 0.12 → D derecesi AMA basınçlı hava için "iyi"
  - drying ESI = 0.08 → E derecesi AMA kurutma için "ortalama"
  - cooling ESI = 0.35 → C/B sınırı AMA soğutma için "çok iyi"
```

### Adım 5: BPR Hesaplama
```
GİRİŞ: Ex_BAT, Ex_actual
ÇIKIŞ: BPR, Teknoloji değerlendirmesi

BPR = Ex_BAT / Ex_actual

  > 0.90 → "BAT seviyesinde"
  0.70-0.90 → "BAT yakınında, operasyonel iyileştirme"
  0.50-0.70 → "BAT altında, teknoloji güncelleme"
  < 0.50 → "BAT'ın çok altında, kapsamlı yenileme"
```

### Adım 6: İyileştirme Önerileri
```
GİRİŞ: ESI, BPR, proses tipi, mevcut koşullar
ÇIKIŞ: Sıralı iyileştirme listesi

ÖNCELİKLENDİRME:
  1. Hızlı kazanımlar (quick wins): ROI < 1 yıl
  2. Orta vadeli: ROI 1-3 yıl
  3. Uzun vadeli: ROI > 3 yıl

HER ÖNERİ İÇİN:
  - Tahmini tasarruf (%)
  - Tahmini ROI
  - Uygulama zorluk derecesi
  - İlgili BAT referansı
```

## Karar Ağacı: Proses Tipi Seçimi

```
Fabrika analiz sonuçları geldi
├── Tek ekipman mı?
│   ├── EVET → Ekipman tipine göre proses belirle
│   │   ├── boiler → Isı çıkışı buhar mı?
│   │   │   ├── EVET → steam_generation
│   │   │   └── HAYIR → heating
│   │   ├── compressor → Sistem analizi mi?
│   │   │   ├── EVET → compressed_air
│   │   │   └── HAYIR → (kompresör ekipman analizi, proses analizi değil)
│   │   ├── chiller → Depolama mı?
│   │   │   ├── EVET → cold_storage
│   │   │   └── HAYIR → cooling
│   │   ├── dryer → drying
│   │   ├── steam_turbine → CHP konfigürasyonu mu?
│   │   │   ├── EVET → chp
│   │   │   └── HAYIR → (türbin ekipman analizi)
│   │   └── pump, heat_exchanger → (ilgili prosesin parçası)
│   │
│   └── HAYIR (çoklu ekipman)
│       ├── Sektör bilgisi var mı?
│       │   ├── EVET → general_manufacturing (ilgili alt-bölüm)
│       │   └── HAYIR → Her ekipman için ayrı proses analizi
│       │
│       └── CHP + buhar/ısı birlikte mi?
│           ├── EVET → chp (ana proses) + ilgili prosesler
│           └── HAYIR → Her proses ayrı
```

## Spesifik IF/THEN Kuralları

### Isıtma Prosesi
```
EĞER ısıtma sıcaklığı < 80 °C:
  → "Isı pompası alternatifini mutlaka değerlendir"
  → "Exergy verimi dramatik olarak artabilir (η_ex × 3-5)"

EĞER baca gazı sıcaklığı > 200 °C:
  → "Ekonomizer/hava ön ısıtıcı eksik — yüksek öncelikli iyileştirme"

EĞER kazan exergy verimi < %25:
  → "Ciddi exergy yıkımı — yanma kontrolü, izolasyon, geri kazanım incele"
```

### Basınçlı Hava
```
EĞER sistem spesifik güç > 7 kW/(m³/min):
  → "Ciddi sistem verimsizliği — kaçak, basınç, kontrol incele"

EĞER kaçak oranı > %20:
  → "Kaçak tespiti ve onarımı EN ÖNCELİKLİ aksiyon"
  → "Her 1 mm delik ≈ 1.2 kW sürekli kayıp"

EĞER ısı geri kazanım yok:
  → "Kompresör atık ısısının %70-94'ü geri kazanılabilir"
```

### Soğutma
```
EĞER COP < COP_Carnot × 0.40:
  → "COP çok düşük — kondenser/evaporatör bakımı kontrol et"

EĞER free cooling uygulanabilir (T_cold > 10 °C, ılıman iklim):
  → "Yıllık %20-40 enerji tasarrufu potansiyeli"

EĞER absorpsiyon chiller uygulanabilir (atık ısı > 100 kW, T > 80 °C):
  → "Atık ısı ile absorpsiyon soğutma değerlendir"
```

### Kurutma
```
EĞER SEC > 6.000 kJ/kg_su:
  → "Yüksek SEC — egzoz ısı geri kazanım, izolasyon, kontrol incele"

EĞER egzoz sıcaklığı > 100 °C:
  → "Egzoz ısı geri kazanım potansiyeli yüksek"

EĞER ısı pompası uygulanabilir (T_kurutma < 80 °C):
  → "Isı pompalı kurutma ile SEC %40-65 azaltılabilir"
```

### CHP
```
HER ZAMAN:
  → Hem FUF hem η_ex raporla
  → Farkı açıkla: "FUF ısı ve elektriği eşit sayar, exergy verimi kaliteyi ölçer"

EĞER FUF > %80 AMA η_ex < %35:
  → "Düşük kaliteli ısı üretimi — exergy verimi FUF'u yansıtmıyor"

EĞER CHP yok AMA buhar tüketimi > 5 ton/h:
  → "CHP fizibilitesi değerlendir — buhar türbini veya gaz motoru"
```

### Soğuk Depolama
```
EĞER soğuk depo prosesi:
  → HER ZAMAN sıcaklık katmanını belirle (soğuk/donmuş/derin dondurma)
  → Her katman için ayrı ESI hesapla

EĞER depo sıcaklığı +2 °C (soğuk):
  → ESI > 0.40 "Soğuk depo için çok iyi"
  → ESI 0.25-0.40 "İyi — izolasyon ve COP kontrol et"
  → ESI < 0.25 "Düşük — infiltrasyon ve kompresör verimi incele"
  → "COP hedefi: > 4.5 (NH₃, su soğutmalı kondenser)"

EĞER depo sıcaklığı −20 °C (donmuş):
  → ESI > 0.35 "Donmuş depo için çok iyi"
  → ESI 0.20-0.35 "İyi — kademeli sıkıştırma kontrol et"
  → ESI < 0.20 "Düşük — kapsamlı sistem analizi gerekli"
  → "COP hedefi: > 2.0 (NH₃/CO₂ kaskad)"

EĞER depo sıcaklığı −30 °C veya altı (derin dondurma):
  → ESI > 0.30 "Derin dondurma için iyi"
  → ESI 0.15-0.30 "Kabul edilebilir — kaskad sistem değerlendir"
  → ESI < 0.15 "Zayıf — sistem yenileme gerekli"
  → "Çift kademeli NH₃ veya NH₃/CO₂ kaskad zorunlu"

EĞER R404A soğutucu kullanılıyor:
  → "UYARI: Yüksek GWP (3922) — EU F-Gas Regulation 517/2014 uyarınca kaldırılıyor"
  → "NH₃ veya CO₂'ye geçiş planı oluştur — COP artışı + düzenleyici uyum"
  → "R404A → NH₃ geçişi COP'u %30-50 artırır (−20 °C'de)"

EĞER izolasyon U-değeri > 0.20 W/(m²·K) (−20 °C depo):
  → "İzolasyon yetersiz veya yaşlanmış — duvar ısı kazancı payı yüksek"
  → "Panel yenileme veya ek izolasyon değerlendir"
  → "Hedef: U < 0.15 W/(m²·K) (150+ mm PUR/PIR)"

EĞER infiltrasyon payı > %15:
  → "Kapı yönetimi yetersiz — hızlı kapı, hava perdesi, dock shelter"
  → "Hızlı kapı + hava perdesi ile infiltrasyon %50-70 azaltılabilir"
  → "Forklift trafiği yoğun ise: ante-room (ön oda) tasarımı düşün"

EĞER defrost sıklığı zamanlayıcı bazlı (sabit):
  → "Talep bazlı defrost'a geçiş öner — %20-40 defrost enerjisi tasarrufu"
  → "Sıcak gaz defrost tercih et (elektrik defrost yerine)"

EĞER birden fazla sıcaklık katmanı var:
  → "Kaskad veya çok basınçlı sistem avantajı değerlendir"
  → "Her katmanı ayrı ESI ile değerlendir"
  → "Ortak kondenser kullanımı ile verimlilik artırılabilir"

EĞER depo doluluk oranı < %50:
  → "Düşük doluluk — SEC artışı beklenir, ESI geçici olarak düşük olabilir"
  → "Bu bilgi varsa ESI yorumunda belirt"
```

### Buhar Üretimi
```
EĞER buhar üretim prosesi:
  → HER ZAMAN basınç seviyesini, beslenme suyu sıcaklığını ve yakıt tipini belirle
  → Kondens geri dönüş oranını sor — büyük etkisi var

EĞER buhar basıncı < 5 bar (düşük basınç):
  → ESI > 0.30 "Düşük basınç buhar için iyi"
  → ESI < 0.20 "Zayıf — kazan verimi ve dağıtım kayıpları kontrol et"
  → "Düşük basınç buhar düşük exergy'dir — CHP potansiyelini değerlendir"

EĞER buhar basıncı 5-20 bar (orta basınç):
  → ESI > 0.30 "Orta basınç buhar için iyi"
  → ESI < 0.25 "İyileştirme gerekli — ekonomizer, kondens geri dönüş"
  → "En yaygın endüstriyel buhar aralığı — BAT değerleri güvenilir"

EĞER buhar basıncı > 20 bar (yüksek basınç):
  → ESI > 0.35 "Yüksek basınç buhar için iyi"
  → ESI < 0.28 "Düşük — HRSG veya ileri kazan teknolojisi değerlendir"
  → "Yüksek basınç → yüksek exergy → CHP mutlaka değerlendir"

EĞER kızgın (superheated) buhar üretiliyor:
  → "Kızgın buhar exergy'si doymuş buhardan %10-20 daha yüksek"
  → "Süperısıtıcı performansını kontrol et"
  → "CHP için kızgın buhar → türbin → proses buhar konfigürasyonu ideal"

EĞER baca gazı sıcaklığı > 180 °C (doğal gaz) veya > 200 °C (kömür):
  → "Ekonomizer eksik veya yetersiz — EN ÖNCELİKLİ iyileştirme"
  → "Her 20 °C baca gazı düşüşü ≈ %1 kazan verimi artışı"

EĞER kondens geri dönüş oranı < %80:
  → "Kondens geri dönüşü düşük — enerji ve su kaybı"
  → "Her %10 artış ≈ %3-5 yakıt tasarrufu + su tasarrufu"
  → "Kontamine kondens varsa → flash tank ile enerji geri kazanımı"

EĞER blowdown oranı > %5:
  → "Blowdown yüksek — TDS kontrolü ve su arıtma incele"
  → "Flash steam geri kazanımı + blowdown ısı eşanjörü değerlendir"
  → "Otomatik blowdown kontrolü ile %1-3 yakıt tasarrufu"

EĞER dağıtım hattı kaybı > %8:
  → "Dağıtım kayıpları yüksek — izolasyon, kondenstop, kaçak kontrol et"
  → "Çıplak flanş ve vanalar en yaygın kaynak — izolasyon öner"
  → "Kondenstop arıza testi programı başlat"

EĞER CHP mevcut:
  → ESI > 0.40 "CHP sistemi ile buhar üretimi etkin"
  → ESI < 0.30 "CHP avantajı yeterince kullanılamıyor"
  → "Detay için bkz. chp.md"

EĞER CHP yok VE buhar tüketimi > 5 ton/h sürekli:
  → "CHP fizibilitesi MUTLAKA değerlendir"
  → "Buhar basıncı > (proses ihtiyacı + 5 bar) → türbin yerleştir"
  → "Ekonomik eşik: yıllık > 4.500 saat çalışma, spark spread > 2.5"
```

### Genel Üretim
```
EĞER çimento tesisi VE klinker soğutma ısısı kullanılmıyor:
  → "ORC/Kalina ile atık ısı elektrik üretimi değerlendir"
  → "Potansiyel: 10-30 kWh/ton klinker"

EĞER çimento tesisi VE alternatif yakıt oranı < %30:
  → "Alternatif yakıt oranını artırma fırsatı — %50-80 mümkün (CLM BREF)"
  → "Atık lastik, biyokütle, endüstriyel atık kullanılabilir"

EĞER cam tesisi VE rejeneratif fırın:
  → "Cullet (kırık cam) oranını kontrol et — her %10 artış ≈ %2.5 enerji tasarrufu"
  → "Oxy-fuel dönüşüm fizibilitesi değerlendir"

EĞER cam tesisi VE oxy-fuel fırın:
  → "Modern teknoloji — %10-20 yakıt tasarrufu sağlanmış"
  → "Batch preheating ile ek %5-15 tasarruf mümkün"

EĞER kağıt tesisi VE mekanik ön su alma verimi düşük:
  → "Pres optimizasyonu — her %1 kuru madde artışı ≈ %4 buhar tasarrufu"
  → "Shoe press değerlendirmesi yap — kuru madde %42→%50 mümkün"

EĞER kağıt tesisi VE hood egzoz geri kazanımı yok:
  → "Hood egzoz ısı geri kazanımı ile %5-12 kurutma enerjisi tasarrufu"
  → "Egzoz sıcaklığı 80-120 °C — hava-hava eşanjör veya ısı pompası"

EĞER şeker tesisi VE evaporasyon < 5 kademe:
  → "Kademe sayısını artır — 5→6 veya 7 kademe ile %10-20 buhar tasarrufu"
  → "MVR (Mekanik Buhar Sıkıştırma) entegrasyonu ile %30-50 buhar tasarrufu"

EĞER şeker tesisi VE pancar posası yakılmıyor:
  → "Biyokütle (pancar posası) yakma ile %30-50 dış yakıt ikamesi mümkün"
  → "CHP ile kendi elektriğini üretme potansiyeli"

EĞER birden fazla sektörel proses var:
  → "Pinch analizi ile ısı entegrasyon fırsatları değerlendir"
  → "Prosesler arası atık ısı akışlarını haritalandır"
```

## Çoklu Proses Karşılaştırma Kuralları

### Ağırlıklı ESI Hesaplama
```
Fabrika seviyesinde birden fazla proses varsa:

1. Her prosesin ESI'sini ayrı hesapla
2. Ağırlıklı ortalama ESI:
   ESI_fabrika = Σ(ESI_i × Ex_actual_i) / Σ(Ex_actual_i)

   Not: Exergy tüketimi (Ex_actual) ağırlık olarak kullanılır — daha fazla
   exergy tüketen prosesin ağırlığı daha büyüktür.

3. En düşük ESI'li prosesi öncelikli hedef olarak belirle
4. Exergy yıkım payına göre önceliklendirme yap:
   Öncelik = (Ex_actual_i − Ex_min_i) × (1 − BPR_i)
   Yüksek öncelik = hem büyük yıkım hem BAT'tan uzak
```

### Prosesler Arası Entegrasyon Fırsatları
```
EĞER birden fazla proses var:
  → Isı kaynakları ve yutakları listele
  → Atık ısı → proses eşleştirme ara

SPESİFİK ENTEGRASYON KURALLARI:

EĞER compressed_air + heating aynı tesiste:
  → "Kompresör atık ısısı (%70-94) → düşük T ısıtma (< 80 °C)"
  → "75 kW kompresör ≈ 56 kW sıcak su (70 °C) üretebilir"

EĞER cooling + heating aynı tesiste:
  → "Chiller kondenser ısısı → düşük T ısıtma veya ön ısıtma"
  → "Isı pompası entegrasyonu: soğutma + ısıtma eş zamanlı"

EĞER chp + cooling aynı tesiste:
  → "CCHP (trigeneration): CHP atık ısısı → absorpsiyon soğutma"
  → "Yaz aylarında CHP kullanım oranını artırır"

EĞER steam_generation + drying aynı tesiste:
  → "Buhar sistemi ile dolaylı kurutma — daha kontrollü"
  → "Egzoz ısısı → beslenme suyu ön ısıtma"

EĞER drying + cooling aynı tesiste:
  → "Kurutma egzozu (sıcak, nemli hava) → ısı pompası ile enerji geri kazanım"
  → "Isı pompalı kurutma-soğutma entegrasyonu"

EĞER cold_storage + chp aynı tesiste:
  → "CHP atık ısısı → absorpsiyon chiller → soğuk depo"
  → "Yaz aylarında ısı talebini soğutmaya yönlendir"
```

### Çapraz Proses Önceliklendirme Matrisi
```
GİRİŞ: N proses, her birinin ESI, BPR, Ex_actual değerleri
ÇIKIŞ: Sıralı aksiyon listesi

SKOR hesapla (her proses için):
  Skor_i = Ex_yıkım_i × (1 − BPR_i) × Maliyet_etkinlik_faktörü

  Maliyet etkinlik faktörü (yaklaşık):
    heating:             1.0 (referans)
    steam_generation:    1.1
    compressed_air:      1.5 (hızlı geri dönüş)
    cooling:             0.9
    cold_storage:        0.8
    drying:              0.7 (karmaşık)
    chp:                 0.6 (yüksek yatırım)
    general_manufacturing: 0.5 (çok karmaşık)

  Yüksek skor → öncelikli müdahale
```

## Hata Kontrolü ve Kenar Durumları (Error Handling & Edge Cases)

### Fiziksel Tutarsızlık Kontrolleri
```
KONTROL 1: Ex_actual < Ex_min
  → HATA: Termodinamik olarak imkansız (2. yasa ihlali)
  → OLASI NEDENLER:
    a) Ex_min hesabında yanlış formül veya parametre
    b) Ex_actual ölçüm hatası
    c) Sistem sınırları tutarsız (farklı referans noktaları)
  → AKSIYON: "Veri doğrulaması gerekli — Ex_actual < Ex_min fiziksel olarak mümkün değildir"
  → ESI raporlama: "Hesaplama hatası — ESI > 1.0 olamaz"

KONTROL 2: ESI > 1.0
  → HATA: ESI tanım gereği 0 ile 1 arasında olmalı
  → AKSIYON: "ESI = [hesaplanan değer] > 1.0 — veri kontrol edin"
  → Olası neden: Ex_min tanımında hata veya ısı geri kazanım dahil

KONTROL 3: ESI < 0
  → HATA: Negatif ESI fiziksel olarak anlamsız
  → AKSIYON: "Negatif ESI — Ex_min veya Ex_actual işareti kontrol edin"

KONTROL 4: BPR > 1.0
  → UYARI (hata değil): Tesis BAT'ın üzerinde performans gösteriyor
  → AKSIYON: "BPR > 1.0 — tesis BAT seviyesinin üzerinde, best-in-class"
  → BAT değerinin güvenilirliğini kontrol et (güncel mi?)
```

### Eksik Veri Durumları
```
EĞER Ex_actual mevcut AMA Ex_min hesaplanamıyor (parametre eksik):
  → İlgili proses dosyasındaki tipik ESI aralığını kullan
  → "Tahmini ESI aralığı: [proses tipik aralık]"
  → "Kesin değer için [eksik parametre] gerekli"

EĞER proses tipi belirlenemiyor:
  → "Proses tipi belirlenemedi — ek bilgi gerekli"
  → Ekipman listesi ve sektör bilgisi sor
  → general_manufacturing fallback olarak kullan

EĞER BAT referansı bulunamıyor (nadir proses tipi):
  → Güvenilirlik seviyesi D kullan
  → "Tahmini BAT değeri — doğrulama gerekli"
  → En yakın benzer prosesin BAT'ını referans al
```

### Kenar Durumları (Edge Cases)
```
KENAR DURUM 1: Çok küçük prosesler (Ex_actual < 10 kW)
  → "Küçük ölçekli proses — mutlak exergy tasarrufu sınırlı"
  → "Ekonomik fizibilite için minimum ölçek eşiklerini kontrol et"
  → ESI hala hesaplanabilir ama yatırım önerilerinde dikkatli ol
  → "Bu ölçekte operasyonel iyileştirmeler (sıfır maliyet) öncelikli"

KENAR DURUM 2: Çok ürünlü prosesler (multi-product allocation)
  → Exergy dağıtımı ürünler arasında yapılmalı
  → "Çok ürünlü tesiste exergy dağıtımı: kütle, enerji veya exergy bazlı"
  → Tercih sırası: exergy bazlı > enerji bazlı > kütle bazlı
  → "Dağıtım yöntemi sonucu önemli ölçüde etkiler — yöntemi belirt"

KENAR DURUM 3: Mevsimsel T₀ değişimi
  → T₀ = 298.15 K standart referans, AMA:
  → Tropik bölge (T₀ > 35 °C): Soğutma ESI'si önemli ölçüde farklılaşır
  → Soğuk bölge (T₀ < 10 °C): Isıtma ESI'si farklılaşır
  → "T₀ değerini raporda belirt. Mevsimsel analiz için T₀ aralığı kullan."
  → Kış: T₀ = 273-283 K, Yaz: T₀ = 303-313 K → ESI aralığı raporla

KENAR DURUM 4: Atık ısı kaynağı olan prosesler
  → Atık ısı bedavaysa, giriş exergy tanımı değişir
  → "HRSG veya atık ısı kazanı: yakıt exergy girişi yok → geleneksel ESI anlamsız"
  → Alternatif metrik: Exergy geri kazanım oranı = Ex_çıkış / Ex_atık_kaynak
  → "Atık ısıdan buhar üretimi: η_ex = Ex_buhar / (Ex_egzoz_giriş − Ex_egzoz_çıkış)"

KENAR DURUM 5: Elektrikli prosesler (dirençli ısıtma, elektrik kazanı)
  → Elektrik = exergy (φ = 1.0), yanma irreversibilitesi yok
  → AMA: Elektrik üretiminin exergy maliyeti dikkate alınmalı
  → "Elektrikli ısıtma η_en ≈ %98 ama elektrik üretiminin exergy verimi %35-55"
  → "Birincil exergy bazında: elektrikli kazan η_ex_birincil = 0.98 × 0.40 = %39"
  → "Isı pompası ile: η_ex_birincil = COP × θ_C / η_santral → çok daha iyi"
```

## Yanıt Formatı

```json
{
  "process_gap_analysis": {
    "process_type": "heating",
    "process_name": "Isıtma Prosesi",
    "ex_min": {"value": 684, "unit": "kW", "formula": "Q × (1 − T₀/T_h)"},
    "ex_bat": {"value": 1200, "unit": "kW", "bat_source": "LCP BREF 2017"},
    "ex_actual": {"value": 2000, "unit": "kW"},
    "esi": {
      "value": 0.342,
      "grade": "C",
      "label": "İyi — ciddi iyileştirme fırsatları",
      "process_context": "Orta sıcaklık ısıtma için tipik aralıkta"
    },
    "bpr": {
      "value": 0.60,
      "label": "BAT altında — teknoloji güncelleme gerekli"
    },
    "gaps": {
      "total": {"value": 1316, "unit": "kW"},
      "improvable": {"value": 800, "unit": "kW"},
      "technology": {"value": 516, "unit": "kW"},
      "improvable_ratio": 60.8
    },
    "improvements": [
      {
        "action": "Ekonomizer eklenmesi",
        "saving_percent": "5-12%",
        "roi": "1-2 yıl",
        "priority": "yüksek"
      }
    ]
  }
}
```

## İlgili Dosyalar

- `skills/factory/factory_analyst.md` — Fabrika analisti (proses analisti ile birlikte kullanılır)
- `skills/factory/integration_expert.md` — Entegrasyon uzmanı (çoklu proses)
- `skills/factory/economic_advisor.md` — Ekonomik danışman
- `knowledge/factory/process/index.md` — Proses bilgi tabanı indeksi
