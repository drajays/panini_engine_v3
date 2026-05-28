"""
3.2.130  इङ्धार्योः शत्रकृच्छ्रिणि  —  VIDHI

Padaccheda: इङ्-धार्य्योः (पञ्चम्यर्थे षष्ठी) शतृँ (लुप्तप्रथमान्तनिर्देशः) अकृच्छ्रिणि

krt-suffix rule: इङ्धार्योः शत्रकृच्छ्रिणि (130)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_130_iNDAryoH_130"


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
    state.meta["krt_kind"] = "3.2.130"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iNDAryoH SatrakfcCriRi",
    text_dev              = "इङ्धार्योः शत्रकृच्छ्रिणि",
    padaccheda_dev        = "इङ्-धार्य्योः (पञ्चम्यर्थे षष्ठी) शतृँ (लुप्तप्रथमान्तनिर्देशः) अकृच्छ्रिणि",
    why_dev               = "धातोः कृत्-प्रत्ययः [इङ्धार्योः शत्रकृच्छ्रिणि] विहितः (३.२.130)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
