"""The ṣaṭ numerals (Kāśikā 1.1.24: ṣaṣ pañcan saptan aṣṭan navan daśan): 1.1.23 / 1.1.24 name them from data/inputs/samkhya_patha.json,
7.1.22 luks the jas / śas after them (pañca), 7.2.84 + 7.1.21 give aṣṭā + auś (aṣṭau); 6.4.8 does not lengthen before a luk'd jas (1.1.63)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive


def forms(stem, vib, vac=3):
    return {b.surface_slp1 for b in explore(lambda: derive(stem, vib, vac, "pulliṅga")) if not any(c * 2 in b.surface_slp1 for c in "wyvrhkgcjtdpbmnlsSzYqQ")}


@pytest.mark.parametrize("stem,gold", [("paYcan", "paYca"), ("saptan", "sapta"), ("navan", "nava"), ("daSan", "daSa")])
def test_jas_sas_luk_after_zat(stem, gold):
    assert forms(stem, 1) == {gold} and forms(stem, 2) == {gold}                    # pañca, not *pañcānaḥ
    s = derive(stem, 1, 3, "pulliṅga")
    assert any(r.get("sutra_id") == "7.1.22" and r.get("status") == "APPLIED" for r in s.trace if isinstance(r, dict))
    assert not any(r.get("sutra_id") == "6.4.8" and r.get("status") == "APPLIED" for r in s.trace if isinstance(r, dict))      # na lumatāṅgasya


def test_ashtan_two_readings():
    assert forms("azwan", 1) == forms("azwan", 2) == {"azwa", "azwO"}              # aṣṭa (luk) · aṣṭau (aṣṭā + auś)
    assert forms("azwan", 3) == {"azwaBiH", "azwABiH"}                              # 7.2.84 is a vikalpa
    assert forms("azwan", 6) == {"azwAnAm"}
    assert forms("azwan", 7) == {"azwasu", "azwAsu"}


def test_the_rest_of_the_paradigm_is_unmoved():
    assert forms("paYcan", 3) == {"paYcaBiH"} and forms("paYcan", 6) == {"paYcAnAm"} and forms("paYcan", 7) == {"paYcasu"}
    assert forms("rAjan", 1) == {"rAjAnaH"}                                         # an ordinary n-stem keeps its dīrgha
