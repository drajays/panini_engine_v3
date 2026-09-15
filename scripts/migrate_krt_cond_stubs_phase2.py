#!/usr/bin/env python3
"""Extended migrator for adhyāya 3 stub cond() patterns."""
from __future__ import annotations

import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUTRAS = ROOT / "sutras" / "adhyaya_3"

KRT_IMPORT = "from engine.krt_eligibility import krt_insertion_eligible\n"
TIN_IMPORT = "from engine.krt_eligibility import tin_pratyaya_gate_eligible\n"


def sutra_id_from_path(p: Path) -> str:
    m = re.search(r"sutra_(\d)_(\d)_(\d+)\.py$", p.name)
    if not m:
        raise ValueError(p)
    return f"{m.group(1)}.{m.group(2)}.{m.group(3)}"


def _ensure_import(text: str, line: str) -> str:
    if line.strip() in text:
        return text
    return text.replace(
        "from engine.state import State\n",
        "from engine.state import State\n" + line,
    )


def migrate_krt_variants(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "krt_insertion_eligible" in text or "_GATE_KEY" not in text:
        return False
    if 'any("dhatu" in t.tags' not in text:
        return False
    sid = sutra_id_from_path(path)

    # Multiline: dhatu + not krt pratyaya yet
    if "not any(\"krt\" in t.tags" in text or "not any('krt' in t.tags" in text:
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

    out = re.sub(
        r"def cond\(state: State\) -> bool:.*?(?=\ndef act|\nSUTRA =)",
        new_cond + "\n",
        text,
        count=1,
        flags=re.S,
    )
    if out == text:
        return False
    out = _ensure_import(out, KRT_IMPORT)
    path.write_text(out, encoding="utf-8")
    return True


def migrate_tin_stubs(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "tin_pratyaya_gate_eligible" in text or "_GATE_KEY" not in text:
        return False
    if "paribhasha_gates" not in text:
        return False
    sid = sutra_id_from_path(path)
    if not sid.startswith("3.4."):
        return False

    new_cond = (
        f"def cond(state: State) -> bool:\n"
        f'    return tin_pratyaya_gate_eligible(state, "{sid}", gate_key=_GATE_KEY)\n'
    )
    out = re.sub(
        r"def cond\(state: State\) -> bool:.*?(?=\ndef act|\nSUTRA =)",
        new_cond + "\n",
        text,
        count=1,
        flags=re.S,
    )
    if out == text:
        return False
    out = _ensure_import(out, TIN_IMPORT)
    path.write_text(out, encoding="utf-8")
    return True


def main() -> None:
    krt_n = tin_n = 0
    for path in sorted(SUTRAS.rglob("sutra_*.py")):
        sid = sutra_id_from_path(path)
        if sid.startswith("3.2.") or sid.startswith("3.3."):
            if migrate_krt_variants(path):
                krt_n += 1
        elif sid.startswith("3.4."):
            if migrate_tin_stubs(path):
                tin_n += 1
    print(f"krt_variants={krt_n} tin_stubs={tin_n}")


if __name__ == "__main__":
    main()
