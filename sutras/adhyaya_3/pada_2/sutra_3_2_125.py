"""
3.2.125  सम्बोधने च  —  VIDHI

Padaccheda: सम्बोधने च

krt-suffix rule: सम्बोधने च (125)
Pāṭha: ashtadhyayi.com data.txt row i=32125 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_125_samboDane_125"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.125", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samboDane ca",
    text_dev              = "सम्बोधने च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne samboDane ca kft lawaH SatfSAnacO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने सम्बोधने च कृत् लटः शतृशानचौ",
    padaccheda_dev        = "सम्बोधने च",
    why_dev               = "धातोः कृत्-प्रत्ययः [सम्बोधने च] विहितः (३.२.125)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
