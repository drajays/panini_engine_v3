"""
4.2.30  सोमाट्ट्यण्  —  VIDHI

Padaccheda: सोमात् ट्यण्

सोमाट्ट्यण् (4.2.30)
Pāṭha: ashtadhyayi.com data.txt row i=42030 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "devatA"), stems=frozenset({"soma"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "wyaR")


SUTRA = SutraRecord(
    sutra_id              = "4.2.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "somAwwyaR",
    text_dev              = "सोमाट्ट्यण्",
    samagra_slp1          = "sA asya devatA iti somAt wyaR",
    samagra_dev           = "'सा अस्य देवता' (इति) सोमात् ट्यण्",
    padaccheda_dev        = "सोमात् ट्यण्",
    why_dev               = "(सूत्रम् 4.2.30) सोमाट्ट्यण्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.2.24',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
