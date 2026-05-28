"""
3.1.38  उषविदजागृभ्योऽन्यतरस्याम्  —  VIDHI

Padaccheda: उष-विद-जागृभ्यः अन्यतरस्याम्

Krt suffix rule from dhatu: उषविदजागृभ्योऽन्यतरस्याम् (38)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_38_uzavidajAgfB_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_38_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uzavidajAgfByo'nyatarasyAm",
    text_dev              = "उषविदजागृभ्योऽन्यतरस्याम्",
    padaccheda_dev        = "उष-विद-जागृभ्यः अन्यतरस्याम्",
    why_dev               = "धातोः [उषविदजागृभ्योऽन्यतरस्याम्]-प्रत्ययः विहितः (३.१.38)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
