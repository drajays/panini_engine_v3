"""7.2.37 grahoṅaliṭi dīrghaḥ (Kāśikā): the iṭ after grah is ī except in liṭ — grahītā, grahīṣyati, agrahīt, agrahīṣam; liṭ keeps it short (jagrahiva);
a ṇic between (grāhitā) is not 'the iṭ of grah'."""
from types import SimpleNamespace as N

import pytest

import sutras  # noqa: F401
from pipelines.tinanta import derive
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("lakara,purusha,vacana,gold", [("luT", 3, 1, "grahItA"), ("lRT", 3, 1, "grahIzyati"), ("lRG", 3, 1, "agrahIzyat"),
                                                           ("luG", 3, 1, "agrahIt"), ("luG", 1, 1, "agrahIzam"), ("luG", 3, 3, "agrahIzuH")])
def test_grah_iT_is_dirgha(lakara, purusha, vacana, gold):
    assert derive("graha~", lakara, "kartari", purusha, vacana).flat_slp1() == gold                       # the recipe
    r = run_autonomously(start_state(N(kind="tinanta", args=("graha~", lakara, purusha, vacana))), gold, "x", 300)
    assert r.surface == gold and r.outcome == "reached"                                                 # the loop


def test_lit_and_other_roots_unmoved():
    assert derive("graha~", "liT", "kartari", 3, 1).flat_slp1() == "jagrAha"
    assert derive("gupU~", "luT", "kartari", 3, 1).flat_slp1() == "gopitA" and derive("lUY", "luT", "kartari", 3, 1).flat_slp1() == "lavitA"


def test_7_2_37_is_applied():
    s = derive("graha~", "luT", "kartari", 3, 1)
    assert any(r.get("sutra_id") == "7.2.37" and r.get("status") == "APPLIED" for r in s.trace if isinstance(r, dict))
