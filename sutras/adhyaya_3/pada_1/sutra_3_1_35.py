"""
3.1.35  कास्प्रत्ययादाममन्त्रे लिटि  —  VIDHI

Padaccheda: कास्-प्रत्ययात् आम् अमन्त्रे लिटि

Krt suffix rule from dhatu: कास्प्रत्ययादाममन्त्रे लिटि (35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_35_kAspratyayAd_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_35_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAspratyayAdAmamantre liwi",
    text_dev              = "कास्प्रत्ययादाममन्त्रे लिटि",
    padaccheda_dev        = "कास्-प्रत्ययात् आम् अमन्त्रे लिटि",
    why_dev               = "धातोः [कास्प्रत्ययादाममन्त्रे लिटि]-प्रत्ययः विहितः (३.१.35)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
