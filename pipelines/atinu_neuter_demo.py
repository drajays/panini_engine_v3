"""
pipelines/atinu_neuter_demo.py — अतिनु neuter stem (`atinu`)

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/अतिनु.md`

Summary (execution spine aligned with the note):
  1. Initial prātipadika ``atinO`` (अतिनौ), neuter.
  2. Nom.sg ``su`` via **4.1.2** → ``su`` string reduced after it-lopa to ``s``.
  3. **1.2.47** shortens the final vowel; ``atinO`` ends in *एच्* (``O``), so the
     same *एच्→इक्* resolver used by **1.1.48** applies inside **1.2.47**
     (``phonology.ec_ig_hrasva``).
  4. **7.1.23** *svamoḥ napuṃsakāt* — luk of ``su`` / ``am`` after neuter aṅga.

Implementation is shared with ``atiri_atinu_kulam_demo`` (same EC-final neuter
substrate machinery).
"""
from __future__ import annotations

from pipelines.atiri_atinu_kulam_demo import derive_atinu

__all__ = ["derive_atinu"]
