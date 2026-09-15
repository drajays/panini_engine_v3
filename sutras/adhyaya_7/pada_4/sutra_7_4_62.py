"""
7.4.62  कुहोश्चुः  —  VIDHI (narrow demo)

Demo slice (जिघृक्षति):
  In the abhyāsa, replace initial guttural `g` (ku) with its corresponding
  palatal `j` (cu).

Teaching **P040** (*juhoti*): *abhyāsa* initial **h** (``hu``) → **j**
(``P040_juhoti_abhyasa`` + ``state.meta['P040_7_4_62_abhyasa_arm']``).

Engine: structural — abhyāsa initial guttural → palatal; P040 via `P040_juhoti_abhyasa` tag.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 74062 · कुहोश्चुः
              padaccheda: कु-होः चुः
              anuvṛtti:   64001: अङ्गस्य | 74058: अभ्यासस्य
  Source #2 — Kāśikā 7.4.62 udāharaṇa:
                चकार
                चखान
                जगाम
  Cross-check — surface pinned by: tests/unit/test_jakzatuH_lit_ad_gas.py, tests/unit/test_jiGfkSati_grah_san_desiderative.py, tests/unit/test_juhoti_hu_lat_tip_Slu.py
  Reference record: sutra_ref_out/7_4_62.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find_p014_k(state: State):
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_62_done"):
            continue
        if t.varnas and t.varnas[0].slp1 == "k":
            return ti
    return None


def _find_lit_ghas_abhyasa(state: State):
    """Structural *liṭ* *ghas*: *abhyāsa* initial *g*/*G* → *j*."""
    if not state.meta.get("lakara_liT"):
        return None
    if not state.meta.get("2_4_40_ad_to_gas"):
        return None
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_62_done"):
            continue
        if t.varnas and t.varnas[0].slp1 in {"g", "G"}:
            return ti
    return None


def _find(state: State):
    hit = _find_lit_ghas_abhyasa(state)
    if hit is not None:
        return hit
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_62_done"):
            continue
        if not t.varnas:
            continue
        # Initial guttural **g**/**G** in abhyāsa → palatal **j** (7.4.62 kuhoścuḥ).
        if t.varnas[0].slp1 in {"g", "G"}:
            return ti
    return None


def _find_p040_juhoti(state: State):
    """hu-abhyāsa h→j: structural via `P040_juhoti_abhyasa` tag."""
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if "P040_juhoti_abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_62_done"):
            continue
        if not t.varnas:
            continue
        if t.varnas[0].slp1 == "h":
            return ti
    return None


def cond(state: State) -> bool:
    return (
        _find_p014_k(state) is not None
        or _find(state) is not None
        or _find_p040_juhoti(state) is not None
    )


def act(state: State) -> State:
    ti_k = _find_p014_k(state)
    if ti_k is not None:
        t = state.terms[ti_k]
        t.varnas[0] = mk("c")
        t.meta["7_4_62_done"] = True
        return state
    ti_p = _find_p040_juhoti(state)
    if ti_p is not None:
        t = state.terms[ti_p]
        t.varnas[0] = mk("j")
        t.meta["7_4_62_done"] = True
        return state
    ti = _find(state)
    if ti is None:
        return state
    t = state.terms[ti]
    t.varnas[0] = mk("j")
    t.meta["7_4_62_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.62",
    sutra_type=SutraType.VIDHI,
    text_slp1="kuhoScuH (narrow)",
    text_dev="कुहोश्चुः",
    padaccheda_dev="कुहोः / चुः",
    why_dev="अभ्यासे कु-वर्णस्य चु-आदेशः (ग→ज; P014: क→च) — जिघृक्षति।",
    anuvritti_from=("7.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

