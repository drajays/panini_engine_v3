"""
2.4.33  एतदस्त्रतसोस्त्रतसौ चानुदात्तौ  —  VIDHI

Padaccheda: एतदः त्र-तसोः त्र-तसौ च अनुदात्तौ

For etad, tra and tasa are substituted, both unaccented.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_33_etadas_tra_tasa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(
        "dvandva_samasa" in t.tags or "samasa_member" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "etadastratasostratasO cAnudAttO",
    text_dev              = "एतदस्त्रतसोस्त्रतसौ चानुदात्तौ",
    padaccheda_dev        = "एतदः त्र-तसोः त्र-तसौ च अनुदात्तौ",
    why_dev               = "एतदः त्र-तसोः त्र-तसौ च अनुदात्तौ (२.४.३३)।",
    anuvritti_from        = ('2.4.32',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
