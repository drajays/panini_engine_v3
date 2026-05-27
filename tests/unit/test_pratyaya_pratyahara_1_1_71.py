"""
Tests for phonology/pratyaya_pratyahara.py — 1.1.71 ādir antyena sahetā
applied to pratyaya ordered lists (SUP, SUT, TAP, TIN, TAN, PARASMAI).
"""
from __future__ import annotations

import pytest

from phonology.pratyaya_pratyahara import (
    SUP, SUT, TAP, TIN, TAN, PARASMAI, TRN, SAN,
    build_pratyaya_pratyahara,
    is_sup_upadesha, is_tin_upadesha,
    is_atmanepada_tin, is_parasmaipada_tin,
)


class TestSUP:
    """सुप् — all 21 sup case-endings (4.1.2)."""

    def test_size(self):
        # 17 distinct upadeshas (some vibhakti share the same upadesha string)
        assert len(SUP) == 17

    def test_first_member(self):
        assert "s~" in SUP   # su (1-1, 8-1)

    def test_last_member(self):
        assert "sup" in SUP  # 7-3, the closing entry

    def test_mid_members(self):
        for upa in ("O", "jas", "am", "Ow", "Sas", "wA", "ByAm", "Bis",
                    "Ne", "Byas", "Nasi", "Nas", "os", "Am", "Ni"):
            assert upa in SUP, f"{upa!r} should be in SUP"

    def test_non_member(self):
        assert "iY" not in SUP   # iñ (taddhita)
        assert "tip" not in SUP  # tiṅ ādeśa


class TestSUT:
    """सुट् — sarvanamasthāna subset (su…auṭ)."""

    def test_members(self):
        assert SUT == {"s~", "O", "jas", "am", "Ow"}

    def test_sut_subset_of_sup(self):
        assert SUT <= SUP

    def test_sut_excludes_later(self):
        assert "ByAm" not in SUT
        assert "Nas" not in SUT


class TestTAP:
    """टाप् — ṭāp/ḍāp/cāp strī-pratyaya group."""

    def test_members(self):
        assert TAP == {"TAp", "qAp", "cAp"}

    def test_membership_function(self):
        from phonology.pratyaya_pratyahara import is_tap_upadesha
        assert is_tap_upadesha("TAp")
        assert is_tap_upadesha("qAp")
        assert is_tap_upadesha("cAp")
        assert not is_tap_upadesha("s~")
        assert not is_tap_upadesha("tip")


class TestTIN:
    """तिङ् — all 18 tiṅ ādeśas (3.4.78)."""

    def test_size(self):
        assert len(TIN) == 18

    def test_parasmaipada_members(self):
        for upa in ("tip", "tas", "jhi", "sip", "Tas", "Ta", "mip", "vas", "mas"):
            assert upa in TIN, f"{upa!r} should be in TIN"

    def test_atmanepada_members(self):
        for upa in ("ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG"):
            assert upa in TIN, f"{upa!r} should be in TIN"

    def test_non_member(self):
        assert "sup" not in TIN
        assert "s~" not in TIN


class TestTAN:
    """तङ् — ātmanepada subset of tiṅ (ta…mahiṅ)."""

    def test_size(self):
        assert len(TAN) == 9

    def test_members(self):
        for upa in ("ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG"):
            assert upa in TAN, f"{upa!r} should be in TAN"

    def test_excludes_parasmaipada(self):
        for upa in ("tip", "tas", "jhi", "sip", "Tas", "Ta", "mip", "vas", "mas"):
            assert upa not in TAN, f"{upa!r} should NOT be in TAN"

    def test_tan_subset_of_tin(self):
        assert TAN <= TIN


class TestPARASMAI:
    """Parasmaipada subset (derived: TIN − TAN)."""

    def test_size(self):
        assert len(PARASMAI) == 9

    def test_partition(self):
        assert TAN | PARASMAI == TIN
        assert TAN & PARASMAI == set()


class TestMembershipFunctions:
    """Utility predicate functions."""

    def test_is_sup(self):
        assert is_sup_upadesha("s~")
        assert is_sup_upadesha("Am")
        assert not is_sup_upadesha("tip")
        assert not is_sup_upadesha("iY")

    def test_is_tin(self):
        assert is_tin_upadesha("tip")
        assert is_tin_upadesha("mahiG")
        assert not is_tin_upadesha("s~")

    def test_atmanepada_tin(self):
        assert is_atmanepada_tin("ta")
        assert is_atmanepada_tin("mahiG")
        assert not is_atmanepada_tin("tip")
        assert not is_atmanepada_tin("s~")

    def test_parasmaipada_tin(self):
        assert is_parasmaipada_tin("tip")
        assert is_parasmaipada_tin("tas")
        assert not is_parasmaipada_tin("ta")
        assert not is_parasmaipada_tin("s~")


class TestBuildFunction:
    """build_pratyaya_pratyahara with custom sequences."""

    def test_basic(self):
        seq = [("a", ""), ("b", ""), ("c", "x")]
        result = build_pratyaya_pratyahara("a", "x", seq)
        assert result == {"a", "b", "c"}

    def test_subset(self):
        seq = [("a", ""), ("b", "y"), ("c", ""), ("d", "x")]
        result = build_pratyaya_pratyahara("a", "y", seq)
        assert result == {"a", "b"}

    def test_last_occurrence(self):
        seq = [("a", "p"), ("b", "p"), ("c", "p")]
        result = build_pratyaya_pratyahara("a", "p", seq, last_occurrence=True)
        assert result == {"a", "b", "c"}

    def test_error_unknown_first(self):
        with pytest.raises(ValueError, match="first_upadesha"):
            build_pratyaya_pratyahara("z", "x", [("a", "x")])

    def test_error_unknown_last_it(self):
        with pytest.raises(ValueError, match="last_it"):
            build_pratyaya_pratyahara("a", "z", [("a", "x")])
