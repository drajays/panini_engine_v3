"""
1.2.38  देवब्रह्मणोरनुदात्तः  (devabrahmaṇor anudāttaḥ)  —  SAMJNA

Meaning: The words "deva" and "brahman" [in certain Vedic/ritual contexts]
have anudātta (grave) accent. This sūtra assigns the anudātta saṃjñā
specifically to these two words, marking them as accent-class participants.

Anuvṛtti: The accent-saṃjñā framework from 1.2.30 (anudātta defined as
"nīcaiḥ") carries forward, providing the definitional context within which
deva and brahman are classified.

Engine:
  - Module-level DEVA_BRAHMAN frozenset holds the SLP1 forms: "deva", "brahman".
  - Gate-style idempotent SAMJNA.
  - cond: fire only if samjna_registry["1_2_38_deva_brahman_anudAtta"] is not True.
  - act: set samjna_registry["1_2_38_deva_brahman_anudAtta"] = DEVA_BRAHMAN;
         return state.
  - r1_form_identity_exempt=True: no surface string changes.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset — CONSTITUTION Article 2
DEVA_BRAHMAN: frozenset = frozenset({"deva", "brahman"})


def cond(state: State) -> bool:
    """Idempotent guard — fire only if deva-brahman anudātta is not yet registered."""
    return state.samjna_registry.get("1_2_38_deva_brahman_anudAtta") is None


def act(state: State) -> State:
    """Register deva-brahman as anudātta members. No varṇa mutation."""
    state.samjna_registry["1_2_38_deva_brahman_anudAtta"] = DEVA_BRAHMAN
    return state


_WHY_DEV = (
    "देव-ब्रह्मन् इत्येतयोः शब्दयोः अनुदात्त-संज्ञा — "
    "वैदिक-आनुष्ठानिक-सन्दर्भे एतयोः स्वरः नीचैः (अनुदात्तः) भवति। "
    "१.२.३० तः 'अनुदात्तः' इत्यनुवृत्तम्।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.38",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "devabrahmaNoH anudAttaH",
    text_dev                = "देवब्रह्मणोरनुदात्तः",
    padaccheda_dev          = "देव-ब्रह्मणोः / अनुदात्तः",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.30",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA", "DEVA_BRAHMAN"]
