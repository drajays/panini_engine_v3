"""
8.2.66  ससजुषो रुः  —  VIDHI

"A final 's' or 'sajus' → ru."

Tripāḍī sūtra.  Converts a pada-final 's' into 'ru' (the intermediate
form that 8.3.15 will then convert to visarga at pāda-end).

Two operational paths:

  1. POST-MERGE (single term): operates on the LAST varṇa of the only
     pada-tagged term.  Handles rāmaḥ, dhanuḥ (prathamā/dvitīyā eka) etc.

  2. PRE-MERGE (two-term state, stem has ``pada_1_4_17`` tag from 1.4.17):
     when the stem ends in 's' AND the immediately following pratyaya is
     HAL-initial, convert the stem-final 's' to 'r' before merge.
     This produces DanurByAm, DanurBiH, DanurByaH (tṛtīyā/caturthī/pañcamī).
     Restricted to HAL-initial pratyaya so that AC-initial pratyayas (ṭā→A,
     ṅi→i) go through ṣatvaṁ (8.3.59) post-merge instead.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk
from phonology.pratyahara import HAL


def _target_postmerge(state: State):
    """POST-MERGE: pada-final 's' in the last pada-tagged term (requires single merged term)."""
    if len(state.terms) != 1:
        return None
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if "pada" not in t.tags:
            continue
        if not t.varnas:
            continue
        last = t.varnas[-1]
        if last.slp1 == "s" and "ru_intermediate" not in last.tags:
            return (i, len(t.varnas) - 1)
        if last.slp1 == "a" and last.dev == "" and len(t.varnas) >= 2:
            prev = t.varnas[-2]
            if prev.slp1 == "s" and "ru_intermediate" not in prev.tags:
                return (i, len(t.varnas) - 2)
        return None
    return None


def _target_premerge(state: State):
    """PRE-MERGE: stem with pada tag and final 's' before a HAL-initial pratyaya.
    Checks 'pada' (not 'pada_1_4_17') since 1.4.18 (bha apavāda) may discard pada_1_4_17
    while leaving the 'pada' tag intact.
    """
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        stem = state.terms[i]
        pratyaya = state.terms[i + 1]
        if "pada" not in stem.tags:
            continue
        if not stem.varnas or stem.varnas[-1].slp1 != "s":
            continue
        if "ru_intermediate" in stem.varnas[-1].tags:
            continue
        if not pratyaya.varnas:
            continue
        if pratyaya.varnas[0].slp1 not in HAL:
            continue
        return (i, len(stem.varnas) - 1)
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _target_postmerge(state) is not None or _target_premerge(state) is not None


def act(state: State) -> State:
    ru = mk("r")
    ru.tags.add("ru_intermediate")

    hit = _target_premerge(state)
    if hit is not None:
        ti, vi = hit
        state.terms[ti].varnas[vi] = ru
        return state

    hit = _target_postmerge(state)
    if hit is not None:
        ti, vi = hit
        state.terms[ti].varnas[vi] = ru
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.66",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sasajuzo ruH",
    text_dev       = "ससजुषो रुः",
    padaccheda_dev = "स-सजुषः रुः",
    why_dev        = "पदान्त-सकारस्य सजुषः च रु-आदेशः (त्रिपादी)।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
