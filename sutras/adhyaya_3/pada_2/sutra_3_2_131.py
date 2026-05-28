"""
3.2.131  द्विषोऽमित्रे  —  VIDHI

Padaccheda: द्विषः अमित्रे

krt-suffix rule: द्विषोऽमित्रे (131)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_131_dvizomitr_131"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvizo'mitre",
    text_dev              = "द्विषोऽमित्रे",
    padaccheda_dev        = "द्विषः अमित्रे",
    why_dev               = "धातोः कृत्-प्रत्ययः [द्विषोऽमित्रे] विहितः (३.२.131)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
