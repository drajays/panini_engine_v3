"""
3.2.74  आतो मनिन्क्वनिप्वनिपश्च  —  VIDHI

Padaccheda: आतः मनिन्-क्वनिप्-वनिपः च

krt-suffix rule: आतो मनिन्क्वनिप्वनिपश्च (74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_74_Ato_74"


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
    state.meta["krt_kind"] = "3.2.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ato maninkvanipvanipaSca",
    text_dev              = "आतो मनिन्क्वनिप्वनिपश्च",
    padaccheda_dev        = "आतः मनिन्-क्वनिप्-वनिपः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [आतो मनिन्क्वनिप्वनिपश्च] विहितः (३.२.74)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
