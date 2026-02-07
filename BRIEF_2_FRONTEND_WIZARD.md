# BRIEF 2: Frontend Wizard — Proses Tanımı Adımı

> **Tarih:** 2026-02-07
> **Öncelik:** Yüksek — Brief 1 tamamlandıktan sonra
> **Bağımlılık:** Brief 1 (API endpointleri hazır olmalı)
> **Dokunduğu Dosyalar:** SADECE frontend/ (backend'e dokunma)
> **Tahmini:** ~500 satır yeni/değişen frontend kodu

---

## 1. Amaç

FactoryWizard'ı 2 adımdan 3 adıma çıkarmak. Yeni adım: **Proses Tanımı**.
Mevcut projelere de proses tanımı eklenebilmeli (Dashboard'dan erişim).

---

## 2. Mevcut Durum

```
FactoryWizard.jsx (274 satır):
  Adım 1: Proje Bilgileri (isim, sektör, açıklama)
  Adım 2: Ekipman Ekleme
```

---

## 3. Hedef Durum

```
FactoryWizard.jsx:
  Adım 1: Proje Bilgileri (isim, sektör, açıklama)     ← MEVCUT, aynı
  Adım 2: Proses Tanımı                                  ← YENİ
  Adım 3: Ekipman Ekleme                                 ← MEVCUT, aynı
```

---

## 4. Yeni Bileşen: `ProcessDefinitionStep.jsx`

### 4.1 Genel Yapı

```
┌─────────────────────────────────────────────────────────────────┐
│  Proses Tanımı                                          2 / 3   │
│                                                                 │
│  Bu fabrika ne yapıyor?                                         │
│                                                                 │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐      │
│  │ 🔥        │ │ ❄️        │ │ 💨        │ │ ♨️        │      │
│  │ Kurutma   │ │ Soğutma   │ │ Basınçlı  │ │ Buhar     │      │
│  │           │ │           │ │ Hava      │ │ Üretimi   │      │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘      │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐      │
│  │ 🌡️        │ │ ⚡        │ │ 🧊        │ │ 🏭        │      │
│  │ Isıtma    │ │ CHP       │ │ Soğuk     │ │ Genel     │      │
│  │           │ │           │ │ Depolama  │ │ Üretim    │      │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘      │
│                                                                 │
│  ── veya ──                                                     │
│  [✓] Proses tanımı olmadan devam et                             │
│      (Sadece ekipman bazlı analiz yapılır)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Proses Seçildikten Sonra

```
┌─────────────────────────────────────────────────────────────────┐
│  Proses Tanımı — Kurutma                                2 / 3   │
│                                                                 │
│  [← Değiştir]                                                   │
│                                                                 │
│  Alt Kategori                                                   │
│  ┌──────────────────────────────────────┐                       │
│  │ Tahıl Kurutma                    ▼   │                       │
│  └──────────────────────────────────────┘                       │
│                                                                 │
│  Proses Açıklaması                                              │
│  ┌──────────────────────────────────────┐                       │
│  │ Mısır kurutma hattı                  │                       │
│  └──────────────────────────────────────┘                       │
│                                                                 │
│  ── Proses Parametreleri ──                                     │
│                                                                 │
│  Malzeme Debisi          [1000        ] kg/h                    │
│  Giriş Nem Oranı         [20          ] %                       │
│  Çıkış Nem Oranı         [5           ] %                       │
│  Giriş Sıcaklığı         [20          ] °C    (opsiyonel)       │
│  Çıkış Sıcaklığı         [50          ] °C    (opsiyonel)       │
│                                                                 │
│  ── Ekonomik Parametreler ──                                    │
│                                                                 │
│  Yıllık Çalışma Saati    [6000        ] saat/yıl               │
│  Enerji Fiyatı           [0.08        ] €/kWh                  │
│                                                                 │
│                                    [Geri]  [Devam →]            │
└─────────────────────────────────────────────────────────────────┘
```

### 4.3 Davranış Kuralları

1. **API'den proses tipleri çekilir:** `GET /api/process-types` — kartların label, icon, description bilgisi
2. **Proses tipi seçilince alt kategoriler yüklenir:** `GET /api/process-types/{type}/subcategories`
3. **Parametreler dinamik:** Her proses tipinin `param_definitions` ve `optional_params`'ı API'den gelir. Form dinamik oluşturulur.
4. **"Olmadan devam et" checkbox'ı:** İşaretlenirse proses alanları null olarak gönderilir. Mevcut davranış korunur.
5. **Validasyon:** Zorunlu parametreler (required_params) boş olamaz. Min/max sınırları kontrol edilir.
6. **Geri butonu:** Adım 1'e döner, girilen veriler korunur.
7. **Devam butonu:** Adım 3'e geçer (ekipman ekleme).

### 4.4 State Yönetimi

```javascript
// FactoryWizard.jsx'e eklenecek state
const [processType, setProcessType] = useState(null);
const [processLabel, setProcessLabel] = useState("");
const [processParams, setProcessParams] = useState({});
const [processSubcategory, setProcessSubcategory] = useState("general");
const [operatingHours, setOperatingHours] = useState(6000);
const [energyPrice, setEnergyPrice] = useState(0.08);
const [skipProcess, setSkipProcess] = useState(false);
```

### 4.5 API Çağrısı (Proje Oluşturma)

Mevcut `POST /api/factory/projects` isteğine yeni alanlar eklenir:

```javascript
const createProject = async () => {
  const body = {
    name: projectName,
    sector: sector,
    description: description,
    // YENİ
    process_type: skipProcess ? null : processType,
    process_label: skipProcess ? null : processLabel,
    process_parameters: skipProcess ? null : processParams,
    process_subcategory: skipProcess ? null : processSubcategory,
    operating_hours: operatingHours,
    energy_price_eur_kwh: energyPrice,
  };
  // ...mevcut API çağrısı
};
```

---

## 5. Mevcut Projeler İçin Proses Ekleme

### 5.1 Dashboard'dan Erişim

FactoryDashboard.jsx'te, proses tanımı olmayan projeler için:

```
┌──────────────────────────────────────────────────────┐
│  ℹ️ Proses tanımı eklenmemiş.                        │
│                                                      │
│  Proses tanımı ekleyerek şunları öğrenebilirsiniz:   │
│  • Termodinamik ideale ne kadar uzaksınız             │
│  • En iyi teknoloji ile kıyaslama                    │
│  • Yıllık tasarruf potansiyeli                       │
│                                                      │
│  [+ Proses Tanımı Ekle]                              │
└──────────────────────────────────────────────────────┘
```

### 5.2 Modal/Drawer

"Proses Tanımı Ekle" butonuna tıklanınca ProcessDefinitionStep bileşeni modal veya drawer içinde gösterilir.

```
PUT /api/factory/projects/{project_id}/process
Body: { process_type, process_label, process_parameters, process_subcategory, ... }
```

Başarılı olunca: Sayfa yenilenir, analiz tekrar çalıştırılmalı mesajı gösterilir.

---

## 6. Lucide İkon Eşlemeleri

```javascript
const PROCESS_ICONS = {
  drying: "Flame",
  heating: "Thermometer",
  cooling: "Snowflake",
  steam_generation: "Cloud",
  compressed_air: "Wind",
  chp: "Zap",
  cold_storage: "Box",      // veya Archive
  general_manufacturing: "Factory",
};
```

---

## 7. Dosya Değişiklikleri

| Dosya | İşlem | Tahmin |
|-------|-------|--------|
| `frontend/src/components/factory/ProcessDefinitionStep.jsx` | **YENİ** | ~250 satır |
| `frontend/src/pages/FactoryWizard.jsx` | **GÜNCELLE** | +80 satır (3. adım, state, API) |
| `frontend/src/pages/FactoryDashboard.jsx` | **GÜNCELLE** | +50 satır (proses ekleme CTA) |
| `frontend/src/components/factory/ProcessEditModal.jsx` | **YENİ** | ~100 satır |

**Toplam: ~480 satır**

---

## 8. UYARILAR

1. **Backend'e DOKUNMA** — API endpointleri Brief 1'de hazırlanmış olmalı
2. **Mevcut Wizard akışını bozma** — "Olmadan devam et" seçeneği zorunlu
3. **engine/ klasörüne DOKUNMA**
4. **Proses tipi kartları API'den gelmeli** — hardcode etme (SUPPORTED_PROCESS_TYPES API'den gelecek)
5. **Parametre formu dinamik olmalı** — Her proses tipi farklı parametreler gerektirir
6. **Mevcut projelerin çalışması etkilenmemeli**

---

*Bu brief FactoryWizard'a proses tanımı adımını ekler. Brief 3 ile paralel çalıştırılamaz (dashboard değişiklikleri çakışabilir).*
