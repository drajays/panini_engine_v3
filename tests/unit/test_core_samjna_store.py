from __future__ import annotations

import sutras  # noqa: F401

from core.samjna_store import State, Term, Varna, samjna_labels
from phonology import mk
from phonology.varna import mk_inherent_a


def test_samjna_labels_empty() -> None:
    s = State()
    assert samjna_labels(s) == frozenset()


def test_samjna_labels_after_registry() -> None:
    s = State()
    s.samjna_registry["ghi"] = frozenset({"B"})
    assert "ghi" in samjna_labels(s)


def test_core_reexport_term() -> None:
    v = [mk("r"), mk_inherent_a()]
    t = Term(kind="prakriti", varnas=v, tags={"prātipadika"}, meta={})
    s = State(terms=[t])
    assert s.terms[0].kind == "prakriti"
    assert isinstance(s.terms[0].varnas[0], Varna)
