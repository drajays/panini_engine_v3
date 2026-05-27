"""
Constitutional test: no morphological decisions predicated on purusha/vacana
cell coordinates.

Scans the main tinanta.py pipeline for lines that combine purusha/vacana
coordinate references with direct 'state.meta[' assignment or '.varnas ='
mutation on the same line.

This catches cases where a morphological transformation is gated on tinganta
cell coordinates rather than phonemic/structural conditions.

Note: the legitimate use of purusha/vacana for ROUTING (selecting which tinam
adesha to call, or which pipeline function to invoke) is NOT a violation.
Only same-line morphological mutations predicated on coordinates are flagged.
"""
from __future__ import annotations

import re
import pathlib
import pytest

_COORD_PATTERN = re.compile(r'\b(?:purusha|vacana)\b')
_META_ASSIGN   = re.compile(r'state\.meta\[')
_VARNAS_ASSIGN = re.compile(r'\.varnas\s*=')

_PIPELINES_ROOT = pathlib.Path(__file__).parent.parent.parent / "pipelines"

# Main pipeline files to scan for this constitutional constraint.
_SCAN_FILES: list[str] = [
    "tinanta.py",
]


@pytest.mark.parametrize(
    "pipeline_file",
    [_PIPELINES_ROOT / f for f in _SCAN_FILES],
    ids=lambda p: p.name,
)
def test_no_purusha_vacana_in_morphological_ops(pipeline_file: pathlib.Path) -> None:
    """Pipeline lines must not combine purusha/vacana coordinate checks with
    direct meta-assignment or varnas-mutation on the same line."""
    source = pipeline_file.read_text(encoding="utf-8")
    lines = source.splitlines()
    violations: list[str] = []
    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if not _COORD_PATTERN.search(line):
            continue
        if _META_ASSIGN.search(line) or _VARNAS_ASSIGN.search(line):
            violations.append(f"  line {lineno}: {stripped}")
    if violations:
        msg = (
            f"{pipeline_file.name} "
            f"combines purusha/vacana coordinate with state.meta[] or .varnas= "
            f"on the same line:\n"
            + "\n".join(violations)
        )
        pytest.fail(msg)
