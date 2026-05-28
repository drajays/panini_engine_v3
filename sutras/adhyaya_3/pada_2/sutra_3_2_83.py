"""
3.2.83  आत्ममाने खश्च  —  VIDHI

Padaccheda: आत्ममाने खः च

krt-suffix rule: आत्ममाने खश्च (83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_83_AtmamAne_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_83_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmamAne KaSca",
    text_dev              = "आत्ममाने खश्च",
    padaccheda_dev        = "आत्ममाने खः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [आत्ममाने खश्च] विहितः (३.२.83)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
