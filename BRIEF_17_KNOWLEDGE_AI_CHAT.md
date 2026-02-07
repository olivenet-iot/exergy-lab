# Brief 17: Knowledge-Powered AI Chat — İnteraktif Enerji Danışmanı

> **Claude Code için:** Bu brief'i oku ve uygula. 305 dosyalık knowledge base'i aktive eden, analiz context'i üzerinden soru-cevap yapabilen AI chat paneli. Mevcut `ClaudeCodeClient` altyapısını genişlet.

---

## 🎯 Hedef

Analiz sonuçlarının yanında **canlı sohbet paneli**. Kullanıcı, mevcut analiz sonuçları context'inde sorular sorar, AI 305 dosyalık knowledge base'den ilgili bilgiyi bulup cevaplayabilir.

**Öncesi:** Analiz yap → statik AI yorumu oku → daha fazla bilgi istiyorsan Google'a git
**Sonrası:** Analiz yap → AI'a "Bejan sayısı 0.85 ne demek?" sor → anında cevap + referans

**Fark:** ExergyLab hesap makinesi değil, **AI enerji danışmanı** olur.

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. Mevcut `claude_code_service.py`'yi ÖNCE dikkatlice oku — özellikle `_load_relevant_knowledge()`, `_load_skills()`, `_build_prompt()`, `interpret()`
3. Mevcut `interpret.py` route'unu oku
4. Knowledge dizin yapısını anla (her ekipman: INDEX.md, benchmarks.md, formulas.md, audit.md, equipment/, solutions/)
5. 413 testi BOZMA
6. Mevcut AI interpret akışını BOZMA — chat ayrı endpoint, ayrı fonksiyon

---

## 📋 Adım 0: Mevcut Sistemi Anla (KRİTİK)

```bash
# 1. AI servis — tüm dosyayı oku
cat api/services/claude_code_service.py

# 2. Interpret route
cat api/routes/interpret.py

# 3. Knowledge dizin yapısı — INDEX dosyaları
find knowledge/ -name "INDEX.md" -type f | head -20

# 4. Bir equipment knowledge INDEX'i oku — dosya routing haritası
cat knowledge/compressor/INDEX.md

# 5. Başka bir knowledge INDEX
cat knowledge/boiler/INDEX.md

# 6. Factory INDEX
cat knowledge/factory/INDEX.md

# 7. Solutions dizini örneği
ls knowledge/compressor/solutions/
ls knowledge/boiler/solutions/

# 8. Factory alt dizinleri
ls knowledge/factory/pinch/
ls knowledge/factory/exergoeconomic/
ls knowledge/factory/energy_management/

# 9. Mevcut skills
ls skills/core/ skills/equipment/ skills/factory/ skills/output/

# 10. Mevcut frontend AIInterpretation component
cat frontend/src/components/results/AIInterpretation.jsx
```

---

## 🧩 Mimari Tasarım

### Core Innovation: Knowledge Router

305 dosyanın hepsi context'e sığmaz. Çözüm: **topic-based knowledge routing** — kullanıcının sorusundan konu tespit et, ilgili dosyaları seç, prompt'a ekle.

```
Kullanıcı Sorusu: "VSD takarsak ne kadar tasarruf ederiz?"
                          ↓
              ┌── Knowledge Router ──┐
              │                      │
              │  Keyword Match:      │
              │  "VSD" → solutions   │
              │  "tasarruf" → econ   │
              │                      │
              │  Equipment: pump     │
              └──────────────────────┘
                          ↓
              Knowledge Files Selected:
              ├── knowledge/pump/solutions/vsd.md (veya en yakın match)
              ├── knowledge/pump/benchmarks.md (her zaman)
              ├── knowledge/pump/formulas.md (her zaman)
              └── knowledge/factory/economic_analysis.md
                          ↓
              Prompt = Skills + Knowledge + Analysis Data + Chat History + Soru
                          ↓
              Claude CLI → Markdown cevap
```

### Akış

```
1. Kullanıcı analizi tamamlar (mevcut akış)
2. Chat paneli gösterilir (sonuçların altında veya sağında — responsive)
3. Kullanıcı soru yazar → Enter/Submit
4. POST /api/chat → {equipment_type, subtype, question, analysis_data, history}
5. Backend: Knowledge Router → dosya seçimi → prompt build → Claude CLI
6. Cevap Markdown olarak döner → frontend render eder
7. History biriktir (son 5 turn)
8. Kullanıcı takip sorusu sorabilir
```

---

## 📦 Adım 1: Backend — Knowledge Router

### 1.1 `api/services/knowledge_router.py` — Yeni Dosya

Bu modül, kullanıcının sorusuna göre hangi knowledge dosyalarının yükleneceğini belirler.

```python
"""
ExergyLab - Knowledge Router

Kullanıcının sorusuna ve mevcut ekipman context'ine göre
ilgili knowledge dosyalarını seçer.

305 dosyalık knowledge base'den max 5-8 dosya seçer (context window sınırı).
"""

import os
import re
from typing import List, Tuple
from functools import lru_cache


# Proje kökü
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")


# ─── Topic Keyword Mapping ───────────────────────────────────────────

TOPIC_ROUTES = [
    {
        'topic': 'solutions',
        'keywords_tr': ['çözüm', 'iyileştirme', 'iyilestirme', 'upgrade', 'değiştir', 'degistir',
                        'tasarruf', 'azalt', 'düşür', 'dusur', 'öneri', 'oneri', 'tavsiye',
                        'nasıl düzeltilir', 'ne yapılmalı', 'ne yapilmali'],
        'keywords_en': ['solution', 'improvement', 'upgrade', 'reduce', 'optimize', 'fix',
                        'recommendation', 'how to improve', 'save', 'savings'],
        'files_equipment': lambda eq: _glob_knowledge(f'{eq}/solutions'),
        'files_factory': [],
    },
    {
        'topic': 'audit',
        'keywords_tr': ['denetim', 'ölçüm', 'olcum', 'kontrol', 'muayene', 'bakım', 'bakim',
                        'veri toplama', 'saha', 'enstrümantasyon'],
        'keywords_en': ['audit', 'measurement', 'inspection', 'maintenance', 'data collection',
                        'instrumentation', 'field'],
        'files_equipment': lambda eq: [f'{eq}/audit.md'],
        'files_factory': ['factory/data_collection.md', 'factory/measurement_verification.md'],
    },
    {
        'topic': 'economics',
        'keywords_tr': ['maliyet', 'yatırım', 'yatirim', 'ROI', 'geri ödeme', 'geri odeme',
                        'fizibilite', 'ekonomik', 'fiyat', 'bütçe', 'butce', 'para',
                        'finansman', 'teşvik', 'tesvik'],
        'keywords_en': ['cost', 'investment', 'ROI', 'payback', 'economic', 'price', 'budget',
                        'feasibility', 'finance', 'incentive'],
        'files_equipment': lambda eq: _glob_knowledge(f'{eq}/economics') if os.path.isdir(
            os.path.join(KNOWLEDGE_DIR, eq, 'economics')) else [],
        'files_factory': ['factory/economic_analysis.md', 'factory/life_cycle_cost.md',
                          'factory/energy_pricing.md'],
    },
    {
        'topic': 'pinch',
        'keywords_tr': ['pinch', 'ısı entegrasyonu', 'isi entegrasyonu', 'HEN',
                        'ısı değiştirici ağı', 'isi degistirici agi', 'composite curve',
                        'minimum enerji', 'delta T'],
        'keywords_en': ['pinch', 'heat integration', 'HEN', 'heat exchanger network',
                        'composite curve', 'minimum energy', 'grand composite'],
        'files_equipment': lambda eq: [],
        'files_factory': _glob_knowledge('factory/pinch', max_files=4),
    },
    {
        'topic': 'exergoeconomic',
        'keywords_tr': ['exergoekonomik', 'SPECO', 'maliyet denklemi', 'fuel-product',
                        'termoekonomik', 'exergy maliyeti'],
        'keywords_en': ['exergoeconomic', 'SPECO', 'cost equation', 'thermoeconomic',
                        'exergy cost', 'fuel product'],
        'files_equipment': lambda eq: [],
        'files_factory': _glob_knowledge('factory/exergoeconomic', max_files=4),
    },
    {
        'topic': 'entropy_generation',
        'keywords_tr': ['entropi', 'Bejan', 'bejan', 'EGM', 'entropi üretimi', 'entropi minimizasyonu',
                        'constructal', 'tersinmezlik'],
        'keywords_en': ['entropy', 'Bejan', 'EGM', 'entropy generation', 'entropy minimization',
                        'constructal', 'irreversibility'],
        'files_equipment': lambda eq: [],
        'files_factory': _glob_knowledge('factory/entropy_generation', max_files=4),
    },
    {
        'topic': 'advanced_exergy',
        'keywords_tr': ['ileri exergy', 'AV/UN', 'EN/EX', 'kaçınılabilir', 'kacinilabilir',
                        'endojen', 'eksojen', 'avoidable', 'unavoidable', 'splitting'],
        'keywords_en': ['advanced exergy', 'avoidable', 'unavoidable', 'endogenous', 'exogenous',
                        'AV/UN', 'EN/EX', 'splitting'],
        'files_equipment': lambda eq: [],
        'files_factory': _glob_knowledge('factory/advanced_exergy', max_files=4),
    },
    {
        'topic': 'energy_management',
        'keywords_tr': ['ISO 50001', 'enerji yönetimi', 'enerji yonetimi', 'EN 16247',
                        'IPMVP', 'EnPI', 'CUSUM', 'M&V', 'mevzuat', 'yönetmelik', 'yonetmelik',
                        'Türkiye', 'turkiye', 'verimlilik kanunu'],
        'keywords_en': ['ISO 50001', 'energy management', 'EN 16247', 'IPMVP',
                        'regulation', 'legislation', 'energy law'],
        'files_equipment': lambda eq: [],
        'files_factory': _glob_knowledge('factory/energy_management', max_files=4),
    },
    {
        'topic': 'waste_heat',
        'keywords_tr': ['atık ısı', 'atik isi', 'geri kazanım', 'geri kazanim', 'CHP',
                        'kojenerasyon', 'trijenerasyon', 'HRSG', 'ORC', 'ısı pompası', 'isi pompasi'],
        'keywords_en': ['waste heat', 'heat recovery', 'CHP', 'cogeneration', 'trigeneration',
                        'HRSG', 'ORC', 'heat pump'],
        'files_equipment': lambda eq: [],
        'files_factory': ['factory/waste_heat_recovery.md', 'factory/cogeneration.md',
                          'factory/heat_integration.md'],
    },
    {
        'topic': 'sector',
        'keywords_tr': ['gıda', 'gida', 'çimento', 'cimento', 'tekstil', 'kağıt', 'kagit',
                        'metal', 'otomotiv', 'kimya', 'seramik', 'ahşap', 'ahsap', 'şeker', 'seker'],
        'keywords_en': ['food', 'cement', 'textile', 'paper', 'metal', 'automotive', 'chemical',
                        'ceramic', 'wood', 'sugar'],
        'files_equipment': lambda eq: _glob_knowledge(f'{eq}/sectors') if os.path.isdir(
            os.path.join(KNOWLEDGE_DIR, eq, 'sectors')) else [],
        'files_factory': lambda q: _match_sector_files(q),  # Dinamik sektör eşleme
    },
    {
        'topic': 'formulas',
        'keywords_tr': ['formül', 'formul', 'denklem', 'hesaplama', 'nasıl hesaplanır',
                        'matematiksel', 'termodinamik', 'bağıntı', 'baginti'],
        'keywords_en': ['formula', 'equation', 'calculation', 'how to calculate',
                        'mathematical', 'thermodynamic'],
        'files_equipment': lambda eq: [f'{eq}/formulas.md'],
        'files_factory': ['factory/exergy_fundamentals.md'],
    },
    {
        'topic': 'equipment_detail',
        'keywords_tr': ['vidali', 'pistonlu', 'scroll', 'santrifüj', 'santrifuj',
                        'firetube', 'watertube', 'kondensing', 'atık ısı kazanı',
                        'vida', 'kademeli', 'emme', 'basma',
                        'shell and tube', 'plakalı', 'plakali', 'kanatlı', 'kanatli',
                        'geri basınçlı', 'geri basinçli', 'kondansasyon', 'çekiş', 'cekis'],
        'keywords_en': ['screw', 'piston', 'reciprocating', 'scroll', 'centrifugal',
                        'firetube', 'watertube', 'condensing', 'shell tube', 'plate',
                        'finned', 'backpressure', 'condensing turbine', 'extraction'],
        'files_equipment': lambda eq: _glob_knowledge(f'{eq}/equipment'),
        'files_factory': [],
    },
]


# Sektör → dosya eşleme
SECTOR_MAP = {
    'gıda': 'sector_food', 'gida': 'sector_food', 'food': 'sector_food', 'şeker': 'sector_food', 'seker': 'sector_food',
    'çimento': 'sector_cement', 'cimento': 'sector_cement', 'cement': 'sector_cement',
    'tekstil': 'sector_textile', 'textile': 'sector_textile',
    'kağıt': 'sector_paper', 'kagit': 'sector_paper', 'paper': 'sector_paper',
    'metal': 'sector_metal',
    'otomotiv': 'sector_automotive', 'automotive': 'sector_automotive',
    'kimya': 'sector_chemical', 'chemical': 'sector_chemical',
}


def _glob_knowledge(subpath: str, max_files: int = 6) -> list:
    """Bir knowledge alt dizinindeki .md dosyalarını listele"""
    full_path = os.path.join(KNOWLEDGE_DIR, subpath)
    if not os.path.isdir(full_path):
        return []
    files = sorted([
        f'{subpath}/{f}' for f in os.listdir(full_path)
        if f.endswith('.md') and f != 'INDEX.md'
    ])
    return files[:max_files]


def _match_sector_files(question: str) -> list:
    """Sorudan sektör tespit et ve ilgili factory sektör dosyasını döndür"""
    q_lower = question.lower()
    matched = []
    for keyword, sector_file in SECTOR_MAP.items():
        if keyword in q_lower:
            matched.append(f'factory/{sector_file}.md')
    return list(set(matched))[:2]


def route_knowledge(question: str, equipment_type: str,
                    subtype: str = None) -> List[str]:
    """
    Kullanıcının sorusuna ve ekipman context'ine göre
    yüklenecek knowledge dosyalarının listesini döndür.
    
    Args:
        question: Kullanıcının sorusu
        equipment_type: Mevcut ekipman tipi (compressor, boiler, vb.)
        subtype: Ekipman alt tipi (opsiyonel)
    
    Returns:
        Yüklenecek dosya yollarının listesi (knowledge/ dizinine göreceli)
        Maximum 8 dosya.
    """
    q_lower = question.lower()
    files = []
    
    # ─── Tier 1: Her zaman yüklenen (equipment base) ───
    base_files = [
        f'{equipment_type}/INDEX.md',
        f'{equipment_type}/benchmarks.md',
        f'{equipment_type}/formulas.md',
    ]
    for f in base_files:
        if os.path.isfile(os.path.join(KNOWLEDGE_DIR, f)):
            files.append(f)
    
    # ─── Tier 2: Topic-based routing ───
    matched_topics = []
    for route in TOPIC_ROUTES:
        all_keywords = route['keywords_tr'] + route['keywords_en']
        for kw in all_keywords:
            if kw.lower() in q_lower:
                matched_topics.append(route)
                break
    
    for route in matched_topics:
        # Equipment-specific files
        eq_files_fn = route['files_equipment']
        if callable(eq_files_fn):
            eq_files = eq_files_fn(equipment_type)
            for f in eq_files:
                if f not in files and os.path.isfile(os.path.join(KNOWLEDGE_DIR, f)):
                    files.append(f)
        
        # Factory-level files
        fac_files = route['files_factory']
        if callable(fac_files):
            fac_files = fac_files(question)
        for f in fac_files:
            if f not in files and os.path.isfile(os.path.join(KNOWLEDGE_DIR, f)):
                files.append(f)
    
    # ─── Tier 3: Fallback — eğer hiç topic match yoksa ───
    if not matched_topics:
        # Genel çözüm dosyalarını yükle
        solutions = _glob_knowledge(f'{equipment_type}/solutions', max_files=3)
        for f in solutions:
            if f not in files:
                files.append(f)
    
    # ─── Max 8 dosya limiti ───
    return files[:8]


def get_knowledge_summary(files: List[str]) -> str:
    """Debug/log için: hangi dosyaların yüklendiğinin özeti"""
    return f"[Knowledge Router] {len(files)} dosya seçildi: {', '.join(os.path.basename(f) for f in files)}"
```

**NOT:** Yukarıdaki kod referans. Mevcut `_load_relevant_knowledge()` fonksiyonunun yapısına uyarla. `_read_file_cached()` fonksiyonu zaten var — onu kullan.

---

## 📦 Adım 2: Backend — Chat Service

### 2.1 `ClaudeCodeClient`'a chat metodu ekle

`api/services/claude_code_service.py`'ye yeni metod:

```python
async def chat(self, equipment_type: str, subtype: str,
               question: str, analysis_data: dict,
               history: list = None) -> dict:
    """
    Knowledge-powered sohbet.
    
    Args:
        equipment_type: Ekipman tipi
        subtype: Alt tip
        question: Kullanıcının sorusu
        analysis_data: Mevcut analiz sonuçları (metrics dict)
        history: Önceki mesajlar [{"role": "user/assistant", "content": "..."}]
    
    Returns:
        {
            "answer": "Markdown cevap...",
            "knowledge_sources": ["benchmarks.md", "solutions/vsd.md", ...],
            "follow_up_suggestions": ["...", "...", "..."]
        }
    """
```

### 2.2 Chat Prompt Yapısı

```
SYSTEM CONTEXT:
─────────────
Sen ExergyLab AI enerji danışmanısın.
Kullanıcı bir {equipment_label} ({subtype}) analizi yapmış ve sana soru soruyor.

MEVCUT ANALİZ VERİLERİ:
─────────────
{analysis_data formatlanmış}

BİLGİ KAYNAKLARI:
─────────────
{knowledge dosyaları içerikleri — router tarafından seçilmiş}

ÖNCEKİ SOHBET:
─────────────
{history — son 5 turn}

KURALLAR:
─────────────
1. Türkçe cevap ver.
2. Cevabını mevcut analiz verileriyle ilişkilendir. Soyut kalma — "Senin kompresörünün verimi %63, bu..." gibi somut ol.
3. Formül kullanıyorsan LaTeX değil, düz metin kullan.
4. Bilmediğin bir şey sorulursa "Bu konuda bilgi tabanımda yeterli veri yok" de — uydurma.
5. Cevap sonunda 2-3 takip sorusu öner.
6. Cevabı Markdown formatında ver (başlıklar, bold, liste kullanabilirsin).
7. Maximum 400 kelime.

KULLANICI SORUSU:
─────────────
{question}

CEVAP FORMAT (JSON):
{
  "answer": "Markdown cevap...",
  "knowledge_sources": ["dosya1.md", "dosya2.md"],
  "follow_up_suggestions": ["Soru 1?", "Soru 2?", "Soru 3?"]
}
```

### 2.3 Implementasyon Detayları

```python
async def chat(self, equipment_type, subtype, question, analysis_data, history=None):
    """Knowledge-powered chat"""
    
    # 1. Knowledge routing
    from api.services.knowledge_router import route_knowledge, get_knowledge_summary
    knowledge_files = route_knowledge(question, equipment_type, subtype)
    
    # 2. Knowledge içeriklerini yükle
    knowledge_content = ""
    loaded_sources = []
    for rel_path in knowledge_files:
        full_path = os.path.join(KNOWLEDGE_DIR, rel_path)
        try:
            content = _read_file_cached(full_path)
            knowledge_content += f"\n\n--- {rel_path} ---\n{content}"
            loaded_sources.append(os.path.basename(rel_path))
        except Exception:
            pass
    
    # 3. Skills yükle (core skills her zaman)
    skills = self._load_skills(equipment_type)
    
    # 4. Analysis data formatla
    analysis_str = self._format_analysis_for_chat(analysis_data)
    
    # 5. History formatla (son 5 turn)
    history_str = ""
    if history:
        for msg in history[-5:]:
            role = "Kullanıcı" if msg["role"] == "user" else "AI"
            history_str += f"\n{role}: {msg['content']}\n"
    
    # 6. Prompt birleştir
    equipment_label = EQUIPMENT_LABELS.get(equipment_type, equipment_type)
    prompt = f"""Sen ExergyLab AI enerji danışmanısın.
Kullanıcı bir {equipment_label} ({subtype or 'genel'}) analizi yapmış ve sana soru soruyor.

{skills}

=== MEVCUT ANALİZ VERİLERİ ===
{analysis_str}

=== BİLGİ KAYNAKLARI ===
{knowledge_content}

=== ÖNCEKİ SOHBET ===
{history_str if history_str else "(İlk soru)"}

=== KURALLAR ===
1. Türkçe cevap ver.
2. Cevabını MUTLAKA mevcut analiz verileriyle ilişkilendir. "Senin ekipmanının verimi %X..." gibi somut ol.
3. Formül kullanıyorsan düz metin kullan (LaTeX değil).
4. Bilmediğin şey sorulursa dürüst ol — uydurma.
5. Cevap sonunda 2-3 takip sorusu öner.
6. Markdown formatında yaz.
7. Maximum 400 kelime.
8. Kullandığın kaynak dosyaları knowledge_sources'a ekle.

=== KULLANICI SORUSU ===
{question}

Cevabını SADECE aşağıdaki JSON formatında ver, başka bir şey yazma:
{{"answer": "Markdown cevap...", "knowledge_sources": ["dosya1.md", "dosya2.md"], "follow_up_suggestions": ["Soru 1?", "Soru 2?", "Soru 3?"]}}"""

    # 7. Claude CLI çağır
    try:
        result = await self._call_claude(prompt)
        parsed = self._extract_json(result)
        if parsed and 'answer' in parsed:
            parsed['knowledge_sources'] = parsed.get('knowledge_sources', loaded_sources)
            if not parsed.get('follow_up_suggestions'):
                parsed['follow_up_suggestions'] = []
            return parsed
    except Exception as e:
        pass
    
    # 8. Fallback
    return {
        "answer": "Üzgünüm, şu anda cevap üretemiyorum. Lütfen tekrar deneyin.",
        "knowledge_sources": loaded_sources,
        "follow_up_suggestions": [],
        "ai_available": False,
    }
```

**ÖNEMLİ NOT:** Mevcut `interpret()` metodu `asyncio.create_subprocess_exec("claude", "-p", prompt)` kullanıyor. Chat metodu da aynı subprocess mekanizmasını kullanmalı. Mevcut `interpret()` metodundaki subprocess çağrısını ortak bir `_call_claude(prompt)` helper'a çıkarmak iyi olabilir — DRY.

---

## 📦 Adım 3: Backend — Chat API Endpoint

### 3.1 `api/routes/chat.py` — Yeni Route Dosyası

```python
"""
ExergyLab - AI Chat Endpoint
Knowledge-powered sohbet API'si.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
from api.services.claude_code_service import ClaudeCodeClient

router = APIRouter(prefix="/api", tags=["chat"])


class ChatMessage(BaseModel):
    role: str  # "user" veya "assistant"
    content: str


class ChatRequest(BaseModel):
    equipment_type: str
    subtype: Optional[str] = None
    question: str
    analysis_data: Optional[Dict] = None
    history: Optional[List[ChatMessage]] = []


class ChatResponse(BaseModel):
    answer: str = ""
    knowledge_sources: List[str] = []
    follow_up_suggestions: List[str] = []
    ai_available: bool = True


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Knowledge-powered AI chat.
    Analiz context'inde soru-cevap.
    """
    if not request.question or not request.question.strip():
        raise HTTPException(400, "Soru boş olamaz")

    client = ClaudeCodeClient.get_instance()
    
    history = [{"role": m.role, "content": m.content} for m in (request.history or [])]
    
    result = await client.chat(
        equipment_type=request.equipment_type,
        subtype=request.subtype,
        question=request.question.strip(),
        analysis_data=request.analysis_data or {},
        history=history,
    )
    
    return ChatResponse(
        answer=result.get("answer", ""),
        knowledge_sources=result.get("knowledge_sources", []),
        follow_up_suggestions=result.get("follow_up_suggestions", []),
        ai_available=result.get("ai_available", True),
    )
```

### 3.2 Router'ı main.py'ye ekle

```python
# api/main.py'de:
from api.routes.chat import router as chat_router
app.include_router(chat_router)
```

---

## 📦 Adım 4: Frontend — Chat Panel Component

### 4.1 `frontend/src/components/chat/ChatPanel.jsx`

```jsx
// Temel chat arayüzü:
// - Mesaj listesi (scroll)
// - Input alanı + gönder butonu
// - Follow-up suggestion chips
// - Loading indicator
// - Knowledge sources gösterimi
// - Markdown rendering

export default function ChatPanel({
  equipmentType,
  subtype,
  analysisData,    // Mevcut analiz sonuçları
  isVisible,       // Panel açık mı
  onClose,         // Kapatma handler
}) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Auto-scroll
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = async (question) => {
    if (!question.trim() || isLoading) return;

    // User mesajını ekle
    const userMsg = { role: 'user', content: question };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await chatWithAI({
        equipment_type: equipmentType,
        subtype: subtype,
        question: question,
        analysis_data: analysisData,
        history: messages.slice(-10),  // Son 10 mesaj (5 turn)
      });

      const assistantMsg = {
        role: 'assistant',
        content: response.answer,
        knowledge_sources: response.knowledge_sources,
        follow_up_suggestions: response.follow_up_suggestions,
      };
      setMessages(prev => [...prev, assistantMsg]);
    } catch (error) {
      const errorMsg = {
        role: 'assistant',
        content: 'Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.',
        isError: true,
      };
      setMessages(prev => [...prev, errorMsg]);
    } finally {
      setIsLoading(false);
    }
  };

  // Render:
  // - Header: "AI Danışman" + close button
  // - Messages list with role-based styling
  // - Follow-up suggestion chips (tıklanabilir)
  // - Input area: textarea + send button
  // - Loading: animated dots veya spinner
}
```

### 4.2 UI Detayları

**Mesaj Styling:**
- User mesajı: sağda, mavi arka plan, beyaz yazı
- AI mesajı: solda, beyaz arka plan, gri border
- AI mesajının altında: knowledge sources (küçük etiketler), follow-up chips

**Markdown Rendering:**
- AI cevabı Markdown gelecek. `dangerouslySetInnerHTML` ile basit render VEYA basit bir markdown-to-html çevirici yaz (bold, italic, başlık, liste, code block destekli).
- **Yeni npm paketi EKLEME** — basit regex-based markdown rendering yap veya mevcut halinde düz metin göster.

**Follow-up Chips:**
```jsx
{msg.follow_up_suggestions?.map((suggestion, i) => (
  <button
    key={i}
    onClick={() => sendMessage(suggestion)}
    className="text-xs px-3 py-1 bg-blue-50 text-blue-600 rounded-full 
               hover:bg-blue-100 border border-blue-200"
  >
    {suggestion}
  </button>
))}
```

**Knowledge Sources:**
```jsx
{msg.knowledge_sources?.length > 0 && (
  <div className="mt-2 flex flex-wrap gap-1">
    <span className="text-xs text-gray-400">Kaynaklar:</span>
    {msg.knowledge_sources.map((src, i) => (
      <span key={i} className="text-xs px-2 py-0.5 bg-gray-100 rounded text-gray-500">
        📄 {src}
      </span>
    ))}
  </div>
)}
```

### 4.3 Basit Markdown Renderer (npm paketi eklemeden)

```javascript
function renderMarkdown(text) {
  if (!text) return '';
  return text
    // Headers
    .replace(/^### (.*$)/gm, '<h4 class="font-semibold text-sm mt-3 mb-1">$1</h4>')
    .replace(/^## (.*$)/gm, '<h3 class="font-semibold text-base mt-3 mb-1">$1</h3>')
    .replace(/^# (.*$)/gm, '<h2 class="font-bold text-lg mt-4 mb-2">$1</h2>')
    // Bold & Italic
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    // Inline code
    .replace(/`(.*?)`/g, '<code class="px-1 py-0.5 bg-gray-100 rounded text-sm">$1</code>')
    // Bullet lists
    .replace(/^- (.*$)/gm, '<li class="ml-4 list-disc">$1</li>')
    // Line breaks
    .replace(/\n\n/g, '<br/><br/>')
    .replace(/\n/g, '<br/>');
}
```

---

## 📦 Adım 5: Frontend — EquipmentAnalysis Entegrasyonu

### 5.1 State ve Handler

```jsx
// EquipmentAnalysis.jsx'e ekle:
const [chatOpen, setChatOpen] = useState(false);

// Render'da — sonuçlar gösterildikten sonra:
// 1. "AI Danışmana Sor" butonu
// 2. ChatPanel (chatOpen === true ise)
```

### 5.2 Layout

```
┌────────────────────────────────────────────────────┐
│ Ekipman Tipi + Alt Tip Seçimi                      │
├──────────────────────┬─────────────────────────────┤
│ Parametre Formu      │ Sonuçlar                    │
│                      │  MetricsCards               │
│ [Analiz Et]          │  AV/UN Bar                  │
│                      │  Radar Chart                │
│                      │  Sankey                     │
│                      │  AI Yorum                   │
│                      │  [What-If]                  │
├──────────────────────┴─────────────────────────────┤
│                                                    │
│  ┌───────────────────────────────────────────────┐ │
│  │ 💬 AI Danışmana Sor  (toggle button)          │ │
│  └───────────────────────────────────────────────┘ │
│                                                    │
│  ┌───────────────────────────────────────────────┐ │
│  │ ChatPanel (açılınca)                          │ │
│  │                                               │ │
│  │  AI: Merhaba! Bu kompresör analiziniz         │ │
│  │  hakkında sorularınızı yanıtlayabilirim.      │ │
│  │                                               │ │
│  │  User: VSD takarsak ne kadar tasarruf ederiz? │ │
│  │                                               │ │
│  │  AI: Mevcut analiz verilerinize göre...       │ │
│  │  📄 solutions/vsd.md  📄 benchmarks.md        │ │
│  │  [Enerji fiyatı etkisi?] [Geri ödeme süresi?]│ │
│  │                                               │ │
│  │  ┌─────────────────────────────┐ [Gönder]     │ │
│  │  │ Sorunuzu yazın...           │              │ │
│  │  └─────────────────────────────┘              │ │
│  └───────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────┘
```

### 5.3 Açılış Mesajı

Chat panel açıldığında otomatik "welcome" mesajı:

```javascript
const getWelcomeMessage = (equipmentType, analysisData) => {
  const efficiency = analysisData?.metrics?.exergy_efficiency_pct;
  const grade = analysisData?.radar_data?.grade;
  return {
    role: 'assistant',
    content: `Merhaba! Bu ${EQUIPMENT_LABELS[equipmentType]} analiziniz hakkında sorularınızı yanıtlayabilirim. ` +
      (efficiency ? `Mevcut exergy veriminiz **%${efficiency.toFixed(1)}**${grade ? ` (${grade})` : ''}. ` : '') +
      `İyileştirme önerileri, teknik detaylar veya maliyet analizi hakkında soru sorabilirsiniz.`,
    follow_up_suggestions: [
      'İyileştirme için ne önerirsin?',
      'Avoidable yıkımı nasıl azaltırım?',
      'Bu sektörde benchmark nedir?',
    ],
  };
};
```

### 5.4 `api.js` — Chat fonksiyonu

```javascript
export async function chatWithAI({ equipment_type, subtype, question, analysis_data, history }) {
  const response = await axios.post(`${API_BASE}/api/chat`, {
    equipment_type,
    subtype,
    question,
    analysis_data,
    history,
  });
  return response.data;
}
```

---

## 📦 Adım 6: Testler

### 6.1 `tests/test_knowledge_router.py`

```python
"""Knowledge Router testleri"""
import pytest
from api.services.knowledge_router import route_knowledge


class TestRouteKnowledge:

    def test_base_files_always_loaded(self):
        """Temel dosyalar (INDEX, benchmarks, formulas) her zaman yüklenir"""
        files = route_knowledge("herhangi bir soru", "compressor")
        basenames = [os.path.basename(f) for f in files]
        assert 'INDEX.md' in basenames
        assert 'benchmarks.md' in basenames
        assert 'formulas.md' in basenames

    def test_solutions_routing(self):
        """Çözüm soruları solutions/ dosyalarını yükler"""
        files = route_knowledge("İyileştirme önerisi nedir?", "compressor")
        assert any('solutions' in f for f in files)

    def test_audit_routing(self):
        """Denetim soruları audit.md yükler"""
        files = route_knowledge("Denetim nasıl yapılır?", "boiler")
        assert any('audit' in f for f in files)

    def test_pinch_routing(self):
        """Pinch soruları factory/pinch/ yükler"""
        files = route_knowledge("Pinch analizi nasıl yapılır?", "heat_exchanger")
        assert any('pinch' in f for f in files)

    def test_economics_routing(self):
        """Ekonomi soruları ilgili dosyaları yükler"""
        files = route_knowledge("Yatırım maliyeti ne kadar?", "pump")
        assert any('economic' in f.lower() or 'cost' in f.lower() or 'price' in f.lower() for f in files)

    def test_max_files_limit(self):
        """Maximum 8 dosya limiti"""
        files = route_knowledge("pinch exergoekonomik entropi çözüm denetim audit", "compressor")
        assert len(files) <= 8

    def test_no_duplicates(self):
        """Aynı dosya iki kez yüklenmemeli"""
        files = route_knowledge("formül hesaplama denklem", "boiler")
        assert len(files) == len(set(files))

    def test_unknown_equipment(self):
        """Bilinmeyen ekipman tipi crash etmemeli"""
        files = route_knowledge("test sorusu", "unknown_type")
        assert isinstance(files, list)

    def test_all_equipment_types(self):
        """Tüm 7 ekipman tipi için routing çalışmalı"""
        for eq in ['compressor', 'boiler', 'chiller', 'pump',
                    'heat_exchanger', 'steam_turbine', 'dryer']:
            files = route_knowledge("İyileştirme önerilerin neler?", eq)
            assert len(files) >= 1, f'{eq}: no files returned'

    def test_sector_routing(self):
        """Sektör soruları sector dosyalarını yükler"""
        files = route_knowledge("Gıda sektöründe kurutma", "dryer")
        # Sektör dosyası veya sector dizini içermeli
        assert len(files) >= 3  # base + sector

    def test_turkish_keywords(self):
        """Türkçe anahtar kelimeler çalışmalı"""
        files = route_knowledge("Bejan sayısı nedir?", "heat_exchanger")
        assert any('entropy' in f for f in files)

    def test_fallback_loads_solutions(self):
        """Topic match yoksa solutions yüklenmeli"""
        files = route_knowledge("xyz abc bilinmeyen konu", "pump")
        assert any('solutions' in f for f in files)


class TestChatAPI:
    """Chat endpoint testleri — Claude CLI'sız test edilemez ama endpoint structure test edilebilir"""

    def test_chat_endpoint_exists(self, client):
        """Chat endpoint mevcut olmalı"""
        resp = client.post('/api/chat', json={
            'equipment_type': 'compressor',
            'question': 'Test sorusu',
        })
        # Claude CLI olmadan 200 veya timeout/fallback dönmeli, 404 DEĞİL
        assert resp.status_code != 404

    def test_chat_empty_question_rejected(self, client):
        """Boş soru → 400"""
        resp = client.post('/api/chat', json={
            'equipment_type': 'compressor',
            'question': '',
        })
        assert resp.status_code == 400

    def test_chat_request_schema(self, client):
        """Geçerli request şeması kabul edilmeli"""
        resp = client.post('/api/chat', json={
            'equipment_type': 'compressor',
            'subtype': 'screw',
            'question': 'Test sorusu',
            'analysis_data': {'exergy_efficiency_pct': 65},
            'history': [
                {'role': 'user', 'content': 'Merhaba'},
                {'role': 'assistant', 'content': 'Size nasıl yardımcı olabilirim?'}
            ],
        })
        # 404 değil — endpoint var
        assert resp.status_code != 404
```

---

## 📋 Entegrasyon Doğrulama

```bash
# 1. Knowledge Router çalışıyor
python3 -c "
from api.services.knowledge_router import route_knowledge, get_knowledge_summary
files = route_knowledge('VSD takarsak ne kadar tasarruf ederiz?', 'pump')
print(get_knowledge_summary(files))
for f in files:
    print(f'  📄 {f}')
"

# 2. Router çeşitli sorularla
python3 -c "
from api.services.knowledge_router import route_knowledge
tests = [
    ('İyileştirme önerisi?', 'compressor'),
    ('Pinch analizi nasıl yapılır?', 'heat_exchanger'),
    ('Exergoekonomik değerlendirme', 'boiler'),
    ('Bejan sayısı ne demek?', 'pump'),
    ('Gıda sektöründe kurutma verimliliği', 'dryer'),
    ('ISO 50001 gereklilikleri', 'boiler'),
    ('Denetim nasıl yapılır?', 'chiller'),
    ('Yatırım maliyeti hesabı', 'steam_turbine'),
]
for q, eq in tests:
    files = route_knowledge(q, eq)
    print(f'✅ \"{q}\" ({eq}) → {len(files)} dosya')
"

# 3. Chat API endpoint erişilebilir (Claude CLI olmadan fallback dönmeli)
python3 -c "
from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)
resp = client.post('/api/chat', json={
    'equipment_type': 'compressor',
    'subtype': 'screw',
    'question': 'Verimlilik nasıl artırılır?',
    'analysis_data': {'exergy_efficiency_pct': 65},
})
print(f'Status: {resp.status_code}')
data = resp.json()
print(f'Answer: {data.get(\"answer\", \"N/A\")[:100]}...')
print(f'Sources: {data.get(\"knowledge_sources\", [])}')
"

# 4. Frontend build
cd frontend && npx vite build 2>&1 | tail -5

# 5. Tüm testler
cd .. && pytest tests/ -v | tail -20
```

---

## ⚠️ Dikkat Edilecekler

1. **Claude CLI Bağımlılığı.** Chat metodu `claude -p` subprocess çağırır. CI/test ortamında Claude CLI yoksa fallback cevap döner. Testler bunu handle etmeli — endpoint'in varlığını ve request/response schema'sını test et, AI cevap kalitesini DEĞİL.

2. **Context Window Limiti.** Knowledge dosyaları çok büyük olabilir. Router max 8 dosya seçer ama bazı dosyalar 500+ satır. Toplam prompt boyutunu izle. Gerekirse dosya içeriğini truncate et (ilk 200 satır).

3. **_read_file_cached() yeniden kullan.** Knowledge dosyalarını okumak için yeni fonksiyon YAZMA — mevcut LRU cached reader'ı kullan.

4. **Mevcut interpret akışını BOZMA.** Chat ayrı endpoint, ayrı metot. `interpret()` fonksiyonu aynen kalsın.

5. **Markdown rendering:** Yeni npm paketi EKLEME. Basit regex-based renderer yaz veya `dangerouslySetInnerHTML` ile göster. Güvenlik riski düşük çünkü content sadece Claude'dan geliyor.

6. **History limiti:** Son 5 turn (10 mesaj) yeterli. Daha fazlası prompt'u şişirir.

7. **Welcome mesajı:** Frontend'de generate et, backend'e gönderme. Analiz datasından verim ve grade çek.

---

## ✅ Tamamlanma Kriterleri

- [ ] `api/services/knowledge_router.py` oluşturuldu — `route_knowledge()` çalışıyor
- [ ] `ClaudeCodeClient.chat()` metodu eklendi
- [ ] `api/routes/chat.py` oluşturuldu — `/api/chat` endpoint
- [ ] Router `api/main.py`'ye eklendi
- [ ] `ChatPanel.jsx` component oluşturuldu (mesaj listesi, input, follow-up chips, markdown render)
- [ ] `EquipmentAnalysis.jsx` entegre edildi — "AI Danışmana Sor" butonu + ChatPanel
- [ ] `api.js` — `chatWithAI()` fonksiyonu eklendi
- [ ] Knowledge Router tüm 7 ekipman tipinde çalışıyor
- [ ] Knowledge Router 12+ farklı topic route'unu destekliyor
- [ ] Welcome mesajı analiz datası ile özelleştirilmiş
- [ ] Follow-up suggestion chips tıklanabilir
- [ ] Mevcut 413 test hâlâ geçiyor
- [ ] Yeni testler (~15) geçiyor
- [ ] Frontend build başarılı
- [ ] `git add -A && git commit && git push`

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| AI etkileşim | Statik yorum | İnteraktif sohbet |
| Knowledge kullanımı | 2 dosya/analiz | 5-8 dosya/soru (305 havuz) |
| Topic coverage | Sadece benchmark+formül | 12 topic route |
| Kullanıcı etkileşimi | Tek yönlü | Çok turlu sohbet |
| Test sayısı | 413 | ~428+ |
