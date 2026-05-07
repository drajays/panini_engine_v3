"""
pipelines/vAcA_tRtIyA_strI_corrected_P004_D_demo.py — **P004-D** वाचा.

हलन्त प्रातिपदिक ``vAc`` + स्त्रीलिङ्ग + तृतीया एकवचन → ``vAcA``.

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

_STEM = "vAc"


def derive_vAcA_tRtIyA_strI_corrected_P004_D() -> State:
    return derive(_STEM, vibhakti=3, vacana=1, linga="strīliṅga")


__all__ = ["derive_vAcA_tRtIyA_strI_corrected_P004_D", "_STEM"]
