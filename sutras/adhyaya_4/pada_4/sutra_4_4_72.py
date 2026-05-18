"""
4.4.72  कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति  —  VIDHI

Padaccheda: कठिनान्त-प्रस्तार-संस्थानेषु व्यवहरति (क्रियापदम्)

कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति (4.4.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_72_kaWinAntap_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_72_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaWinAntaprastArasaMsTAnezu vyavaharati",
    text_dev              = "कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति",
    padaccheda_dev        = "कठिनान्त-प्रस्तार-संस्थानेषु व्यवहरति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.72) कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
