"""
7.1.53  त्रेस्त्रयः  —  VIDHI

Padaccheda: त्रेः त्रयः

त्रेस्त्रयः (7.1.53)
Pāṭha: ashtadhyayi.com data.txt row i=71053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, is_stem
from phonology import mk

def _site(state: State):
    """त्रेस्त्रयः — the numeral त्रि (with tadantavidhi) before आम्: त्रय (त्रयाणाम्: 7.1.54 then gives nuṭ, 6.4.3 the dīrgha)."""
    hit = anga_and_sup(state, "7.1.53")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "tri", tadanta=True) or anga.meta.get("7_1_53_done") or "strīliṅga" in anga.tags:
        return None
    if (sup.meta.get("upadesha_slp1") or "").strip() != "Am":
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-3:] = [mk(x) for x in "traya"]       # tri → traya (the whole word; tadanta keeps what precedes)
    anga.meta["7_1_53_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.1.53",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "trestrayaH",
    text_dev              = "त्रेस्त्रयः",
    samagra_slp1          = "treH aNgasya Ami trayaH",
    samagra_dev           = "त्रेः अङ्गस्य आमि त्रयः",
    padaccheda_dev        = "त्रेः त्रयः",
    why_dev               = "(सूत्रम् 7.1.53) त्रेस्त्रयः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
