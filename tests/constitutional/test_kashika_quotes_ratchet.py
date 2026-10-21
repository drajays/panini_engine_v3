"""A "Kāśikā:" quote in a sūtra docstring must be the Kāśikā's own words, verbatim in the brain (final reference,
docs/BRAIN_FINAL_REFERENCE_PLAN.md B1). Older docstrings carry paraphrases; their number may only fall.
Replace a paraphrase with the brain's text (`make brain S=<id> --full`) and lower CEILING in the same commit."""
from __future__ import annotations

import pytest

from tools.kashika_quote_check import BRAIN_DB, unverified

CEILING = 106

pytestmark = pytest.mark.skipif(not BRAIN_DB.exists(), reason="brain not present")


def test_unverified_kashika_quotes_never_rise():
    bad = unverified()
    assert len(bad) <= CEILING, f"{len(bad)} > {CEILING}: new non-verbatim 'Kāśikā' text in " + ", ".join(sorted(bad)[:10])
