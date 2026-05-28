"""
8.3.97  अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गुमञ्जिपुञ्जिपरमेबर्हिर्दिव्यग्निभ्यः स्थः  —  VIDHI

Padaccheda: अम्ब-आम्-गो-भूमि-सव्य-अप-द्वि-त्रि-कु-शेकु-शङ्‍कु-अङ्गु-मञ्जि-पुञ्जि-परमे-बर्हिः-दिवि-अग्निभ्यः स्थः (षष्ठ्यर्थे प्रथमा)

अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गुमञ्जिपुञ्जिपरमेबर्हिर्दिव्यग्निभ्यः स्थः (8.3.97)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_97_ambAmbagoB_97"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_97_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ambAmbagoBUmisavyApadvitrikuSekuSaNkvaNgumaYjipuYjiparamebarhirdivyagniByaH sTaH",
    text_dev              = "अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गुमञ्जिपुञ्जिपरमेबर्हिर्दिव्यग्निभ्यः स्थः",
    padaccheda_dev        = "अम्ब-आम्-गो-भूमि-सव्य-अप-द्वि-त्रि-कु-शेकु-शङ्‍कु-अङ्गु-मञ्जि-पुञ्जि-परमे-बर्हिः-दिवि-अग्निभ्यः स्थः (षष्ठ्यर्थे प्रथमा)",
    why_dev               = "(सूत्रम् 8.3.97) अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गुमञ्जिपुञ्जिपरमेबर्हिर्दिव्यग्निभ्यः स्थः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
