"""
7.3.83  जुसि च  —  VIDHI

Padaccheda: जुसि च

जुसि च (7.3.83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_83_jusi_83"
_GUNA = {"i": "e", "I": "e", "u": "o", "U": "o"}


def _site(state: State):
    """जुसि च: before jus (jhi→jus, 3.4.108/109) the aṅga's final ik takes guṇa although jus is ṅit-like: abiBayuH."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or not t.varnas or t.meta.get("7_3_83_guna_done"):
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None or (nxt.meta.get("upadesha_slp1") or "").strip() != "jus":
            continue
        if t.varnas[-1].slp1 in "iIuUfFx":
            return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    from phonology import mk
    t = state.terms[i]
    last = t.varnas[-1].slp1
    if last in _GUNA:
        t.varnas[-1] = mk(_GUNA[last])
    else:                                     # ṛ/ṝ/ḷ: a + r/l (1.1.51)
        t.varnas[-1:] = [mk("a"), mk("r" if last in "fF" else "l")]
    t.meta["7_3_83_guna_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.83",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "jusi ca",
    text_dev              = "जुसि च",
    padaccheda_dev        = "जुसि च",
    why_dev               = "(सूत्रम् 7.3.83) जुसि च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
