"""
1.2.30  नीचैरनुदात्तः  (nīcair anudāttaḥ)  —  SAMJNA

Meaning: [A phoneme pronounced] low (nīcaiḥ) is called anudātta (grave
accent). This sūtra defines the technical name "anudātta" for phonemes
produced with a lowered pitch of the voice (nīcaiḥ = lowly).

Anuvṛtti: The word "udāttaḥ" (as model saṃjñā-pattern) carries from
1.2.29 by anuvṛtti, meaning this sūtra follows the same register-a-
saṃjñā structure. The contrast is nīcaiḥ vs. uccaiḥ.

Scope: Universal SAMJNA — registers "anudAtta" into samjna_registry,
complementing the udātta entry set by 1.2.29. Together, 1.2.29–1.2.31
establish the complete Sanskrit accent system (udātta / anudātta / svarita).

What this rule does NOT do: It does not mark any vowel in any word as
anudātta. Actual accent assignment is the work of later vidhi sūtras.

SLP1 representation: "nIcaiH" (= nīcaiḥ, instrumental of nīcais).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    """Idempotent guard — fire only if anudātta is not yet registered."""
    return state.samjna_registry.get("anudAtta") != "nIcaiH"


def act(state: State) -> State:
    """Register 'anudAtta' = 'nIcaiH' in samjna_registry. No varṇa mutation."""
    state.samjna_registry["anudAtta"] = "nIcaiH"
    return state


_WHY_DEV = (
    "नीचैः उच्चारितः स्वरः अनुदात्त-संज्ञकः। "
    "१.२.२९ तः 'उदात्तः' इत्यनुवृत्तम् — तस्य विपरीतः नीचैः-उच्चारितः अनुदात्तः। "
    "इयं संज्ञा परवर्तिषु स्वर-विधि-सूत्रेषु उपयुज्यते।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.30",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "nIcEr anudAttaH",
    text_dev                = "नीचैरनुदात्तः",
    padaccheda_dev          = "नीचैः अनुदात्तः",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.29",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
