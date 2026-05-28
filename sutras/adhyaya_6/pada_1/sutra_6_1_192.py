"""
6.1.192  भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति  —  VIDHI

Padaccheda: भी-ह्री-भृ-हु-मद-जन-धन-दरिद्रा-जागराम् प्रत्ययात् पूर्वम् प्-इति

भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति (6.1.192)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_192_BIhrIBfhum_192"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_192_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.192"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.192",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BIhrIBfhumadajanaDanadaridrAjAgarAM pratyayAt pUrvam piti",
    text_dev              = "भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति",
    padaccheda_dev        = "भी-ह्री-भृ-हु-मद-जन-धन-दरिद्रा-जागराम् प्रत्ययात् पूर्वम् प्-इति",
    why_dev               = "(सूत्रम् 6.1.192) भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
