"""
3.1.105  अजर्यं संगतम्  —  VIDHI

Padaccheda: अजर्यम् संगतम्

Krt suffix rule from dhatu: अजर्यं संगतम् (105)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_105_ajaryaM_105"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_105_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ajaryaM saMgatam",
    text_dev              = "अजर्यं संगतम्",
    padaccheda_dev        = "अजर्यम् संगतम्",
    why_dev               = "धातोः [अजर्यं संगतम्]-प्रत्ययः विहितः (३.१.105)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
