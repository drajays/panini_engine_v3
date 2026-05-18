"""
1.2.18  न क्त्वा सेट्  —  NIYAMA

Meaning: Before the suffix "ktvā" (the gerund suffix), a root that would
otherwise be seṭ is NOT seṭ — i.e., ktvā always takes aniṭ (no iṭ augment).

This is a niyama (restriction): the general seṭ property of a dhātu does
not apply when the following pratyaya is ktvā. The rule is overridden by
explicit exceptions (e.g. 1.2.22 for pūṅ).

Engine:
  - Finds a dhātu Term carrying the "seT" tag.
  - Checks that the immediately following pratyaya Term has
    upadesha_slp1 == "ktvA".
  - Guards re-entry via meta["aniT_ktva_1_2_18"].
  - Removes "seT" tag and adds "aniT" to the dhātu.
  - r1_form_identity_exempt=True: no surface string changes in this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find(state: State) -> int | None:
    """Return the index of a dhātu Term to be made aniṭ, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("aniT_ktva_1_2_18"):
            continue
        if "seT" not in t.tags:
            continue
        # Look for a following pratyaya with upadesha ktvA
        for j in range(i + 1, len(state.terms)):
            pt = state.terms[j]
            if "pratyaya" not in pt.tags:
                continue
            up = (pt.meta.get("upadesha_slp1") or "").strip()
            if up == "ktvA":
                return i
            break  # Only check the immediately relevant pratyaya
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.discard("seT")
    state.terms[i].tags.add("aniT")
    state.terms[i].meta["aniT_ktva_1_2_18"] = True
    state.samjna_registry["1_2_18_na_ktvA_seT"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.18",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "na ktvA seT",
    text_dev              = "न क्त्वा सेट्",
    padaccheda_dev        = "न / क्त्वा / सेट्",
    why_dev               = ("क्त्वा-प्रत्ययस्य पूर्वं सेट्-धातुः अपि अनिट् भवति — "
                             "क्त्वान्तरूपे इडागमो न।"),
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
