"""
engine/registry.py — the global sūtra registry.
─────────────────────────────────────────────────

Every `sutras/**/sutra_X_Y_Z.py` file defines ONE module-level variable
named `SUTRA` that is an instance of `SutraRecord`, and then calls
`register_sutra(SUTRA)` at import time.

On `import sutras` (package), every sūtra file is imported in
deterministic order, which populates `SUTRA_REGISTRY`.

The engine dispatcher looks up rules via `SUTRA_REGISTRY[sutra_id]`.
There is NO other path from sūtra_id to rule — no scheduler hash,
no Python-level priority list, no module-scope side-effects.
"""
from __future__ import annotations

from typing import Dict

from engine.sutra_type import SutraRecord


# Mutable mapping sutra_id -> SutraRecord.
# Populated at import time by each sūtra file's register_sutra() call.
SUTRA_REGISTRY: Dict[str, SutraRecord] = {}


def register_sutra(rec: SutraRecord) -> None:
    """
    Register a SutraRecord.

    Raises
    ------
    ValueError
        If a sūtra with the same id is already registered (no silent
        overrides — every sūtra lives in exactly one file).
    """
    if rec.sutra_id in SUTRA_REGISTRY:
        raise ValueError(
            f"duplicate sūtra registration for {rec.sutra_id}; "
            f"every sūtra must live in exactly one file"
        )
    SUTRA_REGISTRY[rec.sutra_id] = rec


def get_sutra(sutra_id: str) -> SutraRecord:
    try:
        return SUTRA_REGISTRY[sutra_id]
    except KeyError:
        raise KeyError(
            f"sūtra {sutra_id!r} is not registered; "
            f"check sutras/adhyaya_{sutra_id.split('.')[0]}/..."
        )
