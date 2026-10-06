"""
3.1.121  युग्यं च पत्रे  —  VIDHI

Padaccheda: युग्यम् च पत्रे

Krt suffix rule from dhatu: युग्यं च पत्त्रे (121)
Pāṭha: ashtadhyayi.com data.txt row i=31121 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_121_yugyaM_121"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.121", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'yugyaM ca patre',
    text_dev              = 'युग्यं च पत्रे',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH yugyam ca patre kft kyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः युग्यम् च पत्रे कृत् क्यप्",
    padaccheda_dev        = "युग्यम् च पत्रे",
    why_dev               = "धातोः [युग्यं च पत्त्रे]-प्रत्ययः विहितः (३.१.121)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
