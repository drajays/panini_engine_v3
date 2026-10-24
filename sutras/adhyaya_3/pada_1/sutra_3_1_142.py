"""
3.1.142  दुन्योरनुपसर्गे  —  VIDHI

Padaccheda: दु-न्योः अन्-उपसर्गे

Krt suffix rule from dhatu: दुन्योरनुपसर्गे (142)
Pāṭha: ashtadhyayi.com data.txt row i=31142 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, dhatu_ends_tape
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

def cond(state: State) -> bool:
    """du, nī → ṇa in the agent sense, beside ṇvul-tṛc (dāvaḥ, nāyaḥ)"""
    st = "".join(v.slp1 for v in state.terms[-1].varnas) if state.terms else ""
    return vivaksita(state, "krt", "Rvultfc") and dhatu_ends_tape(state) and st in ("du", "nI", "RI")


def act(state: State) -> State:
    # beside ṇvul-tṛc (3.1.133): the reading takes this affix or declines and leaves the tape to them
    return attach_krt(state, "Ra") if policy_pick(state, "3.1.142", 2) == 0 else state


SUTRA = SutraRecord(
    sutra_id              = "3.1.142",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dunyoranupasarge",
    text_dev              = "दुन्योरनुपसर्गे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH dunyoH anupasarge Rvul-tfcO kft RaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः दुन्योः अनुपसर्गे ण्वुल्-तृचौ कृत् णः",
    padaccheda_dev        = "दु-न्योः अन्-उपसर्गे",
    why_dev               = "धातोः [दुन्योरनुपसर्गे]-प्रत्ययः विहितः (३.१.142)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
