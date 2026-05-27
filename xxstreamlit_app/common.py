"""Shared path setup for Streamlit pages."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

GOLD_PATH = ROOT / "data" / "reference" / "subanta_gold" / "rama_pullinga.json"
HARI_GOLD_PATH = ROOT / "data" / "reference" / "subanta_gold" / "hari_pullinga.json"
SARVA_GOLD_PATH = ROOT / "data" / "reference" / "subanta_gold" / "sarva_pullinga.json"
JNANA_GOLD_PATH = ROOT / "data" / "reference" / "subanta_gold" / "jnana_napumsaka.json"
TAD_GOLD_PATH = ROOT / "data" / "reference" / "subanta_gold" / "tad_pullinga.json"


def load_rama_gold() -> dict:
    with open(GOLD_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_hari_gold() -> dict:
    with open(HARI_GOLD_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_sarva_gold() -> dict:
    with open(SARVA_GOLD_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_jnana_gold() -> dict:
    with open(JNANA_GOLD_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_tad_gold() -> dict:
    with open(TAD_GOLD_PATH, encoding="utf-8") as f:
        return json.load(f)
