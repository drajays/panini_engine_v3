"""
3.4.81  लिटस्तझयोरेशिरेच्  —  VIDHI

In liṭ:
  - ātmanepada 3sg `ta` → `eS` (eŚ after IT-lopa = e)
  - ātmanepada 3pl `Ja` (jha) → `irec` (iReC after IT-lopa = ire)

Engine: recipe arms via ``state.meta['liT_esh_recipe']``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 34081 · लिटस्तझयोरेशिरेच्
              padaccheda: लिटः त-झयोः एश्-इरेच्
  Source #2 — Kāśikā 3.4.81 udāharaṇa:
                शकारः सर्वादेशार्थः
                चकारः स्वरार्थः
                पेचे
  Cross-check — surface pinned by: tests/unit/test_IDe_lit_indh.py
  Reference record: sutra_ref_out/3_4_81.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_ta_or_Ja(state: State):
    """Return (index, kind) where kind in {'ta', 'Ja'}."""
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "ta":
            return (i, "ta")
        if up == "Ja":
            return (i, "Ja")
    return None


_ESH = {"ta": "eS", "Ja": "irec"}


def _structural_site(state: State) -> int | None:
    """लिटस्तझयोरेशिरेच् read off the tape: an ātmanepada ta/jha ādeśa whose sthānī is liṭ."""
    for i, t in enumerate(state.terms):
        if (t.kind == "pratyaya" and "tin_adesha_3_4_78" in t.tags and "parasmaipada" not in t.tags
                and not t.meta.get("3_4_81_done")
                and (t.meta.get("source_lakara_upadesha") or "").strip() == "liT"
                and (t.meta.get("upadesha_slp1") or "").strip() in _ESH):
            return i
    return None


def cond(state: State) -> bool:
    if _structural_site(state) is not None:
        return True
    if not state.meta.get("lakara_liT"):
        return False
    if not state.meta.get("liT_esh_recipe"):
        return False
    return _find_ta_or_Ja(state) is not None


def act(state: State) -> State:
    if (i := _structural_site(state)) is not None:
        from engine.sthanivat import TING_PRATYAYATVA, adesha_substitute_varnas
        t = state.terms[i]
        adesha_substitute_varnas(t, _ESH[(t.meta.get("upadesha_slp1") or "").strip()], state, sutra_id="3.4.81",
                                 gunadharmas=frozenset({TING_PRATYAYATVA}))
        t.meta["3_4_81_done"] = True
        return state
    hit = _find_ta_or_Ja(state)
    if hit is None:
        return state
    ti, kind = hit
    pr = state.terms[ti]
    if kind == "ta":
        pr.varnas = list(parse_slp1_upadesha_sequence("eS"))
        pr.meta["upadesha_slp1"] = "eS"
    else:  # Ja → irec
        pr.varnas = list(parse_slp1_upadesha_sequence("irec"))
        pr.meta["upadesha_slp1"] = "irec"
    pr.tags.add("upadesha")
    state.meta["liT_esh_recipe"] = False
    state.meta["anekal_shit_recipe"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.81",
    sutra_type=SutraType.VIDHI,
    text_slp1='liwastaJayoreSirec',
    text_dev='लिटस्तझयोरेशिरेच्',
    padaccheda_dev="लिटः / त-झयोः / एशि-रेच्",
    why_dev="लिटि ‘त’ इत्यस्य ‘एश्’ आदेशः (ईधे)।",
    anuvritti_from=("3.4.78",),
    apavada_of            = ("3.4.79",),   # liṭ-specific eś/irec over the general ṭeḥ e
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

