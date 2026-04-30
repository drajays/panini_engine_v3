"""
pipelines/aDyApaka_kv_prakriya_34_demo.py — ``prakriya_34`` (**अध्यापक क्व** accent spine).

From ``…/separated_prakriyas/prakriya_34_*.json`` — ``ordered_sutra_sequence`` is empty (OCR low
confidence); ``panini_engine_pipeline`` prescribes:

  **2.3.48** *sāmantritam* → **8.1.16** / **8.1.18** → **8.1.19** *āmantriṭasya ca*
  (*sarvānudātta* on ``aDyApaka``) → **6.1.185** *tit-svaritam* (*svarita* note on ``kv``) →
  **1.2.40** *udātta-svarita-parasya sannataraḥ* (*sannatara* registry).

Flat tape: ``aDyApaka`` + ``kv`` → ``aDyApakakv``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_aDyApaka_kv_vocative() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("aDyApaka")),
        tags={
            "anga",
            "prātipadika",
            "sambuddhi_prayoga",
            "prakriya_34_aDyApaka_kv_demo",
        },
        meta={"upadesha_slp1": "aDyApaka"},
    )


def _mk_kv_nipAta() -> Term:
    return Term(
        kind="nipata",
        varnas=list(parse_slp1_upadesha_sequence("kv")),
        tags={"nipāta", "prakriya_34_kv_interrogative_demo"},
        meta={"upadesha_slp1": "kv"},
    )


def derive_aDyApaka_kv_prakriya_34() -> State:
    s = State(
        terms=[_mk_aDyApaka_kv_vocative(), _mk_kv_nipAta()],
        meta={},
        trace=[],
    )

    s.meta["prakriya_34_2_3_48_arm"] = True
    s = apply_rule("2.3.48", s)

    s = apply_rule("8.1.16", s)
    s = apply_rule("8.1.18", s)

    s.meta["prakriya_34_8_1_19_arm"] = True
    s = apply_rule("8.1.19", s)

    s.meta["prakriya_34_6_1_185_arm"] = True
    s = apply_rule("6.1.185", s)

    s.meta["prakriya_34_1_2_40_arm"] = True
    s = apply_rule("1.2.40", s)
    return s


__all__ = [
    "derive_aDyApaka_kv_prakriya_34",
    "_mk_aDyApaka_kv_vocative",
    "_mk_kv_nipAta",
]
