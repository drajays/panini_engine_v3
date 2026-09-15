"""
3.1.77  तुदादिभ्यः शः  —  VIDHI

  For tudādi (gaṇa 6) dhātu, use vikaraṇa `Sa` instead of `Sap`.

cond: dhātu.meta["gana"] == 6 AND no existing Śa term on tape.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31077 · तुदादिभ्यः शः
              padaccheda: तुदादिभ्यः शः
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31022: धातोः | 31067: सार्वधातुके | 31068: कर्तरि
  Source #2 — Kāśikā 3.1.77 udāharaṇa:
                शपोऽपवादः
                शकारः सार्वधातुकसंज्ञार्थः
                तुदति
  Cross-check — surface pinned by: tests/unit/test_kirati_karati_split_prakriyas.py
  Reference record: sutra_ref_out/3_1_77.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _dhatu_gana(state: State) -> int | None:
    for t in state.terms:
        if "dhatu" in t.tags:
            g = t.meta.get("gana")
            return int(g) if g is not None else None
    return None


def _matches(state: State) -> bool:
    if _dhatu_gana(state) != 6:
        return False
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    if any((t.meta.get("upadesha_slp1") or "").strip() == "Sa" for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    sa = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Sa"),
        tags={"pratyaya", "vikarana", "upadesha"},
        meta={"upadesha_slp1": "Sa"},
    )
    state.terms.insert(1, sa)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.77",
    sutra_type=SutraType.VIDHI,
    text_slp1="tudAdibhyaH SaH",
    text_dev="तुदादिभ्यः शः",
    padaccheda_dev="तुदादिभ्यः शः",
    why_dev="तुदादि-गणेभ्यः धातुभ्यः श-विकरणः।",
    anuvritti_from=("3.1.67", "3.1.91"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

# SOI: tudAdi (gana 6) śa — apavāda to śap; score 10 when gana matches, else 0.
from engine.specificity_registry import register_specificity as _rs
_rs("3.1.77", lambda state, _g=6: (
    10 if next((t.meta.get("gana") for t in state.terms if "dhatu" in t.tags), None) == _g else 0
))
del _rs
