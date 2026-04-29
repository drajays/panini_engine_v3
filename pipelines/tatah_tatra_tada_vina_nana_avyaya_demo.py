"""
pipelines/tatah_tatra_tada_vina_nana_avyaya_demo.py — 1.1.38 + 2.4.82 demos.

Implements the note `1.1.38.md` derivations as auditable apply_rule sequences:

  - tataH / yataH   (tad/yad + tas(il) → tatas → su-luk → tataH)
  - tatra / yatra   (tad/yad + tra(l) → tatra; su-luk)
  - tadA / yadA     (tad/yad + dA → tadA; su-luk)
  - vinA            (vi + nA → vinA; su-luk)
  - nAnA            (nA + nA (demo) → nAnA; su-luk)

This module focuses on **1.1.38** (avyaya tagging) and **2.4.82** (sup-luk),
not on fully modelling the taddhita-vidhāna sūtras (5.3.7/10/15, 5.2.27, …).
Those affixes are represented as explicit *taddhita* Terms with
``meta['asarva_vibhakti_taddhita']=True`` so 1.1.38 can remain configuration-driven.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA


def _anga(slp1: str, *, tyadadi: bool = False) -> Term:
    tags = {"anga", "prātipadika"}
    if tyadadi:
        tags.add("tyadadi")
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(slp1)),
        tags=tags,
        meta={"upadesha_slp1": slp1},
    )


def _sup(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": up},
    )


def _taddhita(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": up, META_ASARVA_VIBHAKTI_TADDHITA: True},
    )


def _finish_with_su_luk_and_optional_visarga(s: State) -> State:
    # Attach su (nom.sg) only to trigger 1.1.38→2.4.82 in this demo.
    s.terms.append(_sup("s~"))
    s = apply_rule("1.1.38", s)
    s = apply_rule("2.4.82", s)
    # Merge to a single pada and apply visarga tail where applicable.
    from pipelines.subanta import _pada_merge
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


def derive_tataH() -> State:
    # tad + Nasi + tasil (represented as 'tas')
    tad = _anga("tad", tyadadi=True)
    nasi = _sup("Nasi")
    tas = _taddhita("tas")
    s = State(terms=[tad, nasi, tas], meta={}, trace=[])
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    s = apply_rule("7.2.102", s)
    s = apply_rule("6.1.97", s)
    return _finish_with_su_luk_and_optional_visarga(s)


def derive_yataH() -> State:
    # yad + Nasi + tas
    yad = _anga("yad", tyadadi=True)
    nasi = _sup("Nasi")
    tas = _taddhita("tas")
    s = State(terms=[yad, nasi, tas], meta={}, trace=[])
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    s = apply_rule("7.2.102", s)
    s = apply_rule("6.1.97", s)
    return _finish_with_su_luk_and_optional_visarga(s)


def derive_tatra() -> State:
    tad = _anga("tad", tyadadi=True)
    ni = _sup("Ni")
    tra = _taddhita("tra")
    s = State(terms=[tad, ni, tra], meta={}, trace=[])
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    s = apply_rule("7.2.102", s)
    s = apply_rule("6.1.97", s)
    # For tatra the surface already ends with a; visarga tail is inert.
    s = _finish_with_su_luk_and_optional_visarga(s)
    return s


def derive_yatra() -> State:
    yad = _anga("yad", tyadadi=True)
    ni = _sup("Ni")
    tra = _taddhita("tra")
    s = State(terms=[yad, ni, tra], meta={}, trace=[])
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    s = apply_rule("7.2.102", s)
    s = apply_rule("6.1.97", s)
    return _finish_with_su_luk_and_optional_visarga(s)


def derive_tadA() -> State:
    tad = _anga("tad", tyadadi=True)
    ni = _sup("Ni")
    dA = _taddhita("dA")
    s = State(terms=[tad, ni, dA], meta={}, trace=[])
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    s = apply_rule("7.2.102", s)
    s = apply_rule("6.1.97", s)
    return _finish_with_su_luk_and_optional_visarga(s)


def derive_yadA() -> State:
    yad = _anga("yad", tyadadi=True)
    ni = _sup("Ni")
    dA = _taddhita("dA")
    s = State(terms=[yad, ni, dA], meta={}, trace=[])
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    s = apply_rule("7.2.102", s)
    s = apply_rule("6.1.97", s)
    return _finish_with_su_luk_and_optional_visarga(s)


def derive_vinA() -> State:
    # vi + nA
    vi = _anga("vi")
    nA = _taddhita("nA")
    s = State(terms=[vi, nA], meta={}, trace=[])
    return _finish_with_su_luk_and_optional_visarga(s)


def derive_nAnA() -> State:
    # Demo: nA + nA → nAnA (structural concatenation as stand-in for 5.2.27/7.2.117 slice)
    nA1 = _anga("nA")
    nA2 = _taddhita("nA")
    s = State(terms=[nA1, nA2], meta={}, trace=[])
    return _finish_with_su_luk_and_optional_visarga(s)


__all__ = [
    "derive_tataH",
    "derive_yataH",
    "derive_tatra",
    "derive_yatra",
    "derive_tadA",
    "derive_yadA",
    "derive_vinA",
    "derive_nAnA",
]

