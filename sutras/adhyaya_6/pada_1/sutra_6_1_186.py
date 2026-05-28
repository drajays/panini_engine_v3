"""
6.1.186  तास्यनुदात्तेन्ङिददुपदेशाल्लसार्वधातुकमनुदात्तमहन्विङोः  —  VIDHI

Padaccheda: तासि-अनुदात्त-इत्-ङित्-अत्-उपदेशात् ल-सार्वधातुकम् अनुदात्तम् अ-ह्नु-इङोः

तास्यनुदात्तेन्ङिददुपदेशाल्लसार्वधातुकमनुदात्तमहन्विङोः (6.1.186)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_186_tAsyanudAt_186"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_186_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.186"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.186",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tAsyanudAttenNidadupadeSAllasArvaDAtukamanudAttamahanviNoH",
    text_dev              = "तास्यनुदात्तेन्ङिददुपदेशाल्लसार्वधातुकमनुदात्तमहन्विङोः",
    padaccheda_dev        = "तासि-अनुदात्त-इत्-ङित्-अत्-उपदेशात् ल-सार्वधातुकम् अनुदात्तम् अ-ह्नु-इङोः",
    why_dev               = "(सूत्रम् 6.1.186) तास्यनुदात्तेन्ङिददुपदेशाल्लसार्वधातुकमनुदात्तमहन्विङोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
