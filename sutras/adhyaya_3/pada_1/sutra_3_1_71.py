"""
3.1.71  यसोऽनुपसर्गात्  —  VIDHI

Padaccheda: यसः अनुपसर्गात्

Krt suffix rule from dhatu: यसोऽनुपसर्गात् (71)
Pāṭha: ashtadhyayi.com data.txt row i=31071 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_71_yasonupasar_71"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.71", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'yasonupasargAt',
    text_dev              = 'यसोऽनुपसर्गात्',
    samagra_slp1          = "karttari sArvaDAtuke anupasargAt yasaH DAtoH paraH Syan vA",
    samagra_dev           = "कर्त्तरि सार्वधातुके अनुपसर्गात् यसः धातोः परः श्यन् वा",
    padaccheda_dev        = "यसः अनुपसर्गात्",
    why_dev               = "धातोः [यसोऽनुपसर्गात्]-प्रत्ययः विहितः (३.१.71)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
