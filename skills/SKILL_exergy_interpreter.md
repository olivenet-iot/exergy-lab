# SKILL: Exergy Analysis Interpreter

## Bu skill ne yapar?

Kompresör exergy analiz sonuçlarını yorumlar ve yapılandırılmış JSON formatında detaylı öneriler üretir. Frontend'in doğrudan render edebileceği formatta çıktı verir.

## Ne zaman kullanılır?

Bu skill doğrudan kullanıcı tarafından çağrılmaz. FastAPI backend'in `/api/interpret` endpoint'i tarafından programatik olarak çağrılır. Claude Code CLI print mode (`-p`) ile çalıştırılır.

## Bilgi Kaynakları

Yorumlama sırasında aşağıdaki knowledge dosyaları referans alınmalıdır:

- `/knowledge/benchmarks/compressor_benchmarks.md` — Sektör karşılaştırma verileri
- `/knowledge/equipment/compressor_screw.md` — Vidalı kompresör bilgileri
- `/knowledge/equipment/compressor_piston.md` — Pistonlu kompresör bilgileri
- `/knowledge/equipment/compressor_scroll.md` — Scroll kompresör bilgileri
- `/knowledge/equipment/compressor_centrifugal.md` — Santrifüj kompresör bilgileri
- `/knowledge/solutions/compressor_heat_recovery.md` — Isı geri kazanım çözümleri
- `/knowledge/solutions/compressor_vsd.md` — Değişken hız sürücü çözümleri
- `/knowledge/solutions/compressor_pressure_optimization.md` — Basınç optimizasyonu
- `/knowledge/solutions/compressor_air_leaks.md` — Kaçak tespiti/giderimi
- `/knowledge/solutions/compressor_maintenance.md` — Bakım optimizasyonu
- `/knowledge/solutions/compressor_inlet_optimization.md` — Giriş optimizasyonu
- `/knowledge/solutions/compressor_dryer_optimization.md` — Kurutucu optimizasyonu
- `/knowledge/solutions/compressor_system_design.md` — Sistem tasarımı
- `/knowledge/formulas/compressor_exergy.md` — Exergy hesaplama formülleri

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
