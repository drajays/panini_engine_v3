"""
pipelines/dadhiccChatram_samasa_demo.py — *dadhi* + ``Catram`` (SLP ``C`` = छ्) → **dadhiccCatram** (≈ दधिच्छत्रम्).

Source: ``separated_prakriyas/prakriya_15_2026-04-29_14_16_19.json`` (Prakriyā 1 table).

Spine:
  **6.1.73** (*Che ca* — *tuk* after ``i`` before ``C``) → *pada* merge → **8.2.1** → **8.4.40**
  (*stoḥ ścunā ścuḥ*: ``t`` + ``C`` → ``c``).

Secondary tables in the JSON (*kumarī*, *devadatta* vocative) are omitted here to avoid duplicating
other subanta/sambodhana pipelines; extend with separate demos if needed.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_dadhiccChatram() -> State:
    t1 = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("daDi"),
        tags={"prātipadika", "samAsa_first"},
        meta={"segment_slp1": "daDi"},
    )
    t2 = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("Catram"),
        tags={"prātipadika", "samAsa_second"},
        meta={"segment_slp1": "Catram"},
    )
    s = State(terms=[t1, t2], meta={}, trace=[])

    s.meta["6_1_73_che_ca_arm"] = True
    s = apply_rule("6.1.73", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)

    s.meta["8_4_40_sto_tCh_arm"] = True
    s = apply_rule("8.4.40", s)
    return s


__all__ = ["derive_dadhiccChatram"]
