---
title: "Endüstriyel Uygulama Rehberi — EGM (Industrial Application Guide for EGM)"
category: factory
equipment_type: factory
keywords: [endüstriyel uygulama, EGM checklist, sektörel uygulama, ölçüm, hesaplama, optimizasyon, doğrulama]
related_files: [factory/entropy_generation/overview.md, factory/entropy_generation/heat_exchanger_egm.md, factory/entropy_generation/pipe_flow_egm.md, factory/entropy_generation/refrigeration_egm.md, factory/entropy_generation/power_cycles_egm.md, factory/implementation.md]
use_when: ["EGM endüstriyel uygulaması planlanacakken", "Ekipman bazlı EGM checklist gerektiğinde", "Sektörel EGM örnekleri aranırken"]
priority: medium
last_updated: 2026-02-01
---

# Endüstriyel Uygulama Rehberi — EGM (Industrial Application Guide for EGM)

Bu dosya, Entropi Üretim Minimizasyonu (Entropy Generation Minimization — EGM) metodolojisinin endüstriyel tesislerde sistematik olarak uygulanması için kapsamlı bir rehber sunar. Ekipman bazlı uygulama tabloları, kontrol listeleri, sektörel örnekler ve adım adım uygulama prosedürlerini içerir. Amaç, EGM'nin teorik çerçevesini sahada uygulanabilir mühendislik eylemlere dönüştürmektir.

---

## 1. Ekipman Tipi İçin EGM Uygulama Özet Tablosu

Aşağıdaki tablo, endüstriyel tesislerde en yaygın ekipman tipleri için EGM uygulamasının ana hatlarını özetler. Her ekipman için baskın entropi üretim kaynakları, tipik Bejan sayısı aralığı, optimizasyon hedefleri ve beklenen tasarruf potansiyeli verilmiştir.

| Ekipman | Ana Ṡ_gen Kaynakları | Bejan Sayısı (Be) | Optimizasyon Hedefi | Tipik Tasarruf |
|---|---|---|---|---|
| Isı eşanjörü (Heat exchanger) | ΔT (sonlu sıcaklık farkı), ΔP (akış direnci) | 0.4–0.8 | Approach temperature azaltma, akış hızı optimizasyonu | %10–25 |
| Kazan (Boiler) | Yanma tersinmezliği, baca gazı ΔT | 0.7–0.9 | Baca gazı sıcaklığı düşürme, fazla hava oranı kontrolü | %5–15 |
| Kompresör (Compressor) | Mekanik sürtünme, ısı kaybı, kademe arası kayıplar | 0.2–0.5 | Kademe sayısı artırma, ara soğutma (intercooling) | %10–20 |
| Chiller / Soğutma grubu | Kısılma (throttling), ΔT (evaporatör/kondenser) | 0.3–0.7 | Genleşme cihazı iyileştirme, approach temp azaltma | %10–30 |
| Pompa sistemi (Pump system) | ΔP (vana, dirsek, fitting kayıpları) | 0.1–0.3 | Boru çapı optimizasyonu, vana eliminasyonu | %15–40 |
| Soğutma kulesi (Cooling tower) | ΔT (hava-su temas), karışma tersinmezliği | 0.5–0.7 | Fan hızı kontrolü, approach temperature azaltma | %5–15 |
| Buhar dağıtım (Steam distribution) | ΔP (hat kayıpları), ısı kaybı (yalıtım eksikliği) | 0.2–0.5 | Yalıtım iyileştirme, kapan (trap) bakımı | %5–20 |
| Isı depolama (Thermal storage) | ΔT (şarj/deşarj), ısı kaybı (tank yüzeyi) | 0.6–0.9 | Tank boyutu optimizasyonu, yalıtım kalınlığı | %10–20 |

### 1.1 Tablo Yorumu

**Bejan sayısı (Be)**, entropi üretiminin ne kadarının ısı transferinden (ΔT) kaynaklandığını gösterir:

Bejan sayısı, toplam entropi üretimi içinde ısı transferi kaynaklı tersinmezliğin payını verir. Be → 1 ise ΔT baskındır (eşanjör, kazan gibi), Be → 0 ise ΔP baskındır (pompa sistemi gibi). Bu bilgi, mühendise optimizasyon çabasını nereye yönlendirmesi gerektiğini doğrudan söyler.

$$Be = \frac{\dot{S}_{gen,\Delta T}}{\dot{S}_{gen,\Delta T} + \dot{S}_{gen,\Delta P}}$$

Burada:
- Be → 1: Isı transferi tersinmezliği baskın → approach temperature azaltmaya odaklan
- Be → 0: Akış sürtünmesi baskın → basınç düşümünü azaltmaya odaklan
- Be ≈ 0.5: Her iki kaynak eşit → her ikisini de ele al

**Pratik kural:** Bejan sayısı, EGM uygulamasında ilk bakılacak parametredir. Sayı yüksekse ısıl iyileştirmeler, düşükse hidrolik iyileştirmeler önceliklidir.

---

## 2. Ekipman Bazlı EGM Checklist'leri

Aşağıdaki kontrol listeleri, her ekipman tipi için EGM uygulamasının adım adım takibi için tasarlanmıştır. Her madde spesifik bir eylem veya ölçüm tanımlar.

### 2.1 Isı Eşanjörü EGM Checklist (Heat Exchanger)

Isı eşanjörleri, endüstriyel tesislerde en yaygın entropi üretim kaynaklarından biridir. Sonlu sıcaklık farkı (finite temperature difference) ve akış direnci (flow friction), iki ana tersinmezlik mekanizmasıdır.

- [ ] **Approach temperature ölçüldü mü?** — Sıcak taraf çıkışı ile soğuk taraf girişi arasındaki fark (hedef: ≤ 5–10 °C)
- [ ] **Bejan sayısı hesaplandı mı?** — Be > 0.5 ise ΔT odaklı, Be < 0.5 ise ΔP odaklı iyileştirme
- [ ] **Fouling (kirlenme) durumu kontrol edildi mi?** — Fouling direnci R_f ölçümü; R_f > 0.0003 m²·K/W ise temizlik gerekli
- [ ] **LMTD ve NTU değerleri karşılaştırıldı mı?** — Tasarım değerlerine göre sapma kontrol edildi
- [ ] **Akış düzeni (flow arrangement) uygun mu?** — Karşıt akış (counterflow) en düşük Ṡ_gen'i verir
- [ ] **Akış debisi dengesi kontrol edildi mi?** — Kapasite oranı (C_min/C_max) optimum aralıkta mı?
- [ ] **Basınç düşümü (ΔP) ölçüldü mü?** — Her iki tarafta ΔP, tasarım değerinin %20'sinden fazla sapmamalı
- [ ] **Bypass akışı var mı?** — Bypass, etkinliği (effectiveness) düşürüp Ṡ_gen'i artırır
- [ ] **Yüzey alanı yeterliliği değerlendirildi mi?** — NTU artışı ile ΔT tersinmezliği düşürülebilir mi?
- [ ] **Entropi üretim sayısı (N_s) hesaplandı mı?** — N_s = Ṡ_gen / (ṁ × c_p) ile boyutsuz karşılaştırma yapıldı mı?

### 2.2 Kazan EGM Checklist (Boiler)

Kazanlar, yanma tersinmezliği nedeniyle en yüksek exergy yıkımı olan ekipmanlardır. Tipik olarak yakıt exergy girdisinin %35–50'si yanma odasında yıkılır.

- [ ] **Baca gazı sıcaklığı ölçüldü mü?** — T_baca > 180 °C ise ekonomizer, T_baca > 250 °C ise hava ön ısıtıcı değerlendir
- [ ] **Fazla hava oranı (excess air) belirlendi mi?** — O₂ analizi ile; hedef: doğalgaz %5–10, fuel oil %10–15, kömür %15–25
- [ ] **Ekonomizer mevcut mu / gerekli mi?** — Baca gazından besleme suyu ön ısıtması ile ΔT tersinmezliği azaltılır
- [ ] **Hava ön ısıtıcı (air preheater) mevcut mu?** — Yanma havasını 150–200 °C'ye ön ısıtmak yanma Ṡ_gen'ini düşürür
- [ ] **Yanma verimi ve exergy verimi karşılaştırıldı mı?** — η_I yüksek ama η_II düşükse, yanma tersinmezliği baskın
- [ ] **Blöf (blowdown) oranı kontrol edildi mi?** — Yüksek blöf oranı (>%5) exergy kaybına neden olur; blöf ısı geri kazanımı değerlendir
- [ ] **Yüzey kayıpları ölçüldü mü?** — Kazan dış yüzey sıcaklığı; T_yüzey > 60 °C ise yalıtım yetersiz
- [ ] **Buhar basıncı ve sıcaklığı optimum mu?** — Proses gereksiniminden gereksiz yüksek basınç, throttling kaybına yol açar
- [ ] **Yanma odası sıcaklık profili uygun mu?** — Düzgün sıcaklık dağılımı, yerel aşırı ısınma ve NOx oluşumunu azaltır
- [ ] **Kondensasyon kazanı (condensing boiler) uygulanabilir mi?** — Baca gazı nem geri kazanımı ile ek verim

### 2.3 Kompresör EGM Checklist (Compressor)

Kompresör sistemlerinde, mekanik sürtünme ve sıkıştırma sırasındaki ısı üretimi ana entropi kaynağıdır. İzotermale yaklaşmak, toplam Ṡ_gen'i minimize eder.

- [ ] **Kademe sayısı ve ara soğutma (intercooling) durumu değerlendirildi mi?** — 2+ kademe ve ara soğutma, izotermale yaklaşarak Ṡ_gen'i %15–25 azaltır
- [ ] **Basınç oranı (pressure ratio) optimum mu?** — Her kademenin basınç oranı eşit mi? (eşit oran = minimum Ṡ_gen)
- [ ] **Atık ısı geri kazanım potansiyeli belirlendi mi?** — Kompresör çıkış havası sıcaklığı T > 80 °C ise ısı geri kazanımı değerlendir
- [ ] **Kaçak (leakage) oranı ölçüldü mü?** — Basınçlı hava sistemlerinde tipik kaçak %20–30; hedef <%10
- [ ] **Kısmi yük performansı incelendi mi?** — VSD (Variable Speed Drive) ile kısmi yükte Ṡ_gen azaltılabilir mi?
- [ ] **Emme filtresi temiz mi?** — Kirli filtre ΔP artırır ve emme koşullarını bozar
- [ ] **Soğutucu akışkan sıcaklığı uygun mu?** — Ara soğutucu çıkış sıcaklığı, emme sıcaklığına ne kadar yakın?
- [ ] **İzentropik verim (η_is) izleniyor mu?** — η_is düşüşü doğrudan Ṡ_gen artışını gösterir; hedef: ≥ %75
- [ ] **Basınç ayarı (setpoint) gereğinden yüksek mi?** — Her 1 bar fazla basınç ≈ %7 ek enerji demek
- [ ] **Ölü hacim ve geri akış kontrol edildi mi?** — Valf tıkanıklıkları ve sızıntılar Ṡ_gen'i artırır

### 2.4 Chiller EGM Checklist (Refrigeration / Chiller)

Chiller sistemlerinde, kısılma (throttling) vanası ve eşanjörlerdeki sıcaklık farkları başlıca tersinmezlik kaynaklarıdır.

- [ ] **Genleşme vanası tipi kontrol edildi mi?** — TXV (termostatik) yerine EEV (elektronik genleşme vanası) kısılma Ṡ_gen'ini %5–15 azaltır
- [ ] **Kondenser approach temperature ölçüldü mü?** — T_kond - T_soğutma_suyu; hedef: ≤ 3–5 °C; yüksekse fouling olabilir
- [ ] **Evaporatör approach temperature ölçüldü mü?** — T_chilled_water - T_evap; hedef: ≤ 2–4 °C
- [ ] **Kısılma (throttling) kaybı boyutlandırıldı mı?** — Kısılma sırasında exergy yıkımı: Ẋ_kısılma = T₀ × ṁ × Δs_throttle
- [ ] **Subcoling (alt soğutma) derecesi uygun mu?** — 3–8 °C subcooling, flash gaz miktarını azaltıp COP'u artırır
- [ ] **Superheat (aşırı ısınma) derecesi uygun mu?** — 5–10 K superheat kompresör koruması için gerekli ama fazlası Ṡ_gen artırır
- [ ] **Ekonomizer (flash tank) uygulanabilir mi?** — İki kademeli genleşme ile kısılma Ṡ_gen'i azaltılır
- [ ] **Kondenser ve evaporatör yüzey alanları yeterli mi?** — Düşük alan → yüksek ΔT → yüksek Ṡ_gen
- [ ] **COP ve exergy verimi (η_II) karşılaştırıldı mı?** — COP yüksek ama η_II düşükse, ΔT tersinmezlikleri baskın
- [ ] **Soğutucu akışkan (refrigerant) uygun mu?** — Termodinamik özellikler uygulama sıcaklıklarına uygun mu?

### 2.5 Pompa Sistemi EGM Checklist (Pumping System)

Pompa sistemlerinde, entropi üretiminin büyük kısmı akış direnci kaynaklarından (vanalar, dirsekler, daralmalar) gelir. Bejan sayısı genellikle düşüktür (Be < 0.3), yani ΔP baskındır.

- [ ] **Boru çapları optimum mu?** — Ekonomik hız aralığı kontrol edildi mi? (su: 1.5–3.0 m/s, buhar: 20–40 m/s)
- [ ] **Throttle (kısma) vanası var mı?** — Throttle vanası yerine VSD ile debi kontrolü Ṡ_gen'i %30–60 azaltır
- [ ] **Vana ve fitting sayısı minimize mi?** — Her dirsek ≈ 0.3–1.5 m eşdeğer boru boyu ΔP ekler
- [ ] **Boru güzergahı optimize edildi mi?** — Gereksiz uzunluk ve yön değişiklikleri elimine edildi mi?
- [ ] **Pompa çalışma noktası BEP'e (Best Efficiency Point) yakın mı?** — BEP'ten %20'den fazla sapma Ṡ_gen'i ciddi artırır
- [ ] **Kavitasyon (cavitation) riski değerlendirildi mi?** — Kavitasyon, yoğun entropi üreten bir süreçtir
- [ ] **Paralel pompa çalışması uygun mu?** — Düşük yükte tek pompa, yüksek yükte paralel çalışma
- [ ] **Boru yüzey pürüzlülüğü kontrol edildi mi?** — Korozyon ve tortu birikimi, sürtünme faktörünü (f) artırır
- [ ] **Kontrol vanası ΔP payı makul mü?** — Kontrol vanasına düşen ΔP, toplam sistem ΔP'nin %15'inden az olmalı
- [ ] **Isı izolasyonu (sıcak su hatları için) yeterli mi?** — Yalıtımsız borular hem ısı kaybı hem ΔT tersinmezliği üretir

---

## 3. Sektörel Uygulama Örnekleri

Her endüstri sektörünün kendine özgü enerji profili, sıcaklık seviyeleri ve ekipman kompozisyonu vardır. Bu bölümde dört ana sektör için EGM uygulama stratejileri detaylandırılmıştır.

### 3.1 Gıda Sektörü (Food Industry)

Gıda sektörü, düşük-orta sıcaklık aralığında (60–180 °C) buhar kullanımı ve soğutma ihtiyacının bir arada bulunduğu sektörlerden biridir. Bu durum, hem ısıtma hem de soğutma tarafında EGM fırsatları yaratır.

**Pastörizasyon — Isı Eşanjörü EGM Optimizasyonu:**
Pastörizasyonda süt veya meyve suyu tipik olarak 72–85 °C'ye ısıtılır ve ardından hızla soğutulur. Gelen ürünle giden ürün arasındaki rejeneratif ısı eşanjörü, bu sürecin en kritik noktasıdır.

Rejeneratif eşanjörde ısı geri kazanım oranı (recovery ratio) arttıkça approach temperature düşer ve ΔT tersinmezliği azalır. Ancak daha büyük eşanjör daha fazla ΔP üretir. EGM, bu dengeyi optimize eder.

Pastörizasyon eşanjöründe entropi üretimi, iki akış arasındaki sıcaklık farkı ve akış direncinin toplamına bağlıdır. Rejenerasyon oranı %90'dan %95'e çıkarıldığında ΔT tersinmezliği yaklaşık %30 azalır ama ΔP tersinmezliği %15 artar; net Ṡ_gen iyileşmesi genellikle %10–20 aralığındadır.

**Soğuk Hava Deposu — Chiller + Yalıtım EGM:**
Soğuk hava depolarında (0–4 °C) evaporatör sıcaklığının düşürülmesi COP'u düşürürken, yalıtım iyileştirme ısı kazanımını (heat gain) azaltarak gereken soğutma kapasitesini küçültür.

Depo ısı kazanımı yalıtım kalınlığı ile ters orantılı azalırken, yalıtım maliyeti doğrusal artar. EGM yaklaşımı, toplam entropi üretimini (soğutma çevrimi + yalıtım üzerinden ısı geçişi) minimize eden yalıtım kalınlığını verir:

Optimum yalıtım kalınlığı için, dış ortam ile depo arasındaki sıcaklık farkı büyüdükçe (örneğin yaz aylarında T_dış = 40 °C, T_depo = 2 °C) gerekli kalınlık artar. Tipik değer: 100–200 mm poliüretan.

**Buhar Kullanımı — Dağıtım Şebekesi EGM:**
Gıda tesislerinde buhar, pişirme, sterilizasyon ve CIP (Clean-in-Place) sistemleri için kullanılır. Buhar dağıtım hattındaki entropi üretim kaynakları:
- Yetersiz yalıtım: T_buhar = 150–180 °C, T_çevre = 25 °C → büyük ΔT
- Arızalı buhar kapanları (steam traps): Canlı buhar kaçağı → doğrudan exergy kaybı
- Gereksiz basınç düşürme: 10 bar buharı 3 bar'a kısmak yerine düşük basınçlı kazan kullanımı

| Fırsat | Tipik Ṡ_gen Azaltma | Yatırım | Geri Ödeme |
|---|---|---|---|
| Eşanjör rejenerasyon artışı | %10–20 | Orta | 1–2 yıl |
| Yalıtım iyileştirme | %15–30 | Düşük | 0.5–1 yıl |
| Buhar kapanı bakımı | %5–15 | Düşük | 3–6 ay |
| Evaporatör approach azaltma | %10–25 | Orta-Yüksek | 2–3 yıl |

### 3.2 Kimya Sektörü (Chemical Industry)

Kimya sektörü, yüksek sıcaklıklar (200–800 °C), ekzotermik/endotermik reaksiyonlar ve distilasyon kolonları ile en karmaşık EGM uygulama alanlarından biridir.

**Reaktör Isı Yönetimi — Reaksiyon Ekzotermi Geri Kazanımı:**
Ekzotermik reaksiyonlarda açığa çıkan ısı genellikle soğutma suyu ile uzaklaştırılır. Ancak bu ısının sıcaklık seviyesi yeterince yüksekse (> 80 °C), başka proseslerde kullanılabilir.

Reaktör soğutma sisteminde entropi üretimi, reaksiyon sıcaklığı ile soğutma suyu sıcaklığı arasındaki farka bağlıdır. Reaksiyon sıcaklığı T_rxn = 250 °C olan bir reaktörü 30 °C soğutma suyu ile soğutmak büyük ΔT tersinmezliği yaratır. Kademeli ısı geri kazanımı (önce 120 °C'de proses ısıtma, sonra 60 °C'de ön ısıtma, en son soğutma suyu) Ṡ_gen'i %40–60 azaltabilir.

**Distilasyon — Reboiler ve Kondenser EGM:**
Distilasyon kolonları, kimya endüstrisinin en enerji yoğun ekipmanlarıdır. Reboiler (yeniden kaynatıcı) ve kondenser arasındaki sıcaklık farkı, kolon termodinamiğini belirler.

Reboiler'da giren buharın sıcaklığı ile kolon taban sıcaklığı arasındaki fark (approach temperature) ne kadar küçükse, ΔT tersinmezliği o kadar az olur. Ancak çok küçük ΔT, büyük ısı transfer alanı gerektirir. EGM, bu dengeyi optimize eder.

**Proses Soğutma — Soğutma Suyu Sistemi EGM:**
Kimya tesislerinde soğutma suyu çevrimleri genellikle açık veya kapalı devre soğutma kuleleri ile çalışır. Soğutma kulesi approach temperature'ü (T_su_çıkış - T_yaş_termometre) optimize edilmelidir.

| Fırsat | Tipik Ṡ_gen Azaltma | Yatırım | Geri Ödeme |
|---|---|---|---|
| Kademeli ısı geri kazanımı | %30–50 | Yüksek | 2–4 yıl |
| Distilasyon ısı entegrasyonu | %20–40 | Orta-Yüksek | 2–3 yıl |
| Soğutma kulesi optimizasyonu | %5–15 | Düşük-Orta | 1–2 yıl |
| Reaktör yalıtım iyileştirme | %10–20 | Düşük | 0.5–1 yıl |

### 3.3 Metal Sektörü (Metal Industry)

Metal sektörü, yüksek sıcaklık fırınları (800–1600 °C) ve yoğun soğutma suyu kullanımı ile karakterize edilir. Yüksek sıcaklıklardaki exergy içeriği büyük olduğundan, EGM potansiyeli çok yüksektir.

**Fırın Atık Isı — Yüksek Sıcaklık Geri Kazanımı:**
Metal eritme ve ısıl işlem fırınlarında baca gazı sıcaklıkları 400–1000 °C aralığında olabilir. Bu baca gazının exergy içeriği çok yüksektir.

Yüksek sıcaklıktaki atık ısının exergy değeri, Carnot faktörü ile doğru orantılıdır. Baca gazı sıcaklığı 600 °C (873 K) ve çevre sıcaklığı 25 °C (298 K) olduğunda, bu ısının termodinamik kalitesi ≈ %66'dır (Carnot faktörü: 1 - 298/873). Bu yüksek kaliteli ısıyı doğrudan atmosfere atmak, büyük exergy yıkımı demektir.

$$\eta_{Carnot} = 1 - \frac{T_0}{T_{baca}} = 1 - \frac{298}{873} \approx 0.66$$

Geri kazanım stratejileri:
- Reküperatör (recuperator) ile yanma havası ön ısıtma
- Waste heat boiler ile buhar üretimi
- ORC (Organic Rankine Cycle) ile elektrik üretimi (T_baca < 400 °C için)

**Soğutma Suyu — Soğutma Devreleri EGM:**
Metal işleme makineleri, hadde tezgahları ve indüksiyon fırınları soğutma suyu gerektirir. Bu soğutma suyunun sıcaklığı genellikle 40–60 °C arasındadır — düşük sıcaklıklı ısı geri kazanımı (low-grade heat recovery) ile tesis ısıtma veya ön ısıtma yapılabilir.

**Basınçlı Hava — Kompresör Sistemi EGM:**
Metal sektöründe pneumatik sistemler, kumlama ve boyama için yoğun basınçlı hava kullanılır. Kompresör atık ısısı (tipik olarak elektrik girdisinin %80–90'ı ısıya dönüşür) geri kazanılmalıdır.

Kompresör enerji dönüşümünde, elektrik enerjisinin büyük kısmı kompresyon ısısına dönüşür. 100 kW elektrik tüketen bir kompresörde yaklaşık 85 kW ısı üretilir. Bu ısının sıcaklık seviyesi (70–90 °C) düşük basınçlı sıcak su üretimi için yeterlidir.

| Fırsat | Tipik Ṡ_gen Azaltma | Yatırım | Geri Ödeme |
|---|---|---|---|
| Baca gazı ısı geri kazanımı | %30–50 | Yüksek | 1–3 yıl |
| Kompresör atık ısı kullanımı | %10–20 | Orta | 1–2 yıl |
| Soğutma suyu ısı geri kazanımı | %5–15 | Düşük-Orta | 1–2 yıl |
| Fırın yalıtım iyileştirme | %10–25 | Orta | 1–2 yıl |

### 3.4 Çimento Sektörü (Cement Industry)

Çimento üretimi, son derece enerji yoğun bir prosestir: 1 ton klinker üretimi için yaklaşık 3.0–3.5 GJ termal enerji ve 90–120 kWh elektrik gerekir. Yüksek sıcaklıklar (1450 °C klinker, 800–1100 °C kalsinasyon) büyük EGM potansiyeli sunar.

**Klinker Soğutma — Clinker Cooler Isı Geri Kazanım Optimizasyonu:**
Döner fırından çıkan klinker (~1400 °C) klinker soğutucuda havaya ısı vererek soğutulur. Bu hava, fırın yakma havası olarak kullanılır (secondary air, ~800–1000 °C) veya kalsinör havası olarak (tertiary air, ~700–900 °C). Soğutucu veriminin artırılması doğrudan Ṡ_gen azaltma demektir.

Klinker soğutucuda entropi üretimi, klinker ile hava arasındaki sıcaklık farkına ve havanın dağılım düzgünlüğüne bağlıdır. Düzgün hava dağılımı (uniform air distribution), yerel sıcak noktaları (hot spots) azaltarak ortalama ΔT'yi düşürür ve Ṡ_gen'i minimize eder.

**Fırın Baca Gazı — Ön Isıtıcı Kule (Preheater Tower) EGM:**
Çimento fırınlarında çok kademeli siklon ön ısıtıcılar, hammaddeyi kademeli olarak ısıtır. Her kademede baca gazı ile hammadde arasında ısı transferi gerçekleşir. Kademe sayısı arttıkça (4, 5 veya 6 kademe), toplam ΔT tersinmezliği azalır.

Ön ısıtıcı kademelerinde, her kademe eklenmesi toplam Ṡ_gen'i azaltır çünkü ortalama sıcaklık farkı düşer. Ancak ek kademe ΔP artışı (fan enerji tüketimi) ve yatırım maliyeti demektir. EGM, optimal kademe sayısını belirlemek için kullanılır. Tipik optimum: 5–6 kademe.

**Atık Isı Elektrik Üretimi — ORC/WHR Sistem EGM:**
Çimento tesislerinde ön ısıtıcı çıkış gazı (280–400 °C) ve klinker soğutucu atık havası (250–350 °C) ile WHR (Waste Heat Recovery) sistemi kurulabilir. ORC veya buhar çevrimi ile elektrik üretilir.

WHR sisteminde entropi üretimi, ısı kaynağı (baca gazı/atık hava) ile çalışma akışkanı arasındaki sıcaklık farkından kaynaklanır. Pinch noktasında ΔT'nin minimize edilmesi (ideal: 10–15 °C) toplam Ṡ_gen'i düşürür.

| Fırsat | Tipik Ṡ_gen Azaltma | Yatırım | Geri Ödeme |
|---|---|---|---|
| Klinker soğutucu iyileştirme | %15–30 | Yüksek | 2–4 yıl |
| Ön ısıtıcı kademe ekleme | %10–20 | Çok Yüksek | 3–5 yıl |
| WHR elektrik üretimi | %20–35 | Çok Yüksek | 3–6 yıl |
| Fırın yalıtım onarımı | %5–10 | Düşük-Orta | 0.5–1 yıl |

---

## 4. Uygulama Adımları (Step-by-Step Implementation)

EGM'nin endüstriyel bir tesiste sistematik uygulanması dört temel adımdan oluşur. Her adım bir öncekinin çıktısına dayanır.

### 4.1 Adım 1: Ölçüm (Measurement)

EGM analizinin kalitesi, girdi verilerinin kalitesine doğrudan bağlıdır. "Ölçemediğinizi yönetemezsiniz" prensibi burada da geçerlidir.

**Gerekli Ölçümler:**

| Ölçüm | Ekipman | Doğruluk Hedefi | Ölçüm Cihazı |
|---|---|---|---|
| Sıcaklık (T) | Tüm ekipmanlar | ±0.5 °C | Termokupl (Type K/J), RTD (Pt100) |
| Basınç (P) | Kompresör, pompa, boru | ±0.5% FS | Basınç transmitteri |
| Debi (ṁ) | Tüm akış hatları | ±2% | Ultrasonik, Coriolis, orifis |
| Baca gazı bileşimi | Kazan | O₂: ±0.2%, CO: ±50 ppm | Gaz analizörü |
| Elektrik gücü (Ẇ) | Motor, kompresör, pompa | ±1% | Güç analizörü |
| Nem (φ) | Soğutma kulesi, kurutma | ±2% RH | Hygrometre |

**Ölçüm Noktaları — Genel Prensip:**

Her ekipmanın giriş ve çıkışındaki sıcaklık, basınç ve debi, entropi dengesi (entropy balance) için gerekli minimum veri setidir. Entropi üretimi şu denklemle hesaplanır:

Kararlı halde (steady-state), bir kontrol hacmine giren ve çıkan entropiler ile ısı transferlerinin toplanması, entropi üretim hızını verir. Giriş ve çıkış noktalarındaki termodinamik durum (T, P) bilindiğinde, spesifik entropi (s) termodinamik tablolardan veya CoolProp gibi yazılımlardan okunabilir.

$$\dot{S}_{gen} = \sum \dot{m}_{çıkış} \cdot s_{çıkış} - \sum \dot{m}_{giriş} \cdot s_{giriş} - \sum \frac{\dot{Q}_i}{T_i}$$

Burada:
- ṁ_çıkış, ṁ_giriş: Çıkış ve giriş kütle debileri (kg/s)
- s_çıkış, s_giriş: Çıkış ve giriş spesifik entropileri (kJ/(kg·K))
- Q̇_i: i-inci sınırdan transfer edilen ısı (kW)
- T_i: i-inci sınırın sıcaklığı (K)

**Veri Kalitesi Gereksinimleri:**
- Ölçüm frekansı: Kararlı hal analizi için minimum 15 dakika ortalaması
- Eşzamanlılık: Tüm ölçümler aynı çalışma koşulunda alınmalı (±5 dakika)
- Kalibrasyon: Ölçüm cihazları yılda en az 1 kez kalibre edilmeli
- Tekrarlanabilirlik: Aynı koşullarda en az 3 ölçüm seti, sapma <%5

### 4.2 Adım 2: Hesaplama (Calculation)

Ölçüm verileri toplandıktan sonra, her bileşen için entropi üretimi hesaplanır ve boyutsuz parametrelerle karşılaştırılır.

**2a) Her Bileşen İçin Ṡ_gen Hesaplaması:**

Her ekipmanın giriş ve çıkış koşulları kullanılarak entropi dengesi uygulanır. Örnek — bir ısı eşanjörü için:

Isı eşanjöründe entropi üretimi, sıcak ve soğuk akışların entropi değişimlerinin toplamıdır. Eşanjör dış yüzeyi iyi yalıtılmışsa, ısı kaybı ihmal edilir ve Ṡ_gen doğrudan giriş-çıkış entropi farkından hesaplanır.

$$\dot{S}_{gen,HX} = \dot{m}_s \cdot (s_{s,çıkış} - s_{s,giriş}) + \dot{m}_c \cdot (s_{c,çıkış} - s_{c,giriş})$$

Burada:
- ṁ_s, ṁ_c: Sıcak ve soğuk taraf kütle debileri (kg/s)
- s: Spesifik entropi değerleri (kJ/(kg·K))

**2b) Bejan Sayısı Hesaplama:**

Bejan sayısı, toplam entropi üretiminin hangi mekanizmadan kaynaklandığını gösteren kritik göstergedir. Isı transferi kaynaklı Ṡ_gen ile toplam Ṡ_gen'in oranı olarak tanımlanır.

$$Be = \frac{\dot{S}_{gen,\Delta T}}{\dot{S}_{gen,\Delta T} + \dot{S}_{gen,\Delta P}}$$

Yorum kuralları:
- Be > 0.7: Isı transferi optimizasyonuna odaklan (approach temp, yüzey alanı)
- Be < 0.3: Akış direnci optimizasyonuna odaklan (boru çapı, vana eliminasyonu)
- 0.3 ≤ Be ≤ 0.7: Her iki mekanizma da önemli, birlikte optimize et

**2c) Entropi Üretim Sayısı (N_s) Hesaplama:**

Entropi üretim sayısı (entropy generation number), farklı boyut ve kapasitedeki ekipmanları boyutsuz olarak karşılaştırmaya olanak sağlar. Ṡ_gen'in, akışın taşıdığı entropi kapasitesine oranıdır.

$$N_s = \frac{\dot{S}_{gen}}{\dot{m} \cdot c_p}$$

Burada:
- N_s: Boyutsuz entropi üretim sayısı (—)
- ṁ: Kütle debisi (kg/s)
- c_p: Sabit basınçta özgül ısı (kJ/(kg·K))

Tipik N_s değerleri:
- İyi tasarlanmış eşanjör: N_s < 0.01
- Ortalama eşanjör: N_s = 0.01–0.05
- Kötü tasarlanmış eşanjör: N_s > 0.05
- İyi tasarlanmış boru: N_s < 0.005
- Kötü tasarlanmış boru: N_s > 0.02

**2d) En Büyük Ṡ_gen Kaynaklarını Belirleme:**

Tüm ekipmanların Ṡ_gen değerleri hesaplandıktan sonra, Pareto prensibi uygulanır: en büyükten küçüğe sırala ve kümülatif toplamı hesapla. Toplam Ṡ_gen'in %80'ini oluşturan ekipmanlar, optimizasyon önceliğidir.

Exergy yıkımının parasal değeri, Gouy-Stodola teoremi ve enerji birim fiyatı kullanılarak hesaplanır. Bu, mühendise termodinamik kaybın mali boyutunu gösterir.

$$\dot{X}_{yıkım} = T_0 \cdot \dot{S}_{gen} \quad \text{(kW)}$$

$$C_{yıkım} = \dot{X}_{yıkım} \times t_{çalışma} \times c_{enerji} \quad \text{(€/yıl)}$$

Burada:
- T₀: Çevre sıcaklığı (K), tipik olarak 298 K
- t_çalışma: Yıllık çalışma süresi (saat/yıl), tipik olarak 8000 saat
- c_enerji: Enerji birim fiyatı (€/kWh)

### 4.3 Adım 3: Optimizasyon (Optimization)

En büyük entropi üretim kaynakları belirlendikten sonra, EGM formülleri ile optimum tasarım parametreleri bulunur.

**3a) EGM Formüllerini Uygulama:**

Her ekipman tipi için Ṡ_gen'in tasarım parametreleri cinsinden ifadesi yazılır ve türevi sıfıra eşitlenir. Örnek — optimum boru çapı:

Bir borudaki toplam entropi üretimi, sürtünme (ΔP) ve ısı kaybı (ΔT) bileşenlerinin toplamıdır. Boru çapı arttıkça sürtünme azalır (hız düşer) ama ısı kaybı artar (yüzey alanı büyür). Bu iki zıt etki, optimum boru çapında dengelenir.

$$\dot{S}_{gen,toplam}(D) = \frac{32 \cdot f \cdot \dot{m}^3}{\pi^2 \cdot \rho^2 \cdot T_{ort} \cdot D^5} + \frac{\pi \cdot D \cdot L \cdot U \cdot (T_s - T_0)^2}{T_s \cdot T_0}$$

Burada:
- f: Darcy sürtünme faktörü (—)
- D: Boru iç çapı (m)
- L: Boru uzunluğu (m)
- U: Toplam ısı geçiş katsayısı (W/(m²·K))
- T_s: Boru yüzey sıcaklığı (K)

Türev alınıp sıfıra eşitlenmesi, optimum çapı verir:

$$\frac{d\dot{S}_{gen}}{dD} = 0 \quad \Rightarrow \quad D_{opt}$$

**3b) Mevcut vs Optimum Karşılaştırma:**

Her ekipman için mevcut çalışma koşulları ile EGM optimumu karşılaştırılır:

| Parametre | Mevcut | EGM Optimum | İyileşme Potansiyeli |
|---|---|---|---|
| Eşanjör approach T | 15 °C | 5 °C | Ṡ_gen %40 azalma |
| Boru çapı | DN80 | DN100 | Ṡ_gen %35 azalma |
| Kompresör kademesi | 1 | 2 + intercooling | Ṡ_gen %20 azalma |
| Kazan fazla hava | %25 | %10 | Ṡ_gen %15 azalma |
| Chiller subcooling | 0 °C | 5 °C | Ṡ_gen %10 azalma |

**3c) Önceliklendirme — Ṡ_gen Azaltma Potansiyeline Göre:**

Tüm iyileştirme fırsatları, Ṡ_gen azaltma potansiyeli ve yatırım maliyeti/geri ödeme süresi kombinasyonuna göre sıralanır. Yüksek Ṡ_gen azaltma + düşük yatırım = en yüksek öncelik.

### 4.4 Adım 4: Doğrulama (Verification)

Optimizasyon uygulamalarından sonra, gerçek iyileşmenin doğrulanması kritik önemdedir.

**4a) Öncesi/Sonrası Ṡ_gen Karşılaştırması:**

Optimizasyon öncesi ve sonrası aynı çalışma koşullarında ölçüm yapılarak Ṡ_gen değişimi hesaplanır. İstatistiksel olarak anlamlı olması için en az 3 ölçüm seti gereklidir.

$$\Delta \dot{S}_{gen} = \dot{S}_{gen,önce} - \dot{S}_{gen,sonra} \quad \text{(kW/K)}$$

$$\text{İyileşme } (\%) = \frac{\Delta \dot{S}_{gen}}{\dot{S}_{gen,önce}} \times 100$$

**4b) Enerji ve Maliyet Tasarrufu Doğrulama:**

Ṡ_gen azalmasının enerji tasarrufuna dönüşümü, Gouy-Stodola teoremi ile hesaplanır. Gerçekleşen tasarruf, beklenen tasarrufun en az %70'i olmalıdır; aksi halde hesaplama veya uygulama hatası araştırılmalıdır.

$$\Delta \dot{X} = T_0 \times \Delta \dot{S}_{gen} \quad \text{(kW)}$$

$$\text{Yıllık tasarruf} = \Delta \dot{X} \times t_{çalışma} \times c_{enerji} \quad \text{(€/yıl)}$$

**4c) Sürekli İzleme (Continuous Monitoring) Önerileri:**

EGM optimizasyonu bir kerelik değil, sürekli bir süreç olmalıdır:

- **Gerçek zamanlı izleme:** Kritik ekipmanlar için Ṡ_gen'in online hesaplanması (SCADA/DCS entegrasyonu)
- **Trend analizi:** Ṡ_gen'in zamanla artması, bakım ihtiyacını veya fouling'i gösterir
- **Alarm seviyeleri:** Ṡ_gen, tasarım değerinin %20'sinden fazla artarsa uyarı
- **Periyodik EGM denetimi:** Yılda en az 1 kez kapsamlı EGM analizi
- **Benchmarking:** Benzer tesislerle Ṡ_gen karşılaştırması

---

## 5. EGM Uygulama Zorlukları ve Çözümleri

### 5.1 Veri Eksikliği

**Zorluk:** Birçok endüstriyel tesiste yeterli ölçüm altyapısı yoktur. Özellikle eski tesislerde sıcaklık ve basınç ölçüm noktaları sınırlıdır, debi ölçümleri mevcut olmayabilir.

**Çözümler:**
- **Portatif ölçüm:** Ultrasonik debi ölçer (clamp-on), kızılötesi termometre, temas termokuplları ile geçici ölçüm kampanyaları düzenleyin
- **Enerji dengesi kontrolü:** Mevcut ölçümlerden enerji dengesi kurarak eksik verileri dolaylı hesaplayın. Enerji dengesi kapanmıyorsa ölçüm hatası arayın
- **Tasarım verileri:** Ekipman imalatçı katalog değerlerini başlangıç referansı olarak kullanın, ardından sahada doğrulayın
- **Kademeli yaklaşım:** Önce en büyük ekipmanları (kazanlar, kompresörler) ölçümleyin; küçük ekipmanlar için ampirik korelasyonlar kullanın
- **Minimum veri seti:** T_giriş, T_çıkış, P_giriş, P_çıkış ve ṁ — bu beş parametre her ekipman için Ṡ_gen'i hesaplamaya yeterlidir

### 5.2 Çoklu Değişken Optimizasyonu (Multi-Variable Optimization)

**Zorluk:** Gerçek endüstriyel sistemlerde onlarca tasarım parametresi birbiriyle etkileşir. Bir eşanjörün approach temperature'ünü düşürmek, pompanın ΔP'sini artırabilir.

**Çözümler:**
- **Bağımsız alt sistemler:** Sistemi mümkün olduğunca bağımsız alt sistemlere ayırın ve her birini ayrı optimize edin
- **Sıralı optimizasyon:** Önce en büyük Ṡ_gen kaynağını optimize edin, sonra diğerlerini güncellenmiş koşullarda yeniden hesaplayın
- **Sayısal optimizasyon:** Analitik çözüm mümkün değilse, genetik algoritma (GA) veya parçacık sürüsü optimizasyonu (PSO) gibi meta-sezgisel yöntemler kullanın
- **Duyarlılık analizi:** Her parametrenin Ṡ_gen üzerindeki etkisini belirleyin; düşük etkili parametreleri sabit tutarak problem boyutunu azaltın
- **Pinch analizi entegrasyonu:** Isı eşanjörü ağları için pinch analizi, EGM'nin tamamlayıcısıdır

### 5.3 Mevcut Tesislere Retrofit Kısıtları (Retrofit Constraints)

**Zorluk:** Mevcut tesislerde alan kısıtları, boru güzergahları, yapısal sınırlamalar ve üretim kesintisi maliyetleri, optimum çözümün uygulanmasını zorlaştırır.

**Çözümler:**
- **Kısıtlı optimizasyon:** EGM formülasyonuna fiziksel kısıtları (mevcut alan, mevcut boru çapları, standart ekipman boyutları) ekleyin
- **Pareto frontu:** Birden fazla kısıt altında, Ṡ_gen azaltma ile maliyet/kısıt arasındaki Pareto frontu çizin
- **Aşamalı uygulama:** Büyük yatırımları üretim duraklarına (shutdown) göre planlayın; küçük iyileştirmeleri (yalıtım, vana eliminasyonu) hemen uygulayın
- **Standart boyutlar:** Teorik optimum D = 127 mm ise, en yakın standart çap DN125 veya DN150'den hangisinin Ṡ_gen'e daha yakın olduğunu kontrol edin
- **Modüler yaklaşım:** Mevcut ekipmana paralel ek ünite ekleme (örneğin paralel eşanjör) retrofit'i kolaylaştırır

### 5.4 Ekonomik Değerlendirme Entegrasyonu (Economic Assessment Integration)

**Zorluk:** EGM termodinamik optimumu verir, ancak ekonomik optimum farklı olabilir. Mühendis, bu iki optimum arasında karar vermelidir.

**Çözümler:**
- **Ekzergoekonomik (exergoeconomic) analiz:** Her bileşenin exergy yıkım maliyetini (C_D) ve yatırım maliyetini (Z) hesaplayarak toplam maliyeti minimize edin

Toplam maliyet minimizasyonunda, ekipman yatırım maliyeti ile exergy yıkım maliyetinin toplamı ele alınır. Yatırım artırıldıkça exergy yıkımı azalır; ancak toplam maliyet minimum noktayı geçtikten sonra artmaya başlar.

$$C_{toplam} = Z + C_D = Z + c_f \cdot T_0 \cdot \dot{S}_{gen} \cdot t_{çalışma}$$

Burada:
- Z: Yıllıklandırılmış yatırım maliyeti (€/yıl)
- C_D: Exergy yıkım maliyeti (€/yıl)
- c_f: Yakıt exergy birim fiyatı (€/kWh)

- **Basit geri ödeme süresi:** Yatırım maliyetini yıllık tasarrufa bölün; ≤ 3 yıl ise genellikle kabul edilebilir
- **Net bugünkü değer (NPV):** 10 yıllık proje ömrü için NPV hesaplayın; NPV > 0 ise yatırım yapılabilir
- **Enerji fiyat senaryoları:** Farklı enerji fiyat senaryolarında (düşük, orta, yüksek) ekonomik fizibiliteyi test edin

---

## 6. Pratik Mühendislik Kuralları (Rules of Thumb)

Bu bölümde, EGM'nin sahada hızlı uygulanması için deneyim tabanlı pratik kurallar sunulmuştur. Bu kurallar detaylı hesaplamanın yerini almaz ancak önceliklendirme ve hızlı karar verme için değerlidir.

### 6.1 Önceliklendirme Kuralları

**Pareto prensibi:** Ekipmanların %20'si, toplam Ṡ_gen'in %80'ini oluşturur. Tesisin en büyük enerji tüketicileriyle başlayın — genellikle kazanlar, büyük kompresörler ve ana eşanjörlerdir.

**Bejan sayısı hızlı karar aracıdır:** Be'yi hesapladığınız anda ΔT mi ΔP mi baskın bilirsiniz.
- Be > 0.7 → Approach temperature iyileştirme, yüzey alanı artırma
- Be < 0.3 → Boru çapı büyütme, vana eliminasyonu, VSD ekleme
- 0.3–0.7 → İkisi birlikte; genellikle önce ΔT sonra ΔP

### 6.2 Hızlı Kazanımlar (Quick Wins)

Düşük yatırım, hızlı geri ödeme, hemen uygulanabilir iyileştirmeler:

| Eylem | Tipik Ṡ_gen Azaltma | Yatırım | Geri Ödeme |
|---|---|---|---|
| Fouling temizliği (eşanjör) | %5–15 | Düşük | < 3 ay |
| Vana eliminasyonu (gereksiz olanlar) | %5–10 | Çok düşük | Anında |
| Yalıtım onarımı (hasar görmüş) | %10–25 | Düşük | 3–6 ay |
| Buhar kapanı bakımı/değişimi | %5–15 | Düşük | 3–6 ay |
| Hava kaçağı tespiti ve onarımı | %10–20 | Düşük | 1–3 ay |
| Filtre temizliği/değişimi | %3–8 | Çok düşük | Anında |
| Basınç ayarı (setpoint) düşürme | %3–7 | Sıfır | Anında |

### 6.3 Orta Yatırımlar (Medium Investments)

Orta düzey yatırım gerektiren, 1–3 yıl geri ödemeli iyileştirmeler:

| Eylem | Tipik Ṡ_gen Azaltma | Yatırım | Geri Ödeme |
|---|---|---|---|
| VSD (değişken hız sürücüsü) ekleme | %15–40 | Orta | 1–2 yıl |
| Approach temperature iyileştirme | %10–25 | Orta | 1–3 yıl |
| Ekonomizer ekleme (kazan) | %5–15 | Orta | 1–2 yıl |
| EEV'ye geçiş (chiller) | %5–15 | Düşük-Orta | 1–2 yıl |
| Boru çapı büyütme (kritik hatlar) | %15–30 | Orta | 2–3 yıl |
| Kompresör atık ısı geri kazanımı | %10–20 | Orta | 1–2 yıl |

### 6.4 Büyük Yatırımlar (Large Investments)

Kapsamlı yatırım gerektiren, uzun vadeli stratejik iyileştirmeler:

| Eylem | Tipik Ṡ_gen Azaltma | Yatırım | Geri Ödeme |
|---|---|---|---|
| Ekipman değişimi (yüksek verimli) | %20–40 | Yüksek | 3–5 yıl |
| Isı eşanjörü ağı yeniden tasarımı | %25–50 | Yüksek | 3–5 yıl |
| WHR (atık ısı geri kazanım) sistemi | %20–35 | Çok Yüksek | 3–6 yıl |
| Sistem yeniden tasarımı (layout) | %15–30 | Çok Yüksek | 4–7 yıl |
| Kojenerasyon / trijenerasyon | %30–50 | Çok Yüksek | 4–8 yıl |

### 6.5 Genel EGM Pratik Kuralları

1. **Her 10 °C approach temperature azaltma**, eşanjör Ṡ_gen'ini yaklaşık %15–25 düşürür
2. **Boru çapını bir kademe büyütmek** (örn. DN80 → DN100), sürtünme Ṡ_gen'ini yaklaşık %40–60 düşürür
3. **%10 fazla hava azaltma** (kazanlarda), yanma Ṡ_gen'ini yaklaşık %3–5 düşürür
4. **VSD ekleme**, kısmi yükte pompa/fan Ṡ_gen'ini %30–60 düşürür
5. **Fouling direnci 2× artarsa**, eşanjör Ṡ_gen'i yaklaşık %10–20 artar → temizlik programı kritik
6. **1 bar gereksiz basınç** (kompresörde), elektrik tüketimini ≈ %7 artırır → basınç ayarını gözden geçirin
7. **Yalıtım kalınlığını 2× artırmak**, ısı kaybı Ṡ_gen'ini yaklaşık %50 azaltır
8. **Kısılma vanası yerine VSD**, entropi üretimini sıfıra yakın düşürür (kısılma → sıfır tersinmezlik)
9. **Karşıt akış (counterflow)** düzeni, paralel akışa göre aynı görev için %20–40 daha az Ṡ_gen üretir
10. **Her arızalı buhar kapanı**, saatte 5–50 kg canlı buhar kaybı ve karşılık gelen exergy yıkımı demektir

---

## İlgili Dosyalar

| Dosya | İlişki |
|---|---|
| `factory/entropy_generation/overview.md` | EGM genel bakış ve felsefesi — temel konseptler |
| `factory/entropy_generation/heat_transfer_egm.md` | Isı transferinde EGM — eşanjör formülasyonları |
| `factory/entropy_generation/fluid_flow_egm.md` | Akışkan akışında EGM — boru ve vana formülasyonları |
| `factory/entropy_generation/bejan_number.md` | Bejan sayısı detaylı analizi — ΔT vs ΔP ayrıştırma |
| `factory/entropy_generation/fundamentals.md` | EGM matematiksel temeller — Gouy-Stodola teoremi |
| `factory/entropy_generation/finite_time_thermo.md` | Sonlu zamanlı termodinamik — güç çevrimleri EGM |
| `factory/implementation.md` | Genel EGM uygulama rehberi — fabrika düzeyinde |
| `factory/cross_equipment.md` | Ekipmanlar arası entropi üretim fırsatları |
| `factory/prioritization.md` | Exergy iyileştirme önceliklendirmesi |
| `factory/economic_analysis.md` | EGM sonuçlarının ekonomik değerlendirmesi |
| `factory/waste_heat_recovery.md` | Atık ısı geri kazanımı ile entropi azaltma |

---

## Referanslar

1. **Bejan, A.** (1982). *Entropy Generation Through Heat and Fluid Flow*. Wiley, New York. — EGM'nin temel eseri; ısı transferi ve akış sistemlerinde entropi üretim formülasyonları.

2. **Bejan, A.** (1996). *Entropy Generation Minimization*. CRC Press, Boca Raton. — Kapsamlı EGM monografı; endüstriyel uygulama örnekleri, eşanjör, güç çevrimi ve soğutma sistemi optimizasyonları.

3. **Bejan, A.** (2006). *Advanced Engineering Thermodynamics* (3rd Ed.). Wiley. — İkinci yasa odaklı termodinamik; EGM'nin teorik temelleri.

4. **Tsatsaronis, G.** (1993). "Thermoeconomic analysis and optimization of energy systems." *Progress in Energy and Combustion Science*, 19(3), 227–257. — Ekzergoekonomik analiz temelleri; EGM ile maliyet entegrasyonu.

5. **Sciubba, E. & Wall, G.** (2007). "A brief commented history of exergy from the beginnings to 2004." *International Journal of Thermodynamics*, 10(1), 1–26. — Exergy ve EGM tarihçesi.

6. **Açıkkalp, E. et al.** (2015). "Advanced exergy analysis of an electricity-generating facility using natural gas." *Energy Conversion and Management*, 101, 165–178. — Endüstriyel tesislerde ileri exergy analizi ve EGM uygulaması.

7. **Dincer, I. & Rosen, M.A.** (2013). *Exergy: Energy, Environment and Sustainable Development* (2nd Ed.). Elsevier. — Exergy analizi ve EGM'nin çevresel boyutu.

8. **Kotas, T.J.** (1995). *The Exergy Method of Thermal Plant Analysis*. Krieger Publishing. — Termal tesislerde exergy ve entropi üretim analizi.

9. **Moran, M.J. et al.** (2014). *Fundamentals of Engineering Thermodynamics* (8th Ed.). Wiley. — Termodinamik temel kavramlar ve entropi üretimi.

10. **Feidt, M.** (2017). *Finite Physical Dimensions Optimal Thermodynamics*. Elsevier. — Sonlu boyutlar termodinamiği; EGM'nin pratik mühendislik kısıtları altında uygulanması.

---

> **ExergyLab Notu:** Bu dosya, EGM'nin endüstriyel tesislerde pratik uygulanması için kapsamlı bir rehberdir. Teorik formülasyonlar için `fundamentals.md` ve `bejan_number.md` dosyalarına, ekipman spesifik EGM analizleri için `heat_transfer_egm.md` ve `fluid_flow_egm.md` dosyalarına, çalışılmış örnekler için `worked_examples/` dizinine başvurunuz. Sektörel benchmark değerleri için `factory/factory_benchmarks.md` dosyasını kullanınız.
