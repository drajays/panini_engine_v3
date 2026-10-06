"""
3.2.45  आशिते भुवः करणभावयोः  —  VIDHI

Padaccheda: आशिते भुवः करण-भावयोः

krt-suffix rule: आशिते भुवः करणभावयोः (45)
Pāṭha: ashtadhyayi.com data.txt row i=32045 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_45_ASite_45"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.45", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASite BuvaH karaRaBAvayoH",
    text_dev              = "आशिते भुवः करणभावयोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH ASite BuvaH karaRa-BAvayoH kft karmaRi anupasarge supi Kac",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः आशिते भुवः करण-भावयोः कृत् कर्मणि अनुपसर्गे सुपि खच्",
    padaccheda_dev        = "आशिते भुवः करण-भावयोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [आशिते भुवः करणभावयोः] विहितः (३.२.45)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
