"""
pipelines/yar_anaci_dvitva_tripadi.py — **8.4.47** *anaci ca* + **8.4.46** *aco rahābhyām dve*.

Pedagogical lesson: after *ac*, a *yar* consonant (*hal* − *h*) not immediately
followed by *ac* may optionally geminate; *r* / *h* after *ac* geminate the
**following** *yar* (**8.4.46**), not the *r* / *h*.

Kāśikā vārttikas on **8.4.47** (यणो मयो द्वे, शरः खयो द्वे) fire on adjacent
यण्‖मय् / शर्‖खय् even without *ac* on the left.  For मयो यणो (दध्य्यत्र) use
``D`` = ध (not ``dh``); sandhi ``dadhyatra`` keeps ``h``+``y`` and blocks that path.

SLP1: ``f`` = ऋ, ``z`` = ष, ``n`` = ण, ``R`` = ण (alternate), ``H`` = visarga.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_tripadi_yar_anaci_dvitva_spine
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _one_term(slp1: str) -> State:
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(slp1),
        tags=set(),
        meta={"upadesha_slp1": slp1},
    )
    return State(terms=[t], meta={}, trace=[])


def _two_terms(left: str, right: str) -> State:
    return State(
        terms=[
            Term(
                kind="prakriti",
                varnas=parse_slp1_upadesha_sequence(left),
                tags=set(),
                meta={"upadesha_slp1": left},
            ),
            Term(
                kind="prakriti",
                varnas=parse_slp1_upadesha_sequence(right),
                tags={"nipāta"},
                meta={"upadesha_slp1": right},
            ),
        ],
        meta={},
        trace=[],
    )


def _with_dvitva(s: State, *, exhaustive: bool = False) -> State:
    return P00_tripadi_yar_anaci_dvitva_spine(s, exhaustive=exhaustive)


def derive_kfznaH_prakrti() -> State:
    """कृष्णः — no gemination (baseline)."""
    return _one_term("kfznaH")


def derive_kfznaH_dvitva() -> State:
    """कृष्णः → कृष्ष्णः (*ṣ* gemination after *ṛ*)."""
    return _with_dvitva(_one_term("kfznaH"))


def derive_matyatra_prakrti() -> State:
    return _one_term("matyatra")


def derive_matyatra_dvitva() -> State:
    """मत्यत्र → मत्त्यत्र."""
    return _with_dvitva(_one_term("matyatra"))


def derive_rAmAt_prakrti() -> State:
    return _one_term("rAmAt")


def derive_rAmAt_dvitva() -> State:
    """रामात् → रामात्त्."""
    return _with_dvitva(_one_term("rAmAt"))


def derive_sUry_prakrti() -> State:
    return _one_term("sUry")


def derive_sUry_y_dvitva() -> State:
    """सूर्य → सूर्य्य (**8.4.46**: *ū* + *r* + *y*)."""
    return _with_dvitva(_one_term("sUry"))


def derive_kfzna_sya_prakrti() -> State:
    """कृष्ण + स्य (genitive base)."""
    return _two_terms("kfzna", "sya")


def derive_kfzna_sya_dvitva_both() -> State:
    """कृष्णस्य — both optional sites (ष and स)."""
    return _with_dvitva(_two_terms("kfzna", "sya"), exhaustive=True)


def derive_kfzna_sya_dvitva_z_only() -> State:
    """कृष्ष्णस्य — ष only (``sya`` unchanged)."""
    s = _with_dvitva(_one_term("kfzna"))
    s.terms.append(
        Term(
            kind="prakriti",
            varnas=parse_slp1_upadesha_sequence("sya"),
            tags={"nipāta"},
            meta={"upadesha_slp1": "sya"},
        )
    )
    return s


def derive_kfzna_sya_dvitva_s_only() -> State:
    """कृष्णस्स्य — स at pada boundary only (ष site blocked)."""
    s = _two_terms("kfzna", "sya")
    for v in s.terms[0].varnas:
        if v.slp1 == "z":
            v.tags.add("yar_dvitva_8_4_47")
    return _with_dvitva(s)


def derive_vAlmIki_prakrti() -> State:
    return _one_term("vAlmIki")


def derive_vAlmIki_dvitva() -> State:
    """वाल्मीकि → वाल्म्मीकि (यणो मयो — ल् + म्)."""
    return _with_dvitva(_one_term("vAlmIki"))


def derive_dadDyatra_prakrti() -> State:
    """दध्यत्र with ध = ``D`` (मयो यणो — ध + य)."""
    return _one_term("dadDyatra")


def derive_dadDyatra_dvitva() -> State:
    """दध्यत्र → दध्य्यत्र."""
    return _with_dvitva(_one_term("dadDyatra"))


def derive_sthAtA_prakrti() -> State:
    """स्थ-आता — ``sTAtA`` (``T`` = थ); ``st…`` parses wrongly as ``s``+``t``+``T``."""
    return _one_term("sTAtA")


def derive_sthAtA_dvitva() -> State:
    """स्थाता → स्थ्थाता (शरः खयो — ``s`` + ``T`` → ``sTTAtA``)."""
    return _with_dvitva(_one_term("sTAtA"))


def derive_apsarA_prakrti() -> State:
    return _one_term("apsarA")


def derive_apsarA_dvitva() -> State:
    """अप्सरा → अप्स्सरा (खयो शरः — प् + स्)."""
    return _with_dvitva(_one_term("apsarA"))


__all__ = [
    "derive_kfznaH_prakrti",
    "derive_kfznaH_dvitva",
    "derive_matyatra_prakrti",
    "derive_matyatra_dvitva",
    "derive_rAmAt_prakrti",
    "derive_rAmAt_dvitva",
    "derive_sUry_prakrti",
    "derive_sUry_y_dvitva",
    "derive_kfzna_sya_prakrti",
    "derive_kfzna_sya_dvitva_both",
    "derive_kfzna_sya_dvitva_z_only",
    "derive_kfzna_sya_dvitva_s_only",
    "derive_vAlmIki_prakrti",
    "derive_vAlmIki_dvitva",
    "derive_dadDyatra_prakrti",
    "derive_dadDyatra_dvitva",
    "derive_sthAtA_prakrti",
    "derive_sthAtA_dvitva",
    "derive_apsarA_prakrti",
    "derive_apsarA_dvitva",
]
