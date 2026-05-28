"""
3.2.157  जिदृक्षिविश्रीण्वमाव्यथाभ्यमपरिभूप्रसूभ्यश्च  —  VIDHI

Padaccheda: जि-दृ-क्षि-विश्रि-इण्-वम-अव्यथ-अभ्यम-परिभू-प्रसूभ्यः च

krt-suffix rule: जिदृक्षिविश्रीण्वमाव्यथाभ्यमपरिभूप्रसूभ्यश्च (157)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_157_jidfkziviS_157"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.157"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.157",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jidfkziviSrIRvamAvyaTAByamapariBUprasUByaSca",
    text_dev              = "जिदृक्षिविश्रीण्वमाव्यथाभ्यमपरिभूप्रसूभ्यश्च",
    padaccheda_dev        = "जि-दृ-क्षि-विश्रि-इण्-वम-अव्यथ-अभ्यम-परिभू-प्रसूभ्यः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [जिदृक्षिविश्रीण्वमाव्यथाभ्यमपरिभूप्रसूभ्यश्च] विहितः (३.२.157)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
