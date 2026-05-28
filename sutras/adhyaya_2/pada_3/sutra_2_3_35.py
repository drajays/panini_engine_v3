"""
2.3.35  दूरान्तिकार्थेभ्यो द्वितीया च  —  VIDHI

Padaccheda: दूर-अन्तिक-अर्थेभ्यः द्वितीया च

dura and antika words also take dvitiya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_35_dura_antika_dvitiya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_35_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dUrAntikArTeByo dvitIyA ca",
    text_dev              = "दूरान्तिकार्थेभ्यो द्वितीया च",
    padaccheda_dev        = "दूर-अन्तिक-अर्थेभ्यः द्वितीया च",
    why_dev               = "दूर-अन्तिक-अर्थेभ्यः द्वितीया च (२.३.३५)।",
    anuvritti_from        = ('2.3.2',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
