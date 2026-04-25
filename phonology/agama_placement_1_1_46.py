"""
phonology/agama_placement_1_1_46.py — **1.1.46** *ādyantau ṭakitau*

*Paribhāṣā* (āgama-sthāna): a **ṭit** augment is placed **before** its
*āgamin*; a **kit** augment **after** it.  **Mit** is out of scope here
(**1.1.47**).

These helpers are pure (no ``engine``); *vidhi* that insert augments may
call them when deciding splice order.  Whether a given string is truly an
*āgama* (vs a pratyaya like *ṭak*) needs *śāstra* / *vṛtti* context.
"""
from __future__ import annotations

from typing import Literal

Placement = Literal["before_agamin", "after_agamin"]


def tit_agama_placement() -> Placement:
    """**Ṭit**-marked augment: **ādi** — immediately **before** the *āgamin*."""
    return "before_agamin"


def kit_agama_placement() -> Placement:
    """**Kit**-marked augment: **anta** — immediately **after** the *āgamin*."""
    return "after_agamin"
