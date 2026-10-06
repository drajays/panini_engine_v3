"""
8.1.66  यद्वृत्तान्नित्यम्  —  VIDHI

Padaccheda: यद्वृतात् नित्यम्

यद्वृत्तान्नित्यं (8.1.66)
Pāṭha: ashtadhyayi.com data.txt row i=81066 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_66_yadvfttAnn_66"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.66", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'yadvfttAnnityam',
    text_dev              = 'यद्वृत्तान्नित्यम्',
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO yadvftAt nityam tiN na kziyAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ यद्वृतात् नित्यम् तिङ् न क्षियायाम्",
    padaccheda_dev        = "यद्वृतात् नित्यम्",
    why_dev               = "(सूत्रम् 8.1.66) यद्वृत्तान्नित्यं।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
