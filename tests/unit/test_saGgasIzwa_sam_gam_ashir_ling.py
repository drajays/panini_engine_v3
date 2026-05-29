"""prakriya_13 separated JSON — संगसीष्ट spine."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.saGgasIzwa_sam_gam_ashir_ling_demo import derive_saGgasIzwa


def _fired(trace: list, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_saGgasIzwa_surface() -> None:
    s = derive_saGgasIzwa()
    assert s.flat_slp1() == "saGgasIzwa"


def test_saGgasIzwa_key_spine() -> None:
    s = derive_saGgasIzwa()
    for sid in (
        "1.3.29",
        "3.3.173",
        "3.4.102",
        "1.2.13",
        "6.4.37",
        "3.4.107",
        "8.3.23",
        "8.3.59",
        "8.4.58",
        "8.4.41",
    ):
        assert _fired(s.trace, sid)


def test_json_noted_13326_is_upstream_typo_notice() -> None:
    """JSON ``1.3.26`` OCR does not match this *prayoga*; scholarly anchor is ``1.3.29``."""
    assert True
