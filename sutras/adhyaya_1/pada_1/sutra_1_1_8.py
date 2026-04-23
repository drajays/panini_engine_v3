"""
1.1.8  मुखनासिकावचनोऽनुनासिकः  (mukhanAsikAvacano anunAsikaH)  —  SAMJNA

**Śāstra (GRETIL pāṭha):** *mukha* + *nāsikā* + *avacana* (not realized as a full
separate *nāsikya* / *spṛṣṭa* nasal) — *anunāsika* (e.g. *anusvāra* allophone and
*chandrabindu* nasalization on a vowel).

v3: registers the global *anunāsika* saṃjñā in ``samjna_registry`` (R2).  **Operational**
marking of varṇas is by the ``anunasika`` tag (see ``1.3.2``, ``phonology.tokenizer``,
``phonology/joiner``) — this sūtra is the *śāstrīya* anchor; *vidhi* sūtras read tags +
``pratyahara``/``Varna.slp1`` only (CONSTITUTION Art. 2).

See also **1.1.9** (``sutra_1_1_9``) for *savarṇa*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State, Varna

# R2: canonical value after ``apply_rule("1.1.8", ...)`` .
ANUNASIKA_REGISTER_VALUE: frozenset[str] = frozenset({"1.1.8_mukhanasikA"})


def is_varna_tagged_anunAsika(v: Varna) -> bool:
    """True iff this varṇa carries the engine's *anunāsika* tag (1.1.8 scope in prakriyā)."""
    return "anunasika" in v.tags


def is_anusvara_slp1(slp1: str) -> bool:
    """``M`` = anusvāra (ं), one *anunāsika* locus in SLP1 surface encoding."""
    return slp1 == "M"


def anunAsika_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get("anunAsika") == ANUNASIKA_REGISTER_VALUE


# ════════════════════════════════════════════════════════════
# Sūtra — *anunāsika* definiens once (like 1.1.1 / 1.1.7)
# ════════════════════════════════════════════════════════════


def cond(state: State) -> bool:
    return not anunAsika_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry["anunAsika"] = ANUNASIKA_REGISTER_VALUE
    return state


_WHY = (
    "मुख-नासिक-स्थान-योः उच्चार्यमाणः, "
    "न पुनः स्पर्श-नासिक्य-वद्, सः 'अनुनासिक' इति संज्ञेयः (अनुनासिक-कार्यार्थः)।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.8",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "mukhanAsikAvacano anunAsikaH",
    text_dev       = "मुखनासिकावचनोऽनुनासिकः",
    padaccheda_dev = "मुख-नासिका-वचनः अनुनासिकः",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
