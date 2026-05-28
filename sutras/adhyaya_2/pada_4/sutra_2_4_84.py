"""
2.4.84  तृतीयासप्तम्योर्बहुलम्  —  VIDHI

Padaccheda: तृतीया-सप्तम्योः बहुलम्

Bahulam (varied) for tritiya and saptami.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_84_tritiya_saptami_bahu"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_84_lup_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["lup_kind"]             = "2.4.84"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tftIyAsaptamyorbahulam",
    text_dev              = "तृतीयासप्तम्योर्बहुलम्",
    padaccheda_dev        = "तृतीया-सप्तम्योः बहुलम्",
    why_dev               = "तृतीया-सप्तम्योः बहुलम् (२.४.८४)।",
    anuvritti_from        = ('2.4.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
