"""
6.3.34  स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियाऽऽदिषु  —  VIDHI

Padaccheda: स्त्रियाः पुंवत् भाषितपुंस्कात्-अनूङ् (लुप्तषष्ठीकम्) समानाधिकरणे स्त्रियाम् अ-पूरणी-प्रिया-आदिषु

स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियाऽऽदिषु (6.3.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_34_striyAH_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_34_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "striyAH puMvadBAzitapuMskAdanUN samAnADikaraRe striyAmapUraRIpriyA''dizu",
    text_dev              = "स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियाऽऽदिषु",
    padaccheda_dev        = "स्त्रियाः पुंवत् भाषितपुंस्कात्-अनूङ् (लुप्तषष्ठीकम्) समानाधिकरणे स्त्रियाम् अ-पूरणी-प्रिया-आदिषु",
    why_dev               = "(सूत्रम् 6.3.34) स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियाऽऽदिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
