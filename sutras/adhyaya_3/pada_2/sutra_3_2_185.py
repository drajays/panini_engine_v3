"""
3.2.185  पुवः संज्ञायाम्  —  VIDHI

Padaccheda: पुवः संज्ञायाम्

krt-suffix rule: पुवः संज्ञायाम् (185)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_185_puvaH_185"


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
    state.meta["krt_kind"] = "3.2.185"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.185",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "puvaH saMjYAyAm",
    text_dev              = "पुवः संज्ञायाम्",
    padaccheda_dev        = "पुवः संज्ञायाम्",
    why_dev               = "धातोः कृत्-प्रत्ययः [पुवः संज्ञायाम्] विहितः (३.२.185)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
