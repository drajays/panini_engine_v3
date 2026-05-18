"""
1.2.39  स्वरितात् संहितायामनुदात्तानाम्
        (svaritāt saṃhitāyām anudāttānām)  —  PARIBHASHA

Meaning: After a svarita [syllable], in saṃhitā (continuous speech /
sandhi context), anudātta [vowels become anudātta-fall / remain depressed].

This is a phonological paribhāṣā about accent behaviour in saṃhitā: when
an anudātta vowel follows a svarita in continuous speech, it undergoes the
characteristic depression (falls / remains at low pitch). The rule defines
the interpretive frame for saṃhitā accent processing.

Anuvṛtti: The accent-saṃjñā context from 1.2.30 (anudātta) and 1.2.31
(svarita) carries forward, providing the definitional framework within which
this paribhāṣā operates.

Engine:
  - Gate-style idempotent PARIBHASHA.
  - cond: fire only if paribhasha_gates["1_2_39_svaritAt_saMhitAyAm"] is not True.
  - act: set paribhasha_gates["1_2_39_svaritAt_saMhitAyAm"] = True;
         set samjna_registry["1_2_39_svaritAt_saMhitAyAm"] = True; return state.
  - r1_form_identity_exempt=True: no surface string changes.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    """Idempotent guard — fire only if the svarita-saṃhitā gate is not yet set."""
    return state.paribhasha_gates.get("1_2_39_svaritAt_saMhitAyAm") is not True


def act(state: State) -> State:
    """Register the svarita-saṃhitā paribhāṣā gate. No varṇa mutation."""
    state.paribhasha_gates["1_2_39_svaritAt_saMhitAyAm"] = True
    state.samjna_registry["1_2_39_svaritAt_saMhitAyAm"] = True
    return state


_WHY_DEV = (
    "स्वरितात् परस्य अनुदात्तस्य संहितायां सन्नतर-भावः — "
    "स्वरित-परे अनुदात्त-स्वराः नीचतरं भवन्ति। "
    "इयं परिभाषा संहिता-स्वर-प्रक्रियायाः व्याख्यानं करोति। "
    "१.२.३० (अनुदात्तः), १.२.३१ (स्वरितः) इत्यनुवृत्तम्।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.39",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "svaritAt saMhitAyAm anudAttAnAm",
    text_dev                = "स्वरितात् संहितायामनुदात्तानाम्",
    padaccheda_dev          = "स्वरितात् / संहितायाम् / अनुदात्तानाम्",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.30", "1.2.31"),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
