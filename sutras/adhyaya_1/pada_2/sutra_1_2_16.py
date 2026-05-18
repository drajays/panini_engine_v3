"""
1.2.16  विभाषोपयमने  —  VIBHASHA

Anuvṛtti: from 1.2.15 (yam, aniṭ domain).

Meaning: Optionally (विभाषा), [the root] "yam" in "upayamana"
(उपयमन — the marital / taking-for-oneself context) [is seṭ].

This is the counter-path to 1.2.15: in upayamana context yam may
optionally be seṭ (takes iṭ augment).  The vibhāṣā default is False
(aniṭ remains the default per 1.2.15; seṭ is the optional path).

Engine:
  - Requires a dhātu Term with upadesha_slp1 == "yam".
  - Requires the dhātu to carry the structural tag "upayamana_usage"
    (set by the recipe when the upayamana semantic is intended).
  - Guards re-entry via dhātu meta["seT_1_2_16"].
  - When the vibhāṣā is accepted (vibhasha_choice=True in the recipe
    step), tags the dhātu "seT" and removes any earlier "aniT" tag
    (in case 1.2.15 already fired).
  - r1_form_identity_exempt=True: no surface string changes in this step.
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
        if t.meta.get("seT_1_2_16"):
            continue
        if "upayamana_usage" not in t.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    # Remove aniT if 1.2.15 tagged it earlier (vibhāṣā overrides).
    t.tags.discard("aniT")
    t.tags.add("seT")
    t.meta["seT_1_2_16"] = True
    state.samjna_registry["1_2_16_yam_upayamane_seT"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.16",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzopayamane",
    text_dev              = "विभाषोपयमने",
    padaccheda_dev        = "विभाषा / उपयमने (सेट्-विकल्पः)",
    why_dev               = ("√यम्-धातुः उपयमन-अर्थे विकल्पेन सेट् — "
                             "इडागमः विभाषया भवति (१.२.१५-अपवादः)।"),
    anuvritti_from        = ("1.2.15",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
