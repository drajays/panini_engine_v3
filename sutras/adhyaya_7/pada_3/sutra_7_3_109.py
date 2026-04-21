"""
7.3.109  ह्रस्व-अङ्गस्य जसि गुणः  —  VIDHI

Operational intent for v3.4 (hari-like i-stems):
  - Before the pratyaya **jas** (prathamā-pl / sambuddhi-pl),
    apply **guṇa** to a hrasva IK-ending aṅga.

For hari:
  hari + jas
    (1.3.7 + 1.3.9) delete initial 'j' of jas → as
    7.3.109: i → e  → hare + as
    6.1.78: e + a → aya  → haraya + s
    tripāḍī: s → H  → हरयः

We implement minimal mapping:
  i → e
  u → o

Blindness:
  - cond() keys off pratyaya.meta['upadesha_slp1'] == 'jas' (identity),
    not paradigm coordinates.
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
    if "anga" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "jas":
        return False
    if pr.meta.get("jasi_guna_done"):
        return False
    if not anga.varnas:
        return False
    if anga.varnas[-1].slp1 not in _GUNA_MAP:
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
    pr.meta["jasi_guna_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.109",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "hrasva-aNgasya jasi guRaH",
    text_dev       = "ह्रस्व-अङ्गस्य जसि गुणः",
    padaccheda_dev = "ह्रस्व-अङ्गस्य जसि गुणः",
    why_dev        = "जस्-प्रत्यये परे ह्रस्व-इक्-अन्त-अङ्गस्य गुणः (हरि → हरे)।",
    anuvritti_from = ("7.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

