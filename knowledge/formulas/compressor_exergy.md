# Kompresör Exergy Hesaplamaları

## Temel İlkeler

Kompresör elektrik enerjisini (saf exergy) basınçlı hava exergy'sine dönüştürür.
Dönüşüm sırasında entropi üretilir ve exergy yok edilir.

## Hesaplama Adımları

### 1. Giren Exergy (Elektrik)

Elektrik saf exergy'dir:
```
Ex_in = P_electric [kW]
```

### 2. Kütle Debisi

Hacimsel debiden kütle debisine:
```
ṁ = V̇ × ρ_air

Burada:
- V̇ = Hacimsel debi [m³/s]
- ρ_air = Hava yoğunluğu ≈ 1.2 kg/m³ (25°C, 1 atm'de)
```

### 3. Çıkan Exergy (Basınçlı Hava)

İdeal gaz kabulüyle basınçlı havanın exergy'si:
```
Ex_air = ṁ × R × T₀ × ln(P₂/P₁)

Burada:
- R = 0.287 kJ/kg·K (kuru hava için gaz sabiti)
- T₀ = 298.15 K (dead state sıcaklığı)
- P₂ = Çıkış basıncı [kPa]
- P₁ = Giriş basıncı = 101.325 kPa
```

### 4. Exergy Yıkımı

```
Ex_destroyed = Ex_in - Ex_air [kW]
```

### 5. Exergy Verimi

```
η_ex = Ex_air / Ex_in × 100 [%]
```

### 6. Atık Isı Exergy Potansiyeli

Kompresör atık ısısı aftercooler ve yağ soğutucudan atılır:
```
Q_waste ≈ Ex_destroyed [kW]  (büyük kısmı ısı olarak)

Ex_heat_recoverable = Q_waste × (1 - T₀/T_exhaust)

Burada:
- T_exhaust = Çıkış sıcaklığı [K]
```

### 7. Yıllık Maliyet

```
Yıllık_kayıp_kWh = Ex_destroyed × çalışma_saati
Yıllık_kayıp_EUR = Yıllık_kayıp_kWh × elektrik_fiyatı
```

## Örnek Hesaplama

**Girdiler:**
- P_electric = 32 kW
- V̇ = 6.2 m³/min = 0.103 m³/s
- P₂ = 7.5 bar = 750 kPa
- T_exhaust = 85°C = 358 K
- Çalışma = 6000 saat/yıl
- Elektrik = 0.10 €/kWh

**Hesap:**
```
ṁ = 0.103 × 1.2 = 0.124 kg/s

Ex_air = 0.124 × 0.287 × 298.15 × ln(750/101.325)
       = 0.124 × 0.287 × 298.15 × 2.002
       = 21.25 kW

Ex_destroyed = 32 - 21.25 = 10.75 kW

η_ex = 21.25 / 32 × 100 = 66.4%

Ex_heat = 10.75 × (1 - 298.15/358) = 1.80 kW

Yıllık_kayıp = 10.75 × 6000 = 64,500 kWh
Maliyet = 64,500 × 0.10 = 6,450 €/yıl
```

## Sınırlamalar

1. İdeal gaz kabulü yapılmıştır (yüksek basınçlarda sapma olabilir)
2. Nem etkisi ihmal edilmiştir
3. Yük değişimi dinamikleri dahil değildir
