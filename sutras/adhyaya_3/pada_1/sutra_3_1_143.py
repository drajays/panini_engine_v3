"""
3.1.143  विभाषा ग्रहः  —  VIDHI

Padaccheda: विभाषा ग्रहः

Krt suffix rule from dhatu: विभाषा ग्रहेः (143)
Pāṭha: ashtadhyayi.com data.txt row i=31143 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, dhatu_ends_tape
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

def cond(state: State) -> bool:
    """grah → ṇa in the agent sense (grāhaḥ), beside ṇvul-tṛc"""
    st = "".join(v.slp1 for v in state.terms[-1].varnas) if state.terms else ""
    return vivaksita(state, "krt", "Rvultfc") and dhatu_ends_tape(state) and st == "grah"


def act(state: State) -> State:
    # beside ṇvul-tṛc (3.1.133): the reading takes this affix or declines and leaves the tape to them
    return attach_krt(state, "Ra") if policy_pick(state, "3.1.143", 2) == 0 else state


SUTRA = SutraRecord(
    sutra_id              = "3.1.143",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'viBAzA grahaH',
    text_dev              = 'विभाषा ग्रहः',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH viBAzA grahaH Rvul-tfcO kft RaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः विभाषा ग्रहः ण्वुल्-तृचौ कृत् णः",
    padaccheda_dev        = "विभाषा ग्रहः",
    why_dev               = "धातोः [विभाषा ग्रहेः]-प्रत्ययः विहितः (३.१.143)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
