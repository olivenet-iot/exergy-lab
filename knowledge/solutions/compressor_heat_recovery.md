# Çözüm: Kompresör Atık Isı Geri Kazanımı

## Özet

**Problem:** Kompresör elektrik enerjisinin ~%90'ını ısıya dönüştürür. Bu ısı genellikle atmosfere atılır.

**Çözüm:** Heat Recovery Unit (HRU) ile atık ısıyı proses suyu, bina ısıtma veya başka amaçlarla kullanmak.

**Tipik ROI:** 1-3 yıl

## Uygulanabilirlik Kriterleri

| Kriter | Minimum | İdeal |
|--------|---------|-------|
| Kompresör gücü | 15 kW | >30 kW |
| Çalışma saati | 3000 saat/yıl | >5000 saat/yıl |
| Isı kullanım mesafesi | <50 m | <20 m |
| Isı ihtiyacı sürekliliği | Sezonluk | Yıl boyu |

## Teknik Açıklama

### Isı Kaynakları
1. **Yağ soğutucu:** ~72% (en büyük kaynak, 60-80°C)
2. **Aftercooler:** ~13% (70-90°C basınçlı hava)
3. **Motor:** ~5% (genelde geri kazanılmaz)

### Geri Kazanım Yöntemleri

**Tip A: Hava-Hava (Direkt)**
- Sıcak egzoz havası kanalla yönlendirilir
- Bina ısıtma için kullanılır
- Maliyet: €500-2,000
- Sınırlama: Sadece ısıtma sezonu, mesafe kısıtı

**Tip B: Hava-Su (HRU)**
- Plakalı ısı eşanjörü ile su ısıtılır
- 50-70°C sıcak su üretilir
- Maliyet: €3,000-15,000
- Avantaj: Esnek kullanım, depolama imkanı

**Tip C: Entegre Sistem**
- OEM heat recovery paketi
- Kompresör ile birlikte tasarlanmış
- Maliyet: %10-20 ek (yeni kompresör alımında)
- Avantaj: Garanti, optimize performans

## Yatırım Maliyeti

| Kompresör Gücü | HRU Maliyeti | Kurulum | Toplam |
|----------------|--------------|---------|--------|
| 15-30 kW | €2,000-4,000 | €500-1,000 | €2,500-5,000 |
| 30-75 kW | €4,000-8,000 | €1,000-2,000 | €5,000-10,000 |
| 75-150 kW | €8,000-15,000 | €2,000-4,000 | €10,000-19,000 |
| >150 kW | €15,000-30,000 | €4,000-8,000 | €19,000-38,000 |

## Tasarruf Hesabı

```
Geri kazanılabilir ısı (kW):
Q_recovery = P_compressor × 0.70 × η_HRU

Burada:
- P_compressor = Kompresör gücü [kW]
- 0.70 = Isıya dönüşen oran
- η_HRU = HRU verimi (tipik 0.80-0.90)

Yıllık tasarruf (kWh):
E_saved = Q_recovery × kullanım_saati × eşzamanlılık_faktörü

Parasal tasarruf (€/yıl):
Savings = E_saved × alternatif_ısı_maliyeti

Alternatif ısı maliyetleri:
- Doğalgaz kazan: €0.05-0.08/kWh
- LPG kazan: €0.08-0.12/kWh
- Elektrikli ısıtma: €0.10-0.15/kWh
- Mazot kazan: €0.07-0.10/kWh
```

## Örnek ROI Hesabı

**Senaryo:** 55 kW vidalı kompresör, 5000 saat/yıl, doğalgaz alternatif

```
Q_recovery = 55 × 0.70 × 0.85 = 32.7 kW
E_saved = 32.7 × 5000 × 0.70 = 114,450 kWh/yıl
Savings = 114,450 × 0.06 = €6,867/yıl

Yatırım = €8,000 (HRU + kurulum)
Geri ödeme = 8,000 / 6,867 = 1.17 yıl
```

## Tedarikçiler

| Marka | Ürün | Özellik |
|-------|------|---------|
| Atlas Copco | ER serisi | Entegre, yüksek verim |
| Kaeser | KRAT | Modüler, retrofit uygun |
| Boge | DUOTHERM | Çift sıcaklık çıkışı |
| Bowman | EC serisi | Aftermarket, ekonomik |
| Alfa Laval | CB serisi | Yüksek kapasiteli |

## Uygulama Adımları

1. Isı tüketim noktalarını ve miktarlarını belirle
2. Kompresörden uzaklığı ve boru güzergahını planla
3. Eşzamanlılık faktörünü hesapla (ısı ihtiyacı vs kompresör çalışması)
4. HRU kapasitesi belirle (kompresör gücünün %60-70'i)
5. Minimum 3 tedarikçiden teklif al
6. Kurulum yaptır (genelde 1-2 gün)
7. Devreye alma ve performans doğrulama

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Düşük kullanım | Yaz aylarında ısı gerekmez | Absorpsiyonlu soğutma değerlendir |
| Mesafe kaybı | Uzun boruda ısı kaybı | İzolasyon, maksimum 30m |
| Legionella | Durgun sıcak suda bakteri | Su >60°C tut, sirkülasyon |
| Geri basınç | HRU kompresöre yük bindirir | OEM onaylı ürün kullan |

## Karar Matrisi

| Koşul | Öneri |
|-------|-------|
| Yıl boyu ısı ihtiyacı + >30kW | Kesinlikle uygula |
| Sezonluk ısı + >50kW | Uygula, ROI hesapla |
| Sezonluk ısı + <30kW | Dikkatli değerlendir |
| Isı ihtiyacı yok | Uygulanmaz |
