"""
6.4.25  दंशसञ्जस्वञ्जां शपि  —  VIDHI

Before śap the nasal of दंश्, सञ्ज्, स्वञ्ज् drops — दशति, सजति, स्वजते (KV/SK §43: "दंशसञ्जस्वञ्जां शपि").
Sources: ashtadhyayi.com data row 64025; Kāśikā 6.4.25.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_ROOTS = frozenset({"daMSa~", "zaYja~", "zvaYja~"})
_NASAL = frozenset("nNYmM")


def _site(state: State):
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("6_4_25_done"):
            continue
        if (dh.meta.get("upadesha_slp1") or "").strip() not in _ROOTS:
            continue
        if len(dh.varnas) < 3 or dh.varnas[-2].slp1 not in _NASAL:
            continue
        if any((u.meta.get("upadesha_slp1") or "").strip() == "Sap" for u in state.terms[i + 1:]):
            return dh
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    dh = _site(state)
    if dh is not None:
        del dh.varnas[-2]
        dh.meta["6_4_25_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.25",
    sutra_type=SutraType.VIDHI,
    text_slp1="daMSasaYjasvaYjAM Sapi",
    text_dev="दंशसञ्जस्वञ्जां शपि",
    padaccheda_dev="दंश-सञ्ज-स्वञ्जाम् शपि",
    why_dev="शपि दंश्-सञ्ज्-स्वञ्जां नलोपः (दशति, सजति)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
