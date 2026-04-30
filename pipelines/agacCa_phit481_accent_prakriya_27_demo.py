"""
pipelines/agacCa_phit481_accent_prakriya_27_demo.py — ``prakriya_27`` (*āgaccha* accent).

From ``…/separated_prakriyas/prakriya_27_*.json`` (OCR-corrected):

  • **Phiṭ** **4.81** *upasargāś cābhivarjam* — ``AgacCa`` initial **ā** *udātta* note,
    anchored as **8.1.6** narrow slice (cf. **8.1.3** ↔ Phit 4.18).
  • **8.1.28** *tiṅṅat tiṅḥ* — **gaccha** portion *anudātta* (*śruti* stamp).
  • **8.2.1** Tripāḍī entry for **8.4.66**.
  • **8.4.66** *udāttād anudāttasya svaritaḥ* — registry ``prakriya_27_svarita_locus``.

Flat tape stays ``AgacCa``; accent is metadata/registry only.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_agacCa_tinanta_accent_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("AgacCa")),
        tags={"anga", "prātipadika", "tinanta_accent_demo"},
        meta={"upadesha_slp1": "AgacCa"},
    )


def derive_agacCa_accent_prakriya_27() -> State:
    s = State(terms=[_mk_agacCa_tinanta_accent_demo()], meta={}, trace=[])

    s.meta["prakriya_27_8_1_6_arm"] = True
    s = apply_rule("8.1.6", s)

    s.meta["prakriya_27_8_1_28_arm"] = True
    s = apply_rule("8.1.28", s)

    s = apply_rule("8.2.1", s)

    s.meta["prakriya_27_8_4_66_arm"] = True
    s = apply_rule("8.4.66", s)
    return s


__all__ = ["derive_agacCa_accent_prakriya_27", "_mk_agacCa_tinanta_accent_demo"]
