"""
3.3.132  आशंसायां भूतवच्च  —  VIDHI

Padaccheda: आशंसायाम् भूत-वत् च

krt-suffix rule: आशंसायां भूतवच्च
Pāṭha: ashtadhyayi.com data.txt row i=33132 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_132_ASaMsAyAM_132"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.132", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.132"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.132",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASaMsAyAM BUtavacca",
    text_dev              = "आशंसायां भूतवच्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH ASaMsAyAm BUtavat ca kft vartamAnavat vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः आशंसायाम् भूतवत् च कृत् वर्तमानवत् वा",
    padaccheda_dev        = "आशंसायाम् भूत-वत् च",
    why_dev               = "धातोः प्रत्ययः (३.3.132)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
