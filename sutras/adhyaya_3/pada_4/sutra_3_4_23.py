"""
3.4.23  न यद्यनाकाङ्क्षे  —  VIDHI

Padaccheda: न यदि अनाकाङ्क्षे

krt-suffix rule: न यद्यनाकाङ्क्षे
Pāṭha: ashtadhyayi.com data.txt row i=34023 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_23_na_23"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.23", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.23",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na yadyanAkANkze",
    text_dev              = "न यद्यनाकाङ्क्षे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH na yadi anAkANkze kft ktvA pUrvakAle samAnakarttfkayoH ABIkzRye Ramul ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः न यदि अनाकाङ्क्षे कृत् क्त्वा पूर्वकाले समानकर्त्तृकयोः आभीक्ष्ण्ये णमुल् च",
    padaccheda_dev        = "न यदि अनाकाङ्क्षे",
    why_dev               = "धातोः प्रत्ययः (३.4.23)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
