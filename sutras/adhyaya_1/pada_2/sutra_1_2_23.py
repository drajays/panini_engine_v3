"""
1.2.23  नोपधात्थफान्ताद्वा  —  VIBHASHA

Meaning: Optionally, roots whose final consonant is tha (T in SLP1) or pha
(P in SLP1) — i.e., roots ending in -ttha or -pha — take seṭ.

The sūtra name "nopathāt" signals these roots do NOT have the short-u upadeha
condition of 1.2.21; instead the phonological trigger is the final stop (tha /
pha). "Vā" marks the rule as optional (vibhāṣā).

Engine:
  - Module-level frozenset _TTHA_PHA_ENDINGS holds the SLP1 final phonemes
    that trigger this rule.
  - Finds a dhātu Term whose upadesha_slp1 ends with a phoneme in
    _TTHA_PHA_ENDINGS.
  - Guards re-entry via meta["seT_vibhASA_1_2_23"].
  - vibhasha_default=True → the optional seṭ is applied by default (engine
    handles paksha branching at a higher level).
  - r1_form_identity_exempt=True: no surface string changes at this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset — CONSTITUTION Article 2
# SLP1: T = aspirated dental tha (ठ); P = pha (फ)
_TTHA_PHA_ENDINGS: frozenset = frozenset({"T", "P"})


def _find(state: State) -> int | None:
    """Return index of eligible dhātu Term, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("seT_vibhASA_1_2_23"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not up:
            continue
        if up[-1] not in _TTHA_PHA_ENDINGS:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("seT")
    state.terms[i].meta["seT_vibhASA_1_2_23"] = True
    state.samjna_registry["1_2_23_tthaphAntat_vibhASA"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.23",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = True,
    r1_form_identity_exempt = True,
    text_slp1             = "na upaDAt TaPAntAt vA",
    text_dev              = "नोपधात्थफान्ताद्वा",
    padaccheda_dev        = "न / उपधात् / थ-फ-अन्तात् / वा",
    why_dev               = ("थ-फ-अन्त-धातोः विभाषा सेट् भवति — "
                             "विकल्पेन इडागमो भवति (वा इत्यनेन)।"),
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
