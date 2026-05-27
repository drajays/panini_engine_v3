"""
Constitutional test: no demo/pipeline identifiers in sutra arm key strings.

Scans all sutras/**/*.py files and fails if any file's source contains
demo-ID patterns (P038_, corrected_v2_P013_, prakriya_P013_, etc.) in
state.meta expressions. Pipeline files are excluded (they're being cleaned
up progressively).

Only sutras that have been refactored to remove demo-ID arm keys are
checked here. Additional sutras will be added as they are cleaned up.
"""
from __future__ import annotations

import re
import pathlib
import pytest

# Patterns that indicate demo/prakriya identifiers in arm key names.
_DEMO_ID_PATTERNS: list[re.Pattern] = [
    re.compile(r"P\d{3}_[a-z]"),
    re.compile(r"corrected_v2_P\d+"),
    re.compile(r"prakriya_P\d{3}_"),
]

# Regex to detect state.meta access expressions (get/set).
_META_ACCESS = re.compile(r'state\.meta(?:\[|\.get\()')

_SUTRAS_ROOT = pathlib.Path(__file__).parent.parent.parent / "sutras"

# Sutras that have been refactored to use clean arm keys (Batch 1 and forward).
# These are the sutras we've verified contain no demo-ID arm keys.
_REFACTORED_SUTRAS: list[str] = [
    "adhyaya_3/pada_3/sutra_3_3_161.py",
    "adhyaya_7/pada_4/sutra_7_4_59.py",
    "adhyaya_7/pada_2/sutra_7_2_79.py",
    "adhyaya_3/pada_4/sutra_3_4_105.py",
    "adhyaya_6/pada_1/sutra_6_1_97.py",
    "adhyaya_2/pada_2/sutra_2_2_29.py",
    "adhyaya_2/pada_2/sutra_2_2_34.py",
    "adhyaya_2/pada_4/sutra_2_4_81.py",
    "adhyaya_3/pada_1/sutra_3_1_69.py",
    "adhyaya_3/pada_1/sutra_3_1_77.py",
    "adhyaya_7/pada_1/sutra_7_1_3.py",
    "adhyaya_8/pada_2/sutra_8_2_39.py",
    "adhyaya_8/pada_4/sutra_8_4_56.py",
    "adhyaya_8/pada_4/sutra_8_4_68.py",
    "adhyaya_3/pada_4/sutra_3_4_99.py",
    "adhyaya_6/pada_1/sutra_6_1_66.py",
]


def _collect_refactored_sutra_files():
    return [_SUTRAS_ROOT / s for s in _REFACTORED_SUTRAS]


@pytest.mark.parametrize(
    "sutra_file",
    _collect_refactored_sutra_files(),
    ids=lambda p: str(p.relative_to(_SUTRAS_ROOT)),
)
def test_no_demo_ids_in_sutra_arm_keys(sutra_file: pathlib.Path) -> None:
    """Refactored sutra files must not use demo-ID prefixes in state.meta key strings."""
    source = sutra_file.read_text(encoding="utf-8")
    lines = source.splitlines()
    violations: list[str] = []
    for lineno, line in enumerate(lines, 1):
        # Only check lines that access state.meta
        if not _META_ACCESS.search(line):
            continue
        for pat in _DEMO_ID_PATTERNS:
            if pat.search(line):
                violations.append(f"  line {lineno}: {line.strip()}")
    if violations:
        msg = (
            f"{sutra_file.relative_to(_SUTRAS_ROOT)} "
            f"contains demo-ID arm key patterns in state.meta expressions:\n"
            + "\n".join(violations)
        )
        pytest.fail(msg)
