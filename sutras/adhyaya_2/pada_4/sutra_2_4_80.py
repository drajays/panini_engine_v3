"""
2.4.80  मन्त्रे घसह्वरणशवृदहाद्वृच्कृगमिजनिभ्यो लेः  —  VIDHI

Padaccheda: मन्त्रे घस-ह्वर-णश-वृ-दह-आत्-वृच्-कृ-गमि-जनिभ्यः लेः

luk of le in mantra after ghasa, hvr, at, vrc, kr, gami, jani.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_80_mantre_ghasa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_80_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mantre GasahvaraRaSavfdahAdvfckfgamijaniByo leH",
    text_dev              = "मन्त्रे घसह्वरणशवृदहाद्वृच्कृगमिजनिभ्यो लेः",
    padaccheda_dev        = "मन्त्रे घस-ह्वर-णश-वृ-दह-आत्-वृच्-कृ-गमि-जनिभ्यः लेः",
    why_dev               = "मन्त्रे घस-ह्वर-आत्-वृच्-कृ-गमि-जनिभ्यः लेः (२.४.८०)।",
    anuvritti_from        = ('2.4.72',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
