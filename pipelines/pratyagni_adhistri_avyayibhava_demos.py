"""
pipelines/pratyagni_adhistri_avyayibhava_demos.py

Two avyayībhāva derivations requested by the user:

  1) pratyagni (agni + am + prati → prati+agni → pratyagni)
  2) adhistri (strI + Ni + adhi → adhi+strI → adhistri → adhistri (napuṃsaka hrasva))

These are glass-box demos: they exercise the exact sūtras listed in the user's
step sequence, with minimal semantic arming via ``state.meta`` for samāsa sūtras.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _prakriti(stem: str) -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(stem)),
        tags={"anga", "prātipadika", "samasa_member"},
        meta={"upadesha_slp1": stem},
    )


def _avyaya(word: str) -> Term:
    return Term(
        kind="nipata",
        varnas=list(parse_slp1_upadesha_sequence(word)),
        tags={"avyaya", "samasa_member"},
        meta={"upadesha_slp1": word},
    )


def _sup(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": up},
    )


def _merge_to_single_pratipadika(s: State, *, label: str) -> State:
    all_v = [v.clone() for t in s.terms for v in t.varnas]
    merged = Term(
        kind="prakriti",
        varnas=all_v,
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "".join(v.slp1 for v in all_v)},
    )
    # carry avyayibhava/avyaya/napuṃsaka tags if present
    for tg in ("avyayibhava", "avyaya", "napuṃsaka"):
        if any(tg in t.tags for t in s.terms):
            merged.tags.add(tg)
    b = s.flat_slp1()
    s.terms = [merged]
    s.trace.append({
        "sutra_id": f"__AVYAYIBHAVA_MERGE__{label}__",
        "sutra_type": "STRUCTURAL",
        "type_label": "अव्ययीभाव-मेलनम्",
        "form_before": b,
        "form_after": s.flat_slp1(),
        "why_dev": "समास-पश्चात् एकं प्रातिपदिकम् (संरचनात्मकं)।",
        "status": "APPLIED",
    })
    return s


def derive_pratyagni() -> State:
    agni = _prakriti("agni")
    am = _sup("am")  # internal dvitīyā per the user's statement
    prati = _avyaya("prati")
    s = State(terms=[agni, am, prati], meta={}, trace=[])

    # 2.1.5 avyayībhāva adhikāra + 2.1.13 specific prati-abhimukhya samāsa mark
    s = apply_rule("2.1.5", s)
    s.meta["2_1_13_prati_abhimukhya_arm"] = True
    s = apply_rule("2.1.13", s)

    # 1.2.46 prātipadika-saṃjñā + 2.4.71 internal sup-luk (ghost)
    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    # 1.2.43 upasarjana on the avyaya; 2.2.30 move it to front
    s = apply_rule("1.2.43", s)
    s = apply_rule("2.2.30", s)

    # 6.1.77 yāṇ: arm generic cross-term
    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.77", s)

    # Merge to one term for final output and attach su via 4.1.2, then avyaya via 1.1.41.
    s = _merge_to_single_pratipadika(s, label="pratyagni")
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta["linga"] = "napuṃsaka"
    s = apply_rule("4.1.2", s)
    s = apply_rule("1.1.41", s)
    s = apply_rule("2.4.82", s)
    return s


def derive_adhistri() -> State:
    # strI + Ni (7th plural) + adhi
    strI = _prakriti("strI")
    ni = _sup("Ni")
    adhi = _avyaya("adhi")
    s = State(terms=[strI, ni, adhi], meta={}, trace=[])

    s = apply_rule("2.1.5", s)
    s.meta["2_1_6_avyayibhava_arm"] = True
    s = apply_rule("2.1.6", s)

    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    s = apply_rule("1.2.43", s)
    s = apply_rule("2.2.30", s)

    # avyayibhava napuṃsaka + 1.2.47 hrasva (I→i)
    s = apply_rule("2.4.18", s)
    s = apply_rule("1.2.47", s)

    s = _merge_to_single_pratipadika(s, label="adhistri")
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta["linga"] = "napuṃsaka"
    s = apply_rule("4.1.2", s)
    s = apply_rule("1.1.41", s)
    s = apply_rule("2.4.82", s)
    return s


__all__ = ["derive_pratyagni", "derive_adhistri"]

