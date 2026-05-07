"""
pipelines/brAhmaRAH_prathamA_bahu_corrected_P004_C_demo.py — **P004-C** ब्राह्मणाः.

अकारान्त पुंलिङ्ग ``brAhmaRa`` (ब्राह्मण, ण् = SLP1 ``R``) + प्रथमा बहुवचन → ``brAhmaRAH``.

CONSTITUTION Art. 7 / 11: standard ``pipelines.subanta.derive`` only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State
from pipelines.subanta import derive

_STEM = "brAhmaRa"


def derive_brAhmaRAH_prathamA_bahu_corrected_P004_C() -> State:
    return derive(_STEM, vibhakti=1, vacana=3, linga="pulliṅga")


__all__ = ["derive_brAhmaRAH_prathamA_bahu_corrected_P004_C", "_STEM"]
