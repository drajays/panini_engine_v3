"""1.3.9 तस्य लोपः removes only what an it-saṃjñā sūtra has named: every anunāsika ac that 1.3.9 drops was first
named it by 1.3.2 उपदेशेऽजनुनासिक इत् as its own applied step on the same tape — e.g. स्कुदिँ: 1.3.2 (इँ इत्) → 1.3.9
स्कुद्. The licensing 1.3.2 step carries ``licenses = "1.3.9"`` so every trace view shows the pair."""
from __future__ import annotations

from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state

_ROOTS = [r["id"] for r in iter_dhatu_entries() if r.get("gana") == 1 and "~" in r["upadesha_slp1"]][:60]


def _anunasika_lopas(trace):
    for k, s in enumerate(trace):
        if s.get("sutra_id") == "1.3.9" and s.get("status") == "APPLIED" \
                and (s.get("form_before") or "").count("~") > (s.get("form_after") or "").count("~"):
            yield k, s


def _assert_named_first(trace, label):
    for k, lopa in _anunasika_lopas(trace):
        prior = [s for s in trace[:k] if s.get("sutra_id") == "1.3.2" and s.get("status") == "APPLIED"
                 and s.get("form_after") == lopa.get("form_before")]
        assert prior, f"{label}: 1.3.9 removed an anunāsika ac from {lopa.get('form_before')} with no 1.3.2 before it"
        assert prior[-1].get("licenses") == "1.3.9", f"{label}: the licensing 1.3.2 is not marked"


def test_skudi_pair():
    run = run_autonomously(start_state(NS(kind="tinanta", args=("skudi~", "laT", 3, 1), pada=None)), "", "skudi~", 250)
    rows = [(s["sutra_id"], s["form_before"], s["form_after"]) for s in run.state.trace
            if s.get("sutra_id") in ("1.3.2", "1.3.9") and s.get("status") == "APPLIED"]
    assert rows[:2] == [("1.3.2", "skudi~", "skudi~"), ("1.3.9", "skudi~", "skud")]
    _assert_named_first(run.state.trace, "skudi~")


@pytest.mark.parametrize("ref", _ROOTS)
def test_every_dhatu_anunasika_lopa_follows_1_3_2(ref):
    _assert_named_first(start_state(NS(kind="tinanta", args=(ref, "laT", 3, 1), pada=None)).trace, ref)


@pytest.mark.parametrize("stem,vib,vac", [("rAma", 1, 1), ("hari", 1, 1), ("rAma", 7, 3)])
def test_sup_anunasika_lopa_follows_1_3_2(stem, vib, vac):
    from pipelines.subanta import derive
    _assert_named_first(derive(stem, vib, vac).trace, f"{stem} {vib}-{vac}")


def test_recipe_path_too():
    from pipelines.tinanta import derive
    _assert_named_first(derive("BvAdi_01_0002", "laT", "kartari", 3, 1).trace, "eDa~ recipe")
