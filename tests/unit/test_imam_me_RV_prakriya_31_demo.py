"""Unit tests for ``prakriya_31`` — ``imam`` + ``me`` RV spine."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.imam_me_RV_prakriya_31_demo import (
    derive_imam_me_RV_prakriya_31,
    _mk_imam_acc_demo,
    _mk_me_asmad_demo,
)


def _fired_ids(state: State) -> list[str]:
    out: list[str] = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if not sid or not isinstance(sid, str):
            continue
        st = (e.get("status") or "").upper()
        if st in {"APPLIED", "APPLIED_VACUOUS", "AUDIT"}:
            out.append(sid)
    return out


def test_flat_tape_imam_me() -> None:
    s = derive_imam_me_RV_prakriya_31()
    assert s.flat_slp1() == "imamme"


def test_spine_order() -> None:
    s = derive_imam_me_RV_prakriya_31()
    ids = _fired_ids(s)
    spine = ["6.1.197", "8.1.22", "8.2.1", "8.4.66"]
    for sid in spine:
        assert sid in ids, f"missing {sid}"
    for i in range(len(spine) - 1):
        assert ids.index(spine[i]) < ids.index(spine[i + 1])


def test_registry_and_meta() -> None:
    s = derive_imam_me_RV_prakriya_31()
    assert s.terms[0].meta.get("prakriya_31_imam_first_udAtta_note") is True
    assert s.terms[1].meta.get("prakriya_31_me_anudAtta_from_8122") is True
    assert s.samjna_registry.get("prakriya_31_me_svarita_locus") is True


def test_8_4_66_requires_8122_stamp() -> None:
    s = State(
        terms=[_mk_imam_acc_demo(), _mk_me_asmad_demo()],
        meta={"prakriya_31_8_4_66_arm": True},
        trace=[],
    )
    s.tripadi_zone = True
    s.terms[0].meta["prakriya_31_imam_first_udAtta_note"] = True
    s1 = apply_rule("8.4.66", s)
    assert not s1.samjna_registry.get("prakriya_31_me_svarita_locus")
