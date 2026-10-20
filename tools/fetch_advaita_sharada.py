"""
tools/fetch_advaita_sharada.py — Advaita Sharada (Sringeri) Prasthānatrayī bhāṣyas for the /reader page.
───────────────────────────────────────────────────────────────────────────────────────────────────────

advaitasharada.sringeri.net is the Dakshinamnaya Sri Sharada Peetham's digital
edition of the Śāṅkara-granthāvalī. It is a static site: every page of a work is
prerendered at ``/read/<slug>/<chunk>/`` and every passage carries a stable id

    IS_C01_V01         mūla (verse / mantra / sūtra)   <div class="unit verse">
    IS_C01_V01_B01     its bhāṣya                       <p class="unit prose kind-bhashya">
    IS_C01_V02_I01     avatārikā before the next mūla   <p class="unit prose kind-avatarika">

A ṭīkā is aligned to those ids by ``/vyakhya/<slug>/<chunk>.<code>.json``
(``{"IS_C01_V01_B01": [{"id": "AIS_C01_Q0012", "html": …, "lemma": …}]}``),
the same file the site's own "व्याख्याः" button loads.

**Rights.** The site states "© Dakshinamnaya Sri Sharada Peetham, Sringeri. All
rights reserved." The download is therefore a *local* reading cache: it lands in
``data/reference/advaita_sharada/raw/`` (gitignored), is never committed, and the
reader links every passage back to its page. Only ``SOURCE.json`` (provenance,
no text) is tracked. Reference only (CONSTITUTION Art. 6).

    python3 -m tools.fetch_advaita_sharada            # fetch (cached) + build
    python3 -m tools.fetch_advaita_sharada --no-fetch # rebuild from raw/html only
    python3 -m tools.fetch_advaita_sharada --work isha-bhashya
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import html as _html
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
OUT = _ROOT / "data" / "reference" / "advaita_sharada"
RAW = OUT / "raw"
HTML = RAW / "html"
BASE = "https://advaitasharada.sringeri.net"
UA = "panini-engine-v3 reader cache (local, non-redistributed; contact via online@sringeri.net feedback)"
GROUP = "prasthanatraya-bhashya"
RIGHTS = "© Dakshinamnaya Sri Sharada Peetham, Sringeri. All rights reserved."
DELAY = 1.0


def _get(path: str) -> bytes:
    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def _cached(path: str, dest: Path, refresh: bool = False) -> bytes | None:
    """Fetch once, then read from disk; None on 404 (a ṭīkā absent for this chunk)."""
    if dest.is_file() and not refresh:
        return dest.read_bytes()
    try:
        body = _get(path)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(body)
    time.sleep(DELAY)
    return body


def works(refresh: bool = False) -> dict[str, dict]:
    """``{code: {slug, title, group, chunk1}}`` from the site's cite-map index."""
    body = _cached("/cite-maps/index.json", RAW / "cite-maps-index.json", refresh)
    return json.loads(body)


def chunks(slug: str, refresh: bool = False) -> list[str]:
    body = _cached("/sitemap-0.xml", RAW / "sitemap-0.xml", refresh).decode("utf-8")
    found = re.findall(rf"{re.escape(BASE)}/read/{re.escape(slug)}/([^/<]+)/?</loc>", body)
    return sorted(set(found), key=_num_key)


def _num_key(s: str) -> tuple:
    return tuple(int(x) for x in re.findall(r"\d+", s)) or (0,)


# ── HTML → passages ────────────────────────────────────────────────────────

_UNIT = re.compile(r'<(p|div) class="(unit [^"]*|chapter-head[^"]*|[a-z-]*-head[^"]*)" id="([^"]+)"[^>]*>(.*?)</\1>', re.S)
_CHIP = re.compile(r'<button class="vy-chip[^"]*" data-vy="([^"]+)" data-slug="([^"]+)" data-title="([^"]+)"')
_PRATIKA = re.compile(r'<span class="pratika[^"]*">(.*?)</span>', re.S)
_ULLEKHA_A = re.compile(r'<a class="ullekha" href="([^"]+)"[^>]*>(.*?)</a>', re.S)
_ULLEKHA_S = re.compile(r'<span class="ullekha is-[a-z]+"[^>]*>(.*?)</span>(?:<span class="ullekha-ref">\((.*?)\)</span>)?', re.S)


def text_of(fragment: str) -> str:
    """Plain Devanāgarī: <br> → newline, tags dropped, soft hyphens (compound break hints) removed."""
    s = re.sub(r"<br\s*/?>", "\n", fragment)
    s = re.sub(r"<[^>]+>", "", s)
    s = _html.unescape(s).replace("\u00ad", "")
    return "\n".join(line.strip() for line in s.split("\n")).strip()


def _citations(fragment: str) -> list[dict]:
    out = []
    for href, t in _ULLEKHA_A.findall(fragment):
        target = _html.unescape(href)
        out.append({"text": text_of(t), "href": target, "anchor": target.rsplit("#", 1)[-1] if "#" in target else None})
    for t, ref in _ULLEKHA_S.findall(fragment):
        out.append({"text": text_of(t), "ref": text_of(ref) if ref else None})
    return out


def _kind(cls: str) -> str:
    if "verse" in cls.split():
        return "mula"
    m = re.search(r"kind-(\w+)", cls)
    if m:
        return m.group(1)
    if "colophon" in cls:
        return "colophon"
    return "heading"


def parse_page(html_text: str) -> dict:
    main = html_text[html_text.find("<main"):html_text.find("</main>")]
    main = re.sub(r" data-astro-cid-\w+", "", main)
    head = re.search(r'<main[^>]*data-work="([^"]+)"[^>]*data-chunk="([^"]+)"[^>]*data-worktitle="([^"]+)"', main)
    units = []
    for _tag, cls, uid, body in _UNIT.findall(main):
        kind = _kind(cls)
        u = {"id": uid, "kind": kind}
        if kind == "mula":
            vt = re.search(r'<p class="verse-text">(.*?)</p>', body, re.S)
            vn = re.search(r'<span class="verse-no">(.*?)</span>', body, re.S)
            uv = re.search(r'<span class="uvaca">(.*?)</span>', body, re.S)
            u["text"] = text_of(vt.group(1) if vt else body)
            u["verse_no"] = text_of(vn.group(1)) if vn else None
            if uv:
                u["uvaca"] = text_of(uv.group(1))
        else:
            u["text"] = text_of(body)
        cites = _citations(body)
        if cites:
            u["citations"] = cites
        units.append(u)
    return {
        "work": head.group(1) if head else None,
        "chunk": head.group(2) if head else None,
        "title": _html.unescape(head.group(3)) if head else None,
        "vyakhya": [{"code": c, "slug": s, "title": _html.unescape(t)} for c, s, t in _CHIP.findall(main)],
        "units": units,
    }


def parse_vyakhya(body: bytes) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for anchor, rows in json.loads(body).items():
        out[anchor] = []
        for r in rows:
            h = r.get("html") or ""
            row = {"id": r["id"], "chunk": r.get("chunk"), "text": text_of(h),
                   "pratika": [text_of(p) for p in _PRATIKA.findall(h)]}
            if r.get("lemma"):
                row["lemma"] = text_of(r["lemma"])
            out[anchor].append(row)
    return out


# ── fetch + build ─────────────────────────────────────────────────────────

def build_work(code: str, meta: dict, fetch: bool = True, refresh: bool = False) -> dict:
    slug = meta["slug"]
    pages = []
    for ch in chunks(slug, refresh=False):
        dest = HTML / slug / f"{ch}.html"
        body = _cached(f"/read/{slug}/{ch}/", dest, refresh) if fetch else (dest.read_bytes() if dest.is_file() else None)
        if body is None:
            continue
        page = parse_page(body.decode("utf-8"))
        page["url"] = f"{BASE}/read/{slug}/{ch}"
        for vy in page["vyakhya"]:
            vdest = HTML / slug / f"{ch}.{vy['code']}.json"
            vbody = _cached(f"/vyakhya/{slug}/{ch}.{vy['code']}.json", vdest, refresh) if fetch else (
                vdest.read_bytes() if vdest.is_file() else None)
            vy["aligned"] = parse_vyakhya(vbody) if vbody else {}
        pages.append(page)
        print(f"  {slug}/{ch}: {len(page['units'])} units, ṭīkā {[v['code'] for v in page['vyakhya']]}")
    doc = {"code": code, "slug": slug, "title": meta.get("title"), "group": meta.get("group"),
           "source": BASE, "rights": RIGHTS, "pages": pages}
    (RAW / f"{slug}.json").write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    return doc


def write_source(stats: dict) -> None:
    (OUT / "SOURCE.json").write_text(json.dumps({
        "source": "Advaita Sharada — Dakshinamnaya Sri Sharada Peetham, Sringeri",
        "url": BASE,
        "rights": RIGHTS,
        "policy": "local reading cache only: raw/ is gitignored, never committed or served publicly; "
                  "every passage links back to its page on the site",
        "pages": BASE + "/read/<slug>/<chunk>/",
        "tika_alignment": BASE + "/vyakhya/<slug>/<chunk>.<code>.json",
        "group": GROUP,
        "fetched": _dt.date.today().isoformat(),
        "stats": stats,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", help="one slug (default: every Prasthānatrayī bhāṣya)")
    ap.add_argument("--no-fetch", action="store_true", help="rebuild from raw/html only")
    ap.add_argument("--refresh", action="store_true", help="re-download pages already cached")
    a = ap.parse_args(argv)

    RAW.mkdir(parents=True, exist_ok=True)
    idx = works()
    todo = {c: m for c, m in idx.items() if m.get("group") == GROUP and (not a.work or m["slug"] == a.work)}
    stats = {}
    for code, meta in todo.items():
        doc = build_work(code, meta, fetch=not a.no_fetch, refresh=a.refresh)
        units = [u for p in doc["pages"] for u in p["units"]]
        tika = sum(len(rows) for p in doc["pages"] for v in p["vyakhya"] for rows in v["aligned"].values())
        stats[meta["slug"]] = {"pages": len(doc["pages"]), "mula": sum(u["kind"] == "mula" for u in units),
                               "passages": len(units), "tika_passages": tika,
                               "sha256": hashlib.sha256((RAW / f"{meta['slug']}.json").read_bytes()).hexdigest()}
    if not a.work:
        write_source(stats)
    print(json.dumps({k: {x: y for x, y in v.items() if x != "sha256"} for k, v in stats.items()}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
