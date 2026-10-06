"""
8.1.33  अङ्गाप्रातिलोम्ये  —  VIDHI

Padaccheda: अङ्ग अप्रातिलोम्ये

अङ्गाप्रातिलोम्ये (8.1.33)
Pāṭha: ashtadhyayi.com data.txt row i=81033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_33_aNgAprAtil_33"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.33", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aNgAprAtilomye",
    text_dev              = "अङ्गाप्रातिलोम्ये",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO aNga aprAtilomye tiN na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ अङ्ग अप्रातिलोम्ये तिङ् न",
    padaccheda_dev        = "अङ्ग अप्रातिलोम्ये",
    why_dev               = "(सूत्रम् 8.1.33) अङ्गाप्रातिलोम्ये।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
