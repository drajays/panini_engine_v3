"""
3.1.50  गुपेश्छन्दसि  —  VIDHI

Padaccheda: गुपेः छन्दसि

Krt suffix rule from dhatu: गुपेश्छन्दसि (50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_50_gupeSCandasi_50"


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
    state.meta["krt_kind"] = "3.1.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gupeSCandasi",
    text_dev              = "गुपेश्छन्दसि",
    padaccheda_dev        = "गुपेः छन्दसि",
    why_dev               = "धातोः [गुपेश्छन्दसि]-प्रत्ययः विहितः (३.१.50)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
