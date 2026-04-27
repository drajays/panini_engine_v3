"""
*ābhyām* from *idam* (तृतीया/चतुर्थी/पञ्चमी द्विवचन) — **7.2.113** *हलि* *लोप* + **7.3.102** *सुपि* *च*.

User note: ``…/my panini notes/aabhyam.md`` — after **7.2.102** and **6.1.97** the aṅga is
**i**+**d**+**a**; *hal*ī *sup* (**B**+**y**+…) triggers **7.2.113** → lone **a**; **1.1.21** +
**7.3.102** → **A**+**bhyām** (SLP1 **AByAm**).

Re-exports ``derive``; no second scheduling path.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State
from pipelines.subanta import derive


def derive_idam_dvibhi_aabhyam(
    vibhakti: int,
    *,
    tritiya_chaturthi_pancami_only: bool = True,
) -> State:
    """
    *idam* + 3/4/5 (dual) *sup* *bhyām* → **AByAm** (vibhakti 3, 4, or 5, vacana 2).

    Other *vibhakti* *vacana* combinations use the same *subanta* *motor* but are not
    the *śabda* of this *nota* unless ``tritiya_chaturthi_pancami_only`` is set False
    (default True raises if vibhakti not in {3,4,5}).
    """
    if tritiya_chaturthi_pancami_only and vibhakti not in (3, 4, 5):
        raise ValueError("ābhyām-śabda note: use vibhakti 3, 4, or 5 (dual) only")
    s = derive("idam", vibhakti, 2)
    return s


__all__ = ["derive_idam_dvibhi_aabhyam", "derive"]
