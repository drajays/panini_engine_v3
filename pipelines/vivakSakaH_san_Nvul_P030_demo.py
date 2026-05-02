"""
pipelines/vivakSakaH_san_Nvul_P030_demo.py — P030 **विवक्षकः** (*vac* + *san* + *Nvul*, m. sg.).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P030.json``

Spine (glass-box; **6.4.16** follows *cicīṣati*-style ordering — after *dvitva*):

  **1.1.68** → **3.1.7** (*san* → ``is``) → **1.2.8** (*vac* added to rud-ādi *kitvat*)
  → **1.1.5** → **3.1.32** → samprasāraṇa (**6.1.15**/**1.1.45**/**6.1.108**) →
  **6.1.1**/**6.1.4** → **6.4.16** (*ū* on non-*abhyāsa* ``uc``, ``is``→``s``) →
  **7.4.60** (*P030* *abhyāsa* vowel-only from ``u``/``U``+``c``) → **6.1.77**
  (*u*/*U* + ``U`` → ``v``…) → *pada* merge → **6.1.112** (``vUcs`` → ``vivacs``,
  JSON’s confused **8.4.40** block folded here) → Tripāḍī **8.2.1**/**8.2.30**/**8.3.46**
  → ``vivakS`` + *kṛt* **Nvul** (``pipelines.krdanta`` tail) → prathamā``su``.

The optional JSON steps **7.2.35**/**7.2.10** (*iṭ*) are *prayoga*-blocked here and are
not scheduled (same intent as the JSON’s “blocked” rows).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_subanta_prathama_su_tripadi_visarga,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from pipelines.krdanta import _structural_merge_to_pratipadika
from pipelines.subanta import _pada_merge


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("vac")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "vac"},
    )
    return State(terms=[dhatu], meta={}, trace=[], samjna_registry={})


def derive_vivakSakaH_san_Nvul_P030() -> State:
    s = _build_state()

    s = apply_rule("1.1.68", s)

    s.meta["3_1_7_san_arm"] = True
    s = apply_rule("3.1.7", s)
    s = apply_rule("1.2.8", s)
    s = apply_rule("1.1.5", s)
    s = apply_rule("3.1.32", s)

    s = apply_rule("6.1.15", s)
    s = apply_rule("1.1.45", s)
    s = apply_rule("6.1.108", s)

    s.meta["6_1_1_dvitva_arm"] = True
    s = apply_rule("6.1.1", s)
    s = apply_rule("6.1.4", s)

    s.meta["6_4_16_sani_dirgha_arm"] = True
    s = apply_rule("6.4.16", s)

    s.meta["P030_7_4_60_abhyasa_vowel_only_arm"] = True
    s = apply_rule("7.4.60", s)

    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.77", s)

    _pada_merge(s)
    s.meta["P030_6_1_112_vivakSa_stem_arm"] = True
    s = apply_rule("6.1.112", s)

    if s.terms:
        s.terms[0].kind = "prakriti"
        s.terms[0].tags.update({"dhatu", "anga"})
        s.terms[0].tags.discard("upadesha")
        # Trace-only anchor for humans / downstream audits — must NOT carry
        # ``upadesha`` into the *kṛt* *it* slice (**1.3.3** would eat stem-final hal).
        s.terms[0].meta["upadesha_slp1"] = "vac"

    s.tripadi_zone = False
    s.meta.pop("6_1_77_ik_yan_aci_general_arm", None)

    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.30", s)
    s.meta["8_3_46_ksatva_arm"] = True
    s = apply_rule("8.3.46", s)

    # Exit Tripāḍī locally so *kṛt* **3.1.133** (non–8.x) is not blocked by
    # ``asiddha_violates``; **P00_subanta** re-enters **8.2.1** for ``su``.
    s.tripadi_zone = False

    s.meta["krt_artha"] = "kartari"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s.meta["krt_upadesha_slp1"] = "Nvul"
    s = apply_rule("3.4.67", s)
    s = apply_rule("3.1.133", s)
    for sid in ("1.3.8", "1.3.7", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)
    s = apply_rule("7.1.1", s)
    s = apply_rule("1.4.13", s)
    s = apply_rule("1.1.65", s)
    s = apply_rule("6.4.1", s)
    # JSON **P030** step 16: *acaḥ ñṇiti* does not further strengthen this stem
    # (cf. *sthānivat* / teaching note); **7.2.116** would wrongly vṛddhi the
    # medial *a* of *vivak-* → *vivāk-*.
    s.blocked_sutras.add("7.2.116")
    s = apply_rule("7.2.116", s)
    s.blocked_sutras.discard("7.2.116")
    s = apply_rule("7.2.115", s)
    s = apply_rule("6.1.78", s)
    s = apply_rule("6.1.77", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("1.2.46", s)
    s = _structural_merge_to_pratipadika(s, upadesha_slp1="vivakSaka")

    s.meta["linga"] = "pulliṅga"
    return P00_subanta_prathama_su_tripadi_visarga(s)


__all__ = ["derive_vivakSakaH_san_Nvul_P030"]
