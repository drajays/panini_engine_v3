"""
1.2.15  यमो गन्धने  —  NIYAMA

Anuvṛtti: aniṭ domain (from 1.2.1 adhikāra).

Meaning: The root "yam" (√yam, to restrain; upadesha_slp1 = "yam") in
the sense of "gandhana" (गन्धन — restraint/fragrance context) is aniṭ.

Engine note:
  The semantic "gandhana" meaning cannot be read from the surface form.
  In v3, the recipe marks the dhātu Term with the structural tag
  "gandhana_usage" when this semantic is intended.  This sūtra fires if:
    (a) the dhātu has upadesha_slp1 == "yam", AND
    (b) "seT" is NOT in its tags, AND
    (c) "aniT_1_2_15" is NOT yet in its meta, AND
    (d) the dhātu carries the "gandhana_usage" tag  —OR—
        no usage-discriminator tag is present at all (default: gandhana).
  If the dhātu carries "upayamana_usage" (handled by 1.2.16), this sūtra
  does not fire for that term.

  r1_form_identity_exempt=True: no surface string changes in this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_YAM_UPADESHA: frozenset = frozenset({"yam"})


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _YAM_UPADESHA:
            continue
        if "seT" in t.tags:
            continue
        if t.meta.get("aniT_1_2_15"):
            continue
        # Skip if upayamana usage — that is the domain of 1.2.16.
        if "upayamana_usage" in t.tags:
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
    state.terms[i].meta["aniT_1_2_15"] = True
    state.samjna_registry["1_2_15_yam_gAndane_aniT"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.15",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "yamo ganDane",
    text_dev              = "यमो गन्धने",
    padaccheda_dev        = "यमः / गन्धने (अनिट्)",
    why_dev               = ("√यम्-धातुः गन्धन-अर्थे अनिट् — "
                             "इडागमः न भवति।"),
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
