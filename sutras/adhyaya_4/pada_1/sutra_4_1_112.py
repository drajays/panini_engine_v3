"""
4.1.112  शिवादिभ्योऽण्  —  VIDHI

Padaccheda: शिव-आदिभ्यः अण्

शिवादिभ्योऽण् (4.1.112)
Pāṭha: ashtadhyayi.com data.txt row i=41112 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401


def _site(state: State):
    return taddhita_site(state, gana_name="SivAdiH")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aR")


SUTRA = SutraRecord(
    sutra_id              = "4.1.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'SivAdiByoR',
    text_dev              = 'शिवादिभ्योऽण्',
    samagra_slp1          = "tasya apatyam iti SivAdiByaH aR",
    samagra_dev           = "'तस्य अपत्यम्' (इति)  शिवादिभ्यः अण्",
    padaccheda_dev        = "शिव-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 4.1.112) शिवादिभ्योऽण्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83', '4.1.95'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
