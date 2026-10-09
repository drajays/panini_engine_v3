"""P1 (PRAKARANA_MACHINE_PLAN): the adhikāra scope index covers every sūtra and names only real sūtras."""
import json
from pathlib import Path

from engine.registry import SUTRA_REGISTRY  # noqa: F401
import sutras  # noqa: F401

IDX = json.loads((Path(__file__).resolve().parents[2] / "data" / "inputs" / "adhikara_scope_index.json").read_text())["scope"]


def test_index_covers_every_sutra():
    assert set(IDX) == set(SUTRA_REGISTRY)


def test_heads_are_sutras_and_precede_members():
    key = lambda s: tuple(map(int, s.split(".")))
    for m, hs in IDX.items():
        for h in hs:
            assert h in IDX and key(h) <= key(m), (h, m)
