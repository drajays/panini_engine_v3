"""The pāṭha inventory runs, covers every pāṭha the design names, and the intake of the pāṭhas from the reference brain holds its counts."""
import json
from pathlib import Path

from tools.patha_inventory import BASELINE, inventory, missing

IN = Path(__file__).resolve().parents[2] / "data" / "inputs"


def _by():
    return {r["pATha"]: r for r in inventory()}


def _j(name):
    return json.loads((IN / name).read_text(encoding="utf-8"))


def test_core_pathas_present_and_nonempty():
    r = _by()
    assert r["DhAtupAWa"]["entries"] >= 1900
    assert r["gaRapAWa (full)"]["entries"] >= 200
    assert r["dhAtupAWa gaRasUtra"]["entries"] == 30


def test_no_new_sutra_names_a_list_without_data():
    """Ratchet: a sūtra that names a list with no data and no decision fails here unless it is in the baseline; the baseline only shrinks (no stale entry either)."""
    known = set(json.loads(BASELINE.read_text(encoding="utf-8"))["missing"])
    assert not (missing() - known), sorted(missing() - known)
    assert not (known - missing()), f"covered now, remove from the baseline: {sorted(known - missing())}"


def test_unadi_patha_is_loaded():
    d = _j("unadi_patha.json")
    assert d["count"] == len(d["entries"]) == 748 and d["per_pada"] == {"1": 157, "2": 123, "3": 160, "4": 238, "5": 70}
    assert all(e["sutra_slp1"] and e["pratyaya_slp1"] and e["examples_sk"] for e in d["entries"])
    assert _by()["uRAdi-sUtra"]["entries"] == 748


def test_ganapatha_overlay_applied():
    g = _j("ganapatha_full.json")["ganas"]
    assert len(g["sarvAdiH"]["members"]) == 35 and g["sarvAdiH"]["members"][14:23] == ["pUrva", "para", "avara", "dakziRa", "uttara", "apara", "aDara", "sva", "antara"]
    assert g["pUrvAdiH"]["members"] == g["sarvAdiH"]["members"][14:23] and len(g["qatarAdiH"]["members"]) == 5
    assert g["pAraskarAdiH"]["members"] == ["pAraskara", "kAraskara", "raTaspA", "kizku", "kizkinDA"] and g["pAraskarAdiH"]["akrti"]
    assert g["SramaRAdiH"]["sutra"] == "2.1.70" and g["haritAdiH"]["members"][0] == "harita" and g["kaRvAdiH"]["members"][0] == "kaRva"
    assert g["vargyAdiH"]["derived"]["pratyaya"] == "yat" and sum(1 for v in g.values() if v["akrti"]) >= 27


def test_dhatu_antarganas_match_the_pathas_marks():
    rep =json.loads((Path(__file__).resolve().parents[2] / "sig" / "patha_intake.json").read_text(encoding="utf-8"))
    assert [d["id"] for d in rep["dhatu"]["differences_engine_vs_source"]] == rep["dhatu"]["source_stray_marks_not_taken"] == ["06.0174"]      # beyond the Kāśikā bound of kuṭādi
    assert rep["dhatu"]["bounds"]["जक्षित्यादिः"]["n"] == 7 and rep["dhatu"]["bounds"]["रधादिः"]["n"] == 8


def test_gana_authority_record():
    from engine import gana
    a = gana.authority("vyuzwAdiH", "nitya")
    assert a and a["sutra"] == "5.1.97" and a["pATha"] == "gaRapAWa"
    assert gana.authority("vyuzwAdiH", "no_such_stem") is None
