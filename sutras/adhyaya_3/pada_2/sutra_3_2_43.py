"""
3.2.43  मेघर्तिभयेषु कृञः  —  VIDHI

Padaccheda: मेघ-ऋति-भयेषु कृञः

krt-suffix rule: मेघर्तिभयेषु कृञः (43)
Pāṭha: ashtadhyayi.com data.txt row i=32043 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_43_meGartiBay_43"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.43", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "meGartiBayezu kfYaH",
    text_dev              = "मेघर्तिभयेषु कृञः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH meGa-fti-Bayezu kfYaH kft karmaRi anupasarge supi Kac",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः मेघ-ऋति-भयेषु कृञः कृत् कर्मणि अनुपसर्गे सुपि खच्",
    padaccheda_dev        = "मेघ-ऋति-भयेषु कृञः",
    why_dev               = "धातोः कृत्-प्रत्ययः [मेघर्तिभयेषु कृञः] विहितः (३.२.43)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
