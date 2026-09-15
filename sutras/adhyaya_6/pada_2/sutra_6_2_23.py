"""
6.2.23  सविधसनीडसमर्यादसवेशसदेशेषु सामीप्ये  —  VIDHI

Padaccheda: सविध-सनीड-समर्याद-सवेश-सदेशेषु सामीप्ये

सविधसनीडसमर्यादसवेशसदेशेषु सामीप्ये (6.2.23)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_23_saviDasanI_23"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.23", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saviDasanIqasamaryAdasaveSasadeSezu sAmIpye",
    text_dev              = "सविधसनीडसमर्यादसवेशसदेशेषु सामीप्ये",
    padaccheda_dev        = "सविध-सनीड-समर्याद-सवेश-सदेशेषु सामीप्ये",
    why_dev               = "(सूत्रम् 6.2.23) सविधसनीडसमर्यादसवेशसदेशेषु सामीप्ये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
