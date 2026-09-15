"""
3.3.15  अनद्यतने लुट्  —  VIDHI (narrow)

Glass-box: when a recipe arms ``luT_recipe`` under the **3.3.3** future
adhikāra, attach the *luṭ* *lac* placeholder (``luT``) after the *dhātu*.

``cond`` does not read *lakāra* names from paradigm metadata beyond the
allowlisted ``state.meta`` key (CONSTITUTION Art. 2).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 33015 · अनद्यतने लुट्
              padaccheda: अन्-अद्यतने लुट्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ् | 33003: भविष्यति
  Source #2 — Kāśikā 3.3.15 udāharaṇa:
                लृटोऽपवादः
                श्वःकर्ता
                श्वो भोक्ता
  Cross-check — surface pinned by: tests/unit/test_Bavitum_split_prakriyas.py, tests/unit/test_sutra_3_3_141_vA_lfN_adhikAra.py, tests/unit/test_sutra_3_3_3_bhavizyadadhikAra.py
  Reference record: sutra_ref_out/3_3_15.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("luT_recipe"):
        return False
    if state.meta.get("3_3_15_lut_attached"):
        return False
    return adhikara_in_effect("3.3.15", state, "3.3.3")


def act(state: State) -> State:
    lu = Term(
        kind="pratyaya",
        varnas=[],
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "luT"},
    )
    vs = parse_slp1_upadesha_sequence("luT")
    if vs and vs[-1].slp1 == "T":
        vs = vs[:-1]
    lu.varnas = vs
    state.terms.append(lu)
    state.meta["3_3_15_lut_attached"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.15",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "anadyatane luw",
    text_dev       = "अनद्यतने लुट्",
    padaccheda_dev = "अनद्यतने लुट्",
    why_dev        = "अनद्यतने लुट्-लकारः (भविष्यदधिकारे) — संकीर्ण-विधिः।",
    anuvritti_from = ("3.3.3",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
