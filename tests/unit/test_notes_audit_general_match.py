"""
tools/notes_audit.py — general (सर्वादि/त्यादि) subanta fallback.

The curated docs/data/index.json only lists hand-written one-off recipe
pipelines; it was never going to have सर्वे/सर्वस्मै by name. general_subanta_
match() lets the audit recognize these via the generic subanta.derive()
pipeline instead of reporting "no engine recipe".
"""
from __future__ import annotations

from tools.notes_audit import audit, general_subanta_match


def test_sarva_declensions_match_generically() -> None:
    assert general_subanta_match("sarve") is not None
    assert general_subanta_match("sarvasmE") is not None
    assert general_subanta_match("sarvezAm") is not None


def test_unrelated_surface_forms_do_not_spuriously_match() -> None:
    """Regression: trying a note's own surface form as its stem is unsound —
    subanta.derive() doesn't validate its input is a real prātipadika, and a
    bare-visarga prathamā-ekavacana default made every surface form "match"
    itself. None of these are सर्वादि/त्यादि, so none should match."""
    for key in ("agnI", "kumArI", "gOrI", "yaSAMsi", "jizRu", "muYcati"):
        assert general_subanta_match(key) is None, key


def test_audit_reports_sarva_notes_as_matched(tmp_path) -> None:
    (tmp_path / "सर्वे.md").write_text("सर्वे इति सर्वशब्दस्य प्रथमाबहुवचनम्।\n", encoding="utf-8")
    (tmp_path / "सर्वस्मै.md").write_text("सर्वस्मै इति सर्वशब्दस्य चतुर्थ्येकवचनम्।\n", encoding="utf-8")
    report = audit(tmp_path)
    assert "no engine recipe for sarve" not in report
    assert "no engine recipe for sarvasmE" not in report
    assert "subanta.derive('sarva', 1, 3, 'pulliṅga')" in report
    assert "subanta.derive('sarva', 4, 1, 'pulliṅga')" in report
