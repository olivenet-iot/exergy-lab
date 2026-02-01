# SKILL: Exergy Analysis Interpreter

## Bu skill ne yapar?

Ekipman exergy analiz sonuçlarını yorumlar ve yapılandırılmış JSON formatında detaylı öneriler üretir. Kompresör, kazan, chiller ve pompa olmak üzere 4 ekipman tipi desteklenir. Frontend'in doğrudan render edebileceği formatta çıktı verir.

## Ne zaman kullanılır?

Bu skill doğrudan kullanıcı tarafından çağrılmaz. FastAPI backend'in `/api/interpret` endpoint'i tarafından programatik olarak çağrılır. Claude Code CLI print mode (`-p`) ile çalıştırılır.

## Bilgi Kaynakları

Yorumlama sırasında ekipman tipine göre aşağıdaki knowledge dosyaları referans alınmalıdır:

### Kompresör
- `knowledge/compressor/benchmarks.md` — Sektör karşılaştırma verileri
- `knowledge/compressor/formulas.md` — Exergy hesaplama formülleri
- `knowledge/compressor/equipment/screw.md` — Vidalı kompresör bilgileri
- `knowledge/compressor/equipment/screw_oilfree.md` — Yağsız vidalı kompresör
- `knowledge/compressor/equipment/piston.md` — Pistonlu kompresör bilgileri
- `knowledge/compressor/equipment/scroll.md` — Scroll kompresör bilgileri
- `knowledge/compressor/equipment/centrifugal.md` — Santrifüj kompresör bilgileri
- `knowledge/compressor/equipment/roots.md` — Roots blower bilgileri
- `knowledge/compressor/solutions/heat_recovery.md` — Isı geri kazanım çözümleri
- `knowledge/compressor/solutions/vsd.md` — Değişken hız sürücü çözümleri
- `knowledge/compressor/solutions/pressure_optimization.md` — Basınç optimizasyonu
- `knowledge/compressor/solutions/air_leaks.md` — Kaçak tespiti/giderimi
- `knowledge/compressor/solutions/maintenance.md` — Bakım optimizasyonu
- `knowledge/compressor/solutions/inlet_optimization.md` — Giriş optimizasyonu
- `knowledge/compressor/solutions/dryer_optimization.md` — Kurutucu optimizasyonu
- `knowledge/compressor/solutions/system_design.md` — Sistem tasarımı

### Kazan
- `knowledge/boiler/benchmarks.md` — Kazan sektör karşılaştırma verileri
- `knowledge/boiler/formulas.md` — Kazan exergy hesaplama formülleri
- `knowledge/boiler/equipment/steam_firetube.md` — Ateş borulu buhar kazanı
- `knowledge/boiler/equipment/steam_watertube.md` — Su borulu buhar kazanı
- `knowledge/boiler/equipment/hotwater.md` — Sıcak su kazanı
- `knowledge/boiler/equipment/condensing.md` — Yoğuşmalı kazan
- `knowledge/boiler/equipment/waste_heat.md` — Atık ısı kazanı / HRSG
- `knowledge/boiler/equipment/electric.md` — Elektrikli kazan
- `knowledge/boiler/equipment/biomass.md` — Biyokütle kazanı
- `knowledge/boiler/solutions/economizer.md` — Ekonomizer
- `knowledge/boiler/solutions/air_preheater.md` — Hava ön ısıtıcı
- `knowledge/boiler/solutions/oxygen_control.md` — Oksijen kontrolü
- `knowledge/boiler/solutions/blowdown_recovery.md` — Blöf geri kazanımı
- `knowledge/boiler/solutions/condensate_return.md` — Kondensat geri dönüşü
- `knowledge/boiler/solutions/steam_trap.md` — Buhar kapanı
- `knowledge/boiler/solutions/insulation.md` — Yalıtım
- `knowledge/boiler/solutions/load_optimization.md` — Yük optimizasyonu
- `knowledge/boiler/solutions/combustion_tuning.md` — Yanma ayarı
- `knowledge/boiler/solutions/feedwater_treatment.md` — Besleme suyu arıtma

### Chiller
- `knowledge/chiller/benchmarks.md` — Chiller sektör karşılaştırma verileri
- `knowledge/chiller/formulas.md` — Chiller exergy hesaplama formülleri
- `knowledge/chiller/equipment/vapor_compression.md` — Buhar sıkıştırmalı chiller
- `knowledge/chiller/equipment/screw.md` — Vidalı chiller
- `knowledge/chiller/equipment/centrifugal.md` — Santrifüj chiller
- `knowledge/chiller/equipment/scroll.md` — Scroll chiller
- `knowledge/chiller/equipment/reciprocating.md` — Pistonlu chiller
- `knowledge/chiller/equipment/absorption.md` — Absorpsiyonlu chiller
- `knowledge/chiller/equipment/air_cooled.md` — Hava soğutmalı chiller
- `knowledge/chiller/equipment/water_cooled.md` — Su soğutmalı chiller
- `knowledge/chiller/solutions/vsd.md` — Değişken hız sürücü
- `knowledge/chiller/solutions/condenser_optimization.md` — Kondenser optimizasyonu
- `knowledge/chiller/solutions/chilled_water_reset.md` — Soğuk su sıcaklık ayarı
- `knowledge/chiller/solutions/free_cooling.md` — Serbest soğutma
- `knowledge/chiller/solutions/sequencing.md` — Chiller sıralama
- `knowledge/chiller/solutions/maintenance.md` — Bakım
- `knowledge/chiller/solutions/load_reduction.md` — Yük azaltma
- `knowledge/chiller/solutions/delta_t.md` — Delta-T optimizasyonu
- `knowledge/chiller/solutions/thermal_storage.md` — Termal depolama
- `knowledge/chiller/solutions/heat_recovery.md` — Isı geri kazanımı

### Pompa
- `knowledge/pump/benchmarks.md` — Pompa sektör karşılaştırma verileri
- `knowledge/pump/formulas.md` — Pompa exergy hesaplama formülleri
- `knowledge/pump/equipment/centrifugal.md` — Santrifüj pompa
- `knowledge/pump/equipment/positive_displacement.md` — Pozitif deplasmanlı pompa
- `knowledge/pump/equipment/submersible.md` — Dalgıç pompa
- `knowledge/pump/equipment/vertical_turbine.md` — Dikey türbin pompa
- `knowledge/pump/equipment/booster.md` — Hidrofor
- `knowledge/pump/equipment/vacuum.md` — Vakum pompası
- `knowledge/pump/solutions/vsd.md` — Değişken hız sürücü
- `knowledge/pump/solutions/impeller_trimming.md` — Çark tornalama
- `knowledge/pump/solutions/right_sizing.md` — Doğru boyutlandırma
- `knowledge/pump/solutions/parallel_operation.md` — Paralel çalışma
- `knowledge/pump/solutions/system_optimization.md` — Sistem optimizasyonu
- `knowledge/pump/solutions/motor_upgrade.md` — Motor yükseltme
- `knowledge/pump/solutions/maintenance.md` — Bakım
- `knowledge/pump/solutions/throttle_elimination.md` — Kısma eliminasyonu
- `knowledge/pump/solutions/cavitation_prevention.md` — Kavitasyon önleme
- `knowledge/pump/solutions/control_optimization.md` — Kontrol optimizasyonu

## JSON Çıktı Şeması

Yanıt **mutlaka** aşağıdaki JSON formatında olmalıdır. Markdown fence (```` ```json ... ``` ````) kullanılmamalı, saf JSON döndürülmelidir.

```json
{
  "summary": "Analiz sonuçlarının 2-3 cümlelik genel özeti",
  "detailed_analysis": "Exergy verimi, kayıplar ve benchmark karşılaştırmasının detaylı açıklaması (3-5 cümle)",
  "key_insights": [
    "Önemli bulgu 1",
    "Önemli bulgu 2",
    "Önemli bulgu 3"
  ],
  "recommendations": [
    {
      "title": "Öneri başlığı",
      "description": "Detaylı açıklama",
      "priority": "high|medium|low",
      "estimated_savings_eur_year": 5000,
      "estimated_investment_eur": 15000,
      "payback_years": 3.0,
      "category": "heat_recovery|vsd|pressure|maintenance|leaks|system_design|inlet|dryer"
    }
  ],
  "not_recommended": [
    {
      "title": "Önerilmeyen çözüm",
      "reason": "Neden uygun olmadığının açıklaması"
    }
  ],
  "action_plan": {
    "immediate": ["Hemen yapılabilecek aksiyonlar"],
    "short_term": ["1-3 ay içinde yapılacaklar"],
    "medium_term": ["3-12 ay içinde yapılacaklar"]
  },
  "warnings": ["Dikkat edilmesi gereken uyarılar"]
}
```

## Yorumlama Kuralları

### Verim Değerlendirmesi
- **<%30:** Kritik düşük verim, acil müdahale gerekli
- **%30-45:** Ortalamanın altında, iyileştirme fırsatları mevcut
- **%45-55:** Kabul edilebilir, optimizasyon ile iyileştirilebilir
- **%55-65:** İyi performans, ince ayar önerileri
- **>%65:** Mükemmel performans, koruyucu bakım odaklı öneriler

### Öneri Önceliklendirme
- **high:** ROI < 2 yıl VEYA tasarruf > €5,000/yıl VEYA güvenlik riski
- **medium:** ROI 2-5 yıl VEYA tasarruf €1,000-5,000/yıl
- **low:** ROI > 5 yıl VEYA tasarruf < €1,000/yıl

### Önerilmeyen Çözümler
Mevcut duruma uygun olmayan çözümleri ve nedenlerini belirt. Örneğin:
- Verim zaten yüksekse VSD ekleme gereksiz olabilir
- Küçük kompresörlerde ısı geri kazanım ekonomik olmayabilir

## Dikkat Edilecekler

1. **Türkçe:** Tüm yorumlar ve öneriler Türkçe olmalıdır
2. **Sayısal tutarlılık:** Tasarruf ve yatırım rakamları gerçekçi olmalı, verilen parametrelere dayalı hesaplanmalı
3. **Kompresör tipine özel:** Her kompresör tipinin kendine özgü sorunları ve çözümleri vardır
4. **Saf JSON:** Çıktı saf JSON olmalı, markdown formatting kullanılmamalı
