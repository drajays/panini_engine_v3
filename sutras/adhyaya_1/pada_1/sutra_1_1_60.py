"""
1.1.60  स्थाने अदर्शनं लोपः  —  SAMJNA

**Padaccheda (teaching):** *adṛśanam* (1.1 *prathamā*), *lopaḥ* (1.1).

**Anuvṛtti** from **1.1.50** *sthāne* (baked into *text_slp1* / *text_dev*, not
computed at run time — CONSTITUTION Art. 4).

**Śāstra (one line):** Non-appearance (*adarśanam*) of a single sound or of a
group of sounds, **in the substitutional locus** (*sthāne*), is called *lopa*.
The term subsumes *anuccāraṇa* / *aśravaṇa* in the tradition, not “eye-sight”
only.

**Engine:** registers the definiens in ``samjna_registry['lopa']`` (R2), like
**1.1.7** *saṃyoga* — a canonical marker that the *lopa* saṃjñā is in force;
**1.3.9** and other *vidhi* sūtras perform the actual phoneme deletions when
their *cond* matches.

**Cross-refs (operational *lopa* elsewhere):** 1.3.9, 8.2.23, 6.1.68, 6.4.48, …
**1.1.56–1.1.58** *sthānivat* for *lupta-varṇa* — separate paribhāṣā.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_1.lopa_samjna_1_1_60 import (
    LOPA_REGISTER_VALUE,
    LOPA_SAMJNA_KEY,
    lopa_samjna_is_registered,
)


def cond(state: State) -> bool:
    return not lopa_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry[LOPA_SAMJNA_KEY] = LOPA_REGISTER_VALUE
    return state


_WHY = (
    "स्थानिनि वर्णः वा वर्णसमूहः वा अदर्शनं यत्, तत् 'लोप' इति संज्ञा — "
    "उपयोगः १.३.९, ८.२.२३, ६.१.६८, … इतिषु; अत्र केवल संज्ञा-निर्णयः।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.60",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "sTAne adarSanam lopaH",
    text_dev       = "स्थाने अदर्शनं लोपः",
    padaccheda_dev = "स्थाने (अन्वा. १.१.५०) / अदर्शनं / लोपः",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.50",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
