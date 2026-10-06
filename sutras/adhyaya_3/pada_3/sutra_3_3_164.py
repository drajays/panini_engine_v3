"""
3.3.164  लिङ् चोर्ध्वमौहूर्तिके  —  VIDHI

Padaccheda: लिङ् च ऊर्ध्वमौहूर्तिके

krt-suffix rule: लिङ् चोर्ध्वमौहूर्तिके
Pāṭha: ashtadhyayi.com data.txt row i=33164 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_164_liN_164"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.164", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.164"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.164",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "liN corDvamOhUrtike",
    text_dev              = "लिङ् चोर्ध्वमौहूर्तिके",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH liN ca UrDvamOhUrtike kft prEza-atisarga-prAptakAlezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः लिङ् च ऊर्ध्वमौहूर्तिके कृत् प्रैष-अतिसर्ग-प्राप्तकालेषु",
    padaccheda_dev        = "लिङ् च ऊर्ध्वमौहूर्तिके",
    why_dev               = "धातोः प्रत्ययः (३.3.164)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
