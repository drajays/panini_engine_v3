"""śālīyaḥ (SAlIyaH) — taddhita + subanta (prathamā ekavacana)."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.taddhita_salIya import derive_salIyaH


def test_salIyaH_surface_and_tripadi():
    s = derive_salIyaH()
    assert s.flat_slp1() == "SAlIyaH"
    from engine.trace import TRACE_STATUSES_FIRED

    tids = [
        e.get("sutra_id") for e in s.trace
        if e.get("status") in TRACE_STATUSES_FIRED and e.get("sutra_id") != "__MERGE__"
    ]
    # sup attach + it-lopa + pada + tripadi
    for need in ("4.1.2", "1.3.2", "1.3.9", "1.4.14", "8.2.66", "8.3.15"):
        assert need in tids, f"missing {need}"
    all_ids = [e.get("sutra_id") for e in s.trace]
    assert all_ids.count("1.1.61") == 1
    assert all_ids.index("2.4.71") < all_ids.index("1.1.61")

