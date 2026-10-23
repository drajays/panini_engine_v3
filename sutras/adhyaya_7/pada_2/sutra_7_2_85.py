"""
7.2.85  रायो हलि  —  VIDHI

Padaccheda: रायः हलि

रायो हलि (7.2.85)
Pāṭha: ashtadhyayi.com data.txt row i=72085 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup, is_stem
from engine.state import State
from phonology import mk
from phonology.pratyahara import HAL

def _site(state: State):
    """रायो हलि विभक्तौ आः — the word रै (rE, with tadantavidhi) before a hal-initial vibhakti: राभ्याम्, राभिः, रासु (not रायौ, रायः)."""
    hit = anga_and_sup(state, "7.2.85")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "rE", tadanta=True) or anga.varnas[-1].slp1 != "E" or not sup.varnas:
        return None
    return anga if sup.varnas[0].slp1 in HAL else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[-1] = mk("A")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.85",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "rAyo hali",
    text_dev              = "रायो हलि",
    samagra_slp1          = "rAyaH aNgasya hali viBaktO A",
    samagra_dev           = "रायः अङ्गस्य हलि विभक्तौ आ",
    padaccheda_dev        = "रायः हलि",
    why_dev               = "(सूत्रम् 7.2.85) रायो हलि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
