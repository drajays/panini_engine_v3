"""
pipelines/EdaviDa_jWilaka_aDyApaka_prakriya_32_demo.py — ``prakriya_32`` tri-vocative accent.

From ``…/separated_prakriyas/prakriya_32_*.json`` — corrected ``panini_engine_pipeline``:

  **2.3.48** *sāmantritam* → **6.1.198** *āmantriṭasya ca* (*ādyudātta* note on ``EdaviDa``) →
  **6.1.158** *anudāttaṃ padam ekavarjam* → **8.1.16** / **8.1.18** (*padasya* / *apādādau*) →
  **8.1.72** *āmantriṭaṃ pūrvam avidyamānavat* → **8.1.73** *nām antriṭe samānādhikaraṇe…* →
  **8.1.19** *āmantriṭasya ca* (twice: ``jaWilaka``, ``aDyApaka`` *sarvānudātta* notes) →
  **8.2.1** Tripāḍī · **8.4.66** *udāttād anudāttasya svaritaḥ* (registry on ``EdaviDa``).

Commentary tables sometimes order **8.4.66** before **8.1.72**; the engine applies **8.1.72–73**
before **8.2.1** so Tripāḍī (**8.4.66**) stays ``asiddha``-compatible with ``engine/gates.py``.
JSON ``ordered_sutra_sequence`` lists **8.1.82** — OCR confusion with **8.1.72** (same digit-shape class).

Flat tape (concatenated): ``EdaviDajaWilakaaDyApaka``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_EdaviDa() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("EdaviDa")),
        tags={
            "anga",
            "prātipadika",
            "sambuddhi_prayoga",
            "prakriya_32_tri_vocative_demo",
        },
        meta={"upadesha_slp1": "EdaviDa"},
    )


def _mk_jaWilaka() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("jaWilaka")),
        tags={
            "anga",
            "prātipadika",
            "sambuddhi_prayoga",
            "prakriya_32_tri_vocative_demo",
        },
        meta={"upadesha_slp1": "jaWilaka"},
    )


def _mk_aDyApaka() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("aDyApaka")),
        tags={
            "anga",
            "prātipadika",
            "sambuddhi_prayoga",
            "prakriya_32_tri_vocative_demo",
        },
        meta={"upadesha_slp1": "aDyApaka"},
    )


def derive_EdaviDa_triplet_prakriya_32() -> State:
    s = State(
        terms=[_mk_EdaviDa(), _mk_jaWilaka(), _mk_aDyApaka()],
        meta={},
        trace=[],
    )

    s.meta["prakriya_32_2_3_48_arm"] = True
    s = apply_rule("2.3.48", s)

    s.meta["prakriya_32_6_1_198_arm"] = True
    s = apply_rule("6.1.198", s)

    s.meta["prakriya_32_6_1_158_arm"] = True
    s = apply_rule("6.1.158", s)

    s = apply_rule("8.1.16", s)
    s = apply_rule("8.1.18", s)

    s.meta["prakriya_32_8_1_72_arm"] = True
    s = apply_rule("8.1.72", s)

    s.meta["prakriya_32_8_1_73_arm"] = True
    s = apply_rule("8.1.73", s)

    s.meta["prakriya_32_8_1_19_jWilaka_arm"] = True
    s = apply_rule("8.1.19", s)

    s.meta["prakriya_32_8_1_19_aDyApaka_arm"] = True
    s = apply_rule("8.1.19", s)

    s = apply_rule("8.2.1", s)

    s.meta["prakriya_32_8_4_66_arm"] = True
    s = apply_rule("8.4.66", s)
    return s


__all__ = [
    "derive_EdaviDa_triplet_prakriya_32",
    "_mk_EdaviDa",
    "_mk_jaWilaka",
    "_mk_aDyApaka",
]
