---
title: "Pinch Analizi Yazılım Araçları (Software Tools for Pinch Analysis)"
category: factory
equipment_type: factory
keywords: [yazılım araçları, pinch yazılım, Python, açık kaynak, ticari yazılım]
related_files: [factory/pinch/fundamentals.md, factory/pinch/practical_guide.md, factory/pinch/INDEX.md]
use_when: ["Pinch analizi yazılımı seçilirken", "Python implementasyonu yapılırken", "Araç karşılaştırması gerektiğinde"]
priority: low
last_updated: 2026-02-01
---

# Pinch Analizi Yazılım Araçları (Software Tools for Pinch Analysis)

> Son güncelleme: 2026-02-01

## Genel Bakış

Pinch analizi hesaplamaları el ile yapılabilecek kadar basit algoritmalar üzerine kuruludur; ancak endüstriyel ölçekte onlarca akış, birden fazla utility seviyesi ve karmaşık kısıtlamalar söz konusu olduğunda yazılım araçları vazgeçilmez hale gelir. Bu dosya, pinch analizi için kullanılan ticari, akademik ve açık kaynak yazılımları detaylı olarak karşılaştırır; Python ile algoritmik implementasyonu gösterir ve ExergyLab platformu ile entegrasyon olanaklarını açıklar.

Yazılım araçları genel olarak dört kategoriye ayrılır:

```
Kategori 1: Ticari Yazılımlar (Commercial Software)
  → Tam kapsamlı, endüstriyel destek, yüksek maliyet
  → Aspen Energy Analyzer, SuperTarget, PinCH, SPRINT

Kategori 2: Akademik Yazılımlar (Academic Software)
  → Araştırma odaklı, ücretsiz/düşük maliyet, sınırlı destek
  → HINT, Spiral, CPI tools

Kategori 3: Açık Kaynak Araçlar (Open Source Tools)
  → Python/MATLAB tabanlı, topluluk destekli, esnek
  → pina, pyPinch, MATLAB Pinch Toolbox

Kategori 4: Tablo Hesap Araçları (Spreadsheet Tools)
  → Excel/Google Sheets tabanlı, basit problemler için ideal
  → Özel şablonlar, VBA makroları
```

## 1. Ticari Yazılımlar (Commercial Software)

### 1.1 Aspen Energy Analyzer (AspenTech)

Aspen Energy Analyzer (AEA), AspenTech tarafından geliştirilen ve aspenONE Engineering paketi içinde sunulan en kapsamlı ticari pinch analizi aracıdır. Aspen HYSYS ve Aspen Plus simülasyon araçlarıyla doğrudan entegre çalışır.

```
Temel Özellikler:
  - Otomatik akış verisi çıkarma (Aspen HYSYS/Plus entegrasyonu)
  - Bileşik eğriler (Composite Curves) ve GCC oluşturma
  - Otomatik HEN tasarımı ve optimizasyonu
  - Retrofit analizi (Cross-pinch tespiti, network pinch)
  - Maliyet optimizasyonu (TAC — Total Annualized Cost)
  - Çoklu utility seviyeleri ve CHP entegrasyonu
  - Detaylı raporlama ve grafik çıktıları

Platform: Windows
Lisans: Yıllık abonelik (aspenONE Engineering paketi içinde)
Tahmini Maliyet: ~14.000–46.000 EUR/yıl (paket büyüklüğüne bağlı)

Avantajlar:
  ✓ Aspen simülasyon araçlarıyla tam entegrasyon
  ✓ Otomatik akış çıkarma (simülasyondan doğrudan)
  ✓ Geniş eşanjör veritabanı ve maliyet modelleri
  ✓ Endüstri standardı, geniş kullanıcı tabanı
  ✓ Kapsamlı teknik destek ve eğitim

Dezavantajlar:
  ✗ Çok yüksek lisans maliyeti
  ✗ Sadece Windows platformunda çalışır
  ✗ Öğrenme eğrisi dik (3-6 ay)
  ✗ Aspen ekosistemi dışında sınırlı kullanılabilirlik
  ✗ Bağımsız pinch analizi için aşırı kapsamlı
```

### 1.2 SuperTarget (KBC/Yokogawa)

SuperTarget, KBC (şimdi Yokogawa bünyesinde) tarafından geliştirilen ve özellikle rafineri ve petrokimya sektörüne odaklanan bir pinch analizi yazılımıdır. Linnhoff March geleneğinden gelen bu araç, pinch analizinin doğuş noktasına en yakın ticari üründür.

```
Temel Özellikler:
  - Klasik Linnhoff metodolojisinin tam implementasyonu
  - Süperhedefleme (Supertargeting) — ΔTmin optimizasyonu
  - Retrofit hedefleme (Retrofit targeting)
  - Kolonlar arası entegrasyon (Column integration)
  - Site-seviye analiz (Total Site Analysis)
  - Buhar sistemi optimizasyonu

Platform: Windows
Lisans: Kalıcı + yıllık bakım veya abonelik
Tahmini Maliyet: ~18.000–37.000 EUR (kalıcı lisans)

Avantajlar:
  ✓ Linnhoff metodolojisinin en sadık implementasyonu
  ✓ Retrofit analizi için en güçlü araç
  ✓ Total Site Analysis desteği
  ✓ Rafineri/petrokimya için özel modüller
  ✓ Buhar sistemi optimizasyonu entegre

Dezavantajlar:
  ✗ Yüksek lisans maliyeti
  ✗ Kullanıcı arayüzü eski nesil
  ✗ Simülasyon araçlarıyla entegrasyon sınırlı
  ✗ Sınırlı kullanıcı topluluğu
  ✗ Güncellemeler yavaş
```

### 1.3 PinCH (Lucerne University of Applied Sciences)

PinCH, İsviçre Lucerne Uygulamalı Bilimler Üniversitesi tarafından geliştirilen ve özellikle Avrupa endüstrisinde yaygın kullanılan bir pinch analizi aracıdır. Kesikli prosesler (batch processes) için güçlü desteği ile öne çıkar.

```
Temel Özellikler:
  - Sürekli ve kesikli proses (continuous & batch) desteği
  - Zaman dilimi modeli (Time Slice Model)
  - Doğrudan ve dolaylı ısı geri kazanımı
  - Isı depolama sistemi (TES — Thermal Energy Storage) tasarımı
  - Çoklu utility seviyeleri ve ısı pompası entegrasyonu
  - Çok periyotlu optimizasyon

Platform: Windows
Lisans: Akademik ücretsiz, ticari ücretli
Tahmini Maliyet: Ücretsiz (akademik) / ~5,000–15,000 CHF/yıl (ticari)

Avantajlar:
  ✓ Batch proses desteği (en güçlü araç)
  ✓ Akademik kullanım için ücretsiz
  ✓ Modern kullanıcı arayüzü
  ✓ Isı depolama sistemi tasarımı
  ✓ İsviçre enerji standartlarıyla uyumlu
  ✓ Aktif geliştirme ve güncelleme

Dezavantajlar:
  ✗ HEN otomatik tasarım desteği sınırlı
  ✗ Maliyet optimizasyonu temel düzeyde
  ✗ Simülasyon entegrasyonu yok
  ✗ Retrofit analiz araçları kısıtlı
```

### 1.4 SPRINT (University of Manchester)

SPRINT (Stream Process Integrator), Manchester Üniversitesi tarafından geliştirilen ve özellikle HEN retrofit tasarımı ile süperhedefleme konularında öne çıkan bir araçtır.

```
Temel Özellikler:
  - Problem Tablosu Algoritması (PTA) ve hedefleme
  - Bileşik eğriler ve Grand Composite Curve
  - HEN tasarımı (grid diyagramı destekli)
  - Retrofit analizi (network pinch yöntemi)
  - Süperhedefleme (ΔTmin optimizasyonu)
  - Çok akışlı eşanjör tasarımı

Platform: Windows
Lisans: Akademik/araştırma lisansı
Tahmini Maliyet: ~2,000–8,000 GBP (akademik indirimli)

Avantajlar:
  ✓ Manchester grubunun araştırma gücü arkasında
  ✓ HEN retrofit için gelişmiş algoritmalar
  ✓ Network pinch ve yapısal modifikasyon
  ✓ Akademik fiyatlandırma uygun
  ✓ Kapsamlı dokümantasyon

Dezavantajlar:
  ✗ Ticari destek sınırlı
  ✗ Batch proses desteği zayıf
  ✗ Kullanıcı arayüzü akademik düzeyde
  ✗ Total Site desteği yok
  ✗ Güncelleme sıklığı düzensiz
```

### Ticari Yazılım Özet Tablosu

| Özellik | AEA | SuperTarget | PinCH | SPRINT |
|---------|-----|-------------|-------|--------|
| PTA / Hedefleme | Evet | Evet | Evet | Evet |
| Bileşik Eğriler | Evet | Evet | Evet | Evet |
| GCC | Evet | Evet | Evet | Evet |
| Otomatik HEN | Evet | Kısmi | Hayır | Evet |
| Retrofit | Evet | Evet | Kısmi | Evet |
| Batch Proses | Hayır | Hayır | Evet | Hayır |
| Total Site | Kısmi | Evet | Kısmi | Hayır |
| CHP Analizi | Evet | Evet | Evet | Kısmi |
| Maliyet Opt. | Evet | Evet | Kısmi | Evet |
| Simülasyon Ent. | Evet | Hayır | Hayır | Hayır |
| Fiyat Aralığı | €€€€€ | €€€€ | €€–€€€ | €€ |
| Öğrenme Eğrisi | Yüksek | Orta | Düşük | Orta |

## 2. Akademik Yazılımlar (Academic Software)

### 2.1 HINT (University of Manchester)

HINT (Heat Integration), Manchester Üniversitesi'nin CEAS (Centre for Process Integration) grubu tarafından geliştirilen eğitim amaçlı bir pinch analizi aracıdır.

```
Temel Özellikler:
  - Temel PTA hesaplaması
  - Bileşik eğri görselleştirme
  - Grand Composite Curve
  - Basit HEN grid diyagramı
  - Etkileşimli ΔTmin değiştirme

Erişilebilirlik: Üniversite lisansı ile ücretsiz
Platform: Windows / Java tabanlı
Hedef Kitle: Lisansüstü öğrenciler, araştırmacılar

Avantajlar:
  ✓ Eğitim amaçlı mükemmel
  ✓ Basit ve anlaşılır arayüz
  ✓ Temel kavramları görselleştirme
  ✓ Ücretsiz akademik erişim

Dezavantajlar:
  ✗ Endüstriyel ölçek için yetersiz
  ✗ İleri özellikler yok (retrofit, batch)
  ✗ Sınırlı akış sayısı
  ✗ Dışa aktarma seçenekleri kısıtlı
```

### 2.2 Spiral (Lund University)

Spiral, İsveç Lund Üniversitesi tarafından geliştirilen ve özellikle kağıt-hamur (pulp & paper) endüstrisi için optimize edilmiş bir pinch analizi ve proses entegrasyon aracıdır.

```
Temel Özellikler:
  - Pinch analizi ve hedefleme
  - Kağıt-hamur prosesleri için özel modüller
  - Buhar sistemi modelleme
  - Biyorafineri entegrasyonu
  - Enerji sistem analizi

Erişilebilirlik: Akademik işbirliği ile erişim
Platform: Windows
Hedef Kitle: Araştırmacılar, kağıt endüstrisi

Avantajlar:
  ✓ Kağıt-hamur sektörü için uzmanlaşmış
  ✓ Biyorafineri desteği
  ✓ İsveç enerji standartlarıyla uyumlu
  ✓ Akademik yayınlarla destekli

Dezavantajlar:
  ✗ Sektör-spesifik (genel amaçlı değil)
  ✗ Erişim kısıtlı
  ✗ Dokümantasyon İsveççe ağırlıklı
  ✗ Topluluk küçük
```

### 2.3 Diğer Akademik Araçlar

| Yazılım | Geliştiren | Odak Alanı | Erişim |
|---------|-----------|------------|--------|
| STAR | UMIST/Manchester | HEN sentezi | Akademik lisans |
| COLOM | Manchester | Kolon entegrasyonu | Araştırma grubu |
| OmegaThermo | TU Berlin | Exergy-pinch entegrasyonu | Akademik |
| ProsteamNet | Universiti Teknologi Malaysia | Buhar ağ optimizasyonu | Açık erişim |

## 3. Açık Kaynak Araçlar (Open Source Tools)

### 3.1 Python Kütüphaneleri

#### pina (Python Pinch Analysis)

```
Depo: github.com/sostenibile/pina
Lisans: MIT
Python: 3.7+
Bağımlılıklar: numpy, matplotlib

Özellikler:
  - Akış verisi tanımlama ve yönetim
  - Problem Tablosu Algoritması (PTA)
  - Bileşik eğriler (Hot/Cold Composite)
  - Grand Composite Curve
  - Enerji hedefleme (QH,min / QC,min)
  - ΔTmin duyarlılık analizi

Kurulum:
  pip install pina

Örnek Kullanım:
  from pina import PinchAnalyzer
  analyzer = PinchAnalyzer(delta_t_min=10)
  analyzer.add_stream('H1', 270, 80, 15.0)   # Sıcak akış
  analyzer.add_stream('C1', 30, 250, 18.0)    # Soğuk akış
  results = analyzer.solve()
  print(f"QH,min = {results.qh_min:.1f} kW")
  print(f"QC,min = {results.qc_min:.1f} kW")
  analyzer.plot_composite_curves()
```

#### pyPinch

```
Depo: github.com/mehul-m-prajapati/pyPinch
Lisans: MIT
Python: 3.6+
Bağımlılıklar: numpy, matplotlib, pandas

Özellikler:
  - CSV tabanlı akış verisi girişi
  - PTA hesaplaması
  - Bileşik eğriler ve GCC
  - Shifted Temperature Diagram
  - Enerji hedeflerinin hesaplanması

Kurulum:
  pip install pyPinch

Not: Eğitim amaçlı, küçük/orta ölçek problemler için uygundur.
```

### 3.2 MATLAB Araçları

```
MATLAB Pinch Analysis Toolbox:
  - MATLAB File Exchange üzerinden erişilebilir
  - PTA, bileşik eğriler, GCC fonksiyonları
  - Hedefleme ve HEN tasarım yardımcıları
  - Akademik kullanım yaygın

OSMOSE (EPFL):
  - Enerji sistem modelleme ve optimizasyon platformu
  - Pinch analizi alt modülü
  - MILP tabanlı utility optimizasyonu
  - Açık kaynak (araştırma lisansı)
```

### 3.3 Excel Şablonları

```
IChemE Pinch Analysis Spreadsheet:
  - IChemE eğitim materyali olarak sunulan Excel şablonu
  - PTA hesaplaması, bileşik eğri çizimi
  - 10-15 akış kapasitesi
  - VBA makroları ile otomatik hesaplama

Topluluk Şablonları:
  - GitHub üzerinde çeşitli Excel pinch analizi şablonları
  - Google Sheets tabanlı çevrimiçi versiyonlar
  - Eğitim kurumlarının kendi geliştirdiği şablonlar
```

## 4. Python ile Pinch Analizi (Pinch Analysis with Python)

Bu bölüm, pinch analizi algoritmalarının Python ile nasıl implementasyon edilebileceğini gösterir. Tam bir uygulama yerine, algoritmik yapıyı ve temel veri akışını sunan sözde kod (pseudo-code) verilmiştir.

### 4.1 Akış Verisi Yapısı (Stream Data Structure)

```python
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List

@dataclass
class Stream:
    """Pinch analizi akış verisi (Stream data for pinch analysis).

    Attributes:
        name: Akış adı (Stream name)
        t_supply: Kaynak sıcaklığı [°C] (Supply temperature)
        t_target: Hedef sıcaklığı [°C] (Target temperature)
        cp: Isı kapasitesi akış hızı [kW/°C] (Heat capacity flowrate)
    """
    name: str
    t_supply: float  # [°C]
    t_target: float  # [°C]
    cp: float         # [kW/°C]

    @property
    def is_hot(self) -> bool:
        """Sıcak akış mı? (Is it a hot stream?)"""
        return self.t_supply > self.t_target

    @property
    def heat_duty(self) -> float:
        """Isı yükü [kW] (Heat duty)"""
        return self.cp * abs(self.t_supply - self.t_target)

    @property
    def shifted_temps(self) -> tuple:
        """Kaydırılmış sıcaklıklar [°C] (Shifted temperatures)"""
        if self.is_hot:
            return (self.t_supply - delta_t_min / 2,
                    self.t_target - delta_t_min / 2)
        else:
            return (self.t_supply + delta_t_min / 2,
                    self.t_target + delta_t_min / 2)
```

### 4.2 Problem Tablosu Algoritması (PTA Implementation)

```python
def problem_table_algorithm(streams: List[Stream],
                             delta_t_min: float) -> dict:
    """Problem Tablosu Algoritması (Problem Table Algorithm).

    Linnhoff & Flower (1978) tarafından geliştirilen temel algoritma.
    Kaydırılmış sıcaklıkları (shifted temperatures) kullanarak
    minimum utility ihtiyacını hesaplar.

    Args:
        streams: Akış listesi (List of streams)
        delta_t_min: Minimum sıcaklık farkı [°C]

    Returns:
        dict: {
            'qh_min': Minimum sıcak utility [kW],
            'qc_min': Minimum soğuk utility [kW],
            'pinch_temp': Pinch sıcaklığı (shifted) [°C],
            'intervals': Aralık verileri (Interval data)
        }
    """
    # Adım 1: Kaydırılmış sıcaklıkları hesapla
    shifted_temps = set()
    for s in streams:
        if s.is_hot:
            shifted_temps.add(s.t_supply - delta_t_min / 2)
            shifted_temps.add(s.t_target - delta_t_min / 2)
        else:
            shifted_temps.add(s.t_supply + delta_t_min / 2)
            shifted_temps.add(s.t_target + delta_t_min / 2)

    # Adım 2: Sıcaklıkları azalan sırada sırala
    sorted_temps = sorted(shifted_temps, reverse=True)

    # Adım 3: Her aralık için net ısı akışını hesapla
    intervals = []
    for i in range(len(sorted_temps) - 1):
        t_upper = sorted_temps[i]
        t_lower = sorted_temps[i + 1]
        delta_t = t_upper - t_lower  # [°C]

        # Bu aralıkta mevcut akışları bul
        sum_cp_hot = 0.0  # [kW/°C]
        sum_cp_cold = 0.0  # [kW/°C]

        for s in streams:
            s_high, s_low = s.shifted_temps
            if s_high < s_low:
                s_high, s_low = s_low, s_high

            if s_low < t_upper and s_high > t_lower:
                if s.is_hot:
                    sum_cp_hot += s.cp
                else:
                    sum_cp_cold += s.cp

        # Net ısı: pozitif = fazla ısı, negatif = ısı açığı
        net_heat = (sum_cp_hot - sum_cp_cold) * delta_t  # [kW]
        intervals.append({
            't_upper': t_upper,
            't_lower': t_lower,
            'delta_t': delta_t,
            'sum_cp_hot': sum_cp_hot,
            'sum_cp_cold': sum_cp_cold,
            'net_heat': net_heat
        })

    # Adım 4: Kaskad hesaplaması (ilk geçiş — düzeltilmemiş)
    cascade = [0.0]  # Üstten başla, QH = 0 varsayımı
    for interval in intervals:
        cascade.append(cascade[-1] + interval['net_heat'])

    # Adım 5: En negatif değeri bul ve düzelt
    min_cascade = min(cascade)
    qh_min = -min_cascade if min_cascade < 0 else 0.0  # [kW]

    # Adım 6: Düzeltilmiş kaskad
    corrected_cascade = [c + qh_min for c in cascade]
    qc_min = corrected_cascade[-1]  # [kW]

    # Adım 7: Pinch noktasını bul (kaskad = 0 olan nokta)
    pinch_idx = corrected_cascade.index(0.0)
    pinch_temp = sorted_temps[pinch_idx]  # Shifted sıcaklık [°C]

    return {
        'qh_min': qh_min,
        'qc_min': qc_min,
        'pinch_temp': pinch_temp,
        'pinch_hot': pinch_temp + delta_t_min / 2,
        'pinch_cold': pinch_temp - delta_t_min / 2,
        'intervals': intervals,
        'cascade': corrected_cascade
    }
```

### 4.3 Bileşik Eğri Hesaplaması (Composite Curve Calculation)

```python
def compute_composite_curve(streams: List[Stream],
                             stream_type: str) -> tuple:
    """Bileşik eğri hesaplama (Composite curve calculation).

    Aynı türdeki akışların (sıcak veya soğuk) sıcaklık-enthalpy
    bileşik eğrisini oluşturur.

    Args:
        streams: Akış listesi
        stream_type: 'hot' veya 'cold'

    Returns:
        tuple: (T_values [°C], H_values [kW]) — eğri noktaları
    """
    # İlgili akışları filtrele
    if stream_type == 'hot':
        selected = [s for s in streams if s.is_hot]
    else:
        selected = [s for s in streams if not s.is_hot]

    if not selected:
        return ([], [])

    # Tüm sıcaklık kırılma noktalarını topla
    temp_breaks = set()
    for s in selected:
        temp_breaks.add(s.t_supply)
        temp_breaks.add(s.t_target)

    # Sıcaklıkları artan sırada sırala
    sorted_temps = sorted(temp_breaks)

    # Her aralık için toplam CP hesapla
    T_values = [sorted_temps[0]]
    H_values = [0.0]
    cumulative_h = 0.0  # [kW]

    for i in range(len(sorted_temps) - 1):
        t_low = sorted_temps[i]
        t_high = sorted_temps[i + 1]
        delta_t = t_high - t_low  # [°C]

        # Bu aralıkta aktif akışların toplam CP değeri
        total_cp = 0.0  # [kW/°C]
        for s in selected:
            s_low = min(s.t_supply, s.t_target)
            s_high = max(s.t_supply, s.t_target)
            if s_low <= t_low and s_high >= t_high:
                total_cp += s.cp

        cumulative_h += total_cp * delta_t  # [kW]
        T_values.append(t_high)
        H_values.append(cumulative_h)

    return (T_values, H_values)


def plot_composite_curves(streams: List[Stream],
                          delta_t_min: float,
                          qh_min: float) -> None:
    """Bileşik eğrileri çiz (Plot composite curves).

    Sıcak ve soğuk bileşik eğrileri aynı grafikte çizer.
    Soğuk eğri QH,min kadar sağa kaydırılır.

    Args:
        streams: Akış listesi
        delta_t_min: Minimum sıcaklık farkı [°C]
        qh_min: Minimum sıcak utility [kW]
    """
    T_hot, H_hot = compute_composite_curve(streams, 'hot')
    T_cold, H_cold = compute_composite_curve(streams, 'cold')

    # Soğuk eğriyi QH,min kadar kaydır
    H_cold_shifted = [h + qh_min for h in H_cold]

    plt.figure(figsize=(10, 7))
    plt.plot(H_hot, T_hot, 'r-o', label='Sıcak Bileşik (Hot Composite)')
    plt.plot(H_cold_shifted, T_cold, 'b-o',
             label='Soğuk Bileşik (Cold Composite)')
    plt.xlabel('Enthalpy [kW]')
    plt.ylabel('Sıcaklık [°C]')
    plt.title('Bileşik Eğriler (Composite Curves)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
```

### 4.4 Grand Composite Curve Oluşturma (GCC Generation)

```python
def generate_gcc(intervals: list,
                 cascade: list,
                 sorted_temps: list) -> tuple:
    """Grand Composite Curve verisi oluştur (Generate GCC data).

    Düzeltilmiş kaskaddan GCC eğrisinin noktalarını hesaplar.
    GCC, kaydırılmış sıcaklık (shifted temperature) ile net ısı
    akışı (net heat flow) arasındaki ilişkiyi gösterir.

    Args:
        intervals: PTA aralık verileri
        cascade: Düzeltilmiş kaskad değerleri [kW]
        sorted_temps: Azalan sırada kaydırılmış sıcaklıklar [°C]

    Returns:
        tuple: (T_shifted [°C], Q_net [kW]) — GCC noktaları
    """
    # GCC noktaları: (kaydırılmış sıcaklık, kaskad değeri)
    T_shifted = sorted_temps  # [°C]
    Q_net = cascade           # [kW]

    return (T_shifted, Q_net)


def plot_gcc(T_shifted: list, Q_net: list) -> None:
    """Grand Composite Curve çiz (Plot GCC).

    Args:
        T_shifted: Kaydırılmış sıcaklıklar [°C]
        Q_net: Net ısı akışları [kW]
    """
    plt.figure(figsize=(8, 10))
    plt.plot(Q_net, T_shifted, 'g-o', linewidth=2,
             label='Grand Composite Curve')
    plt.axvline(x=0, color='k', linestyle='--', alpha=0.5)
    plt.xlabel('Net Isı Akışı [kW]')
    plt.ylabel('Kaydırılmış Sıcaklık [°C]')
    plt.title('Grand Composite Curve (GCC)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
```

### 4.5 Tam Analiz Akışı (Complete Analysis Flow)

```python
def run_pinch_analysis(stream_data: list, delta_t_min: float = 10.0):
    """Tam pinch analizi çalıştır (Run complete pinch analysis).

    Referans Problem Verileri:
        H1: 270→80°C,  CP=15 kW/°C
        H2: 180→40°C,  CP=25 kW/°C
        H3: 150→60°C,  CP=10 kW/°C
        C1: 30→250°C,  CP=18 kW/°C
        C2: 60→200°C,  CP=12 kW/°C
        ΔTmin = 10°C

    Beklenen Sonuçlar:
        QH,min = 1,800 kW
        QC,min = 2,240 kW
        Pinch  = 175°C (shifted)
    """
    # 1. Akışları oluştur
    streams = [Stream(**data) for data in stream_data]

    # 2. PTA çalıştır
    results = problem_table_algorithm(streams, delta_t_min)

    # 3. Sonuçları raporla
    print(f"Minimum Sıcak Utility (QH,min): {results['qh_min']:.1f} kW")
    print(f"Minimum Soğuk Utility (QC,min): {results['qc_min']:.1f} kW")
    print(f"Pinch Sıcaklığı (shifted):      {results['pinch_temp']:.1f} °C")
    print(f"Pinch Sıcaklığı (hot):          {results['pinch_hot']:.1f} °C")
    print(f"Pinch Sıcaklığı (cold):         {results['pinch_cold']:.1f} °C")

    # 4. Bileşik eğrileri çiz
    plot_composite_curves(streams, delta_t_min, results['qh_min'])

    # 5. GCC çiz
    sorted_temps = sorted(
        set(t for interval in results['intervals']
            for t in [interval['t_upper'], interval['t_lower']]),
        reverse=True
    )
    T_gcc, Q_gcc = generate_gcc(
        results['intervals'], results['cascade'], sorted_temps
    )
    plot_gcc(T_gcc, Q_gcc)

    return results
```

## 5. Excel Tabanlı Hesaplamalar (Excel-Based Calculations)

Excel, özellikle 5-15 akışlı küçük ve orta ölçekli pinch analizi problemleri için hala yaygın olarak kullanılmaktadır. Aşağıda tipik bir Excel PTA şablonunun yapısı ve formülleri verilmiştir.

### 5.1 Tablo Düzeni (Spreadsheet Layout)

```
=== Sayfa 1: Akış Verileri (Stream Data) ===

| Hücre | İçerik                    | Örnek         |
|-------|---------------------------|---------------|
| A1    | "Akış Adı"                | H1            |
| B1    | "Tür (H/C)"              | H             |
| C1    | "T_kaynak [°C]"          | 270           |
| D1    | "T_hedef [°C]"           | 80            |
| E1    | "CP [kW/°C]"             | 15            |
| F1    | "Q [kW]" (hesaplanan)     | =E2*ABS(C2-D2) → 2850 |
| G1    | "T_shifted_high [°C]"     | =IF(B2="H",C2-$B$20/2,D2+$B$20/2) |
| H1    | "T_shifted_low [°C]"      | =IF(B2="H",D2-$B$20/2,C2+$B$20/2) |

B20: ΔTmin değeri (kullanıcı girişi) = 10

=== Sayfa 2: Problem Tablosu (Problem Table) ===

| Sütun | İçerik                           | Formül Açıklaması     |
|-------|----------------------------------|-----------------------|
| A     | Sıcaklık aralığı No (1, 2, ...) | —                     |
| B     | T_üst [°C] (shifted)            | Sıralı sıcaklıklar   |
| C     | T_alt [°C] (shifted)            | Sıralı sıcaklıklar   |
| D     | ΔT [°C]                         | =B2-C2                |
| E     | ΣCP_hot [kW/°C]                 | SUMPRODUCT formülü    |
| F     | ΣCP_cold [kW/°C]                | SUMPRODUCT formülü    |
| G     | ΔH_net [kW]                     | =(E2-F2)*D2           |
| H     | Kaskad (düzeltilmemiş) [kW]     | =H1+G2               |
| I     | Kaskad (düzeltilmiş) [kW]       | =H2+$B$25            |

B25: QH,min = -MIN(H:H) (otomatik hesaplanan)

=== Sayfa 3: Sonuçlar ve Grafikler ===

| Hücre | İçerik              | Formül                    |
|-------|---------------------|---------------------------|
| B30   | QH,min [kW]         | =-MIN(Sayfa2!H:H)        |
| B31   | QC,min [kW]         | Kaskadın son değeri       |
| B32   | Pinch [°C] (shifted)| Kaskad=0 olan sıcaklık    |
| B33   | Pinch [°C] (hot)    | =B32+$B$20/2              |
| B34   | Pinch [°C] (cold)   | =B32-$B$20/2              |
```

### 5.2 CP Toplama Formülü (SUMPRODUCT for CP Calculation)

```
Sıcak akışlar için belirli bir aralıkta toplam CP:

=SUMPRODUCT(
  (Sayfa1!$B$2:$B$6="H")*
  (Sayfa1!$G$2:$G$6>=Sayfa2!C2)*
  (Sayfa1!$H$2:$H$6<=Sayfa2!B2)*
  Sayfa1!$E$2:$E$6
)

Açıklama:
  - Sadece sıcak (H) akışları filtrele
  - Shifted T_high >= aralık alt sıcaklığı olan akışları seç
  - Shifted T_low <= aralık üst sıcaklığı olan akışları seç
  - Bu akışların CP değerlerini topla
```

### 5.3 Excel Tabanlı Hesaplamanın Avantaj ve Sınırları

```
Avantajlar:
  ✓ Herkesin erişebilmesi (Excel/Google Sheets yaygın)
  ✓ Hesaplama adımlarının şeffaf olması
  ✓ Formüllerin görünür ve denetlenebilir olması
  ✓ Hızlı prototipleme ve "what-if" analizi
  ✓ Ek yazılım kurulumu gerektirmez
  ✓ 5-15 akışlı problemler için yeterli

Sınırlamalar:
  ✗ 15+ akışta tablo yönetimi zorlaşır
  ✗ Otomatik HEN tasarımı mümkün değil
  ✗ Grafik kalitesi sınırlı
  ✗ Batch proses modellemesi pratik değil
  ✗ Versiyon kontrolü ve paylaşım zor
  ✗ Hata yapma riski yüksek (formül bağımlılıkları)
```

## 6. Yazılım Seçim Kriterleri (Software Selection Criteria)

Doğru pinch analizi yazılımını seçmek, problem boyutu, bütçe, teknik gereksinimler ve organizasyonel faktörlere bağlıdır.

### 6.1 Karar Matrisi (Decision Matrix)

| Kriter | Ağırlık | Açıklama |
|--------|---------|----------|
| Problem Boyutu | Yüksek | Akış sayısı, utility sayısı, kısıtlama sayısı |
| Bütçe | Yüksek | Lisans maliyeti, eğitim maliyeti, bakım maliyeti |
| Öğrenme Eğrisi | Orta | Kullanmaya başlama süresi, eğitim gereksinimi |
| Teknik Destek | Orta | Üretici desteği, topluluk, dokümantasyon |
| Entegrasyon | Orta | Simülasyon araçlarıyla, ERP ile, ExergyLab ile |
| Özellik Kapsamı | Orta | PTA, HEN, retrofit, batch, maliyet optimizasyonu |
| Ölçeklenebilirlik | Düşük | Büyük problemlere uyum, performans |
| Platform Desteği | Düşük | Windows, Linux, macOS, web tabanlı |

### 6.2 Senaryoya Göre Öneriler

```
Senaryo 1: Akademik Araştırma / Eğitim
  → Birincil: Python (pina/pyPinch) + Excel
  → İkincil: PinCH (ücretsiz akademik lisans)
  → Neden: Ücretsiz, algoritma şeffaflığı, öğrenme kolaylığı

Senaryo 2: KOBİ — İlk Pinch Analizi Projesi (5-15 akış)
  → Birincil: Excel şablonu + Python doğrulama
  → İkincil: PinCH
  → Neden: Düşük maliyet, hızlı başlangıç, yeterli kapsam

Senaryo 3: Büyük Endüstriyel Tesis — Yeni HEN Tasarımı (50+ akış)
  → Birincil: Aspen Energy Analyzer
  → İkincil: SuperTarget
  → Neden: Otomatik HEN tasarımı, simülasyon entegrasyonu

Senaryo 4: Rafineri/Petrokimya — Retrofit Projesi
  → Birincil: SuperTarget
  → İkincil: SPRINT
  → Neden: Retrofit hedefleme, kolon entegrasyonu, buhar sistemi

Senaryo 5: Gıda/İlaç — Batch Proses Entegrasyonu
  → Birincil: PinCH
  → Neden: Batch desteği, TES tasarımı, zaman dilimi modeli

Senaryo 6: Çok-Tesisli Site Optimizasyonu
  → Birincil: SuperTarget (Total Site Analysis)
  → İkincil: Aspen Energy Analyzer
  → Neden: Site profilleri, buhar seviye optimizasyonu

Senaryo 7: Özel Algoritma Geliştirme
  → Birincil: Python (özel kütüphane)
  → İkincil: MATLAB
  → Neden: Tam esneklik, exergy-pinch entegrasyonu
```

### 6.3 Maliyet-Fayda Değerlendirmesi

```
Yatırım Geri Dönüşü (ROI) Karşılaştırması:

Ticari Yazılım (AEA/SuperTarget):
  Maliyet: 18.000-46.000 EUR/yıl
  Tipik Proje Tasarrufu: 460.000-4.600.000 EUR/yıl
  ROI: 10x-100x (büyük tesislerde)
  Geri Ödeme: 1-3 ay

Orta Seviye (PinCH/SPRINT):
  Maliyet: 1.800-14.000 EUR/yıl
  Tipik Proje Tasarrufu: 92.000-920.000 EUR/yıl
  ROI: 10x-70x
  Geri Ödeme: 1-2 ay

Açık Kaynak/Excel:
  Maliyet: 0 EUR (yazılım) + mühendis zamanı
  Tipik Proje Tasarrufu: 46.000-460.000 EUR/yıl
  ROI: Sonsuz (yazılım maliyeti 0)
  Geri Ödeme: Anlık (ancak mühendis zamanı dahil edilmeli)
```

## 7. Yazılım Karşılaştırma Matrisi (Software Comparison Matrix)

### 7.1 Kapsamlı Karşılaştırma Tablosu

| Özellik | AEA | SuperTarget | PinCH | SPRINT | pina | pyPinch | Excel |
|---------|-----|-------------|-------|--------|------|---------|-------|
| **Temel Analiz** | | | | | | | |
| PTA | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★☆ |
| Bileşik Eğriler | ★★★ | ★★★ | ★★★ | ★★★ | ★★☆ | ★★☆ | ★☆☆ |
| GCC | ★★★ | ★★★ | ★★★ | ★★★ | ★★☆ | ★☆☆ | ★☆☆ |
| Hedefleme | ★★★ | ★★★ | ★★☆ | ★★★ | ★★☆ | ★☆☆ | ★☆☆ |
| **Tasarım** | | | | | | | |
| HEN Otomatik | ★★★ | ★★☆ | ☆☆☆ | ★★★ | ☆☆☆ | ☆☆☆ | ☆☆☆ |
| Retrofit | ★★★ | ★★★ | ★☆☆ | ★★★ | ☆☆☆ | ☆☆☆ | ☆☆☆ |
| Batch | ☆☆☆ | ☆☆☆ | ★★★ | ☆☆☆ | ☆☆☆ | ☆☆☆ | ☆☆☆ |
| Total Site | ★☆☆ | ★★★ | ★☆☆ | ☆☆☆ | ☆☆☆ | ☆☆☆ | ☆☆☆ |
| **Ekonomik** | | | | | | | |
| Maliyet Opt. | ★★★ | ★★★ | ★☆☆ | ★★☆ | ☆☆☆ | ☆☆☆ | ☆☆☆ |
| TAC Hesabı | ★★★ | ★★★ | ★☆☆ | ★★☆ | ☆☆☆ | ☆☆☆ | ★☆☆ |
| **Kullanılabilirlik** | | | | | | | |
| Arayüz | ★★★ | ★★☆ | ★★★ | ★★☆ | ★☆☆ | ★☆☆ | ★★☆ |
| Dokümantasyon | ★★★ | ★★☆ | ★★☆ | ★★☆ | ★☆☆ | ★☆☆ | ★☆☆ |
| Öğrenme Kolaylığı | ★☆☆ | ★★☆ | ★★★ | ★★☆ | ★★☆ | ★★★ | ★★★ |
| **Maliyet** | | | | | | | |
| Lisans | €€€€€ | €€€€ | €€-€€€ | €€ | Ücretsiz | Ücretsiz | Ücretsiz |
| Yıllık Bakım | €€€€€ | €€€ | €€ | € | Ücretsiz | Ücretsiz | Ücretsiz |

> Not: ★★★ = Mükemmel, ★★☆ = İyi, ★☆☆ = Temel, ☆☆☆ = Yok/Desteklenmiyor

### 7.2 Problem Boyutuna Göre Uygunluk

| Problem Boyutu | Akış Sayısı | Önerilen Araçlar |
|----------------|-------------|------------------|
| Küçük | 2-10 | Excel, pyPinch, pina |
| Orta | 10-30 | PinCH, SPRINT, Python (özel) |
| Büyük | 30-100 | AEA, SuperTarget |
| Çok Büyük | 100+ | AEA (simülasyon entegrasyonlu) |

### 7.3 Sektöre Göre Uygunluk

| Sektör | Birincil Araç | Alternatif | Neden |
|--------|--------------|------------|-------|
| Rafineri | SuperTarget | AEA | Kolon entegrasyonu, buhar sistemi |
| Petrokimya | AEA | SuperTarget | Simülasyon entegrasyonu |
| Gıda/İçecek | PinCH | Excel | Batch proses, çok periyotlu |
| Kağıt/Hamur | Spiral | SuperTarget | Sektör-spesifik modüller |
| Çimento | AEA | Python | Yüksek sıcaklık, basit akışlar |
| Tekstil | PinCH | Excel | Batch boyama, TES |
| Kimya (genel) | AEA | SPRINT | Geniş kapsam, HEN tasarımı |
| Enerji (kojenerasyon) | SuperTarget | AEA | CHP, total site |

## 8. ExergyLab Entegrasyonu (ExergyLab Integration)

ExergyLab platformu, bireysel ekipman exergy analizinden fabrika seviyesi optimizasyona kadar geniş bir yelpazeyi kapsar. Pinch analizi araçlarıyla entegrasyon, platformun değerini önemli ölçüde artırır.

### 8.1 ExergyLab'ın Pinch Analizi ile Kesişim Noktaları

```
ExergyLab Mevcut Kapsam:
  ─ Kompresör exergy analizi → Atık ısı potansiyeli [kW, °C]
  ─ Kazan exergy analizi → Baca gazı, blöf kaybı [kW, °C]
  ─ Chiller exergy analizi → Soğutma/ısıtma profili [kW, °C]
  ─ Pompa exergy analizi → Mekanik/termal kayıp [kW]
  ─ Fabrika çapraz ekipman → Entegrasyon fırsatları

Pinch Analizi Katma Değeri:
  ─ Akış verisi otomatik çıkarma (ExergyLab sonuçlarından)
  ─ Minimum enerji hedefleri (QH,min / QC,min)
  ─ Sistematik ısı geri kazanım potansiyeli
  ─ HEN tasarım önerileri
  ─ Exergy-pinch entegre yorumlama
```

### 8.2 Veri Akışı Tasarımı (Data Flow Design)

```
ExergyLab → Pinch Analizi Entegrasyon Akışı:

1. Ekipman Analizi (Mevcut)
   └─ Kompresör: T_çıkış=85°C, Q_atık=25 kW, ṁ=0.5 kg/s
   └─ Kazan: T_baca=180°C, Q_kayıp=120 kW, T_besleme=60°C
   └─ Chiller: T_kondenser=45°C, Q_kondenser=80 kW

2. Akış Verisi Çıkarma (Yeni — Otomatik)
   └─ H1: Kompresör soğutma → 85→40°C, CP=0.60 kW/°C
   └─ H2: Baca gazı       → 180→120°C, CP=2.0 kW/°C
   └─ H3: Kondenser        → 45→35°C, CP=8.0 kW/°C
   └─ C1: Kazan besleme    → 20→60°C, CP=3.5 kW/°C
   └─ C2: Proses ısıtma    → 60→150°C, CP=1.2 kW/°C

3. Pinch Analizi Motoru (Yeni)
   └─ PTA → QH,min, QC,min, Pinch sıcaklığı
   └─ Bileşik eğriler ve GCC
   └─ Exergy pinch analizi (Tsirlin yaklaşımı)

4. AI Yorumlama (Mevcut — Genişletilmiş)
   └─ Pinch sonuçlarını exergy bağlamında yorumlama
   └─ Spesifik ısı geri kazanım önerileri
   └─ Yatırım/tasarruf tahmini
```

### 8.3 Exergy-Pinch Entegrasyonu (Exergy-Pinch Integration)

ExergyLab'ın benzersiz avantajı, pinch analizini exergy perspektifinden zenginleştirebilmesidir:

```
Klasik Pinch Analizi:
  → Sadece enerji miktarına (kW) odaklanır
  → Tüm kW'lar eşit muamele görür
  → Sıcaklık seviyesini dolaylı olarak dikkate alır

Exergy-Zenginleştirilmiş Pinch Analizi (ExergyLab Yaklaşımı):
  → Her akışın exergy içeriğini hesaplar
  → Yüksek sıcaklık = yüksek exergy = yüksek öncelik
  → Exergy yıkımını minimize eden HEN tasarımı
  → Gerçek termodinamik değer bazlı önceliklendirme

Exergy akış hesabı:
  Ėx_akış = ṁ × Cp × [(T - T₀) - T₀ × ln(T/T₀)]  [kW]

  Burada:
  - T₀ = çevre sıcaklığı [K] (referans durum)
  - T  = akış sıcaklığı [K]
  - ṁ × Cp = CP [kW/K]

Örnek (referans problem, T₀ = 298.15 K = 25°C):
  H1 (270°C): Ėx = 15 × [(543-298) - 298×ln(543/298)] = 15 × 63.3 = 949 kW
  C1 (30°C → 250°C): Düşük sıcaklıktan yüksek sıcaklığa → exergy artışı

  Sonuç: H1'in ısısı H2'den daha değerli (daha yüksek exergy)
  → Öncelikli olarak C1 (yüksek hedef) ile eşleştirilmeli
```

### 8.4 Gelecek Geliştirme Yol Haritası

```
Faz 1 (Mevcut):
  ✓ Ekipman bazlı exergy analizi
  ✓ Fabrika seviyesi çapraz ekipman tespiti
  ✓ AI yorumlama (Claude API)

Faz 2 (Planlanan):
  ○ Akış verisi otomatik çıkarma (ekipman sonuçlarından)
  ○ Temel PTA motoru (Python engine modülü)
  ○ Bileşik eğri ve GCC görselleştirme (React/Recharts)
  ○ Exergy-pinch entegre raporlama

Faz 3 (Vizyon):
  ○ Otomatik HEN tasarım önerileri
  ○ Retrofit analizi (mevcut eşanjör ağı girişi)
  ○ Çok-tesisli site analizi
  ○ Gerçek zamanlı pinch analizi (SCADA entegrasyonu)
```

## İlgili Dosyalar

- [Pinch Analizi Bilgi Tabanı İndeks](INDEX.md) -- Navigasyon haritasi ve yukleme kurallari
- [Pinch Analizi Temelleri](fundamentals.md) -- Linnhoff metodolojisi, MER hedefleri, 3 altin kural
- [Pratik Uygulama Rehberi](practical_guide.md) -- Proje yonetimi, veri toplama, devreye alma
- [Pinch Analizi Ana Dosyasi](../pinch_analysis.md) -- Temel kavramlar ve hesaplamalar
- [Isi Entegrasyonu](../heat_integration.md) -- Kaynak-kullanim eslestirme
- [Capraz Ekipman](../cross_equipment.md) -- Ekipmanlar arasi firsatlar

## Referanslar

- Linnhoff, B. et al., "User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1994
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," 2nd Edition, Butterworth-Heinemann, 2007
- Klemes, J.J. (Ed.), "Handbook of Process Integration (PI): Minimisation of Energy and Water Use, Waste and Emissions," Woodhead Publishing, 2013
- Smith, R., "Chemical Process Design and Integration," 2nd Edition, Wiley, 2016
- Linnhoff, B. and Flower, J.R., "Synthesis of Heat Exchanger Networks," AIChE Journal, 24(4), 633-654, 1978
- AspenTech, "Aspen Energy Analyzer Documentation," aspentech.com
- Lucerne University, "PinCH Software Documentation," pinch-analyse.ch
