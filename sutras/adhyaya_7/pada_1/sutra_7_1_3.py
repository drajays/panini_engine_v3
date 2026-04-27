"""
7.1.3  झोऽन्तः  —  VIDHI (narrow: *jhi* → *anti*)

Glass-box: when ``state.meta["7_1_3_jho_anta_arm"]`` is true and a *tiṅ* *ādeśa*
``Term`` has ``upadesha_slp1 == "jhi"`` with varṇa-shape *j* + *h* + *i* (initial
*jh* cluster in two *varṇa*s), replace that ``Term`` with *anti*.

*Cross-check:* ``sutrANi.tsv`` row 7.1.3; machine index i=71003.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_jhi(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "jhi":
            continue
        if len(t.varnas) != 3:
            continue
        v0, v1, v2 = t.varnas[0].slp1, t.varnas[1].slp1, t.varnas[2].slp1
        if v0 not in ("j", "J") or v1 != "h" or v2 != "i":
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("7_1_3_jho_anta_arm"):
        return False
    return _find_jhi(state) is not None


def act(state: State) -> State:
    idx = _find_jhi(state)
    if idx is None:
        return state
    old = state.terms[idx]
    anti = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("anti"),
        tags=set(old.tags),
        meta=dict(old.meta),
    )
    anti.meta["upadesha_slp1"] = "anti"
    state.terms[idx] = anti
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
