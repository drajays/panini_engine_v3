"""
1.1.7  हलोऽनन्तराः संयोगः  (halo anantarAH saMyogaH)  —  SAMJNA

**Śāstra:** consecutive *hal* (no intervening *ac*) receive the saṃjñā *saṃyoga* (a
consonant cluster, one phonological place for certain operations).

v3 writes the **definition** into ``samjna_registry['samyoga']`` (R2) as a
canonical *frozen* value; the **operational** “is this span a cluster?” test is
``has_samyoga_consecutive_hals`` / ``is_hal_letter`` over Māheśvara *hal* (see
``phonology.pratyahara.HAL``), without consulting gold paradigms (CONSTITUTION
Art. 2, Art. 6).

See also **1.1.8** (``sutra_1_1_8``) for *anunāsika* saṃjñā, then **1.1.9** (``sutra_1_1_9``) for *savarṇa*.
"""
from __future__ import annotations

from typing import Sequence

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State, Varna
from phonology     import pratyahara

# R2: single canonical payload after successful ``apply_rule("1.1.7", ...)`` .
SAMYOGA_REGISTER_VALUE: frozenset[str] = frozenset({"1.1.7_halo_anantarA"})


def is_hal_letter(slp1: str) -> bool:
    """True iff ``slp1`` is a single Māheśvara *hal* (consonant, SLP1)."""
    return slp1 in pratyahara.HAL


def has_samyoga_consecutive_hals(varnas: Sequence[Varna]) -> bool:
    """
    True iff the sequence contains at least one pair of *contiguous* *hal* varṇa,
    the structural definiens of *saṃyoga* (1.1.7; see also 8.2.66, …).
    """
    for i in range(len(varnas) - 1):
        a, b = varnas[i].slp1, varnas[i + 1].slp1
        if a in pratyahara.HAL and b in pratyahara.HAL:
            return True
    return False


def samyoga_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get("samyoga") == SAMYOGA_REGISTER_VALUE


# ══════════════════════════════════════════════════════════════
# Sūtra: register the global *samyoga* definiens once.
# ══════════════════════════════════════════════════════════════


def cond(state: State) -> bool:
    return not samyoga_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry["samyoga"] = SAMYOGA_REGISTER_VALUE
    return state


_WHY = (
    "ये हल्-वर्णाः अनन्तराः, न च अच्-अन्तरः, ते 'संयोग' इति संज्ञинः।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.7",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "halo anantarAH saMyogaH",
    text_dev       = "हलोऽनन्तराः संयोगः",
    padaccheda_dev = "हलः अनन्तराः संयोगः",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
