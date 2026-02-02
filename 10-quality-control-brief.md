# ExergyLab Brief: Kalite Kontrol ve Entegrasyon (Quality Assurance)

> **Claude Code için:** Bu brief, 1-9 arası brief'lerin çıktılarını doğrular, düzeltir ve entegre eder. Tüm dosyaları incele, eksikleri tamamla, tutarsızlıkları gider.

---

## 🎯 OTONOM YETKİ

Bu brief **en son** çalıştırılır. Görevin:
1. Tüm 9 brief'i oku ve ne yapılması gerektiğini anla
2. Proje genelinde tüm dosyaları tara ve doğrula
3. Eksik, hatalı veya tutarsız her şeyi düzelt
4. Entegrasyon sorunlarını çöz
5. Genel proje kalitesini artır
6. Mevcut çalışan işlevselliği bozma (testler geçmeli)

**Kısıt:** Commit ve push yapma.

---

## 📋 ADIM 1: Brief'leri Oku

Sırasıyla oku ve her birinin ne üretmesi gerektiğini anla:

```
01-heat-exchanger-brief.md    → knowledge/heat_exchanger/ (~20 dosya) + skill
02-steam-turbine-chp-brief.md → knowledge/steam_turbine/ (~20 dosya) + skill
03-dryer-brief.md             → knowledge/dryer/ (~22 dosya) + skill
04-pinch-analysis-brief.md    → knowledge/factory/pinch/ (~18 dosya)
05-energy-management-brief.md → knowledge/factory/energy_management/ (~21 dosya)
06-advanced-exergy-brief.md   → knowledge/factory/advanced_exergy/ (~18 dosya)
07-exergoeconomic-brief.md    → knowledge/factory/exergoeconomic/ (~17 dosya)
08-thermoeconomic-optimization-brief.md → knowledge/factory/thermoeconomic_optimization/ (~15 dosya)
09-entropy-generation-brief.md → knowledge/factory/entropy_generation/ (~19 dosya)
```

---

## 📋 ADIM 2: Dosya Varlık Kontrolü

Her brief için beklenen dizin ve dosyaların var olduğunu kontrol et.

### 2.1 Yeni Ekipman Dizinleri

```bash
# Isı eşanjörü
ls knowledge/heat_exchanger/
ls knowledge/heat_exchanger/equipment/
ls knowledge/heat_exchanger/solutions/
ls knowledge/heat_exchanger/INDEX.md

# Buhar türbini
ls knowledge/steam_turbine/
ls knowledge/steam_turbine/equipment/
ls knowledge/steam_turbine/systems/
ls knowledge/steam_turbine/solutions/
ls knowledge/steam_turbine/economics/
ls knowledge/steam_turbine/INDEX.md

# Kurutma fırını
ls knowledge/dryer/
ls knowledge/dryer/equipment/
ls knowledge/dryer/solutions/
ls knowledge/dryer/sectors/
ls knowledge/dryer/INDEX.md
```

### 2.2 Factory Alt Dizinleri

```bash
# Pinch analizi
ls knowledge/factory/pinch/

# Enerji yönetimi
ls knowledge/factory/energy_management/

# İleri exergy
ls knowledge/factory/advanced_exergy/
ls knowledge/factory/advanced_exergy/equipment_specific/

# Exergoekonomik
ls knowledge/factory/exergoeconomic/
ls knowledge/factory/exergoeconomic/worked_examples/

# Termoekonomik optimizasyon
ls knowledge/factory/thermoeconomic_optimization/
ls knowledge/factory/thermoeconomic_optimization/worked_examples/

# Entropi üretim minimizasyonu
ls knowledge/factory/entropy_generation/
ls knowledge/factory/entropy_generation/worked_examples/
```

### 2.3 Skill Dosyaları

```bash
ls skills/equipment/heat_exchanger_expert.md
ls skills/equipment/steam_turbine_expert.md
ls skills/equipment/dryer_expert.md
```

### 2.4 Eksik Dosya Raporu

Her brief'te belirtilen dosya listesini kontrol et. Eksik dosyaları listele ve oluştur.

---

## 📋 ADIM 3: Dosya Kalite Kontrolü

Her dosya için şu kontrolleri yap:

### 3.1 YAML Frontmatter Kontrolü

```bash
# Tüm yeni dosyalarda YAML frontmatter var mı?
for dir in knowledge/heat_exchanger knowledge/steam_turbine knowledge/dryer \
           knowledge/factory/pinch knowledge/factory/energy_management \
           knowledge/factory/advanced_exergy knowledge/factory/exergoeconomic \
           knowledge/factory/thermoeconomic_optimization knowledge/factory/entropy_generation; do
  echo "=== $dir ==="
  find "$dir" -name "*.md" | while read f; do
    head -1 "$f" | grep -q "^---" || echo "MISSING FRONTMATTER: $f"
  done
done
```

Her dosyada olması gereken frontmatter alanları:
- `title` (zorunlu)
- `category` (zorunlu)
- `keywords` (zorunlu)
- `related_files` (zorunlu)
- `priority` (zorunlu)

Eksik alan varsa ekle.

### 3.2 Minimum Satır Sayısı Kontrolü

```bash
# Ekipman dosyaları: minimum 150 satır
# İleri konular: minimum 200 satır
find knowledge/heat_exchanger knowledge/steam_turbine knowledge/dryer -name "*.md" | while read f; do
  lines=$(wc -l < "$f")
  if [ "$lines" -lt 150 ]; then
    echo "SHORT FILE ($lines lines): $f"
  fi
done

find knowledge/factory/pinch knowledge/factory/advanced_exergy \
     knowledge/factory/exergoeconomic knowledge/factory/thermoeconomic_optimization \
     knowledge/factory/entropy_generation -name "*.md" | while read f; do
  lines=$(wc -l < "$f")
  if [ "$lines" -lt 150 ]; then
    echo "SHORT FILE ($lines lines): $f"
  fi
done
```

Kısa dosyaları zenginleştir (daha fazla içerik, örnek, tablo ekle).

### 3.3 Cross-Reference Kontrolü

```bash
# İlgili Dosyalar bölümü var mı?
find knowledge/heat_exchanger knowledge/steam_turbine knowledge/dryer \
     knowledge/factory/pinch knowledge/factory/energy_management \
     knowledge/factory/advanced_exergy knowledge/factory/exergoeconomic \
     knowledge/factory/thermoeconomic_optimization knowledge/factory/entropy_generation \
     -name "*.md" | while read f; do
  grep -q "İlgili Dosyalar" "$f" || echo "MISSING CROSS-REF: $f"
done
```

Cross-reference eksikse ekle.

### 3.4 Referanslar Kontrolü

```bash
# Referanslar bölümü var mı?
find knowledge/heat_exchanger knowledge/steam_turbine knowledge/dryer \
     knowledge/factory/pinch knowledge/factory/energy_management \
     knowledge/factory/advanced_exergy knowledge/factory/exergoeconomic \
     knowledge/factory/thermoeconomic_optimization knowledge/factory/entropy_generation \
     -name "*.md" | while read f; do
  grep -q "Referanslar" "$f" || echo "MISSING REFERENCES: $f"
done
```

### 3.5 Türkçe Başlık Kontrolü

```bash
# Dosyalarda Türkçe başlıklar kullanılmış mı? (## ile başlayan satırlar)
find knowledge/heat_exchanger knowledge/steam_turbine knowledge/dryer -name "*.md" | while read f; do
  headings=$(grep "^## " "$f" | head -3)
  echo "$f: $headings"
done
```

Tamamen İngilizce başlıklar varsa Türkçeye çevir.

### 3.6 Birim Kontrolü

SI birimleri kullanılmış mı kontrol et:
- kW (Watt değil)
- °C (Fahrenheit değil)
- bar (psi değil)
- EUR / € (USD değil, özel durum hariç)
- m³/h (GPM değil)

---

## 📋 ADIM 4: INDEX Dosyaları Entegrasyonu

### 4.1 Ana INDEX Güncelleme

`/knowledge/INDEX.md` dosyasını güncelle — tüm yeni dizinleri ekle:

```markdown
## Ekipman Knowledge Base

| Dizin | Dosya Sayısı | Açıklama |
|-------|-------------|----------|
| compressor/ | 18 | Kompresör exergy analizi |
| boiler/ | 22 | Kazan exergy analizi |
| chiller/ | 24 | Chiller exergy analizi |
| pump/ | 22 | Pompa exergy analizi |
| heat_exchanger/ | ~20 | Isı eşanjörü analizi |
| steam_turbine/ | ~20 | Buhar türbini ve CHP |
| dryer/ | ~22 | Kurutma fırını analizi |

## Fabrika Knowledge Base

| Dizin | Dosya Sayısı | Açıklama |
|-------|-------------|----------|
| factory/ (ana) | 33 | Fabrika analizi temelleri |
| factory/pinch/ | ~18 | Pinch analizi detay |
| factory/energy_management/ | ~21 | ISO 50001, denetim, M&V |
| factory/advanced_exergy/ | ~18 | İleri exergy analizi |
| factory/exergoeconomic/ | ~17 | Exergoekonomik analiz |
| factory/thermoeconomic_optimization/ | ~15 | Termoekonomik optimizasyon |
| factory/entropy_generation/ | ~19 | Entropi üretim minimizasyonu |
```

### 4.2 Alt INDEX Tutarlılığı

Her dizinin kendi INDEX.md dosyası var mı? İçerikleri doğru mu? Dosya listesi gerçek dosyalarla eşleşiyor mu?

---

## 📋 ADIM 5: Skill Dosyaları Kontrolü

### 5.1 Yeni Equipment Skills Kontrolü

```bash
# Yeni skill dosyaları var mı?
ls -la skills/equipment/heat_exchanger_expert.md
ls -la skills/equipment/steam_turbine_expert.md
ls -la skills/equipment/dryer_expert.md
```

Her skill dosyasında olması gerekenler:
- [ ] YAML frontmatter (skill_id, version, type, triggers, dependencies, knowledge_files)
- [ ] Uzmanlık alanı tanımı
- [ ] Kritik metrikler tablosu
- [ ] Karar ağacı
- [ ] Tipik öneriler ve ROI tablosu
- [ ] Yanıt örneği (JSON)

### 5.2 Mevcut Skills Güncelleme

Brief'ler mevcut skill dosyalarını güncellemeyi de istiyordu:

```bash
# Bu dosyalar güncellenmiş mi kontrol et:
cat skills/core/exergy_fundamentals.md | grep -c "kaçınılabilir\|avoidable\|EGM\|entropi üretim"
cat skills/factory/factory_analyst.md | grep -c "pinch\|exergoekonomik\|thermoeconomic"
cat skills/factory/integration_expert.md | grep -c "pinch\|ısı eşanjör ağı\|HEN"
```

Güncellenmemişlerse, yeni konulara referanslar ekle.

### 5.3 Skills README Güncelleme

`/skills/README.md` dosyasında yeni skill'ler listeleniyor mu?

---

## 📋 ADIM 6: Cross-Equipment Entegrasyon

### 6.1 Yeni Ekipmanların Factory Entegrasyonu

`knowledge/factory/cross_equipment.md` dosyasında yeni ekipmanlar var mı?

Eklenmesi gereken cross-equipment fırsatları:
- Isı eşanjörü ↔ tüm ekipmanlar (eşanjör her entegrasyonun parçası)
- Buhar türbini ↔ kazan (back-pressure türbin → proses buhar)
- Kurutma fırını ↔ kazan (buhar → kurutma)
- Kurutma fırını ↔ chiller (egzoz → absorption)
- Kurutma fırını egzoz → ısı eşanjörü → besleme ön ısıtma

### 6.2 Sektörel Dosyalarda Yeni Ekipmanlar

`knowledge/factory/sector_*.md` dosyalarında yeni ekipmanlar referans ediliyor mu?

```
Tekstil → kurutma fırını (ram fırın, tenter) eklenmeli
Gıda → kurutma fırını (sprey, bant) eklenmeli
Kağıt → kurutma fırını (silindir) + buhar türbini eklenmeli
Kimya → ısı eşanjörü + CHP eklenmeli
Çimento → atık ısı ORC eklenmeli
```

---

## 📋 ADIM 7: CLAUDE.md Güncelleme

`/CLAUDE.md` dosyasını güncelle:

1. Dizin yapısına yeni klasörleri ekle
2. Ekipman listesini güncelle (4 → 7 ekipman tipi)
3. İleri analiz yöntemlerini ekle
4. Knowledge base istatistiklerini güncelle

---

## 📋 ADIM 8: Mevcut Testlerin Geçtiğini Doğrula

```bash
cd /home/ubuntu/exergy-lab
python -m pytest tests/ -v 2>&1 | tail -20
```

Testler geçmiyorsa sorunu bul ve düzelt. Yeni dosyalar mevcut kodu bozmamalı.

```bash
# Frontend build
cd frontend && npm run build 2>&1 | tail -10
```

---

## 📋 ADIM 9: İstatistik Raporu Oluştur

Son olarak, projenin güncel durumunu özetleyen bir rapor oluştur:

```bash
echo "=== ExergyLab Knowledge Base İstatistikleri ==="
echo ""

echo "--- Ekipman Knowledge ---"
for dir in compressor boiler chiller pump heat_exchanger steam_turbine dryer; do
  count=$(find "knowledge/$dir" -name "*.md" 2>/dev/null | wc -l)
  lines=$(find "knowledge/$dir" -name "*.md" 2>/dev/null -exec cat {} \; | wc -l)
  echo "$dir: $count dosya, $lines satır"
done

echo ""
echo "--- Factory Knowledge ---"
for dir in knowledge/factory/*.md; do
  echo "$(basename $dir)"
done
count_factory_root=$(find knowledge/factory -maxdepth 1 -name "*.md" | wc -l)
echo "Factory root: $count_factory_root dosya"

for subdir in pinch energy_management advanced_exergy exergoeconomic thermoeconomic_optimization entropy_generation; do
  count=$(find "knowledge/factory/$subdir" -name "*.md" 2>/dev/null | wc -l)
  lines=$(find "knowledge/factory/$subdir" -name "*.md" 2>/dev/null -exec cat {} \; | wc -l)
  echo "factory/$subdir: $count dosya, $lines satır"
done

echo ""
echo "--- Skills ---"
find skills -name "*.md" | wc -l
find skills -name "*.md" -exec echo {} \;

echo ""
echo "--- Toplam ---"
total_files=$(find knowledge -name "*.md" | wc -l)
total_lines=$(find knowledge -name "*.md" -exec cat {} \; | wc -l)
echo "Toplam knowledge dosyası: $total_files"
echo "Toplam satır: $total_lines"

echo ""
echo "--- Testler ---"
cd /home/ubuntu/exergy-lab && python -m pytest tests/ --tb=no -q 2>&1 | tail -5
```

Bu raporu `/home/ubuntu/exergy-lab/QA_REPORT.md` dosyasına kaydet.

---

## 📋 ADIM 10: Sorun Özeti

Tüm kontroller sonrası bir sorun özeti oluştur:

```markdown
# QA Raporu

## ✅ Geçen Kontroller
- [x] ...

## ⚠️ Düzeltilen Sorunlar
- Dosya X eksik frontmatter → Eklendi
- Dosya Y 80 satır → 180 satıra genişletildi
- ...

## ❌ Çözülemeyen Sorunlar (varsa)
- ...

## 📊 Final İstatistikler
- Toplam knowledge dosyası: ???
- Toplam satır: ???
- Toplam skill dosyası: ???
- Test durumu: ???/??? geçiyor
```

---

## ✅ Tamamlama Kontrol Listesi

### Doğrulama:
- [ ] 9 brief'in tüm beklenen dosyaları mevcut
- [ ] Tüm dosyalarda YAML frontmatter var
- [ ] Tüm dosyalar minimum satır gereksinimini karşılıyor
- [ ] Tüm dosyalarda İlgili Dosyalar bölümü var
- [ ] Tüm dosyalarda Referanslar bölümü var
- [ ] Türkçe başlıklar kullanılmış
- [ ] SI birimleri kullanılmış

### Entegrasyon:
- [ ] Ana INDEX.md güncellendi
- [ ] Alt INDEX dosyaları tutarlı
- [ ] Yeni skill dosyaları mevcut ve doğru formatta
- [ ] Mevcut skill dosyaları güncellendi
- [ ] Skills README güncellendi
- [ ] CLAUDE.md güncellendi
- [ ] Cross-equipment entegrasyonlar yapıldı
- [ ] Sektörel dosyalar güncellendi

### Doğrulama:
- [ ] Mevcut testler geçiyor
- [ ] Frontend build başarılı
- [ ] QA_REPORT.md oluşturuldu

### Düzeltmeler:
- [ ] Eksik dosyalar oluşturuldu
- [ ] Kısa dosyalar zenginleştirildi
- [ ] Tutarsızlıklar giderildi
- [ ] Cross-reference eksikleri tamamlandı

**Bu brief HİÇBİR ŞEYİ ATLAMA. Her adımı sırasıyla uygula. Commit ve push YAPMA.**
