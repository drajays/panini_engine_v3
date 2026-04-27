"""
*सर्व* — one *prakriyā* for all 24 *sup* cells: ``derive_sarva_pulliṅga`` (``pipelines/sarva_subanta``).
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest
import sutras  # noqa: F401

from engine.trace import TRACE_STATUSES_FIRED
from phonology.joiner import slp1_to_devanagari
from pipelines.sarva_subanta import (
    SARVA_PUM_24_CELLS,
    derive_sarva_pulliṅga,
    iter_sarva_paradigm,
    sarva_cell_key,
)
from pipelines.subanta import derive


def _gold_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "data"
        / "reference"
        / "subanta_gold"
        / "sarva_pullinga.json"
    )


def test_derive_sarva_same_as_subanta_derive():
    s1 = derive_sarva_pulliṅga(2, 3)
    s2 = derive("sarva", 2, 3, "pulliṅga")
    assert s1.flat_slp1() == s2.flat_slp1()
    assert s1.render() == s2.render()


def test_24_cells_match_reference_gold():
    with _gold_path().open(encoding="utf-8") as f:
        data = json.load(f)
    cells = data["cells"]
    for v, vac in SARVA_PUM_24_CELLS:
        st = derive_sarva_pulliṅga(v, vac)
        key = sarva_cell_key(v, vac)
        dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
        assert dev == cells[key]["form_dev"], key


def test_iter_sarva_paradigm_length_and_keys():
    t = iter_sarva_paradigm()
    assert len(t) == 24
    assert {k for k, _ in t} == {f"{v}-{vv}" for v in range(1, 9) for vv in range(1, 4)}


def _fired_sutra_ids(s):
    return {
        e["sutra_id"]
        for e in s.trace
        if e.get("sutra_id")
        and e.get("status") in TRACE_STATUSES_FIRED
        and not str(e.get("sutra_id", "")).startswith("__")
    }


@pytest.mark.parametrize("must", ("1.1.27", "1.2.45", "7.1.17", "6.1.87"))
def test_sarve_prathama_bahu_key_rules(must: str):
    """
    *सर्वे* (1-3): *sarvanāma* + *jasaḥ śī* + *guṇa* (user ``सर्वे .md``).

    4.1.2 is *ADHIKARA* (often ``AUDIT`` in trace, not a "fired" *vidhi*).
    """
    s = derive_sarva_pulliṅga(1, 3)
    ids = _fired_sutra_ids(s)
    assert must in ids, f"missing {must} in {sorted(ids)}"


def test_sarve_surface_slp1_sarve():
    s = derive_sarva_pulliṅga(1, 3)
    assert s.flat_slp1() == "sarve"
    assert s.render() == "sarve"


# --- *सर्वेषाम्* (6-3) user ``सर्वेषाम्.md``: *suṭ* + *sAm* + *7.3.103* *e* + *8.3.59* *ṣ* ---


def _trace_sutra_statuses(s) -> dict[str, str]:
    """Last occurrence of each *sūtra* id in the trace (latest wins for repeated rows)."""
    out: dict[str, str] = {}
    for e in s.trace:
        sid = e.get("sutra_id")
        if not sid or str(sid).startswith("__"):
            continue
        if e.get("status") is not None:
            out[str(sid)] = e["status"]
    return out


def _first_trace_index(s, sid: str) -> int:
    for i, e in enumerate(s.trace):
        if e.get("sutra_id") == sid:
            return i
    return -1


def test_sarveShAm_6_3_surface_matches_gold():
    s = derive_sarva_pulliṅga(6, 3)
    with _gold_path().open(encoding="utf-8") as f:
        expected_dev = json.load(f)["cells"]["6-3"]["form_dev"]
    assert s.flat_slp1() == "sarvezAm"
    assert slp1_to_devanagari(s.terms[0].varnas) == expected_dev
    assert expected_dev == "सर्वेषाम्"


def test_sarveShAm_6_3_vidhi_chain_order_su7_e7_sha8():
    s = derive_sarva_pulliṅga(6, 3)
    i52 = _first_trace_index(s, "7.1.52")
    i103 = _first_trace_index(s, "7.3.103")
    i859 = _first_trace_index(s, "8.3.59")
    assert -1 < i52 < i103 < i859
    st = _trace_sutra_statuses(s)
    assert st.get("7.1.52") == "APPLIED"
    assert st.get("7.3.103") == "APPLIED"
    assert st.get("8.3.59") == "APPLIED"
    assert st.get("7.1.54") == "SKIPPED"


def test_viSveShAm_6_3_parallel_sarveShAm():
    s = derive("viSva", 6, 3, "pulliṅga")
    assert s.flat_slp1() == "viSvezAm"
    assert slp1_to_devanagari(s.terms[0].varnas) == "विश्वेषाम्"


def test_rAma_6_3_contrast_nu7_not_7_1_52_su7():
    s = derive("rAma", 6, 3, "pulliṅga")
    st = _trace_sutra_statuses(s)
    assert st.get("7.1.54") == "APPLIED"
    assert st.get("7.1.52") == "SKIPPED"
    assert s.flat_slp1() == "rAmARAm"
