"""
4.2.37  तस्य समूहः  —  VIDHI

Padaccheda: तस्य समूहः

तस्य समूहः (4.2.37)
Pāṭha: ashtadhyayi.com data.txt row i=42037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "samUha"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.2.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasya samUhaH",
    text_dev              = "तस्य समूहः",
    samagra_slp1          = "tasya samUhaH iti samarTAnAM praTamAt paraH aR pratyayaH",
    samagra_dev           = "'तस्य समूहः' (इति) समर्थानां प्रथमात् परः अण्  प्रत्ययः",
    padaccheda_dev        = "तस्य समूहः",
    why_dev               = "(सूत्रम् 4.2.37) तस्य समूहः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
