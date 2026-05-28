"""
2.3.61  प्रेष्यब्रुवोर्हविषो देवतासम्प्रदाने  —  VIDHI

Padaccheda: प्रेष्य-ब्रुवोः हविषः देवता-सम्प्रदाने

presya and bruv take caturthy for havish-devata.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_61_presya_bruvo"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prezyabruvorhavizo devatAsampradAne",
    text_dev              = "प्रेष्यब्रुवोर्हविषो देवतासम्प्रदाने",
    padaccheda_dev        = "प्रेष्य-ब्रुवोः हविषः देवता-सम्प्रदाने",
    why_dev               = "प्रेष्य-ब्रुवोः हविषः देवता-सम्प्रदाने (२.३.६१)।",
    anuvritti_from        = ('2.3.13',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
