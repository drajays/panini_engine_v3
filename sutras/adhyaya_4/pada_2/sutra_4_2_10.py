"""
4.2.10  परिवृतो रथः  —  VIDHI

Padaccheda: परिवृतः रथः

परिवृतो रथः (4.2.10)
Pāṭha: ashtadhyayi.com data.txt row i=42010 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "parivfta"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.2.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parivfto raTaH",
    text_dev              = "परिवृतो रथः",
    samagra_slp1          = "tena parivfto raTaH iti samarTAnAm praTamAt paraH aR pratyayaH",
    samagra_dev           = "'तेन परिवृतो रथः' (इति) समर्थानाम् प्रथमात् परः अण् प्रत्ययः",
    padaccheda_dev        = "परिवृतः रथः",
    why_dev               = "(सूत्रम् 4.2.10) परिवृतो रथः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
