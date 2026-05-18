"""
6.4.20  ज्वरत्वरश्रिव्यविमवामुपधायाश्च  —  VIDHI

Padaccheda: ज्वर-त्वर-स्रिवि-अवि-मवाम् उपधायाः च

ज्वरत्वरश्रिव्यविमवामुपधायाश्च (6.4.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_20_jvaratvara_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_20_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jvaratvaraSrivyavimavAmupaDAyASca",
    text_dev              = "ज्वरत्वरश्रिव्यविमवामुपधायाश्च",
    padaccheda_dev        = "ज्वर-त्वर-स्रिवि-अवि-मवाम् उपधायाः च",
    why_dev               = "(सूत्रम् 6.4.20) ज्वरत्वरश्रिव्यविमवामुपधायाश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
