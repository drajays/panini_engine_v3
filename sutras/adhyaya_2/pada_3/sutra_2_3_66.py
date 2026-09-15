"""
2.3.66  उभयप्राप्तौ कर्मणि  —  VIDHI

Padaccheda: उभय-प्राप्तौ कर्मणि

When both karaka can be obtained, karma takes over.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_66_ubhaya_prapti"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uBayaprAptO karmaRi",
    text_dev              = "उभयप्राप्तौ कर्मणि",
    padaccheda_dev        = "उभय-प्राप्तौ कर्मणि",
    why_dev               = "उभय-प्राप्तौ कर्मणि (२.३.६६)।",
    anuvritti_from        = ('2.3.65',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
