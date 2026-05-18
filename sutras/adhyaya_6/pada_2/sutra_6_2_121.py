"""
6.2.121  कूलतीरतूलमूलशालाऽक्षसममव्ययीभावे  —  VIDHI

Padaccheda: कूल-तीर-तूल-मूल-शाला-अक्ष-समम् अव्ययीभावे

कूलतीरतूलमूलशालाऽक्षसममव्ययीभावे (6.2.121)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_121_kUlatIratU_121"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_121_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kUlatIratUlamUlaSAlA'kzasamamavyayIBAve",
    text_dev              = "कूलतीरतूलमूलशालाऽक्षसममव्ययीभावे",
    padaccheda_dev        = "कूल-तीर-तूल-मूल-शाला-अक्ष-समम् अव्ययीभावे",
    why_dev               = "(सूत्रम् 6.2.121) कूलतीरतूलमूलशालाऽक्षसममव्ययीभावे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
