"""
tools/fetch_dcs.py — Digital Corpus of Sanskrit (DCS) CoNLL-U chapters as test gold.
──────────────────────────────────────────────────────────────────────────────────────

Source #20 of the roster: DCS (Oliver Hellwig), github.com/OliverHellwig/sanskrit,
``dcs/data/conllu`` — every word sandhi-split and tagged with lemma, case /
gender / number or tense / mood / person / number; CC BY 4.0. It is
**reference only** (CONSTITUTION Art. 6): tools and tests read it, the rule
path never does. The tags are a hypothesis; the engine judges them
(``tools.dcs_reader``).

    python3 -m tools.fetch_dcs --list              # texts in the dump
    python3 -m tools.fetch_dcs                     # default kāvya + Āyurveda set
    python3 -m tools.fetch_dcs --text Meghadūta --text Raghuvaṃśa

Raw files land in data/reference/dcs/raw/ (gitignored, ≈1.1 GB for the whole
dump); ``SOURCE.json`` (committed) records the upstream commit and licence.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import shutil
import subprocess
import tempfile
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
OUT = _ROOT / "data" / "reference" / "dcs"
RAW = OUT / "raw"
REPO = "OliverHellwig/sanskrit"
FILES = "dcs/data/conllu/files/"
LOOKUP = "dcs/data/conllu/lookup/dictionary.csv"
LICENCE = "CC BY 4.0 — Oliver Hellwig: Digital Corpus of Sanskrit (DCS), 2010–2024"

KAVYA = ["Meghadūta", "Kumārasaṃbhava", "Kirātārjunīya", "Ṛtusaṃhāra", "Amaruśataka",
         "Śatakatraya", "Gītagovinda", "Buddhacarita", "Saundarānanda", "Hitopadeśa"]
AYURVEDA = ["Carakasaṃhitā", "Suśrutasaṃhitā", "Aṣṭāṅgahṛdayasaṃhitā"]
DEFAULT = KAVYA + AYURVEDA


def _nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def _get(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def tree() -> tuple[str, list[dict]]:
    """(commit sha, blobs) of the upstream repo — one API call."""
    t = json.loads(_get(f"https://api.github.com/repos/{REPO}/git/trees/master?recursive=1"))
    if t.get("truncated"):
        raise RuntimeError("GitHub tree listing truncated")
    return t["sha"], [b for b in t["tree"] if b["type"] == "blob"]


def _raw_url(sha: str, path: str) -> str:
    return f"https://raw.githubusercontent.com/{REPO}/{sha}/{urllib.parse.quote(path)}"


def texts(blobs: list[dict]) -> dict[str, list[dict]]:
    by: dict[str, list[dict]] = {}
    for b in blobs:
        if b["path"].startswith(FILES) and b["path"].endswith(".conllu"):
            by.setdefault(_nfc(b["path"][len(FILES):].split("/")[0]), []).append(b)
    return by


def _sparse_checkout(sha: str, paths: list[str], into: Path) -> bool:
    """Blob-less sparse clone of just ``paths`` — seconds, where raw.githubusercontent.com throttles thousands of files."""
    git = shutil.which("git")
    if not git:
        return False
    run = lambda *a: subprocess.run([git, *a], cwd=into, check=True, capture_output=True)  # noqa: E731
    try:
        subprocess.run([git, "clone", "-q", "--filter=blob:none", "--no-checkout",
                        f"https://github.com/{REPO}.git", str(into)], check=True, capture_output=True)
        run("sparse-checkout", "set", "--no-cone", *paths)
        run("checkout", "-q", sha)
    except subprocess.CalledProcessError:
        return False
    return True


def fetch(names: list[str]) -> dict:
    sha, blobs = tree()
    by = texts(blobs)
    names = [_nfc(n) for n in names]
    missing = [n for n in names if n not in by]
    if missing:
        raise SystemExit(f"not in the DCS dump: {', '.join(missing)} (see --list)")
    RAW.mkdir(parents=True, exist_ok=True)
    lookup = RAW / "dictionary.csv"
    todo = [n for n in names
            if any(not (RAW / n / _nfc(b["path"].rsplit("/", 1)[1])).is_file() for b in by[n])]
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "dcs"
        if (todo or not lookup.is_file()) and _sparse_checkout(sha, [FILES + n + "/" for n in todo] + [LOOKUP], repo):
            for n in todo:
                (RAW / n).mkdir(exist_ok=True)
                for f in (repo / FILES / n).glob("*.conllu"):
                    shutil.copyfile(f, RAW / n / _nfc(f.name))
            if not lookup.is_file():
                shutil.copyfile(repo / LOOKUP, lookup)
    if not lookup.is_file():
        lookup.write_bytes(_get(_raw_url(sha, LOOKUP)))
    stats = {}
    for n in names:
        d = RAW / n
        d.mkdir(exist_ok=True)
        for b in by[n]:  # per-file fallback (no git) and size check
            f = d / _nfc(b["path"].rsplit("/", 1)[1])
            if not f.is_file() or f.stat().st_size != b.get("size"):
                f.write_bytes(_get(_raw_url(sha, b["path"])))
        stats[n] = len(by[n])
        print(f"  {n}: {stats[n]} chapters")
    src = OUT / "SOURCE.json"
    prev = json.loads(src.read_text(encoding="utf-8")) if src.is_file() else {}
    (OUT / "SOURCE.json").write_text(json.dumps({
        "source": f"github.com/{REPO}/tree/{sha}/dcs/data/conllu",
        "licence": LICENCE,
        "commit": sha,
        "fetched": _dt.date.today().isoformat(),
        "texts": {**prev.get("texts", {}), **stats},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return stats


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="print the texts in the dump")
    ap.add_argument("--text", action="append", help="text name (repeatable); default kāvya + Āyurveda")
    a = ap.parse_args(argv)
    if a.list:
        _, blobs = tree()
        for n, bs in sorted(texts(blobs).items()):
            print(f"{n}\t{len(bs)} chapters\t{sum(b.get('size', 0) for b in bs) / 1e6:.1f} MB")
        return 0
    fetch(a.text or DEFAULT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
