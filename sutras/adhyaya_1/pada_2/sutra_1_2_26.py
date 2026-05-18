"""
1.2.26  रलो व्युपधाद्धलादेः संश्च  —  NIYAMA

Meaning: A root that has r or l as its penultimate phoneme (r/l-upadhā),
AND begins with a consonant (hal-ādi), AND occurs in composition with the
prefix "sam" — [is aniṭ].

This sūtra marks an aniṭ context for hal-ādi, rl-upadhā roots that follow
the "sam" prefix. It is in anuvṛtti from the aniṭ domain opened at 1.2.10.

Engine:
  - Uses module-level _HAL frozenset from phonology.HAL.
  - Finds a dhātu Term where:
      (a) upadesha_slp1[-2] is in {"r", "l"} (r/l penultimate)
      (b) upadesha_slp1[0] is in _HAL (consonant-beginning)
      (c) dhātu.meta has "sam_prefix" == True (sam-prefix context)
  - Guards re-entry via meta["aniT_1_2_26"].
  - Tags the dhātu "aniT".
  - r1_form_identity_exempt=True: no surface string changes in this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import HAL

_HAL: frozenset = HAL

# r/l phonemes that qualify as "upadhā" in this context
_RL: frozenset = frozenset({"r", "l"})


def _find(state: State) -> int | None:
    """Return index of a dhātu Term satisfying ralo-vyupadhā conditions, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("aniT_1_2_26"):
            continue
        # Requires sam prefix in meta
        if not t.meta.get("sam_prefix"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if len(up) < 2:
            continue
        # hal-ādi: consonant-beginning
        if up[0] not in _HAL:
            continue
        # r/l-upadhā: penultimate phoneme is r or l
        if up[-2] not in _RL:
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
    state.terms[i].meta["aniT_1_2_26"] = True
    state.samjna_registry["1_2_26_ralo_vyupaDAt"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.26",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "ralo vyupaDAdDalAdeH saMS ca",
    text_dev              = "रलो व्युपधाद्धलादेः संश्च",
    padaccheda_dev        = "रलः / व्युपधात् / हलादेः / संश्च (अनिट्)",
    why_dev               = ("र-ल-उपधाकस्य हलादे-र्धातोः सम्-पूर्वकस्य "
                             "अनिट्त्वम् — इडागमो न भवति।"),
    anuvritti_from        = ("1.2.10",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
