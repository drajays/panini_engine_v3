"""
1.1.9  तुल्यास्यप्रयत्नं सवर्णम्  (tulyAsyaprayatnaM savarNam)  —  SAMJNA

**Śāstra (GRETIL pāṭha):** *tulya* (same) *āsy* (place) and *prayatna* (effort) → the
technical term *savarṇa* (homogeneous set: hrasva–dīrgha pairs, varga members, …).

v3: **R2** — registers the global *savarṇa* saṃjñā.  The **operational** relation
``is_savarna(a, b)`` (and *dīrgha* helpers) live in ``phonology.savarna``; this
sūtra file re-exports for *śāstrīya* trace / ``apply_rule("1.1.9", …)`` without
duplicating the Māheśvara tables (CONSTITUTION Art. 2, Art. 7).

See also **1.1.10** (``sutra_1_1_10``) — *nājjhalau* paribhāṣā for *it* in *upadeśa*;
**1.1.11** (``sutra_1_1_11``) for *pragṛhya* in *dvivacana*;
**1.1.12** (``sutra_1_1_12``) — *adaso māt* ( *aś* / *etad*–*adas* *it* prakaraṇa);
**1.1.13** (``sutra_1_1_13``) — *śe* ( *pragṛhya* *prayoga* off in the *aś* / *ś* locus);
**1.1.14** (``sutra_1_1_14``) *nipāta ekājanāṅ*; **1.1.100** (``sutra_1_1_100``) *Kāśikā* *na mātrā samāse*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import dirgha_of, is_savarna

# R2: canonical value after ``apply_rule("1.1.9", …)`` .
SAVARNA_REGISTER_VALUE: frozenset[str] = frozenset({"1.1.9_tulyAsyA"})


def is_savarna_slp1(a: str, b: str) -> bool:
    """True iff two SLP1 letters are *savarṇa* (1.1.9; ``phonology.savarna``)."""
    return is_savarna(a, b)


def dirgha_savarna_of_ak(slp1: str) -> str:
    """Dīrgha in the *ak* *savarṇa* series; delegates to ``phonology.savarna.dirgha_of``."""
    return dirgha_of(slp1)


def savarNa_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get("savarNa") == SAVARNA_REGISTER_VALUE


# ═══════════════════════════════════════════════════════════
# Sūtra — *savarṇa* definiens once (like 1.1.1 / 1.1.7 / 1.1.8)
# ═══════════════════════════════════════════════════════════


def cond(state: State) -> bool:
    return not savarNa_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry["savarNa"] = SAVARNA_REGISTER_VALUE
    return state


_WHY = (
    "यस्मिन् वर्ण-द्वये आस्यं च प्रयत्नं च तुल्यौ, "
    "ताव् 'सवर्ण' इति प्रसिद्धौ (दीर्ध-सन्धि-नियमादौ)।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.9",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "tulyAsyaprayatnaM savarNam",
    text_dev       = "तुल्यास्यप्रयत्नं सवर्णम्",
    padaccheda_dev = "तुल्य-आस्य-प्रयत्नं सवर्णम्",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
