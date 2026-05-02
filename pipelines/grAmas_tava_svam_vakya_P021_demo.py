"""
pipelines/grAmas_tava_svam_vakya_P021_demo.py — P021 (वाक्य-उदाहरणम्)

Target (SLP1 surface): ``grAmastavasvam`` (spacing omitted by ``flat_slp1``)

Illustration only (no full morphological derivation):
  grAmaH + tava + svam  →  grAmas + tava + svam

Sandhi spine:
  - 1.1.50 (context paribhāṣā note; installs *sthāne'ntaratamaḥ* gates)
  - 8.2.1  (Tripāḍī gate)
  - 8.3.34 (visarga H → s before t)  [narrow slice for this vākya]
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_grAmas_tava_svam_vakya_P021() -> State:
    grAmaH = Term(
        kind="pada",
        varnas=parse_slp1_upadesha_sequence("grAmaH"),
        tags={"pada"},
        meta={"upadesha_slp1": "grAmaH"},
    )
    tava = Term(
        kind="pada",
        varnas=parse_slp1_upadesha_sequence("tava"),
        tags={"pada"},
        meta={"upadesha_slp1": "tava"},
    )
    svam = Term(
        kind="pada",
        varnas=parse_slp1_upadesha_sequence("svam"),
        tags={"pada"},
        meta={"upadesha_slp1": "svam"},
    )
    s = State(terms=[grAmaH, tava, svam], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.50", s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.34", s)
    return s


__all__ = ["derive_grAmas_tava_svam_vakya_P021"]

