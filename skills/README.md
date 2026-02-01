# ExergyLab Skills Sistemi

## Genel Bakış

Skills, AI'ın davranışını ve uzmanlık alanlarını tanımlayan modüler dosyalardır.

## Skill Kategorileri

### Core Skills
Tüm analizlerde kullanılan temel beceriler.

### Equipment Skills
Ekipman tipine özel uzmanlık.

### Factory Skills
Fabrika seviyesi analiz becerileri.

### Output Skills
Çıktı formatı ve stil kuralları.

## Skill Seçim Mantığı

```
1. Analiz tipi belirlenir (single_equipment / factory)
2. Ekipman tipi belirlenir
3. İlgili skill dosyaları yüklenir
4. Karar ağacı işletilir
5. Yanıt formatına göre çıktı üretilir
```

## Yeni Skill Ekleme

1. Uygun kategoride .md dosyası oluştur
2. Metadata header ekle
3. Karar kurallarını tanımla
4. Örnekler ekle
5. Test et
