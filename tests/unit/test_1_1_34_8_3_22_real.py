"""1.1.34 pūrvādi jas vibhāṣā (pūrve / pūrvāḥ, Kāśikā) and 8.3.22 hali sarveṣām as the apavāda of 8.3.19/20 before a haś (Bho janāḥ)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.pada_samhita import join_tripadi
from pipelines.subanta import derive


def _readings(f):
    return {b.surface_slp1: {t["sutra_id"] for t in b.state.trace if t.get("status") == "APPLIED"} for b in explore(f)}


def test_purva_jasi_both_readings_via_1_1_34():
    r = _readings(lambda: derive("pUrva", 1, 3))
    assert "pUrve" in r and "pUrvAH" in r
    assert "1.1.34" in r["pUrvAH"] and "7.1.17" not in r["pUrvAH"]
    assert "7.1.17" in r["pUrve"]


def test_samjna_use_is_never_sarvanama():
    r = _readings(lambda: derive("uttara", 1, 3, arthaViSeSa="saMjYA"))
    assert "uttarAH" in r and "uttare" not in r


def test_bho_janah_8_3_22_not_8_3_20():
    r = _readings(lambda: join_tripadi("Bos", "janAH"))
    ids = next(v for k, v in r.items() if k == "BojanAH")
    assert "8.3.22" in ids and "8.3.20" not in ids
    ids = next(v for k, v in _readings(lambda: join_tripadi("Bos", "atra")).items() if k == "Boatra")
    assert "8.3.20" in ids          # before an aś that is not a haś 8.3.20 still does it
