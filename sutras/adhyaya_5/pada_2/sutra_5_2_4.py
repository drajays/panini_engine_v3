"""
5.2.4  विभाषा तिलमाषोमाभङ्गाऽणुभ्यः  —  VIDHI

Padaccheda: विभाषा तिल-माष-उमा-भङ्गा-अणुभ्यः

विभाषा तिलमाषोमाभङ्गाऽणुभ्यः (5.2.4)
Pāṭha: ashtadhyayi.com data.txt row i=52004 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_4_viBAzA_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.4", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'viBAzA tilamAzomABaNgARuByaH',
    text_dev              = 'विभाषा तिलमाषोमाभङ्गाऽणुभ्यः',
    samagra_slp1          = "DAnyAnAm Bavane kzetre iti tila-mAza-umA-BaNgA-aRuByaH viBAzA yat  KaY",
    samagra_dev           = "'धान्यानाम् भवने क्षेत्रे' (इति) तिल-माष-उमा-भङ्गा-अणुभ्यः विभाषा यत् , खञ्",
    padaccheda_dev        = "विभाषा तिल-माष-उमा-भङ्गा-अणुभ्यः",
    why_dev               = "(सूत्रम् 5.2.4) विभाषा तिलमाषोमाभङ्गाऽणुभ्यः।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
