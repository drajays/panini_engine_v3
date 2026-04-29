"""
pipelines/subanta_trc.py — *tṛc* prātipadika + *subanta* (continuous *State*).

**Zero-patchwork:** no ``trc_nom_sg_pipeline`` meta, no ``apply_rule`` scripts.
The kṛdanta merge tags the stem with ``krt_tfc`` (see ``krdanta._structural_merge_trc_pratipadika``);
sūtras **7.1.94**, **6.4.11**, **6.1.66**, **8.2.7** self-gate on that tag + tape shape.
All execution goes through ``pipelines.subanta`` (``apply_rule`` only).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State

from pipelines.subanta import build_initial_state, derive_from_state


def derive_trc_nom_sg(
    stem_slp1: str,
    *,
    vibhakti: int = 1,
    vacana: int = 1,
    linga: str = "pulliṅga",
) -> State:
    """
    *Subanta* on a *tṛc* stem string (e.g. ``cetf``): same motor as ``derive``,
    provided the stem carries ``krt_tfc`` when coming from ``derive_tfc_pratipadika``.

    For a bare string like ``cetf`` without ``krt_tfc``, use
    ``derive_trc_nom_sg_from_state`` after building *State* upstream.
    """
    s = build_initial_state(stem_slp1, vibhakti, vacana, linga)
    return derive_trc_nom_sg_from_state(s, vibhakti=vibhakti, vacana=vacana, linga=linga)


def derive_trc_nom_sg_from_state(
    s: State,
    *,
    vibhakti: int = 1,
    vacana: int = 1,
    linga: str = "pulliṅga",
) -> State:
    """
    Continue *subanta* on an existing *State* (kṛdanta → subanta) without
    flattening. Requires ``krt_tfc`` on the prātipadika *Term* from the tṛc merge.
    """
    return derive_from_state(s, vibhakti, vacana, linga=linga)


__all__ = [
    "derive_trc_nom_sg",
    "derive_trc_nom_sg_from_state",
]
