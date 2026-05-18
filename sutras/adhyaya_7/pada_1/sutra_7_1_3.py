"""
7.1.3  झोऽन्तः  —  VIDHI

Replaces the 'jh' sound with 'ant':
  • laṭ/laṅ path with jhi intact (3 varnas j+h+i):  jhi → anti
  • laṅ path after 3.4.100 drops 'i' (2 varnas j+h): jh  → ant

The jhi upadeśa tag is used to identify the target term in both cases.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_jhi(state: State) -> tuple[int, bool] | None:
    """Return (index, has_i) where has_i=True means jhi (3 varnas), False means jh (2 varnas)."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "jhi":
            continue
        vs = t.varnas
        if len(vs) == 3:
            v0, v1, v2 = vs[0].slp1, vs[1].slp1, vs[2].slp1
            if v0 in ("j", "J") and v1 == "h" and v2 == "i":
                return i, True
        elif len(vs) == 2:
            v0, v1 = vs[0].slp1, vs[1].slp1
            if v0 in ("j", "J") and v1 == "h":
                return i, False
    return None


def cond(state: State) -> bool:
    if not state.meta.get("7_1_3_jho_anta_arm"):
        return False
    return _find_jhi(state) is not None


def act(state: State) -> State:
    result = _find_jhi(state)
    if result is None:
        return state
    idx, has_i = result
    old = state.terms[idx]
    # jhi (has_i=True) → anti; jh (has_i=False, after 3.4.100) → ant
    new_slp1 = "anti" if has_i else "ant"
    new_term = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(new_slp1),
        tags=set(old.tags),
        meta=dict(old.meta),
    )
    new_term.meta["upadesha_slp1"] = new_slp1
    new_term.tags.discard("upadesha")  # prevent 1.3.3 re-firing on ant/anti finals
    state.terms[idx] = new_term
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.3",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Jho antaH",
    text_dev       = "झोऽन्तः",
    padaccheda_dev = "झः / अन्तः",
    why_dev        = "झि-प्रत्ययस्य झकारस्य अन्तादेशः → अन्ति (ग्लास-बॉक्स्)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
