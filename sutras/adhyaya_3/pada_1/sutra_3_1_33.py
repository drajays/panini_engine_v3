"""
3.1.33  स्यतासी लृलुटोः  —  VIDHI (narrow)

Glass-box: under ``3_1_33_tasi_lut_arm``, insert the *tāsi* *vikaraṇa* shape
``t``-``A``-``s`` immediately before the *luṭ* *lac* placeholder ``Term``.

``cond`` is mechanically blind to *puruṣa* / *vacana* (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _p019_sy_insert_index(state: State) -> int | None:
    if not state.meta.get("corrected_v2_P019_3_1_33_sy_arm"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "vft":
            continue
        nxt = state.terms[i + 1]
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if up not in {"ti", "tip"}:
            continue
        if "".join(v.slp1 for v in nxt.varnas) != "ti":
            continue
        return i + 1
    return None


def _luT_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "luT" and "lakAra_pratyaya_placeholder" in t.tags:
            return i
    return None


def cond(state: State) -> bool:
    if (
        state.meta.get("corrected_v2_P019_3_1_33_sy_arm")
        and not state.meta.get("corrected_v2_P019_3_1_33_sy_done")
        and _p019_sy_insert_index(state) is not None
    ):
        return True
    if not state.meta.get("3_1_33_tasi_lut_arm"):
        return False
    if state.meta.get("3_1_33_tasi_lut_done"):
        return False
    return _luT_index(state) is not None


def act(state: State) -> State:
    j_sy = _p019_sy_insert_index(state)
    if j_sy is not None:
        sy = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("sy")),
            tags={"pratyaya", "vikarana", "ardhadhatuka"},
            meta={"upadesha_slp1": "sy"},
        )
        state.terms.insert(j_sy, sy)
        state.meta["corrected_v2_P019_3_1_33_sy_done"] = True
        state.meta.pop("corrected_v2_P019_3_1_33_sy_arm", None)
        return state
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
    why_dev        = "लुट्-परे तासि-आगमः; P019: लृङि ``sy``-विकरणः।",
    anuvritti_from = ("3.1.22",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
