"""
6.1.71  ह्रस्वस्य पिति कृति तुक्  —  VIDHI (narrow: insert t before ya of lyap)

Engine (narrow v3):
  For lyap outputs in ``split_prakriyas_11/P017.json`` we model *tuk* as insertion
  of a single ``t`` varṇa immediately before the ``ya`` residue (after it-lopa on
  ``lyap`` has yielded ``ya``).

Teaching **P041** (*agnicit*): *hrasva*-final *upapada* ``agni`` + *dhātu* ``ci``
(after *kvip* loss) → append ``t`` (*tuk*) to the ``ci`` ``Term`` (``P041_6_1_71_tuk_arm``).

This is intentionally narrow: it checks for a pratyaya term whose upadeśa was
``lyap`` and whose current phonetic tape begins with ``y``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import is_hrasva


def _find_site(state: State):
    if len(state.terms) < 2:
        return None
    dh = next((i for i, t in enumerate(state.terms) if "dhatu" in t.tags), None)
    if dh is None:
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "lyap":
            continue
        if t.meta.get("6_1_71_tuk_done"):
            continue
        if not t.varnas or t.varnas[0].slp1 != "y":
            continue
        return (i, 0)
    return None


def _find_p041_agnicit_tuk(state: State):
    if not state.meta.get("P041_6_1_71_tuk_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "P041_ci_dhatu" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "ci":
            continue
        if t.meta.get("6_1_71_P041_tuk_done"):
            continue
        if i == 0:
            return None
        prev = state.terms[i - 1]
        if not prev.varnas:
            return None
        pv = prev.varnas[-1]
        if not is_hrasva(pv.slp1):
            return None
        return i
    return None


def cond(state: State) -> bool:
    return _find_site(state) is not None or _find_p041_agnicit_tuk(state) is not None


def act(state: State) -> State:
    p041_i = _find_p041_agnicit_tuk(state)
    if p041_i is not None:
        t = state.terms[p041_i]
        t.varnas.append(mk("t"))
        t.meta["6_1_71_P041_tuk_done"] = True
        state.meta.pop("P041_6_1_71_tuk_arm", None)
        return state
    hit = _find_site(state)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas.insert(vi, mk("t"))
    state.terms[ti].meta["6_1_71_tuk_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.71",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "hrasvasya piti kfti tuk",
    text_dev       = "ह्रस्वस्य पिति कृति तुक्",
    padaccheda_dev = "ह्रस्वस्य / पिति / कृति / तुक्",
    why_dev        = "ल्यप्-प्रसङ्गे (… + य) पूर्वं तुक्-आगमः — P017 narrow demo.",
    anuvritti_from = ("6.1.68",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

