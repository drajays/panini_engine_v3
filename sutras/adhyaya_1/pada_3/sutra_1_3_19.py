"""
1.3.19  विपराभ्यां जेः  —  VIDHI

*Padaccheda:* *vi-parā-ābhyām* (पञ्चमी-द्विवचन) / *jeḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for the dhātu ji (to conquer/win) when preceded by
the prefix vi or parā (e.g. vijayate, parājayate).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term has upadesha_slp1 == "ji" and carries at least one of the
prefix tags in _VI_PARA_PREFIXES, and (c) the idempotency stamp
"Atmanepada_1_3_19" is absent from state.meta.  No arm flags (CONSTITUTION
Art. 13).  r1_form_identity_exempt=True because no surface phonological
change occurs.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset of prefix tags that trigger this rule.
_VI_PARA_PREFIXES: frozenset[str] = frozenset({
    "vi_prefix",
    "parA_prefix",
})

_DHATU_SLP1   = "ji"
_REGISTRY_KEY = "1_3_19_vi_parA_ji"
_STAMP_KEY    = "Atmanepada_1_3_19"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() == _DHATU_SLP1
        and not _VI_PARA_PREFIXES.isdisjoint(t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.19",
    sutra_type=SutraType.VIDHI,
    text_slp1="vi-parAByAM jeH",
    text_dev="विपराभ्यां जेः",
    padaccheda_dev="वि-पराभ्याम् (पञ्चमी-द्विवचन) / जेः (षष्ठी)",
    why_dev=(
        "वि-, परा-पूर्वस्य जि-धातोः प्रयोगे आत्मनेपदम् — "
        "vijayate, parājayate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
