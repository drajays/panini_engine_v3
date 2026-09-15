#!/usr/bin/env python3
"""
One-shot migrator: adhyāya 3 kṛt stub cond() → krt_insertion_eligible().

Run from repo root:
    python3 scripts/migrate_krt_cond_stubs.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUTRAS = ROOT / "sutras" / "adhyaya_3"

STANDARD_COND = re.compile(
    r"def cond\(state: State\) -> bool:\n"
    r"    if state\.paribhasha_gates\.get\(_GATE_KEY\) is True:\n"
    r"        return False\n"
    r"    if any\(\"dhatu\" in t\.tags for t in state\.terms\):\n"
    r"        return True\n"
    r"(?:    return False\n)?",
    re.MULTILINE,
)

IMPORT_LINE = "from engine.krt_eligibility import krt_insertion_eligible\n"


def sutra_id_from_path(p: Path) -> str:
    m = re.search(r"sutra_(\d)_(\d)_(\d+)\.py$", p.name)
    if not m:
        raise ValueError(p)
    return f"{m.group(1)}.{m.group(2)}.{m.group(3)}"


def migrate_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "krt_insertion_eligible" in text:
        return False
    if "_GATE_KEY" not in text:
        return False
    if not STANDARD_COND.search(text):
        return False

    sid = sutra_id_from_path(path)
    new_cond = (
        f"def cond(state: State) -> bool:\n"
        f'    return krt_insertion_eligible(state, "{sid}", '
        f"gate_key=_GATE_KEY, adhikara_id=\"3.1.1\")\n"
    )
    out = STANDARD_COND.sub(new_cond, text, count=1)
    if IMPORT_LINE not in out:
        out = out.replace(
            "from engine.state import State\n",
            "from engine.state import State\n" + IMPORT_LINE,
        )
    if out == text:
        return False
    path.write_text(out, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    skipped = 0
    for path in sorted(SUTRAS.rglob("sutra_*.py")):
        # 3.4.x tiṅ rules — separate discipline; 3.1.x mixed patterns
        parts = path.name.replace("sutra_", "").replace(".py", "").split("_")
        if len(parts) >= 2 and parts[0] == "3" and parts[1] in {"1", "4"}:
            skipped += 1
            continue
        if migrate_file(path):
            changed += 1
        else:
            skipped += 1
    print(f"migrated={changed} skipped={skipped}")


if __name__ == "__main__":
    main()
