"""
3.3.51  अवे ग्रहो वर्षप्रतिबन्धे  —  VIDHI

Padaccheda: अवे ग्रहः वर्ष-प्रतिबन्धे

krt-suffix rule: अवे ग्रहो वर्षप्रतिबन्धे
Pāṭha: ashtadhyayi.com data.txt row i=33051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_51_ave_51"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.51", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ave graho varzapratibanDe",
    text_dev              = "अवे ग्रहो वर्षप्रतिबन्धे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm ave grahaH varzapratibanDe kft GaY viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् अवे ग्रहः वर्षप्रतिबन्धे कृत् घञ् विभाषा",
    padaccheda_dev        = "अवे ग्रहः वर्ष-प्रतिबन्धे",
    why_dev               = "धातोः प्रत्ययः (३.3.51)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
