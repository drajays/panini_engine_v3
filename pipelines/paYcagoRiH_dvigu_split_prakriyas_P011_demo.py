"""
pipelines/paYcagoRiH_dvigu_split_prakriyas_P011_demo.py — **P011** (**पञ्चगोणिः**).

Source: ``…/my_scripts/final/split_prakriyas_11/P011.json``.

This is a dvigu-compound slice with a “tena krītam” taddhita sense (stamped by
**5.1.37** + **5.1.28** in this repo as *saṃjñā* notes), then internal sup-luk,
then **1.2.48** hrasva on *goṇī* as per the JSON (encoded by tagging the target
member as ``upasarjana`` + ``TAp_anta`` and arming 1.2.48).

Spine (apply_rule only; structural merge uses canonical helper at the end):
  **2.1.3** → **2.1.51** → **8.2.7** (n-lopa on *paYcan*, narrow armed compound branch) →
  **4.1.76** → **5.1.37** → **5.1.28** → **1.2.46** → **2.4.71** → **1.2.46** →
  **1.2.48** → subanta nom.sg tail (**4.1.2**, **8.2.66**, **8.3.15**) via
  ``P00_subanta_prathama_su_tripadi_visarga``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_subanta_prathama_su_tripadi_visarga
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _prakriti_member(stem: str) -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(stem)),
        tags={"anga", "prātipadika", "samasa_member", "prakriya_P011_paYcagoRiH_demo"},
        meta={"upadesha_slp1": stem},
    )


def _sup(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": up},
    )


def derive_paYcagoRiH_dvigu_split_prakriyas_P011() -> State:
    paYcan = _prakriti_member("paYcan")
    su1 = _sup("s~")
    goRI = _prakriti_member("goRI")
    su2 = _sup("s~")
    s = State(terms=[paYcan, su1, goRI, su2], meta={}, trace=[])

    s.meta["prakriya_P011_taddhitartha_samAhAra_note"] = True
    s.meta["prakriya_P011_2_1_51_arm"] = True
    s = apply_rule("2.1.3", s)
    s = apply_rule("2.1.51", s)

    # paYcan-goRI boundary: drop final n of paYcan (JSON cites 8.2.7).
    s.meta["8_2_7_compound_purvapada_n_lopa_arm"] = True
    s = apply_rule("8.2.7", s)

    # taddhita “tena krītam” stamps and luk-note stamp (no varṇa mutation here).
    s = apply_rule("4.1.76", s)
    s.meta["prakriya_P011_tena_krItam_note"] = True
    s.meta["prakriya_P011_5_1_37_arm"] = True
    s = apply_rule("5.1.37", s)

    s.meta["prakriya_P011_dvigu_Tak_luk_note"] = True
    s.meta["prakriya_P011_5_1_28_arm"] = True
    s = apply_rule("5.1.28", s)

    # internal sup-luk (2.4.71) on the samāsa members.
    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    # 1.2.48 hrasva on goRI (I → i) as per JSON: mark that member as upasarjana + strī-final signal.
    for t in s.terms:
        if t.kind == "prakriti" and (t.meta.get("upadesha_slp1") or "") == "goRI":
            t.tags.add("upasarjana")
            t.tags.add("TAp_anta")
    s.meta["1_2_48_arm"] = True
    s = apply_rule("1.2.48", s)

    # Finish as a subanta nom.sg: merge + su + ru + ḥ.
    s = P00_subanta_prathama_su_tripadi_visarga(s)
    return s


__all__ = ["derive_paYcagoRiH_dvigu_split_prakriyas_P011"]

