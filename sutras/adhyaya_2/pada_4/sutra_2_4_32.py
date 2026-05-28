"""
2.4.32  इदमोऽन्वादेशेऽशनुदात्तस्तृतीयाऽऽदौ  —  VIDHI

Padaccheda: इदमः अन्वादेशे अश् अनुदात्तः तृतीया-आदौ

In anvaadesa, ash-form of idam is unaccented in tritiya etc.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_32_idamas_anvadesa"


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
    state.meta["samasa_kind"]             = "2.4.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "idamo'nvAdeSe'SanudAttastftIyA''dO",
    text_dev              = "इदमोऽन्वादेशेऽशनुदात्तस्तृतीयाऽऽदौ",
    padaccheda_dev        = "इदमः अन्वादेशे अश् अनुदात्तः तृतीया-आदौ",
    why_dev               = "अन्वादेशे अश् अनुदात्तः तृतीया-आदौ (२.४.३२)।",
    anuvritti_from        = ('2.4.31',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
