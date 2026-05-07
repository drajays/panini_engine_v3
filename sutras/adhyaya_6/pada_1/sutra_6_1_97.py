"""
6.1.97  अतो गुणे  —  VIDHI

Operational role (v3.7, tyadādi pronouns like तद्):
  After 7.2.102 makes a final 'a', the aṅga may contain adjacent 'a' + 'a'
  at its tail (e.g. tad → t a a). This rule performs pararūpa-style
  ekādeśa by removing the first of the two identical 'a' sounds.

We implement narrowly:
  - only when aṅga is tagged `tyadadi`
  - find consecutive 'a''a' inside the aṅga and delete the earlier one

**P013** (*śuśrūṣate*): ``corrected_v2_P013_6_1_97_arm`` — same *pararūpa* on the
merged *pada* ``Term`` (``śap`` ``a`` + ``a`` from *tiṅ*).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

_META_P013 = "corrected_v2_P013_6_1_97_arm"
_META_P017_PAR = "corrected_v2_P017_6_1_97_pararupa_arm"


def _find_p017_pararupa(state: State) -> bool:
    """
    **P017**: ``pawat`` + ``pawat`` + ``qAc`` → single **``pawapawat``** before *it*
    on डाच् (*pararūpa* bundle step; **6.1.97** anchor in engine).
    """
    if not state.meta.get(_META_P017_PAR):
        return False
    if len(state.terms) != 3:
        return False
    t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
    if t0.meta.get("p017_pararupa_done"):
        return False
    f0 = "".join(v.slp1 for v in t0.varnas)
    f1 = "".join(v.slp1 for v in t1.varnas)
    if f0 != "pawat" or f1 != "pawat":
        return False
    if (t2.meta.get("upadesha_slp1") or "").strip() != "qAc":
        return False
    return True


def _find_tyadadi(state: State) -> tuple[int, int] | None:
    if not state.terms:
        return None
    anga = state.terms[0]
    if "anga" not in anga.tags or "tyadadi" not in anga.tags:
        return None
    if anga.meta.get("ato_gune_pararupa_done"):
        return None
    for i in range(len(anga.varnas) - 1):
        if anga.varnas[i].slp1 == "a" and anga.varnas[i + 1].slp1 == "a":
            return (0, i)
    return None


def _find_p013(state: State) -> tuple[int, int] | None:
    if not state.meta.get(_META_P013):
        return None
    for ti, t in enumerate(state.terms):
        if "pada" not in t.tags and "anga" not in t.tags:
            continue
        if t.meta.get("ato_gune_pararupa_done"):
            continue
        for i in range(len(t.varnas) - 1):
            if t.varnas[i].slp1 == "a" and t.varnas[i + 1].slp1 == "a":
                return (ti, i)
    return None


def _find_pair(state: State) -> tuple[int, int] | None:
    hit = _find_p013(state)
    if hit is not None:
        return hit
    return _find_tyadadi(state)


def cond(state: State) -> bool:
    if _find_p017_pararupa(state):
        return True
    return _find_pair(state) is not None


def act(state: State) -> State:
    if _find_p017_pararupa(state):
        t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
        merged = Term(
            kind="prakriti",
            varnas=list(t0.varnas[:-1]) + list(t1.varnas),
            tags=set(t0.tags) | {"anga", "prātipadika"},
            meta=dict(t0.meta),
        )
        merged.meta["p017_pararupa_done"] = True
        state.terms = [merged, t2]
        state.meta.pop(_META_P017_PAR, None)
        return state
    hit = _find_pair(state)
    if hit is None:
        return state
    ti, i = hit
    anga = state.terms[ti]
    del anga.varnas[i]
    anga.meta["ato_gune_pararupa_done"] = True
    state.meta.pop(_META_P013, None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.97",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ataH guRe",
    text_dev       = "अतो गुणे",
    padaccheda_dev = "अतः गुणे",
    why_dev        = "त्यदादि-शब्देषु अकार-द्वय-संयोगे पर-रूप-एकादेशः (त + अ + अ → त + अ)।",
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

