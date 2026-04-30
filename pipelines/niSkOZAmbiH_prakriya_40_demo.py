"""
pipelines/niSkOZAmbiH_prakriya_40_demo.py — ``prakriya_40`` (निष्कोशाम्बिः spine fragment).

Source: ``…/separated_prakriyas/prakriya_40_2026-04-29_14_21_45.json``.

JSON ``ordered_sutra_sequence``: **5.3.15**, **8.3.41**.

The commentary ``panini_engine_pipeline`` cites **8.3.15** (*खरवसानयोर्विसर्जनीयः*) for ``र्`` →
visarga before ``क``, not **5.3.15** (different adhyāya — OCR/keying confusion with ``5|3|15``).

This demo stitches only the Tripāḍī fragment aligned with that narrative:

  **8.2.1** (Tripāḍī gate) → **8.3.15** (``ru`` → ``H``) → **8.3.41** (``H`` + ``k`` → ``z`` + ``k``, i.e. ``निः`` → ``निष्``).

Witness tape: ``निर्`` + ``कौशाम्बि`` merged as ``n`` ``i`` ``r`` (``ru_intermediate``) + ``kOSAmbi``, modelling *laghu* **कौशाम्बि**
after **1.2.48** etc., omitted here.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_nirkOSAmbi_stem() -> Term:
    rest = list(parse_slp1_upadesha_sequence("kOSAmbi"))
    varnas = [mk("n"), mk("i"), mk("r", "ru_intermediate")] + rest
    return Term(
        kind="prakriti",
        varnas=varnas,
        tags={"anga", "prātipadika", "prakriya_40_nihka_witness"},
        meta={"upadesha_slp1": "nirkOSAmbi"},
    )


def derive_niSkOZAmbi_stem_prakriya_40() -> State:
    """Return state after **8.3.15** + **8.3.41** on the ``निर्+कौशाम्बि`` fragment."""
    s = State(terms=[_witness_nirkOSAmbi_stem()], meta={}, trace=[])

    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.15", s)

    s.meta["prakriya_40_8_3_41_arm"] = True
    s = apply_rule("8.3.41", s)
    return s


__all__ = ["derive_niSkOZAmbi_stem_prakriya_40", "_witness_nirkOSAmbi_stem"]
