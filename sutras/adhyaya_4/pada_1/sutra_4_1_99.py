"""
4.1.99  नडादिभ्यः फक्  —  ANUVADA (temporary no-op stub)

This file exists only to keep at least one `SutraType.ANUVADA` representative
in the registry (see `tests/unit/test_sutra_type_contracts.py`).

When 4.1.99 is implemented for real, change this to the correct SutraType and
behaviour.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra


SUTRA = SutraRecord(
    sutra_id       = "4.1.99",
    sutra_type     = SutraType.ANUVADA,
    text_slp1      = "naDAdibhyaH Pak",
    text_dev       = "नडादिभ्यः फक्",
    padaccheda_dev = "नड-आदिभ्यः / फक्",
    why_dev        = "अनुवाद-स्थगनम् (no-op stub) — SutraType coverage हेतु।",
    anuvritti_from = (),
    cond           = None,
    act            = None,
)

register_sutra(SUTRA)

