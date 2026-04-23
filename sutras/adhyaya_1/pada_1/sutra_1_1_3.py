"""
1.1.3  इको गुणवृद्धी  (iko guNavfdDI)  —  PARIBHASHA

**Paribhāṣā (sthāniniyama):** when a later *vidhi* names the operation *guṇa* or
*vṛddhi* but does **not** already name the *sthāyin* in ṣaṣṭhī, the replacement
is understood to target only vowels in pratyāhāra *ik* (short *i, u, ṛ, ḷ* in
SLP1: i, u, f, x).  Gate (A) (operation so named) and “explicit *sthāyin*” are
resolved with flags from the triggering sūtra — use `ik_suppletion_context()`.

**What this file registers:** `state.paribhasha_gates[GATE_KEY]` holds the
canonical *ik* member set (Māheśvara-derived) so resolvers and *vidhi* sūtras
can test *sthāyin* without reading gold lists.

See also **1.1.4** / **1.1.5** — ``sutra_1_1_4.ik_guna_vriddhi_blocked_by_1_1_4`` (*ārdhadhātuke*
*dhātu* lopa) and ``sutra_1_1_5.ik_guna_vriddhi_blocked_by_1_1_5`` (*kṅiti* locus for *kit*
*pratyāya*); then **1.1.6** (*dīdhī*…).
"""
from __future__ import annotations

from typing import FrozenSet

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import pratyahara

# Single key for `paribhasha_gates` — consult this from resolvers / vidhi.
GATE_KEY: str = "iko_guna_vrddhi"


def ik_sthanin_set_slp1() -> FrozenSet[str]:
    """Pratyāhāra *ik* in SLP1; identical to `phonology.pratyahara.IK`."""
    return pratyahara.IK


def is_guna_vriddhi_sthanin(slp1_char: str) -> bool:
    """
    True iff this single SLP1 vowel may be *sthāyin* when 1.1.3 *ik* suppletion
    applies: candidate must belong to *ik*.
    """
    return slp1_char in pratyahara.IK


def ik_suppletion_context(
    *,
    operation_named_guna_or_vriddhi: bool,
    sthanin_explicit_in_triggering_sutra: bool,
) -> bool:
    """
    When True, the *ik-only* *sthāyin* rule is relevant: only
    `is_guna_vriddhi_sthanin(c)` candidates are allowed. When False, the
    triggering sūtra fixes the target set, or the operation is not a *guṇa* /
    *vṛddhi* in the metarule sense.
    """
    return operation_named_guna_or_vriddhi and not sthanin_explicit_in_triggering_sutra


# ═══════════════════════════════════════════════════════════════════
# Sūtra: register *ik* *sthāyin* gate once (idempotent, like 1.1.50).
# ═══════════════════════════════════════════════════════════════════


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "sthanin_ik_slp1": frozenset(pratyahara.IK),
    }
    return state


_WHY = (
    "यत्र गुण-वृद्धी उत्सर्गतः, न च स्थानी षष्ठ्यन्तं निर्दिष्टः, "
    "तत्र स्थानी इक्-वर्ण एव; अत्र तत्-परिभाषा-द्वारा निश्चयः।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.3",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "iko guNavfdDI",
    text_dev       = "इको गुणवृद्धी",
    padaccheda_dev = "इकः गुणवृद्धी",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
