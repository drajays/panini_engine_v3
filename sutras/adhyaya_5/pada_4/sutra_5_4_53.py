"""
5.4.53  अभिविधौ सम्पदा च  —  VIDHI

Padaccheda: अभिविधौ सम्पदा च

अभिविधौ सम्पदा च (5.4.53)
Pāṭha: ashtadhyayi.com data.txt row i=54053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_53_aBiviDO_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.53", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aBiviDO sampadA ca",
    text_dev              = "अभिविधौ सम्पदा च",
    samagra_slp1          = "aBUtatadBAve aBiviDO kf-BU-asti-yoge sampadA ca viBAzA sAtiH",
    samagra_dev           = "अभूततद्भावे अभिविधौ कृ-भू-अस्ति-योगे सम्पदा च विभाषा सातिः",
    padaccheda_dev        = "अभिविधौ सम्पदा च",
    why_dev               = "(सूत्रम् 5.4.53) अभिविधौ सम्पदा च।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
