"""
3.3.124  जालमानायः  —  VIDHI

Padaccheda: जालम् आनायः

krt-suffix rule: जालमानायः
Pāṭha: ashtadhyayi.com data.txt row i=33124 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_124_jAlamAnAya_124"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.124", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAlamAnAyaH",
    text_dev              = "जालमानायः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH karaRADikaraRayoH jAlam AnAyaH kft karaRa-aDikaraRayoH ca puMsi GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः करणाधिकरणयोः जालम् आनायः कृत् करण-अधिकरणयोः च पुंसि घञ्",
    padaccheda_dev        = "जालम् आनायः",
    why_dev               = "धातोः प्रत्ययः (३.3.124)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
