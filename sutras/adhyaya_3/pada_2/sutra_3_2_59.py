"""
3.2.59  ऋत्विग्दधृक्स्रग्दिगुष्णिगञ्चुयुजिक्रुञ्चां च  —  VIDHI

Padaccheda: ऋत्विक्-दधृक्-स्रक्-दिक्-उष्णिक्-अञ्चु-युजि-क्रुञ्चाम् च

krt-suffix rule: ऋत्विग्दधृक्स्रग्दिगुष्णिगञ्चुयुजिक्रुञ्चां च (59)
Pāṭha: ashtadhyayi.com data.txt row i=32059 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_59_ftvigdaDfk_59"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.59", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ftvigdaDfksragdiguzRigaYcuyujikruYcAM ca",
    text_dev              = "ऋत्विग्दधृक्स्रग्दिगुष्णिगञ्चुयुजिक्रुञ्चां च",
    samagra_slp1          = "ftvig-daDfk-srag-dig-uzRig-aYcu-yuji-kruYcAm kvin pratyayaH paraH AdyudAttaH",
    samagra_dev           = "ऋत्विग्-दधृक्-स्रग्-दिग्-उष्णिग्-अञ्चु-युजि-क्रुञ्चाम् क्विन् प्रत्ययः परः आद्युदात्तः",
    padaccheda_dev        = "ऋत्विक्-दधृक्-स्रक्-दिक्-उष्णिक्-अञ्चु-युजि-क्रुञ्चाम् च",
    why_dev               = "धातोः कृत्-प्रत्ययः [ऋत्विग्दधृक्स्रग्दिगुष्णिगञ्चुयुजिक्रुञ्चां च] विहितः (३.२.59)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
