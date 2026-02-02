---
title: "EGM vs Exergoekonomik Karsilastirma (EGM vs Exergoeconomic Comparison)"
category: factory
equipment_type: factory
keywords: [EGM, exergoekonomik, SPECO, Tsatsaronis, termodinamik optimizasyon, ekonomik optimizasyon, maliyet]
related_files: [factory/entropy_generation/overview.md, factory/entropy_generation/fundamentals.md, factory/economic_analysis.md, factory/life_cycle_cost.md]
use_when: ["EGM ve exergoekonomik yontemler karsilastirilacakken", "Optimizasyon yontemi secimi yapilacakken", "Hibrit yaklasim planlanacakken"]
priority: medium
last_updated: 2026-02-01
---

# EGM vs Exergoekonomik Karsilastirma (EGM vs Exergoeconomic Comparison)

> Son guncelleme: 2026-02-01

## Genel Bakis

Endustriyel sistemlerin optimizasyonunda iki temel yaklasim one cikar: Adrian Bejan'in **Entropi Uretim Minimizasyonu** (Entropy Generation Minimization -- EGM) ve George Tsatsaronis'in **Exergoekonomik Analiz** (Exergoeconomic Analysis) yontemi. EGM, termodinamigin ikinci yasasina dayali saf fiziksel bir optimizasyon sunarken; exergoekonomik analiz, exergy kavramini maliyet tahsisi (cost allocation) icin bir temel olarak kullanarak termodinamik ile ekonomiyi birlestiren butunlesik bir karar destek araci sunar.

Bu dosya, her iki yontemi derinlemesine karsilastirarak muhendislerin proje asamasina ve ihtiyacina gore dogru yontemi -- veya hibrit bir yaklasimi -- secmesine rehberlik eder.

---

## 1. Iki Yaklasimin Felsefi Farki (Philosophical Difference)

### 1.1 EGM: Termodinamik Optimizasyon (Thermodynamic Optimization)

EGM, bir sistemi **saf termodinamik perspektiften** optimize eder. Amaci, sistem icerisindeki toplam entropi uretimini (S_gen) minimize etmektir. Maliyet, yatirim kisiti veya piyasa kosullari bu yaklasimda dogrudan yer almaz.

**Temel soru:** "Termodinamik acisindan mumkun olan en iyi tasarim nedir?"

**Fiziksel sezgi:** EGM, bir sistemi dogaya en yakin -- yani en az israf yapan -- noktaya tasimaya calisir. Tersinir (reversible) surec asla ulasilamayan ideal limittir; EGM bu limite mumkun oldugunca yaklasmayi hedefler. Bu, bir aracin "en dusuk yakit tuketimi icin optimum hiz nedir?" sorusuna benzer -- maliyet, konfor veya zaman hesaba katilmaz, yalnizca fizik konusur.

EGM'nin temel ozelliklerini soyle ozetleyebiliriz:

- **Amac fonksiyonu (Objective function):** min S_gen [kW/K]
- **Sonuc:** Termodinamik acisindan optimum tasarim parametreleri
- **Maliyeti dogrudan dikkate almaz** -- ekonomik veri gerektirmez
- **Evrensel gecerlilik:** Piyasa kosullarindan bagimsiz sonuclar uretir
- **Basitlik:** Fiziksel sezgiye dayali, zarif matematiksel formalizm
- **Sinirlilik:** Ekonomik gercekligi goremez -- S_gen'i minimuma indiren tasarim cok pahali olabilir

### 1.2 Exergoekonomik: Termoekonomik Optimizasyon (Thermoeconomic Optimization)

Exergoekonomik analiz, termodinamik ile ekonomiyi **exergy** kavramini kopru olarak kullanarak birlestiren butunlesik bir yaklasimdir. Amaci, toplam maliyeti (yatirim + yakit + cevre) minimize etmektir.

**Temel soru:** "En dusuk maliyetli tasarim nedir?"

**Fiziksel sezgi:** Exergoekonomik analiz, surecin termodinamik performansini iyilestirmenin "bedelini" sorgular. Bir esanjorun yuzey alanini artirmak S_gen'i azaltir ama yatirim maliyetini arttirir. Bu iki karsi etkinin optimum dengesi, termodinamik degil ekonomik bir sorundur. Exergoekonomik analiz tam olarak bu dengeyi bulur.

Temel ozellikler:

- **Amac fonksiyonu:** min C_total = C_fuel + C_investment + C_environmental [EUR/saat]
- **Sonuc:** Maliyet acisindan optimum tasarim ve isletme parametreleri
- **Exergy'yi maliyet tahsisi temeli olarak kullanir** -- her exergy akisina parasal deger atar
- **Piyasaya bagimli:** Enerji fiyatlari, faiz oranlari, ekipman maliyetleri sonuclari etkiler
- **Karmasiklik:** Daha fazla veri ve hesaplama gerektirir
- **Karar destegi:** Dogrudan yatirim kararlarina rehberlik eder

### 1.3 Temel Felsefe Tablosu (Fundamental Philosophy Comparison)

| Ozellik | EGM (Bejan) | Exergoekonomik (Tsatsaronis) |
|---|---|---|
| Amac | min S_gen | min C_total |
| Optimizasyon degiskeni | Entropi uretimi [kW/K] | Maliyet [EUR/saat] |
| Cikti | Optimum tasarim parametreleri | Optimum maliyet dengeleri |
| Sorulan soru | "En az entropi?" | "En dusuk maliyet?" |
| Temel kitap | Bejan (1996) | Tsatsaronis (1993), Bejan et al. (1996) |
| Guclu yan | Fiziksel sezgi, basitlik | Ekonomik karar destegi |
| Zayif yan | Maliyeti gormezden gelir | Karmasik, veri yogun |
| Veri gereksinimi | Termodinamik ozellikler | Termodinamik + ekonomik veriler |
| Sonuc gecerliligi | Evrensel (fizik degismez) | Piyasaya bagimli (fiyatlar degisir) |
| Uygun asama | On tasarim (conceptual) | Detayli tasarim (detailed engineering) |
| Hesaplama karmasikligi | Dusuk-orta | Orta-yuksek |

---

## 2. SPECO Yontemi (Specific Exergy Costing)

### 2.1 Tsatsaronis'in SPECO Metodu

SPECO (Specific Exergy Costing), Tsatsaronis ve Lazzaretto tarafindan gelistirilen sistematik bir exergoekonomik analiz metodolojisidir. Yontem, termodinamik sistemdeki her exergy akisina bir parasal deger (specific cost, c) atayarak maliyet olusumunu takip eder.

**Fiziksel sezgi:** Bir fabrikada uretilen buhar, farkli sicaklik ve basinclarda farkli "deger"e sahiptir. 10 bar doymus buhar, 2 bar doymus buhardan daha yuksek exergy'ye sahiptir -- dolayisiyla daha "degerli"dir. SPECO, bu fiziksel degeri parasal degere cevirir ve her bilesen icerisinde maliyetin nasil olusup birikerek aktigi gosterir.

SPECO ucuncu bir soru sorar: "Her kilojoulluk exergy ne kadara mal oluyor ve maliyet nerede olusup nerede birikir?"

**Maliyet dengesi (Cost balance):** Bir bilesene giren exergy akislarinin toplam maliyeti ile bilesene ait yatirim maliyet hizi (Ż), o bilesenden cikan exergy akislarinin toplam maliyetini ve kayip maliyetini verir:

**Fiziksel sezgi:** Maliyet dengesi, enerji korunumu gibi dusunulebilir -- ancak burada korunan sey enerji degil maliyettir. Bir bilesene giren "maliyet akislari" toplami, cikan "maliyet akislari" toplamina esittir. Bilesen icindeki exergy yikimi ek bir maliyet olusturur ve bu maliyet urune yansir.

```
Maliyet Dengesi (Cost Balance):

  sum(C_out) + C_loss = sum(C_in) + Z_dot

Burada:
  C_out  = cikan exergy akislarinin maliyet hizi [EUR/saat]
  C_loss = kayip exergy akisinin maliyet hizi [EUR/saat]
  C_in   = giren exergy akislarinin maliyet hizi [EUR/saat]
  Z_dot  = bilesene ait toplam yatirim maliyet hizi [EUR/saat]
         = (CI + OM) / isletme saati
  CI     = sermaye yatirimi (Capital Investment) [EUR]
  OM     = isletme-bakim maliyeti (Operation & Maintenance) [EUR]
```

Her exergy akisinin maliyet hizi, o akisin exergy hizi ile birim exergy maliyetinin carpimi olarak yazilir:

**Fiziksel sezgi:** Bir akisin "maliyeti", o akisin tasidiginin exergy miktari ile her birim exergy'nin birim fiyatinin carpimidir. Tipki bir sivi icin "toplam fiyat = litre x birim fiyat" mantigi gibi.

```
Exergy Akisi Maliyet Hizi:

  C_dot_k = c_k x Ex_dot_k

Burada:
  C_dot_k = k-inci akisin maliyet hizi [EUR/saat]
  c_k     = k-inci akisin birim exergy maliyeti [EUR/kJ] veya [EUR/GJ]
  Ex_dot_k = k-inci akisin exergy hizi [kW]
```

### 2.2 Exergoekonomik Faktor (Exergoeconomic Factor, f)

Exergoekonomik faktor, bir bilesen icin **yatirim maliyeti** ile **exergy yikim maliyeti** arasindaki dengeyi gosteren en onemli karar parametresidir.

**Fiziksel sezgi:** f faktoru su soruyu yanitlar: "Bu bilesene harcadigimiz paranin ne kadari ekipmanin kendisi icin, ne kadari o ekipmanin yiktigi exergy icin?" Yuksek f, pahali ama termodinamik acidan iyi bir bilesen anlamina gelir. Dusuk f, ucuz ama cok exergy yikan bir bilesen anlamina gelir.

```
Exergoekonomik Faktor:

  f = Z_dot / (Z_dot + C_dot_D)

Burada:
  f       = exergoekonomik faktor [boyutsuz, 0-1 arasi]
  Z_dot   = yatirim maliyet hizi [EUR/saat]
  C_dot_D = exergy yikim maliyet hizi [EUR/saat]

Yorumlama:
  f > 0.5  -->  Yatirim maliyeti baskin
               --> Daha ucuz ekipman dusunulebilir
               --> Termodinamik iyilestirme maliyet-etkin OLMAYABILIR

  f < 0.5  -->  Exergy yikim maliyeti baskin
               --> Termodinamik performansi iyilestir
               --> Daha iyi ekipman yatirimi karsiligini verir

  f ≈ 0.5  -->  Denge noktasina yakin
               --> Detayli optimizasyon gerektirir

Tipik degerler (endustriyel ekipmanlar):
  Esanjor (Heat Exchanger)  : f ≈ 0.35 - 0.55
  Turbin                    : f ≈ 0.50 - 0.75
  Kompresor                 : f ≈ 0.40 - 0.60
  Kazan (Boiler)            : f ≈ 0.20 - 0.40
  Chiller                   : f ≈ 0.30 - 0.50
  Pompa                     : f ≈ 0.45 - 0.65
```

### 2.3 Exergy Yikim Maliyeti (Exergy Destruction Cost)

Exergy yikim maliyeti, bir bilesen icerisinde yikilan exergy'nin parasal degerini temsil eder. Bu, EGM ile exergoekonomik analiz arasindaki en onemli kopru kavramidir.

**Fiziksel sezgi:** Bir kazanda yanma sirasinda uretilen entropi (S_gen), Gouy-Stodola teoremine gore exergy yikiyor. Bu yikilan exergy'nin bir "fiyati" var -- cunku o exergy'yi uretmek icin yakit yakildigi. Exergy yikim maliyeti, "bu tersinmezlik bize ne kadara mal oluyor?" sorusunu yantilar.

```
Exergy Yikim Maliyeti:

  C_dot_D = c_fuel x Ex_dot_D

Burada:
  C_dot_D = exergy yikim maliyet hizi [EUR/saat]
  c_fuel  = yakit exergy'sinin birim maliyeti [EUR/kJ]
  Ex_dot_D = yikilan exergy hizi [kW]

Gouy-Stodola baglantisi ile:
  Ex_dot_D = T_0 x S_dot_gen

Dolayisiyla:
  C_dot_D = c_fuel x T_0 x S_dot_gen

Burada:
  T_0       = cevre sicakligi [K], tipik 298.15 K (25 °C)
  S_dot_gen = entropi uretim hizi [kW/K]
```

### 2.4 SPECO vs EGM Baglantisi (The Bridge)

EGM ve exergoekonomik analiz, Gouy-Stodola teoremi uzerinden matematiksel olarak birbirine baglidir. Ancak exergoekonomik analiz, EGM'nin uzerine bir ekonomik katman ekler.

**Fiziksel sezgi:** EGM "entropi uretimini azalt" der ve burada durur. SPECO ayni entropi uretimini alir, parasal degere cevirir ve sonra sorar: "Bu entropi uretimini azaltmak icin yapacagim yatirim, tasarruf ettigim exergy yikim maliyetinden daha mi az?" Bu, fiziksel optimumun otesinde ekonomik optimumu arar.

```
EGM ve SPECO Karsilastirmasi:

  EGM:    min S_dot_gen
          --> I = T_0 x S_dot_gen  (exergy yikimini minimize et)
          --> Sonuc: Termodinamik optimum

  SPECO:  min (C_dot_D + Z_dot)
          --> C_dot_D = c_fuel x T_0 x S_dot_gen
          --> Z_dot = f(tasarim parametreleri)
          --> Sonuc: Ekonomik optimum

Fark:
  - EGM yalnizca C_dot_D'yi (dolayli olarak) minimize eder
  - SPECO, C_dot_D + Z_dot toplamini minimize eder
  - SPECO, EGM'nin goremedigi yatirim maliyeti boyutunu ekler
  - Ekonomik optimum her zaman termodinamik optimumdan "kotu"dur
    (daha fazla S_gen uretir) ama daha ucuzdur
```

Bu baglanti, grafik olarak su sekilde gosterilir:

```
Maliyet                      Toplam maliyet (C_total)
  ^                         /
  |                        /  .
  |     Z_dot            /  .   .    C_dot_D (exergy yikim maliyeti)
  |       /            /  .       .
  |      /           *.              .
  |     /          . |  .               .
  |    /         .   |    .                 .
  |   /        .     |      .
  |  /       .       |
  | /      .         |
  |/     .           |
  +-----|------------|-----------------------> Tasarim parametresi
        |            |                         (ornegin HX alani)
   Ekonomik     Termodinamik
    optimum      optimum (EGM)
```

**Fiziksel sezgi:** Grafik gosteriyor ki yatirim maliyeti (Z_dot) arttikca exergy yikim maliyeti (C_dot_D) azalir. Toplam maliyet egrisinin minimumu ekonomik optimumdur. EGM optimumu ise C_dot_D'nin minimumudur -- ancak bu noktada Z_dot cok yuksektir. Ekonomik optimum daima EGM optimumunun "solunda" (daha az yatirim, daha fazla S_gen) yer alir.

---

## 3. Guclu ve Zayif Yanlar Karsilastirmasi (Strengths and Weaknesses)

### 3.1 EGM Guclu Yanlari

1. **Basitlik ve zarafet (Simplicity):** EGM, tek bir amac fonksiyonuna (S_gen) odaklanir. Ekonomik veri, piyasa tahminleri veya maliyet korelasyonlari gerektirmez.

2. **Evrensel gecerlilik (Universality):** Fizik yasalari degismez. EGM sonuclari 2026'da da 2050'de de gecerlidir. Enerji fiyatlari degisse bile termodinamik optimum ayni kalir.

3. **Fiziksel sezgi (Physical insight):** EGM, muhendise sistemin "nerede ve neden israf yaptigini" anlatir. Bu kavrayis, deneyimsiz muhendisler icin bile degerlidir.

4. **On tasarim icin ideal (Conceptual design):** Detayli maliyet verisi olmadan bile tasarim alternatiflerini karsilastirmak icin guclur bir aractir.

5. **Egitim degeri (Educational value):** Termodinamigin ikinci yasasini pratik muhendislige baglayan en dogal koprudur.

6. **Hesaplama hizi (Computational speed):** Ekonomik veri ve iterasyon gerektirmedigi icin daha hizli sonuc verir.

### 3.2 EGM Zayif Yanlari

1. **Ekonomik korluk (Economic blindness):** S_gen'i minimize eden esanjor sonsuz buyuklukte olabilir -- fiziken optimal ama ekonomik olarak imkansiz.

2. **Yatirim kisitlarini goremez (Investment constraints):** Gercek dunyada butce sinirlidir. EGM, "bu iyilestirme ne kadara mal olur?" sorusunu yanytlayamaz.

3. **Cok bilesenli sistemlerde zorluk (Multi-component complexity):** Bir bilesendeki S_gen azaltmasi baska bilesende artisa neden olabilir. EGM bunu gorur ancak maliyet trade-off'unu goremez.

4. **Karar destegiinin sinirliigi (Limited decision support):** "Hangisine yatirim yapmaliyim?" sorusuna dogrudan yanit veremez.

5. **Isletme maliyetlerini iceremez:** Bakim, isgucu, cevre maliyetleri gibi faktorler kapsam disidir.

### 3.3 Exergoekonomik Guclu Yanlari

1. **Dogrudan ekonomik optimum (Direct economic optimum):** Sonuclar EUR/saat veya EUR/yil cinsinden -- yonetim ve finans ekipleri icin anlasilir.

2. **Yatirim-isletme dengesi (Investment-operation balance):** f faktoru ile "daha iyi ekipman mi yoksa daha ucuz ekipman mi?" sorusuna net yanitlar verir.

3. **Bilesen bazinda karar destegi (Component-level decisions):** Her bilesen icin ayri f, C_dot_D ve Z_dot degerleri -- nereden baslanacagi net.

4. **Maliyet olusumu takibi (Cost formation tracking):** Urun maliyetinin hangi bilesende, ne kadar olustugunu gosterir.

5. **Yatirim gerekcelendirmesi (Investment justification):** "Bu iyilestirme 2.3 yilda kendini amorti eder" gibi somut sonuclar.

6. **Cevre maliyeti entegrasyonu:** Karbon vergisi, emisyon maliyeti gibi cevre faktorleri dahil edilebilir.

### 3.4 Exergoekonomik Zayif Yanlari

1. **Veri yogunlugu (Data intensity):** Ekipman maliyet korelasyonlari, enerji fiyatlari, faiz oranlari, bakim yuzdesi vb. gerektirir.

2. **Piyasaya bagimlilik (Market dependency):** Enerji fiyatlari degistiginde sonuclar degisir. 2024'teki optimum, 2026'da optimum olmayabilir.

3. **Karmasiklik (Complexity):** SPECO metodolojisi, maliyet dengeleri, yardimci denklemler -- ogrenim egrisi dikdir.

4. **Fiziksel sezgi kaybi (Loss of physical intuition):** Ekonomik katman, termodinamik gercekleri golgede birakabilir.

5. **Maliyet korelasyon belirsizligi:** Ekipman maliyetleri uretici, konum ve zamana gore %20-50 degisebilir.

6. **Cok sayida varsayim:** Ekonomik omur, faiz orani, kapasite faktoru gibi parametreler varsayim gerektirir.

---

## 4. Ne Zaman Hangisini Kullan? -- Karar Agaci (Decision Tree)

### 4.1 EGM Kullan

Asagidaki durumlarda EGM tercih edilmelidir:

- **On tasarim / kavramsal tasarim asamasi (Conceptual design):** Henuz detayli maliyet verisi yokken alternatif tasarimlari karsilastirmak icin
- **Tasarim alternatifleri kiyaslama:** "A mi yoksa B konfigurasyonu mu termodinamik acidan ustun?" sorusu icin
- **Maliyet verisi mevcut degilken:** Yeni teknolojiler veya ozel ekipmanlar icin maliyet korelasyonlari bulunmayabilir
- **Sistemin temel fizigini anlamak icin:** "Kayiplar nerede ve neden olusyor?" sorusunu yanytlamak icin
- **Akademik / arastirma baglaminda:** Temel muhendislik bilgisi ve kavramsal anlayis icin
- **Hizli tarama (Quick screening):** Iyilestirme firsatlarinin on degerlendirmesinde
- **Egitim ve ogretim:** Yeni muhendislere exergy kavramini ogretmek icin

### 4.2 Exergoekonomik Kullan

Asagidaki durumlarda exergoekonomik analiz tercih edilmelidir:

- **Detayli muhendislik tasarimi:** Son tasarim parametrelerinin belirlenmesinde
- **Yatirim karar verme:** "Bu iyilestirmeye yatirim yapalim mi?" sorusu icin
- **Guvenilir maliyet verisi mevcut olduggunda:** Ekipman teklifleri, enerji sozlesmeleri varsa
- **Sermaye harcamasi gerekcelendirme:** Yonetim sunumlarinda parasal sonuclar gerektiginde
- **Retrofit secenekleri karsilastirma:** Farkli maliyetli iyilestirme opsiyonlari arasinda secim icin
- **Musteri odakli analiz:** Parasal degerlerle iletisim gereken durumlarda
- **Yasal/regulatif gereklilik:** Cevre etki degerlendirmesi veya karbon maliyeti hesaplanacaksa

### 4.3 Hibrit Yaklasim (Hybrid Approach) -- Tavsiye Edilen

En etkili sonuclar, iki yontemi sirali olarak birlestiren hibrit yaklasimla elde edilir:

```
Hibrit Yaklasim -- Asamali Uygulama:

  Faz 1: EGM ile kavramsal tarama
  |--> S_gen dagilimini belirle
  |--> Bejan sayilariini hesapla
  |--> En buyuk S_gen kaynaklarini sirala
  |--> Termodinamik iyilestirme yonlerini belirle

  Faz 2: Exergoekonomik detayli analiz
  |--> Faz 1'deki en buyuk S_gen kaynaklarina SPECO uygula
  |--> f faktorlerini hesapla
  |--> Yatirim-tasarruf dengesini kur
  |--> Ekonomik optimumu belirle
  |--> Geri odeme suresini hesapla

  Sonuc: Fiziksel sezgi + ekonomik karar destegi
```

---

## 5. Hibrit Yaklasim -- EGM + Exergoekonomik Entegrasyon (Hybrid Integration)

### 5.1 Entegrasyon Metodolojisi

Asagida, iki yontemi adim adim birlestiren sistematik bir metodoloji sunulmustur:

**Adim 1: EGM Analizi -- Termodinamik Haritalama**

**Fiziksel sezgi:** Ilk adimda, fabrikadaki tum bilesenlerin entropi uretimini hesaplayip, "entropi haritasi" cikaririz. Bu harita, tersinmezliklerin nerede yogunlastigini gosterir -- tipki bir sicaklik haritasinin "sicak noktalari" gostermesi gibi.

- Tum bilesenler icin S_dot_gen hesapla
- Bejan sayisi (Be) ile isi transferi vs. surtunme payini ayrist
- Pareto siralamasi yap (en buyuk S_gen kaynagindan baslayarak)

**Adim 2: On Eleme -- Termodinamik Filtreleme**

- Toplam S_gen'in %80'ini olusturan bilesenleri sec (Pareto ilkesi)
- Geri kalanlari detayli analizden cikar
- Bu adim, exergoekonomik analizin kapsamini daraltarak verimliligi arttirir

**Adim 3: SPECO Uygulamasi -- Ekonomik Katman**

**Fiziksel sezgi:** Simdi termodinamik acidan en sorunlu bilesenleri biliyoruz. Bu bilesenlerin her birine maliyet dengesi yazarak "bu sorunu cozmek ne kadara mal olur?" sorusunu sorariz.

- Adim 2'de secilen bilesenlere maliyet dengesi yaz
- f faktorlerini hesapla
- C_dot_D ve Z_dot degerlerini karsilastir

**Adim 4: Karar Matrisi -- Entegre Degerlendirme**

```
Karar Matrisi:

  Durum 1: S_gen yuksek VE f dusuk (< 0.4)
  --> NET FIRSAT: Termodinamik iyilestirme maliyet-etkin
  --> Eylem: Daha verimli ekipman yatirimi yap

  Durum 2: S_gen yuksek VE f yuksek (> 0.6)
  --> DIKKAT: Zaten iyi yatirim yapilmis, daha iyisi pahali
  --> Eylem: Baska bilesenlere odaklan

  Durum 3: S_gen dusuk VE f dusuk
  --> DUSUK ONCELIK: Kucuk kayip, dusuk yatirim
  --> Eylem: Son sirada degerlendir

  Durum 4: S_gen dusuk VE f yuksek
  --> ASIRI YATIRIM: Kucuk kayip icin fazla para harcanmis
  --> Eylem: Daha ucuz alternatif degerlendir
```

**Adim 5: Iterasyon -- Tasarim Guncelleme**

- Adim 4'teki kararlara gore tasarimi guncelle
- Yeni tasarimla EGM analizini tekrarla
- S_gen dagilimini yeniden degerlendir
- Yakinsama saglanana kadar tekrarla

### 5.2 Uygulama Ornegi -- Karma Fabrika (Practical Example)

Bir gida sektorundeki fabrikada kazan, esanjor agi ve chiller birlikte calistigi durumu ele alalim:

**Fabrika Bilgileri:**
- Kazan: 5 MW dogalgaz yakitli buhar kazani
- Esanjor agi: 3 adet kabuk-boru esanjor
- Chiller: 500 kW sogutma kapasiteli absorpsiyon chiller
- Cevre sicakligi: T_0 = 298.15 K (25 °C)

**Adim 1 -- EGM Sonuclari:**

```
Bilesen                  S_dot_gen [kW/K]    Pay [%]
-----------------------------------------------------
Kazan (yanma)                2.85             52.3
Kazan (isi transferi)        0.95             17.4
Esanjor #1                   0.62             11.4
Chiller (genlesme vanasi)    0.48              8.8
Esanjor #2                   0.28              5.1
Pompa sirkülasyon            0.15              2.8
Esanjor #3                   0.12              2.2
-----------------------------------------------------
Toplam                       5.45            100.0
```

**Adim 2 -- Pareto Filtreleme:**

Ilk 4 bilesen toplam S_gen'in %89.9'unu olusturuyor --> Bu 4 bilesene SPECO uygulanacak.

**Adim 3 -- SPECO Sonuclari:**

```
Bilesen                  C_dot_D [EUR/h]  Z_dot [EUR/h]   f
------------------------------------------------------------
Kazan (yanma)                8.55            2.10         0.20
Kazan (isi transferi)        2.85            1.50         0.34
Esanjor #1                   1.86            1.20         0.39
Chiller (genlesme vanasi)    1.44            0.35         0.20
------------------------------------------------------------
```

**Adim 4 -- Karar:**

- **Kazan yanmasi:** S_gen en yuksek, f = 0.20 (cok dusuk) --> **NET FIRSAT.** Onisitici (economizer) veya hava on isitma ile yanma verimliligi arttirilabilir.
- **Kazan isi transferi:** f = 0.34 (dusuk) --> Isi transfer yuzeyini artirmak maliyet-etkin.
- **Esanjor #1:** f = 0.39 (sinirda) --> Detayli analiz gerekir, yuzey artisi degerlendirilebilir.
- **Chiller genlesme vanasi:** S_gen yuksek, f = 0.20 (dusuk) --> Ejektorlu sistem gibi alternatif dusunulebilir. **ANCAK** ejektorun yatirim maliyeti yuksek olabilir -- detayli maliyet analizi sart.

**Sonuc:** Kazan economizer'i en oncelikli yatirimdir (yuksek S_gen + dusuk f). Chiller ejektoru termodinamik acidan cazip ama ekonomik dogrulamasi gerekir.

### 5.3 Entegrasyon Avantajlari (Integration Benefits)

1. **EGM fiziksel yonu belirler:** "Nereye bakmali?" sorusuna yanit
2. **Exergoekonomik ekonomik dogrulamayi saglar:** "Ne kadar yatirim yapmali?" sorusuna yanat
3. **Birlikte: Saglikli muhendislik karar verme sureci olusturur**
4. **Zaman tasarrufu:** EGM ile on filtreleme yapilarak SPECO'nun uygulanacagi kapsam daraltilir
5. **Risk azaltma:** Yalniz EGM'ye dayanmak ekonomik felakete, yalniz exergoekonomige dayanmak fiziksel sezgi kaybina yol acabilir
6. **Iletisim kolayligi:** Teknik ekibe EGM sonuclari, yonetime exergoekonomik sonuclar sunulabilir

---

## 6. Diger Yontemlerle Karsilastirma (Comparison with Other Methods)

### 6.1 Termoekonomik Fonksiyonel Analiz (TFA -- Thermoeconomic Functional Analysis)

**Fiziksel sezgi:** TFA, sistemi "fonksiyonlar" acisindan modeller. Her bilesen bir fonksiyon saglar (isit, sogut, sikistir) ve bu fonksiyonun maliyeti izlenir. SPECO akis bazli iken TFA fonksiyon bazlidir.

| Ozellik | EGM | SPECO | TFA |
|---|---|---|---|
| Temel birim | S_gen | Exergy akisi | Fonksiyon |
| Maliyet tahsisi | Yok | Akis bazli | Fonksiyon bazli |
| Karmasiklik | Dusuk | Orta | Yuksek |
| Fonksiyon tanimina bagimlilik | Hayir | Hayir | Evet |
| Uygulama kolayligi | Kolay | Orta | Zor |

TFA'nin avantaji, bilesenlerin "ne isin yaptigini" daha acik gostermesidir. Dezavantaji, fonksiyon taniminin subjektif olabilmesi ve yontemin daha karmasik olmasidir.

### 6.2 Exergy Tabanli Yasam Dongusu Degerlendirmesi (Exergy-Based Life Cycle Assessment -- ExLCA)

**Fiziksel sezgi:** ExLCA, exergy kavramini urunun tum yasam dongusu boyunca uygular -- hammadde cikarimindan imalata, kullanimdan bertarafa kadar. Bu yaklasim, yalnizca isletme asamasini degil, urunun "besinten mezara" tum exergy tuketimini degerlendirir.

| Ozellik | EGM | Exergoekonomik | ExLCA |
|---|---|---|---|
| Kapsam | Tek sistem | Tek sistem + maliyet | Tum yasam dongusu |
| Zaman ufku | Anlik | Ekonomik omur | Besikten mezara |
| Cevre etkisi | Dolayli | Sinirli | Kapsamli |
| Veri gereksinimi | Dusuk | Orta | Cok yuksek |
| Karar duzeyi | Tasarim | Yatirim | Strateji / politika |

ExLCA, ozellikle surdurulebilirlik ve cevre etkisi on planda olduggunda degerlidir. Ancak veri gereksinimi cok yuksektir ve sonuclarin belirsizligi de buna paralel olarak artar.

### 6.3 EMERGY Analizi (Embodied Energy Analysis)

**Fiziksel sezgi:** EMERGY (Embodied Energy), bir urun veya hizmeti uretmek icin harcanan tum enerjinin gunes enerjisi eşdegeri (solar emjoules) cinsinden ifadesidir. H.T. Odum tarafindan gelistirilen bu yaklasim, ekolojik ve ekonomik sistemleri ortak bir birimde degerlendirmeyi amaclar.

| Ozellik | EGM | Exergoekonomik | EMERGY |
|---|---|---|---|
| Birim | kW/K | EUR/saat | sej (solar emjoules) |
| Perspektif | Muhendislik | Ekonomi | Ekoloji |
| Referans | Termodinamik | Piyasa | Gunes enerjisi |
| Uygulama alani | Tasarim optimizasyonu | Yatirim karari | Ekolojik degerlendirme |
| Endustride yayginlik | Yuksek | Yuksek | Dusuk |

EMERGY analizi, endustriyel muhendislik uygulamalarinda sinirli kullanim alanina sahiptir ancak surdurulebilirlik ve ekolojik ayak izi degerlendirmelerinde benzersiz bir perspektif sunar.

### 6.4 Yontemler Arasi Iliski Semasi

```
                    Fizik <------------------------> Ekonomi
                      |                                |
                     EGM                        Maliyet Analizi
                      |                                |
                      +--- Gouy-Stodola ---+          |
                      |                    |          |
                      v                    v          v
                  Exergy Analizi ----> Exergoekonomik <--- Piyasa Verisi
                      |                    |
                      v                    v
                    ExLCA            SPECO / TFA
                      |
                      v
                   EMERGY
```

---

## 7. Pratik Muhendislik Kurallari (Practical Engineering Rules of Thumb)

### 7.1 Yontem Secimi Hizli Kilavuzu

**Fiziksel sezgi:** Her muhendislik projesi farkli bir olgunluk asamasindadir ve her asamanin bilgi ihtiyaci farklidir. Asagidaki kurallar, hangi asamada hangi yontemi kullanmayi onerdiklerini ozetler.

```
Proje Asamasi ve Uygun Yontem:

  Fikir asamasi (TRL 1-3)     --> EGM (yeterli, basit, hizli)
  On tasarim (TRL 3-5)        --> EGM + basit maliyet tahmini
  Detayli tasarim (TRL 5-7)   --> Exergoekonomik (SPECO)
  Retrofit / iyilestirme      --> Hibrit (EGM tarama + SPECO detay)
  Yatirim karari              --> Exergoekonomik (zorunlu)
  Strateji / politika         --> ExLCA veya EMERGY
```

### 7.2 EGM ile "Yapalim mi?" Sorusunu Yanitle

EGM, bir iyilestirme firsatinin var olup olmadigini anlamak icin idealdir:

- S_gen dagilimini hesapla
- En buyuk kaynaklari belirle
- Teorik iyilestirme potansiyelini hesapla: Delta_Ex = T_0 x Delta_S_gen

**Fiziksel sezgi:** Eger bir bilesenin S_gen'i toplamin %5'inden azsa, o bilesen uzerinde zaman harcamak genellikle verimsizdir. Pareto ilkesi (80/20 kurali) burada guclu bir rehberdir.

### 7.3 Exergoekonomik ile "Ne Kadar Yatirim Yapalim?" Sorusunu Yanitle

f faktoru, yatirim kararinin anahtaridir:

```
Karar Kurallari:

  S_gen yuksek VE f < 0.3:
  --> Kesin iyilestirme firsati
  --> Yatirim geri donusu yuksek olacaktir
  --> Ekonomik analizi zaman kaybetmeden yap

  S_gen yuksek VE f > 0.6:
  --> Dikkat: Zaten iyi ekipman kullaniliyor
  --> Ek yatirim maliyet-etkin olmayabilir
  --> Baska bilesenlere yonel

  S_gen orta VE f ≈ 0.5:
  --> Detayli optimizasyon gerekiyor
  --> Hassasiyet analizi yap (enerji fiyati, faiz orani)
  --> Karar sinirlarda -- kucuk degisiklikler sonucu degistirebilir
```

### 7.4 Optimum Noktalar Arasi Mesafe

Deneyimsel olarak, EGM optimumu ile ekonomik optimum arasindaki fark genellikle sinirlidir:

**Fiziksel sezgi:** Termodinamik optimum ile ekonomik optimumun "yakin" olmasi, EGM'nin ilk asamada guvenilir bir yol gostericisi olabilecegini dogrular. Enerji fiyatlari arttikca bu iki optimum birbirine daha da yaklasir -- cunku pahalilasan enerji, termodinamik verimliligin ekonomik degerini arttirir.

```
Tipik EGM vs Ekonomik Optimum Farki:

  Parametre              | Tipik Fark
  -----------------------|---------------------
  Esanjor yuzey alani    | %10 - 20
  Kompresor basinci      | %5 - 15
  Kazan verim hedefi     | %3 - 10
  Chiller COP hedefi     | %8 - 18

Enerji fiyati etkisi:
  Dusuk enerji fiyati   --> Fark buyur (%15 - 25)
  Yuksek enerji fiyati  --> Fark kuculu (%5 - 10)
  Cok yuksek fiyat      --> Fark ≈ 0 (ekonomik = termodinamik)
```

### 7.5 Enerji Fiyati ve Optimum Kaymayi

**Fiziksel sezgi:** Enerji ucuzken, "ideal" ve "ekonomik" tasarim birbirinden uzaktir -- cunku enerji israfinin bedeli dusuktur. Enerji pahalandiginda, israfin bedeli yukselir ve ekonomik optimum, EGM optimumuna dogru "kayar." Bu nedenle yuksek enerji fiyatlari doneminde EGM sonuclari, ekonomik kararlara daha yakin rehberlik eder.

```
Enerji Fiyati Senaryolari:

  Senaryo        | c_fuel [EUR/GJ] | Ekonomik Optimum | EGM'ye Yakinlik
  ---------------|-----------------|------------------|------------------
  Ucuz enerji    | 3 - 5           | Dusuk verim OK   | Uzak
  Normal enerji  | 8 - 12          | Orta verim       | Orta
  Pahali enerji  | 15 - 25         | Yuksek verim     | Yakin
  Kriz donemi    | > 30            | Maksimum verim   | Cok yakin
```

### 7.6 Cok Kriterli Karar Tablosu (Multi-Criteria Decision Summary)

Asagidaki tablo, farkli senaryolar icin en uygun yontemi ozetler:

| Senaryo | Onerilen Yontem | Gerekce |
|---|---|---|
| Yeni fabrika tasarimi | Hibrit (EGM + SPECO) | En kapsamli sonuc |
| Mevcut fabrika iyilestirmesi | SPECO (f faktoru) | Yatirim karari gerektiriyor |
| Akademik arastirma | EGM | Fiziksel kavrayis on planda |
| Hizli fizibilite | EGM | Maliyet verisi gerekmiyor |
| Yatirim sunumu | Exergoekonomik | Parasal sonuclar sart |
| Ekipman secimi | Hibrit | Fiziksel + ekonomik karsilastirma |
| Enerji denetimi | EGM tarama --> SPECO detay | Verimli zaman kullanimi |
| Karbon azaltma | ExLCA + SPECO | Cevre + ekonomi birlkte |

---

## İlgili Dosyalar (Related Files)

- `knowledge/factory/entropy_generation/overview.md` -- EGM genel bakis ve felsefesi
- `knowledge/factory/entropy_generation/fundamentals.md` -- Gouy-Stodola teoremi ve termodinamik temeller
- `knowledge/factory/entropy_generation/bejan_number.md` -- Bejan sayisi ve S_gen ayristirmasi
- `knowledge/factory/entropy_generation/heat_transfer_egm.md` -- Isi transferinde EGM
- `knowledge/factory/entropy_generation/fluid_flow_egm.md` -- Akiskan akisinda EGM
- `knowledge/factory/economic_analysis.md` -- Ekonomik analiz temelleri
- `knowledge/factory/life_cycle_cost.md` -- Yasam dongusu maliyet analizi
- `knowledge/factory/exergy_fundamentals.md` -- Exergy analizi temelleri

---

## Referanslar (References)

1. **Bejan, A.** "Entropy Generation Minimization." CRC Press, 1996. -- EGM'nin temel referans kitabi.

2. **Bejan, A., Tsatsaronis, G., Moran, M.** "Thermal Design and Optimization." Wiley, 1996. -- EGM ve exergoekonomik analizi birlestiren onemli referans.

3. **Tsatsaronis, G.** "Thermoeconomic Analysis and Optimization of Energy Systems." Progress in Energy and Combustion Science, 19(3), 227-257, 1993. -- Exergoekonomik analizin sistematik formulasyonu.

4. **Lazzaretto, A., Tsatsaronis, G.** "SPECO -- A Systematic and General Methodology for Calculating Efficiencies and Costs in Thermal Systems." Energy, 31(8-9), 1257-1289, 2006. -- SPECO metodolojisinin tanimi.

5. **Tsatsaronis, G., Park, M.H.** "On Avoidable and Unavoidable Exergy Destructions and Investment Costs in Thermal Systems." Energy Conversion and Management, 43(9-12), 1259-1270, 2002. -- Kacinilabilir/kacinilmaz exergy yikimi kavrami.

6. **Bejan, A.** "Advanced Engineering Thermodynamics." 4th Edition, Wiley, 2016. -- EGM'nin ileri uygulamalari.

7. **Szargut, J., Morris, D.R., Steward, F.R.** "Exergy Analysis of Thermal, Chemical, and Metallurgical Processes." Hemisphere, 1988. -- Exergy analizi temel referans.

8. **Odum, H.T.** "Environmental Accounting: Emergy and Environmental Decision Making." Wiley, 1996. -- EMERGY analizi referansi.
