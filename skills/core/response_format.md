---
skill_id: response_format
version: 1.0
type: core
---

# AI Yanıt Formatları

## Tek Ekipman Analizi JSON Schema

```json
{
  "summary": "string - 2-3 cümle özet",
  "detailed_analysis": "string - Detaylı teknik analiz",

  "key_findings": [
    {
      "finding": "string - Bulgu",
      "severity": "high|medium|low",
      "evidence": "string - Kanıt/veri"
    }
  ],

  "recommendations": [
    {
      "title": "string - Öneri başlığı",
      "priority": "high|medium|low",
      "description": "string - Detaylı açıklama",
      "annual_savings_eur": number,
      "investment_eur": number,
      "payback_years": number
    }
  ],

  "not_recommended": [
    {
      "title": "string",
      "reason": "string"
    }
  ],

  "action_plan": {
    "immediate": ["string"],
    "short_term": ["string"],
    "medium_term": ["string"]
  },

  "warnings": ["string"]
}
```

## Fabrika Analizi JSON Schema

```json
{
  "summary": "string",
  "factory_efficiency_assessment": "string",

  "hotspot_analysis": [
    {
      "equipment_id": "string",
      "equipment_name": "string",
      "priority": "high|medium|low",
      "analysis": "string",
      "exergy_destroyed_kW": number
    }
  ],

  "integration_opportunities": [
    {
      "title": "string",
      "source": "string",
      "target": "string",
      "description": "string",
      "potential_savings_eur": number,
      "investment_eur": number,
      "roi_years": number
    }
  ],

  "prioritized_actions": [
    {
      "rank": number,
      "action": "string",
      "priority": "high|medium|low",
      "annual_savings_eur": number,
      "investment_eur": number,
      "payback_years": number
    }
  ],

  "sector_specific_insights": ["string"],

  "warnings": ["string"]
}
```

## Yanıt Kuralları

1. **Somut ol:** "İyileştirme yapılabilir" yerine "€5,000/yıl tasarruf sağlanabilir"
2. **Rakam ver:** Her öneri için tasarruf, yatırım, ROI
3. **Önceliklendir:** High > Medium > Low
4. **Uyarı ekle:** Risk ve dikkat edilmesi gerekenler
5. **Türkçe yaz:** Teknik terimler parantez içinde İngilizce olabilir
