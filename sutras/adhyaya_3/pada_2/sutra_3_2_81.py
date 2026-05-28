"""
3.2.81  बहुलमाभीक्ष्ण्ये  —  VIDHI

Padaccheda: बहुलम् आभीक्ष्ण्ये

krt-suffix rule: बहुलमाभीक्ष्ण्ये (81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_81_bahulamABI_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_81_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahulamABIkzRye",
    text_dev              = "बहुलमाभीक्ष्ण्ये",
    padaccheda_dev        = "बहुलम् आभीक्ष्ण्ये",
    why_dev               = "धातोः कृत्-प्रत्ययः [बहुलमाभीक्ष्ण्ये] विहितः (३.२.81)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
