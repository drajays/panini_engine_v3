"""
4.2.7  दृष्टं साम  —  VIDHI

Padaccheda: दृष्टम् साम

दृष्ट्अं साम (4.2.7)
Pāṭha: ashtadhyayi.com data.txt row i=42007 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "dfzwa"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.2.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'dfzwaM sAma',
    text_dev              = 'दृष्टं साम',
    samagra_slp1          = "tena dfzwaM sAma iti samarTAnAm praTamAt paraH aR pratyayaH",
    samagra_dev           = "'तेन दृष्टं साम' (इति) समर्थानाम् प्रथमात् परः अण् प्रत्ययः",
    padaccheda_dev        = "दृष्टम् साम",
    why_dev               = "(सूत्रम् 4.2.7) दृष्ट्अं साम।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
