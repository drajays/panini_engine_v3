"""
3.1.61  दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम्  —  VIDHI

Padaccheda: दीप-जन-बुध-पूरि-तायि-प्यायिभ्यः अन्यतरस्याम्

Krt suffix rule from dhatu: दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम् (61)
Pāṭha: ashtadhyayi.com data.txt row i=31061 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_61_dIpajanabuDa_61"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.61", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'dIpajanabuDapUritAyipyAyiByonyatarasyAm',
    text_dev              = 'दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH dIpa-jana-buDa-pUri-tAyi-pyAyiByaH anyatarasyAm luNi cleH ciR te",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः दीप-जन-बुध-पूरि-तायि-प्यायिभ्यः अन्यतरस्याम् लुङि च्लेः चिण् ते",
    padaccheda_dev        = "दीप-जन-बुध-पूरि-तायि-प्यायिभ्यः अन्यतरस्याम्",
    why_dev               = "धातोः [दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम्]-प्रत्ययः विहितः (३.१.61)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
