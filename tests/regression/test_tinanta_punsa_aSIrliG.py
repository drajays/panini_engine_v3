"""6.4.24 does not fire on a ṇic-lopa'd aṅga (1.1.62 sthānivat): puMsa~ āśīrliṅ → puMsyAt, not *pusyAt. Vidyut agrees."""
from types import SimpleNamespace as NS

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


def test_punsa_AsIrliG():
    r = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == "punsa~" and r.get("gana") == 10)
    ref = r.get("id") or "punsa~"
    assert run_autonomously(start_state(NS(kind="tinanta", args=(ref, "AsIrliG", 3, 1), pada="parasmai")), "", ref, 250).surface == "puMsyAt"
