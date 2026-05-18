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
_META_TINGANTA = "6_1_97_tinganta_arm"
_META_ASMAD_CROSSTERM = "6_1_97_asmad_crossterm_arm"


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


def _find_tinganta_cross(state: State) -> int | None:
    """
    Tiṅanta context: cross-term `a`(vikaraṇa-final) + `a`(tiṅ-initial) junction.
    Returns index i of the left term (vikaraṇa) whose final `a` is to be deleted.
    Fires after 7.1.3 transforms jhi → anti; the vikaraṇa `a` elides before `a` of anti.
    """
    if not state.meta.get(_META_TINGANTA):
        return None
    for i in range(len(state.terms) - 1):
        t1 = state.terms[i]
        t2 = state.terms[i + 1]
        if not t1.varnas or not t2.varnas:
            continue
        if t1.varnas[-1].slp1 != "a":
            continue
        if t2.varnas[0].slp1 != "a":
            continue
        if t1.meta.get("6_1_97_tinganta_done"):
            continue
        return i
    return None


def _find_asmad_consecutive_a(state: State) -> tuple[int, int] | None:
    """
    Asmad case: after any of the stem-change rules (7.2.94, 7.2.92, 7.2.93,
    7.2.95, 7.2.96), the stem contains consecutive [a, a] from the junction of
    the replacement string and the remaining stem. Find the first such pair
    and return (term_idx, varna_idx_of_first_a).

    Eligible done tags (any one suffices):
      "7_2_94_done", "7_2_92_done", "7_2_93_done", "7_2_95_done", "7_2_96_done"
    Only fires when stem has not yet "asmad_ato_gune_done".
    """
    _ASMAD_DONE_TAGS = {
        "7_2_94_done", "7_2_92_done", "7_2_93_done",
        "7_2_95_done", "7_2_96_done",
    }
    for ti, t in enumerate(state.terms):
        if not (t.tags & _ASMAD_DONE_TAGS):
            continue
        if "anga" not in t.tags:
            continue
        if t.meta.get("asmad_ato_gune_done"):
            continue
        for i in range(len(t.varnas) - 1):
            if t.varnas[i].slp1 == "a" and t.varnas[i + 1].slp1 == "a":
                return (ti, i)
    return None


def _find_asmad_crossterm(state: State) -> int | None:
    """
    Cross-term asmad boundary: stem-final 'a' + pratyaya-initial 'a'.
    Fires when arm flag "_META_ASMAD_CROSSTERM" is set.
    Deletes the stem-final 'a' (pararūpa: keep the pratyaya-initial 'a').
    Returns the stem term index, or None.
    """
    if not state.meta.get(_META_ASMAD_CROSSTERM):
        return None
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        t1 = state.terms[i]
        t2 = state.terms[i + 1]
        if "anga" not in t1.tags:
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
    hit = _find_p013(state)
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
    if _find_asmad_crossterm(state) is not None:
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
    i = _find_tinganta_cross(state)
    if i is not None:
        del state.terms[i].varnas[-1]
        state.terms[i].meta["6_1_97_tinganta_done"] = True
        state.meta.pop(_META_TINGANTA, None)
        state.samjna_registry["6_1_97_tinganta_pararupa"] = True
        return state
    # Asmad cross-term boundary: stem-a + pratyaya-a → delete stem-final a
    ct_hit = _find_asmad_crossterm(state)
    if ct_hit is not None:
        anga = state.terms[ct_hit]
        del anga.varnas[-1]
        anga.meta["6_1_97_crossterm_done"] = True
        state.meta.pop(_META_ASMAD_CROSSTERM, None)
        state.samjna_registry["6_1_97_asmad_crossterm_pararupa"] = True
        return state

    # Asmad case: check before generic pair
    asmad_hit = _find_asmad_consecutive_a(state)
    if asmad_hit is not None:
        ti, i = asmad_hit
        anga = state.terms[ti]
        del anga.varnas[i]
        anga.meta["asmad_ato_gune_done"] = True
        anga.meta["ato_gune_pararupa_done"] = True
        state.samjna_registry["6_1_97_asmad_pararupa"] = True
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

