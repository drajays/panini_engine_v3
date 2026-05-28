"""
3.2.59  ऋत्विग्दधृक्स्रग्दिगुष्णिगञ्चुयुजिक्रुञ्चां च  —  VIDHI

Padaccheda: ऋत्विक्-दधृक्-स्रक्-दिक्-उष्णिक्-अञ्चु-युजि-क्रुञ्चाम् च

krt-suffix rule: ऋत्विग्दधृक्स्रग्दिगुष्णिगञ्चुयुजिक्रुञ्चां च (59)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_59_ftvigdaDfk_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_59_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ftvigdaDfksragdiguzRigaYcuyujikruYcAM ca",
    text_dev              = "ऋत्विग्दधृक्स्रग्दिगुष्णिगञ्चुयुजिक्रुञ्चां च",
    padaccheda_dev        = "ऋत्विक्-दधृक्-स्रक्-दिक्-उष्णिक्-अञ्चु-युजि-क्रुञ्चाम् च",
    why_dev               = "धातोः कृत्-प्रत्ययः [ऋत्विग्दधृक्स्रग्दिगुष्णिगञ्चुयुजिक्रुञ्चां च] विहितः (३.२.59)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
