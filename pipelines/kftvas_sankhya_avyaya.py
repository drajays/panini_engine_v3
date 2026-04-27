"""
pipelines/kftvas_sankhya_avyaya.py — *saṅkhyā* + *kṛtvasuṭ* → *…kṛtvaḥ* (*avyaya* *luk* *tail*).

**Corpus** (user ``बहुकृत्वः.md`` / ``तावत्कृत्वः.md``):

  * **bahukftvaH** — ``bahu`` + *kṛtvasuṭ* (**5.4.17**) after **1.1.23**.
  * **tAvatkftvaH** — ``tAvat`` (pre-built *vatuṭ* *anta*; **5.2.39**–**6.3.91** *corpus* *slice* elsewhere) + **5.4.17**.
  * **katikftvaH** — ``kim`` + ``qati`` → **6.4.143** (*kim*/*ḍati* branch) → ``kati`` + **5.4.17**.

Shared tail: **1.2.46** (two *Term*s) → ``P00_taddhita_it_lopa_chain`` → structural merge →
``P00_attach_sup_from_pratipadika`` (``vibhakti_vacana`` ``1-1``) → ``sup_attach_it_chain`` →
**2.4.71** *luk* → **1.4.14** → ``_pada_merge`` → ``P14_tripadi_purvakhya_visarga``.

CONSTITUTION Art. 7 / 11: *apply_rule* + documented structural *pada* merge only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term

from core.canonical_pipelines import (
    P00_attach_sup_from_pratipadika,
    P00_taddhita_it_lopa_chain,
    P14_tripadi_purvakhya_visarga,
    sup_attach_it_chain,
)
from phonology import parse_slp1_upadesha_sequence
from pipelines.subanta import _pada_merge


def _merge_anga_taddhita(s: State, *, label: str) -> State:
    all_v = [v.clone() for t in s.terms for v in t.varnas]
    stem = "".join(v.slp1 for v in all_v)
    merged = Term(
        kind="prakriti",
        varnas=all_v,
        tags={"prātipadika", "anga", "pulliṅga"},
        meta={"upadesha_slp1": stem},
    )
    b = s.flat_slp1()
    s.terms = [merged]
    s.trace.append(
        {
            "sutra_id": f"__KFTVAS_MERGE__{label}__",
            "sutra_type": "STRUCTURAL",
            "type_label": "कृत्वस्-मेलनम्",
            "form_before": b,
            "form_after": s.flat_slp1(),
            "why_dev": "अङ्ग+कृत्वसुट्-संयोजनम् (संरचनात्मकं)।",
            "status": "APPLIED",
        }
    )
    return s


def _kftvas_tail_from_single_sankhya_pratipadika(s: State, *, merge_label: str) -> State:
    """``s`` has one *prātipadika* *saṅkhyā* stem *Term*; **1.1.23** already applied."""
    s.meta["5_4_17_kftvasuT_arm"] = True
    s = apply_rule("5.4.17", s)
    s = apply_rule("1.2.46", s)
    s = P00_taddhita_it_lopa_chain(s)
    s = _merge_anga_taddhita(s, label=merge_label)
    s.meta["vibhakti_vacana"] = "1-1"
    s = P00_attach_sup_from_pratipadika(s)
    s = sup_attach_it_chain(s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    s = apply_rule("1.4.14", s)
    _pada_merge(s)
    s = P14_tripadi_purvakhya_visarga(s)
    return s


def derive_bahukftvaH() -> State:
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("bahu"),
        tags={"anga"},
        meta={"upadesha_slp1": "bahu"},
    )
    s = State(terms=[t], meta={"linga": "pulliṅga"}, trace=[])
    s = apply_rule("1.2.45", s)
    s = apply_rule("1.1.23", s)
    return _kftvas_tail_from_single_sankhya_pratipadika(s, merge_label="bahu")


def derive_tAvatkftvaH() -> State:
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("tAvat"),
        tags={"anga"},
        meta={"upadesha_slp1": "tAvat"},
    )
    s = State(terms=[t], meta={"linga": "pulliṅga"}, trace=[])
    s = apply_rule("1.2.45", s)
    s = apply_rule("1.1.23", s)
    return _kftvas_tail_from_single_sankhya_pratipadika(s, merge_label="tAvat")


def derive_katikftvaH() -> State:
    kim = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("kim"),
        tags={"anga"},
        meta={"upadesha_slp1": "kim"},
    )
    qati = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("qati"),
        tags={"pratyaya", "taddhita", "upadesha", "dit_pratyaya"},
        meta={"upadesha_slp1": "qati"},
    )
    s = State(terms=[kim, qati], meta={"linga": "pulliṅga"}, trace=[])
    s.meta["6_4_143_kim_qati_arm"] = True
    s = apply_rule("6.4.143", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("1.1.23", s)
    return _kftvas_tail_from_single_sankhya_pratipadika(s, merge_label="kati")


__all__ = ["derive_bahukftvaH", "derive_tAvatkftvaH", "derive_katikftvaH"]
