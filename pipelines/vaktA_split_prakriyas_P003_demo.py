"""
pipelines/vaktA_split_prakriyas_P003_demo.py — **P003** (**वक्ता** / ``vaktA``).

Source: ``…/my_scripts/final/split_prakriyas_11/P003.json``.

Kṛdanta spine (**vac** + **3.2.135** *tṛn*):
  **3.2.135** → **1.3.3** → **1.3.9** → **8.2.1** → **8.2.30** (*coḥ kuḥ*) → **1.2.45** → **1.2.46** →
  ``_structural_merge_trc_pratipadika`` (**तृन्** tape as SLP1 ``tfn`` — **7.1.94** *ṛ*-stem path).

Then **subanta** nom. sg. (**derive_from_state** … **pulliṅga**): **4.1.2** → … → **7.1.94** → **6.4.11**
→ **6.1.66** → … → **8.2.7** — matching ``test_trc_nom_sg_surfaces`` ordering.

**Tripāḍī reboot:** **8.2.1** is applied for **8.2.30** on the kṛdanta tape, then ``tripadi_zone`` is cleared
before ``derive_from_state`` so **subanta** preflight is not **asiddha**-blocked (same practical split as a fresh
subanta ``State``).

**Edition notes (JSON vs engine):**
  • Step 10 cites **6.4.14**; this repo’s lengthening before ``su`` for ``…an`` + *tṛc*/*tṛn* stems is **6.4.11**
    (*aptṛntṛc…* narrow slice).
  • Step 12 cites **6.1.68**; subanta spine uses **6.1.66** for apṛkta ``s``-lopa here (see ``test_trc_nom_sg_order``).

CONSTITUTION Art. 7 / 11: ``apply_rule`` + documented structural merges only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from pipelines.krdanta import _structural_merge_trc_pratipadika
from pipelines.subanta import derive_from_state


def _witness_vac_split_P003() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("vac")),
        tags={"dhatu", "anga", "prātipadika", "prakriya_P003_vaktA_demo"},
        meta={"upadesha_slp1": "vac"},
    )


def derive_vaktA_split_prakriyas_P003() -> State:
    s = State(terms=[_witness_vac_split_P003()], meta={}, trace=[])

    s.meta["prakriya_P003_3_2_135_tRn_arm"] = True
    s = apply_rule("3.2.135", s)

    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.30", s)
    s.tripadi_zone = False

    s = apply_rule("1.2.45", s)
    s = apply_rule("1.2.46", s)

    s = _structural_merge_trc_pratipadika(s, upadesha_slp1="tfn")
    s.terms[0].tags.add("pulliṅga")

    return derive_from_state(s, 1, 1, linga="pulliṅga")


__all__ = ["derive_vaktA_split_prakriyas_P003", "_witness_vac_split_P003"]
