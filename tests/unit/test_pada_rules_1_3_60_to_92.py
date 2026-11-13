"""Pada chosen by the sūtras from the tape (dhātu + lakāra tags), no caller pada: 1.3.60 / 61 / 74 / 91 / 92.
Kāśikā 1.3.60 SIyate; 1.3.61 mamAra, marizyati, mriyate, amfta; 1.3.74 kArayate; 1.3.91 vyadyutat; 1.3.92 vartsyati."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive


def _all(dh, lak):
    return {b.surface_slp1 for b in explore(lambda: derive(dh, lak, "kartari", 3, 1))}


def _fired(dh, lak, sid):
    return any(t.get("sutra_id") == sid and t.get("status") == "APPLIED" for t in derive(dh, lak, "kartari", 3, 1).trace)


def test_1_3_60_sad_sit():
    assert _all("Sadx~", "laT") == {"SIyate"}          # śit (laṭ): ātmanepada
    assert _all("Sadx~", "lRT") == {"Satsyati"}        # not śit: parasmaipada stays
    assert _fired("Sadx~", "laT", "1.3.60")


def test_1_3_61_mf_niyama():
    assert _all("mfN", "laT") == {"mriyate"}
    assert _all("mfN", "luG") == {"amfta"}
    assert _all("mfN", "liT") == {"mamAra"}
    assert _all("mfN", "lRT") == {"marizyati"}
    assert _fired("mfN", "lRT", "1.3.61")


def test_1_3_91_dyut_lung_vibhasha():
    r = _all("ruca~", "luG")                            # ātmanepadī dyutādi root; dyuta~ itself is already ubhayapadī
    assert any(x.endswith("t") or x.endswith("d") for x in r) and len(r) >= 2, r   # parasmaipada reading from the rule
    assert _all("ruca~", "laT") == {"rocate"}


def test_1_3_92_vrt_sya_vibhasha():
    r = _all("vftu~", "lRT")
    assert "vartizyati" in r and "vartizyate" in r      # pada only; iṭ-niṣedha 7.2.59 is separate
    assert _all("vftu~", "laT") == {"vartate"}


def test_1_3_74_nic_atmanepada_needs_vivaksha():
    s = derive("pA", "laT", "kartari", 3, 1, nic_recipe=True)
    assert s.flat_dev() == "पाययते"
    assert any(t.get("sutra_id") == "1.3.74" and t.get("status") == "APPLIED" for t in s.trace)
