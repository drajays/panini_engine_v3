"""
1.3.26  अकर्मकाच्च  —  VIDHI

*Padaccheda:* *akarmakāt* (पञ्चमी) / *ca*.

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* And [ātmanepada] for akarmaka (intransitive) roots [in the senses
above]. Intransitive roots that have no external object naturally take
ātmanepada.

*Engine:* cond checks (a) pada not already "Atmanepada", (b) any dhātu Term
carries the tag "akarmaka" (intransitive), and (c) idempotency guard
"Atmanepada_1_3_26" is absent from meta.  No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_26_akarmaka_Atmanepada"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get("Atmanepada_1_3_26"):
        return False
    return any(
        "dhatu" in t.tags and "akarmaka" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.meta["Atmanepada_1_3_26"] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.26",
    sutra_type=SutraType.VIDHI,
    text_slp1="akarmakAcca",
    text_dev="अकर्मकाच्च",
    padaccheda_dev="अकर्मकात् (पञ्चमी) / च",
    why_dev=(
        "अकर्मक-धातोः आत्मनेपदं भवति; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
