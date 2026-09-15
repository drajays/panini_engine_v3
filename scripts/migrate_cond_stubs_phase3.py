#!/usr/bin/env python3
"""Migrate 3.1 / 6.x / 8.x stub cond() patterns."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sutra_id_from_path(p: Path) -> str:
    m = re.search(r"sutra_(\d)_(\d)_(\d+)\.py$", p.name)
    if not m:
        raise ValueError(p)
    return f"{m.group(1)}.{m.group(2)}.{m.group(3)}"


def _ensure_import(text: str, line: str) -> str:
    if line.strip() in text:
        return text
    anchor = "from engine.state import State\n"
    if anchor in text:
        return text.replace(anchor, anchor + line)
    return text


def _replace_cond(path: Path, new_cond: str, import_line: str) -> bool:
    text = path.read_text(encoding="utf-8")
    out = re.sub(
        r"def cond\(state: State\) -> bool:.*?(?=\ndef act|\nSUTRA =)",
        new_cond + "\n",
        text,
        count=1,
        flags=re.S,
    )
    if out == text:
        return False
    out = _ensure_import(out, import_line)
    path.write_text(out, encoding="utf-8")
    return True


def migrate_31(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "krt_insertion_eligible" in text or "_GATE_KEY" not in text:
        return False
    if 'any("dhatu" in t.tags' not in text:
        return False
    sid = sutra_id_from_path(path)
    if "not any(\"krt\" in t.tags" in text:
        new_cond = (
            f"def cond(state: State) -> bool:\n"
            f"    if not krt_insertion_eligible(state, \"{sid}\", "
            f"gate_key=_GATE_KEY, adhikara_id=\"3.1.1\"):\n"
            f"        return False\n"
            f"    return not any(\n"
            f"        \"krt\" in t.tags and \"pratyaya\" in t.tags for t in state.terms\n"
            f"    )\n"
        )
    else:
        new_cond = (
            f"def cond(state: State) -> bool:\n"
            f'    return krt_insertion_eligible(state, "{sid}", '
            f"gate_key=_GATE_KEY, adhikara_id=\"3.1.1\")\n"
        )
    return _replace_cond(
        path,
        new_cond,
        "from engine.krt_eligibility import krt_insertion_eligible\n",
    )


def migrate_6(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "samhita_gate_eligible" in text or "_GATE_KEY" not in text:
        return False
    if "paribhasha_gates" not in text:
        return False
    sid = sutra_id_from_path(path)
    new_cond = (
        f"def cond(state: State) -> bool:\n"
        f'    return samhita_gate_eligible(state, "{sid}", gate_key=_GATE_KEY)\n'
    )
    return _replace_cond(
        path,
        new_cond,
        "from engine.krt_eligibility import samhita_gate_eligible\n",
    )


def migrate_8(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "tripadi_gate_eligible" in text or "_GATE_KEY" not in text:
        return False
    if not text.strip().startswith('"""') or "8." not in sutra_id_from_path(path):
        pass
    sid = sutra_id_from_path(path)
    if not sid.startswith("8."):
        return False
    new_cond = (
        f"def cond(state: State) -> bool:\n"
        f'    return tripadi_gate_eligible(state, "{sid}", gate_key=_GATE_KEY)\n'
    )
    return _replace_cond(
        path,
        new_cond,
        "from engine.krt_eligibility import tripadi_gate_eligible\n",
    )


def main() -> None:
    n31 = n6 = n8 = 0
    for path in sorted((ROOT / "sutras").rglob("sutra_*.py")):
        sid = sutra_id_from_path(path)
        if sid.startswith("3.1."):
            if migrate_31(path):
                n31 += 1
        elif sid.startswith("6."):
            if migrate_6(path):
                n6 += 1
        elif sid.startswith("8."):
            if migrate_8(path):
                n8 += 1
    print(f"3.1={n31} 6.x={n6} 8.x={n8}")


if __name__ == "__main__":
    main()
