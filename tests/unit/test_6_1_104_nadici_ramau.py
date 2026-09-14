"""
6.1.104 नादिचि — the निषेध that shapes *rāmau*.

Kaumudī on रामौ::

    राम + औ  →  ६.१.१०२ प्रथमयोः पूर्वसवर्णः  प्राप्तः
              →  ६.१.१०४ नादिचि              निषेधः
              →  ६.१.८८  वृद्धिरेचि           रामौ

The point of these tests is the *path*, not only the surface: an engine that
reaches रामौ without staging the निषेध has hard-coded the answer.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY
from engine.sutra_type import SutraType
from pipelines.subanta import derive
from sutras.adhyaya_1.pada_1 import sutra_1_1_11 as s1111


def _status(trace, sutra_id):
    return [s.get("status") for s in trace if s.get("sutra_id") == sutra_id]


def test_nadici_is_a_pratishedha_that_blocks_6_1_102():
    rec = SUTRA_REGISTRY["6.1.104"]
    assert rec.sutra_type is SutraType.PRATISHEDHA
    assert "6.1.102" in rec.blocks_sutra_ids


def test_ramau_blocks_purvasavarna_and_takes_vrddhi():
    state = derive("rAma", 1, 2)
    assert state.flat_dev() == "रामौ"
    assert "APPLIED" in _status(state.trace, "6.1.104")
    assert _status(state.trace, "6.1.102") == ["BLOCKED"]
    assert "APPLIED" in _status(state.trace, "6.1.88")
    assert "6.1.102" in state.blocked_sutras


def test_i_and_u_stems_keep_purvasavarna():
    """हरी / वायू — the pūrva is not आत्, so नादिचि must stay silent."""
    for stem, expected in (("hari", "हरी"), ("vAyu", "वायू")):
        state = derive(stem, 1, 2)
        assert state.flat_dev() == expected
        assert "APPLIED" not in _status(state.trace, "6.1.104")
        assert "APPLIED" in _status(state.trace, "6.1.102")


def test_ramau_is_not_pragrhya_but_hari_dual_is():
    """1.1.11 names ईत् ऊत् एत् only — औ-ending duals are outside it."""
    assert not s1111.is_pragrahya_slp1_vowel("O")
    assert "APPLIED" not in _status(derive("rAma", 1, 2).trace, "1.1.11")
    assert "APPLIED" in _status(derive("hari", 1, 2).trace, "1.1.11")


def test_other_rama_cells_unchanged():
    assert derive("rAma", 1, 1).flat_dev() == "रामः"
    assert derive("rAma", 1, 3).flat_dev() == "रामाः"
    assert derive("rAma", 2, 3).flat_dev() == "रामान्"


def test_nadi_dual_is_not_pragrhya_before_its_sup_arrives():
    """नद्यौ — the stem *nadī* is pragṛhya only as a finished dual pada.

    While the औ is still unattached, tagging the stem blocked 6.1.77 इको यणचि
    and the dual came out *nadīau*.
    """
    state = derive("nadI", 1, 2, linga="strīliṅga")
    assert state.flat_dev() == "नद्यौ"
    assert "APPLIED" in _status(state.trace, "6.1.77")
    # हरी keeps its pragṛhya: there 6.1.102 spends the sup into the aṅga first.
    assert derive("hari", 1, 2).flat_dev() == "हरी"
