"""
1.3.41  वेः पादविहरणे  —  VIDHI

*Padaccheda:* *veḥ* (पञ्चमी-एकवचन) / *pādaviharaṇe* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for [i / go with prefix vi] in the sense of
pādaviharaṇa (walking / foot movement). For example: viharate — he
walks about (with the feet).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term carries the tag "vi_prefix" and the tag
"pAdaviharaNa_usage", and (c) the idempotency stamp "Atmanepada_1_3_41"
is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_41_vi_pAdaviharaNa"
_STAMP_KEY    = "Atmanepada_1_3_41"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and "vi_prefix" in t.tags
        and "pAdaviharaNa_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.41",
    sutra_type=SutraType.VIDHI,
    text_slp1="veH pAdaviharaNe",
    text_dev="वेः पादविहरणे",
    padaccheda_dev="वेः (पञ्चमी-एकवचन) / पादविहरणे (सप्तमी-एकवचन)",
    why_dev=(
        "वि-पूर्वकस्य धातोः पादविहरण-अर्थे प्रयोगे आत्मनेपदम् — "
        "viharate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
