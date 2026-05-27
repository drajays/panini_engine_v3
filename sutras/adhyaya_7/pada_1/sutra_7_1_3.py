"""
7.1.3  झोऽन्तः  —  VIDHI

Replaces the jh (jha) sound with anta:
  • kartari (parasmai) laṭ/laṅ  jhi (j+h+i): jhi → anti
  • laṅ after 3.4.100 drops i   jh  (j+h):   jh  → ant
  • karmani (ātmanepada) 3pl:   Ja  (J single-char jha, after 3.4.79 → Je):
                                  Je  → ante   (J+rest → ant+rest)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_jh_term(state: State):
    """Return (index, kind) where kind in {'jhi','jh','Je'}."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        vs = t.varnas
        # Parasmai (kartari): upadesha jhi, varnas j+h+i or j+h
        if up == "jhi":
            if len(vs) == 3 and vs[0].slp1 in {"j","J"} and vs[1].slp1 == "h" and vs[2].slp1 == "i":
                return (i, "jhi")
            if len(vs) == 2 and vs[0].slp1 in {"j","J"} and vs[1].slp1 == "h":
                return (i, "jh")
        # Ātmanepada (karmani): upadesha Ja/Je (laT) or JAm (loṭ after 3.4.90), varnas start with J
        if len(vs) >= 1 and vs[0].slp1 == "J" and "tin_adesha_3_4_78" in t.tags:
            return (i, "Je")
    return None


def cond(state: State) -> bool:
    return _find_jh_term(state) is not None


def act(state: State) -> State:
    result = _find_jh_term(state)
    if result is None:
        return state
    idx, kind = result
    old = state.terms[idx]
    if kind == "jhi":
        new_slp1 = "anti"
        new_varnas = parse_slp1_upadesha_sequence("anti")
    elif kind == "jh":
        new_slp1 = "ant"
        new_varnas = parse_slp1_upadesha_sequence("ant")
    else:
        # karmani: J-initial term (Je after laT 3.4.79, or JAm after loṭ 3.4.90)
        # → replace J with [a,n,t], keep rest → ante or antAm
        new_varnas = parse_slp1_upadesha_sequence("ant") + list(old.varnas[1:])
        new_slp1 = "ant" + "".join(v.slp1 for v in old.varnas[1:])
    new_term = Term(
        kind="pratyaya",
        varnas=new_varnas,
        tags=set(old.tags),
        meta=dict(old.meta),
    )
    new_term.meta["upadesha_slp1"] = new_slp1
    new_term.tags.discard("upadesha")
    state.terms[idx] = new_term
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.3",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Jho antaH",
    text_dev       = "झोऽन्तः",
    padaccheda_dev = "झः / अन्तः",
    why_dev        = (
        "झि-प्रत्ययस्य झकारस्य अन्तादेशः → अन्ति (परस्मैपद); "
        "कर्मणि झ (J) → अन्त → झे (Je) के बाद अन्ते।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
