"""
3.2.162  विदिभिदिच्छिदेः कुरच्  —  VIDHI

Padaccheda: विदि-भिदि-च्छिदेः कुरच्

krt-suffix rule: विदिभिदिच्छिदेः कुरच् (162)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_162_vidiBidicC_162"


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
    state.meta["krt_kind"] = "3.2.162"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.162",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vidiBidicCideH kurac",
    text_dev              = "विदिभिदिच्छिदेः कुरच्",
    padaccheda_dev        = "विदि-भिदि-च्छिदेः कुरच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [विदिभिदिच्छिदेः कुरच्] विहितः (३.२.162)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
