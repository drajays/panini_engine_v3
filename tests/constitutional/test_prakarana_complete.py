"""AMENDMENT 24 / Art. 23 §6: every sūtra of the engine is a member of at least one prakaraṇa module (Pushpa Dixit's prakaraṇas, Pāṇini's
data), and the map names no sūtra the engine does not have. Static: ids come from the sūtra file names (cheap, import-order proof)."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAP = json.loads((ROOT / "data" / "inputs" / "prakarana_map.json").read_text(encoding="utf-8"))
FILES = sorted((ROOT / "sutras").glob("adhyaya_*/pada_*/sutra_*.py"))
ENGINE_IDS = {".".join(re.match(r"sutra_(\d+)_(\d+)_(\d+)", f.name).groups()) for f in FILES}


def test_every_engine_sutra_is_in_a_prakarana():
    attached = set(MAP["sutra_to_prakarana"])
    assert ENGINE_IDS - attached == set(), f"unattached: {sorted(ENGINE_IDS - attached)[:10]}"
    assert attached - ENGINE_IDS == set(), f"map names sūtras the engine lacks: {sorted(attached - ENGINE_IDS)[:10]}"


def test_inverse_is_consistent():
    inv = {}
    for pid, mod in MAP["prakaranas"].items():
        assert mod["status"] in {"data", "hyp", "pending"}, pid
        for s in mod["sutras"]:
            inv.setdefault(s, []).append(pid)
    assert {k: sorted(v) for k, v in inv.items()} == {k: sorted(v) for k, v in MAP["sutra_to_prakarana"].items()}


def test_module_reader():
    from engine import prakarana

    assert "6.1.8" in prakarana.members("P04") and prakarana.of("6.1.8")
    assert all(prakarana.of(s) for s in list(ENGINE_IDS)[:200])
