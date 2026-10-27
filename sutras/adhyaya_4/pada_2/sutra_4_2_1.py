"""
4.2.1  तेन रक्तं रागात्  —  VIDHI

Padaccheda: तेन रक्तम् रागात्

तेन रक्तं रागात् (4.2.1)
Pāṭha: ashtadhyayi.com data.txt row i=42001 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "rakta"), tag="rAga")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.2.1",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tena raktaM rAgAt",
    text_dev              = "तेन रक्तं रागात्",
    samagra_slp1          = "tena raktaM rAgAt iti samarTAnAm praTamAt paraH aR pratyayaH",
    samagra_dev           = "'तेन रक्तं रागात्' (इति) समर्थानाम् प्रथमात् परः अण् प्रत्ययः",
    padaccheda_dev        = "तेन रक्तम् रागात्",
    why_dev               = "(सूत्रम् 4.2.1) तेन रक्तं रागात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
