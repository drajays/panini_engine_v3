"""
1.4.109  परः संनिकर्षः संहिता  —  SAMJNA

Padaccheda: परः १/१ सन्निकर्षः १/१ संहिता १/१

Extreme proximity (para-sannikarsah) of sounds is called samhita
(sandhi context). This is the foundational definition for sandhi rules.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_KEY: str = "1_4_109_samhita"


def cond(state: State) -> bool:
    return _KEY not in state.samjna_registry


def act(state: State) -> State:
    state.samjna_registry[_KEY]       = True
    state.samjna_registry["samhita"]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.4.109",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "paraH saMnikarzaH saMhitA",
    text_dev              = "परः संनिकर्षः संहिता",
    padaccheda_dev        = "परः १/१ सन्निकर्षः १/१ संहिता १/१",
    why_dev               = "परः सन्निकर्षः (अत्यन्त-सामीप्यम्) संहिता-संज्ञा (१.४.१०९)।",
    anuvritti_from        = (),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
