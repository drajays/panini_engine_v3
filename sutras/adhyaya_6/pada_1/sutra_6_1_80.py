"""
6.1.80  धातोस्तन्निमित्तस्यैव  —  VIDHI

Padaccheda: धातोः तन्निमित्तस्य अन्त्यस्य एव

धातोस्तन्निमित्तस्यैव (6.1.80)
Pāṭha: ashtadhyayi.com data.txt row i=61080 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_80_DAtostanni_80"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.80", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DAtostannimittasyEva",
    text_dev              = "धातोस्तन्निमित्तस्यैव",
    samagra_slp1          = "DAtoH yi-pratyaye tannimitasyEva ecaH vAntaH saMhitAyAm",
    samagra_dev           = "धातोः यि-प्रत्यये तन्निमितस्यैव एचः वान्तः संहितायाम्",
    padaccheda_dev        = "धातोः तन्निमित्तस्य अन्त्यस्य एव",
    why_dev               = "(सूत्रम् 6.1.80) धातोस्तन्निमित्तस्यैव।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
