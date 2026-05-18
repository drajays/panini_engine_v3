"""
5.3.118  अभिजिद्विदभृच्छालावच्छिखावच्छमीवदूर्णावच्छ्रुमदणो यञ्  —  VIDHI

Padaccheda: अभिजित्-विदभृत्-शालावत्-शिखावत्-शमीवत्-ऊर्णावत्-श्रुमत्-अणः यञ्

अभिजिद्विदभृच्छालावच्छिखावच्छमीवदूर्णावच्छ्रुमदणो यञ् (5.3.118)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_118_aBijidvida_118"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_118_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.118"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.118",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aBijidvidaBfcCAlAvacCiKAvacCamIvadUrRAvacCrumadaRo yaY",
    text_dev              = "अभिजिद्विदभृच्छालावच्छिखावच्छमीवदूर्णावच्छ्रुमदणो यञ्",
    padaccheda_dev        = "अभिजित्-विदभृत्-शालावत्-शिखावत्-शमीवत्-ऊर्णावत्-श्रुमत्-अणः यञ्",
    why_dev               = "(सूत्रम् 5.3.118) अभिजिद्विदभृच्छालावच्छिखावच्छमीवदूर्णावच्छ्रुमदणो यञ्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
