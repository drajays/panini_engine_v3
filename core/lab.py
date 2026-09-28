"""
core/lab.py — the local test panel: one paradigm, engine vs Vidyut, cell by cell.

``grid()`` derives every cell of a tiṅanta (9) or subanta (24) paradigm, asks
Vidyut for the same cells in one batch (``bench/oracle_batch`` under the repo's
``.venv``), and marks each cell agree / disagree / engine-error / oracle-silent.
A cell's derivation is fetched separately (``/v1/tinanta``, ``/v1/subanta``).

Presentation/test code only: never imported by engine / sutras / phonology / pipelines.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from core.practice import cell_label

_ROOT = Path(__file__).resolve().parent.parent
_VENV_PY = _ROOT / ".venv" / "bin" / "python"
_LINGA = {"pulliṅga": "pum", "strīliṅga": "stri", "napuṃsaka": "napumsaka"}
LAKARAS = ["laT", "liT", "luT", "lRT", "loT", "laG", "liG", "AsIrliG", "luG", "lRG"]


def _oracle(cells: list[dict]) -> list[list[str]] | None:
    """Vidyut forms per cell, or None when the oracle isn't available."""
    if not _VENV_PY.exists():
        return None
    try:
        r = subprocess.run([str(_VENV_PY), "-m", "bench.oracle_batch"], cwd=_ROOT,
                           input=json.dumps(cells), capture_output=True, text=True, timeout=120)
        return json.loads(r.stdout) if r.returncode == 0 else None
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return None


def grid(kind: str, lemma: str, *, lakara: str = "laT", prayoga: str = "kartari",
         pada: str | None = None, linga: str = "pulliṅga") -> dict[str, Any]:
    from core.transliterate import slp1_to_dev

    cells, oracle_cells, meta = [], [], {}
    if kind == "tinanta":
        from pipelines.dhatupatha import resolve_dhatu_identifier
        from pipelines.tinanta import derive
        row = resolve_dhatu_identifier(lemma)
        up, path_id = row["upadesha_slp1"], row.get("dhatupatha_id") or ""
        meta = {"upadesha": up, "mula_dev": row.get("mula_dhatu_dev", ""), "path_id": path_id,
                "gana": row.get("gana"), "artha_dev": row.get("artha_dev", ""),
                "pada_dev": row.get("pada_label_dev", "")}
        kw = {"pada": pada} if pada else {}
        for purusha in (3, 2, 1):
            for vacana in (1, 2, 3):
                f = {"lakara": lakara, "prayoga": prayoga, "purusha": purusha, "vacana": vacana}
                cells.append((f, lambda f=f: derive(up, lakara, prayoga, f["purusha"], f["vacana"], **kw)))
                oracle_cells.append({"kind": "tinanta", "dhatu": up, "path_id": path_id, **f})
    else:
        from pipelines.subanta import derive
        meta = {"stem": lemma, "stem_dev": slp1_to_dev(lemma), "linga": linga}
        for vibhakti in range(1, 9):
            for vacana in (1, 2, 3):
                f = {"vibhakti": vibhakti, "vacana": vacana, "linga": linga}
                cells.append((f, lambda f=f: derive(lemma, f["vibhakti"], f["vacana"], linga=linga)))
                oracle_cells.append({"kind": "subanta", "stem": lemma, "linga": _LINGA[linga],
                                     "vibhakti": vibhakti, "vacana": vacana})

    theirs = _oracle(oracle_cells)
    out = []
    for i, (f, run) in enumerate(cells):
        c: dict[str, Any] = {"features": f, "label": cell_label(kind, f)}
        try:
            s = run()
            c |= {"slp1": s.flat_slp1(), "dev": s.flat_dev(), "steps": len(s.trace)}
        except Exception as ex:
            c["error"] = f"{type(ex).__name__}: {ex}"[:240]
        v = theirs[i] if theirs is not None else None
        c["vidyut"] = [{"slp1": x, "dev": slp1_to_dev(x)} for x in v] if v else []
        c["status"] = ("error" if "error" in c else "no-oracle" if theirs is None
                       else "oracle-silent" if not v else "agree" if c["slp1"] in v else "disagree")
        out.append(c)
    tally = {k: sum(c["status"] == k for c in out)
             for k in ("agree", "disagree", "error", "oracle-silent", "no-oracle")}
    return {"kind": kind, "input": {"lemma": lemma, "lakara": lakara, "prayoga": prayoga,
                                    "pada": pada, "linga": linga},
            "meta": meta, "cells": out, "tally": tally, "oracle": theirs is not None}


if __name__ == "__main__":   # smoke check
    g = grid("tinanta", "eDa~", lakara="laG")
    assert len(g["cells"]) == 9 and g["oracle"], g["tally"]
    assert g["cells"][0]["status"] == "agree", g["cells"][0]       # ऐधत
    g = grid("subanta", "rAma")
    assert len(g["cells"]) == 24 and g["tally"]["agree"] >= 20, g["tally"]
    print("ok", g["tally"])
