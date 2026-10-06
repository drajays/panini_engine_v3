"""
6.1.148  वर्चस्केऽवस्करः  —  VIDHI

Padaccheda: वर्चस्के अवस्करः

वर्चस्केऽवस्करः (6.1.148)
Pāṭha: ashtadhyayi.com data.txt row i=61148 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_148_varcaskev_148"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.148", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.148"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.148",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'varcaskevaskaraH',
    text_dev              = 'वर्चस्केऽवस्करः',
    samagra_slp1          = "saMhitAyAm suwkAtpUrvaH varcaske avaskaraH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् सुट्कात्पूर्वः वर्चस्के अवस्करः",
    padaccheda_dev        = "वर्चस्के अवस्करः",
    why_dev               = "(सूत्रम् 6.1.148) वर्चस्केऽवस्करः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
