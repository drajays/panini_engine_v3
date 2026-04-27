"""
2.1.1  समर्थः पदविधिः  —  PARIBHASHA

Padaccheda: समर्थः / पदविधिः

Śāstra (one line): rules that operate on padas (*padavidhi*) require semantic
compatibility (*samarthya*) among the items they relate.

Engine: the core engine is mechanically blind to semantics (CONSTITUTION Art. 2),
so this sūtra is represented as an interpretive gate in
``state.paribhasha_gates`` when a recipe chooses to record “samarthya assumed”
for a glass-box derivation narrative.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2.1.1_samartha_padavidhi"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.1.1",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "samarthaH padavidhiH",
    text_dev       = "समर्थः पदविधिः",
    padaccheda_dev = "समर्थः / पदविधिः",
    why_dev        = (
        "पदविधि-प्रसङ्गे सामर्थ्य-अपेक्षा — इह यन्त्रे अर्थ-अन्धत्वात् "
        "केवलं परिभाषा-गेट-रूपेण निबद्धम् (ग्लास-बॉक्स्-आडिट्)।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

