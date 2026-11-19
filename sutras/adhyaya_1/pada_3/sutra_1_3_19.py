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
Pāṭha: ashtadhyayi.com data.txt row i=13019 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.pada_ctx import decide, pada_site
from engine.state import State

# Module-level frozenset of prefix tags that trigger this rule.
_UPASARGAS: frozenset[str] = frozenset({"vi", "parA"})   # read off the tape (engine/pada_ctx.py); the recipe resolver lets this override 1.3.78

_DHATU_SLP1   = "ji"
_REGISTRY_KEY = "1_3_19_vi_parA_ji"
_STAMP_KEY    = "Atmanepada_1_3_19"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    return pada_site(state, frozenset({_DHATU_SLP1}), _UPASARGAS, _STAMP_KEY)


def act(state: State) -> State:
    return decide(state, "Atmanepada", _STAMP_KEY, _REGISTRY_KEY)


SUTRA = SutraRecord(
    sutra_id="1.3.19",
    sutra_type=SutraType.VIDHI,
    text_slp1='viparAByAM jeH',
    text_dev='विपराभ्यां जेः',
    samagra_slp1="vi-parAByAm jeH Atmanepadam",
    samagra_dev="वि-पराभ्याम् जेः आत्मनेपदम्",
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
