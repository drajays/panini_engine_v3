"""
1.3.6  षः प्रत्ययस्य  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — initial **ṣ** (SLP1 ``z``) of a **pratyaya** upadeśa
  (not of a **dhātu**) is *it*.

• **Scope:** Same term scan as **1.3.5** / **1.3.7**; skips **dhātu**-tagged
  terms.

• **v2 reference:** panini_engine_v2/core/it_rules.py ``cond_1_3_6`` /
  ``act_1_3_6`` (v3 scans the sup pratyaya term in multi-term states).
"""
from __future__ import annotations

from typing import Optional

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import HAL

from sutras.adhyaya_1.pada_3.sutra_1_3_9 import IT_LOPA_TAGS


def _terms_sup_or_primary(state: State):
    cand = [
        t for t in state.terms
        if "sup" in t.tags and "taddhita" not in t.tags
    ]
    if cand:
        return cand
    if state.terms:
        return [state.terms[0]]
    return []


def _first_hal_idx(varnas) -> Optional[int]:
    for j, v in enumerate(varnas):
        if v.slp1 in HAL:
            return j
    return None


def _eligible(state: State):
    if not any("upadesha" in t.tags for t in state.terms):
        return
    for term in _terms_sup_or_primary(state):
        if "dhatu" in term.tags:
            continue
        try:
            ti = state.terms.index(term)
        except ValueError:
            continue
        vs = term.varnas
        j = _first_hal_idx(vs)
        if j is None:
            continue
        v = vs[j]
        if v.slp1 != "z":
            continue
        if v.tags & IT_LOPA_TAGS:
            continue
        yield ti, term, j


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    got = next(_eligible(state), None)
    if got is None:
        return state
    ti, term, j = got
    v = term.varnas[j]
    v.tags.add("it_candidate_sha_pratyaya")
    state.samjna_registry[("it_sha_pratyaya", ti, j)] = frozenset({v.slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.6",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "zaH pratyayasya",
    text_dev       = "षः प्रत्ययस्य",
    padaccheda_dev = "षः प्रत्ययस्य",
    why_dev        = "प्रत्ययस्य आदौ ष्-वर्णः ‘इत्’ संज्ञकः; लोपः १.३.९।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
