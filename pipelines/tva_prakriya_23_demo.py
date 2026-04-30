"""
pipelines/tva_prakriya_23_demo.py — ``prakriya_23`` (*tvā* for *tvām*).

Glass-box spine (JSON ``panini_engine_pipeline`` / corrected commentary):
  Fully formed *padam* ``tvAm`` (accusative of *yuṣmad*, not at a *pāda*-initial
  locus — recipe-asserted) → **8.1.18** *anudāttaṃ sarvam apādādau* *adhikāra* →
  **8.1.23** *tvāmau dvitīyāyāḥ* → ``tvA``, with ``sarva_anudAtta_8_1_18`` on the
  *ādeśa* when the **8.1.18** scope is on ``adhikara_stack``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_tvAm_pada() -> Term:
    """Lexical *pada* ``tvAm`` (``yuṣmad`` + *dvitīyā* ``am``), not *pāda*-initial."""
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("tvAm")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "tvAm"},
    )


def derive_tva_prakriya_23() -> State:
    s = State(terms=[_mk_tvAm_pada()], meta={}, trace=[])
    s = apply_rule("8.1.18", s)
    s.meta["prakriya_23_apAda_adau_arm"] = True
    s.meta["prakriya_23_8_1_23_arm"] = True
    s = apply_rule("8.1.23", s)
    return s


__all__ = ["derive_tva_prakriya_23", "_mk_tvAm_pada"]
