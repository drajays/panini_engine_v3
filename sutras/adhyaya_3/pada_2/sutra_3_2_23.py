"""
3.2.23  न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु  —  VIDHI

Padaccheda: न शब्द-श्लोक-कलह-गाथा-वैर-चाटु-सूत्र-मन्त्र-पदेषु

krt-suffix rule: न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु (23)
Pāṭha: ashtadhyayi.com data.txt row i=32023 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_23_na_23"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.23", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.23",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na SabdaSlokakalahagATAvEracAwusUtramantrapadezu",
    text_dev              = "न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH na Sabda-Sloka-kalaha-gATA-vEra-cAwu-sUtra-mantra-padezu kft karmaRi anupasarge supi waH kfYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः न शब्द-श्लोक-कलह-गाथा-वैर-चाटु-सूत्र-मन्त्र-पदेषु कृत् कर्मणि अनुपसर्गे सुपि टः कृञः",
    padaccheda_dev        = "न शब्द-श्लोक-कलह-गाथा-वैर-चाटु-सूत्र-मन्त्र-पदेषु",
    why_dev               = "धातोः कृत्-प्रत्ययः [न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु] विहितः (३.२.23)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
