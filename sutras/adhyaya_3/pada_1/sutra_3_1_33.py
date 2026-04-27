"""
3.1.33  स्यतासी लृलुटोः  —  VIDHI (narrow)

Glass-box: under ``3_1_33_tasi_lut_arm``, insert the *tāsi* *vikaraṇa* shape
``t``-``A``-``s`` immediately before the *luṭ* *lac* placeholder ``Term``.

``cond`` is mechanically blind to *puruṣa* / *vacana* (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk


def _luT_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "luT" and "lakAra_pratyaya_placeholder" in t.tags:
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("3_1_33_tasi_lut_arm"):
        return False
    if state.meta.get("3_1_33_tasi_lut_done"):
        return False
    return _luT_index(state) is not None


def act(state: State) -> State:
    j = _luT_index(state)
    if j is None:
        return state
    t_as = Term(
        kind="pratyaya",
        varnas=[mk("t"), mk("A"), mk("s")],
        tags={"pratyaya", "ardhadhatuka"},
        meta={"upadesha_slp1": "tAs", "tAsi_vikaraṇa": True},
    )
    state.terms.insert(j, t_as)
    state.meta["3_1_33_tasi_lut_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.33",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "syatAsI lRluwoH",
    text_dev       = "स्यतासी लृलुटोः",
    padaccheda_dev = "स्य-तासी / लृ-लुटोः",
    why_dev        = "लुट्-परे तासि-आगमः (संकीर्ण-विधिः)।",
    anuvritti_from = ("3.1.22",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
