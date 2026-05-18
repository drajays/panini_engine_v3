"""
3.1.141  श्याऽऽद्व्यधास्रुसंस्र्वतीणवसाऽवहृलिहश्लिषश्वसश्च  —  VIDHI

Padaccheda: श्या-आत्-व्यध-आस्रु-संस्रु-अतीण्-अवसा-अवहृ-लिह-श्लिष-श्वसः च

Krt suffix rule from dhatu: श्याऽऽद्व्यधास्रुसंस्र्वतीणवसाऽवहृलिहश्लिषश्वसश्च (141)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_141_SyAdvyaDAs_141"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_141_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.141"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.141",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SyA''dvyaDAsrusaMsrvatIRavasA'vahflihaSlizaSvasaSca",
    text_dev              = "श्याऽऽद्व्यधास्रुसंस्र्वतीणवसाऽवहृलिहश्लिषश्वसश्च",
    padaccheda_dev        = "श्या-आत्-व्यध-आस्रु-संस्रु-अतीण्-अवसा-अवहृ-लिह-श्लिष-श्वसः च",
    why_dev               = "धातोः [श्याऽऽद्व्यधास्रुसंस्र्वतीणवसाऽवहृलिहश्लिषश्वसश्च]-प्रत्ययः विहितः (३.१.141)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
