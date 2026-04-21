"""
1.3.7  चुटु  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — first **hal** belonging to **cuṭ** (``CUTU``) in the
  upadeśa is *it*.

• **Scope:** Non-**dhātu**, **sup**-primary term list (same as **1.3.5**).

• **v2 reference:** panini_engine_v2/core/it_rules.py ``cond_1_3_7`` /
  ``act_1_3_7``.
"""
from __future__ import annotations

from typing import Optional

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import CUTU
from phonology.varna import HAL_DEV

from sutras.adhyaya_1.pada_3.sutra_1_3_9 import IT_LOPA_TAGS


def _terms_sup_or_primary(state: State):
    cand = [
        t for t in state.terms
        if "sup" in t.tags and "taddhita" not in t.tags
    ]
    if cand:
        return cand
    krt = [
        t for t in state.terms
        if "krt" in t.tags and "upadesha" in t.tags
    ]
    if krt:
        return krt
    if state.terms:
        return [state.terms[0]]
    return []


def _first_hal_idx(varnas) -> Optional[int]:
    # Use canonical hal inventory (includes ``R`` = ण्), not only ``pratyahara.HAL``.
    for j, v in enumerate(varnas):
        if v.slp1 in HAL_DEV:
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
        if v.slp1 not in CUTU:
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
    v.tags.add("it_candidate_cutu")
    # Include current upadeśa identity in the key so a later pratyaya-substitution
    # that reintroduces a cuṭu-initial hal at the same (ti,j) still records a
    # distinct saṃjñā event (avoids R2 false-positive on re-fires).
    upa = term.meta.get("upadesha_slp1")
    state.samjna_registry[("it_cutu", ti, j, upa)] = frozenset({v.slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.7",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "cuwu",
    text_dev       = "चुटु",
    padaccheda_dev = "चुटु",
    why_dev        = "चवर्ग-टवर्गीयः प्रथमः हल् ‘इत्’ संज्ञकः; लोपः १.३.९।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
