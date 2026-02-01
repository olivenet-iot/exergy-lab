# Fabrika Bilgi Tabanı İndeks

## Genel Bakış
Fabrika seviyesi exergy analizi, çapraz ekipman entegrasyonu ve sektörel karşılaştırma için kapsamlı bilgi tabanı.

## Dosya Listesi

### Çekirdek Analiz Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `cross_equipment.md` | Ekipmanlar arası entegrasyon fırsatları | Yüksek | Çapraz ekipman değerlendirmesi |
| `prioritization.md` | Yatırım önceliklendirme rehberi | Yüksek | Aksiyon sıralama |
| `factory_benchmarks.md` | Fabrika seviyesi sektörel benchmark | Yüksek | Genel değerlendirme |
| `heat_integration.md` | Isı entegrasyonu fırsatları | Yüksek | Atık ısı değerlendirmesi |
| `waste_heat_recovery.md` | Atık ısı geri kazanım teknolojileri | Yüksek | Teknoloji seçimi |

### Metodoloji Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `methodology.md` | Analiz metodolojisi | Orta | Analiz planı |
| `system_boundaries.md` | Sistem sınırları tanımı | Orta | Kapsam belirleme |
| `exergy_fundamentals.md` | Exergy temel kavramları | Orta | Teori referansı |
| `exergy_flow_analysis.md` | Exergy akış analizi | Orta | Akış diyagramları |
| `energy_flow_analysis.md` | Enerji akış analizi | Orta | Enerji balansı |
| `mass_balance.md` | Kütle dengesi | Düşük | Detaylı analiz |
| `pinch_analysis.md` | Pinch analizi temelleri | Düşük | Isı entegrasyon tasarımı |
| `process_integration.md` | Proses entegrasyonu | Düşük | İleri entegrasyon |

### Ekonomik Analiz Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `economic_analysis.md` | Ekonomik analiz yöntemleri | Orta | ROI, NPV hesaplama |
| `life_cycle_cost.md` | Yaşam döngüsü maliyet analizi | Düşük | Uzun vadeli değerlendirme |
| `energy_pricing.md` | Enerji fiyatlandırma bilgileri | Orta | Maliyet hesaplama |

### KPI ve Performans Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `kpi_definitions.md` | KPI tanımları | Orta | İzleme metrikleri |
| `performance_indicators.md` | Performans göstergeleri | Orta | Değerlendirme kriterleri |
| `data_collection.md` | Veri toplama rehberi | Düşük | Ölçüm planlama |
| `measurement_verification.md` | Ölçüm ve doğrulama | Düşük | Kalite kontrol |

### Uygulama Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `implementation.md` | Uygulama rehberi | Düşük | Proje yönetimi |
| `reporting.md` | Raporlama şablonları | Düşük | Rapor oluşturma |
| `case_studies.md` | Vaka çalışmaları | Düşük | Referans örnekler |
| `cogeneration.md` | Kojenerasyon bilgileri | Orta | CHP değerlendirmesi |
| `energy_management.md` | Enerji yönetim sistemi | Düşük | ISO 50001 referansı |
| `utility_analysis.md` | Yardımcı tesis analizi | Düşük | Tesis değerlendirmesi |

### Sektöre Özel Dosyalar (`sector_*.md`)
| Dosya | Sektör | Kullanım |
|-------|--------|----------|
| `sector_automotive.md` | Otomotiv | sector=automotive |
| `sector_cement.md` | Çimento | sector=cement |
| `sector_chemical.md` | Kimya | sector=chemical |
| `sector_food.md` | Gıda | sector=food |
| `sector_metal.md` | Metal | sector=metal |
| `sector_paper.md` | Kağıt | sector=paper |
| `sector_textile.md` | Tekstil | sector=textile |

## Navigasyon Kuralları
1. Fabrika analizinde `cross_equipment.md` + `prioritization.md` + `factory_benchmarks.md` her zaman oku
2. Sektör biliniyorsa ilgili `sector_{sector}.md` oku
3. Isı entegrasyonu fırsatı varsa `heat_integration.md` + `waste_heat_recovery.md` oku
4. Ekonomik analiz gerektiğinde `economic_analysis.md` + `energy_pricing.md` oku
