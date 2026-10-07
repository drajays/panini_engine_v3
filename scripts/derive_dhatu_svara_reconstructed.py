#!/usr/bin/env python3
"""
Build ``data/inputs/dhatu_svara_reconstructed.json`` by running 1.3.11/1.3.12/
1.3.72/1.3.78 **in reverse** over ``data/inputs/dhatupatha_upadesha.json``.

Pāṇini's own dhātupāṭha marks each dhātu's *vowel* with one of three svaras —
udātta (unmarked), anudātta (the "underline" mark), or svarita (the vertical
stroke) — and 1.3.12/1.3.72/1.3.78 read those marks (plus the structural ṅit/
ñit anubandhas, which are separate from accent) forward, to assign kartari
pada. This engine's own upadeśa strings never carried the accent diacritic
(only the anunāsika ``~`` survived import — see docs/DHATU_SVARA_RECONSTRUCTION.md);
``pada_label_dev`` was instead scraped pre-resolved from ashtadhyayi.com.

This script runs that implication **backward**: given the already-classified
``pada_label_dev`` (परस्मैपदी / आत्मनेपदी / उभयपदी) and the *structural* ṅit/ñit
facts (which do NOT require accent — they are visible as the dhātu's own
trailing it-consonant in ``upadesha_dev``, e.g. षूङ्, कृञ्), it reconstructs
which svara the upadeśa's vowel *must* have carried for 1.3.12/1.3.72/1.3.78 to
land on that pada by the default (śeṣa) route, one entry at a time:

  पद              ित्-मार्ग (कोई उच्चारण नहीं)        उच्चारण-मार्ग
  -----------      --------------------------        -------------------
  आत्मनेपदी        ङित् (अन्त्य ङ्)  → कोई स्वर नहीं     अन्यथा → अनुदात्त   (1.3.12)
  उभयपदी           ञित् (अन्त्य ञ्)  → कोई स्वर नहीं     अन्यथा → स्वरित    (1.3.72)
  परस्मैपदी        (कभी ङित्/ञित् नहीं — शेष)                      → उदात्त     (1.3.78, default)

See docs/DHATU_SVARA_RECONSTRUCTION.md for full methodology, caveats (chiefly:
the brain at ~/data-master/ashtadhyayi-ai, which carries the real accented
upadeśa for cross-verification, is not available in this session/container,
so this reconstruction is a best-effort inverse of the already-verified
pada_label_dev — not an independent confirmation from source accent), and the
known anomaly (नीञ् / BvAdi_nIY).

Run from repo root::

    python3 scripts/derive_dhatu_svara_reconstructed.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "inputs" / "dhatupatha_upadesha.json"
OUT = ROOT / "data" / "inputs" / "dhatu_svara_reconstructed.json"

_NGIT_SUFFIX = "ङ्"
_YIT_SUFFIX = "ञ्"


def _pada_of(entry: dict) -> str | None:
    label = entry.get("pada_label_dev") or ""
    if "उभय" in label:
        return "U"
    if "आत्मने" in label:
        return "A"
    if "परस्मै" in label:
        return "P"
    return None


def _ngit_final(entry: dict) -> bool:
    return (entry.get("upadesha_dev") or "").strip().endswith(_NGIT_SUFFIX)


def _yit_final(entry: dict) -> bool:
    return (entry.get("upadesha_dev") or "").strip().endswith(_YIT_SUFFIX)


def _reconstruct(entry: dict) -> dict:
    pada = _pada_of(entry)
    ngit, yit = _ngit_final(entry), _yit_final(entry)

    svara: str | None
    governed_by: str | None
    basis: str
    confidence: str
    caveat: str | None = None

    if pada == "A":
        if ngit:
            svara, governed_by, basis, confidence = None, "1.3.12", "ngit", "high"
        else:
            svara, governed_by, basis, confidence = "anudatta", "1.3.12", "accent", "high"
    elif pada == "U":
        if yit:
            svara, governed_by, basis, confidence = None, "1.3.72", "yit", "high"
            caveat = (
                "1.3.72 ubhayapada is kartari-abhiprāya-conditioned at the usage "
                "level (vibhāṣā); this entry's lexical capacity for ātmanepada "
                "rests on its ñit marking alone, independent of accent."
            )
        else:
            svara, governed_by, basis, confidence = "svarita", "1.3.72", "accent", "medium"
            caveat = (
                "No trailing ñit marker; reconstructed svarita is inferred "
                "solely from the उभयपदी label — the brain's accented upadeśa "
                "was not available in this session to verify directly."
            )
    elif pada == "P":
        basis = "default"
        svara, governed_by, confidence = "udatta", "1.3.78", "high"
        if ngit or yit:
            confidence = "low"
            bad = _NGIT_SUFFIX if ngit else _YIT_SUFFIX
            caveat = (
                f"Lexically labeled परस्मैपदी despite a trailing {bad} it-marker, "
                "which should license आत्मनेपद/उभयपद by 1.3.12/1.3.72. Likely a "
                "data anomaly in this engine's curated row, not a real "
                "exception — needs re-verification against the brain."
            )
    else:
        basis = "unknown"
        svara, governed_by, confidence = None, None, "low"
        if yit or ngit:
            mark, implied = (_YIT_SUFFIX, "उभयपदी (1.3.72 ñit)") if yit else (_NGIT_SUFFIX, "आत्मनेपदी (1.3.12 ṅit)")
            caveat = (
                f"No pada_label_dev on this row; trailing {mark} structurally "
                f"implies {implied} by convention — pada_label_dev should be "
                "backfilled and this entry reverified."
            )
        else:
            caveat = "No pada_label_dev and no ṅit/ñit marker; cannot reconstruct."

    return {
        "id": entry.get("id"),
        "dhatupatha_id": entry.get("dhatupatha_id"),
        "gana": entry.get("gana"),
        "upadesha_dev": entry.get("upadesha_dev"),
        "upadesha_slp1": entry.get("upadesha_slp1"),
        "pada_label_dev": entry.get("pada_label_dev"),
        "ngit_final": ngit,
        "yit_final": yit,
        "reconstructed_svara": svara,
        "svara_governed_by": governed_by,
        "svara_basis": basis,
        "confidence": confidence,
        "caveat": caveat,
    }


_WARNING = (
    "CIRCULAR WRT pada_label_dev — DO NOT wire into 1.3.12/1.3.72/1.3.78 cond()/act(). "
    "Every reconstructed_svara here was computed FROM pada_label_dev (plus structural "
    "ngit/yit); feeding it back to re-derive pada is pada_label_dev re-deriving itself "
    "through an extra hop, not an independent structural check. It only becomes a "
    "legitimate cond() input once it is replaced by svara read from the brain's real "
    "accented upadesha (see docs/DHATU_SVARA_RECONSTRUCTION.md Caveats)."
)


def _payload() -> dict:
    src = json.loads(SRC.read_text(encoding="utf-8"))
    rows = [_reconstruct(e) for e in src["entries"]]

    stats: dict[str, int] = {}
    for r in rows:
        key = f"{r['pada_label_dev'] or 'none'}:{r['svara_basis']}"
        stats[key] = stats.get(key, 0) + 1
    confidence_counts: dict[str, int] = {}
    for r in rows:
        confidence_counts[r["confidence"]] = confidence_counts.get(r["confidence"], 0) + 1

    return {
        "_schema_version": "1",
        "_title": "Dhātu svara (udātta/anudātta/svarita) reconstructed in reverse from "
                   "pada_label_dev + structural ṅit/ñit, per 1.3.11/1.3.12/1.3.72/1.3.78",
        "_source": str(SRC.relative_to(ROOT)),
        "_method": "docs/DHATU_SVARA_RECONSTRUCTION.md",
        "_warning": _WARNING,
        "_stats": {"by_pada_and_basis": stats, "by_confidence": confidence_counts, "total": len(rows)},
        "entries": rows,
    }


def main() -> None:
    payload = _payload()
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} — {payload['_stats']}")


if __name__ == "__main__":
    main()
