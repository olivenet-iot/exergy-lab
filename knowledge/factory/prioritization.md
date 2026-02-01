---
title: "Proje Önceliklendirme ve Karar Analizi (Project Prioritization and Decision Analysis)"
category: factory
equipment_type: factory
keywords: [önceliklendirme, yatırım, fabrika, ROI]
related_files: [factory/economic_analysis.md, factory/cross_equipment.md, factory/implementation.md]
use_when: ["Yatırım önceliklendirmesi yapılırken", "Proje sıralaması belirlenirken"]
priority: high
last_updated: 2026-01-31
---
# Proje Önceliklendirme ve Karar Analizi (Project Prioritization and Decision Analysis)

> Son güncelleme: 2026-01-31

## Genel Bakış

Enerji verimlilik projelerinin önceliklendirilmesi, sınırlı bütçe ve kaynaklar altında maksimum fayda elde etmeyi amaçlar. Bu dosya; Çok Kriterli Karar Analizi (MCDA), ağırlıklı puanlama modeli, hızlı kazanım (quick wins) çerçevesi, risk-getiri matrisi ve portföy optimizasyonu yöntemlerini sunar. Kapsamlı bir çalışılmış örnek ile 10 enerji verimlilik önleminin puanlanması, sıralanması ve duyarlılık analizi gösterilmektedir.

## 1. Çok Kriterli Karar Analizi — MCDA (Multi-Criteria Decision Analysis)

### 1.1 MCDA Metodolojisi

```
MCDA, birden fazla (genellikle çelişen) kritere göre alternatiflerin
sistematik olarak değerlendirilmesi ve sıralanması yöntemidir.

Adımlar:
1. Karar kriterlerini tanımla
2. Kriter ağırlıklarını belirle (toplam = 100%)
3. Her alternatifi her kritere göre puanla (1-10 veya 1-5 ölçek)
4. Ağırlıklı puanları hesapla
5. Toplam puanlara göre sırala
6. Duyarlılık analizi yap (ağırlık değişimlerine karşı)
7. Final kararı ver

Toplam Puan:
S_j = Σᵢ (wᵢ × sᵢⱼ)

Burada:
- S_j = j-inci alternatifin toplam ağırlıklı puanı
- wᵢ = i-inci kriterin ağırlığı [oran, Σwᵢ = 1]
- sᵢⱼ = j-inci alternatifin i-inci kriter puanı [1-10]
```

### 1.2 Kriter Tanımları ve Ağırlıklar

| Kategori | Kriter | Ağırlık [%] | Açıklama |
|---|---|---|---|
| **Ekonomik (%40)** | | | |
| | Geri ödeme süresi (SPP) | 20 | Kısa SPP = yüksek puan |
| | NPV / yatırım oranı | 12 | Yüksek NPV/yatırım = yüksek puan |
| | Yıllık tasarruf miktarı | 8 | Mutlak tasarruf büyüklüğü |
| **Teknik (%30)** | | | |
| | Teknik fizibilite | 12 | Kanıtlanmış teknoloji = yüksek puan |
| | Uygulama kolaylığı | 10 | Kolay montaj, az duruş = yüksek puan |
| | Teknik risk | 8 | Düşük risk = yüksek puan |
| **Stratejik (%30)** | | | |
| | CO₂ azaltma potansiyeli | 12 | Yüksek emisyon azaltma = yüksek puan |
| | Sürdürülebilirlik / ESG etkisi | 8 | Kurumsal hedeflerle uyum |
| | Enerji güvenliği etkisi | 5 | Dış enerjiye bağımlılık azaltma |
| | Mevzuat uyumu | 5 | Yasal gereklilik veya teşvik |

### 1.3 Puanlama Ölçeği

```
Her kriter için 1-10 puanlama rehberi:

Geri Ödeme Süresi (SPP):
  10: <6 ay      8: 6-12 ay     6: 1-2 yıl
   5: 2-3 yıl    3: 3-5 yıl     1: >5 yıl

NPV / Yatırım Oranı:
  10: >5.0       8: 3.0-5.0     6: 1.5-3.0
   5: 1.0-1.5    3: 0.5-1.0     1: <0.5

Yıllık Tasarruf:
  10: >€50,000   8: €30-50K     6: €15-30K
   5: €8-15K     3: €3-8K       1: <€3K

Teknik Fizibilite:
  10: Plug & play 8: Standart    6: Mühendislik gerektiren
   5: Kompleks    3: Deneysel    1: Kanıtlanmamış

Uygulama Kolaylığı:
  10: Duruş yok   8: <1 gün     6: 1-5 gün
   5: 1-2 hafta   3: 2-4 hafta  1: >4 hafta duruş

Teknik Risk:
  10: Risksiz      8: Düşük     6: Orta
   5: Orta-yüksek  3: Yüksek   1: Çok yüksek

CO₂ Azaltma:
  10: >200 tCO₂/yıl  8: 100-200  6: 50-100
   5: 20-50           3: 5-20     1: <5

Sürdürülebilirlik:
  10: Doğrudan ESG hedefi  8: Güçlü katkı  6: Orta katkı
   5: Dolaylı katkı        3: Az katkı     1: Etkisiz

Enerji Güvenliği:
  10: %10+ bağımlılık azalma  8: %5-10  6: %2-5
   5: %1-2                    3: <%1    1: Etkisiz

Mevzuat Uyumu:
  10: Yasal zorunluluk    8: Teşvik/destek var  6: Gelecek mevzuat
   5: Sektör beklentisi   3: İsteğe bağlı       1: İlgisiz
```

## 2. Hızlı Kazanım Çerçevesi (Quick Wins Framework)

### 2.1 Proje Sınıflandırması

```
Hızlı Kazanım (Quick Win) kriterleri:
- Yatırım: <€10,000
- SPP: <1 yıl
- Uygulama: <1 ay
- Risk: Düşük
- Duruş: Yok veya minimal

Orta Vadeli Proje kriterleri:
- Yatırım: €10,000 - €100,000
- SPP: 1-3 yıl
- Uygulama: 1-6 ay
- Risk: Düşük-orta
- Duruş: Planlı bakım döneminde

Stratejik Yatırım kriterleri:
- Yatırım: >€100,000
- SPP: 3-7 yıl
- Uygulama: 6-24 ay
- Risk: Orta-yüksek
- Duruş: Planlı uzun duruş gerekebilir
```

### 2.2 Proje Sınıflandırma Matrisi

| | Düşük Maliyet (<€10K) | Orta Maliyet (€10-100K) | Yüksek Maliyet (>€100K) |
|---|---|---|---|
| **Kısa SPP (<1 yıl)** | HEMEN UYGULA (Quick Win) | ÖNCELİKLİ (Faz 1) | STRATEJİK ÖNCELİK |
| **Orta SPP (1-3 yıl)** | ÖNCELİKLİ (Faz 1) | PLANLI (Faz 2) | DEĞERLENDİR |
| **Uzun SPP (3-5 yıl)** | FIRSATÇI | DEĞERLENDİR | UZUN VADELİ |
| **Çok Uzun SPP (>5 yıl)** | DÜŞÜK ÖNCELİK | STRATEJİK | ÖZEL GEREKÇELİ |

## 3. Risk-Getiri Matrisi (Risk-Return Matrix)

### 3.1 Risk Değerlendirme Kriterleri

| Risk Faktörü | Düşük (1-3) | Orta (4-6) | Yüksek (7-10) |
|---|---|---|---|
| Teknoloji olgunluğu | Kanıtlanmış, standart | Bilinen ama özel | Yeni/deneysel |
| Proses etkisi | Bağımsız, etki yok | Kısmi etki, yönetilebilir | Proses durdurmak gerekli |
| Tasarruf belirsizliği | ±%10 | ±%10-30 | ±>%30 |
| Tedarik riski | Yerel, çoklu tedarikçi | İthalat, 2-3 tedarikçi | Tek kaynak, uzun termin |
| Operatör etkisi | Eğitim gerektirmez | Kısa eğitim | Yoğun eğitim/adaptasyon |

### 3.2 Risk-Getiri Pozisyonları

```
Risk-Getiri Matrisi (ASCII):

Getiri (NPV/Yatırım)
    |
 10 |  [D]          [A]
    |
  8 |     [E]    [B]
    |
  6 |        [C]      [F]
    |
  4 |     [G]   [H]
    |
  2 |  [I]         [J]
    |________________________
    1    3    5    7    9   Risk

Bölgeler:
- Sol üst (düşük risk, yüksek getiri): İDEAL → Hemen uygula
- Sağ üst (yüksek risk, yüksek getiri): DİKKATLİ → Risk azaltma ile uygula
- Sol alt (düşük risk, düşük getiri): FIRSATÇI → Uygun zamanda uygula
- Sağ alt (yüksek risk, düşük getiri): KAÇIN → Özel gerekçe lazım
```

## 4. Uygulama Zorluk Matrisi (Implementation Difficulty Matrix)

### 4.1 Zorluk Değerlendirme

| Zorluk Faktörü | Kolay (1-3) | Orta (4-6) | Zor (7-10) |
|---|---|---|---|
| Duruş gereksinimi | Yok | <1 hafta | >1 hafta |
| Mühendislik tasarımı | Standart | Proje bazlı | Ar-Ge gerekli |
| İzin/onay süreci | Yok | İç onay | Dış izin gerekli |
| Alan/mekan kısıtı | Yeterli alan | Sınırlı ama çözülebilir | Ciddi alan sorunu |
| Diğer projelere bağımlılık | Bağımsız | Kısmi bağımlı | Tam bağımlı |

### 4.2 Tasarruf-Zorluk Matrisi

```
Tasarruf [€/yıl]
     |
 50K |  [CHP]          [Pinch]
     |
 30K |        [VSD]      [Economizer]
     |
 15K |  [Basınç]   [Isı GK]
     |     [Kaçak]
  5K |  [Kapan]    [LED]
     |     [İzolasyon]
     |________________________
     1    3    5    7    9   Zorluk

Strateji:
- Sol üst: Öncelik 1 → Büyük tasarruf, kolay uygulama
- Sol alt: Quick win → Küçük ama kolay, hemen uygula
- Sağ üst: Planlı → Büyük tasarruf ama planlama gerekli
- Sağ alt: Değerlendir → Zor ve küçük tasarruf, dikkatli ol
```

## 5. Kapsamlı Çalışılmış Örnek: 10 Enerji Önlemi Değerlendirmesi

### 5.1 Proje Listesi

| No | Proje | Yatırım [€] | Yıllık Tasarruf [€] | SPP [yıl] | CO₂ [tCO₂/yıl] |
|---|---|---|---|---|---|
| P1 | Basınçlı hava kaçak onarımı | 3,500 | 17,000 | 0.21 | 42 |
| P2 | Kompresör basınç düşürme | 500 | 8,500 | 0.06 | 21 |
| P3 | Buhar kapanı bakım/değişim | 6,000 | 22,000 | 0.27 | 55 |
| P4 | Kompresör VSD retrofit | 22,000 | 12,000 | 1.83 | 30 |
| P5 | Economizer ekleme | 38,000 | 18,000 | 2.11 | 85 |
| P6 | Kompresör atık ısı geri kazanımı | 15,000 | 7,500 | 2.00 | 35 |
| P7 | LED aydınlatma dönüşümü | 28,000 | 11,000 | 2.55 | 27 |
| P8 | İzolasyon iyileştirme | 12,000 | 6,500 | 1.85 | 30 |
| P9 | Chiller VSD ve optimizasyon | 35,000 | 9,000 | 3.89 | 22 |
| P10 | Pinch tabanlı ısı entegrasyonu | 120,000 | 45,000 | 2.67 | 210 |

### 5.2 MCDA Puanlama

```
Kriter ağırlıkları:
w1 = SPP: 0.20
w2 = NPV/Yatırım: 0.12
w3 = Yıllık Tasarruf: 0.08
w4 = Teknik Fizibilite: 0.12
w5 = Uygulama Kolaylığı: 0.10
w6 = Teknik Risk: 0.08
w7 = CO₂ Azaltma: 0.12
w8 = Sürdürülebilirlik: 0.08
w9 = Enerji Güvenliği: 0.05
w10 = Mevzuat Uyumu: 0.05
```

### 5.3 Puanlama Tablosu (Her Proje, Her Kriter)

| Proje | SPP (w=0.20) | NPV/I (w=0.12) | Tasarruf (w=0.08) | Fiz. (w=0.12) | Kolay (w=0.10) | Risk (w=0.08) | CO₂ (w=0.12) | Sürd. (w=0.08) | Güv. (w=0.05) | Mevz. (w=0.05) |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 10 | 10 | 5 | 10 | 9 | 10 | 5 | 6 | 4 | 5 |
| P2 | 10 | 10 | 4 | 10 | 10 | 10 | 3 | 5 | 4 | 5 |
| P3 | 10 | 10 | 6 | 9 | 8 | 9 | 6 | 7 | 5 | 7 |
| P4 | 6 | 7 | 4 | 8 | 6 | 7 | 4 | 6 | 3 | 6 |
| P5 | 5 | 6 | 5 | 8 | 5 | 7 | 7 | 8 | 6 | 7 |
| P6 | 5 | 6 | 3 | 7 | 6 | 6 | 5 | 7 | 5 | 5 |
| P7 | 5 | 5 | 4 | 9 | 7 | 9 | 4 | 7 | 2 | 6 |
| P8 | 6 | 7 | 3 | 9 | 8 | 9 | 4 | 6 | 4 | 5 |
| P9 | 3 | 4 | 4 | 7 | 5 | 6 | 3 | 5 | 3 | 5 |
| P10 | 4 | 5 | 9 | 6 | 3 | 5 | 10 | 9 | 8 | 8 |

### 5.4 Ağırlıklı Puan Hesabı

```
S_j = Σᵢ (wᵢ × sᵢⱼ)

P1:  0.20×10 + 0.12×10 + 0.08×5 + 0.12×10 + 0.10×9 + 0.08×10
     + 0.12×5 + 0.08×6 + 0.05×4 + 0.05×5
   = 2.00 + 1.20 + 0.40 + 1.20 + 0.90 + 0.80 + 0.60 + 0.48 + 0.20 + 0.25
   = 8.03

P2:  0.20×10 + 0.12×10 + 0.08×4 + 0.12×10 + 0.10×10 + 0.08×10
     + 0.12×3 + 0.08×5 + 0.05×4 + 0.05×5
   = 2.00 + 1.20 + 0.32 + 1.20 + 1.00 + 0.80 + 0.36 + 0.40 + 0.20 + 0.25
   = 7.73

P3:  0.20×10 + 0.12×10 + 0.08×6 + 0.12×9 + 0.10×8 + 0.08×9
     + 0.12×6 + 0.08×7 + 0.05×5 + 0.05×7
   = 2.00 + 1.20 + 0.48 + 1.08 + 0.80 + 0.72 + 0.72 + 0.56 + 0.25 + 0.35
   = 8.16

P4:  0.20×6 + 0.12×7 + 0.08×4 + 0.12×8 + 0.10×6 + 0.08×7
     + 0.12×4 + 0.08×6 + 0.05×3 + 0.05×6
   = 1.20 + 0.84 + 0.32 + 0.96 + 0.60 + 0.56 + 0.48 + 0.48 + 0.15 + 0.30
   = 5.89

P5:  0.20×5 + 0.12×6 + 0.08×5 + 0.12×8 + 0.10×5 + 0.08×7
     + 0.12×7 + 0.08×8 + 0.05×6 + 0.05×7
   = 1.00 + 0.72 + 0.40 + 0.96 + 0.50 + 0.56 + 0.84 + 0.64 + 0.30 + 0.35
   = 6.27

P6:  0.20×5 + 0.12×6 + 0.08×3 + 0.12×7 + 0.10×6 + 0.08×6
     + 0.12×5 + 0.08×7 + 0.05×5 + 0.05×5
   = 1.00 + 0.72 + 0.24 + 0.84 + 0.60 + 0.48 + 0.60 + 0.56 + 0.25 + 0.25
   = 5.54

P7:  0.20×5 + 0.12×5 + 0.08×4 + 0.12×9 + 0.10×7 + 0.08×9
     + 0.12×4 + 0.08×7 + 0.05×2 + 0.05×6
   = 1.00 + 0.60 + 0.32 + 1.08 + 0.70 + 0.72 + 0.48 + 0.56 + 0.10 + 0.30
   = 5.86

P8:  0.20×6 + 0.12×7 + 0.08×3 + 0.12×9 + 0.10×8 + 0.08×9
     + 0.12×4 + 0.08×6 + 0.05×4 + 0.05×5
   = 1.20 + 0.84 + 0.24 + 1.08 + 0.80 + 0.72 + 0.48 + 0.48 + 0.20 + 0.25
   = 6.29

P9:  0.20×3 + 0.12×4 + 0.08×4 + 0.12×7 + 0.10×5 + 0.08×6
     + 0.12×3 + 0.08×5 + 0.05×3 + 0.05×5
   = 0.60 + 0.48 + 0.32 + 0.84 + 0.50 + 0.48 + 0.36 + 0.40 + 0.15 + 0.25
   = 4.38

P10: 0.20×4 + 0.12×5 + 0.08×9 + 0.12×6 + 0.10×3 + 0.08×5
     + 0.12×10 + 0.08×9 + 0.05×8 + 0.05×8
   = 0.80 + 0.60 + 0.72 + 0.72 + 0.30 + 0.40 + 1.20 + 0.72 + 0.40 + 0.40
   = 6.26
```

### 5.5 Sonuç Sıralaması

| Sıra | Proje | Toplam Puan | Kategori | Yatırım [€] | Kümülatif [€] |
|---|---|---|---|---|---|
| 1 | P3: Buhar kapanı bakım | 8.16 | Quick Win | 6,000 | 6,000 |
| 2 | P1: Hava kaçak onarımı | 8.03 | Quick Win | 3,500 | 9,500 |
| 3 | P2: Basınç düşürme | 7.73 | Quick Win | 500 | 10,000 |
| 4 | P8: İzolasyon iyileştirme | 6.29 | Orta vadeli | 12,000 | 22,000 |
| 5 | P5: Economizer | 6.27 | Orta vadeli | 38,000 | 60,000 |
| 6 | P10: Pinch ısı entegrasyonu | 6.26 | Stratejik | 120,000 | 180,000 |
| 7 | P4: Kompresör VSD | 5.89 | Orta vadeli | 22,000 | 202,000 |
| 8 | P7: LED aydınlatma | 5.86 | Orta vadeli | 28,000 | 230,000 |
| 9 | P6: Kompresör ısı GK | 5.54 | Orta vadeli | 15,000 | 245,000 |
| 10 | P9: Chiller optimizasyon | 4.38 | Uzun vadeli | 35,000 | 280,000 |

### 5.6 Balon Grafik Konsepti (Bubble Chart)

```
Yıllık Tasarruf [€/yıl]
     |
 45K |                              ● P10 (büyük balon, €120K yatırım)
     |
 30K |
     |
 22K |  ● P3 (€6K)
     |
 18K |  ● P1 (€3.5K)              ● P5 (€38K)
     |
 12K |           ● P4 (€22K)
     |                    ● P7 (€28K)
  9K |                          ● P9 (€35K)
     |
  8K |  ● P2 (€0.5K)
  7K |           ● P6 (€15K)
  6K |       ● P8 (€12K)
     |____________________________________
     0    1     2     3     4    SPP [yıl]

Balon boyutu = Yatırım miktarı
Sol üst köşe = En cazip projeler (kısa SPP + yüksek tasarruf)
```

## 6. Bütçe Kısıtı Altında Portföy Optimizasyonu

### 6.1 Bütçe Senaryoları

```
Senaryo 1: Kısıtlı bütçe (€50,000)
Seçilen projeler (MCDA sırasına göre):
1. P3: Buhar kapanı → €6,000 (küm: €6,000)
2. P1: Hava kaçak → €3,500 (küm: €9,500)
3. P2: Basınç düşürme → €500 (küm: €10,000)
4. P8: İzolasyon → €12,000 (küm: €22,000)
5. P4: Kompresör VSD → €22,000 (küm: €44,000)

Toplam yatırım: €44,000 / €50,000
Toplam yıllık tasarruf: 22,000+17,000+8,500+6,500+12,000 = €66,000/yıl
Portföy SPP: 44,000 / 66,000 = 0.67 yıl
Toplam CO₂ azaltma: 55+42+21+30+30 = 178 tCO₂/yıl

Senaryo 2: Orta bütçe (€150,000)
Senaryo 1 + P5: Economizer + P7: LED + P6: Kompresör ısı GK
Toplam yatırım: €44,000 + 38,000 + 28,000 + 15,000 = €125,000
Toplam yıllık tasarruf: 66,000 + 18,000 + 11,000 + 7,500 = €102,500/yıl
Portföy SPP: 125,000 / 102,500 = 1.22 yıl
Toplam CO₂: 178 + 85 + 27 + 35 = 325 tCO₂/yıl

Senaryo 3: Geniş bütçe (€300,000)
Tüm projeler dahil: Toplam yatırım €280,000
Toplam yıllık tasarruf: €156,500/yıl
Portföy SPP: 280,000 / 156,500 = 1.79 yıl
Toplam CO₂: 557 tCO₂/yıl
```

### 6.2 Portföy Performans Karşılaştırması

| Senaryo | Bütçe [€] | Yatırım [€] | Tasarruf [€/yıl] | SPP [yıl] | CO₂ [tCO₂/yıl] | Proje Sayısı |
|---|---|---|---|---|---|---|
| Kısıtlı | 50,000 | 44,000 | 66,000 | 0.67 | 178 | 5 |
| Orta | 150,000 | 125,000 | 102,500 | 1.22 | 325 | 8 |
| Geniş | 300,000 | 280,000 | 156,500 | 1.79 | 557 | 10 |

```
Marjinal analiz:
- Kısıtlı → Orta: Ek €81,000 yatırım → ek €36,500/yıl (SPP: 2.22 yıl)
- Orta → Geniş: Ek €155,000 yatırım → ek €54,000/yıl (SPP: 2.87 yıl)

Sonuç: Marjinal getiri azalmaktadır. İlk projeler en yüksek getiriyi sağlar.
Bütçe artırımının mantıklılığı marjinal SPP ile değerlendirilmelidir.
```

## 7. Duyarlılık Analizi (Sensitivity Analysis)

### 7.1 Ağırlık Duyarlılığı

```
Baz senaryo ağırlıkları: Ekonomik %40, Teknik %30, Stratejik %30

Alternatif ağırlık senaryoları:

Senaryo A — Ekonomi odaklı (Ekonomik %60, Teknik %20, Stratejik %20):
1. P3 (8.56)  2. P1 (8.50)  3. P2 (8.14)  4. P8 (6.20)  5. P5 (5.68)
Değişim: Quick win'ler güçleniyor, P10 (stratejik) geriyor

Senaryo B — Teknik odaklı (Ekonomik %25, Teknik %50, Stratejik %25):
1. P3 (8.10)  2. P1 (7.93)  3. P2 (7.88)  4. P8 (6.72)  5. P7 (6.38)
Değişim: P7 (LED) yükseliyor (kolay uygulama), P10 geriyor

Senaryo C — Strateji odaklı (Ekonomik %25, Teknik %25, Stratejik %50):
1. P3 (7.82)  2. P10 (7.02)  3. P1 (6.97)  4. P5 (6.72)  5. P2 (6.50)
Değişim: P10 (Pinch) 2. sıraya yükseliyor (yüksek CO₂ azaltma)
```

### 7.2 Sıralama Kararlılığı

| Proje | Baz Sıra | Ek. Odaklı | Tek. Odaklı | Str. Odaklı | Kararlılık |
|---|---|---|---|---|---|
| P3 | 1 | 1 | 1 | 1 | Çok kararlı |
| P1 | 2 | 2 | 2 | 3 | Kararlı |
| P2 | 3 | 3 | 3 | 5 | Kararlı |
| P10 | 6 | 8 | 9 | 2 | Değişken |
| P9 | 10 | 10 | 10 | 10 | Kararlı (son) |

```
Duyarlılık sonuçları:
- P3, P1, P2: Her senaryoda ilk 5'te → SAĞLAM KARAR, uygulanmalı
- P10: Stratejik öncelikler artarsa ilk 3'e girer → YÖNETİM KARARI
- P9: Her durumda son sıra → ERTELENEBILIR
- P8, P5: Orta sıralarda kararlı → PLANA ALINMALI
```

## 8. Karar Ağacı (Decision Tree)

### 8.1 Proje Seçim Karar Ağacı

```
                     [PROJE DEĞERLENDİRME]
                            │
                    SPP < 1 yıl?
                    /            \
                EVET              HAYIR
                  │                 │
          Yatırım < €10K?      SPP < 3 yıl?
          /          \          /         \
       EVET          HAYIR   EVET        HAYIR
        │              │       │           │
   ┌─────────┐   ┌─────────┐ ┌──────┐  SPP < 5 yıl?
   │QUICK WIN│   │ Faz 1   │ │Faz 2 │  /        \
   │Hemen    │   │Öncelikli│ │Planlı│ EVET     HAYIR
   │uygula   │   │uygula   │ │yatırım│  │        │
   └─────────┘   └─────────┘ └──────┘ ┌──────┐ ┌──────┐
                                       │Strat.│ │Reddet│
                                       │proje │ │veya  │
                                       │(NPV  │ │özel  │
                                       │>0?)  │ │gerek.│
                                       └──────┘ └──────┘
```

### 8.2 Hızlı Değerlendirme Skorkartı

```
Hızlı proje değerlendirme (5 dakikada):

1. SPP < 2 yıl mı?              Evet: +3  Hayır: +0
2. Yatırım < €50,000 mi?        Evet: +2  Hayır: +0
3. Duruş gerektirmez mi?        Evet: +2  Hayır: +0
4. Kanıtlanmış teknoloji mi?    Evet: +2  Hayır: +0
5. CO₂ > 50 tCO₂/yıl mı?       Evet: +1  Hayır: +0

Toplam:
8-10: Derhal uygula
5-7:  Detaylı analiz yap ve planla
3-4:  Bütçe müsaitliğine göre değerlendir
0-2:  Erteleme veya reddet
```

## 9. Uygulama Yol Haritası Şablonu

### 9.1 Faz Bazlı Uygulama Planı

| Faz | Süre | Bütçe | Projeler | Beklenen Tasarruf |
|---|---|---|---|---|
| Faz 0: Quick Wins | 0-3 ay | €10,000 | P1, P2, P3 | €47,500/yıl |
| Faz 1: Kolay Projeler | 3-12 ay | €50,000 | P4, P8, P7 | €29,500/yıl |
| Faz 2: Orta Projeler | 12-24 ay | €65,000 | P5, P6, P9 | €34,500/yıl |
| Faz 3: Stratejik | 24-36 ay | €120,000 | P10 | €45,000/yıl |

### 9.2 Kümülatif Etki Projeksiyonu

```
Yıl 0 (başlangıç): Toplam tasarruf = €0
Yıl 0.25 (Faz 0 tamamlandıktan sonra):
  Yıllık tasarruf = €47,500/yıl
  Kümülatif yatırım = €10,000

Yıl 1 (Faz 1 tamamlandıktan sonra):
  Yıllık tasarruf = €47,500 + €29,500 = €77,000/yıl
  Kümülatif yatırım = €60,000
  Kümülatif tasarruf ≈ €57,000

Yıl 2 (Faz 2 tamamlandıktan sonra):
  Yıllık tasarruf = €77,000 + €34,500 = €111,500/yıl
  Kümülatif yatırım = €125,000
  Kümülatif tasarruf ≈ €148,000

Yıl 3 (Faz 3 tamamlandıktan sonra):
  Yıllık tasarruf = €111,500 + €45,000 = €156,500/yıl
  Kümülatif yatırım = €245,000
  Kümülatif tasarruf ≈ €293,000

Break-even (tüm yatırımın geri kazanılması): ~Yıl 2.5
5. Yıl sonu kümülatif net tasarruf: ~€538,000
```

## 10. Performans Değerlendirme

### 10.1 Portföy SPP Sınıflandırması

| Portföy SPP | Değerlendirme | Tipik Durum |
|---|---|---|
| <1 yıl | Mükemmel | Quick win ağırlıklı portföy |
| 1-2 yıl | İyi | Dengeli portföy |
| 2-3 yıl | Ortalama | Orta-büyük projeler ağırlıklı |
| 3-5 yıl | Düşük | Stratejik projeler ağırlıklı |
| >5 yıl | Kritik | Portföy yeniden değerlendirilmeli |

### 10.2 Başarı Kriterleri

```
Proje uygulama başarı izleme:

1. Gerçekleşen tasarruf / Planlanan tasarruf ≥ %80 → BAŞARILI
2. Gerçekleşen yatırım / Planlanan yatırım ≤ %120 → BÜTÇE DAHİLİNDE
3. Gerçekleşen süre / Planlanan süre ≤ %130 → ZAMANINDA
4. Operasyonel sorun yok → TEKNİK BAŞARI
5. Sürdürülebilir (12 ay sonra performans korunuyor) → KALICI

Tüm kriterler karşılanırsa: Tam başarı
3-4 kriter: Kısmi başarı
<3 kriter: Başarısız — kök neden analizi gerekli
```

## İlgili Dosyalar

- [Ekonomik Analiz](economic_analysis.md) — NPV, IRR, SPP hesaplama detayları
- [Yaşam Döngüsü Maliyet](life_cycle_cost.md) — LCC bazlı ekipman seçimi
- [Yardımcı Sistemler](utility_analysis.md) — Utility projeleri ve benchmark
- [Pinch Analizi](pinch_analysis.md) — Isı entegrasyonu projeleri
- [Enerji Yönetimi](energy_management.md) — ISO 50001 ve sürekli iyileştirme
- [Metodoloji](methodology.md) — Audit bulgu ve öneri formatı
- [KPI Tanımları](kpi_definitions.md) — Performans göstergeleri ve hedefler
- [Kazan Audit](../boiler/audit.md) — Kazan iyileştirme projeleri
- [Kompresör Audit](../compressor/audit.md) — Basınçlı hava iyileştirme projeleri
- [Chiller Audit](../chiller/audit.md) — Soğutma sistemi iyileştirme projeleri

## Referanslar

- Thumann, A. & Younger, W., "Handbook of Energy Audits," 9th Edition, Fairmont Press, 2012
- Turner, W.C. & Doty, S., "Energy Management Handbook," 9th Edition, Fairmont Press, 2013
- Belton, V. & Stewart, T.J., "Multiple Criteria Decision Analysis: An Integrated Approach," Kluwer Academic Publishers, 2002
- Saaty, T.L., "The Analytic Hierarchy Process," McGraw-Hill, 1980
- US DOE, "Guidelines for Techno-Economic Analysis of Energy Technologies"
- European Commission, "Guide to Cost-Benefit Analysis of Investment Projects," 2014
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- ASHRAE, "Procedures for Commercial Building Energy Audits," 2nd Edition, 2011
- Keeney, R.L. & Raiffa, H., "Decisions with Multiple Objectives," Cambridge University Press, 1993
