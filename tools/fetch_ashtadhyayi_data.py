"""
tools/fetch_ashtadhyayi_data.py — pinned test/reference data from ashtadhyayi-com/data.

Data © ashtadhyayi.com (https://github.com/ashtadhyayi-com/data), used with
credit per its README. It is **reference only** — test gold (bench/) and real
examples for the teaching layer (core/, api/). The rule path never reads it
(tests/constitutional/test_no_reference_import_from_engine.py,
test_engine_is_rule_based.py).

    python3 -m tools.fetch_ashtadhyayi_data            # fetch at the pinned commit
    python3 -m tools.fetch_ashtadhyayi_data --sha <x>  # re-pin deliberately

Files land in data/reference/ashtadhyayi_com/ (gitignored: ~50 MB); the pinned
commit is recorded in data/reference/ashtadhyayi_com/SOURCE.json.
"""
from __future__ import annotations

import argparse
import json
import urllib.request
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
OUT = _ROOT / "data" / "reference" / "ashtadhyayi_com"
PINNED_SHA = "5744762f010d677cfb43f347a42d02796cf615d6"
FILES = (
    "dhatu/data.txt",                                # their dhātupāṭha (id → upadeśa)
    "dhatu/dhatuforms_vidyut_shuddha_kartari.txt",   # all roots × 10 lakāras, p/a
    "dhatu/dhatuforms_vidyut_shuddha_karmani.txt",   # all roots × 10 lakāras, karmaṇi
    "dhatu/dhatuprayogas.txt",                       # attested usages per form
    "shabda/data2.txt",                              # noun paradigms
    "shabda/shabdaprakriya.txt",                     # noun derivation paths (sūtras)
    "sutraani/sutra_prayogas.txt",                   # attested usages per sūtra
)


def fetch(sha: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for f in FILES:
        url = f"https://raw.githubusercontent.com/ashtadhyayi-com/data/{sha}/{f}"
        dest = OUT / f.replace("/", "__")
        with urllib.request.urlopen(url, timeout=120) as r:
            dest.write_bytes(r.read())
        print(f"  {dest.name}  {dest.stat().st_size:,} B")
    (OUT / "SOURCE.json").write_text(json.dumps({
        "repo": "https://github.com/ashtadhyayi-com/data", "commit": sha, "files": list(FILES),
        "credit": "Data © ashtadhyayi.com — used with credit per its README",
    }, indent=1) + "\n")


def path(name: str) -> Path:
    """Local path of a fetched file, e.g. path('dhatu/dhatuprayogas.txt')."""
    return OUT / name.replace("/", "__")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sha", default=PINNED_SHA)
    fetch(ap.parse_args(argv).sha)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
