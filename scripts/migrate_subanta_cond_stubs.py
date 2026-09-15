#!/usr/bin/env python3
"""Batch-migrate adhyāya 1.2 / 1.4 / 2.3 / 2.4 paribhāṣā-stub cond() patterns."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GATE_KEY_RE = re.compile(
    r"state\.paribhasha_gates\.get\(\s*"
    r"(?:"
    r'(?P<var>[A-Z_][A-Z0-9_]*)'
    r"|"
    r'"(?P<lit>[^"]+)"'
    r")\s*\)\s*is not True"
)


def sutra_id_from_path(p: Path) -> str:
    m = re.search(r"sutra_(\d)_(\d)_(\d+)\.py$", p.name)
    if not m:
        raise ValueError(p)
    return f"{m.group(1)}.{m.group(2)}.{m.group(3)}"


def _ensure_import(text: str, line: str) -> str:
    if line.strip() in text:
        return text
    for anchor in (
        "from engine.state import State\n",
        "from engine.state  import State\n",
    ):
        if anchor in text:
            return text.replace(anchor, anchor + line, 1)
    return text


def _replace_cond(path: Path, new_cond: str, import_line: str) -> bool:
    text = path.read_text(encoding="utf-8")
    out = re.sub(
        r"def cond\(state(?:: State)?\) -> bool:.*?(?=\ndef act|\nSUTRA =)",
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


def _extract_gate_key(text: str) -> str | None:
    m = GATE_KEY_RE.search(text)
    if not m:
        return None
    if m.group("var"):
        return m.group("var")
    return f'"{m.group("lit")}"'


def _extract_gate_key_var(text: str) -> str | None:
    m = re.search(r"(_GATE_KEY|GATE_KEY|_GATE)\s*[:=]", text)
    if m:
        return m.group(1)
    return None


def _helper_for_sid(sid: str) -> tuple[str, str] | None:
    parts = [int(x) for x in sid.split(".")]
    if parts[0] == 1 and parts[1] == 2:
        if sid == "1.2.34":
            return (
                "yajna_accent_gate_eligible",
                "from engine.subanta_eligibility import yajna_accent_gate_eligible\n",
            )
        return (
            "accent_paribhasha_gate_eligible",
            "from engine.subanta_eligibility import accent_paribhasha_gate_eligible\n",
        )
    if parts[0] == 1 and parts[1] == 4:
        if sid in {"1.4.105", "1.4.106", "1.4.107"}:
            return (
                "sarvanama_paribhasha_gate_eligible",
                "from engine.subanta_eligibility import sarvanama_paribhasha_gate_eligible\n",
            )
        if sid in {"1.4.20", "1.4.21"} or sid >= "1.4.84":
            return (
                "chandasi_gate_eligible",
                "from engine.subanta_eligibility import chandasi_gate_eligible\n",
            )
        return (
            "nominal_paribhasha_gate_eligible",
            "from engine.subanta_eligibility import nominal_paribhasha_gate_eligible\n",
        )
    if parts[0] == 2 and parts[1] == 3:
        return (
            "karaka_gate_eligible",
            "from engine.subanta_eligibility import karaka_gate_eligible\n",
        )
    if parts[0] == 2 and parts[1] == 4 and parts[2] <= 9:
        return (
            "samasa_lakara_gate_eligible",
            "from engine.subanta_eligibility import samasa_lakara_gate_eligible\n",
        )
    return None


def migrate_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "subanta_eligibility" in text:
        return False
    gate_key = _extract_gate_key(text)
    if not gate_key:
        return False
    sid = sutra_id_from_path(path)
    helper_info = _helper_for_sid(sid)
    if not helper_info:
        return False
    helper, import_line = helper_info
    new_cond = (
        f"def cond(state: State) -> bool:\n"
        f"    return {helper}(state, {gate_key})\n"
    )
    return _replace_cond(path, new_cond, import_line)


def migrate_23_anga_pattern(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "subanta_eligibility" in text:
        return False
    if '"anga" in t.tags' not in text:
        return False
    gate_var = _extract_gate_key_var(text)
    if not gate_var:
        return False
    new_cond = (
        "def cond(state: State) -> bool:\n"
        f"    return karaka_gate_eligible(state, {gate_var})\n"
    )
    return _replace_cond(
        path,
        new_cond,
        "from engine.subanta_eligibility import karaka_gate_eligible\n",
    )


def fix_missing_imports() -> int:
    fixed = 0
    for path in ROOT.glob("sutras/**/*.py"):
        text = path.read_text(encoding="utf-8")
        if "subanta_eligibility import" in text:
            continue
        for helper, import_line in (
            ("karaka_gate_eligible", "from engine.subanta_eligibility import karaka_gate_eligible\n"),
            ("accent_paribhasha_gate_eligible", "from engine.subanta_eligibility import accent_paribhasha_gate_eligible\n"),
            ("chandasi_gate_eligible", "from engine.subanta_eligibility import chandasi_gate_eligible\n"),
            ("nominal_paribhasha_gate_eligible", "from engine.subanta_eligibility import nominal_paribhasha_gate_eligible\n"),
            ("samasa_lakara_gate_eligible", "from engine.subanta_eligibility import samasa_lakara_gate_eligible\n"),
            ("sarvanama_paribhasha_gate_eligible", "from engine.subanta_eligibility import sarvanama_paribhasha_gate_eligible\n"),
        ):
            if f"{helper}(state," in text:
                new_text = _ensure_import(text, import_line)
                if new_text != text:
                    path.write_text(new_text, encoding="utf-8")
                    fixed += 1
                break
    return fixed


def main() -> None:
    changed = 0
    globs = [
        "sutras/adhyaya_1/pada_2/sutra_1_2_*.py",
        "sutras/adhyaya_1/pada_4/sutra_1_4_*.py",
        "sutras/adhyaya_2/pada_3/sutra_2_3_*.py",
        "sutras/adhyaya_2/pada_4/sutra_2_4_[1-9].py",
    ]
    for pattern in globs:
        for path in sorted(ROOT.glob(pattern)):
            if migrate_file(path):
                changed += 1
                print("migrated", path.relative_to(ROOT))
    for path in sorted(ROOT.glob("sutras/adhyaya_2/pada_3/sutra_2_3_*.py")):
        if migrate_23_anga_pattern(path):
            changed += 1
            print("migrated anga", path.relative_to(ROOT))
    imports = fix_missing_imports()
    print(f"done: {changed} cond migrations, {imports} import fixes")


if __name__ == "__main__":
    main()
