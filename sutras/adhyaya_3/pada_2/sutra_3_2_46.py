"""
3.2.46  संज्ञायां भृतॄवृजिधारिसहितपिदमः  —  VIDHI

Padaccheda: संज्ञायाम् भृ-तॄ-वृ-जि-धारि-सहि-तपि-दमः

krt-suffix rule: संज्ञायां भृतॄवृजिधारिसहितपिदमः (46)
Pāṭha: ashtadhyayi.com data.txt row i=32046 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_46_saMjYAyAM_46"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.46", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM BftFvfjiDArisahitapidamaH",
    text_dev              = "संज्ञायां भृतॄवृजिधारिसहितपिदमः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH saMjYAyAm Bf-tF-vfji-DAri-sahi-tapi-damaH kft karmaRi anupasarge supi Kac",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः संज्ञायाम् भृ-तॄ-वृजि-धारि-सहि-तपि-दमः कृत् कर्मणि अनुपसर्गे सुपि खच्",
    padaccheda_dev        = "संज्ञायाम् भृ-तॄ-वृ-जि-धारि-सहि-तपि-दमः",
    why_dev               = "धातोः कृत्-प्रत्ययः [संज्ञायां भृतॄवृजिधारिसहितपिदमः] विहितः (३.२.46)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
