"""
4.4.27  ओजस्सहोऽम्भसा वर्तते  —  VIDHI

Padaccheda: ओजः-सहः-अम्भसा वर्तते (क्रियापदम्)

ओजस्सहोऽम्भसा वर्तते (4.4.27)
Pāṭha: ashtadhyayi.com data.txt row i=44027 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_27_ojassahom_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.27", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'ojassahomBasA vartate',
    text_dev              = 'ओजस्सहोऽम्भसा वर्तते',
    samagra_slp1          = "tena vartate iti ojas-sahas-amBasA samarTAnAm praTamAt paraH Wak pratyayaH",
    samagra_dev           = "'तेन वर्तते' इति ओजस्-सहस्-अम्भसा समर्थानाम् प्रथमात् परः ठक् प्रत्ययः",
    padaccheda_dev        = "ओजः-सहः-अम्भसा वर्तते (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.27) ओजस्सहोऽम्भसा वर्तते।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
