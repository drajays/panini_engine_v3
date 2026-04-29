"""
pipelines/rAjan_su_rAjA_demo.py — 'राजा' (rAjA) prakriyā demo.

Matches the note `1_1_43.md`:
  rAjan + su
    1.2.46   (kṛt/taddhita/samāsa → prātipadika) — demo uses a kṛt-tagged stem
    4.1.2    sup: su
    1.3.2/9  it-lopa: su → s
    1.1.43   suḍ-anapuṃsakasya: mark sarvanāmasthāna (recipe-armed)
    6.4.8    upadhā dīrgha before sarvanāmasthāna (asambuddhau): rAjan → rAjAn
    1.2.41   apṛkta (for single s)
    6.1.68   sutis... apṛkta hal-lopa (recipe-armed): drop final s
    __MERGE__ structural pada merge (so Tripāḍī sees a single pada)
    8.2.1    Tripāḍī gate
    8.2.7    nalopa (recipe-armed): rAjAn → rAjA
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.subanta import _pada_merge


def derive_rAjA() -> State:
    # Demo stem: treat rAjan as vyutpanna (kṛt-tagged) so 1.2.46 can assign prātipadika.
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("rAjan")),
        tags={"anga", "krt"},
        meta={"upadesha_slp1": "rAjan"},
    )
    stem.tags.add("pulliṅga")
    s = State(terms=[stem], meta={"linga": "pulliṅga"}, trace=[])

    s = apply_rule("1.2.46", s)
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)   # su

    s = apply_rule("1.3.2", s)   # u-it
    s = apply_rule("1.3.9", s)   # u-lopa => s

    s.meta["1_1_43_arm"] = True
    s = apply_rule("1.1.43", s)
    s.meta.pop("1_1_43_arm", None)

    s = apply_rule("6.4.8", s)   # rAjan -> rAjAn (needs sarvanamasthana)

    s = apply_rule("1.2.41", s)  # apṛkta on single s
    s.meta["6_1_68_arm"] = True
    s = apply_rule("6.1.68", s)  # drop s
    s.meta.pop("6_1_68_arm", None)

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s.meta["8_2_7_arm"] = True
    s = apply_rule("8.2.7", s)
    s.meta.pop("8_2_7_arm", None)
    return s


__all__ = ["derive_rAjA"]

