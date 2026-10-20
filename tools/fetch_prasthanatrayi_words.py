"""
tools/fetch_prasthanatrayi_words.py — word-level analyses of the Prasthānatrayī + Śāṅkara-bhāṣya (CC BY 4.0).
────────────────────────────────────────────────────────────────────────────────────────────────────────────

Tamal Maharaj (RKMVERI), *A Word-Level Digital Reader of the Prasthānatrayī with
Śaṅkara's Bhāṣya*, Zenodo 10.5281/zenodo.21279193 (v1.0.0), arXiv:2607.07282.
Every mūla word carries ``{w: surface, p: padaccheda, g: grammar, m: English, c: h|m|l}``;
the bhāṣya is a surface-form dictionary of the same shape. The analyses were
drafted with LLM assistance under a verify + refute protocol and expert review —
in the /reader they are *hypotheses*: a word is ✓ only when the engine
re-derives it (Art. 17). Reference only (CONSTITUTION Art. 6).

    python3 -m tools.fetch_prasthanatrayi_words

The deposit is pinned by record id and SHA-256; JSON lands in
``data/reference/prasthanatrayi_words/raw/`` (gitignored — 35 MB).
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import io
import json
import urllib.request
import zipfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
OUT = _ROOT / "data" / "reference" / "prasthanatrayi_words"
RAW = OUT / "raw"
RECORD = "21279193"
URL = f"https://zenodo.org/api/records/{RECORD}/files/prasthanatrayi-zenodo-deposit.zip/content"
SHA256 = "e40cb46eecb51cca2e92ef6f68d7b19fde18d18421c0cc34a82356c28394aea5"
ATTRIBUTION = ("Word analyses: Tamal Maharaj, A Word-Level Digital Reader of the Prasthānatrayī with "
               "Śaṅkara's Bhāṣya (Zenodo 10.5281/zenodo.21279193, CC BY 4.0). Each ✓ is re-derived by the engine.")
KEEP = ("LICENSE", "ATTRIBUTIONS.md", "CITATION.cff", "README.md")


def main() -> int:
    with urllib.request.urlopen(URL, timeout=300) as r:
        blob = r.read()
    digest = hashlib.sha256(blob).hexdigest()
    if digest != SHA256:
        raise SystemExit(f"deposit SHA-256 {digest} ≠ pinned {SHA256}")
    RAW.mkdir(parents=True, exist_ok=True)
    files = {}
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        for name in z.namelist():
            base = name.rsplit("/", 1)[-1]
            if (name.startswith("data/") and base.endswith(".json")) or base in KEEP:
                (RAW / base).write_bytes(z.read(name))
                files[base] = z.getinfo(name).file_size
    (OUT / "SOURCE.json").write_text(json.dumps({
        "source": "Tamal Maharaj, A Word-Level Digital Reader of the Prasthānatrayī with Śaṅkara's Bhāṣya",
        "doi": "10.5281/zenodo.21279193", "paper": "arXiv:2607.07282", "version": "1.0.0",
        "license": "CC-BY-4.0", "url": URL, "sha256": SHA256,
        "kept": "data/*.json word analyses + licence files",
        "fetched": _dt.date.today().isoformat(), "files": files,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  {len(files)} files → {RAW}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
