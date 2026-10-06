"""
6.4.9  वा षपूर्वस्य निगमे  —  VIDHI

Padaccheda: वा ष-पूर्वस्य निगमे

वा षपूर्वस्य निगमे (6.4.9)
Pāṭha: ashtadhyayi.com data.txt row i=64009 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_9_vA_9"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.9", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA zapUrvasya nigame",
    text_dev              = "वा षपूर्वस्य निगमे",
    samagra_slp1          = "nigame zapUrvasya naH aNgasya upaDAyAH asambudDO sarvanAmasTAne vA dIrGaH",
    samagra_dev           = "निगमे षपूर्वस्य नः अङ्गस्य उपधायाः असम्बुद्धौ सर्वनामस्थाने वा दीर्घः",
    padaccheda_dev        = "वा ष-पूर्वस्य निगमे",
    why_dev               = "(सूत्रम् 6.4.9) वा षपूर्वस्य निगमे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
