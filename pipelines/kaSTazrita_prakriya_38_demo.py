"""
pipelines/kaSTazrita_prakriya_38_demo.py — ``prakriya_38`` (**कष्टश्रितः** gate).

From ``…/separated_prakriyas/prakriya_38_*.json`` — ``ordered_sutra_sequence``: **2.1.3**, **2.1.23**.

Narrow slice:

  **2.1.3** *prāk kaḍārāt samāsaḥ* (adhikāra) → **2.1.23** *dvitīyā śritātīta…* (registry stamp for
  **कष्ट** + **श्रित** ``tat-puruṣa`` neighbourhood).

Full **१.२.४३**, **२.२.३०**, **१.२.४६**, **२.४.७१**, **८.२.६६**, **८.३.१५** … are out of scope here.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_kaSTazrita_witness() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kaSTazrita")),
        tags={"anga", "prātipadika", "prakriya_38_kaSTazrita_demo"},
        meta={"upadesha_slp1": "kaSTazrita"},
    )


def derive_kaSTazrita_prakriya_38() -> State:
    s = State(terms=[_mk_kaSTazrita_witness()], meta={}, trace=[])

    s = apply_rule("2.1.3", s)

    s.meta["prakriya_38_dvitIyA_compound_vidhi_note"] = True
    s.meta["prakriya_38_2_1_23_arm"] = True
    s = apply_rule("2.1.23", s)
    return s


__all__ = ["derive_kaSTazrita_prakriya_38", "_mk_kaSTazrita_witness"]
