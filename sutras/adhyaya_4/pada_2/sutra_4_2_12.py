"""
4.2.12  द्वैपवैयाघ्रादञ्  —  VIDHI

Padaccheda: द्वैप-वैयाघ्रात् अञ्

द्वैपवैयाघ्रादञ् (4.2.12)
Pāṭha: ashtadhyayi.com data.txt row i=42012 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "parivfta"), stems=frozenset({"dvEpa","vEyAGra"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aY")


SUTRA = SutraRecord(
    sutra_id              = "4.2.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvEpavEyAGrAdaY",
    text_dev              = "द्वैपवैयाघ्रादञ्",
    samagra_slp1          = "tena parivfto raTaH iti dvEpa-vEyAGrAt aY",
    samagra_dev           = "'तेन परिवृतो रथः' (इति)  द्वैप-वैयाघ्रात् अञ्",
    padaccheda_dev        = "द्वैप-वैयाघ्रात् अञ्",
    why_dev               = "(सूत्रम् 4.2.12) द्वैपवैयाघ्रादञ्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.2.10',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
