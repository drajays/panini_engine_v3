"""7.2.35 ārdhadhātukasyeḍ valādeḥ before 7.4.49 saḥ syārdhadhātuke: a seṭ root with s-final keeps the s (asa~ lṛṭ asiṣyati, not *atiṣyati);
an aniṭ root still gets the t (ghas -> ghatsyati stays on the loop path of its own tests)."""
from types import SimpleNamespace as NS

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


def test_asa_lRT_has_is_not_t():
    ref = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == "asa~" and r.get("gana") == 1)["id"]
    got = run_autonomously(start_state(NS(kind="tinanta", args=(ref, "lRT", 3, 1), pada="parasmai")), "", ref, 250).surface
    assert got == "asizyati"
