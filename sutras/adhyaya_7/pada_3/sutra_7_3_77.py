"""
7.3.77  इषुगमियमां छः  —  VIDHI

The final of इषुँ (tudādi), गम्, यम् becomes छ् before a śit; 6.1.73 then adds
tuk: इच्छति, गच्छति, यच्छति.
Pāṭha: ashtadhyayi.com data.txt row i=73077 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.nimitta_predicates import dhatu_before_sit
from engine.state import State
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _stem(t) -> str:
    return "".join(v.slp1 for v in t.varnas if "aT_agama_v" not in v.tags)       # the aṭ of laṅ stands in the same pada


def _hit(state: State):
    i = dhatu_before_sit(state)
    if i is None:
        return None
    t = state.terms[i]
    st = _stem(t)
    if st in ("gam", "yam") or (st in ("iz", "Ez", "Aiz") and (t.meta.get("upadesha_slp1") or "").startswith("izu")):
        return i
    return None


def cond(state: State) -> bool:
    return _hit(state) is not None


def act(state: State) -> State:
    t = state.terms[_hit(state)]
    t.varnas[-1] = mk("C")                  # अलोऽन्त्यस्य
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.77",
    sutra_type=SutraType.VIDHI,
    text_slp1="izugamiyamAM CaH",
    text_dev="इषुगमियमां छः",
    samagra_slp1="aNgasya izugamiyamAm CaH Siti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="अङ्गस्य इषुगमियमाम् छः शिति",
    padaccheda_dev="इषु-गमि-यमाम् छः",
    why_dev="इषु-गम्-यम्-धातूनाम् अन्त्यस्य छकारः शिति परे (इच्छति, गच्छति, यच्छति)।",
    anuvritti_from=("7.3.73",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
