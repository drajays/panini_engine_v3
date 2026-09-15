"""
3.4.65  शकधृषज्ञाग्लाघटरभलभक्रमसहार्हास्त्यर्थेषु तुमुन्  —  VIDHI

Padaccheda: शक-धृष-ज्ञा-ग्ला-घट-रभ-लभ-क्रम-सह-अर्ह-अस्ति-अर्थेषु तुमुँन्

krt-suffix rule: शकधृषज्ञाग्लाघटरभलभक्रमसहार्हास्त्यर्थेषु तुमुन्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_65_SakaDfzajY_65"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.65", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SakaDfzajYAglAGawaraBalaBakramasahArhAstyarTezu tumun",
    text_dev              = "शकधृषज्ञाग्लाघटरभलभक्रमसहार्हास्त्यर्थेषु तुमुन्",
    padaccheda_dev        = "शक-धृष-ज्ञा-ग्ला-घट-रभ-लभ-क्रम-सह-अर्ह-अस्ति-अर्थेषु तुमुँन्",
    why_dev               = "धातोः प्रत्ययः (३.4.65)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
