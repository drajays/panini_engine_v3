"""
1.2.2  विज इट्  —  SAMJNA

Anuvṛtti: seṭ (under 1.2.1 adhikāra region).

Meaning: The root "vij" (to tremble / be agitated) is seṭ — it takes the
iṭ augment before ardhadhātuka suffixes.

Engine:
  - Finds any dhātu Term whose upadesha_slp1 == "vij" and that has not yet
    been tagged "seT" by this sūtra.
  - Tags it "seT" and records the samjna in the registry.
  - r1_form_identity_exempt=True: no surface string changes.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_VIJ_UPADESHA: frozenset = frozenset({"vij"})


def _find_vij(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _VIJ_UPADESHA:
            continue
        if "seT" in t.tags:
            continue
        if t.meta.get("seT_1_2_2"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_vij(state) is not None


def act(state: State) -> State:
    i = _find_vij(state)
    if i is None:
        return state
    state.terms[i].tags.add("seT")
    state.terms[i].meta["seT_1_2_2"] = True
    state.samjna_registry["1_2_2_vij_seT"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.2",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = "vij iw",
    text_dev              = "विज इट्",
    padaccheda_dev        = "विजः / इट्",
    why_dev               = "विज्-धातुः सेट् — अस्य इडागमः अर्धधातुके परे भवति।",
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
