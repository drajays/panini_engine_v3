"""
3.3.81  अपघनोऽङ्गम्  —  VIDHI

Padaccheda: अपघनः अङ्गम्

krt-suffix rule: अपघनोऽङ्गम्
Pāṭha: ashtadhyayi.com data.txt row i=33081 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_81_apaGanoNg_81"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.81", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'apaGanoNgam',
    text_dev              = 'अपघनोऽङ्गम्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm apaGanaH aNgam kft ap hanaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् अपघनः अङ्गम् कृत् अप् हनः",
    padaccheda_dev        = "अपघनः अङ्गम्",
    why_dev               = "धातोः प्रत्ययः (३.3.81)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
