"""
1.2.33  एकश्रुति दूरात् सम्बुद्धौ  (ekaśruti dūrāt sambuddhau)  —  SAMJNA

Meaning: [The vowels used] in calling from a distance (dūrāt) in the
vocative (sambuddhi) [have] ekaśruti (monotone / single-pitch) accent.
When a speaker calls out to someone from afar, the vocative syllables are
pronounced at a single, level pitch — neither rising nor falling — and that
quality is technically named "ekaśruti."

Anuvṛtti: The accent-saṃjñā framework from 1.2.29 (udātta) carries forward;
ekaśruti completes a special accent category outside the standard
udātta/anudātta/svarita triad.

Scope: SAMJNA — registers the "ekaśruti" accent saṃjñā for the dūrāt-
sambuddhi context into ``samjna_registry``. The key
``"1_2_33_ekazruti"`` is the idempotency guard; ``"ekazruti"`` carries the
contextual value ``"dUrAt_sambudDau"``.

What this rule does NOT do: It does not mark any vowel in any word as
ekaśruti. That assignment belongs to vidhi sūtras in the derivation.

Blindness:
  - cond() reads only ``state.samjna_registry`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    """Idempotent guard — fire only if ekaśruti is not yet registered."""
    return state.samjna_registry.get("1_2_33_ekazruti") is not True


def act(state: State) -> State:
    """Register ekaśruti saṃjñā for the dūrāt-sambuddhi context."""
    state.samjna_registry["1_2_33_ekazruti"] = True
    state.samjna_registry["ekazruti"] = "dUrAt_sambudDau"
    return state


_WHY_DEV = (
    "दूरात् (विप्रकृष्टस्थानात्) सम्बोधने — सम्बुद्धि-सन्दर्भे — "
    "उच्चारितः स्वरः एकश्रुति-संज्ञकः। "
    "एकश्रुतिः न उदात्तः, न अनुदात्तः, न स्वरितः — "
    "अपि तु समस्वर-विशेषः। "
    "इयं संज्ञा 'एकश्रुति' शब्दस्य अर्थं निर्धारयति।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.33",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "ekazruti dUrAt sambudDAv",
    text_dev                = "एकश्रुति दूरात् सम्बुद्धौ",
    padaccheda_dev          = "एकश्रुतिः / दूरात् / सम्बुद्धौ",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.29",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
