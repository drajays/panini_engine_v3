"""1.3.47–50 and 1.3.66: the pada the speaker's sense decides (AMENDMENT 30). Forms: Kāśikā 1.3.47–50, 1.3.66 (ashtadhyayi.db)."""
from __future__ import annotations

import pytest

import sutras  # noqa: F401
from engine.vivaksha_explore import OPEN, derive_all
from pipelines.tinanta import derive

SAMUCCARANA = {"vyaktavAk": "vyaktavAc", "samuccAraRa": "samuccAraRa"}


def _surfaces(*a, **kw):
    return {b.surface_slp1 for b in derive_all("tinanta", *a, **kw)}


@pytest.mark.parametrize("sense,up", [("BAsana", []), ("upasamBAzA", ["upa"]), ("jYAna", []), ("yatna", []), ("vimati", ["vi"]),
                                      ("upamantraRa", ["upa"])])
def test_1_3_47_vad_in_each_sense_is_atmanepada(sense, up):
    s = derive("vada~", "laT", "kartari", 3, 1, upasargas=up or None, vivaksha={"vadArTa": sense})
    assert s.flat_slp1().endswith("vadate") and "1.3.47" in [t["sutra_id"] for t in s.trace if not t.get("skip_reason")]


def test_1_3_47_no_sense_meant_stays_parasmaipada():          # Kāśikā: एतेष्विति किम्? यत्किंचिद्वदति
    s = derive("vada~", "laT", "kartari", 3, 1)
    assert s.flat_slp1() == "vadati" and "1.3.47" not in [t["sutra_id"] for t in s.trace if not t.get("skip_reason")]


def test_1_3_47_vimati_plural_vivadante():                   # क्षेत्रे विवदन्ते
    assert derive("vada~", "laT", "kartari", 3, 3, upasargas=["vi"], vivaksha={"vadArTa": "vimati"}).flat_slp1() == "vivadante"


def test_1_3_48_samuccarana_sampravadante_but_not_for_birds_or_alone():
    s = derive("vada~", "laT", "kartari", 3, 3, upasargas=["sam", "pra"], vivaksha=SAMUCCARANA)
    assert s.flat_slp1().startswith("sampravada") and s.flat_slp1().endswith("te") and "1.3.48" in [t["sutra_id"] for t in s.trace if not t.get("skip_reason")]
    assert derive("vada~", "laT", "kartari", 3, 3, upasargas=["sam", "pra"], vivaksha={"samuccAraRa": "samuccAraRa"}).flat_slp1().endswith("ti")   # kukkuṭāḥ: not vyaktavāk
    assert derive("vada~", "laT", "kartari", 3, 1, vivaksha={"vyaktavAk": "vyaktavAc"}).flat_slp1() == "vadati"                                  # brāhmaṇo vadati


def test_1_3_49_anuvadate_akarmaka_only():
    s = derive("vada~", "laT", "kartari", 3, 1, upasargas=["anu"], vivaksha={"vyaktavAk": "vyaktavAc", "karmakatva": "akarmaka"})
    assert s.flat_slp1() == "anuvadate"
    assert derive("vada~", "laT", "kartari", 3, 1, upasargas=["anu"], vivaksha={"vyaktavAk": "vyaktavAc"}).flat_slp1() == "anuvadati"   # yajur anuvadati
    assert derive("vada~", "laT", "kartari", 3, 1, upasargas=["anu"], vivaksha={"karmakatva": "akarmaka"}).flat_slp1() == "anuvadati"     # anuvadati vIRA


def test_1_3_50_vipralapa_is_vibhasha_both_readings():
    out = {b.surface_slp1: b for b in derive_all("tinanta", "vada~", "laT", "kartari", 3, 3, upasargas=["vi", "pra"],
                                                  vivaksha={**SAMUCCARANA, "vipralApa": "vipralApa"})}
    assert set(out) == {"vipravadante", "vipravadanti"}
    assert ("1.3.50", True) in out["vipravadante"].choices and ("1.3.50", False) in out["vipravadanti"].choices


def test_1_3_48_steps_aside_for_1_3_50_in_vipralapa_only():
    fired = lambda s: [t["sutra_id"] for t in s.trace if not t.get("skip_reason")]
    s = derive("vada~", "laT", "kartari", 3, 3, upasargas=["vi", "pra"], vivaksha={**SAMUCCARANA, "vipralApa": "vipralApa"})
    assert "1.3.48" not in fired(s) and "1.3.50" in fired(s)


def test_1_3_66_rudhadi_buj_anavana_is_atmanepada():
    got = {b.surface_slp1: b.choices for b in derive_all("tinanta", "Buja~", "laT", "kartari", 3, 1, vivaksha={"BujArTa": OPEN})}
    assert got["Bunakti"] == () and got["BuNkte"] == (("vivaksha", "BujArTa", "anavana"),)
    assert _surfaces("Buja~", "laT", "kartari", 3, 3, vivaksha={"BujArTa": OPEN}) == {"BuYjanti", "BuYjate"}      # bhuñjāte/bhuñjate: dvivacana is not asked here


def test_1_3_66_does_not_touch_other_roots():
    assert derive("BU", "laT", "kartari", 3, 1, vivaksha={"BujArTa": "anavana"}).flat_slp1() == "Bavati"
