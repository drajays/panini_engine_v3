"""
pipelines/adhyagIzwa.py

Entry source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_02_2026-04-29_14_05_58.json`

This entry’s corrected prakriyā is the same `अध्यगीष्ट` luṅ demo as
`pipelines/adhyagIzwa_luN.py`. To avoid duplicate pipelines (CONSTITUTION
Art. 12), this module is a thin alias wrapper only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

from engine.state import State
from pipelines.adhyagIzwa_luN import derive_aDhyagIzwa


def derive_prakriya_02() -> State:
    return derive_aDhyagIzwa()


__all__ = ["derive_prakriya_02"]

