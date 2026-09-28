"""
tests/constitutional/test_engine_is_rule_based.py
─────────────────────────────────────────────────

The engine derives by rule, never by consulting an answer.

Three external answer sources now live in this repo, all *downstream* of the
engine: the Vidyut oracle (``bench/``), the list of cells it verified
(``bench/oracle/practice_verified.json``) and the presentation layers built on
them (``core/practice.py``, ``core/lab.py``). They may read the engine; the
engine may never read them. (``data/reference`` and ``forms.db`` have their
own firewalls: test_no_reference_import_from_engine, test_form_index_is_a_cache.)
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

RULE_PATH = [
    *(ROOT / d for d in ("engine", "sutras", "phonology", "pipelines")),
    ROOT / "core" / "phases",
    ROOT / "core" / "canonical_pipelines.py",
]
FORBIDDEN = re.compile(
    r"^\s*(?:from|import)\s+(?:vidyut|bench|core\.practice|core\.lab)\b"
    r"|practice_verified|oracle_vidyut|oracle_batch",
    re.M,
)


def _rule_files():
    for base in RULE_PATH:
        yield from ([base] if base.is_file() else base.rglob("*.py"))


def test_rule_path_never_imports_an_answer_source():
    offenders = [p.relative_to(ROOT).as_posix() for p in _rule_files()
                 if FORBIDDEN.search(p.read_text(encoding="utf-8"))]
    assert offenders == [], (
        "a sūtra or spine that consults Vidyut / the verified list / the practice "
        f"layer is deciding by lookup, not by rule — {offenders}"
    )


def test_deriving_never_loads_an_answer_source():
    """Runtime proof: derive a spread of forms in a clean process; none of the
    answer sources may be in sys.modules afterwards."""
    code = (
        "import sutras\n"
        "from pipelines.subanta import derive as s\n"
        "from pipelines.tinanta import derive as t\n"
        "s('rAma', 3, 1); t('eDa~', 'liT', 'kartari', 3, 1); t('pac', 'lRT', 'karmani', 3, 1)\n"
        "t('BU', 'luG', 'kartari', 3, 1); t('qukfY', 'laT', 'bhave', 3, 1)\n"
        "import sys\n"
        "bad = [m for m in sys.modules if m.split('.')[0] in {'vidyut', 'bench'}"
        " or m in {'core.practice', 'core.lab'}]\n"
        "print(bad)"
    )
    out = subprocess.run([sys.executable, "-c", code], cwd=ROOT,
                         capture_output=True, text=True, check=True)
    assert out.stdout.strip().splitlines()[-1] == "[]", out.stdout
