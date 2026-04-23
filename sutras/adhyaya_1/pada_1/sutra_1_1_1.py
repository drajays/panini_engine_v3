"""
1.1.1  वृद्धिरादैच्  (vfdDiH Adaic)  —  SAMJNA

Important facts (engine + śāstra alignment)
──────────────────────────────────────────
• **Scope:** Universal **saṃjñā** — not uttered under any **adhikāra** bracket;
  the name *vṛddhi* is available wherever later sūtras use the word (including
  by **anuvṛtti** into other rules).

• **What this rule does *not* do:** It does **not** perform *vṛddhi*
  substitution on random words. It only **defines** which phonemes count as
  *vṛddhi* (membership in ``samjna_registry['vṛddhi']``). Actual *vṛddhi*
  **prayoga** (operational replacement) is carried out by **vidhi** sūtras
  (e.g. 6.1.88 *vṛddhir eci*, 7.2.x, …) when their own ``cond`` matches — i.e.
  “when some other rule asks for *vṛddhi* in the operational sense.”

• **What ``act`` does:** It registers the **set** {ā, ai, au} in SLP1 as
  {A, E, O}. No ``Term`` is traversed; no word is “tagged” — only the global
  definiendum for the technical term *vṛddhi* is fixed (R2 / SAMJNA contract).

• **Recipe timing:** ``pipelines/subanta`` may call this early so that the
  registry is populated before sandhi passes; that is **scheduling**, not
  “applying vṛddhi to every form.”
  **[Scheduled in the recipe for śāstrīya order; operational *vṛddhi*
  substitution is not applied at this locus — no *vidhi* has yet “called for”
  prayoga; only the saṃjñā registration runs.]**

Nine sūtras where *vṛddhi* (the saṃjñā) is **directly** expressed in the
Aṣṭādhyāyī (sākṣāt); anuvṛtti can carry the term into further rules:
  1.1.3, 1.1.73, 6.1.88, 6.2.105, 6.3.28, 6.3.39, 7.2.1, 7.2.114, 7.3.89

(See ``~/Documents/panini_engine_v2/core/sutra_1_1_1.py`` for the older axiom-registration
pattern; v3 keeps definition in registry + full trace.)
"""
from __future__ import annotations

from typing import FrozenSet, Tuple

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# ── Scholarly / UI metadata (single source for Streamlit + comments) ───────
VRIDHI_PHONEMES_SLP1: FrozenSet[str] = frozenset({"A", "E", "O"})

# (sutra_id, short Devanāgarī lemma) — sākṣāt use of the saṃjñā *vṛddhi*
VRIDHI_SAMJNA_REFERENCING_SUTRAS: Tuple[Tuple[str, str], ...] = (
    ("1.1.3",  "इको गुणवृद्धी"),
    ("1.1.73", "वृद्धिर्यस्याचामादिस्तद् वृद्धम्"),
    ("6.1.88", "वृद्धिरेचि"),
    ("6.2.105", "उत्तरपदवृद्धौ सर्वं च"),
    ("6.3.28", "इद्वृद्धौ"),
    ("6.3.39", "वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे"),
    ("7.2.1", "सिचि वृद्धिः परस्मैपदेषु"),
    ("7.2.114", "मृजेर्वृद्धिः"),
    ("7.3.89", "उतो वृद्धिर्लुकि हलि"),
)


def cond(state: State) -> bool:
    """Register *vṛddhi* membership once (idempotent). Does not mean every
    pada is modified — only the global definiendum is written until complete."""
    existing = state.samjna_registry.get("vṛddhi")
    return existing != VRIDHI_PHONEMES_SLP1


def act(state: State) -> State:
    """Set ``samjna_registry['vṛddhi']`` to the Ā/ai/au phoneme set (SLP1).
    No varṇa mutation; *prayoga* of vṛddhi is left to vidhi sūtras."""
    state.samjna_registry["vṛddhi"] = VRIDHI_PHONEMES_SLP1
    return state


_WHY_DEV = (
    "आ-ऐ-औ इति वृद्धि-संज्ञा (अधिकार-बद्धा न, सर्वत्र उपलब्धा)। "
    "अनया केवल वर्ण-समूहस्य निर्देशः — पदेषु स्वतः परिवर्तनं न। "
    "वृद्धि-प्रयोगः तु यदा विधि-सूत्रेषु (यथा ६.१.८८) प्रसङ्गः, तदा। "
    "अष्टाध्याय्यां 'वृद्धि' इयं संज्ञा नवसु सूत्रेषु साक्षात्, अन्यत्र अनुवृत्त्या च।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.1",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "vfdDiH Adaic",
    text_dev       = "वृद्धिरादैच्",
    padaccheda_dev = "वृद्धिः आत्-ऐच्",
    why_dev        = _WHY_DEV,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
