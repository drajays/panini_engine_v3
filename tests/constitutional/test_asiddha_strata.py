"""
tests/constitutional/test_asiddha_strata.py
───────────────────────────────────────────

असिद्धत्व as a matrix (ROADMAP B4). The acceptance case is the cycle that
made the flag necessary in the first place: **8.2.66 (s → ru)** and
**8.3.34 (ru → s)** undo each other, and only पूर्वत्रासिद्धम् stops them.
"""
from __future__ import annotations

import pytest

from engine.gates import is_tripadi
from engine.strata import domains, explain, in_tripadi, not_modelled, visible


def test_the_cycle_is_broken_by_asymmetry_not_by_pipeline_order():
    """8.2.66 cannot see 8.3.34; 8.3.34 can see 8.2.66. That asymmetry is 8.2.1."""
    earlier_sees_later = visible("8.2.66", "8.3.34")
    later_sees_earlier = visible("8.3.34", "8.2.66")
    assert not earlier_sees_later, "the ru ⇄ s cycle would re-form"
    assert earlier_sees_later.by == "8.2.1"
    assert later_sees_earlier, "a later tripāḍī rule must see the earlier one"


def test_nothing_before_the_tripadi_sees_into_it():
    assert not visible("6.1.77", "8.2.66")
    assert visible("8.2.66", "6.1.77"), "the tripāḍī sees everything before it"


def test_abhiya_section_is_asiddhavat_to_itself():
    verdict = visible("6.4.24", "6.4.100")
    assert not verdict and verdict.by == "6.4.22"
    # Outside the section the rules see each other normally.
    assert visible("6.4.2", "6.4.100")


def test_ekadesha_is_asiddha_for_satva_and_tuk():
    assert not visible("8.3.59", "6.1.88").visible      # ṣatva
    assert not visible("6.1.72", "6.1.88").visible      # tuk
    assert visible("6.1.87", "6.1.88"), "ordinary rules see the ekādeśa"


def test_every_domain_carries_its_sutra_text_and_range_authority():
    for key, domain in domains().items():
        assert domain["dev"], key
        assert domain["padaccheda_dev"], key
        assert len(domain["range_authority"]) > 30, key


def test_what_is_not_modelled_is_written_down():
    assert len(not_modelled()) >= 2


def test_the_gate_and_the_matrix_agree_on_the_tripadi_bounds():
    for sid in ("8.1.73", "8.2.1", "8.3.34", "8.4.68", "8.4.69"):
        assert is_tripadi(sid) == in_tripadi(sid)


@pytest.mark.parametrize("observer,effect_of", [("8.2.66", "8.3.34"), ("6.4.24", "6.4.100")])
def test_explain_names_the_sutra_that_hides_it(observer, effect_of):
    text = explain(observer, effect_of)
    assert "cannot see" in text and visible(observer, effect_of).by in text
