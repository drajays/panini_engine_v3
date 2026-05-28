"""
3.1.110  ऋदुपधाच्चाकॢपिचृतेः  —  VIDHI

Padaccheda: ऋत्-उपधात् च अ-कॢपि-चृतेः

Krt suffix rule from dhatu: ऋदुपधाच्चाकॢपिचृतेः (110)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_110_fdupaDAccAkx_110"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_110_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fdupaDAccAkxpicfteH",
    text_dev              = "ऋदुपधाच्चाकॢपिचृतेः",
    padaccheda_dev        = "ऋत्-उपधात् च अ-कॢपि-चृतेः",
    why_dev               = "धातोः [ऋदुपधाच्चाकॢपिचृतेः]-प्रत्ययः विहितः (३.१.110)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
