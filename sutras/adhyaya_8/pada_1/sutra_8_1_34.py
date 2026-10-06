"""
8.1.34  हि च  —  VIDHI

Padaccheda: हि च

हि च (8.1.34)
Pāṭha: ashtadhyayi.com data.txt row i=81034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_34_hi_34"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.34", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hi ca",
    text_dev              = "हि च",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO hi ca tiN na aNga aprAtilomye",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ हि च तिङ् न अङ्ग अप्रातिलोम्ये",
    padaccheda_dev        = "हि च",
    why_dev               = "(सूत्रम् 8.1.34) हि च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
