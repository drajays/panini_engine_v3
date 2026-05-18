"""
1.2.24  वञ्चिलुञ्च्यृतश्च  —  NIYAMA

Meaning: The roots vañc (to go crookedly), luñc (to pull out / pluck), and ṛt
(to go / reach) — collected as the "vañci-group" — are also seṭ ("ca" ties
them to the preceding seṭ-granting context of 1.2.1's adhikāra).

This is a niyama explicitly declaring these roots seṭ so that they receive the
iṭ augment in the appropriate kṛt contexts.

Engine:
  - Module-level frozenset _VANCI_GROUP holds the SLP1 upadeśa forms for
    vañc, luñc, and ṛt.
  - Finds a dhātu Term whose upadesha_slp1 is in _VANCI_GROUP and which does
    not yet carry the "seT" tag (avoids redundant application).
  - Guards re-entry via meta["seT_1_2_24"].
  - Adds "seT"; stores the group frozenset in samjna_registry.
  - r1_form_identity_exempt=True: no surface string changes at this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset — CONSTITUTION Article 2
# SLP1: vaYc = vañc, luYc = luñc, ft = ṛt
_VANCI_GROUP: frozenset = frozenset({"vaYc", "luYc", "ft"})


def _find(state: State) -> int | None:
    """Return index of an eligible vañci-group dhātu Term, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("seT_1_2_24"):
            continue
        if "seT" in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _VANCI_GROUP:
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
    state.terms[i].meta["seT_1_2_24"] = True
    state.samjna_registry["1_2_24_vaYci_group"] = _VANCI_GROUP
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.24",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "vaYci-luYcy-ftaS ca",
    text_dev              = "वञ्चिलुञ्च्यृतश्च",
    padaccheda_dev        = "वञ्चि-लुञ्चि-ऋतः / च",
    why_dev               = ("वञ्च्-लुञ्च्-ऋत्-धातवः अपि सेट् भवन्ति — "
                             "एतेभ्यः इडागमो नित्यं भवति।"),
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
