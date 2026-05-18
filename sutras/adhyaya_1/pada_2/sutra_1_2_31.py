"""
1.2.31  समाहारः स्वरितः  (samāhāraḥ svaritaḥ)  —  SAMJNA

Meaning: The combination (samāhāra — a pitch that merges the udātta-fall
with an anudātta-rise) is called svarita (circumflex accent). This sūtra
defines the technical name "svarita" for the mixed-pitch phoneme.

Phonological note: The svarita is acoustically a pitch that begins high
(residual udātta) and falls to low (anudātta), or in the jātya / kṣaipra
analysis it combines both tonal qualities in a single syllable. Pāṇini's
"samāhāra" captures this composite nature precisely.

Anuvṛtti: The accent-saṃjñā framework from 1.2.29 (udātta) and 1.2.30
(anudātta) carries forward — svarita completes the triad.

Scope: Universal SAMJNA — registers "svarita" into samjna_registry,
completing the three-accent system: udātta (1.2.29), anudātta (1.2.30),
svarita (1.2.31).

What this rule does NOT do: It does not mark any vowel in any word as
svarita. Actual svarita assignment is the work of accent vidhi sūtras
(e.g., 8.2.4, 8.4.66, etc.).

SLP1 representation: "samAhAraH" (= samāhāraḥ, nominative singular).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    """Idempotent guard — fire only if svarita is not yet registered."""
    return state.samjna_registry.get("svarita") != "samAhAraH"


def act(state: State) -> State:
    """Register 'svarita' = 'samAhAraH' in samjna_registry. No varṇa mutation."""
    state.samjna_registry["svarita"] = "samAhAraH"
    return state


_WHY_DEV = (
    "उदात्त-अनुदात्त-उभयात्मकः समाहारः स्वरित-संज्ञकः। "
    "१.२.२९ उदात्तः, १.२.३० अनुदात्तः — तयोः संयोगात्मकः स्वरितः। "
    "एवं त्रिविधा स्वर-संज्ञा पूर्णा भवति।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.31",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "samAhAraH svaritaH",
    text_dev                = "समाहारः स्वरितः",
    padaccheda_dev          = "समाहारः स्वरितः",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.29", "1.2.30"),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
