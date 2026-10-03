"""
8.2.7  नलोपः प्रातिपदिकान्तस्य  —  VIDHI

Operational role (v3.6):
  In Tripāḍī zone, for a single-term pada that ends in final ``n``, elide
  that ``n`` structurally (e.g. ``rAjAn`` → ``rAjA``) — no caller arming.

  Also fires pre-merge: an ``an_pratipadika``-tagged stem ending in ``n``,
  immediately followed by a HAL-initial sup, loses that ``n`` before merge
  (राजन्+भिस् → राज्+भिस् → राजभिः). A vowel-initial sup (राजन्+औ → राजानौ,
  राजन्+अस् → राज्ञः) does not trigger this branch — the न् survives and
  combines under 6.4.8 / 8.4.40 instead.

(The earlier "legacy slice" that treated every ``krt_tfc`` pada as armed is gone: 7.1.94 now tags the anaṅ-made n ``an_pratipadika``
 itself, and the old shortcut wrongly deleted the n of भवितॄन्.)

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
from phonology.pratyahara import HAL


def _target_premerge(state: State):
    """PRE-MERGE: an_pratipadika stem ending in 'n', followed by a HAL-initial sup."""
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        stem, pratyaya = state.terms[i], state.terms[i + 1]
        if "an_pratipadika" not in stem.tags:
            continue
        if stem.meta.get("nalopa_8_2_7_done"):
            continue
        if not stem.varnas or stem.varnas[-1].slp1 != "n":
            continue
        if "sup" not in pratyaya.tags or not pratyaya.varnas:
            continue
        if pratyaya.varnas[0].slp1 not in HAL:
            continue
        return i
    return None


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
        return "an_pratipadika" in t0.tags   # 7.1.94's anaṅ tags the real prātipadika n; a krt_tfc stem's sup-n (भवितॄन्) is not it

    # Branch B (narrow demo): samāsa boundary n-lopa on the prior member (P011 dvigu).
    if state.meta.get("purvapada_n_lopa_recipe") and len(state.terms) >= 2:
        t0 = state.terms[0]
        if not t0.meta.get("nalopa_8_2_7_done") and t0.varnas and t0.varnas[-1].slp1 == "n":
            return True

    # Branch C: pre-merge, HAL-initial sup after an an_pratipadika stem-final न्.
    # Runs just before pada-merge (subanta P13), one step ahead of 8.2.1
    # opening the Tripāḍī zone — narrow enough (an_pratipadika + sup HAL-
    # initial) to stay safe firing there; see pipelines/subanta.py P13.
    return _target_premerge(state) is not None


def act(state: State) -> State:
    hit = _target_premerge(state)
    if hit is not None and not state.meta.get("purvapada_n_lopa_recipe"):
        stem = state.terms[hit]
        stem.varnas.pop()
        stem.meta["nalopa_8_2_7_done"] = True
        return state

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
