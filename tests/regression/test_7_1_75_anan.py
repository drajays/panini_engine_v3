"""7.1.75 asthidadhisakthyakṣṇām anaṅ udāttaḥ (Kāśikā): asthna, dadhnā, sakthnā, akṣṇā — the final i is an before an ac-initial sup of the third vibhakti on;
the apavāda of 7.1.73 (num: *dadhinā*) and of 7.3.120 (ṭā → nā after a ghi). The dual nominative and the bhyām / su sups keep the i (asthinī, dadhibhyām)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive


def forms(stem, vib, vac, linga="napuṃsaka"):
    """The readings explore() finds, minus the optional doublings of 8.4.46 / 8.4.47 (dadDnA = daDnA with a doubled d)."""
    undoubled = lambda x: not any(c * 2 in x for c in "wyvrhkgcjtdpbmnlsSzYqQ") and not any(a + b in x for a, b in ("dD", "tT", "gG", "kK", "jJ", "bB", "wW", "qQ"))
    return {b.surface_slp1 for b in explore(lambda: derive(stem, vib, vac, linga)) if undoubled(b.surface_slp1)}


@pytest.mark.parametrize("stem,inst,dat,gen_du,gen_pl", [("daDi", "daDnA", "daDne", "daDnoH", "daDnAm"), ("asTi", "asTnA", "asTne", "asTnoH", "asTnAm"),
                                                            ("sakTi", "sakTnA", "sakTne", "sakTnoH", "sakTnAm"), ("akzi", "akzRA", "akzRe", "akzRoH", "akzRAm")])
def test_anan_before_ac_sups_of_the_third_on(stem, inst, dat, gen_du, gen_pl):
    assert forms(stem, 3, 1) == {inst} and forms(stem, 4, 1) == {dat} and forms(stem, 6, 2) == {gen_du} and forms(stem, 6, 3) == {gen_pl}
    s = derive(stem, 3, 1, "napuṃsaka")
    assert any(r.get("sutra_id") == "7.1.75" and r.get("status") == "APPLIED" for r in s.trace if isinstance(r, dict))


def test_locative_keeps_both_readings_and_the_rest_keeps_the_i():
    assert forms("daDi", 7, 1) == {"daDani", "daDni"}                              # 6.4.136 vibhāṣā ṅiśyoḥ
    assert forms("daDi", 1, 2) == {"daDinI"} and forms("daDi", 3, 2) == {"daDiByAm"} and forms("daDi", 7, 3) == {"daDizu"}
    assert forms("vAri", 3, 1) == {"vAriRA"} and forms("vAri", 6, 1) == {"vAriRaH"}      # an ordinary neuter i-stem is unmoved
