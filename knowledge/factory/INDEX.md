---
title: "Fabrika Bilgi Tabanı İndeks (Factory Knowledge Base Index)"
category: reference
keywords: [fabrika, factory, çapraz ekipman, sektörel, indeks, navigasyon]
related_files: [knowledge/INDEX.md, knowledge/factory/cross_equipment.md, knowledge/factory/factory_benchmarks.md]
use_when: ["Fabrika seviyesi bilgi tabanı navigasyonu gerektiğinde"]
priority: high
last_updated: 2026-02-02
---
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

### Exergoekonomik Analiz Dosyaları (`exergoeconomic/`)
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `exergoeconomic/INDEX.md` | Exergoekonomik navigasyon haritası | Yüksek | Bilgi tabanı girişi |
| `exergoeconomic/overview.md` | Genel bakış, tarihçe, uygulama alanları | Yüksek | Kavram tanıtımı |
| `exergoeconomic/speco_method.md` | SPECO metodolojisi (4 adım) | Yüksek | Analiz yöntemi |
| `exergoeconomic/fuel_product_definitions.md` | 10 ekipman tipi F/P tanımları | Yüksek | F/P belirleme |
| `exergoeconomic/cost_equations.md` | PEC korelasyonları, düzeltme faktörleri | Yüksek | Maliyet tahmini |
| `exergoeconomic/cost_databases.md` | CEPCI değerleri, Türkiye ayarları | Orta | Fiyat referansı |
| `exergoeconomic/levelized_cost.md` | CRF formülü, Ż hesabı, Türkiye WACC | Yüksek | Yıllıklaştırma |
| `exergoeconomic/exergoeconomic_balance.md` | Ċ_P = Ċ_F + Ż maliyet bilançosu | Yüksek | Denge denklemi |
| `exergoeconomic/auxiliary_equations.md` | F-kuralı, P-kuralı, sınır koşulları | Orta | Yardımcı denklemler |
| `exergoeconomic/matrix_formulation.md` | [A]{c}={Z} matris çözümü, Python kodu | Orta | Matris çözüm |
| `exergoeconomic/evaluation_criteria.md` | Ċ_D, f_k, r_k tanım/eşik/karar | Yüksek | Sonuç yorumlama |
| `exergoeconomic/advanced_exergoeconomic.md` | AV/UN, EN/EX, 4-yollu matris | Orta | İleri analiz |
| `exergoeconomic/optimization.md` | İteratif ve matematiksel optimizasyon | Orta | Maliyet min. |
| `exergoeconomic/sensitivity_analysis.md` | OAT, tornado, Monte Carlo, Sobol | Orta | Belirsizlik analizi |
| `exergoeconomic/case_studies.md` | 6 akademik vaka çalışması | Düşük | Referans örnekler |

**Çözümlü Örnekler** (`exergoeconomic/worked_examples/`):
| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `simple_cycle.md` | Basit Rankine çevrimi (4 bileşen) SPECO analizi | Temel örnek |
| `cogeneration.md` | Gaz türbini CHP (7 bileşen) + ileri analiz | CHP örneği |
| `industrial_plant.md` | ExergyLab ekipmanları ile tesis analizi (5 bileşen) | Endüstriyel örnek |

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

### İlişkili Ekipman Bilgi Tabanları
| Dizin | Açıklama | Kullanım |
|-------|----------|----------|
| `../steam_turbine/` | Buhar türbini / CHP bilgi tabanı (21 dosya) | Türbin/CHP analizi, fizibilite |
| `../steam_turbine/systems/` | CHP/CCHP sistem konfigürasyonları | CHP detaylı analiz |
| `../steam_turbine/economics/` | Türbin/CHP ekonomik analiz | Fizibilite, teşvikler |

### Pinch Analizi Bilgi Tabanı (`pinch/`)
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `pinch/INDEX.md` | Pinch bilgi tabanı navigasyon haritası | Yüksek | Pinch bilgi tabanı girişi |
| `pinch/fundamentals.md` | Linnhoff metodolojisi, MER, 3 altın kural, exergy bağlantısı | Yüksek | Temel pinch kavramları |
| `pinch/composite_curves.md` | Hot/Cold composite curve oluşturma | Yüksek | Bileşik eğri analizi |
| `pinch/problem_table.md` | PTA algoritması, kaskad, düzeltilmiş kaskad | Yüksek | Enerji hedef hesabı |
| `pinch/grand_composite.md` | GCC, ısı cebi, utility yerleştirme, CHP potansiyeli | Yüksek | Utility optimizasyonu |
| `pinch/hen_design.md` | Grid diyagramı, CP kuralları, akış bölme, döngü kırma | Yüksek | HEN tasarımı |
| `pinch/targeting.md` | Enerji/alan/maliyet hedefleri, Bath formülü | Yüksek | Hedefleme |
| `pinch/delta_t_min.md` | ΔTmin seçimi, süperhedefleme, TAC optimizasyonu | Yüksek | ΔTmin optimizasyonu |
| `pinch/stream_data.md` | Akış verisi çıkarma, faz değişimi, ExergyLab | Orta | Veri hazırlama |
| `pinch/hen_retrofit.md` | Cross-pinch tespiti, network pinch, retrofit | Orta | Mevcut tesis iyileştirme |
| `pinch/utility_systems.md` | Çoklu utility, CHP, ısı pompası yerleştirme | Orta | Utility tasarımı |
| `pinch/cost_estimation.md` | Eşanjör maliyet, Bath formülü, TAC, NPV | Orta | Ekonomik analiz |
| `pinch/batch_integration.md` | Zaman dilimi modeli, TES, program optimizasyonu | Orta | Kesikli proses |
| `pinch/total_site.md` | Total Site Analysis, site profilleri, buhar optimizasyonu | Orta | Çok-tesisli analiz |
| `pinch/practical_guide.md` | Proje yönetimi, veri toplama, kontrol listesi | Orta | Uygulama rehberi |
| `pinch/common_mistakes.md` | Yaygın hatalar ve tespit yöntemleri | Orta | Hata önleme |
| `pinch/software_tools.md` | Ticari/açık kaynak araçlar, Python implementasyonu | Düşük | Araç seçimi |
| `pinch/case_studies.md` | 7 sektörel vaka çalışması | Düşük | Referans örnekler |

### İleri Exergy Analizi (`advanced_exergy/`)
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `advanced_exergy/INDEX.md` | İleri exergy analizi navigasyon haritası | Yüksek | İleri analiz bilgi tabanı girişi |
| `advanced_exergy/overview.md` | Genel bakış, tarihçe, 3 dekompozisyon | Yüksek | Kavram tanıtımı |
| `advanced_exergy/avoidable_unavoidable.md` | Kaçınılabilir/kaçınılamaz (AV/UN) dekompozisyon | Yüksek | I_AV, I_UN hesaplama |
| `advanced_exergy/endogenous_exogenous.md` | Endojen/ekzojen (EN/EX) dekompozisyon | Yüksek | I_EN, I_EX hesaplama |
| `advanced_exergy/four_way_splitting.md` | 4-yollu dekompozisyon, IPN | Yüksek | Tam analiz ve önceliklendirme |
| `advanced_exergy/ideal_conditions.md` | Ekipman bazında ideal/kaçınılamaz koşullar | Yüksek | Parametre referansı |
| `advanced_exergy/methodology.md` | 8-adımlı hesaplama metodolojisi | Yüksek | Hesaplama rehberi |
| `advanced_exergy/interpretation_guide.md` | Sonuç yorumlama rehberi, karar kuralları | Yüksek | AI yorumlama desteği |
| `advanced_exergy/improvement_priority.md` | IPN, θ sınıflandırma, önceliklendirme | Yüksek | Yatırım sıralama |
| `advanced_exergy/visualization.md` | Görselleştirme yöntemleri | Orta | Görsel çıktı tasarımı |
| `advanced_exergy/limitations.md` | Sınırlılıklar ve uyarılar | Orta | Sonuç güvenilirliği |
| `advanced_exergy/case_studies.md` | 3 vaka çalışması | Orta | Referans örnekler |

**Ekipman Bazında İleri Analiz** (`advanced_exergy/equipment_specific/`):
| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `compressor_advanced.md` | 75 kW vidalı kompresör worked example | Kompresör ileri analizi |
| `boiler_advanced.md` | 4 ton/h buhar kazanı worked example | Kazan ileri analizi |
| `heat_exchanger_advanced.md` | Atık ısı geri kazanım HX worked example | HX ileri analizi |
| `turbine_advanced.md` | Buhar türbini CHP worked example | Türbin ileri analizi |
| `pump_advanced.md` | 15 kW pompa + kısma vanası worked example | Pompa ileri analizi |
| `chiller_advanced.md` | 300 kW santrifüj chiller worked example | Chiller ileri analizi |

### Entropi Üretim Minimizasyonu — EGM (`entropy_generation/`)
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `entropy_generation/INDEX.md` | EGM navigasyon haritası | Yüksek | EGM bilgi tabanı girişi |
| `entropy_generation/overview.md` | EGM genel bakış ve felsefesi | Yüksek | EGM konsept tanıtımı |
| `entropy_generation/fundamentals.md` | Gouy-Stodola, entropi temelleri | Yüksek | Temel kavramlar |
| `entropy_generation/bejan_number.md` | Bejan sayısı (Be) ve N_s | Yüksek | İrreversibllik kaynağı belirleme |
| `entropy_generation/heat_transfer_egm.md` | Isı transferi EGM | Yüksek | ΔT kaynaklı S_gen |
| `entropy_generation/fluid_flow_egm.md` | Akış sistemi EGM | Yüksek | ΔP kaynaklı S_gen |
| `entropy_generation/finite_time_thermo.md` | Curzon-Ahlborn verimi | Orta | Verim sınırları |
| `entropy_generation/heat_exchanger_egm.md` | Eşanjör optimizasyonu | Yüksek | Eşanjör EGM |
| `entropy_generation/pipe_flow_egm.md` | Boru çapı optimizasyonu | Orta | Boru EGM |
| `entropy_generation/power_cycles_egm.md` | Güç çevrimleri EGM | Orta | Rankine, Brayton |
| `entropy_generation/refrigeration_egm.md` | Soğutma çevrimi EGM | Orta | Chiller EGM |
| `entropy_generation/heat_storage_egm.md` | Isı depolama EGM | Orta | Termal depolama |
| `entropy_generation/constructal_theory.md` | Constructal yasa | Orta | Ağ/düzen tasarımı |
| `entropy_generation/industrial_applications.md` | Uygulama rehberi | Orta | Checklist ve adımlar |
| `entropy_generation/egm_vs_exergoeconomic.md` | EGM vs exergoekonomik | Orta | Yöntem karşılaştırması |
| `entropy_generation/case_studies.md` | Vaka çalışmaları | Düşük | Endüstriyel örnekler |

**Çözümlü Örnekler** (`entropy_generation/worked_examples/`):
| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `heat_exchanger_opt.md` | 500 kW eşanjör EGM optimizasyonu | Hesaplama örneği |
| `pipe_sizing.md` | Boru çapı optimizasyonu (D_opt) | Hesaplama örneği |
| `cooling_system.md` | 200 kW soğutma sistemi EGM analizi | Hesaplama örneği |

### Termoekonomik Optimizasyon Bilgi Tabanı (`thermoeconomic_optimization/`)
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `thermoeconomic_optimization/INDEX.md` | Navigasyon haritası | Yüksek | Termoekonomik bilgi tabanı girişi |
| `thermoeconomic_optimization/overview.md` | Termoekonomik optimizasyon temelleri, SPECO | Yüksek | Kavramsal temel |
| `thermoeconomic_optimization/objective_functions.md` | Amaç fonksiyonları, maliyet bileşenleri, CBAM | Yüksek | Maliyet formülasyonu |
| `thermoeconomic_optimization/decision_variables.md` | Karar değişkenleri, kısıtlar, sınırlar | Yüksek | Optimizasyon model kurulumu |
| `thermoeconomic_optimization/iterative_method.md` | Tsatsaronis iteratif yöntemi, f_k/r_k analizi | Yüksek | Mevcut sistemlerin iyileştirmesi |
| `thermoeconomic_optimization/structural_optimization.md` | Üst-yapı, MINLP, konfigürasyon seçimi | Orta | Yeni tesis / büyük retrofit |
| `thermoeconomic_optimization/parametric_optimization.md` | NLP, SQP, gradient tabanlı optimizasyon | Yüksek | Parametre ince ayarı |
| `thermoeconomic_optimization/multi_objective.md` | Pareto, NSGA-II, TOPSIS, çok amaçlı | Yüksek | Maliyet-verimlilik-çevre dengesi |
| `thermoeconomic_optimization/algorithms.md` | GA, PSO, SQP, NSGA-II, hibrit yöntemler | Orta | Algoritma seçimi |
| `thermoeconomic_optimization/sensitivity_analysis.md` | Duyarlılık, Monte Carlo, senaryo analizi | Yüksek | Belirsizlik değerlendirmesi |
| `thermoeconomic_optimization/trade_off_curves.md` | Ödünleşim eğrileri, optimal nokta seçimi | Orta | Karar destek |
| `thermoeconomic_optimization/practical_guide.md` | 10 adımlı uygulama prosedürü, hatalar, tuzaklar | Yüksek | Endüstriyel uygulama |
| `thermoeconomic_optimization/case_studies.md` | Akademik ve endüstriyel vaka çalışmaları | Orta | Referans ve doğrulama |

**Çözümlü Örnekler** (`thermoeconomic_optimization/worked_examples/`):
| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `worked_examples/boiler_optimization.md` | 3.000 kW kazan termoekonomik optimizasyonu | Tek ekipman örneği |
| `worked_examples/chp_optimization.md` | 500 kWe CHP çok amaçlı optimizasyon | Sistem seviyesi örnek |
| `worked_examples/factory_optimization.md` | Tekstil fabrikası portföy optimizasyonu | Fabrika seviyesi örnek |

### Proses Boşluk Analizi Bilgi Tabanı (`process/`)
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `process/index.md` | Proses bilgi tabanı navigasyon haritası | Yüksek | Proses bilgi tabanı girişi |
| `process/gap_analysis_methodology.md` | 3 katmanlı boşluk modeli, ESI, BPR formülleri | Yüksek | Proses analizi temel referans |
| `process/bat_overview.md` | BAT kavramı, EU BREF sistemi, exergy dönüşümü | Yüksek | BAT değerleri yorumlanırken |
| `process/sustainability_index.md` | ESI tanımı, A-F derecelendirme, sektörel tipik değerler | Yüksek | ESI sonuçları yorumlanırken |
| `process/heating.md` | Isıtma prosesi — Ex_min, BAT, ESI, iyileştirme | Yüksek | Isıtma/kazan analizi |
| `process/steam_generation.md` | Buhar üretimi — 10 bar ≈ 819 kJ/kg, BAT η_ex | Yüksek | Buhar sistemi analizi |
| `process/compressed_air.md` | Basınçlı hava — W_min, sistem ESI, kaçak analizi | Yüksek | Basınçlı hava sistemi analizi |
| `process/cooling.md` | Soğutma — ters Carnot, COP, free cooling | Yüksek | Chiller/soğutma analizi |
| `process/cold_storage.md` | Soğuk depolama — 3 sıcaklık katmanı, izolasyon | Orta | Soğuk depo analizi |
| `process/drying.md` | Kurutma — SEC, SMER, ısı pompalı kurutucu | Yüksek | Kurutucu analizi |
| `process/chp.md` | CHP — FUF vs η_ex farkı, CCGT, gaz türbini | Yüksek | CHP/kojenerasyon analizi |
| `process/general_manufacturing.md` | Çimento, cam, kağıt, şeker — sektörel BAT | Orta | Spesifik üretim sektörleri |

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
5. İleri exergy analizi (AV/UN, EN/EX, 4-yollu) gerektiğinde önce `advanced_exergy/INDEX.md` oku → navigasyon kurallarına göre ilgili dosyalara yönlen
6. EGM / entropi analizi gerektiğinde `entropy_generation/INDEX.md` oku → ilgili dosyalara yönlen
7. CHP/türbin analizi gerektiğinde `cogeneration.md` + `../steam_turbine/systems/*.md` oku
8. Türbin fizibilitesi için `../steam_turbine/economics/feasibility.md` oku
9. Pinch analizi gerektiğinde önce `pinch/INDEX.md` oku, yükleme kurallarına göre ilgili pinch/ dosyalarını yükle
10. Detaylı HEN tasarımı için `pinch/hen_design.md` + `pinch/fundamentals.md` oku
11. Mevcut tesis ısı entegrasyon iyileştirmesi için `pinch/hen_retrofit.md` + `pinch/practical_guide.md` oku
12. Termoekonomik optimizasyon gerektiğinde önce `thermoeconomic_optimization/INDEX.md` oku → navigasyon kurallarına göre ilgili dosyalara yönlen
13. Toplam exergy yıkım maliyeti > 50.000 €/yıl veya çoklu yatırım kararı varsa `thermoeconomic_optimization/practical_guide.md` + `thermoeconomic_optimization/iterative_method.md` oku
14. Exergoekonomik analiz (Ċ_D, f_k, r_k, maliyet paylaştırma) gerektiğinde önce `exergoeconomic/INDEX.md` oku → navigasyon kurallarına göre ilgili dosyalara yönlen
15. f_k/r_k tabanlı bileşen değerlendirmesi için `exergoeconomic/evaluation_criteria.md` + `exergoeconomic/optimization.md` oku
16. Proses seviyesi boşluk analizi (ESI, BAT karşılaştırması) gerektiğinde önce `process/index.md` oku → ilgili proses dosyasına yönlen
17. ESI derecelendirmesi veya proses bazlı benchmark gerektiğinde `process/sustainability_index.md` + `process/gap_analysis_methodology.md` + ilgili proses dosyasını oku

## Referanslar

1. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
2. Bejan, A., Tsatsaronis, G. & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
3. Linnhoff, B. et al. (1982). *User Guide on Process Integration for the Efficient Use of Energy*. IChemE.
4. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*. 2nd ed., Elsevier.
5. Tsatsaronis, G. & Morosuk, T. (2010). "Advanced exergetic analysis of a refrigeration system." *Energy*, 35(2), 649-657.
