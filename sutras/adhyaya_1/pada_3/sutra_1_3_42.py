"""
1.3.42  प्रोपाभ्यां समर्थाभ्याम्  —  VIDHI

*Padaccheda:* *pra-upābhyām* (पञ्चमी-द्विवचन) / *samarthābhyām* (पञ्चमी-द्विवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for [roots] after pra or upa when both prefix and
root are meaningfully conjoined (samarthābhyām / used together with full
semantic force). For example: prakramate, upakramate.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term carries one of _PROPA_PREFIXES and also carries the tag
"samarTa_usage", and (c) the idempotency stamp "Atmanepada_1_3_42" is
absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_PROPA_PREFIXES: frozenset[str] = frozenset({"pra_prefix", "upa_prefix"})

_REGISTRY_KEY = "1_3_42_pra_upa_samarTA"
_STAMP_KEY    = "Atmanepada_1_3_42"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and not _PROPA_PREFIXES.isdisjoint(t.tags)
        and "samarTa_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.42",
    sutra_type=SutraType.VIDHI,
    text_slp1="propAByAM samArTAByAm",
    text_dev="प्रोपाभ्यां समर्थाभ्याम्",
    padaccheda_dev="प्र-उपाभ्याम् (पञ्चमी-द्विवचन) / समर्थाभ्याम् (पञ्चमी-द्विवचन)",
    why_dev=(
        "प्र-पूर्वकस्य वा उप-पूर्वकस्य धातोः समर्थ-प्रयोगे आत्मनेपदम् — "
        "prakramate, upakramate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
