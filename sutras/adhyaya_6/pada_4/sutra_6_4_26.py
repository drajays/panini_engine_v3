"""
6.4.26  रञ्जेश्च  —  VIDHI

Before śap the nasal of रञ्ज् drops — रजति, रजते (not before kit liṭ: ररञ्जे) (KV/SK §43: "रञ्जेश्च").
Sources: ashtadhyayi.com data row 64026; Kāśikā 6.4.26.
Pāṭha: ashtadhyayi.com data.txt row i=64026 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_ROOTS = frozenset({"ranja~"})
_NASAL = frozenset("nNYmM")


def _site(state: State):
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("6_4_26_done"):
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
        dh.meta["6_4_26_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.26",
    sutra_type=SutraType.VIDHI,
    text_slp1="ranjeS ca",
    text_dev="रञ्जेश्च",
    samagra_slp1="raYjeH aNgasya upaDAyAH Sapi nalopaH",
    samagra_dev="रञ्जेः अङ्गस्य उपधायाः शपि नलोपः",
    padaccheda_dev="रञ्जेः च",
    why_dev="शपि रञ्जेर्नलोपः (रजति)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
