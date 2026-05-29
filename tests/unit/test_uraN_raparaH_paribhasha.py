"""Unit tests for ``pipelines/uraN_raparaH_paribhasha_P010_demo.py`` (**P010**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.uraN_raparaH_paribhasha_P010_demo import (
    derive_uraN_raparaH_paribhasha_P010_demo,
)


def test_P010_uraN_raparaH_two_illustrations_in_trace():
    s = derive_uraN_raparaH_paribhasha_P010_demo()

    applied_1151 = [x for x in s.trace if x.get("sutra_id") == "1.1.51" and x.get("status") == "APPLIED"]
    assert len(applied_1151) == 2

    # First: after 7.3.84 + 1.1.51, the demonstration target is kar (dhātu tape only).
    assert "kar" in (applied_1151[0].get("form_after") or "")

    # Second: vṛddhi illustration on A-substitute tape.
    assert applied_1151[1].get("form_after") == "kAr"

