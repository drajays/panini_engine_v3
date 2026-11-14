"""Vārttikas on 6.1.64 / 6.1.65 (Kāśikā): a dhātu made from a subanta keeps its ṣ / ṇ — षोडीयति, षण्डीयति; णकारीयति ("सुब्धातोरयमपि नेष्यते").
A real dhātu with the same first letter still takes the sūtra (ṣah → sah, ṇam → nam)."""
import sutras  # noqa: F401
from engine import SUTRA_REGISTRY
from engine.state import State, Term
from phonology import mk

import pytest


def _state(slp1, *tags):
    return State(terms=[Term(kind="prakriti", varnas=[mk(c) for c in slp1], tags={"dhatu", *tags}, meta={})])


@pytest.mark.parametrize("sid,stem", [("6.1.64", "zaRqa"), ("6.1.65", "Rakara")])
def test_cond_holds_for_a_real_dhatu_not_a_subdhatu(sid, stem):
    cond = SUTRA_REGISTRY[sid].cond
    assert cond(_state(stem)) is True
    assert cond(_state(stem, "subdhatu")) is False


def test_nama_dhatu_is_tagged_subdhatu():
    from pipelines import chain
    d = chain.nama_dhatu(chain.Stem("Rakara"))
    assert d.slp1.startswith("R"), d.slp1          # ṇakārīya-: the ṇ is kept
    assert "subdhatu" in d.terms[0].tags


def test_nama_dhatu_keeps_s_with_dot_of_a_subdhatu():
    from pipelines import chain
    d = chain.nama_dhatu(chain.Stem("zaRqa"))
    assert d.slp1.startswith("zaRqIya"), d.slp1        # ṣaṇḍīya- (षण्डीयति), not saṇḍīya-
