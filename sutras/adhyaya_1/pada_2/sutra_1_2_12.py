"""
1.2.12  उश्च  —  NIYAMA

Anuvṛtti: aniṭ domain (from 1.2.10 region).
The particle "ca" (च) extends the aniṭ scope.

Meaning: And [a root ending in] "u" (u-kārānta) [is also aniṭ].
Roots whose upadesha ends in "u" or "U" (long ū) and that have not
been declared seṭ are marked aniṭ — they do not take the iṭ augment.

Engine:
  - Finds a dhātu Term whose upadesha_slp1 ends in "u" or "U" AND that
    does not already carry the "seT" tag AND has not yet been processed
    by this sūtra.
  - Tags the dhātu Term "aniT" and guards re-entry via meta["aniT_1_2_12"].
  - r1_form_identity_exempt=True: no surface string changes in this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_U_KARAS: frozenset = frozenset({"u", "U"})


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("aniT_1_2_12"):
            continue
        # Already declared seṭ — this niyama does not apply.
        if "seT" in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not up or up[-1] not in _U_KARAS:
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
    state.terms[i].meta["aniT_1_2_12"] = True
    state.samjna_registry["1_2_12_u_aniT"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.12",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "uz ca",
    text_dev              = "उश्च",
    padaccheda_dev        = "उः / च (अनिट्)",
    why_dev               = ("उकारान्त-धातुः (सेट्-भिन्नः) अनिट् — "
                             "इडागमः न भवति (१.२.१०-अनुवृत्ति-विस्तारः)।"),
    anuvritti_from        = ("1.2.10",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
