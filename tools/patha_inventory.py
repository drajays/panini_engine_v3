"""tools/patha_inventory.py — what Pāṇini's own pāṭhas the engine holds as data, and how complete they are.

    python3 -m tools.patha_inventory        # writes sig/patha_inventory.json, prints one line per pāṭha

Read-only over data/inputs/*. Each row: pāṭha, file, entries, source note, and the traditional size it should be compared with
(``expected``: the figure the tradition gives; None where we do not assert one). The 'authority' design is docs/REFERENCE_PATHAS_AUTHORITY.md.
"""
from __future__ import annotations

import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_IN = _ROOT / "data" / "inputs"
OUT = _ROOT / "sig" / "patha_inventory.json"


def _load(name: str):
    p = _IN / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def _rows(d, *keys):
    """The list/dict of entries under the first key that exists (files differ in shape)."""
    if isinstance(d, list):
        return d
    for k in keys:
        if isinstance(d, dict) and k in d:
            return d[k]
    return []


def inventory() -> list[dict]:
    out: list[dict] = []

    def row(patha, file, entries, *, expected=None, note="", fields=None):
        out.append({"pATha": patha, "file": file, "entries": entries, "expected": expected, "note": note, "fields": fields or []})

    d = _load("dhatupatha_upadesha.json")
    es = _rows(d, "entries")
    row("DhAtupAWa", "dhatupatha_upadesha.json", len(es), expected=2000,
        note="tradition: ~2000 roots in 10 gaṇas (Kṣīrataraṅgiṇī / Mādhavīya count varies)", fields=sorted(es[0]) if es else [])

    d = _load("unadi_patha.json")
    es = _rows(d, "entries")
    row("uRAdi-sUtra", "unadi_patha.json", len(es), expected=748,
        note="loaded by tools/intake_patha.py from the brain (Siddhānta-kaumudī edition, 5 pādas: 157/123/160/238/70)")

    es = _rows(_load("dhatupatha_ganasutras.json"), "entries")
    row("dhAtupAWa gaRasUtra", "dhatupatha_ganasutras.json", len(es), expected=30, note="ghaṭādayo mitaḥ, svādayaḥ oditaḥ … (rows of the pāṭha that are not roots)")

    for f, label in (("ganapatha_full.json", "gaRapAWa (full)"),):
        d = _load(f)
        g = (d or {}).get("ganas", {})
        n = sum(len(v["members"]) for v in g.values())
        akrti = sum(1 for v in g.values() if v.get("akrti"))
        row(label, f, len(g), expected=None,
            note=f"{n} members in {len(g)} gaṇas; {akrti} flagged ākṛtigaṇa (open); {sum(1 for v in g.values() if not v.get('sutra'))} gaṇas with no sūtra link",
            fields=["members", "sutra", "akrti"])

    d = _load("ganapatha.json")
    g = d.get("ganas", d) if isinstance(d, dict) else {}
    row("gaRapAWa (legacy small)", "ganapatha.json", len(g), note="older, smaller file; superseded by ganapatha_full (duplicate to retire)")

    full = (_load("ganapatha_full.json") or {}).get("ganas", {})
    for f, label, key, gk in (("sarvadi_slp1.json", "sarvAdi", "sarvadi", "sarvAdiH"), ("tyadadi_slp1.json", "tyadAdi", "tyadadi", None),
                              ("ajadi_gana_slp1.json", "ajAdi", "members", "ajAdiH")):
        es = _rows(_load(f), key)
        in_full = len(full[gk]["members"]) if gk in full else None
        row(label, f, len(es), note=f"duplicate of ganapatha_full['{gk}'] ({in_full} members)" if gk else "no ganapatha_full counterpart; tyadādi is the first seven of sarvādi (1.1.27 gaṇa)")

    d = _load("linga_anushasana.json")
    row("liNgAnuSAsana", "linga_anushasana.json", sum(len(d[k]) for k in ("pulliṅga", "strīliṅga", "napuṃsaka")), note="STUB (14 stems); not Pāṇini's — Vyāḍi/Kātyāyana/Hemacandra tradition; a lexical, not rule, source")

    for f, label in (("krit_pratyaya.json", "kft-pratyaya list"), ("taddhita_pratyaya.json", "taddhita-pratyaya list"),
                     ("tin_upadesha.json", "tiN"), ("sup_upadesha.json", "sup")):
        d = _load(f)
        row(label, f, len([k for k in d if not k.startswith("_")]) if f.startswith("taddhita") else len(d.get("entries", d)) if isinstance(d, dict) else len(d or []),
            note="STUB: the pratyaya set is also taught by the sūtras themselves" if f.startswith("taddhita") else "")

    d = _load("subanta_lexicon.json")
    es = (d or {}).get("entries", [])
    row("lexicon (prAtipadika analyses)", "subanta_lexicon.json", len(es), note="NOT a Pāṇinian pāṭha: caller-side lexical facts; each entry carries `source`",
        fields=["stem", "linga", "components", "source"])
    return out


# ---- sūtra → list cross-reference ----------------------------------------------------------------------------------------------

BASELINE = _ROOT / "docs" / "data" / "patha_missing_baseline.json"
CLASSIFIED = _ROOT / "docs" / "data" / "patha_xref_classified.json"
STILL_MISSING = {"source-needed", "laukika-numerals", "open-akrti"}      # the rest of the classes are present / derived / in the sūtra / not a list
# lists a sūtra names that are not a gaṇa of the Gaṇapāṭha: (sūtra, list, data file or None, engine loader name)
EXPLICIT = [
    ("1.1.69", "akzarasamAmnAya (14 Siva-sUtras)", "maheshvara_sutras.json", "maheshvara_sutras"),
    ("1.1.71", "pratyAhAra table (from the 14 sUtras)", "maheshvara_sutras.json", "maheshvara_sutras"),
    ("1.3.1", "DAtupAWa (BUvAdi … curAdi)", "dhatupatha_upadesha.json", "dhatupatha_upadesha"),
    ("3.3.1", "uRAdi-sUtra", "unadi_patha.json", "unadi_patha"),
    ("1.1.23", "saMKyA words (eka … , bahu, gaRa, vatu, qati)", None, None),
    ("1.2.72", "tyadAdi", "tyadadi_slp1.json", "tyadadi_slp1"),
    ("4.1.2", "sup (21 pratyayas)", "sup_upadesha.json", "sup_upadesha"),
    ("3.4.78", "tiN (18 pratyayas)", "tin_upadesha.json", "tin_upadesha"),
    ("3.1.91", "kft pratyayas", "krit_pratyaya.json", "krit_pratyaya"),
    ("3.4.77", "lakAra list", "lakara_metadata.json", "lakara_metadata"),
]
# words with Adi that name no list ("tasmAdi", "AdirantyEna" …)
_NOT_LIST = {"tasmAdi", "tasyAdi", "Adi", "AdirantyEna", "AdirYiwuqavaH", "anyAdi", "vfdDiryasyAcAmAdi", "AdiH", "sarvAdi"}


_POSITIONAL = ("halAdi", "saMyogAdi", "antAdi", "uttarapadAdi", "tftIyAdi", "parAdi", "yaRAdi", "nityAdi", "aByastAnAmAdi", "sAvekAcastftIyAdi", "pUrvAdini", "AdyudAtta")
_DHATU_GANA = ("juhotyAdi", "divAdi", "tudAdi", "ruDAdi", "tanAdi", "kryAdi", "rudAdi", "curAdi", "BvAdi", "adAdi", "svAdi")
_DHATU_SUB = ("puzAdi", "dyutAdi", "kuwAdi")


def _code_text() -> str:
    parts = []
    for d in ("engine", "sutras", "pipelines", "core", "tools"):
        for f in (_ROOT / d).rglob("*.py"):
            if f.name != "patha_inventory.py" and not f.name.startswith("build_"):
                parts.append(f.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def _sutra_file(sid: str) -> Path:
    a, p, n = sid.split(".")
    return _ROOT / "sutras" / f"adhyaya_{a}" / f"pada_{p}" / f"sutra_{a}_{p}_{n}.py"


def _count(d) -> int:
    if isinstance(d, dict):
        n = len(d.get("entries") or d.get("members") or [])
        return n or sum(len(v) for v in d.values() if isinstance(v, list)) or len([k for k in d if not k.startswith("_")])
    return len(d or [])


def xref() -> list[dict]:
    """sūtra → list → data file → engine loader → status (present-wired / present-unused / missing)."""
    import re
    import sys

    sys.path.insert(0, str(_ROOT))
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY

    code = _code_text()
    full = (_load("ganapatha_full.json") or {}).get("ganas", {})
    rows: list[dict] = []
    for name, g in sorted(full.items(), key=lambda kv: tuple(int(x) for x in kv[1]["sutra"].split("."))):
        f = _sutra_file(g["sutra"])
        src = f.read_text(encoding="utf-8") if f.exists() else ""
        wired = name in src or "gana" in src or f'"{name}"' in code
        has = g["members"] or g.get("members_restricted") or g.get("derived")      # pāraskarādi: notes only; vargyādi: derived from digādi
        status = "missing" if not has else "present-wired" if wired else "present-unused"
        rows.append({"sutra": g["sutra"], "list": name, "kind": "gaRa", "file": "ganapatha_full.json", "loader": "engine.gana", "status": status})
    for sid, lst, file, loader in EXPLICIT:
        n = _count(_load(file)) if file else 0
        status = "missing" if not n else "present-wired" if loader in code else "present-unused"
        rows.append({"sutra": sid, "list": lst, "kind": "in-sutra/pATha", "file": file, "loader": loader, "status": status})
    # sūtras that name an "-Adi" list for which the Gaṇapāṭha holds no gaṇa (heuristic on the sūtra's own words)
    have = {g["sutra"] for g in full.values()} | {r[0] for r in EXPLICIT}
    for sid, r in SUTRA_REGISTRY.items():
        if sid in have:
            continue
        for w in re.findall(r"[A-Za-z]+", r.text_slp1 or ""):
            m = re.match(r"^([A-Za-z]{3,}?)(Adi\w*|Adayo|Adaya\w*)$", w)
            if not m or w in _NOT_LIST or m.group(1) + "Adi" in _NOT_LIST or any(w.startswith(p) for p in _POSITIONAL):
                continue
            if any(k in w for k in _DHATU_SUB):        # a sub-list of the dhātupāṭha that its file does not mark (no per-entry field)
                rows.append({"sutra": sid, "list": w, "kind": "dhAtu-sub-gaRa", "file": "dhatupatha_upadesha.json", "loader": "dhatupatha_upadesha", "status": "missing"})
            elif any(k in w for k in _DHATU_GANA):     # one of the ten gaṇas: the gana field of the dhātupāṭha
                rows.append({"sutra": sid, "list": w, "kind": "dhAtu-gaRa", "file": "dhatupatha_upadesha.json", "loader": "dhatupatha_upadesha", "status": "present-wired"})
            else:
                rows.append({"sutra": sid, "list": w, "kind": "gaRa-name-in-sutra (heuristic)", "file": None, "loader": None, "status": "missing"})
    # decisions on what the heuristic first reported missing (hand-judged with the Kāśikā evidence): only these classes stay missing
    cls = json.loads(CLASSIFIED.read_text(encoding="utf-8"))["entries"] if CLASSIFIED.exists() else {}
    for r in rows:
        c = cls.get(f"{r['sutra']}|{r['list']}")
        if r["status"] == "missing" and c and c["class"] not in STILL_MISSING:
            r["status"], r["why"] = f"classified-{c['class']}", c["why"]
    return rows


def missing() -> set[str]:
    return {f"{r['sutra']}|{r['list']}" for r in xref() if r["status"] == "missing"}


def main() -> int:
    import collections

    rows = inventory()
    x = xref()
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({"rows": rows, "xref": x}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("xref:", dict(collections.Counter(r["status"] for r in x)))
    for r in rows:
        print(f"{r['pATha']:34} {r['entries']:>6}  expected={r['expected']}  {r['note']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
