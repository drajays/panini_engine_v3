"""
*मासपूर्वाय* — *tṛtīyā* *tatpuruṣa* + **1.1.30** *tṛtīyā-samāse* (user ``तृतीयासमासे निषेध .md``).

*Upadeśa* ``mAsa-pUrva`` is a *gaṇa* id in ``data/inputs/sarvadi_slp1.json`` (like ``priya-viSva``) so
**1.1.27** arms, then **1.1.30** strips *sarvanāma*; **7.1.14** inert, **7.1.13** + **7.3.102** for *caturthī* *eka*.

*CONSTITUTION*: *no* *gold*; *structural* *tags* only; ``derive(…, tRtIyA_tatpurusha_samAsa=True)``.

Parallel thin wrappers: ``derive_dvyaha_pUrva…``, ``derive_tryaha_pUrva…`` for the note *Form* 2–3 *śabda* *ids* already in the *sarvādi* list.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State
from pipelines.subanta import derive

STEM_MASA_PURVA: str = "mAsa-pUrva"
STEM_DVYAHA_PURVA: str = "dvyaha-pUrva"
STEM_TRYAHA_PURVA: str = "tryaha-pUrva"
LIṄGA_PUM: str = "pulliṅga"


def _derive(stem: str) -> State:
    return derive(
        stem,
        4,
        1,
        LIṄGA_PUM,
        tRtIyA_tatpurusha_samAsa=True,
    )


def derive_mAsapUrvAya_caturthI_eka() -> State:
    """*māsa* + *pūrv* *tṛtīyā* *tatpuruṣa* (one month before), *caturthī* *eka*."""
    return _derive(STEM_MASA_PURVA)


def derive_dvyahapUrvAya_caturthI_eka() -> State:
    """*dvyah* + *pūrv* (two days before) — *śabda* *id* includes internal *dvyaha* *sandhi*."""
    return _derive(STEM_DVYAHA_PURVA)


def derive_tryahapUrvAya_caturthI_eka() -> State:
    """*tryah* + *pūrv* (three days before) — *śabda* *id* ``tryaha-`` in *sarvādi* *list*."""
    return _derive(STEM_TRYAHA_PURVA)


__all__ = [
    "STEM_DVYAHA_PURVA",
    "STEM_MASA_PURVA",
    "STEM_TRYAHA_PURVA",
    "LIṄGA_PUM",
    "derive_dvyahapUrvAya_caturthI_eka",
    "derive_mAsapUrvAya_caturthI_eka",
    "derive_tryahapUrvAya_caturthI_eka",
]
