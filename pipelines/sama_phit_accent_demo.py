"""
pipelines/sama_phit_accent_demo.py — ``prakriya_17`` (``sama`` + Phit accent path).

Narrative (from ``…/separated_prakriyas/prakriya_17_*.json``, OCR-corrected):
  • **Phit 1.1** *फिषोऽन्त उदात्तः* — *phiṣa* stems: final syllable *udātta* by default.
  • **Phit 4.18** *स्वङ् सम सिम …* list — ``sama`` is *sarvānudātta* (blocks that utsarga).
  • **Aṣṭ. 6.1.158** *अनुदात्तं पदमेकवर्जम्* — sentence-level *anudātta-pada* note (trace).

v3: no *svara* marks on ``Varna`` rows; ``apply_rule`` only registers audit keys.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_phiSa_stem(*, upadesha_slp1: str) -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(upadesha_slp1)),
        tags={"prātipadika", "phiSa_pratipadika"},
        meta={"upadesha_slp1": upadesha_slp1},
    )


def derive_sama_phit_accent() -> State:
    """``sama`` — Phit 4.18 wins; **8.4.66** (*Phit* 1.1 utsarga) is blocked."""
    s = State(terms=[_mk_phiSa_stem(upadesha_slp1="sama")])
    s.meta["phit_sama_demo_arm"] = True
    s.meta["prakriya_17_6_1_158_arm"] = True
    s = apply_rule("6.1.158", s)
    s.meta.pop("prakriya_17_6_1_158_arm", None)
    s.meta["phit_4_18_arm"] = True
    s = apply_rule("8.1.3", s)
    s.meta["phit_1_1_arm"] = True
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.4.66", s)
    return s


def derive_non_phit418_phiSa_stem() -> State:
    """Control: stem not in the Phit 4.18 list → **8.4.66** registers the utsarga candidate."""
    s = State(terms=[_mk_phiSa_stem(upadesha_slp1="rAma")])
    s.meta["phit_sama_demo_arm"] = True
    s.meta["prakriya_17_6_1_158_arm"] = True
    s = apply_rule("6.1.158", s)
    s.meta.pop("prakriya_17_6_1_158_arm", None)
    s.meta["phit_4_18_arm"] = True
    s = apply_rule("8.1.3", s)
    s.meta["phit_1_1_arm"] = True
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.4.66", s)
    return s


__all__ = ["derive_non_phit418_phiSa_stem", "derive_sama_phit_accent"]
