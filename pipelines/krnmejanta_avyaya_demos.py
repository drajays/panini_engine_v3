"""
pipelines/krnmejanta_avyaya_demos.py — demos for **1.1.39 कृन्मेजन्तः**.

We implement two representative derivations from the user's note:

  A) स्वादुकारं भुङ्क्ते
     - upapada: ``svAdu`` tagged ``upapada``
     - kṛdanta: ``kAr`` + ``am`` (kṛt pratyaya surface ends in m)
     - **1.1.39** ⇒ avyaya
     - **2.2.20** merges upapada+am-anta avyaya
     - attach ``su`` then **2.4.82** ghosts it

  B) वक्षे रायः
     - ``vak`` + ``se`` (kṛt pratyaya surface ends in e ∈ ec)
     - **1.1.39** ⇒ avyaya
     - attach ``su`` then **2.4.82** ghosts it

These demos focus on the **kṛn/mejanta → avyaya → sup-luk** chain, not on fully
modelling all Vedic/taddhita affix-vidhāna sūtras from 3.4.9/3.4.26 etc.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _anga(slp1: str, *, upapada: bool = False) -> Term:
    tags = {"anga", "prātipadika"}
    if upapada:
        tags.add("upapada")
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(slp1)),
        tags=tags,
        meta={"upadesha_slp1": slp1},
    )


def _krt_pratyaya_surface(slp1: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(slp1)),
        tags={"pratyaya", "krt", "upadesha"},
        meta={"upadesha_slp1": slp1},
    )


def _sup(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": up},
    )


def derive_svAdu_kAraM() -> State:
    # svAdu (upapada) + kAr + am(kṛt)
    up = _anga("svAdu", upapada=True)
    kar = _anga("kAr")
    am = _krt_pratyaya_surface("am")
    s = State(terms=[up, kar, am], meta={}, trace=[])
    s = apply_rule("1.1.39", s)
    # Merge upapada + am-anta avyaya (2.2.20) — requires adjacency, so merge kar+am first.
    # Structural concat kar+am into one pratyaya-like kṛt block for the narrow demo.
    merged = Term(
        kind="pratyaya",
        varnas=[v.clone() for v in kar.varnas] + [v.clone() for v in am.varnas],
        tags={"pratyaya", "krt", "upadesha", "avyaya"},
        meta={"upadesha_slp1": "kAram"},
    )
    s.terms = [up, merged]
    s = apply_rule("2.2.20", s)
    # Attach su then avyaya→sup-luk.
    s.terms.append(_sup("s~"))
    s = apply_rule("2.4.82", s)
    return s


def derive_vakSe() -> State:
    vak = _anga("vak")
    se = _krt_pratyaya_surface("se")
    s = State(terms=[vak, se], meta={}, trace=[])
    s = apply_rule("1.1.39", s)
    s.terms.append(_sup("s~"))
    s = apply_rule("2.4.82", s)
    return s


__all__ = ["derive_svAdu_kAraM", "derive_vakSe"]

