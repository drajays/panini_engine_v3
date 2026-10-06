"""
8.1.68  सगतिरपि तिङ्  —  VIDHI

Padaccheda: स-गतिः अपि तिङ्

सगतिरपि तिङ् (8.1.68)
Pāṭha: ashtadhyayi.com data.txt row i=81068 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_68_sagatirapi_68"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.68", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sagatirapi tiN",
    text_dev              = "सगतिरपि तिङ्",
    samagra_slp1          = "padasya padAt anudAttaM sarvamApAdAdO sagatiH api tiN kziyAyAm pUjanAt pUjitam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पदात् अनुदात्तं सर्वमापादादौ सगतिः अपि तिङ् क्षियायाम् पूजनात् पूजितम्",
    padaccheda_dev        = "स-गतिः अपि तिङ्",
    why_dev               = "(सूत्रम् 8.1.68) सगतिरपि तिङ्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
