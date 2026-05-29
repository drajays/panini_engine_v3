"""
3.1.33  स्यतासी लृलुटोः  —  VIDHI (narrow)

Glass-box paths:
  • ``3_1_33_lrt_sy_arm``: lṛṭ — insert *sya* vikaraṇa (s+y+a) after the
    dhātu, before the tiṅ ādeśa.  The final 'a' is the inherent vowel of 'ya'
    and is essential for 7.3.101 (ato dīrgho yañi) in uttama forms.
  • ``tasi_luT_recipe``: luṭ — insert *tāsi* vikaraṇa before luṭ placeholder.
  • ``luN_sy_recipe``: luṅ P019 — insert *sy* (no 'a') before
    existing 'ti' in the *vṛt* context.

``cond`` is mechanically blind to *puruṣa* / *vacana* (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _lrng_ṛ_sy_insert_index(state: State) -> int | None:
    """Lṛṅ + ṛ-dhātu (``vft``) + following ``ti`` ādeśa: insert ``sy`` (not ``sya``)."""
    if (state.meta.get("lakara") or "").strip() != "lRG":
        return None
    if state.meta.get("lrng_ṛ_sy_done"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if not any(v.slp1 == "f" for v in t.varnas):
            continue
        nxt = state.terms[i + 1]
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if up not in {"ti", "tip"}:
            continue
        if "".join(v.slp1 for v in nxt.varnas) != "ti":
            continue
        return i + 1
    return None


def _p019_sy_insert_index(state: State) -> int | None:
    if not state.meta.get("luN_sy_recipe"):
        return None
    return _lrng_ṛ_sy_insert_index(state)


def _luT_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "luT" and "lakAra_pratyaya_placeholder" in t.tags:
            return i
    return None


def _lrt_dhatu_index(state: State) -> int | None:
    """For lṛṭ: find dhātu position to insert *sya* immediately after it."""
    if not state.meta.get("3_1_33_lrt_sy_arm"):
        return None
    if state.meta.get("3_1_33_lrt_sy_done"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i + 1
    return None


def _lRG_dhatu_index(state: State) -> int | None:
    """For lṛṅ: find dhātu position to insert *sya* immediately after it."""
    if not state.meta.get("3_1_33_lRG_sy_arm"):
        return None
    if state.meta.get("3_1_33_lRG_sy_done"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i + 1
    return None


def cond(state: State) -> bool:
    if _lrng_ṛ_sy_insert_index(state) is not None:
        return True
    if (
        not state.meta.get("luN_sy_done")
        and _p019_sy_insert_index(state) is not None
    ):
        return True
    if _lrt_dhatu_index(state) is not None:
        return True
    if _lRG_dhatu_index(state) is not None:
        return True
    if not state.meta.get("tasi_luT_recipe"):
        return False
    if state.meta.get("3_1_33_tasi_lut_done"):
        return False
    return _luT_index(state) is not None


def act(state: State) -> State:
    j_ṛ = _lrng_ṛ_sy_insert_index(state)
    if j_ṛ is not None:
        sy = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("sy")),
            tags={"pratyaya", "vikarana", "ardhadhatuka"},
            meta={"upadesha_slp1": "sy"},
        )
        state.terms.insert(j_ṛ, sy)
        state.meta["lrng_ṛ_sy_done"] = True
        state.meta.pop("luN_sy_recipe", None)
        state.meta.pop("luN_sy_done", None)
        return state
    j_sy = _p019_sy_insert_index(state)
    if j_sy is not None:
        sy = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("sy")),
            tags={"pratyaya", "vikarana", "ardhadhatuka"},
            meta={"upadesha_slp1": "sy"},
        )
        state.terms.insert(j_sy, sy)
        state.meta["luN_sy_done"] = True
        return state
    j_lrt = _lrt_dhatu_index(state)
    if j_lrt is not None:
        sya = Term(
            kind="pratyaya",
            varnas=[mk("s"), mk("y"), mk("a")],
            tags={"pratyaya", "vikarana", "upadesha"},
            meta={"upadesha_slp1": "sya", "lrt_vikarana": True},
        )
        state.terms.insert(j_lrt, sya)
        state.meta["3_1_33_lrt_sy_done"] = True
        state.meta.pop("3_1_33_lrt_sy_arm", None)
        return state
    j_lRG = _lRG_dhatu_index(state)
    if j_lRG is not None:
        # lṛṅ vikaraṇa 'sya': same as lṛṭ but tagged lRG_vikarana for 3.4.114.
        sya = Term(
            kind="pratyaya",
            varnas=[mk("s"), mk("y"), mk("a")],
            tags={"pratyaya", "vikarana", "upadesha"},
            meta={"upadesha_slp1": "sya", "lRG_vikarana": True},
        )
        state.terms.insert(j_lRG, sya)
        state.meta["3_1_33_lRG_sy_done"] = True
        state.meta.pop("3_1_33_lRG_sy_arm", None)
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
