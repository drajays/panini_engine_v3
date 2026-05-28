"""
3.1.118  प्रत्यपिभ्यां ग्रहेश्छन्दसि  —  VIDHI

Padaccheda: प्रति-अपिभ्याम् ग्रहेः छन्दसि

Krt suffix rule from dhatu: प्रत्यपिभ्यां ग्रहेश्छन्दसि (118)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_118_pratyapiByAM_118"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_118_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.118"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.118",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratyapiByAM graheSCandasi",
    text_dev              = "प्रत्यपिभ्यां ग्रहेश्छन्दसि",
    padaccheda_dev        = "प्रति-अपिभ्याम् ग्रहेः छन्दसि",
    why_dev               = "धातोः [प्रत्यपिभ्यां ग्रहेश्छन्दसि]-प्रत्ययः विहितः (३.१.118)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
