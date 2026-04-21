"""
1.1.65  अलोऽन्त्यात् पूर्व उपधा  —  SAMJNA

The phoneme immediately preceding a stem-final *al* (here: last consonant
of the minimal dhātu segment) is called *upadhā*.

Narrow engine use: for a triliteral dhātu shape ``CVC`` (hal–ac–hal), the
medial vowel index is registered for ``7.2.116`` / paribhāṣā alignment.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import AC, HAL


def cond(state: State) -> bool:
    if not state.terms:
        return False
    for ti, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        vs = t.varnas
        if len(vs) < 2:
            continue
        if vs[-1].slp1 not in HAL:
            continue
        if vs[-2].slp1 not in AC:
            continue
        key = ("1.1.65_upadha", ti)
        if state.samjna_registry.get(key) is not None:
            continue
        return True
    return False


def act(state: State) -> State:
    for ti, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        vs = t.varnas
        if len(vs) < 2:
            continue
        if vs[-1].slp1 not in HAL:
            continue
        if vs[-2].slp1 not in AC:
            continue
        key = ("1.1.65_upadha", ti)
        if state.samjna_registry.get(key) is None:
            state.samjna_registry[key] = frozenset({len(vs) - 2})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.65",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "alo antyAt pUrva upadhA",
    text_dev       = "अलोऽन्त्यात् पूर्व उपधा",
    padaccheda_dev = "अलः अन्त्यात् पूर्वः उपधा",
    why_dev        = "अन्त्याल्-वर्णात् पूर्वः वर्णः उपधा-संज्ञकः।",
    anuvritti_from = ("1.1.64",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
