"""
4.2.11  पाण्डुकम्बलादिनिः  —  VIDHI

Padaccheda: पाण्डु-कम्बलात् इनिः

पाण्डुकम्बलादिनिः (4.2.11)
Pāṭha: ashtadhyayi.com data.txt row i=42011 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "parivfta"), stems=frozenset({"pARqukambala"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "in")


SUTRA = SutraRecord(
    sutra_id              = "4.2.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pARqukambalAdiniH",
    text_dev              = "पाण्डुकम्बलादिनिः",
    samagra_slp1          = "parivfto raTaH iti pARqukambalAt iniH",
    samagra_dev           = "'परिवृतो रथः' (इति) पाण्डुकम्बलात् इनिः",
    padaccheda_dev        = "पाण्डु-कम्बलात् इनिः",
    why_dev               = "(सूत्रम् 4.2.11) पाण्डुकम्बलादिनिः।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.2.10',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
