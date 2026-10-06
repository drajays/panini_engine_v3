"""
3.2.171  आदृगमहनजनः किकिनौ लिट् च  —  VIDHI

Padaccheda: आ-दृ-गम-हन-जनः कि-किनौ लिट् च

krt-suffix rule: आदृगमहनजनः किकिनौ लिट् च (171)
Pāṭha: ashtadhyayi.com data.txt row i=32171 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_171_Adfgamahan_171"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.171", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.171"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.171",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AdfgamahanajanaH kikinO liw ca",
    text_dev              = "आदृगमहनजनः किकिनौ लिट् च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu Adf-gama-hana-janaH ki-kinO liw ca kft Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु आदृ-गम-हन-जनः कि-किनौ लिट् च कृत् छन्दसि",
    padaccheda_dev        = "आ-दृ-गम-हन-जनः कि-किनौ लिट् च",
    why_dev               = "धातोः कृत्-प्रत्ययः [आदृगमहनजनः किकिनौ लिट् च] विहितः (३.२.171)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
