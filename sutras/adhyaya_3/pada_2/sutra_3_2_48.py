"""
3.2.48  अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः  —  VIDHI

Padaccheda: अन्त-अत्यन्त-अध्व-दूर-पार-सर्व-अनन्तेषु डः

krt-suffix rule: अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः (48)
Pāṭha: ashtadhyayi.com data.txt row i=32048 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_48_antAtyantA_48"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.48", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "antAtyantADvadUrapArasarvAnantezu qaH",
    text_dev              = "अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH anta-atyanta-aDvan-dUra-pAra-sarva-anantezu qaH kft karmaRi anupasarge supi gamaH ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः अन्त-अत्यन्त-अध्वन्-दूर-पार-सर्व-अनन्तेषु डः कृत् कर्मणि अनुपसर्गे सुपि गमः च",
    padaccheda_dev        = "अन्त-अत्यन्त-अध्व-दूर-पार-सर्व-अनन्तेषु डः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः] विहितः (३.२.48)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
