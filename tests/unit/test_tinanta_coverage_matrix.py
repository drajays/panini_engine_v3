"""
T1 — Tiṅanta coverage matrix (audit_tinanta_cursor.md §3).

Records OK / NI (NotImplemented) / ERR / SKIP (unknown dhātu) for a fixed
smoke set × 10 lakāras × 3 prayogas × 9 cells.  Writes a JSON artifact when
``PANINI_WRITE_AUDIT_ARTIFACT=1`` (see ``write_coverage_artifact``).
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
from typing import Any

import pytest

from pipelines.tinanta import derive

_REPO = Path(__file__).resolve().parents[2]
_AUDIT_DIR = _REPO / ".audit"

LAKARAS = (
    "laT", "liT", "luT", "lRT", "loT", "laG", "liG", "AsIrliG", "luG", "lRG",
)
PRAYOGAS = ("kartari", "karmani", "bhave")
PURUSHA = (3, 2, 1)
VACANA = (1, 2, 3)

# audit_tinanta_cursor.md §0 — upadeśa SLP1 from dhatupatha_upadesha.json
DHATU_SMOKE = ("BU", "paci~", "kfvi~")


def _classify(dhatu: str, lakara: str, prayoga: str, purusha: int, vacana: int) -> dict[str, Any]:
    try:
        state = derive(dhatu, lakara, prayoga, purusha, vacana)
        surf = state.flat_dev()
        if not surf:
            return {"status": "EMPTY", "surface_dev": "", "surface_slp1": state.flat_slp1()}
        return {
            "status": "OK",
            "surface_dev": surf,
            "surface_slp1": state.flat_slp1(),
        }
    except NotImplementedError as e:
        return {"status": "NI", "error": str(e)}
    except KeyError as e:
        return {"status": "SKIP", "error": str(e)}
    except Exception as e:
        return {"status": "ERR", "error": f"{type(e).__name__}: {e}"}


def build_coverage_matrix(*, full_paradigm: bool = True) -> dict[str, Any]:
    cells: list[dict[str, Any]] = []
    counts: dict[str, int] = {"OK": 0, "NI": 0, "ERR": 0, "SKIP": 0, "EMPTY": 0}

    pu_va = list(product(PURUSHA, VACANA)) if full_paradigm else [(3, 1)]

    for dhatu, prayoga, lakara in product(DHATU_SMOKE, PRAYOGAS, LAKARAS):
        for purusha, vacana in pu_va:
            row = {
                "dhatu": dhatu,
                "prayoga": prayoga,
                "lakara": lakara,
                "purusha": purusha,
                "vacana": vacana,
            }
            row.update(_classify(dhatu, lakara, prayoga, purusha, vacana))
            cells.append(row)
            counts[row["status"]] = counts.get(row["status"], 0) + 1

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "full_paradigm": full_paradigm,
        "dhatu_smoke": list(DHATU_SMOKE),
        "counts": counts,
        "cells": cells,
    }


def write_coverage_artifact(matrix: dict[str, Any] | None = None) -> Path:
    _AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = _AUDIT_DIR / f"tinanta_matrix_{stamp}.json"
    path.write_text(
        json.dumps(matrix or build_coverage_matrix(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


@pytest.fixture(scope="module")
def coverage_matrix() -> dict[str, Any]:
    return build_coverage_matrix(full_paradigm=True)


def test_bhu_kartari_all_lakaras_3sg_ok(coverage_matrix: dict[str, Any]) -> None:
    """Regression guard: भू kartari 3sg must succeed for every lakāra."""
    fails: list[str] = []
    for lak in LAKARAS:
        hit = next(
            (
                c
                for c in coverage_matrix["cells"]
                if c["dhatu"] == "BU"
                and c["prayoga"] == "kartari"
                and c["lakara"] == lak
                and c["purusha"] == 3
                and c["vacana"] == 1
            ),
            None,
        )
        if not hit or hit["status"] != "OK":
            fails.append(f"{lak}:{hit and hit['status']}")
    assert not fails, f"BU kartari 3sg failures: {fails}"


def test_smoke_matrix_no_regressions_on_bhvadi_kartari(coverage_matrix: dict[str, Any]) -> None:
    """BU × kartari: at least 90% of full paradigm cells are OK."""
    rows = [
        c
        for c in coverage_matrix["cells"]
        if c["dhatu"] == "BU" and c["prayoga"] == "kartari"
    ]
    ok = sum(1 for c in rows if c["status"] == "OK")
    assert ok >= int(0.9 * len(rows)), f"BU kartari OK {ok}/{len(rows)}"


def test_smoke_matrix_bhave_lat_liT_ok(coverage_matrix: dict[str, Any]) -> None:
    """भू bhāve laṭ/liṭ 3sg must derive (T4 precursor)."""
    for lak in ("laT", "liT"):
        hit = next(
            c
            for c in coverage_matrix["cells"]
            if c["dhatu"] == "BU" and c["prayoga"] == "bhave" and c["lakara"] == lak
            and c["purusha"] == 3 and c["vacana"] == 1
        )
        assert hit["status"] == "OK", hit


def test_coverage_matrix_summary_logged(coverage_matrix: dict[str, Any], capsys: pytest.CaptureFixture[str]) -> None:
    """Emit summary counts for human / CI logs."""
    c = coverage_matrix["counts"]
    total = sum(c.values())
    print(
        f"TINANTA_MATRIX total={total} OK={c.get('OK',0)} NI={c.get('NI',0)} "
        f"ERR={c.get('ERR',0)} SKIP={c.get('SKIP',0)} EMPTY={c.get('EMPTY',0)}"
    )
    if os.environ.get("PANINI_WRITE_AUDIT_ARTIFACT") == "1":
        p = write_coverage_artifact(coverage_matrix)
        print(f"TINANTA_MATRIX artifact={p}")


@pytest.mark.parametrize("dhatu", ("paci~", "kfvi~"))
def test_sakarmaka_kartari_lat_3sg_ok(dhatu: str, coverage_matrix: dict[str, Any]) -> None:
    hit = next(
        c
        for c in coverage_matrix["cells"]
        if c["dhatu"] == dhatu and c["prayoga"] == "kartari" and c["lakara"] == "laT"
        and c["purusha"] == 3 and c["vacana"] == 1
    )
    assert hit["status"] == "OK", hit
