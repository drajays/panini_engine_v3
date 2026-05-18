"""
3.2.75  अन्येभ्योऽपि दृश्यन्ते  —  VIDHI

Padaccheda: अन्येभ्यः अपि दृश्यन्ते (क्रियापदम्)

krt-suffix rule: अन्येभ्योऽपि दृश्यन्ते (75)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_75_anyeByopi_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_75_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anyeByo'pi dfSyante",
    text_dev              = "अन्येभ्योऽपि दृश्यन्ते",
    padaccheda_dev        = "अन्येभ्यः अपि दृश्यन्ते (क्रियापदम्)",
    why_dev               = "धातोः कृत्-प्रत्ययः [अन्येभ्योऽपि दृश्यन्ते] विहितः (३.२.75)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
