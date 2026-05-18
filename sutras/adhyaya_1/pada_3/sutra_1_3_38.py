"""
1.3.38  वृत्तिसर्गतायनेषु क्रमः  —  VIDHI

*Padaccheda:* *vṛtti-sarga-tāyaneṣu* (सप्तमी-बहुवचन) / *kramaḥ* (प्रथमा-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for kram (to step) in the senses of vṛtti
(livelihood), sarga (creation/emission/flow), and tāyana (moving/going).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term has upadesha_slp1 in {"kram","kramu~"} and carries at least
one tag from _KRAM_USAGES, and (c) the idempotency stamp
"Atmanepada_1_3_38" is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_KRAM_ROOTS: frozenset[str] = frozenset({"kram", "kramu~"})
_KRAM_USAGES: frozenset[str] = frozenset({"vftti_usage", "sarga_usage", "tAyana_usage"})

_REGISTRY_KEY = "1_3_38_kram_usages"
_STAMP_KEY    = "Atmanepada_1_3_38"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _KRAM_ROOTS
        and not _KRAM_USAGES.isdisjoint(t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.38",
    sutra_type=SutraType.VIDHI,
    text_slp1="vfttisar gatAyaneSu kramaH",
    text_dev="वृत्तिसर्गतायनेषु क्रमः",
    padaccheda_dev="वृत्ति-सर्ग-तायनेषु (सप्तमी-बहुवचन) / क्रमः (प्रथमा-एकवचन)",
    why_dev=(
        "वृत्ति-सर्ग-तायन-अर्थेषु क्रम्-धातोः प्रयोगे आत्मनेपदम् — "
        "kramate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
