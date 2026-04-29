"""
1.1.41  अव्ययीभावश्च  —  SAMJNA

Assign avyaya-saṃjñā to an avyayībhāva compound.

Engine (narrow v3 slice):
  - If any term in the current samāsa block carries the structural tag
    ``avyayibhava`` (set by 2.1.6/2.1.13 demo sūtras), tag the whole block as
    ``avyaya`` (all terms, including the merged stem).

This is used to trigger **2.4.82** *sup*-luk for pratyagni/adhistri demos.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_2.pada_1.sutra_2_1_6 import TAG_AVYAYIBHAVA


def cond(state: State) -> bool:
    if not any(TAG_AVYAYIBHAVA in t.tags for t in state.terms):
        return False
    # Apply if there exists at least one term in the block not yet tagged avyaya.
    return any("avyaya" not in t.tags for t in state.terms)


def act(state: State) -> State:
    if not any(TAG_AVYAYIBHAVA in t.tags for t in state.terms):
        return state
    for t in state.terms:
        t.tags.add("avyaya")
    state.samjna_registry["1_1_41_avyayibhava_avyaya"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.41",
    sutra_type     = SutraType.SAMJNA,
    r1_form_identity_exempt=True,
    text_slp1      = "avyayIBAvaH ca",
    text_dev       = "अव्ययीभावश्च",
    padaccheda_dev = "अव्ययीभावः / च",
    why_dev        = "अव्ययीभाव-समासः अव्यय-संज्ञकः (२.४.८२ सुप्-लुक्-प्रसङ्गः)।",
    anuvritti_from = ("1.1.37",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

