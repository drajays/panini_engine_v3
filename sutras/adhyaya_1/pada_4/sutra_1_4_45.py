"""
1.4.45  आधारोऽधिकरणम्  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked *anuvṛtti*):** *kārake ādhāraḥ adhikaraṇam* — **1.4.23** *kārake*;
**1.4.1** *ekasañjñā* (metadata).

*Śāstra (laghu):* the *pada*/*artha* that is the *ādhāra* (locus / support) for the
action insofar as it bears the *vyāpāra* of the *kartṛ* or the *phala* of the
*karman* receives the technical name *adhikaraṇa-kāraka* (e.g. *kaṭe āste*,
*sthālyāṃ pacati*; *saptamī* by **2.3.36** when *adhikaraṇa* is expressed).

*Engine:* writes ``state.samjna_registry[SAMJNA_KEY] = frozenset(term_indices)``.
The recipe sets ``state.meta[META_LOCUS_INDICES]`` to a non-empty ``tuple`` of
valid term indices (caller supplies *vākya*-level analysis). **R2**-safe;
``cond`` does not read paradigm coordinates (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

# Public names for recipes / tests (do not read ``anuvritti_from`` at runtime).
SAMJNA_KEY = "1.4.45_adhikaraNa"
META_LOCUS_INDICES = "1_4_45_adhikaraNa_locus_term_indices"


def _proposed_indices(state: State) -> frozenset[int] | None:
    raw = state.meta.get(META_LOCUS_INDICES)
    if not isinstance(raw, tuple) or not raw:
        return None
    if not all(isinstance(i, int) for i in raw):
        return None
    n = len(state.terms)
    if not all(0 <= i < n for i in raw):
        return None
    return frozenset(raw)


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.45", state, "1.4.23"):
        return False
    prop = _proposed_indices(state)
    if prop is None:
        return False
    prev = state.samjna_registry.get(SAMJNA_KEY)
    if prev == prop:
        return False
    return True


def act(state: State) -> State:
    prop = _proposed_indices(state)
    assert prop is not None
    state.samjna_registry[SAMJNA_KEY] = prop
    for i in prop:
        if 0 <= i < len(state.terms):
            state.terms[i].tags.add("adhikaraṇa")
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.45",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "kArake ADhAraH adhikaraRam",
    text_dev       = "कारके आधारः अधिकरणम् (एकसंज्ञा १.४.१)",
    padaccheda_dev = "कारके / आधारः / अधिकरणम्",
    why_dev        = (
        "क्रियायाः कर्तुः कर्मणो वा यः पदार्थ आधारः, स अधिकरण-कारक-संज्ञकः "
        "(काशिका-मतेन) — अभिकल्प्य मेटा 1_4_45_adhikaraNa_locus_term_indices इति।"
    ),
    anuvritti_from = ("1.4.1", "1.4.23"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
