"""
3.2.176  रदादिभ्यो वरच्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=302176
- Kāśikā: रदादिभ्यो वरच् (यायावरः — यङन्तात् कर्तृ-कृदन्तम्)
- Cross-validation: tests/unit/test_yAyAvaraH_yang_varac.py,
  tests/unit/test_yAyAvar_yang_varac_purvavidhau_lesson.py

After the *yaṅ* *abhyāsa* frame, attach *kṛt* *varac* (surface *vara*), tagged
*kṅiti* (``c`` *it*) for downstream **6.4.64** / **1.3** chains.
``state.meta['varac_recipe']`` arms append of upadeśa ``varac``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("varac_recipe"):
        return False
    return not any((t.meta.get("upadesha_slp1") or "").strip() == "varac" for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    varac = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("varac")),
        tags={"pratyaya", "krt", "upadesha", "kngiti"},
        meta={"upadesha_slp1": "varac", "it_markers": {"c"}},
    )
    state.terms.append(varac)
    state.meta.pop("varac_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.176",
    sutra_type=SutraType.VIDHI,
    text_slp1="rad-Adibhyo varac",
    text_dev="रदादिभ्यो वरच्",
    padaccheda_dev="रदादिभ्यः / वरच्",
    why_dev="इत्यादेभ्यो वरच् — प०२९ (*यायावर*)।",
    anuvritti_from=("3.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
