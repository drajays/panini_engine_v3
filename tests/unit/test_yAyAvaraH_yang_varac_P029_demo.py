from __future__ import annotations


def test_derive_yAyAvaraH_yang_varac_P029():
    from pipelines.yAyAvaraH_yang_varac_P029_demo import derive_yAyAvaraH_yang_varac_P029

    s = derive_yAyAvaraH_yang_varac_P029()
    assert s.render() == "yAyAvaraH"
