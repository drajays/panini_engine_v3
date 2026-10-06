"""
8.2.86  गुरोरनृतोऽनन्त्यस्याप्येकैकस्य प्राचाम्  —  VIDHI

Padaccheda: गुरोः अन्-ऋतः अन्-अन्त्यस्य अपि एकैकस्य प्राचाम्

गुरोरनृतोऽनन्त्यस्याप्येकैकस्य प्राचाम् (8.2.86)
Pāṭha: ashtadhyayi.com data.txt row i=82086 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_86_guroranfto_86"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.86", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'guroranftonantyasyApyekEkasya prAcAm',
    text_dev              = 'गुरोरनृतोऽनन्त्यस्याप्येकैकस्य प्राचाम्',
    samagra_slp1          = "dUrAt hute vAkyasya anftaH anantyasya api ekEkasya guroH prAcAm plutaH udAttaH",
    samagra_dev           = "दूरात् हुते वाक्यस्य अनृतः अनन्त्यस्य अपि एकैकस्य गुरोः प्राचाम् प्लुतः उदात्तः",
    padaccheda_dev        = "गुरोः अन्-ऋतः अन्-अन्त्यस्य अपि एकैकस्य प्राचाम्",
    why_dev               = "(सूत्रम् 8.2.86) गुरोरनृतोऽनन्त्यस्याप्येकैकस्य प्राचाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
