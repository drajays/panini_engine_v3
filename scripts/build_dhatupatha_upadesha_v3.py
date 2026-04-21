#!/usr/bin/env python3
"""
Build ``data/inputs/dhatupatha_upadesha.json`` from v2 exports:

  * ``panini_engine_v2/data/dhatu_upadesha_post_it_lopa.json`` (940 Bhvādi roots)
  * ``panini_engine_v2/data/dhatupatha_ashtadhyayi_txt.json`` (meanings / it-class / pada)

Plus **curated extensions** for dhātus outside that Bhvādi slice (other gaṇas) used by
pipelines/tests (tṛc examples, णीञ्, etc.).

Reference documentation: ``~/Documents/my panini notes/dhatupath.md`` (full pāṭha text).

Run from repo root::

    python3 scripts/build_dhatupatha_upadesha_v3.py
"""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

from phonology.pratyahara import is_ekac_upadesha
from phonology.tokenizer import devanagari_to_slp1_flat

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "panini_engine_v2" / "data"
OUT = ROOT / "data" / "inputs" / "dhatupatha_upadesha.json"

POST_IT = V2 / "dhatu_upadesha_post_it_lopa.json"
ASH = V2 / "dhatupatha_ashtadhyayi_txt.json"


def _safe_slp1_from_deva(label: str, dev: str) -> str:
    if not dev:
        return ""
    try:
        return devanagari_to_slp1_flat(dev)
    except Exception as e:
        raise ValueError(f"{label}: {dev!r} → {e}") from e


def _it_class_to_flags(it_lab: str | None) -> dict:
    """Map Kaumudī-style ``it_class_label_dev`` to engine ``flags``."""
    if not it_lab:
        return {"anit": False, "set": False, "vet": False}
    t = it_lab.strip()
    anit = "अनिट" in t
    set_ = "सेट" in t and "अनि" not in t[:3]  # avoid अनिट substring false positive
    vet = "वेट" in t
    if anit:
        set_ = vet = False
    return {"anit": bool(anit), "set": bool(set_), "vet": bool(vet)}


def _merge_bvadi_rows() -> list[dict]:
    post = json.loads(POST_IT.read_text(encoding="utf-8"))
    ash_d = json.loads(ASH.read_text(encoding="utf-8"))
    meta_by_id = {d["dhatupatha_id"]: d for d in ash_d["dhatus"]}

    out: list[dict] = []
    for e in post["entries"]:
        did = e["dhatupatha_id"]
        am = (meta_by_id.get(did) or {}).get("ashtadhyayi_com") or {}
        up_dev = e["upadesha_dev"]
        up_slp = _safe_slp1_from_deva(did, up_dev)
        after_dev = e.get("dhatu_after_it_lopa") or ""
        after_slp = _safe_slp1_from_deva(f"{did}_after", after_dev) if after_dev else ""

        it_lab = am.get("it_class_label_dev")
        flags = _it_class_to_flags(it_lab)
        flags["ekac"] = bool(after_slp and is_ekac_upadesha(after_slp))
        flags["udatta"] = False

        gana_name = "BvAdi"
        entry_id = f"{gana_name}_{did.replace('.', '_')}"

        row = {
            "id": entry_id,
            "tier": "bvadi_merged",
            "dhatupatha_id": did,
            "gana": e.get("gana"),
            "gana_number": e.get("gana"),
            "serial_in_gana": e.get("serial_in_gana"),
            "sutra_ref": f"1.{e.get('serial_in_gana')}",
            "upadesha_dev": up_dev,
            "upadesha_slp1": up_slp,
            "mula_dhatu_dev": am.get("mula_dhatu_dev") or e.get("mula_dhatu_dev"),
            "raw_dhatu_after_it_lopa_dev": after_dev,
            "raw_dhatu_after_it_lopa_slp1": after_slp,
            "artha_dev": am.get("artha_dev"),
            "artha_slp1": _safe_slp1_from_deva(did + "_artha", am["artha_dev"])
            if am.get("artha_dev")
            else None,
            "artha_en": am.get("artha_en"),
            "artha_hi": am.get("artha_hi"),
            "gana_label_dev": am.get("gana_label_dev"),
            "pada_label_dev": am.get("pada_label_dev"),
            "karmatva_label_dev": am.get("karmatva_label_dev"),
            "it_class_label_dev": it_lab,
            "it_markers": e.get("it_markers") or [],
            "flags": flags,
            "notes": None,
        }
        out.append(row)
    return out


# Dhātus used by tests / tṛc demos but **not** present in the 940 Bhvādi post-it export.
_CURATED_EXTENSIONS: list[dict] = [
    {
        "id": "BvAdi_ciY",
        "tier": "curated_extension",
        "dhatupatha_id": None,
        "gana": 5,
        "gana_number": 5,
        "serial_in_gana": 5,
        "sutra_ref": "5.5",
        "upadesha_dev": "चिञ्",
        "upadesha_slp1": "ciY",
        "mula_dhatu_dev": "चि",
        "raw_dhatu_after_it_lopa_dev": "चि",
        "raw_dhatu_after_it_lopa_slp1": "ci",
        "artha_dev": "चयने",
        "artha_slp1": "cayane",
        "artha_en": "to gather, to collect",
        "gana_label_dev": "स्वादिः",
        "pada_label_dev": "उभयपदी",
        "it_class_label_dev": "अनिट्",
        "it_markers": ["ञ्"],
        "flags": {"anit": True, "set": False, "vet": False, "ekac": True, "udatta": False},
        "notes": "स्वादि चिञ् — engine तृच् demos; not in 940 Bhvādi v2 slice.",
    },
    {
        "id": "BvAdi_nIY",
        "tier": "curated_extension",
        "dhatupatha_id": None,
        "gana": 1,
        "gana_number": 1,
        "serial_in_gana": 988,
        "sutra_ref": "1.988",
        "upadesha_dev": "नीञ्",
        "upadesha_slp1": "nIY",
        "mula_dhatu_dev": "नी",
        "raw_dhatu_after_it_lopa_dev": "नी",
        "raw_dhatu_after_it_lopa_slp1": "nI",
        "artha_dev": "नयने",
        "artha_slp1": "nayane",
        "gana_label_dev": "भ्वादिः",
        "pada_label_dev": "परस्मैपदी",
        "it_class_label_dev": "अनिट्",
        "it_markers": [],
        "flags": {"anit": True, "set": False, "vet": False, "ekac": True, "udatta": False},
        "notes": "भ्वादि नीञ् (दातुपाठ १.९८८) — नेता तृच्।",
    },
    {
        "id": "BvAdi_zwuY",
        "tier": "curated_extension",
        "dhatupatha_id": None,
        "gana": 1,
        "gana_number": 1,
        "serial_in_gana": 1153,
        "sutra_ref": "1.1153",
        "upadesha_dev": "स्तुञ्",
        "upadesha_slp1": "stuY",
        "mula_dhatu_dev": "स्तु",
        "raw_dhatu_after_it_lopa_dev": "स्तु",
        "raw_dhatu_after_it_lopa_slp1": "stu",
        "artha_dev": "स्तुतौ",
        "artha_slp1": "stutO",
        "it_class_label_dev": "अनिट्",
        "it_markers": [],
        "flags": {"anit": True, "set": False, "vet": False, "ekac": True, "udatta": False},
        "notes": "स्तोता — ``stuY`` SLP1; full ``zwuY`` ठु-it pending extended १.३.५/९ in engine.",
    },
    {
        "id": "BvAdi_DukfY",
        "tier": "curated_extension",
        "dhatupatha_id": "08.0010",
        "gana": 8,
        "gana_number": 8,
        "serial_in_gana": 10,
        "sutra_ref": "8.10",
        "upadesha_dev": "डुकृञ्",
        "upadesha_slp1": "kF",
        "mula_dhatu_dev": "कृ",
        "raw_dhatu_after_it_lopa_dev": "कृ",
        "raw_dhatu_after_it_lopa_slp1": "kf",
        "artha_dev": "करणे",
        "artha_slp1": "karaRe",
        "gana_label_dev": "तनादिः",
        "pada_label_dev": "उभयपदी",
        "it_class_label_dev": "अनिट्",
        "it_markers": [],
        "flags": {"anit": True, "set": False, "vet": False, "ekac": True, "udatta": False},
        "notes": "डुकृञ् — ``kF`` engine slice until ``DukfY`` / ``qukfY`` डु-it is complete in it-prakaraṇa.",
    },
    {
        "id": "BvAdi_hfY",
        "tier": "curated_extension",
        "dhatupatha_id": None,
        "gana": 1,
        "gana_number": 1,
        "serial_in_gana": 1044,
        "sutra_ref": "1.1044",
        "upadesha_dev": "हृञ्",
        "upadesha_slp1": "hfY",
        "mula_dhatu_dev": "हृ",
        "raw_dhatu_after_it_lopa_dev": "हृ",
        "raw_dhatu_after_it_lopa_slp1": "hf",
        "artha_dev": "हरणे",
        "artha_slp1": "haraRe",
        "it_class_label_dev": "अनिट्",
        "it_markers": [],
        "flags": {"anit": True, "set": False, "vet": False, "ekac": True, "udatta": False},
        "notes": "हर्ता तृच्।",
    },
    {
        "id": "divAdi_tF",
        "tier": "curated_extension",
        "dhatupatha_id": None,
        "gana": 4,
        "gana_number": 4,
        "serial_in_gana": 1,
        "sutra_ref": "4.1",
        "upadesha_dev": "तॄ",
        "upadesha_slp1": "tF",
        "mula_dhatu_dev": "तॄ",
        "raw_dhatu_after_it_lopa_dev": "तॄ",
        "raw_dhatu_after_it_lopa_slp1": "tF",
        "artha_dev": "प्लवने",
        "artha_slp1": "plavane",
        "gana_label_dev": "दिवादिः",
        "pada_label_dev": "परस्मैपदी",
        "it_class_label_dev": "सेट्",
        "it_markers": [],
        "flags": {"anit": False, "set": True, "vet": False, "ekac": True, "udatta": True},
        "notes": "तरिता — दिवादि तॄ; उदात्त/सेट् for ७.२.१०।",
    },
    {
        "id": "BvAdi_950",
        "tier": "curated_extension",
        "dhatupatha_id": None,
        "gana": 1,
        "gana_number": 1,
        "serial_in_gana": 950,
        "sutra_ref": "1.950",
        "upadesha_dev": "णीञ्",
        "upadesha_slp1": "RIY",
        "mula_dhatu_dev": "णी",
        "raw_dhatu_after_it_lopa_dev": "नी",
        "raw_dhatu_after_it_lopa_slp1": "nI",
        "artha_dev": "प्रापणे",
        "artha_slp1": "prApaNe",
        "it_class_label_dev": "अनिट्",
        "it_markers": ["ण्", "ञ्"],
        "flags": {
            "anit": True,
            "set": False,
            "vet": False,
            "ekac": False,
            "udatta": False,
            "Nit_initial": True,
        },
        "notes": "णीञ् — णो नः (6.1.65) on Nvul path.",
    },
]


def _payload() -> dict:
    merged = _merge_bvadi_rows()
    extensions = deepcopy(_CURATED_EXTENSIONS)
    entries = merged + extensions

    # Aliases for stable short ids used in pipelines/tests.
    id_aliases = {
        "BvAdi_BU": "BvAdi_01_0001",
    }
    # Optional udātta / tṛc-oriented overrides (engine meta; see 7.2.10).
    flag_overrides = {
        "BvAdi_01_0001": {"udatta": True, "ekac": True},
    }

    return {
        "_schema_version": "2",
        "_title": "Dhātupāṭha — merged Bhvādi (v2) + curated extensions",
        "_sources": {
            "post_it_lopa": str(POST_IT.relative_to(ROOT)),
            "ashtadhyayi_txt": str(ASH.relative_to(ROOT)),
            "notes_md": "~/Documents/my panini notes/dhatupath.md (reference text, not machine-imported)",
        },
        "_stats": {
            "bvadi_merged": len(merged),
            "curated_extensions": len(extensions),
            "total_entries": len(entries),
        },
        "id_aliases": id_aliases,
        "flag_overrides": flag_overrides,
        "entries": entries,
    }


def main() -> None:
    payload = _payload()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    st = payload["_stats"]
    print(f"Wrote {OUT} — bvadi_merged={st['bvadi_merged']}, "
          f"curated_extensions={st['curated_extensions']}, total={st['total_entries']}")


if __name__ == "__main__":
    main()
