"""exercise_audit label shapes: sanādi (san / Ṇic) go through the tiṅanta entry; strī-from-base-stem is not scored as a cell."""
from tools.exercise_audit import _spec


def test_san_label_is_a_sanadi_call():
    spec, exp, why = _spec("vada~ (01.1164) +san Lat Kartari Prathama Eka → vivadizate", "vidyut", "sanadi", "vada~", "vivadizate")
    assert why is None and exp == "vivadizate"
    assert spec == ("sanadi", "01.1164", "laT", "kartari", 3, 1, "san_recipe", None)


def test_nic_label_and_yan_label():
    spec, _, _ = _spec("DUpa~ (01.0462) +Ric Lat Kartari Prathama Eka → DUpAyayate", "vidyut", "sanadi", "DUpa~", "DUpAyayate")
    assert spec[6] == "nic_recipe"
    spec, _, why = _spec("x (01.0001) +yaN Lat Kartari Prathama Eka → y", "vidyut", "sanadi", "x", "y")
    assert spec is None and "yaṅ" in why


def test_stri_from_base_stem_is_not_a_cell():
    spec, _, why = _spec("SiKA Stri Prathama Eka → SiKI", "vidyut", "subanta", "SiKA", "SiKI")
    assert spec is None and "strī-pratyaya" in why
    spec, _, _ = _spec("mati Stri Prathama Eka → matiH", "vidyut", "subanta", "mati", "matiH")
    assert spec and spec[0] == "subanta"
