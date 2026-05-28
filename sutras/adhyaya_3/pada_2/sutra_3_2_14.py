"""
3.2.14  शमि धातोः संज्ञायाम्  —  VIDHI

Padaccheda: शमि धातोः संज्ञायाम् ( अत्र शम् इत्यव्ययम् ; तस्मात् प्रातिपदिकानुकरणत्वाद् विभक्तेरुत्पत्तिः| एवम् सवंत्राव्ययस्थले बोध्यम्|)

krt-suffix rule: शमि धातोः संज्ञायाम् (14)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_14_Sami_14"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_14_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Sami DAtoH saMjYAyAm",
    text_dev              = "शमि धातोः संज्ञायाम्",
    padaccheda_dev        = "शमि धातोः संज्ञायाम् ( अत्र शम् इत्यव्ययम् ; तस्मात् प्रातिपदिकानुकरणत्वाद् विभक्तेरुत्पत्तिः| एवम् सवंत्राव्ययस्थले बोध्यम्|)",
    why_dev               = "धातोः कृत्-प्रत्ययः [शमि धातोः संज्ञायाम्] विहितः (३.२.14)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
