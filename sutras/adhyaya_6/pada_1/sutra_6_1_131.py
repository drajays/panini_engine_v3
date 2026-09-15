"""
6.1.131  दिव उत्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=601131
- Kāśikā: "दिवो भ्याम्" (तृतीयाद्विवचनस्य भ्याम् प्रत्यये वकारस्य उ-आदेशः)
- Cross-validation: regression test tests/unit/test_sthanivat_al_ashrita_exceptions.py

*div* stem-final *v* → *u* (same locus); **1.1.56** does **not** extend *v*-antatva
onto the *u* ādeśa (*al*-vidhi at the substitution site).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.sthanivat import BLOCK_AL_SAME_SITE, mark_sthanivat_block
from phonology import mk


def _div_index(state: State) -> int | None:
    if state.meta.get("6_1_131_div_ut_done"):
        return None
    for i, t in enumerate(state.terms):
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up != "div" and [v.slp1 for v in t.varnas] != ["d", "i", "v"]:
            continue
        if not t.varnas or t.varnas[-1].slp1 != "v":
            continue
        if i + 1 >= len(state.terms):
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas:
            continue
        # *Byām* / *bhyām* class: initial *bh* / *B* in SLP1 upadeśa.
        if nxt.varnas[0].slp1 not in {"B", "b"}:
            if not state.meta.get("sthanivat_lesson_div_byam"):
                continue
        return i
    return None


def cond(state: State) -> bool:
    return _div_index(state) is not None


def act(state: State) -> State:
    i = _div_index(state)
    if i is None:
        return state
    left = state.terms[i]
    left.varnas = [mk("d"), mk("i")]
    left.meta["upadesha_slp1"] = "di"
    u = Term(
        kind="prakriti",
        varnas=[mk("u")],
        tags=set(left.tags),
        meta={
            "upadesha_slp1": "u",
            "6_1_131_residue_from_div": True,
            "vantatva_inhibited": True,
        },
    )
    mark_sthanivat_block(u, BLOCK_AL_SAME_SITE)
    state.terms.insert(i + 1, u)
    state.meta["6_1_131_div_ut_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.131",
    sutra_type=SutraType.VIDHI,
    text_slp1="diva ut",
    text_dev="दिव उत्",
    padaccheda_dev="दिवः उत्",
    why_dev="दिव्-अन्त्य-व्-स्थाने उ-आदेशः; वकारत्वम् उ-आदेशे न स्थानिवत्।",
    anuvritti_from=("6.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
