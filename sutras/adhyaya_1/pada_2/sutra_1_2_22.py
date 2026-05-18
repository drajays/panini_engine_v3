"""
1.2.22  पूङः क्त्वा च  —  NIYAMA

Meaning: The root pūṅ (to purify, gana 9 / ā-group) is seṭ before ktvā also
("ca" connects it to the niṣṭhā context of 1.2.19). This sūtra is an explicit
apavāda (exception) to 1.2.18 (na ktvā seṭ): pūṅ retains the iṭ augment
before ktvā.

Engine:
  - Finds a dhātu Term whose upadesha_slp1 matches a pūṅ form (pUN or pU).
  - Checks that the following pratyaya has upadesha_slp1 == "ktvA".
  - Guards re-entry via meta["seT_pUN_ktva_1_2_22"].
  - Removes "aniT" if present (reversing any 1.2.18 application) and adds "seT".
  - r1_form_identity_exempt=True: no surface string changes in this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset for pūṅ upadeśa forms (SLP1)
_PUN_UPADESHA: frozenset = frozenset({"pUN", "pU"})


def _find(state: State) -> int | None:
    """Return index of pūṅ dhātu Term before ktvā, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("seT_pUN_ktva_1_2_22"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _PUN_UPADESHA:
            continue
        # Look for ktvā pratyaya immediately following
        for j in range(i + 1, len(state.terms)):
            pt = state.terms[j]
            if "pratyaya" not in pt.tags:
                continue
            pup = (pt.meta.get("upadesha_slp1") or "").strip()
            if pup == "ktvA":
                return i
            break
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.discard("aniT")
    state.terms[i].tags.add("seT")
    state.terms[i].meta["seT_pUN_ktva_1_2_22"] = True
    state.samjna_registry["1_2_22_pUN_ktvA_seT"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.22",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "pUNaH ktvA ca",
    text_dev              = "पूङः क्त्वा च",
    padaccheda_dev        = "पूङः / क्त्वा / च",
    why_dev               = ("पूङ्-धातोः क्त्वा-प्रत्ययस्य पूर्वमपि सेट् भवति — "
                             "१.२.१८-अपवादः, पूत्वा इत्यत्र इडागमो भवति।"),
    anuvritti_from        = ("1.2.18",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
