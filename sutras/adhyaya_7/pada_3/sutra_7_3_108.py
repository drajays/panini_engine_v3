"""
7.3.108  ह्रस्व-घि-अङ्गस्य सम्बुद्धौ गुणः  —  VIDHI

Operational intent for v3.4 (hari-like i-stems):
  - In sambuddhi-ekavacana (tagged on the sup pratyaya by 4.1.2 as
    Term.tags contains 'sambuddhi'), after 6.1.69 deletes the 's' of su,
    apply guṇa to a hrasva ghi aṅga so:

      hari + (sambuddhi su) → hare

Blindness:
  - cond() reads only the pratyaya's 'sambuddhi' tag + aṅga tags/phoneme.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


_GUNA_MAP = {"i": "e", "u": "o"}


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "ghi" not in anga.tags:
        return False
    if "sup" not in pr.tags or "sambuddhi" not in pr.tags:
        return False
    if pr.meta.get("sambuddhi_guna_done"):
        return False
    if not anga.varnas:
        return False
    if anga.varnas[-1].slp1 not in _GUNA_MAP:
        return False
    # Typical trigger: the sambuddhi-su has lost its 's' already.
    if pr.varnas:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    pr   = state.terms[-1]
    anga.varnas[-1] = mk(_GUNA_MAP[anga.varnas[-1].slp1])
    pr.meta["sambuddhi_guna_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.108",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "hrasva-Gi-aNgasya sambuddhau guRaH",
    text_dev       = "ह्रस्व-घि-अङ्गस्य सम्बुद्धौ गुणः",
    padaccheda_dev = "ह्रस्व-घि-अङ्गस्य सम्बुद्धौ गुणः",
    why_dev        = "सम्बुद्धौ (८-१) ह्रस्व-घि-अङ्गस्य गुणः (हरि → हरे)।",
    anuvritti_from = ("7.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

