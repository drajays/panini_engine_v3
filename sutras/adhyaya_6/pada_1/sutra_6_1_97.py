"""
6.1.97  अतो गुणे  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=60197
- Kāśikā: अतो गुणे — गुणे पररूपम् (एकादेशः) यत्र अकारो द्विर्वर्तते।
- Cross-validation: regression tests/unit/test_corrected_prakriyas_v2_bundle.py
  (P013 SuSrUzate, P017 pawapawAyati); pipelines/asmad_subanta.py paradigm cells.

Operational role (v3):
  *Pararūpa* / ekādeśa when consecutive ``a`` (or ``a``+``e`` at tiṅ junction)
  meets the guṇa-context constraints — no ``state.meta[..._arm]`` gates.

Contexts (structural ``cond`` only):
  - **P017** (*āmreḍita*): two ``pawat`` stems + ``qAc`` pratyaya on tape.
  - **Tiṅanta pre-merge**: ``vikarana``-tagged term final ``a`` + next term
    initial ``a``/``e`` (kartari/karmaṇi 3pl, etc.).
  - **Post-merge pada**: single ``pada`` Term with internal ``a``+``a`` (P013).
  - **Asmad intra-stem**: aṅga with ``7_2_*_done`` or ``asmad_stem``, consecutive ``a``+``a``.
  - **Asmad cross-term**: aṅga-final ``a`` + pratyaya-initial ``a`` after intra
    pass (intra checked first in ``cond`` order).
  - **Tyadādi**: aṅga tagged ``tyadadi``, consecutive ``a``+``a`` (तद् spine).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

_ASMAD_DONE_TAGS = frozenset({
    "7_2_94_done", "7_2_92_done", "7_2_93_done",
    "7_2_95_done", "7_2_96_done",
})


def _is_asmad_anga(term: Term) -> bool:
    """Asmad aṅga: stem-change done and/or ``asmad_stem`` from ``asmad_subanta``."""
    if "anga" not in term.tags:
        return False
    return bool(term.tags & _ASMAD_DONE_TAGS) or "asmad_stem" in term.tags


def _find_p017_pararupa(state: State) -> bool:
    """P017: ``pawat`` + ``pawat`` + ``qAc`` → ``pawapawat`` before *it* lopa."""
    if len(state.terms) != 3:
        return False
    t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
    if t0.meta.get("p017_pararupa_done"):
        return False
    f0 = "".join(v.slp1 for v in t0.varnas)
    f1 = "".join(v.slp1 for v in t1.varnas)
    if f0 != "pawat" or f1 != "pawat":
        return False
    return (t2.meta.get("upadesha_slp1") or "").strip() == "qAc"


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


def _find_merged_pada_pararupa(state: State) -> tuple[int, int] | None:
    """Post-``_pada_merge``: internal ``a``+``a`` on one ``pada`` Term (P013 spine)."""
    if any("vikarana" in t.tags for t in state.terms):
        return None
    for ti, t in enumerate(state.terms):
        if "pada" not in t.tags:
            continue
        if t.meta.get("ato_gune_pararupa_done"):
            continue
        if "tyadadi" in t.tags:
            continue
        if _is_asmad_anga(t):
            continue
        for i in range(len(t.varnas) - 1):
            if t.varnas[i].slp1 == "a" and t.varnas[i + 1].slp1 == "a":
                return (ti, i)
    return None


def _find_tinganta_cross(state: State) -> int | None:
    """
    Pre-merge tiṅanta: ``vikarana``-final ``a`` + tiṅ-initial ``a``/``e``.
    """
    for i in range(len(state.terms) - 1):
        t1 = state.terms[i]
        t2 = state.terms[i + 1]
        if "vikarana" not in t1.tags:
            continue
        if not t1.varnas or not t2.varnas:
            continue
        if t1.varnas[-1].slp1 != "a":
            continue
        if t2.varnas[0].slp1 not in {"a", "e"}:
            continue
        if t1.meta.get("6_1_97_tinganta_done"):
            continue
        return i
    return None


def _find_asmad_consecutive_a(state: State) -> tuple[int, int] | None:
    for ti, t in enumerate(state.terms):
        if not _is_asmad_anga(t):
            continue
        if t.meta.get("asmad_ato_gune_done"):
            continue
        for i in range(len(t.varnas) - 1):
            if t.varnas[i].slp1 == "a" and t.varnas[i + 1].slp1 == "a":
                return (ti, i)
    return None


def _find_asmad_crossterm(state: State) -> int | None:
    """
    Cross-term asmad: stem-final ``a`` + pratyaya-initial ``a``.
    Defers while intra-stem ``a``+``a`` is still pending.
    """
    if _find_asmad_consecutive_a(state) is not None:
        return None
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        t1 = state.terms[i]
        t2 = state.terms[i + 1]
        if not _is_asmad_anga(t1):
            continue
        if not t1.varnas or not t2.varnas:
            continue
        if t1.varnas[-1].slp1 != "a":
            continue
        if t2.varnas[0].slp1 != "a":
            continue
        if t1.meta.get("6_1_97_crossterm_done"):
            continue
        return i
    return None


def _find_pair(state: State) -> tuple[int, int] | None:
    hit = _find_merged_pada_pararupa(state)
    if hit is not None:
        return hit
    hit2 = _find_asmad_consecutive_a(state)
    if hit2 is not None:
        return hit2
    return _find_tyadadi(state)


def cond(state: State) -> bool:
    if _find_p017_pararupa(state):
        return True
    if _find_tinganta_cross(state) is not None:
        return True
    if _find_pair(state) is not None:
        return True
    return _find_asmad_crossterm(state) is not None


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
        return state
    i = _find_tinganta_cross(state)
    if i is not None:
        del state.terms[i].varnas[-1]
        state.terms[i].meta["6_1_97_tinganta_done"] = True
        state.samjna_registry["6_1_97_tinganta_pararupa"] = True
        return state
    asmad_hit = _find_asmad_consecutive_a(state)
    if asmad_hit is not None:
        ti, vi = asmad_hit
        anga = state.terms[ti]
        del anga.varnas[vi]
        anga.meta["asmad_ato_gune_done"] = True
        anga.meta["ato_gune_pararupa_done"] = True
        state.samjna_registry["6_1_97_asmad_pararupa"] = True
        return state
    hit = _find_pair(state)
    if hit is not None:
        ti, vi = hit
        anga = state.terms[ti]
        del anga.varnas[vi]
        anga.meta["ato_gune_pararupa_done"] = True
        return state
    ct_hit = _find_asmad_crossterm(state)
    if ct_hit is not None:
        anga = state.terms[ct_hit]
        del anga.varnas[-1]
        anga.meta["6_1_97_crossterm_done"] = True
        state.samjna_registry["6_1_97_asmad_crossterm_pararupa"] = True
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.97",
    sutra_type=SutraType.VIDHI,
    text_slp1="ataH guRe",
    text_dev="अतो गुणे",
    padaccheda_dev="अतः गुणे",
    why_dev="गुणे पररूप-एकादेशः — अकार-द्वय-संयोगे प्रथमम् अकारं लोपयति।",
    anuvritti_from=("6.1.84",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
