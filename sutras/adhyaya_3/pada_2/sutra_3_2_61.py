"""
3.2.61  सत्सूद्विषद्रुहदुहयुजविदभिदच्छिदजिनीराजामुपसर्गेऽपि क्विप्  —  VIDHI

Padaccheda: सत्-सू-द्विष-द्रुह-दुह-युज-विद-भिद-च्छिद-जि-नी-राजाम् उपसर्गे अपि क्विँप्

krt-suffix rule: सत्सूद्विषद्रुहदुहयुजविदभिदच्छिदजिनीराजामुपसर्गेऽपि क्विप् (61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_61_satsUdviza_61"


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
    state.meta["krt_kind"] = "3.2.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "satsUdvizadruhaduhayujavidaBidacCidajinIrAjAmupasarge'pi kvip",
    text_dev              = "सत्सूद्विषद्रुहदुहयुजविदभिदच्छिदजिनीराजामुपसर्गेऽपि क्विप्",
    padaccheda_dev        = "सत्-सू-द्विष-द्रुह-दुह-युज-विद-भिद-च्छिद-जि-नी-राजाम् उपसर्गे अपि क्विँप्",
    why_dev               = "धातोः कृत्-प्रत्ययः [सत्सूद्विषद्रुहदुहयुजविदभिदच्छिदजिनीराजामुपसर्गेऽपि क्विप्] विहितः (३.२.61)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
