"""
3.3.25  वौ क्षुश्रुवः  —  VIDHI

Padaccheda: वौ क्षु-श्रुवः

krt-suffix rule: वौ क्षुश्रुवः
Pāṭha: ashtadhyayi.com data.txt row i=33025 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_25_vO_25"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.25", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vO kzuSruvaH",
    text_dev              = "वौ क्षुश्रुवः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm vO kzu-SruvaH kft GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् वौ क्षु-श्रुवः कृत् घञ्",
    padaccheda_dev        = "वौ क्षु-श्रुवः",
    why_dev               = "धातोः प्रत्ययः (३.3.25)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
