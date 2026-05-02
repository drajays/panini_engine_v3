"""
pipelines/dADikam_taddhita_split_prakriyas_P018_demo.py — **P018** (**दाधिकम्**).

Source: ``…/my_scripts/final/split_prakriyas_11/P018.json``.

Narrow glass-box spine (apply_rule only):
  **4.1.76** → **4.4.135** (attach Tak) → **1.3.7** → **7.3.50** (Tak→ika) →
  **1.1.50** (sthanāntara gates for vṛddhi selection) → **6.4.1** → **6.4.129** →
  **7.2.117** (ādi-vṛddhi) → **6.4.148** (armed i-lopa before ika) →
  **1.2.46** → **4.1.2** → **7.1.24** → **6.1.101**.

Target: ``dADikam``.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_dADikam_taddhita_split_prakriyas_P018() -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("daDi")),
        tags={"anga", "prātipadika", "napuṃsaka", "prakriya_P018_dADikam_demo"},
        meta={"upadesha_slp1": "daDi"},
    )
    s = State(terms=[stem], meta={}, trace=[])
    s.meta["prakriya_P018_dADikam_split_prakriyas_11"] = True

    s = apply_rule("4.1.76", s)
    s.meta["prakriya_P018_4_4_135_Tak_arm"] = True
    s = apply_rule("4.4.135", s)

    s = apply_rule("1.3.7", s)
    s = apply_rule("7.3.50", s)

    # install sthānāntara vṛddhi map used by 7.2.117 when present
    s = apply_rule("1.1.50", s)

    s = apply_rule("6.4.1", s)
    s = apply_rule("7.2.117", s)

    # Open *bhasya* just before 6.4.148 (see 6.4.129 note in this repo).
    s = apply_rule("6.4.129", s)
    s.meta["prakriya_P018_6_4_148_i_lopa_before_ika_arm"] = True
    s = apply_rule("6.4.148", s)

    s = apply_rule("1.2.46", s)

    # Structural merge: taddhita-anta is treated as a single aṅga for sup steps.
    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)

    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("7.1.24", s)
    # a + am → am in this engine via 6.1.107 (JSON cites 6.1.101, but 6.1.107 is the correct narrow slice here).
    s = apply_rule("6.1.107", s)
    return s


__all__ = ["derive_dADikam_taddhita_split_prakriyas_P018"]

