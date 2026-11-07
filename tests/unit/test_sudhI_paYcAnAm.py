"""suDI + jas → suDiyaH (the lexicon gives suDI its dhātu DIN: 6.4.85 stops yaṇ, 6.4.77 iyaṅ); the loop alone reaches paYcAnAm (8.2.7 in the merged pada)."""
from types import SimpleNamespace as N

from pipelines.subanta import derive
from tools.autonomy_report import run_autonomously, start_state


def test_sudhI_jas_iyan():
    assert derive("suDI", 1, 3, "pulliṅga").flat_slp1() == "suDiyaH"
    assert derive("suDI", 1, 1, "pulliṅga").flat_slp1() == "suDIH"


def test_loop_paYcan_nam_nalopa():
    r = run_autonomously(start_state(N(kind="subanta", args=("paYcan", 6, 3, "pulliṅga"))), "paYcAnAm", "paYcan", 300)
    assert r.surface == "paYcAnAm" and any(x[0] == "8.2.7" for x in r.steps)
    r = run_autonomously(start_state(N(kind="subanta", args=("rAjan", 3, 3, "pulliṅga"))), "rAjaBiH", "rAjan", 300)
    assert r.surface == "rAjaBiH"
