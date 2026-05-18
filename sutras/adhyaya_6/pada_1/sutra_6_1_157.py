"""
6.1.157  पारस्करप्रभृतीनि च संज्ञायाम्  —  VIDHI

Padaccheda: पारस्कर-प्रभृतीनि च संज्ञायाम्

पारस्करप्रभृतीनि च संज्ञायाम् (6.1.157)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_157_pAraskarap_157"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_157_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.157"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.157",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pAraskarapraBftIni ca saMjYAyAm",
    text_dev              = "पारस्करप्रभृतीनि च संज्ञायाम्",
    padaccheda_dev        = "पारस्कर-प्रभृतीनि च संज्ञायाम्",
    why_dev               = "(सूत्रम् 6.1.157) पारस्करप्रभृतीनि च संज्ञायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
