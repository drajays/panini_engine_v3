"""
1.3.16  इतरेतरान्योन्योपपदाच्च  —  VIDHI

*Padaccheda:* *itaretara-anyonya-upapada* (षष्ठी-तत्पुरुष) / *ca* (अव्यय).

*Anuvṛtti:* ātmanepada from 1.3.12, 1.3.14.

*Content:* And [ātmanepada] when itaretara (mutual/each-other) or anyonya
(one-another) is the upapada (associated word/context).  Reciprocal
pronoun context → ātmanepada.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term carries "itaretara_usage" or "anyonya_usage" (set by the
recipe to signal reciprocal construction), and (c) the idempotency stamp
"Atmanepada_1_3_16" is absent from state.meta.  No arm flags (CONSTITUTION
Art. 13).  r1_form_identity_exempt=True because no surface phonological
change occurs.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset of usage tags that signal a reciprocal construction.
_RECIPROCAL_USAGE_TAGS: frozenset[str] = frozenset({
    "itaretara_usage",
    "anyonya_usage",
})

_REGISTRY_KEY = "1_3_16_itaretara"
_STAMP_KEY    = "Atmanepada_1_3_16"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags and not _RECIPROCAL_USAGE_TAGS.isdisjoint(t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]    = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.16",
    sutra_type=SutraType.VIDHI,
    text_slp1="itaretara-anyonyopapAdAc ca",
    text_dev="इतरेतरान्योन्योपपदाच्च",
    padaccheda_dev="इतरेतर-अन्योन्य-उपपदात् (षष्ठी) / च (अव्यय)",
    why_dev=(
        "इतरेतर-अन्योन्य-उपेतोक्ते प्रयोगे परस्परक्रिया-बोधकत्वात् "
        "आत्मनेपदम् — १.३.१२, १.३.१४ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.14"),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
