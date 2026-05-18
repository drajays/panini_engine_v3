"""
1.2.10  हलन्ताच्च  —  NIYAMA

Anuvṛtti: seṭ (1.2.1 adhikāra), aniṭ-restriction (from 1.2.9 region).
The particle "ca" (च) extends the aniṭ-domain of 1.2.9.

Meaning: And from a hal-ending root also [the pratyaya is aniṭ].  Roots
whose upadesha ends in a HAL consonant and that have not been declared seṭ
are marked aniṭ — they do not take the iṭ augment.

Engine:
  - Finds a dhātu Term whose upadesha_slp1 ends in a HAL phoneme AND that
    does not already carry the "seT" tag AND has not yet been processed by
    this sūtra.
  - Tags the dhātu Term "aniT" and guards re-entry via meta["aniT_1_2_10"].
  - r1_form_identity_exempt=True: no surface string changes in this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import HAL

_HAL: frozenset = HAL


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("aniT_1_2_10"):
            continue
        # Already declared seṭ — this niyama does not apply.
        if "seT" in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not up or up[-1] not in _HAL:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("aniT")
    state.terms[i].meta["aniT_1_2_10"] = True
    state.samjna_registry["1_2_10_halantAt_aniT"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.10",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "halantAc ca",
    text_dev              = "हलन्ताच्च",
    padaccheda_dev        = "हलन्तात् / च (अनिट्)",
    why_dev               = ("हलन्त-धातुः (सेट्-भिन्नः) अनिट् — "
                             "इडागमः न भवति (१.२.९-अनुवृत्ति-विस्तारः)।"),
    anuvritti_from        = ("1.2.9",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
