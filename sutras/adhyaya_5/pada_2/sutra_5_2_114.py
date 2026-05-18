"""
5.2.114  ज्योत्स्नातमिस्राशृङ्गिणोजस्विन्नूर्जस्वलगोमिन्मलिनमलीमसाः  —  VIDHI

Padaccheda: ज्योत्स्ना-तमिस्रा-शृङ्गिण-ऊजस्विन्-ऊर्जस्वल-गोमिन्-मलिन-मलीमसाः

ज्योत्स्नातमिस्राशृङ्गिणोजस्विन्नूर्जस्वलगोमिन्मलिनमलीमसाः (5.2.114)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_114_jyotsnAtam_114"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_114_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.114"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jyotsnAtamisrASfNgiRojasvinnUrjasvalagominmalinamalImasAH",
    text_dev              = "ज्योत्स्नातमिस्राशृङ्गिणोजस्विन्नूर्जस्वलगोमिन्मलिनमलीमसाः",
    padaccheda_dev        = "ज्योत्स्ना-तमिस्रा-शृङ्गिण-ऊजस्विन्-ऊर्जस्वल-गोमिन्-मलिन-मलीमसाः",
    why_dev               = "(सूत्रम् 5.2.114) ज्योत्स्नातमिस्राशृङ्गिणोजस्विन्नूर्जस्वलगोमिन्मलिनमलीमसाः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
