"""
6.3.12  अमूर्धमस्तकात् स्वाङ्गादकामे  —  VIDHI

Padaccheda: अ-मूर्ध-मस्तकात् स्वाङ्गात् अकामे

अमूर्धमस्तकात् स्वाङ्गादकामे (6.3.12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_12_amUrDamast_12"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "amUrDamastakAt svANgAdakAme",
    text_dev              = "अमूर्धमस्तकात् स्वाङ्गादकामे",
    padaccheda_dev        = "अ-मूर्ध-मस्तकात् स्वाङ्गात् अकामे",
    why_dev               = "(सूत्रम् 6.3.12) अमूर्धमस्तकात् स्वाङ्गादकामे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
