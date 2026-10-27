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
        "kartf": ["kartari"], "karman": ["karmaRi"], "BAva": ["BAve"], "karaRa": ["karaRe", "karaRam"],
        "aDikaraRa": ["aDikaraRe"], "sampradAna": ["sampradAne"], "apAdAna": ["apAdAne"],
        # the meanings the kṛtya sūtras 3.1.103, 115, 116, 121, 125 name in their own words
        "svAmivESya": ["vESyayoH"], "nada": ["nade"], "nakzatra": ["nakzatre"], "patra": ["patre"], "AvaSyaka": ["AvaSyake"],
    },
    "kala": {"BUta": ["BUte"], "vartamAna": ["vartamAne"], "Bavizyat": ["Bavizyati"], "pUrvakAla": ["pUrvakAle"]},
    "kartrabhiprAya": {"kartraBiprAya": ["kartraBiprAye"]},
    # AMENDMENT 25 addendum (2026-10-24, owner: "update if as per the sūtra"): the kṛt families the Aṣṭādhyāyī itself sets side by side
    # as adhikāra-level choices — कृत्याः (3.1.95), ण्वुल्तृचौ (3.1.133) — and the kriyārthā sense of 3.3.10. The word is the sūtra's own.
    "krt": {"kftya": ["kftyAH"], "Rvultfc": ["tfcO"]},
    "kriyArTA": {"kriyArTA": ["kriyArTAyAm"]},
    # 3.2.124: śatṛ-śānac replace laṭ when the word agrees with a noun that is not in the first case (pacantaṃ caitram paśya)
    "samAnADikaraRa": {"apraTamA": ["apraTamAsamAnADikaraRe"]},
    # 3.2.125–133: the meanings that place śatṛ / śānac / śānan / cānaś in laṭ's stead (each word is the sūtra's own)
    "sambodhana": {"sambodhana": ["samboDane"]},
    "lakzaRahetu": {"lakzaRa": ["lakzaRahetvoH"], "hetu": ["lakzaRahetvoH"]},
    "tAcCIlyAdi": {"tAcCIlya": ["tAcCIlya"], "vayovacana": ["vayovacana"], "Sakti": ["Saktizu"]},
    "akfcCra": {"akfcCra": ["akfcCriRi"]}, "amitra": {"amitra": ["amitre"]},
    "yajYasaMyoga": {"yajYasaMyoga": ["yajYasaMyoge"]}, "praSaMsA": {"praSaMsA": ["praSaMsAyAm"]},
    # ashtadhyayi.com spells the 3.4.21 pada कर्त्तृ (samAnakarttfkayoH); 3.1.7 and 3.3.158 have one t
    "samAnakartfka": {"samAnakartfka": ["samAnakarttfkayoH", "samAnakartfkezu", "samAnakartfkAt"]},
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
