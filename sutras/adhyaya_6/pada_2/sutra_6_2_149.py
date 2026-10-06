"""
6.2.149  इत्थम्भूतेन कृतमिति च  —  VIDHI

Padaccheda: इत्थम्भूतेन कृतम् इति च

इत्थम्भूतेन कृतमिति च (6.2.149)
Pāṭha: ashtadhyayi.com data.txt row i=62149 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_149_itTamBUten_149"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.149", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.149"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.149",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "itTamBUtena kftamiti ca",
    text_dev              = "इत्थम्भूतेन कृतमिति च",
    samagra_slp1          = "uttarapadAdiH antaH itTamBUtena kftam iti ca ktaH kArakAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः इत्थम्भूतेन कृतम् इति च क्तः कारकात्",
    padaccheda_dev        = "इत्थम्भूतेन कृतम् इति च",
    why_dev               = "(सूत्रम् 6.2.149) इत्थम्भूतेन कृतमिति च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
