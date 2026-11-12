"""3.4.110 AtaH (luG, sic luk'd: asTuH, apuH) and 3.4.111 laNaH SAkawAyanasyEva (laG: aruH beside arAn), each reached by the sutra, then 6.1.96."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive


def _r(dhatu, lakara):
    return {b.surface_slp1: {t["sutra_id"] for t in b.state.trace if t.get("status") == "APPLIED"} for b in explore(lambda: derive(dhatu, lakara, "kartari", 3, 3))}


def test_luG_3pl_after_A_root_sic_luk():
    for d, f in (("01.1077", "asTuH"), ("01.1074", "apuH")):
        r = _r(d, "luG")
        assert f in r and {"2.4.77", "3.4.110", "6.1.96"} <= r[f]


def test_laG_3pl_after_A_root_is_vibhasha():
    r = _r("02.0052", "laG")
    assert "aruH" in r and "3.4.111" in r["aruH"] and "arAn" in r and "3.4.111" not in r["arAn"]
