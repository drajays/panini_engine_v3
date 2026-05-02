"""
pipelines/tasmAd_iti_uttarasya_paribhasha_P044_note_demo.py — **P044** note demo.

Source: ``…/my_scripts/final/split_prakriyas_11/P044.json``.

Illustrates **1.1.67** *tasmād iti uttarasya* (pañcamī → operation on *para*),
**8.1.28** *tiṅ atiṅaḥ* (*atiṅ* in pañcamī position relative to *tiṅ*), contrast
**1.1.66** *tasminn iti … pūrvasya*, with sample *vākya* ``odanam pacati``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_tasmAd_iti_uttarasya_paribhasha_P044_note() -> State:
    terms = [
        Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence("odanam")),
            tags={"anga", "prātipadika", "P044_atiNa_position_pada"},
            meta={"upadesha_slp1": "odanam"},
        ),
        Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence("pacati")),
            tags={"anga", "prātipadika", "P044_tin_position_pada"},
            meta={"upadesha_slp1": "pacati"},
        ),
    ]
    s = State(terms=terms, meta={}, trace=[])
    s.meta["prakriya_P044_paribhasha_note"] = True
    s.meta["prakriya_P044_paribhasha_note_only"] = True

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.1.67", s)

    s.meta["P044_8_1_28_tin_context_arm"] = True
    s = apply_rule("8.1.28", s)

    s.meta["P044_1_1_67_atina_arm"] = True
    s = apply_rule("1.1.67", s)

    s.meta["P044_8_1_28_nighata_illustration_arm"] = True
    s = apply_rule("8.1.28", s)

    s = apply_rule("1.1.66", s)

    s.meta["P044_1_1_67_siddhi_arm"] = True
    s = apply_rule("1.1.67", s)
    return s


__all__ = ["derive_tasmAd_iti_uttarasya_paribhasha_P044_note"]
