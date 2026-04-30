"""
pipelines/gaurAvaskandin_prakriya_29_demo.py — ``prakriya_29`` (*gaurāvaskandin* vocative accent).

From ``…/separated_prakriyas/prakriya_29_*.json`` (OCR-corrected ``panini_engine_pipeline``):

  • **2.3.48** *sāmantritam* — ``sAmantrita`` on the vocative surface.
  • **6.1.197** *ñaṇityādir nityam* — first-syllable *udātta* note (*ṇit* narrative).
  • **6.1.158** *anudāttaṃ padam ekavarjam* — sentence-level *anudātta-pada* note.
  • **6.1.198** *āmantriṭasya ca* — *ādyudātta* confirmation stamp.
  • **8.2.1** Tripāḍī · **8.4.66** *udāttād anudāttasya svaritaḥ*.

Affixation (**4.1.x**), **6.1.68** *su*-lopa, and Phiṭ *nipātā ādyudāttāḥ* (*iva*) are out of
scope for this accent-only slice; flat tape stays ``gaurAvaskandin``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_gaurAvaskandin_vocative_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("gaurAvaskandin")),
        tags={
            "anga",
            "prātipadika",
            "sambuddhi_prayoga",
            "prakriya_29_Riti_pratyaya_demo",
        },
        meta={"upadesha_slp1": "gaurAvaskandin"},
    )


def derive_gaurAvaskandin_prakriya_29() -> State:
    s = State(terms=[_mk_gaurAvaskandin_vocative_demo()], meta={}, trace=[])

    s.meta["prakriya_29_2_3_48_arm"] = True
    s = apply_rule("2.3.48", s)

    s.meta["prakriya_29_6_1_197_arm"] = True
    s = apply_rule("6.1.197", s)

    s.meta["prakriya_29_6_1_158_arm"] = True
    s = apply_rule("6.1.158", s)

    s.meta["prakriya_29_6_1_198_arm"] = True
    s = apply_rule("6.1.198", s)

    s = apply_rule("8.2.1", s)

    s.meta["prakriya_29_8_4_66_arm"] = True
    s = apply_rule("8.4.66", s)
    return s


__all__ = ["derive_gaurAvaskandin_prakriya_29", "_mk_gaurAvaskandin_vocative_demo"]
