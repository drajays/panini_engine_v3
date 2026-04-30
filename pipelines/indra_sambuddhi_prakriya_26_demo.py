"""
pipelines/indra_sambuddhi_prakriya_26_demo.py — ``prakriya_26`` (*indra* vocative accent).

Glass-box spine (corrected ``panini_engine_pipeline`` in JSON):

  **2.3.48** *sāmantritam* → **6.1.198** *āmantriṭasya ca* (*ādyudātta* note) →
  **6.1.158** *anudāttaṃ padam ekavarjam* → **8.4.66** *udāttād anudāttasya svaritaḥ*
  (registry ``prakriya_26_svarita_locus``) → **1.2.37** *subrahmaṇyā…* closure
  (``prakriya_26_subrahmaNyAhvAna_closure``).

The flat tape stays ``indra``; accent is *śruti*-metadata only (cf. **6.1.158**).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_indra_sambuddhi() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("indra")),
        tags={"anga", "prātipadika", "sambuddhi_prayoga"},
        meta={"upadesha_slp1": "indra"},
    )


def derive_indra_sambuddhi_prakriya_26() -> State:
    s = State(terms=[_mk_indra_sambuddhi()], meta={}, trace=[])

    s.meta["prakriya_26_2_3_48_arm"] = True
    s = apply_rule("2.3.48", s)

    s.meta["prakriya_26_6_1_198_arm"] = True
    s = apply_rule("6.1.198", s)

    s.meta["prakriya_26_6_1_158_arm"] = True
    s = apply_rule("6.1.158", s)

    s.tripadi_zone = True
    s.meta["prakriya_26_8_4_66_arm"] = True
    s = apply_rule("8.4.66", s)

    # **1.2.37** is adhyāya 1 — outside Tripāḍī.  With ``tripadi_zone`` still True,
    # ``asiddha_violates`` would skip it (``engine/gates.py``); exit Tripāḍī for
    # this *āhvāna*-closure *anuvāda* row only.
    s.tripadi_zone = False
    s.meta["prakriya_26_1_2_37_arm"] = True
    s = apply_rule("1.2.37", s)
    return s


__all__ = ["derive_indra_sambuddhi_prakriya_26", "_mk_indra_sambuddhi"]
