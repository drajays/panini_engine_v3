"""
pipelines/hotAram_prakriya_21_demo.py — ``prakriya_21`` (*hotāram*).

Glass-box spine (JSON ``panini_engine_pipeline``):
  ``hu`` + ``tfc`` (**3.1.133** …) → ``hotf`` via ``derive_tfc_pratipadika``;
  **subanta** preflight + **4.1.2** ``am`` → **1.1.43** (*sarvanāmasthāna* on
  ``am``) → **7.3.110** + **1.1.51** (ṛ → ``ar``) → **6.4.11** (upadhā-dīrgha
  ``hotar`` → ``hotAr``) → **3.1.4** → ``subanta_post_4_1_2`` (**6.1.107**,
  Tripāḍī) → ``hotAram``.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule

from core.canonical_pipelines import subanta_post_4_1_2
from pipelines.krdanta import derive_tfc_pratipadika
from pipelines.subanta import run_subanta_preflight_through_1_4_7


def derive_hotAram_prakriya_21():
    s = derive_tfc_pratipadika("hu")
    s.meta["prakriya_21_hotAram"] = True
    if s.terms:
        s.terms[0].tags.add("pulliṅga")
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "2-1"

    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)

    s.meta["prakriya_21_1_1_43_am_arm"] = True
    s = apply_rule("1.1.43", s)
    s.meta.pop("prakriya_21_1_1_43_am_arm", None)

    s.meta["prakriya_21_7_3_110_arm"] = True
    s = apply_rule("7.3.110", s)
    s = apply_rule("1.1.51", s)

    s.meta["prakriya_21_6_4_11_arm"] = True
    s = apply_rule("6.4.11", s)

    s = apply_rule("3.1.4", s)
    s = subanta_post_4_1_2(s)
    return s


__all__ = ["derive_hotAram_prakriya_21"]
