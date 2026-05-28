"""
2.1.21  अन्यपदार्थे च संज्ञायाम्  (anyapadārthe ca saṃjñāyām)  —  SAMJNA

**Pāṭha:** In a proper noun (*saṃjñā*) context, a compound whose meaning
refers to some *other* referent beyond the literal sum of its parts
(*anyapadārtha*) receives the *avyayībhāva* designation.

This sūtra closes the avyayībhāva adhikāra opened at 2.1.5
(scope end = "2.1.21").

v3 narrow slice: gate-marks the saṃjñā avyayībhāva gate with key
``2_1_21_anyapadaartha_sanjna``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_21_anyapadaartha_sanjna"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.21",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = "anyapadArTe ca saMjYAyAm",
    text_dev              = "अन्यपदार्थे च संज्ञायाम्",
    padaccheda_dev        = "अन्यपदार्थे / च / संज्ञायाम्",
    why_dev               = "संज्ञायां यस्य अन्यपदार्थः तस्य अव्ययीभावसंज्ञा (२.१.२१)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
