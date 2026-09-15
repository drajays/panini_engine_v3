"""
3.2.71  मन्त्रे श्वेतवहौक्थशस्पुरोडाशो ण्विन्  —  VIDHI

Padaccheda: मन्त्रे श्वेतवह-उक्थशस्-पुरोडाशः ण्विन्

krt-suffix rule: मन्त्रे श्वेतवहौक्थशस्पुरोडाशो ण्विन् (71)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_71_mantre_71"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.71", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mantre SvetavahOkTaSaspuroqASo Rvin",
    text_dev              = "मन्त्रे श्वेतवहौक्थशस्पुरोडाशो ण्विन्",
    padaccheda_dev        = "मन्त्रे श्वेतवह-उक्थशस्-पुरोडाशः ण्विन्",
    why_dev               = "धातोः कृत्-प्रत्ययः [मन्त्रे श्वेतवहौक्थशस्पुरोडाशो ण्विन्] विहितः (३.२.71)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
