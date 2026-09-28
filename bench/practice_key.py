"""
bench/practice_key.py — which forms.db cells are safe to use as a practice answer key.
─────────────────────────────────────────────────────────────────────────────────────

A practice question that teaches a wrong form is worse than no question, so
``core/practice`` only asks cells where this engine's surface is among
Vidyut's forms for the same cell. Runs under the venv that has ``vidyut``:

    .venv/bin/python -m bench.practice_key

Writes ``bench/oracle/practice_verified.json``:
    {"generated_at": ..., "verified": [cell_key, ...], "disagree": {cell_key: [ours, vidyut]},
     "path_ok": [cell_key, ...], "path_extra": {cell_key: [sūtra, ...]}}
``verified``  — our surface is among Vidyut's (safe for form questions).
``path_ok``   — additionally, every sūtra that changed our surface appears in
                Vidyut's path (safe for "which sūtra?" and sūtra examples).
``path_extra``— right form, sūtra Vidyut never used: a glass-box bug.
The disagreements double as a bug list for the engine.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from bench.oracle_vidyut import _derive  # noqa: E402
from engine.form_index import connect, iter_rows  # noqa: E402

OUT_PATH = _ROOT / "bench" / "oracle" / "practice_verified.json"
_LINGA = {"pulliṅga": "pum", "strīliṅga": "stri", "napuṃsaka": "napumsaka"}


def oracle_cell(row: dict) -> dict:
    f = row["features"]
    if row["kind"] == "subanta":
        return {"kind": "subanta", "stem": row["lemma"], "linga": _LINGA[f["linga"]],
                "vibhakti": f["vibhakti"], "vacana": f["vacana"]}
    path_id = row["cell_key"].split("@")[1].split(":")[0]         # tinanta:BU@01.0001:laT:1:1
    return {"kind": "tinanta", "dhatu": accented(row["lemma"], path_id),
            "gana": int(path_id.split(".")[0]), "lakara": f["lakara"],
            "purusha": f["purusha"], "vacana": f["vacana"]}


def accented(upadesha: str, path_id: str) -> str:
    """Vidyut reads pada *and* seṭ/aniṭ from svara, which our upadeśas omit.
    Mark them as Vidyut's own dhātupāṭha does:
      - aniṭ (anudātta upadeśa, 7.2.10): ``\\`` after the root vowel — qupa\\ca~^z, RI\\Y
      - ātmanepadī: the anunāsika it-vowel anudātta — eDa~\\
      - ubhayapadī: the it-vowel svarita — qupa\\ca~^z
    A ṅit/ñit root already carries its pada in the final it-consonant."""
    from pipelines.dhatupatha import resolve_dhatu_identifier
    try:
        row = resolve_dhatu_identifier(path_id)
    except KeyError:
        return upadesha
    out = upadesha
    if (row.get("flags") or {}).get("anit"):
        start = 2 if out.startswith(("qu", "wu", "Yi")) else 0   # skip ādi ñi/ṭu/ḍu
        for i in range(start, len(out)):
            if out[i] in "aAiIuUfFxXeEoO" and not out[i + 1:i + 2] == "~":
                out = out[:i + 1] + "\\" + out[i + 1:]
                break
    mark = {"आत्मनेपदी": "\\", "उभयपदी": "^"}.get(row.get("pada_label_dev"))
    if mark and not out.endswith(("N", "Y")) and "~" in out:
        i = out.rindex("~") + 1
        out = out[:i] + mark + out[i:]
    return out


def main() -> int:
    ours: dict[str, set[str]] = defaultdict(set)
    rows: dict[str, dict] = {}
    for row in iter_rows():
        ours[row["cell_key"]].add(row["surface_slp1"])
        rows[row["cell_key"]] = row
    fired: dict[str, set[str]] = defaultdict(set)
    conn = connect()
    for sid, key in conn.execute("SELECT sutra_id, cell_key FROM firings"):
        fired[key].add(sid)
    conn.close()
    verified, disagree, declined = [], {}, 0
    path_ok, path_extra = [], {}
    for key, row in rows.items():
        try:
            forms, path = _derive(oracle_cell(row))
        except Exception:
            forms, path = "", ""
        if not forms:
            declined += 1
            continue
        theirs = set(forms.split("|"))
        if ours[key] <= theirs:
            verified.append(key)
            extra = sorted(fired[key] - set(path.split()))
            if extra:
                path_extra[key] = extra
            else:
                path_ok.append(key)
        else:
            disagree[key] = [sorted(ours[key]), sorted(theirs)]
    OUT_PATH.write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "verified": sorted(verified), "disagree": disagree,
        "path_ok": sorted(path_ok), "path_extra": path_extra,
    }, ensure_ascii=False, indent=0) + "\n")
    print(f"[practice_key] {len(rows)} cells: {len(verified)} verified, "
          f"{len(disagree)} disagree, {declined} oracle-declined; of verified: "
          f"{len(path_ok)} path-ok, {len(path_extra)} wrong-sūtra → {OUT_PATH.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
