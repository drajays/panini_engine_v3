"""
3.2.47  गमश्च  —  VIDHI

Padaccheda: गमः च

krt-suffix rule: गमश्च (47)
Pāṭha: ashtadhyayi.com data.txt row i=32047 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_47_gamaSca_47"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.47", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gamaSca",
    text_dev              = "गमश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH gamaH ca kft karmaRi anupasarge supi Kac saMjYAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः गमः च कृत् कर्मणि अनुपसर्गे सुपि खच् संज्ञायाम्",
    padaccheda_dev        = "गमः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [गमश्च] विहितः (३.२.47)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
