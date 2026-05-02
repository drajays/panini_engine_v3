"""
3.4.105  झस्य रन्  —  VIDHI (narrow: *vidhi-liṅ* *ātmanepada*)

Teaching **P038** (*paceran*): in the *vidhi-liṅ* frame, *tiṅ* *ādeśa* ``Ja`` is
replaced by ``ran`` (SLP1 ``r`` ``a`` ``n``).

Narrow: ``state.meta['P038_3_4_105_arm']`` + ``vidhi_liG`` + ``Ja`` *tiṅ* term.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_ja_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "Ja":
            continue
        if t.meta.get("P038_3_4_105_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("P038_3_4_105_arm"):
        return False
    if not state.meta.get("vidhi_liG"):
        return False
    return _find_ja_index(state) is not None


def act(state: State) -> State:
    idx = _find_ja_index(state)
    if idx is None:
        return state
    t = state.terms[idx]
    t.varnas = list(parse_slp1_upadesha_sequence("ran"))
    t.meta["upadesha_slp1"] = "ran"
    t.meta["P038_3_4_105_done"] = True
    state.meta.pop("P038_3_4_105_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.105",
    sutra_type=SutraType.VIDHI,
    text_slp1="Jasya ran",
    text_dev="झस्य रन्",
    padaccheda_dev="झस्य / रन्",
    why_dev="विधि-लिङि आत्मनेपदे झ-आदेशस्य स्थाने रन् (P038)।",
    anuvritti_from=("3.4.78",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
