"""
3.1.88  तपस्तपःकर्मकस्यैव  —  VIDHI

Padaccheda: तपः तपः-कर्मकस्य एव

Krt suffix rule from dhatu: तपस्तपःकर्मकस्यैव (88)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_88_tapastapaHka_88"


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
    state.meta["krt_kind"] = "3.1.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tapastapaHkarmakasyEva",
    text_dev              = "तपस्तपःकर्मकस्यैव",
    padaccheda_dev        = "तपः तपः-कर्मकस्य एव",
    why_dev               = "धातोः [तपस्तपःकर्मकस्यैव]-प्रत्ययः विहितः (३.१.88)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
