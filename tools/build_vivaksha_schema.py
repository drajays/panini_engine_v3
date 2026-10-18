"""tools/build_vivaksha_schema.py — AMENDMENT 25: the closed vivakṣā vocabulary, taken from the Aṣṭādhyāyī's own words.

    python3 -m tools.build_vivaksha_schema        # writes data/inputs/vivaksha_schema.json

A value is admitted only if one of its word forms occurs as a word of some sūtra's samagra text (ashtadhyayi.com,
Art. 4); the file lists those sūtras as its citation. Nothing is invented: a value with no occurrence is refused.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))
OUT = _ROOT / "data" / "inputs" / "vivaksha_schema.json"

# key -> value (SLP1 stem) -> the inflected forms in which Pāṇini states that meaning in a sūtra
VOCABULARY = {
    "artha": {
        "kartf": ["kartari"], "karman": ["karmaRi"], "BAva": ["BAve"], "karaRa": ["karaRe"],
        "aDikaraRa": ["aDikaraRe"], "sampradAna": ["sampradAne"], "apAdAna": ["apAdAne"],
    },
    "kala": {"BUta": ["BUte"], "vartamAna": ["vartamAne"], "Bavizyat": ["Bavizyati"]},
    "kartrabhiprAya": {"kartraBiprAya": ["kartraBiprAye"]},
}
_SPLIT = re.compile(r"[\s\-,.;:|।॥()'\"]+")


def build() -> dict:
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY

    words = {sid: set(_SPLIT.split(getattr(rec, "samagra_slp1", "") or "")) for sid, rec in SUTRA_REGISTRY.items()}
    order = lambda s: tuple(map(int, s.split(".")))
    schema: dict = {"_doc": __doc__.strip().splitlines()[0], "source": "samagra_slp1 of the sūtra records (ashtadhyayi.com)",
                    "keys": {}}
    for key, values in VOCABULARY.items():
        schema["keys"][key] = {}
        for value, forms in values.items():
            cited = sorted((sid for sid, w in words.items() if w & set(forms)), key=order)
            if not cited:
                raise SystemExit(f"{key}={value}: none of {forms} occurs in any samagra — refused")
            schema["keys"][key][value] = {"forms": forms, "sutras": cited}
    return schema


def main() -> int:
    schema = build()
    OUT.write_text(json.dumps(schema, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for key, values in schema["keys"].items():
        print(key, {v: len(d["sutras"]) for v, d in values.items()})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
