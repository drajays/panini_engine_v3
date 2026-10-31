"""Art. 25 / AMENDMENT 29: vārttikas live inside their host sūtra — schema, source text, trace, tier switch."""
import sqlite3
from pathlib import Path

import pytest

import sutras  # noqa: F401
from engine.registry import SUTRA_REGISTRY
from engine.tape_init.taddhita import build_taddhita_state
from engine.vartika import RELATIONS, TIERS, Vartika, disabled_tiers, paribhasha_ids, validate
from tools.autonomy_report import run_autonomously

DB = Path.home() / "data-master/ashtadhyayi-ai/db/ashtadhyayi.db"
HOSTS = [r for r in SUTRA_REGISTRY.values() if r.vartikas]


def test_a_host_exists():
    assert "4.2.43" in {r.sutra_id for r in HOSTS}


@pytest.mark.parametrize("rec", HOSTS, ids=lambda r: r.sutra_id)
def test_schema_and_dated_source(rec):
    validate(rec.sutra_id, rec.vartikas)
    for v in rec.vartikas:
        assert isinstance(v, Vartika) and v.tier in TIERS and v.relation in RELATIONS and set(v.paribhasha) <= paribhasha_ids()
        if DB.exists():     # cite, do not invent: the words are the DB's (vartika table, or the Bhāṣya's own quotation)
            con = sqlite3.connect(DB)
            rows = con.execute(
                "select content from texts where sutra_id=? and source in ('vartika','bhashya')", (rec.sutra_id,)).fetchall()
            con.close()
            assert any(v.text_dev in c[0] for c in rows), v.id


def test_bad_entries_are_refused():
    ok = Vartika("4.2.43.v9", "x", "T1", "extension", "x", lambda s: False, lambda s: s)
    validate("4.2.43", (ok,))
    for bad in (Vartika("4.2.44.v1", "x", "T1", "extension", "x", ok.cond, ok.act),
                Vartika("4.2.43.v9", "x", "T7", "extension", "x", ok.cond, ok.act),
                Vartika("4.2.43.v9", "x", "T1", "private-priority", "x", ok.cond, ok.act),
                Vartika("4.2.43.v9", "x", "T1", "extension", "x", ok.cond, ok.act, paribhasha=("PS9999",))):
        with pytest.raises(ValueError):
            validate("4.2.43", (bad,))


def _run(stem):
    s = build_taddhita_state(stem, None, taddhitArtha="samUha")
    s.phase = "upadesha"
    return run_autonomously(s, "", stem, 300, stop_before_tripadi=True)


def test_trace_names_host_and_vartika_and_switch_off():
    run = _run("parSu")
    assert run.surface == "pArSva"
    row = next(x for x in run.state.trace if x.get("vartika"))
    assert row["sutra_id"] == "4.2.43" and row["vartika"] == "4.2.43.v4" and row["vartika_label"] == "4.2.43 + vā. 4"
    assert row["vartika_tier"] == "T1"
    with disabled_tiers("T1"):
        assert "4.2.43" not in [x[0] for x in _run("parSu").steps]
    assert _run("grAma").surface == "grAmata"      # the host's own path is untouched
