"""
1.2.38  देवब्रह्मणोरनुदात्तः  —  SAMJNA

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
Pāṭha: ashtadhyayi.com data.txt row i=12038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset — CONSTITUTION Article 2
DEVA_BRAHMAN: frozenset = frozenset({"deva", "brahman"})


def cond(state: State) -> bool:
    """देवब्रह्मणोरनुदात्तः: the words देव / ब्रह्मन् in a sambuddhi (1.2.37 anuvṛtti)."""
    return (state.samjna_registry.get("1_2_38_deva_brahman_anudAtta") is None
            and any("sambuddhi" in t.tags for t in state.terms)
            and any((t.meta.get("upadesha_slp1") or "").strip() in ("deva", "brahman") for t in state.terms))


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
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = 'devabrahmaRoranudAttaH',
    text_dev                = 'देवब्रह्मणोरनुदात्तः',
    samagra_slp1            = "deva-brahmaRoH anudAttaH ekaSruti subrahmaRyAyAm svaritasya tu udAttaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev             = "देव-ब्रह्मणोः अनुदात्तः एकश्रुति सुब्रह्मण्यायाम् स्वरितस्य तु उदात्तः",
    padaccheda_dev          = "देव-ब्रह्मणोः / अनुदात्तः",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.30",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA", "DEVA_BRAHMAN"]
