"""
6.4.25  दंशसञ्जस्वञ्जां शपि  —  VIDHI

Padaccheda: दंश-सञ्ज-स्वञ्जाम् शपि

दन्शसञ्जस्वञ्जां शपि (6.4.25)
Pāṭha: ashtadhyayi.com data.txt row i=64025 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_25_danSasaYja_25"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.25", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'daMSasaYjasvaYjAM Sapi',
    text_dev              = 'दंशसञ्जस्वञ्जां शपि',
    samagra_slp1          = "daMSa-saYja-svaYjAmaNgasya upaDAyAH Sapi nalopaH",
    samagra_dev           = "दंश-सञ्ज-स्वञ्जामङ्गस्य उपधायाः शपि नलोपः",
    padaccheda_dev        = "दंश-सञ्ज-स्वञ्जाम् शपि",
    why_dev               = "(सूत्रम् 6.4.25) दन्शसञ्जस्वञ्जां शपि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
