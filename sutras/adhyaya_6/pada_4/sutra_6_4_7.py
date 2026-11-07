"""
6.4.7  नोपधायाः  —  VIDHI

Padaccheda: न (लुप्तषष्ठ्यन्तनिर्देशः) उपधायाः

नोपधायाः (6.4.7)
Pāṭha: ashtadhyayi.com data.txt row i=64007 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup
from engine.state import State
from phonology    import mk

_DIRGHA_MAP = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}


def _site(state: State):
    """नोपधायाः — an aṅga ending in n: its upadhā (the vowel before the n) is lengthened before the nām (nuṭ + Ām): पञ्चानाम्, सप्तानाम्. (The
    final vowel of a vowel-ending aṅga is 6.4.3's.)"""
    hit = anga_and_sup(state, "6.4.7")
    if hit is None:
        return None
    anga, sup = hit
    vs = anga.varnas
    if (anga.meta.get("6_4_7_done") or not sup.varnas or "nut_agama_inserted" not in sup.varnas[0].tags
            or len(vs) < 2 or vs[-1].slp1 != "n" or vs[-2].slp1 not in _DIRGHA_MAP):
        return None
    return anga


# SHORTCUT S136: see docs/SHORTCUT_LEDGER.md
def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-2] = mk(_DIRGHA_MAP[anga.varnas[-2].slp1])
    anga.meta["6_4_7_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.7",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "nopaDAyAH",
    text_dev              = "नोपधायाः",
    samagra_slp1          = "naH aNgasya upaDAyAH nAmi dIrGaH",
    samagra_dev           = "नः अङ्गस्य उपधायाः नामि दीर्घः",
    padaccheda_dev        = "नः (नकारः, लुप्तषष्ठ्यन्तनिर्देशः) उपधायाः",
    why_dev               = "नोपधायाः — नान्तस्याङ्गस्य उपधायाः दीर्घः नामि परे (पञ्चानाम्)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
