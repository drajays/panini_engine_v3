"""
6.1.36  अपस्पृधेथामानृचुरानृहुश्चिच्युषेतित्याजश्राताःश्रितमाशीराशीर्त्तः  —  VIDHI

Padaccheda: अपस्पृधेथाम् (तिङ्) आनृचुः (तिङ्) आनृहुः (तिङ्) चिच्युषे (तिङ्) तित्याज (तिङ्) श्राताः श्रितम् आशीर् आशीर्त्ताः

अपस्पृधेथामानृचुरानृहुश्चिच्युषेतित्याजश्राताःश्रितमाशीराशीर्त्तः (6.1.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_36_apaspfDeTA_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_36_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "apaspfDeTAmAnfcurAnfhuScicyuzetityAjaSrAtAHSritamASIrASIrttaH",
    text_dev              = "अपस्पृधेथामानृचुरानृहुश्चिच्युषेतित्याजश्राताःश्रितमाशीराशीर्त्तः",
    padaccheda_dev        = "अपस्पृधेथाम् (तिङ्) आनृचुः (तिङ्) आनृहुः (तिङ्) चिच्युषे (तिङ्) तित्याज (तिङ्) श्राताः श्रितम् आशीर् आशीर्त्ताः",
    why_dev               = "(सूत्रम् 6.1.36) अपस्पृधेथामानृचुरानृहुश्चिच्युषेतित्याजश्राताःश्रितमाशीराशीर्त्तः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
