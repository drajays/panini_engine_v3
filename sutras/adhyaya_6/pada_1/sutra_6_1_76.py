"""
6.1.76  पदान्ताद्वा  —  VIDHI

Padaccheda: पदान्तात् वा

पदान्ताद्वा (6.1.76)
Pāṭha: ashtadhyayi.com data.txt row i=61076 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_76_padAntAdvA_76"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.76", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "padAntAdvA",
    text_dev              = "पदान्ताद्वा",
    samagra_slp1          = "dIrGAt padAntAt saMhitAyAm vA tugAgamaH",
    samagra_dev           = "दीर्घात् पदान्तात् संहितायाम् वा तुगागमः",
    padaccheda_dev        = "पदान्तात् वा",
    why_dev               = "(सूत्रम् 6.1.76) पदान्ताद्वा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
