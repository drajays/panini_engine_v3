#!/usr/bin/env python3
"""
Build ``data/inputs/dhatupatha_upadesha.json`` from v2 exports:

  * ``dhatu_upadesha_post_it_lopa.json`` (940 Bhvādi roots)
  * ``dhatupatha_ashtadhyayi_txt.json`` (meanings / it-class / pada)

Resolved from, in order: ``<repo>/panini_engine_v2/data`` if present, else
``~/Documents/panini_engine_v2/data`` (see ``_v2_data_dir()``).

Plus **curated extensions** for dhātus outside that Bhvādi slice (other gaṇas) used by
pipelines/tests (tṛc examples, णीञ्, etc.), plus a bulk import of **gaṇas 2–10** from
``ashtadhyayi-com/data`` (``dhatu/data.txt``, cached at ``data/upstream/`` and fetched on
first run) — Phase E1 of ``ROADMAP.md``. That source already carries the post-it-lopa
``dhatu`` form alongside the ``aupadeshik`` (upadeśa) form, so no it-lopa is guessed here;
``it_markers`` is left ``[]`` for imported rows since ``aupadeshik → dhatu`` sometimes
involves n-āgama/samprasāraṇa, not pure substring removal, and the field is not
consumed by the live 1.3.2–1.3.9 it-saṃjñā sūtras (those read ``upadesha_slp1`` directly).

Reference documentation: ``~/Documents/my panini notes/dhatupath.md`` (full pāṭha text).

Run from repo root::

    python3 scripts/build_dhatupatha_upadesha_v3.py
"""
from __future__ import annotations

import json
import urllib.request
from copy import deepcopy
from pathlib import Path

from phonology.pratyahara import is_ekac_upadesha
from phonology.tokenizer import devanagari_to_slp1_flat

ROOT = Path(__file__).resolve().parents[1]

ASHTADHYAYI_DHATU_URL = "https://raw.githubusercontent.com/ashtadhyayi-com/data/master/dhatu/data.txt"
ASHTADHYAYI_DHATU_CACHE = ROOT / "data" / "upstream" / "ashtadhyayi_dhatu_data.json"

_GANA_META = {
    2: ("Adadi", "अदादिः", "adadi"),
    3: ("JuhotyAdi", "जुहोत्यादिः", "juhotyadi"),
    4: ("divAdi", "दिवादिः", "divadi"),
    5: ("svAdi", "स्वादिः", "svadi"),
    6: ("tudAdi", "तुदादिः", "tudadi"),
    7: ("ruDAdi", "रुधादिः", "rudhadi"),
    8: ("tanAdi", "तनादिः", "tanadi"),
    9: ("kryAdi", "क्र्यादिः", "kryadi"),
    10: ("curAdi", "चुरादिः", "curadi"),
}
_PADA_LABEL = {"P": "परस्मैपदी", "A": "आत्मनेपदी", "U": "उभयपदी"}
_KARMA_LABEL = {"S": "सकर्मकः", "A": "अकर्मकः", "D": "द्विकर्मकः"}
_SETTVA_LABEL = {"S": "सेट्", "A": "अनिट्", "V": "वेट्"}


def _v2_data_dir() -> Path:
    """Prefer nested ignored clone; fallback to Documents checkout."""
    nested = ROOT / "panini_engine_v2" / "data"
    docs = Path.home() / "Documents" / "panini_engine_v2" / "data"
    marker = "dhatu_upadesha_post_it_lopa.json"
    if (nested / marker).is_file():
        return nested
    if (docs / marker).is_file():
        return docs
    return nested


V2 = _v2_data_dir()
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


def _load_ashtadhyayi_dhatu_source() -> list[dict]:
    """All dhātupāṭha rows from ashtadhyayi-com/data; cached locally after first fetch."""
    if not ASHTADHYAYI_DHATU_CACHE.is_file():
        ASHTADHYAYI_DHATU_CACHE.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(ASHTADHYAYI_DHATU_URL, timeout=30) as resp:
            ASHTADHYAYI_DHATU_CACHE.write_bytes(resp.read())
    payload = json.loads(ASHTADHYAYI_DHATU_CACHE.read_text(encoding="utf-8"))
    return payload["data"]


def _merge_ganas_2_10_rows(existing_keys: set[tuple[int, str]]) -> list[dict]:
    """Gaṇas 2–10 bulk-imported from ashtadhyayi-com/data, skipping ids already curated."""
    out: list[dict] = []
    skipped_existing = skipped_unspecified = 0
    for e in _load_ashtadhyayi_dhatu_source():
        gana_raw = str(e.get("gana", ""))
        if not gana_raw.isdigit():
            continue
        gana = int(gana_raw)
        if not (2 <= gana <= 10):
            continue
        did = e["baseindex"]
        if (gana, did) in existing_keys:
            skipped_existing += 1
            continue
        pada, settva, karma = e.get("pada"), e.get("settva"), e.get("karma")
        if pada not in _PADA_LABEL or settva not in _SETTVA_LABEL or karma not in _KARMA_LABEL:
            skipped_unspecified += 1
            continue
        prefix, gana_label, tier = _GANA_META[gana]
        up_dev, after_dev = e["aupadeshik"], e["dhatu"]
        up_slp = _safe_slp1_from_deva(did, up_dev)
        after_slp = _safe_slp1_from_deva(f"{did}_after", after_dev)
        artha_dev = e.get("artha") or None
        row = {
            "id": f"{prefix}_{did.replace('.', '_')}",
            "tier": f"{tier}_v3_import",
            "dhatupatha_id": did,
            "gana": gana,
            "gana_number": gana,
            "serial_in_gana": int(did.split(".")[1]),
            "sutra_ref": did,
            "upadesha_dev": up_dev,
            "upadesha_slp1": up_slp,
            "mula_dhatu_dev": after_dev,
            "raw_dhatu_after_it_lopa_dev": after_dev,
            "raw_dhatu_after_it_lopa_slp1": after_slp,
            "artha_dev": artha_dev,
            "artha_slp1": _safe_slp1_from_deva(f"{did}_artha", artha_dev) if artha_dev else None,
            "artha_en": e.get("artha_english") or None,
            "artha_hi": e.get("artha_hindi") or None,
            "gana_label_dev": gana_label,
            "pada_label_dev": _PADA_LABEL[pada],
            "karmatva_label_dev": _KARMA_LABEL[karma],
            "it_class_label_dev": _SETTVA_LABEL[settva],
            "it_markers": [],
            "flags": {
                "anit": settva == "A",
                "set": settva == "S",
                "vet": settva == "V",
                "ekac": bool(after_slp and is_ekac_upadesha(after_slp)),
                "udatta": "उदात्त" in (e.get("tags") or ""),
            },
            "notes": f"ashtadhyayi-com/data dhatu/data.txt i={e.get('i')}.",
        }
        out.append(row)
    out.sort(key=lambda r: (r["gana"], r["serial_in_gana"]))
    print(
        f"ganas 2-10 import: {len(out)} new, {skipped_existing} already curated, "
        f"{skipped_unspecified} unspecified pada/settva/karma skipped"
    )
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


def _merged_and_extensions_base() -> tuple[list[dict], list[dict]]:
    """(merged, extensions) — rebuilt from v2 sources when available, else the rows
    already committed in ``OUT`` are treated as an opaque, trusted base."""
    if POST_IT.is_file() and ASH.is_file():
        return _merge_bvadi_rows(), deepcopy(_CURATED_EXTENSIONS)
    if OUT.is_file():
        existing = json.loads(OUT.read_text(encoding="utf-8"))
        return existing.get("entries", []), []
    return [], []


def _payload() -> dict:
    merged, extensions = _merged_and_extensions_base()
    existing_keys = {
        (r["gana"], r["dhatupatha_id"])
        for r in merged + extensions
        if r.get("dhatupatha_id") is not None
    }
    ganas_2_10 = _merge_ganas_2_10_rows(existing_keys)
    entries = merged + extensions + ganas_2_10

    # Aliases for stable short ids used in pipelines/tests.
    id_aliases = {
        "BvAdi_BU": "BvAdi_01_0001",
    }
    # Optional udātta / tṛc-oriented overrides (engine meta; see 7.2.10).
    flag_overrides = {
        "BvAdi_01_0001": {"udatta": True, "ekac": True},
    }

    return {
        "_schema_version": "3",
        "_title": "Dhātupāṭha — merged Bhvādi (v2) + curated extensions + gaṇas 2-10 (ashtadhyayi-com/data)",
        "_sources": {
            "post_it_lopa": str(POST_IT.relative_to(ROOT)),
            "ashtadhyayi_txt": str(ASH.relative_to(ROOT)),
            "notes_md": "~/Documents/my panini notes/dhatupath.md (reference text, not machine-imported)",
            "ashtadhyayi_com_dhatu": f"{ASHTADHYAYI_DHATU_URL} (cached: {ASHTADHYAYI_DHATU_CACHE.relative_to(ROOT)})",
        },
        "_stats": {
            "bvadi_merged": len(merged),
            "curated_extensions": len(extensions),
            "ganas_2_10_imported": len(ganas_2_10),
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
