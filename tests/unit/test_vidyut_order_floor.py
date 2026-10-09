from tools.vidyut_order import compare


def test_subsequence_extras_allowed():
    assert compare(["6.1.77", "6.1.101"], ["1.1.1", "6.1.77", "9.9.9", "6.1.101"]) == {"missing": [], "inverted": []}


def test_inversion_and_missing_reported():
    c = compare(["6.1.77", "6.1.101", "7.7.7"], ["6.1.101", "6.1.77"])
    assert c["missing"] == ["7.7.7"] and c["inverted"] == [["6.1.77", "6.1.101"]]
