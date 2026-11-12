"""Exercise-audit cluster A (adhyāya 7): 7.3.35 jani-vadhyoś ca, 7.3.36 puk, 7.3.58 viBAzA ceH, 7.1.69 labh num, 7.3.91 guṇo'pṛkte,
7.3.78 dāṇ only (Kāśikā 7.3.78 'dāṇ'), plus the neuter abhyasta Śatṛ cell of 7.1.79 (dadanti / dadati)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines import chain
from pipelines.tinanta import derive


def _forms(*a, **k):
    return {b.surface_slp1 for b in explore(lambda: derive(*a, **k))}


def test_7_3_35_ajani():                       # Kāśikā 7.3.35: ajani (no upadhā vṛddhi before ciṇ)
    assert "ajani" in _forms("04.0044", "luG", "karmani", 3, 1)
    assert "ajAni" not in _forms("04.0044", "luG", "karmani", 3, 1)


def test_7_3_36_puk_before_nic():              # Kāśikā 7.3.36: ā-final aṅga + puk (jñā → jñāpayati)
    assert "jYApayati" in _forms("10.0258", "laT", "kartari", 3, 1)


def test_7_3_58_ci_vibhasha_kutva():           # Kāśikā 7.3.58: cicāya, cikāya; Vidyut cikye
    from tools.exercise_audit import _derive_loop            # the autonomous loop is the path 7.3.58 is pooled in
    loop = lambda pada: {b.surface_slp1 for b in explore(lambda: _derive_loop(("tinanta", "05.0005", "liT", "kartari", 3, 1, pada)))}
    assert {"cicAya", "cikAya"} <= loop("parasmai")
    assert "cikye" in loop("atmane")


def test_7_1_69_labh_num_vibhasha():           # Kāśikā 7.1.69: alābhi / alambhi
    assert {"alABi", "alamBi"} <= _forms("01.1130", "luG", "karmani", 3, 1)


def test_7_3_91_urnu_guna():                   # Kāśikā 7.3.91: aurṇot (guṇa), beside 7.3.90's aurṇaut
    assert {"OrRot", "OrROt"} <= _forms("02.0034", "laG", "kartari", 3, 1)


def test_7_3_78_only_dan_takes_yaccha():       # dāṇ → yacchati; ḍudāñ keeps dadāti (and dadat → dadanti / dadati by 7.1.79)
    assert "yacCati" in _forms("01.1079", "laT", "kartari", 3, 1)
    st = chain.krt("03.0010", kala="vartamAna", samAnADikaraRa="apraTamA")
    got = {b.surface_slp1 for b in explore(lambda: chain.sup(st, 1, 3, "napuṃsaka"))}
    assert {"dadanti", "dadati"} <= got


def test_7_1_60_nas_num_before_jhal():         # Kāśikā 7.1.60: naṃṣṭā …; Vidyut naś liṭ 2sg nanaMzWa
    assert "nanaMzWa" in _forms("04.0091", "liT", "kartari", 2, 1, pada="parasmai")
