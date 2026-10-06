"""
3.3.68  प्रमदसम्मदौ हर्षे  —  VIDHI

Padaccheda: प्रमदसम्मदौ हर्षे

krt-suffix rule: प्रमदसम्मदौ हर्षे
Pāṭha: ashtadhyayi.com data.txt row i=33068 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_68_pramadasam_68"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.68", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pramadasammadO harze",
    text_dev              = "प्रमदसम्मदौ हर्षे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm pramada-sammadO harze kft ap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् प्रमद-सम्मदौ हर्षे कृत् अप्",
    padaccheda_dev        = "प्रमदसम्मदौ हर्षे",
    why_dev               = "धातोः प्रत्ययः (३.3.68)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
