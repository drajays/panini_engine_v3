"""
3.2.88  बहुलं छन्दसि  —  VIDHI

Padaccheda: बहुलम् छन्दसि

krt-suffix rule: बहुलं छन्दसि (88)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_88_bahulaM_88"


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
    state.meta["krt_kind"] = "3.2.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahulaM Candasi",
    text_dev              = "बहुलं छन्दसि",
    padaccheda_dev        = "बहुलम् छन्दसि",
    why_dev               = "धातोः कृत्-प्रत्ययः [बहुलं छन्दसि] विहितः (३.२.88)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
