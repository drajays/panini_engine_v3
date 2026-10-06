"""
6.4.18  क्रमश्च क्त्वि  —  VIDHI

Padaccheda: क्रमः च क्त्वि

क्रमश्च क्त्वि (6.4.18)
Pāṭha: ashtadhyayi.com data.txt row i=64018 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_18_kramaSca_18"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.18", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kramaSca ktvi",
    text_dev              = "क्रमश्च क्त्वि",
    samagra_slp1          = "aNgasya kramaH ca ktvi dIrGaH na upaDAyAH kvi-JaloH kNiti viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य क्रमः च क्त्वि दीर्घः न उपधायाः क्वि-झलोः क्ङिति विभाषा",
    padaccheda_dev        = "क्रमः च क्त्वि",
    why_dev               = "(सूत्रम् 6.4.18) क्रमश्च क्त्वि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
