"""
1.2.3  विभाषोर्णोः  —  VIBHASHA

Anuvṛtti: seṭ (under 1.2.1 adhikāra region).

Meaning: Optionally (vibhāṣā), the root "ūrṇu" (to cover / clothe) is seṭ
— it may take the iṭ augment.  When declined (the other option), ūrṇu is
treated as aniṭ in that derivational path.

Engine:
  - Finds any dhātu Term whose upadesha_slp1 == "UrzRu" that has not yet
    been processed by this sūtra.
  - act (vibhasha_default=True): adds "seT" tag and marks meta to prevent
    re-entry.
  - r1_form_identity_exempt=True: no surface string changes in this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_URNNU_UPADESHA: frozenset = frozenset({"UrzRu"})


def _find_urnnu(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _URNNU_UPADESHA:
            continue
        if t.meta.get("seT_1_2_3"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_urnnu(state) is not None


def act(state: State) -> State:
    i = _find_urnnu(state)
    if i is None:
        return state
    state.terms[i].tags.add("seT")
    state.terms[i].meta["seT_1_2_3"] = True
    state.samjna_registry["1_2_3_UrzRu_seT_vibhASA"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.3",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    vibhasha_default      = True,
    text_slp1             = "vibhASA UrzRoH",
    text_dev              = "विभाषोर्णोः",
    padaccheda_dev        = "विभाषा / ऊर्णोः",
    why_dev               = "ऊर्णु-धातुः विकल्पेन सेट् — इडागमः विकल्पेन अर्धधातुके।",
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
