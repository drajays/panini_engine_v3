from pipelines.tinanta import derive


def _f(d, lak, p, n):
    return derive(d, lak, "kartari", p, n).flat_dev()


def test_as_laT_paradigm_7_4_50():  # असि: s of the root drops before s-initial sip
    assert [_f("Adadi_02_0060", "laT", p, n) for p in (1, 2, 3) for n in (1, 2, 3)] == \
        ["अस्मि", "स्वः", "स्मः", "असि", "स्थः", "स्थ", "अस्ति", "स्तः", "सन्ति"]


def test_vid_loT_2sg_viddhi_6_4_101():
    assert _f("Adadi_02_0059", "loT", 2, 1) == "विद्धि"
