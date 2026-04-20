"""
sutras/__init__.py — orchestrated loader.
───────────────────────────────────────────

Importing `sutras` causes every sūtra file under
`sutras/adhyaya_*/pada_*/sutra_*.py` to be imported in Aṣṭādhyāyī
order.  Each file calls register_sutra(), so after this import
`engine.SUTRA_REGISTRY` is fully populated.

We walk the directory tree and import files in the canonical order:
  1. Adhyāya 1 → 8
  2. within each adhyāya, pāda 1 → 4
  3. within each pāda, numeric sūtra order (1, 2, ... 10, 11, ...)
"""
from __future__ import annotations

import importlib
import pkgutil
import re
from pathlib import Path


_SUTRA_FILE_RE = re.compile(r"^sutra_(\d+)_(\d+)_(\d+)(?:_.+)?$")


def _load_all_sutras() -> None:
    root = Path(__file__).parent
    # Deterministic walk.
    for adhyaya_dir in sorted(root.glob("adhyaya_*")):
        if not adhyaya_dir.is_dir():
            continue
        for pada_dir in sorted(adhyaya_dir.glob("pada_*")):
            if not pada_dir.is_dir():
                continue
            # Collect sūtra files with numeric sort.
            files = []
            for p in pada_dir.glob("sutra_*.py"):
                m = _SUTRA_FILE_RE.match(p.stem)
                if not m:
                    continue
                files.append((
                    (int(m.group(1)), int(m.group(2)), int(m.group(3))),
                    p,
                ))
            files.sort()
            for _key, path in files:
                mod_name = (
                    f"sutras.{adhyaya_dir.name}.{pada_dir.name}.{path.stem}"
                )
                importlib.import_module(mod_name)


# Load on package import.
_load_all_sutras()
