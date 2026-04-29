"""
*प्रियविश्वाय* — *bahuvrīhi* *sarvādi* *upadeśa* with **1.1.29** *na bahuvrīhau* (user ``प्रियविश्वाय.md``).

The *prakṛti* is the list form ``priya-viSva`` in ``data/inputs/sarvadi_slp1.json`` (ASCII hyphen: skipped in
*varṇa* *parse*; full string is **1.1.27** *sarvādi* id).  The *bahuvrīhi* tag must
arrive on the `State` (samāsa memory); this pipeline is a thin wrapper that
supplies the tag structurally for the user note.
**1.1.27** then **1.1.29** give *no* *sarvanāma*; **7.1.14** is inert, **7.1.13** + **7.3.102** → *priyaviśvāya* / ``priyaviSvAya``.

*CONSTITUTION*: *meta* *arm* is the *bahuvrīhī* *tag* on the stem (set only by *recipe* / ``build_initial_state``), not
a *cond* read of *siddha* *vivakṣā* strings; *no* *gold* in the engine.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State
from pipelines.subanta import build_initial_state, derive_from_state

STEM_PRIYA_VISHVA_SLP1: str = "priya-viSva"
LIṄGA_PUM: str = "pulliṅga"


def derive_priyaviSvAya_caturthI_eka() -> State:
    """
    *sampadāna* *eka* of the *bahuvrīhī* *prakṛti* (vigraha: *priyā viśve yasya*).
    """
    s = build_initial_state(STEM_PRIYA_VISHVA_SLP1, 4, 1, LIṄGA_PUM)
    if s.terms:
        s.terms[0].tags.add("bahuvrihi")
    return derive_from_state(s, 4, 1, linga=LIṄGA_PUM)


__all__ = [
    "STEM_PRIYA_VISHVA_SLP1",
    "LIṄGA_PUM",
    "derive_priyaviSvAya_caturthI_eka",
]
