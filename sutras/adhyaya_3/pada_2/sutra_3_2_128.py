"""
3.2.128  पूङ्यजोः शानन्  —  VIDHI

Padaccheda: पूङ्-यजोः (पञ्चम्यर्थे षष्ठी) शानन्

krt-suffix rule: पूङ्यजोः शानन् (128)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_128_pUNyajoH_128"


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
    state.meta["krt_kind"] = "3.2.128"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.128",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUNyajoH SAnan",
    text_dev              = "पूङ्यजोः शानन्",
    padaccheda_dev        = "पूङ्-यजोः (पञ्चम्यर्थे षष्ठी) शानन्",
    why_dev               = "धातोः कृत्-प्रत्ययः [पूङ्यजोः शानन्] विहितः (३.२.128)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
