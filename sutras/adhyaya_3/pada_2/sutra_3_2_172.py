"""
3.2.172  स्वपितृषोर्नजिङ्  —  VIDHI

Padaccheda: स्वपि-तृषोः नजिङ्

krt-suffix rule: स्वपितृषोर्नजिङ् (172)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_172_svapitfzor_172"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_172_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.172"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.172",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svapitfzornajiN",
    text_dev              = "स्वपितृषोर्नजिङ्",
    padaccheda_dev        = "स्वपि-तृषोः नजिङ्",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्वपितृषोर्नजिङ्] विहितः (३.२.172)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
