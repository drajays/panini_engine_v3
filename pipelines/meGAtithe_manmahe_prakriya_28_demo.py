"""
pipelines/meGAtithe_manmahe_prakriya_28_demo.py — ``prakriya_28`` Vedic phrase accent.

From ``…/separated_prakriyas/prakriya_28_*.json`` (OCR-corrected narrative):

  • **2.1.2** *subāmantite parāṅgavat svare* — *parāṅgavat* accent unit.
  • **6.1.198** *āmantriṭasya ca* — *ādyudātta* note on the composite unit.
  • **6.1.158** *anudāttaṃ padam ekavarjam* — sentence-level *anudātta-pada* note.
  • **8.2.1** Tripāḍī · **8.4.66** *udāttād anudāttasya svaritaḥ*.

The JSON ``ordered_sutra_sequence`` lists **8.4.65** (OCR); the corrected spine uses
**8.4.66** (same as the ``panini_engine_pipeline`` table).

Flat tape: ``meGAtithe`` + ``manmahe`` concatenated (no inter-word space in ``flat_slp1``).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_meGAtithe_voc() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("meGAtithe")),
        tags={"anga", "prātipadika", "prakriya_28_subanta_vocative"},
        meta={"upadesha_slp1": "meGAtithe"},
    )


def _mk_manmahe_tin() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("manmahe")),
        tags={"anga", "prātipadika", "prakriya_28_following_tin"},
        meta={"upadesha_slp1": "manmahe"},
    )


def derive_meGAtithe_manmahe_prakriya_28() -> State:
    s = State(terms=[_mk_meGAtithe_voc(), _mk_manmahe_tin()], meta={}, trace=[])

    s.meta["prakriya_28_2_1_2_arm"] = True
    s = apply_rule("2.1.2", s)

    s.meta["prakriya_28_6_1_198_arm"] = True
    s = apply_rule("6.1.198", s)

    s.meta["prakriya_28_6_1_158_arm"] = True
    s = apply_rule("6.1.158", s)

    s = apply_rule("8.2.1", s)

    s.meta["prakriya_28_8_4_66_arm"] = True
    s = apply_rule("8.4.66", s)
    return s


__all__ = [
    "derive_meGAtithe_manmahe_prakriya_28",
    "_mk_meGAtithe_voc",
    "_mk_manmahe_tin",
]
