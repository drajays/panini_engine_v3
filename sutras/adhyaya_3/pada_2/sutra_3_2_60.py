"""
3.2.60  त्यदादिषु दृशोऽनालोचने कञ् च  —  VIDHI

Padaccheda: त्यद्-आदिषु दृशः अनालोचने कञ् च

krt-suffix rule: त्यदादिषु दृशोऽनालोचने कञ् च (60)
Pāṭha: ashtadhyayi.com data.txt row i=32060 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_60_tyadAdizu_60"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.60", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'tyadAdizu dfSonAlocane kaY ca',
    text_dev              = 'त्यदादिषु दृशोऽनालोचने कञ् च',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH tyadAdizu dfSaH anAlocane kaY ca kft anupasarge supi kvin",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः त्यदादिषु दृशः अनालोचने कञ् च कृत् अनुपसर्गे सुपि क्विन्",
    padaccheda_dev        = "त्यद्-आदिषु दृशः अनालोचने कञ् च",
    why_dev               = "धातोः कृत्-प्रत्ययः [त्यदादिषु दृशोऽनालोचने कञ् च] विहितः (३.२.60)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
