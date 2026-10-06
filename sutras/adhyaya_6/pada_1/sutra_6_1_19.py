"""
6.1.19  स्वपिस्यमिव्येञां यङि  —  VIDHI

Padaccheda: स्वपि-स्यमि-व्येञाम् यङि

स्वपिस्यमिव्येञां यङि (6.1.19)
Pāṭha: ashtadhyayi.com data.txt row i=61019 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_19_svapisyami_19"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.19", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svapisyamivyeYAM yaNi",
    text_dev              = "स्वपिस्यमिव्येञां यङि",
    samagra_slp1          = "svapi-syami-vyeYAm yaNi samprasAraRam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "स्वपि-स्यमि-व्येञाम् यङि सम्प्रसारणम्",
    padaccheda_dev        = "स्वपि-स्यमि-व्येञाम् यङि",
    why_dev               = "(सूत्रम् 6.1.19) स्वपिस्यमिव्येञां यङि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
