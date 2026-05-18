"""
2.4.3  अनुवादे चरणानाम्  —  VIDHI

Padaccheda: अनुवादे / चरणानाम्

Śāstra: in an anuvāda (citation / mention context), a dvandva of Vedic
recitation branches (caraṇa) takes ekavacana.

Engine: sets gate "2_4_3_anuvade_carana_ekavacana".
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "2_4_3_anuvade_carana_ekavacana"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.3",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = "anuvAde caraRAnam",
    text_dev       = "अनुवादे चरणानाम्",
    padaccheda_dev = "अनुवादे / चरणानाम्",
    why_dev        = "अनुवाद-प्रसङ्गे चरण-द्वन्द्वः एकवचने भवति।",
    anuvritti_from = ("2.4.1", "2.4.2"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
