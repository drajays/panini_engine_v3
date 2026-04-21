"""Shared path setup for Streamlit pages."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

GOLD_PATH = ROOT / "data" / "reference" / "subanta_gold" / "rama_pullinga.json"


def load_rama_gold() -> dict:
    with open(GOLD_PATH, encoding="utf-8") as f:
        return json.load(f)
