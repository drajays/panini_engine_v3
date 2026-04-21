"""
6.4.3  नामि  —  VIDHI

Operational intent for v3.4 (hari-like i-stems, genitive plural):
  After 7.1.54 inserts nuṭ (n-) before sup upadeśa **Am** (6-3),
  lengthen the aṅga-final vowel before that n-.

This yields:
  hari + (n + Am)  →  harī + nAm  →  (8.4.2) harīṇām

We implement the minimal transformation needed for i/u stems:
  i → I, u → U

Blindness:
  - cond() checks only adjacent term boundary + inserted nuṭ tag.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk


_DIRGHA_MAP = {"i": "I", "u": "U"}


def _matches(state: State) -> bool:
    if not adhikara_in_effect("6.4.3", state, "6.4.1"):
        return False
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "Am":
        return False
    if pr.meta.get("nami_dirgha_done"):
        return False
    if not anga.varnas or not pr.varnas:
        return False
    if anga.varnas[-1].slp1 not in _DIRGHA_MAP:
        return False
    # Require nuṭ insertion evidence: first varṇa tagged by 7.1.54.
    if "nut_agama_inserted" not in pr.varnas[0].tags:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    pr   = state.terms[-1]
    anga.varnas[-1] = mk(_DIRGHA_MAP[anga.varnas[-1].slp1])
    pr.meta["nami_dirgha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.3",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "nAmi (aNgasya)",
    text_dev       = "नामि (अङ्गस्य)",
    padaccheda_dev = "नामि — अङ्गस्य",
    why_dev        = "नुट्-आगमेन नामि-पर्याये अङ्गस्य अन्त्य-स्वरस्य दीर्घः (हरि → हरी; हरिणाम् → हरीणाम्)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

