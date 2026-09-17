"""
8.2.7  नलोपः प्रातिपदिकान्तस्य  —  VIDHI

Operational role (v3.6):
  In Tripāḍī zone, for a single-term pada that ends in final ``n``, elide
  that ``n`` structurally (e.g. ``rAjAn`` → ``rAjA``) — no caller arming.

Legacy slice:
  Also supports the existing **tṛc** nominal output path (``krt_tfc`` on the
  pada), which is treated as always-armed within that narrow demo family.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82007 · नलोपः प्रातिपदिकान्तस्य
              padaccheda: न (लुप्तषष्ठ्यन्तः) लोपः प्रातिपदिक (इति लुप्तषष्ठीकम्) अन्तस्य
              anuvṛtti:   81016: पदस्य
  Source #2 — Kāśikā 8.2.7 udāharaṇa:
                राजा
                राजभ्याम्
                राजभिः
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_trc.py, tests/unit/test_audit_pipeline_auditor.py, tests/unit/test_paYcagoRiH_dvigu_split_prakriyas.py
  Reference record: sutra_ref_out/8_2_7.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    # Branch A (default): Tripāḍī, pada-final n-lopa — but only when that
    # final n *belongs to the prātipadika* (राजन्, आत्मन् … — प्रातिपदिकान्तस्य,
    # tagged ``an_pratipadika`` at subanta tape-init), not when it is a sup
    # ending that happens to surface as n after sandhi (रामान्, सर्वान् —
    # अकारान्त स्तेम + अम्-द्वितीया).
    if state.tripadi_zone and len(state.terms) == 1 and "pada" in state.terms[0].tags:
        t0 = state.terms[0]
        if t0.meta.get("nalopa_8_2_7_done"):
            return False
        if not t0.varnas or t0.varnas[-1].slp1 != "n":
            return False
        if "sambuddhi" in t0.tags or "ngi" in t0.tags:
            return False  # 8.2.8 न ङिसम्बुद्ध्योः — blocks this very rule there
        return "krt_tfc" in t0.tags or "an_pratipadika" in t0.tags

    # Branch B (narrow demo): samāsa boundary n-lopa on the prior member (P011 dvigu).
    if not state.meta.get("purvapada_n_lopa_recipe"):
        return False
    if len(state.terms) < 2:
        return False
    t0 = state.terms[0]
    if t0.meta.get("nalopa_8_2_7_done"):
        return False
    if not t0.varnas:
        return False
    return t0.varnas[-1].slp1 == "n"


def act(state: State) -> State:
    t0 = state.terms[0]
    t0.varnas.pop()
    t0.meta["nalopa_8_2_7_done"] = True
    # One-shot for the narrow compound branch.
    state.meta.pop("purvapada_n_lopa_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.7",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "nalopaH prAtipadikAntasya",
    text_dev       = "नलोपः प्रातिपदिकान्तस्य",
    padaccheda_dev = "न-लोपः प्रातिपदिकान्तस्य",
    why_dev        = "प्रातिपदिकान्त्यवर्णे नकारस्य लोपः (चेता-पथ)।",
    anuvritti_from = ("8.2.6",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
