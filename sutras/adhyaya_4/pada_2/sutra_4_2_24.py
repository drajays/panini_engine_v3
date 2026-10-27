"""
4.2.24  सास्य देवता  —  VIDHI

Padaccheda: सा अस्य देवता

साऽस्य देवता (4.2.24)
Pāṭha: ashtadhyayi.com data.txt row i=42024 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "devatA"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.2.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'sAsya devatA',
    text_dev              = 'सास्य देवता',
    samagra_slp1          = "sA asya devatA iti samarTAnAm praTamAt paraH aR pratyayaH",
    samagra_dev           = "'सा अस्य देवता' (इति) समर्थानाम् प्रथमात् परः अण्  प्रत्ययः",
    padaccheda_dev        = "सा अस्य देवता",
    why_dev               = "(सूत्रम् 4.2.24) साऽस्य देवता।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
