"""
6.4.29  अवोदैधौद्मप्रश्रथहिमश्रथाः  —  VIDHI

Padaccheda: अवोद-एध-ओद्म-प्रश्रथ-हिमश्रथाः

अवोदैधौद्मप्रश्रथहिमश्रथाः (6.4.29)
Pāṭha: ashtadhyayi.com data.txt row i=64029 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_29_avodEDOdma_29"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.29", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avodEDOdmapraSraTahimaSraTAH",
    text_dev              = "अवोदैधौद्मप्रश्रथहिमश्रथाः",
    samagra_slp1          = "aNgasya asidDavadatrABAt avoda-eDa-odma-praSraTa-himaSraTAH nalopaH upaDAyAH GaYi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् अवोद-एध-ओद्म-प्रश्रथ-हिमश्रथाः नलोपः उपधायाः घञि",
    padaccheda_dev        = "अवोद-एध-ओद्म-प्रश्रथ-हिमश्रथाः",
    why_dev               = "(सूत्रम् 6.4.29) अवोदैधौद्मप्रश्रथहिमश्रथाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
