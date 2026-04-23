"""
1.3.5  आदिरञिटुडवः  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — first **hal** in **ñi∪ṭu∪ḍu** (``NI_TU_DU``) in the
  upadeśa gets *it* (candidate tag → **1.3.9** lopa).

• **Scope:** Non-taddhita **sup** rows when present; else the primary upadeśa
  term (``terms[0]``), matching v2 ``_terms_sup_or_primary_upadesha``.

• **v2 reference:** ``~/Documents/panini_engine_v2/core/it_rules.py``
  ``cond_1_3_5`` /
  ``act_1_3_5``.
"""
from __future__ import annotations

from typing import Optional

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import NI_TU_DU
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
    for j, v in enumerate(varnas):
        if v.slp1 in HAL_DEV:
            return j
    return None


def _eligible(state: State):
    if not any("upadesha" in t.tags for t in state.terms):
        return
    for term in _terms_sup_or_primary(state):
        try:
            ti = state.terms.index(term)
        except ValueError:
            continue
        vs = term.varnas
        j = _first_hal_idx(vs)
        if j is None:
            continue
        v = vs[j]
        if v.slp1 not in NI_TU_DU:
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
    v.tags.add("it_candidate_nit_tu_du")
    # In dhātu upadeśas like "qupac~z", the anubandha is "qu" (डु) —
    # both the initial hal (q) and the following vowel (u) are part of the marker.
    # We tag the following 'u' as it-candidate too when present.
    if j + 1 < len(term.varnas) and term.varnas[j + 1].slp1 == "u":
        term.varnas[j + 1].tags.add("it_candidate_nit_tu_du")
        state.samjna_registry[("it_nit_tu_du", ti, j, "qu")] = frozenset({v.slp1, "u"})
    else:
        state.samjna_registry[("it_nit_tu_du", ti, j)] = frozenset({v.slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.5",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "AdiraYiTuDavAH",
    text_dev       = "आदिरञिटुडवः",
    padaccheda_dev = "आदिः ञि-टु-ड-वः",
    why_dev        = "ञ्-इट्-डु-वर्णेषु प्रथमः हल् ‘इत्’ संज्ञकः; लोपः १.३.९।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
