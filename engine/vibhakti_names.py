"""Vibhakti / vacana saṃjñā-names as Term tags (stamped by 4.1.2, the one place coordinates enter the engine).

``cond()`` may read these tags (Art. 2: saṃjñā) but never the (vibhakti, vacana) coordinates themselves.
"""
from __future__ import annotations

VIBHAKTI_TAG = {1: "vib_prathama", 2: "vib_dvitiya", 3: "vib_trtiya", 4: "vib_caturthi",
                5: "vib_panchami", 6: "vib_shashthi", 7: "vib_saptami", 8: "vib_sambodhana"}
VACANA_TAG = {1: "vac_eka", 2: "vac_dvi", 3: "vac_bahu"}


def vibhakti_vacana_tags(vv: str) -> set[str]:
    """``"4-1"`` → ``{"vib_caturthi", "vac_eka"}``."""
    v, c = (int(x) for x in vv.split("-"))
    return {VIBHAKTI_TAG[v], VACANA_TAG[c]}
