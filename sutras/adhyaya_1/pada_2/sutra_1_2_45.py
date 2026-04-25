"""
1.2.45  अर्थवदधातुरप्रत्ययः प्रातिपदिकम्  —  SAMJNA

*Padaccheda:* **अर्थवत्**, **अधातुः**, **अप्रत्ययः**, **प्रातिपदिकम्**
(prathamā *ekavacana* each).

A stem that is *arthavat* (meaningful; engine default **True** unless
``meta['arthavad_false']``), **not** a *dhātu*, **not** a *pratyaya*, and **not**
*pratyayānta* / *vyutpanna* (``meta['pratyayanta']`` / ``meta['vyutpanna']``),
receives the *prātipadika* saṃjñā — the *avyutpanna* case (*rāma*, *bālaka*,
…).  *Vyutpanna* bases take *prātipadika* from **1.2.46** *kṛttaddhitasamāsāś ca*
instead (see that module).

*Vṛtti (laghu):* *dhātuṃ pratyayaṃ pratyayāntaṃ ca varjayitvā … prātipadikam*.

English (one-line): Any meaningful word-form that is not a root, not an
affix, and not (treated as) affix-terminated is called *prātipadika*.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state  import State, Term
from engine.it_phonetic import term_phonetic_slp1
from engine.registries.lexicon_lookup import is_in_dhatupatha, is_known_pratyaya

_REGISTRY_KEY = "1.2.45_arthavad_pratipadika_indices"


def _eligible_terms(state: State):
    for i, t in enumerate(state.terms):
        if not _term_eligible(t):
            continue
        yield i


def _term_eligible(t: Term) -> bool:
    if t.kind not in ("prakriti",):
        return False
    if "dhatu" in t.tags:
        return False
    if "pratyaya" in t.tags:
        return False
    if t.meta.get("pratyayanta") or t.meta.get("vyutpanna"):
        return False
    if t.meta.get("arthavad_false"):
        return False
    return True


def _indices_to_add(state: State) -> frozenset[int]:
    # 1.2.45 is the **avyutpanna** prātipadika gate. Once any pratyaya has been
    # attached, prātipadika for this community must come from 1.2.46 instead.
    if any("pratyaya" in t.tags for t in state.terms):
        return frozenset()
    prev = state.samjna_registry.get(_REGISTRY_KEY)
    if not isinstance(prev, frozenset):
        prev = frozenset()
    add: set[int] = set()
    for i in _eligible_terms(state):
        if i in prev:
            continue
        t = state.terms[i]
        slp1 = (t.meta.get("upadesha_slp1") or "").strip() or term_phonetic_slp1(t)
        # adhātu: neither tagged as dhātu, nor present in dhātupāṭha registry
        if is_in_dhatupatha(slp1):
            continue
        # apratyaya: neither tagged as pratyaya, nor present in pratyaya inventory
        if is_known_pratyaya(slp1):
            continue
        add.add(i)
    return frozenset(add)


def cond(state: State) -> bool:
    return len(_indices_to_add(state)) > 0


def act(state: State) -> State:
    prev = state.samjna_registry.get(_REGISTRY_KEY)
    if not isinstance(prev, frozenset):
        prev = frozenset()
    add = _indices_to_add(state)
    new_idx = frozenset(prev | add)
    for i in add:
        state.terms[i].tags.add("prātipadika")
    state.samjna_registry[_REGISTRY_KEY] = new_idx
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.2.45",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "arthavadadhAturapratyayaH prAtipadikam",
    text_dev       = "अर्थवदधातुरप्रत्ययः प्रातिपदिकम्",
    padaccheda_dev = "अर्थवत् अधातुः अप्रत्ययः प्रातिपदिकम्",
    why_dev        = (
        "धातु-प्रत्यय-प्रत्ययान्त-वर्जितम् अर्थवच्छब्दरूपं प्रातिपदिकसंज्ञकम्।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
