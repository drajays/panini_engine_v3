"""``prakriya_19`` Part A — *puras* / ``puraH`` (``pipelines/puras_avyaya_prakriya_19_demo``)."""
import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.puras_avyaya_prakriya_19_demo import (
    _mk_Ni_sup,
    _mk_asi_taddhita,
    _mk_pUrva,
    derive_puras_avyaya_prakriya_19,
)


def _fired_ids(state: State) -> list[str]:
    out: list[str] = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if not sid or not isinstance(sid, str):
            continue
        st = (e.get("status") or "").upper()
        if st in {"APPLIED", "AUDIT"}:
            out.append(sid)
    return out


def _trace_row(state: State, sutra_id: str) -> dict | None:
    for e in state.trace:
        if e.get("sutra_id") == sutra_id:
            return e
    return None


def test_puras_prakriya_19_surface() -> None:
    s = derive_puras_avyaya_prakriya_19()
    assert s.flat_slp1() == "puraH"


def test_puras_prakriya_19_spine_order() -> None:
    s = derive_puras_avyaya_prakriya_19()
    ids = _fired_ids(s)
    # ``3.1.1``–``3.1.3`` register the *pratyaya* *ādyudātta* *adhikāra* (often AUDIT).
    must = ["3.1.1", "3.1.2", "3.1.3", "5.3.39", "2.4.71", "1.1.38", "2.4.82", "8.2.66"]
    for m in must:
        assert m in ids, f"missing {m}"
    assert ids.index("5.3.39") < ids.index("2.4.71")
    assert ids.index("2.4.71") < ids.index("1.1.38") < ids.index("2.4.82")
    struct = _trace_row(s, "__PRAKRIYA_19_ASI_TO_AS__")
    assert struct is not None
    assert (struct.get("status") or "").upper() == "APPLIED"


def test_sutra_5_3_39_pUrva_to_pur() -> None:
    s = State(terms=[_mk_pUrva(), _mk_Ni_sup(), _mk_asi_taddhita()])
    s.meta["prakriya_19_puras"] = True
    s.meta["prakriya_19_puras_5_3_39_arm"] = True
    s = apply_rule("5.3.39", s)
    assert s.terms[0].meta.get("upadesha_slp1") == "pur"
    assert s.flat_slp1().startswith("pur")
