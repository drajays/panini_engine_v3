"""वैपाशः — *vipAS* + *Ni* + *aṇ* (*tatra-bhava*, note: वैपाशः.md)."""

from __future__ import annotations

from pipelines.vaipASaH_vipAS_tatra_bhava import derive_vaipASaH, derive_vaipASa_pratipadika


def test_vaipASa_pratipadika():
    s = derive_vaipASa_pratipadika()
    assert s.flat_slp1().strip() == "vEpASa"


def test_vaipASaH_final():
    s = derive_vaipASaH()
    assert s.flat_slp1().strip() == "vEpASaH"


def test_trace_key_steps():
    s = derive_vaipASaH()
    ids = [row.get("sutra_id") for row in s.trace]
    for need in ("2.3.36", "4.3.53", "7.2.117", "6.4.129", "6.4.148"):
        assert need in ids
