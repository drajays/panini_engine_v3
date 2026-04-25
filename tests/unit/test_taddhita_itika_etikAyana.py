"""*itika* + *phak* → *EtikAyana* / *EtikAyanaH* (``pipelines/taddhita_itika_etikAyana``)."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.taddhita_itika_etikAyana import (
    derive_EtikAyana_subanta,
    derive_full_itika_EtikAyanaH,
    derive_taddhita_itika_EtikAyana,
    validate_trace_against_whitelist,
)


def test_taddhita_EtikAyana_surface():
    s = derive_taddhita_itika_EtikAyana()
    assert s.flat_slp1() == "EtikAyana"
    assert "Etik" in "".join(v.slp1 for v in s.terms[0].varnas)
    from engine.trace import TRACE_STATUSES_FIRED

    tids = [
        e.get("sutra_id") for e in s.trace
        if e.get("status") in TRACE_STATUSES_FIRED and e.get("sutra_id") != "__MERGE__"
    ]
    for need in (
        "4.1.82", "4.1.92", "4.1.99", "1.2.46", "2.4.71",
        "1.4.13", "7.1.2", "1.3.10", "7.2.118", "1.4.18", "6.4.129", "6.4.148",
    ):
        assert need in tids, f"missing {need} in {tids}"
    assert tids.index("7.1.2") < tids.index("7.2.118")
    assert tids.index("1.4.18") < tids.index("6.4.129") < tids.index("6.4.148")
    oob = validate_trace_against_whitelist(s)
    assert oob == [], f"off-whitelist: {oob}"


def test_subanta_EtikAyanaH_nominative():
    s = derive_EtikAyana_subanta()
    assert s.flat_slp1() == "EtikAyanaH"
    from engine.trace import TRACE_STATUSES_FIRED

    tids = [
        e.get("sutra_id") for e in s.trace
        if e.get("status") in TRACE_STATUSES_FIRED and e.get("sutra_id") != "__MERGE__"
    ]
    for need in ("6.1.72", "8.1.16", "8.2.1", "8.2.66", "8.3.15"):
        assert need in tids, f"missing {need} in {tids}"


def test_full_prakriya_both_stages():
    t, b = derive_full_itika_EtikAyanaH()
    assert t.flat_slp1() == "EtikAyana"
    assert b.flat_slp1() == "EtikAyanaH"
