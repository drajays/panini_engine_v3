"""
1.2.29  उच्चैरुदात्तः  (uccair udāttaḥ)  —  SAMJNA

Meaning: [A phoneme pronounced] high (uccaiḥ) is called udātta (acute
accent). This sūtra defines the technical name "udātta" for phonemes that
are produced with a raised pitch of the voice (uccaiḥ = highly).

Scope: Universal SAMJNA — registers the definiendum for the accent term
"udātta" into samjna_registry. Subsequent sūtras (1.2.30, 1.2.31) define
the complementary accent terms by anuvṛtti from this rule.

What this rule does NOT do: It does not assign the udātta accent to any
phoneme in any word. That assignment is the work of vidhi sūtras (e.g.,
accent rules in 6.1, 6.2). This rule only fixes the interpretive gate —
the meaning of the word "udātta" whenever it appears in later sūtras.

SLP1 representation: "uccaiH" (= uccaiḥ, instrumental ablative of uccais).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    """Idempotent guard — fire only if udātta is not yet registered."""
    return state.samjna_registry.get("udAtta") != "uccaiH"


def act(state: State) -> State:
    """Register 'udAtta' = 'uccaiH' in samjna_registry. No varṇa mutation."""
    state.samjna_registry["udAtta"] = "uccaiH"
    return state


_WHY_DEV = (
    "उच्चैः उच्चारितः स्वरः उदात्त-संज्ञकः। "
    "इयं संज्ञा 'उदात्त' शब्दस्य अर्थं निर्धारयति — "
    "परवर्तिषु सूत्रेषु 'उदात्त' इति पदं यत्रोपयुज्यते तत्र इयं व्याख्या।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.29",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "uccEr udAttaH",
    text_dev                = "उच्चैरुदात्तः",
    padaccheda_dev          = "उच्चैः उदात्तः",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
