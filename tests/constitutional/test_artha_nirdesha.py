"""
Constitution Art. 20 — अर्थनिर्देश.

An ``ArthaNirdesha`` may sit only on an ADHIKARA record, must reach back to an
earlier sūtra, and its ``source`` sentence (the vṛtti that attests पूर्वैः) must be
quoted verbatim in the sūtra file's docstring.
"""
from __future__ import annotations

import importlib

import pytest

import sutras  # noqa: F401
from engine import ArthaNirdesha, SUTRA_REGISTRY, SutraRecord, SutraType


def _records():
    return [r for r in SUTRA_REGISTRY.values() if r.artha_nirdesha is not None]


def test_known_artha_nirdesha_heads():
    assert {r.sutra_id for r in _records()} >= {"4.1.92"}


@pytest.mark.parametrize("rec", _records(), ids=lambda r: r.sutra_id)
def test_artha_nirdesha_is_cited_in_docstring(rec):
    assert rec.sutra_type is SutraType.ADHIKARA
    a, p, n = rec.sutra_id.split(".")
    mod = importlib.import_module(f"sutras.adhyaya_{a}.pada_{p}.sutra_{a}_{p}_{n}")
    assert rec.artha_nirdesha.source in (mod.__doc__ or ""), "vṛtti source must be quoted (Art. 14/20)"


def test_record_validation():
    an = ArthaNirdesha(artha="x", artha_dev="x", purva_from="4.1.83", source="q")
    with pytest.raises(ValueError):
        SutraRecord(sutra_id="9.9.9", sutra_type=SutraType.VIDHI, text_slp1="x", text_dev="x", padaccheda_dev="x", why_dev="x",
                    cond=lambda s: False, act=lambda s: s, artha_nirdesha=an)
    with pytest.raises(ValueError):
        SutraRecord(sutra_id="4.1.80", sutra_type=SutraType.ADHIKARA, text_slp1="x", text_dev="x", padaccheda_dev="x", why_dev="x",
                    cond=lambda s: False, act=lambda s: s, adhikara_scope=("4.1.80", "4.1.90"),
                    artha_nirdesha=an)
