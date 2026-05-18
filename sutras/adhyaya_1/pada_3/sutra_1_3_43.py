"""
1.3.43  अनुपसर्गाद्वा  —  VIBHASHA

*Padaccheda:* *anupasargāt* (पञ्चमी-एकवचन) / *vā* (अव्यय).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* Without a prefix (anupasarga), optionally (vā) [ātmanepada
applies]. That is, when no upasarga (verbal prefix) precedes the root,
ātmanepada is optionally available.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) no dhātu
Term has any tag ending in "_prefix" (i.e., the root bears no upasarga),
and (c) the idempotency stamp "Atmanepada_vibhASA_1_3_43" is absent from
state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
vibhasha_default=True: the optional form is taken by default.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_43_anupasarga_vibhASA"
_STAMP_KEY    = "Atmanepada_vibhASA_1_3_43"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    # "anupasarga" = no tag ending in "_prefix" on any dhātu term
    return any(
        "dhatu" in t.tags
        and not any(tag for tag in t.tags if tag.endswith("_prefix"))
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.43",
    sutra_type=SutraType.VIBHASHA,
    vibhasha_default=True,
    text_slp1="anupasargAd vA",
    text_dev="अनुपसर्गाद्वा",
    padaccheda_dev="अनुपसर्गात् (पञ्चमी-एकवचन) / वा (अव्यय)",
    why_dev=(
        "उपसर्गरहितस्य धातोः प्रयोगे वा आत्मनेपदम् — "
        "अनुपसर्गाद् इति अनुपसर्गपूर्वकस्य विभाषा; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
