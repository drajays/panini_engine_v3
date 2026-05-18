"""
2.4.1  द्विगुरेकवचनम्  (dvigur ekavacanam)  —  VIDHI

Padaccheda: द्विगुः / एकवचनम्

Śāstra: a dvigु compound (numeral-first compound) takes the singular number
(ekavacana).

Engine: sets a gate in paribhasha_gates recording that the dvigु ekavacana
rule has been noted; downstream steps use the samjna_registry entry
"2_4_1_dvigu_ekavacana" to apply singular inflection.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "2_4_1_dvigu_ekavacana"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.1",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = "dvigur ekavacanam",
    text_dev       = "द्विगुरेकवचनम्",
    padaccheda_dev = "द्विगुः / एकवचनम्",
    why_dev        = "द्विगु-समासः एकवचने भवति।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
