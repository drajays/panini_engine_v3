"""
1.1.73  वृद्धिर्यस्याचामादिस्तद् वृद्धम्  —  SAMJNA (*vṛddha-pada*)

**Pāṭha (baked):** *yasya acām ādiḥ vṛddhiḥ, tat vṛddham* — the **first** vowel
(*ac*) in a *pada* (in *varṇa* order) that belongs to the *vṛddhi* set
(**1.1.1** {*ā, ai, au*} → SLP1 ``A, E, O``) licenses the technical name
*vṛddham* for that whole *pada*.

**Vārttika 1 —** *vā nāmadheyasya vṛddha-saṃjñā vaktavyā:* a *pauruṣeya*
proper-name (*nāmadheya*) may **optionally** be called *vṛddham* even when its
first *ac* is not *ā/ai/au*, so that *vṛddhāc chaḥ* (**4.2.114**) etc. may apply
(*devadatta* → *devadattīya* / *daivadatta* + *aṇ* path).  The recipe sets
``state.meta[META_NAMADHEYA_VRDDHA_INDICES]`` to a non-empty ``frozenset`` /
``tuple`` of valid term indices.

**Vārttika 2 —** *jihvākātya-haritakātya-varjam:* *jihvākātya* and *haritakātya*
never receive that optional *vṛddha* licence (``upadesha_slp1`` exact match on
``VARTTIKA2_BLOCKED_STEMS_SLP1``).

**Śāstra cross-refs (*vṛddha* prayoga):** **1.2.65**; **4.1.113**, **148**,
**157**, **160**, **166**, **171**; **4.2.114**, **120**, **125**, **141**;
**4.3.144**; **5.3.62**; **6.4.157** — plus *anuvṛtti* into further rules.

*Engine:* ``samjna_registry[VRIDDHAM_INDICES_KEY]``; also adds ``vṛddha`` to
``Term.tags`` for those indices (audit; **cond** is still phoneme / *vārttika*
based only).  No *vṛddhi* *prayoga* here (**vidhi** sūtras only).  See **1.1.1**
for the *vṛddhi* phoneme set.
"""
from __future__ import annotations

from typing import FrozenSet, Optional

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import AC_DEV

from sutras.adhyaya_1.pada_1.sutra_1_1_1 import VRIDHI_PHONEMES_SLP1

VRIDDHAM_INDICES_KEY = "1.1.73_vrddham_term_indices"
META_NAMADHEYA_VRDDHA_INDICES = "1_1_73_nAmadheya_vrddha_term_indices"

VARTTIKA2_BLOCKED_STEMS_SLP1: FrozenSet[str] = frozenset({
    "jihvAkAtya",
    "haritakAtya",
})


def first_ac_slp1_in_term(term: Term) -> Optional[str]:
    """First vowel letter (*ac*) in ``term.varnas`` reading order, or ``None``."""
    for v in term.varnas:
        if v.slp1 in AC_DEV:
            return v.slp1
    return None


def _upadesha_stem_slp1(term: Term) -> str:
    m = term.meta or {}
    u = m.get("upadesha_slp1")
    return u.strip() if isinstance(u, str) else ""


def varttika2_blocks_vrddha_samjna(term: Term) -> bool:
    """*Jihvākātya-haritakātya-varjam* — no optional *vṛddha* for these stems."""
    return _upadesha_stem_slp1(term) in VARTTIKA2_BLOCKED_STEMS_SLP1


def _nAmadheya_indices(state: State) -> FrozenSet[int]:
    raw = state.meta.get(META_NAMADHEYA_VRDDHA_INDICES)
    if raw is None:
        return frozenset()
    if isinstance(raw, frozenset):
        seq = raw
    elif isinstance(raw, (set, tuple, list)):
        seq = raw
    else:
        return frozenset()
    out: list[int] = []
    for x in seq:
        try:
            out.append(int(x))
        except (TypeError, ValueError):
            continue
    return frozenset(out)


def vrddham_term_indices(state: State) -> FrozenSet[int]:
    """
    Indices of ``state.terms`` that are *vṛddha-pada*:
      • first *ac* ∈ **1.1.1** *vṛddhi*, unless *vārttika* 2 blocks; or
      • index listed under ``META_NAMADHEYA_VRDDHA_INDICES`` (*vārttika* 1),
        unless *vārttika* 2 blocks.
    """
    n = len(state.terms)
    nam = {i for i in _nAmadheya_indices(state) if 0 <= i < n}
    out: list[int] = []
    for i, t in enumerate(state.terms):
        if varttika2_blocks_vrddha_samjna(t):
            continue
        ac0 = first_ac_slp1_in_term(t)
        if ac0 is not None and ac0 in VRIDHI_PHONEMES_SLP1:
            out.append(i)
        elif i in nam:
            out.append(i)
    return frozenset(out)


def cond(state: State) -> bool:
    new = vrddham_term_indices(state)
    old = state.samjna_registry.get(VRIDDHAM_INDICES_KEY)
    if old is None:
        old = frozenset()
    return new != old


def act(state: State) -> State:
    new = vrddham_term_indices(state)
    old = state.samjna_registry.get(VRIDDHAM_INDICES_KEY)
    if not isinstance(old, frozenset):
        old = frozenset()
    for i in old - new:
        if 0 <= i < len(state.terms):
            state.terms[i].tags.discard("vṛddha")
    for i in new:
        if 0 <= i < len(state.terms):
            state.terms[i].tags.add("vṛddha")
    state.samjna_registry[VRIDDHAM_INDICES_KEY] = new
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.73",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "yasya acAm AdiH vfdDiH tat vfdDam",
    text_dev       = "यस्य अचामादिः वृद्धिः, तत् वृद्धम्",
    padaccheda_dev = (
        "वृद्धिः (प्रथमा-एकवचनम्) / यस्य (षष्ठी-एकवचनम्) / "
        "अचाम् (षष्ठी-बहुवचनम्) / आदिः (प्रथमा-एकवचनम्) / "
        "तत् (प्रथमा-एकवचनम्) / वृद्धम् (प्रथमा-एकवचनम्)"
    ),
    why_dev        = (
        "प्रथमः स्वर आ-ऐ-औ-संज्ञकः चेत् पदं वृद्धम्; नामधेये विकल्पेन वृद्ध-संज्ञा "
        "(वा नामधेयस्य…); जिह्वाकात्य-हरितकात्य-वर्जम् इति निषेधः। "
        "तद्धितादौ प्रयोजनम् — ४.२.११४ इत्यादिषु।"
    ),
    anuvritti_from = ("1.1.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
