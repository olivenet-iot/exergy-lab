---
skill_id: dryer_expert
version: 1.0
type: equipment
equipment_type: dryer
triggers:
  - single_equipment_analysis
  - equipment_type == "dryer"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/dryer/benchmarks.md
  - knowledge/dryer/formulas.md
  - knowledge/dryer/psychrometrics.md
  - knowledge/dryer/audit.md
  - knowledge/dryer/equipment/*.md
  - knowledge/dryer/solutions/*.md
---

# Kurutma Firini Uzmani (Industrial Dryer Expert)

## Uzmanlik Alani

Konvektif, iletimli ve radyasyonlu kurutma sistemleri exergy analizi:
- Tunel, bant, doner, akiskan yatakli, sprey, silindir kurutucular
- Isi pompali ve kizilotesi kurutma sistemleri
- Psikrometrik analiz ve nemli hava termodinamigi
- Kurutma prosesi optimizasyonu

## Kritik Metrikler

| Metrik | Formul | Iyi Deger |
|--------|--------|-----------|
| SMER (Specific Moisture Extraction Rate) | kg_nem / kWh | > 0.5 kg/kWh (konvektif), > 3.0 kg/kWh (isi pompali) |
| Exergy verimi | Ex_urun / Ex_giris | Tipe bagli (asagida) |
| Enerji verimi | Q_kurutma / Q_giris | > 50% |
| SEC (Specific Energy Consumption) | kWh / kg_nem | < 2.0 kWh/kg |
| Egzoz sicakligi | Olcum | < 80C (ideal) |
| Egzoz bagil nemi | Olcum | > 70% |
| Kurutma hizi | kg_nem / (m2.h) | Malzemeye bagli |

## Ozel Kurallar

### Exergy Verimi Degerlendirmesi
```
Not: Kurutucu exergy verimi DOGASI GEREGI DUSUKTUR cunku
kurutma termodinamik olarak yikici bir prosestir.

Konvektif kurutucular:
- > 15%: Iyi
- 10-15%: Ortalama
- 5-10%: Dusuk
- < 5%: Kritik (acil mudahale)

Isi pompali kurutucular:
- > 25%: Iyi
- 15-25%: Ortalama
- < 15%: Dusuk

IR/Mikrodalga kurutucular:
- Farkli olcek (elektrik girdisi), SMER ile degerlendir
```

### SMER Siniflandirmasi (Kurutucu Tipine Gore)
```
Konvektif (sicak hava):     0.2-0.6 kg/kWh
Doner kurutucu:             0.3-0.8 kg/kWh
Akiskan yatakli:            0.3-0.7 kg/kWh
Sprey kurutucu:             0.2-0.5 kg/kWh
Bant kurutucu:              0.3-0.6 kg/kWh
Isi pompali:                1.0-4.0 kg/kWh
Kizilotesi (IR):            0.3-0.8 kg/kWh
Mikrodalga:                 0.4-0.9 kg/kWh
```

### Egzoz Geri Kazanim Kurali
```
Egzoz sicakligi > 80C
  → Egzoz isi geri kazanimi oner

Egzoz bagil nemi < 60%
  → Hava resirkulasyonu oner

Kurutma sicakligi < 80C VE konvektif sistem
  → Isi pompasi retrofiti degerlendir

Mekanik su alma yok VE besleme nemi > %50
  → Oncelikle mekanik su alma oner (pres, santrifuj)

Her %10 mekanik nem azaltma ≈ %30-40 termal enerji tasarrufu
```

## Exergy Kayip Dagilimi (Tipik — Konvektif Kurutucu)

| Kayip Kaynagi | Oran |
|---------------|------|
| Egzoz havasi (exhaust loss) | 35-50% |
| Yanma irreversibility | 15-25% |
| Isi transferi irreversibility | 10-15% |
| Radyasyon ve iletim kaybi | 3-8% |
| Mekanik (fanlar, konveyor) | 2-5% |

## EGM Bazli Tasarim Kurallari

### Egzoz Havasi — En Buyuk S_gen Kaynagi
Konvektif kurutucularda entropi uretiminin %40-55'i egzoz havasinin atilmasindan gelir:
```
S_gen_egzoz ≈ m_hava × (s_egzoz - s_ortam)
```
Yuksek sicaklik ve dusuk bagil nemdeki egzoz havasi onemli exergy tasir. Azaltma yollari:
- Egzoz isi geri kazanimi (hava-hava esanjor)
- Kismi hava resirkulasyonu (%30-60 geri dondurmek)
- Kondenserli nem geri kazanimi

### Optimum Kurutma Sicakligi
Kurutma sicakligi entropi-kalite dengesiyle belirlenir:
```
T_kurutma_opt: S_gen_toplam + Urun kalite kisiti = minimum
```
- Yuksek T_kurutma → dusuk S_gen_egzoz ama urun bozulma riski
- Dusuk T_kurutma → yuksek S_gen ama iyi urun kalitesi
- Her malzeme icin maksimum izin verilen sicaklik kontrol edilmeli

### Bejan Sayisi — Kurutucu
| Bilesen | Tipik Be | Yorum |
|---------|----------|-------|
| Yanma/Isitma | 0.80-0.95 | Isi transferi baskin |
| Kurutma odasi | 0.60-0.80 | Kutle transferi etkili |
| Egzoz kanali | 0.50-0.70 | Dengeli |
| Isi geri kazanim | 0.40-0.60 | Dengeye yakin |

Detayli bilgi: `knowledge/dryer/psychrometrics.md`

## Tipik Oneriler ve ROI

| Oneri | Tasarruf | Yatirim | ROI |
|-------|----------|---------|-----|
| Egzoz isi geri kazanimi | %10-20 yakit | €15-35K | 0.8-1.5 yil |
| Hava resirkulasyonu | %15-30 yakit | €10-25K | 0.5-1.5 yil |
| Isi pompasi retrofiti | %40-60 enerji | €50-150K | 2-4 yil |
| Mekanik su alma (on islem) | %30-40 termal | €20-60K | 1-2 yil |
| Izolasyon iyilestirme | %3-8 yakit | €5-15K | 0.5-1 yil |
| Sicaklik optimizasyonu | %5-15 yakit | €3-10K | 0.3-0.8 yil |
| Gunes enerjisi on isitma | %10-25 yakit | €30-80K | 2-4 yil |
