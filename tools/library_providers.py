"""
tools/library_providers.py — one catalogue of the Sanskrit literature the engine holds, for clients.
─────────────────────────────────────────────────────────────────────────────────────────────────────

Subhastini is the reading front door (docs/INTEGRATION_CLIENTS.md); it reads these texts live over
``/v1/library`` and copies none of them. Each source is a *provider* with the same four calls:

    works()                         → [work]
    sections(slug)                  → [{id, label}]
    section(slug, sec)              → {label, items: [item without commentary bodies]}
    item(slug, sec, item_id)        → item with passages + commentaries

    work  {id "<provider>:<slug>", provider, title, author, group, group_label, rights, local_only,
           source_url, has_words}
    item  {id, ref, kind, text, commentary_titles, passages?, commentaries?, links?}

A new source is a new provider class appended to ``PROVIDERS``. Providers:

* ``as``  — Advaita Sharada (Sringeri), local cache only ("All rights reserved"): local_only = True.
* ``scl`` — Saṃsādhanī e-readers (UoH, GPL-2.0), with engine-verified word analysis in /reader.
* ``ac``  — ashtadhyayi.com data (credit ashtadhyayi.com): Aṣṭādhyāyī with its vṛttis, the
  Kaumudīs, Mahābhāṣya, Vākyapadīya, Paribhāṣenduśekhara, Bhūṣaṇasāra, Mañjūṣā, Tarkasaṅgraha …
  read from ``$PANINI_DATA_MASTER`` (default ``~/data-master``).

Tools layer (CONSTITUTION Art. 6): reference text for reading; never an engine input.
"""
from __future__ import annotations

import json
import os
import re
from functools import lru_cache
from pathlib import Path

READER = os.environ.get("PANINI_READER_URL", "http://127.0.0.1:5050/reader")


def clean(s) -> str:
    """ashtadhyayi.com markup → plain text: ``[[1.1.1]]`` → (1.1.1), ``<<…>>`` → «…», tags dropped."""
    s = str(s or "")
    s = re.sub(r"\[\[([\d.]+)\]\]", r"(\1)", s)
    s = s.replace("<<", "«").replace(">>", "»")
    s = re.sub(r"<[^<>]+>", "", s)
    return s.strip()


def _num_key(s: str) -> tuple:
    return tuple(int(x) for x in re.findall(r"\d+", str(s))) or (0,)


# ── Advaita Sharada ────────────────────────────────────────────────────────

class AdvaitaSharada:
    id = "as"
    rights = "© Dakshinamnaya Sri Sharada Peetham, Sringeri. All rights reserved. Local reading copy."

    def _ar(self):
        from tools import advaita_sharada_reader as ar
        return ar

    def works(self) -> list[dict]:
        ar = self._ar()
        return [{"id": u["id"], "provider": self.id, "slug": u["id"][len(ar.PREFIX):], "title": u["book"],
                 "author": None, "group": u["group"], "group_label": u["group_label"], "rights": self.rights,
                 "local_only": True, "source_url": "https://advaitasharada.sringeri.net/", "has_words": u["words"]}
                for u in ar.catalogue()]

    def sections(self, slug: str) -> list[dict]:
        doc = self._ar()._doc(slug)
        out = []
        for p in doc["pages"]:
            head = next((u["text"] for u in p["units"] if u["kind"] == "heading"), "")
            out.append({"id": p["chunk"], "label": head or p["chunk"]})
        return out

    @staticmethod
    def _tika(p: dict, full: bool) -> list[dict]:
        return [{"source": t["code"], "title": t["title"], "count": len(t["rows"]),
                 **({"rows": [{"text": r["text"], "pratika": r["pratika"]} for r in t["rows"]]} if full else {})}
                for t in p.get("tika", [])]

    def section(self, slug: str, sec: str) -> dict:
        ar = self._ar()
        items = []
        for v in ar._verses(slug, sec):
            ps = [*v["pre"], v["mula"], *v["post"]]
            items.append({"id": v["id"], "ref": v["ref"], "kind": v["mula"]["kind"], "text": v["mula"]["text"],
                          "commentary_titles": sorted({t["title"] for p in ps for t in p.get("tika", [])}),
                          "passage_kinds": [p["kind"] for p in ps if p["id"] != v["id"]]})
        return {"label": next((s["label"] for s in self.sections(slug) if s["id"] == sec), sec), "items": items}

    def item(self, slug: str, sec: str, item_id: str) -> dict:
        ar = self._ar()
        v = next((x for x in ar._verses(slug, sec) if x["id"] == item_id), None)
        if v is None:
            raise KeyError(item_id)
        page = next(p for p in ar._doc(slug)["pages"] if p["chunk"] == sec)
        passages = [{"id": p["id"], "kind": p["kind"], "position": pos, "text": p["text"],
                     "commentaries": self._tika(p, True)}
                    for pos, group in (("before", v["pre"]), ("after", v["post"])) for p in group]
        links = {"source": f"{page['url']}#{item_id}"}
        if slug in ar.WORDS_KEY:
            links["analysis"] = f"{READER}#{ar.PREFIX}{slug}/{sec}/{item_id}"
        return {"id": v["id"], "ref": v["ref"], "kind": v["mula"]["kind"], "text": v["mula"]["text"],
                "passages": passages, "commentaries": self._tika(v["mula"], True), "links": links}

    def search(self, q: str, limit: int) -> list[dict]:
        ar, hits = self._ar(), []
        for w in self.works():
            for h in ar.search(w["id"], q, limit=limit - len(hits)):
                hits.append({"work": w["id"], "title": w["title"], "section": h["chapter"], "item": h["sloka"],
                             "ref": h["ref"], "kind": h["kind"], "snippet": h["word"]})
            if len(hits) >= limit:
                break
        return hits


# ── Saṃsādhanī e-readers ──────────────────────────────────────────────────

class Samsaadhanii:
    id = "scl"
    rights = "Saṃsādhanī e-readers, University of Hyderabad (GPL-2.0); word analyses re-derived by the engine."

    def _rd(self):
        from tools import samsaadhanii_reader as rd
        return rd

    def works(self) -> list[dict]:
        return [{"id": f"{self.id}:{u['id']}", "provider": self.id, "slug": u["id"], "title": u["label"],
                 "author": None, "group": "samsaadhanii", "group_label": "संसाधनी — पद-विश्लेषणम्",
                 "rights": self.rights, "local_only": False,
                 "source_url": "http://ereaders.samsaadhanii.in/books/ereaders/", "has_words": True}
                for u in self._rd().catalogue()]

    def sections(self, slug: str) -> list[dict]:
        return [{"id": c, "label": c} for c in self._rd().chapters(slug)]

    def section(self, slug: str, sec: str) -> dict:
        items = [{"id": v["sloka"], "ref": f"{sec}.{v['sloka']}", "kind": "mula", "text": "\n".join(v["text"]),
                  "commentary_titles": []} for v in self._rd().verses(slug, sec)]
        return {"label": sec, "items": items}

    def item(self, slug: str, sec: str, item_id: str) -> dict:
        v = next((x for x in self._rd().verses(slug, sec) if x["sloka"] == item_id), None)
        if v is None:
            raise KeyError(item_id)
        return {"id": item_id, "ref": f"{sec}.{item_id}", "kind": "mula", "text": "\n".join(v["text"]),
                "passages": [], "commentaries": [], "links": {"analysis": f"{READER}#{slug}/{sec}/{item_id}"}}

    def search(self, q: str, limit: int) -> list[dict]:
        hits = []
        for w in self.works():
            for h in self._rd().search(w["slug"], q, limit=limit - len(hits)):
                hits.append({"work": w["id"], "title": w["title"], "section": h["chapter"], "item": h["sloka"],
                             "ref": f"{h['chapter']}.{h['sloka']}", "kind": "mula", "snippet": h.get("word") or ""})
            if len(hits) >= limit:
                break
        return hits


# ── ashtadhyayi.com data ──────────────────────────────────────────────────

DATA_MASTER = Path(os.environ.get("PANINI_DATA_MASTER", Path.home() / "data-master"))

# Commentaries keyed by sūtra id (``11001`` = 1.1.1), in the order a reader meets them.
SUTRA_VRTTIS = [
    ("vartika", "वार्तिकानि"), ("kashika", "काशिकावृत्तिः"), ("nyaas", "न्यासः"), ("padamanjari", "पदमञ्जरी"),
    ("bhashya", "महाभाष्यम्"), ("kaumudi", "सिद्धान्तकौमुदी"), ("balamanorama", "बालमनोरमा"),
    ("tattvabodhini", "तत्त्वबोधिनी"), ("praudhamanorama", "प्रौढमनोरमा"), ("sudha", "सुधा"),
    ("laghushabdendushekhar", "लघुशब्देन्दुशेखरः"), ("laghukaumudi", "लघुसिद्धान्तकौमुदी"), ("sarala", "सरला"),
    ("prakriyasarvasvam", "प्रक्रियासर्वस्वम्"), ("sutrartha", "सूत्रार्थः"), ("vasu_english", "Vasu (1891), English"),
]
_DIGITS = str.maketrans("0123456789", "०१२३४५६७८९")


def _dev(n) -> str:
    return str(n).translate(_DIGITS)


@lru_cache(maxsize=48)
def _json(rel: str):
    return json.loads((DATA_MASTER / rel).read_text(encoding="utf-8"))


def _rows(rel: str) -> list[dict]:
    d = _json(rel)
    return d["data"] if isinstance(d, dict) and "data" in d else d


@lru_cache(maxsize=1)
def _sutras() -> list[dict]:
    return _rows("sutraani/data.txt")


@lru_cache(maxsize=1)
def _vartikas() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for r in _rows("sutraani/vartika.txt"):
        out.setdefault(r["sutra"], []).append(clean(r["vartika"]))
    return out


def _vrtti(key: str, sid: str) -> str:
    """One commentary on one sūtra (``sid`` like ``1.1.1``); '' when the commentary is silent."""
    if key == "vartika":
        return "\n".join(_vartikas().get(sid, []))
    path = DATA_MASTER / "sutraani" / f"{key}.txt"
    if not path.is_file():
        return ""
    v = _json(f"sutraani/{key}.txt").get("".join(f"{int(x):0{w}d}" for x, w in zip(sid.split("."), (1, 1, 3))), "")
    if isinstance(v, dict):
        v = "\n\n".join(clean(x) for x in v.values() if isinstance(x, str) and x.strip())
    return clean(v)


class _Work:
    """A grantha read from one ashtadhyayi.com file: ``rows`` → sections → items."""

    def __init__(self, slug, title, author, files, group="vyakarana"):
        self.slug, self.title, self.author, self.files, self.group = slug, title, author, files, group

    def available(self) -> bool:
        return all((DATA_MASTER / f).is_file() for f in self.files)

    def sections(self) -> list[dict]:
        raise NotImplementedError

    def items(self, sec: str) -> list[dict]:
        raise NotImplementedError


class _Sutrapatha(_Work):
    """Aṣṭādhyāyī in pāṇinīya order (sections = pāda) or a kaumudī order (sections = its chapter numbers)."""

    def __init__(self, slug, title, author, order=None, chapter=None, main=None):
        super().__init__(slug, title, author, ["sutraani/data.txt"])
        self.order, self.chapter, self.main = order, chapter, main

    def _rows(self):
        rows = _sutras()
        if self.order:
            rows = sorted((r for r in rows if r.get(self.order, "").isdigit() and int(r[self.order]) > 0),
                          key=lambda r: int(r[self.order]))
        return rows

    def _sec(self, r) -> str:
        return r[self.chapter] if self.chapter else f"{r['a']}.{r['p']}"

    def sections(self) -> list[dict]:
        seen = []
        for r in self._rows():
            s = self._sec(r)
            if s not in seen:
                seen.append(s)
        label = (lambda s: f"अध्यायः {_dev(s.split('.')[0])} पादः {_dev(s.split('.')[1])}") if not self.chapter \
            else (lambda s: f"भागः {_dev(s)}")
        return [{"id": s, "label": label(s)} for s in seen]

    def items(self, sec: str, full: bool = False) -> list[dict]:
        out = []
        for r in self._rows():
            if self._sec(r) != sec:
                continue
            sid = f"{r['a']}.{r['p']}.{r['n']}"
            text = r["s"] + (f"\n{_vrtti(self.main, sid)}" if self.main else "")
            item = {"id": sid, "ref": f"{sid}" + (f" · {self.order.upper()} {r[self.order]}" if self.order else ""),
                    "kind": "sutra", "text": text.strip()}
            vrttis = [(k, t) for k, t in SUTRA_VRTTIS if k != self.main]
            if full:
                item["commentaries"] = [{"source": k, "title": t, "text": c} for k, t in vrttis
                                        if (c := _vrtti(k, sid))]
                item["passages"] = []
                item["links"] = {"source": f"https://ashtadhyayi.com/sutraani/{r['a']}/{r['p']}/{r['n']}"}
            else:
                item["commentary_titles"] = [t for k, t in vrttis if _vrtti(k, sid)]
            out.append(item)
        return out


class _Rows(_Work):
    """A grantha whose file is a list of records; ``fields`` maps record keys to the item."""

    def __init__(self, slug, title, author, file, text, sec=None, sec_label=None, ref=None, before=(), after=(),
                 commentary_files=()):
        super().__init__(slug, title, author, [file])
        self.file, self.text, self.sec, self.sec_label, self.ref = file, text, sec, sec_label, ref
        self.before, self.after, self.commentary_files = before, after, commentary_files

    def _records(self) -> list[dict]:
        return _rows(self.file)

    def _sec_of(self, r) -> str:
        return str(r.get(self.sec) or "") if self.sec else "1"

    def sections(self) -> list[dict]:
        out: dict[str, str] = {}
        for r in self._records():
            s = self._sec_of(r)
            if s not in out:
                out[s] = clean(r.get(self.sec_label)) if self.sec_label and r.get(self.sec_label) else (s or "—")
        return [{"id": s, "label": lab} for s, lab in out.items()]

    def items(self, sec: str, full: bool = False) -> list[dict]:
        out = []
        for i, r in enumerate(self._records(), 1):
            if self._sec_of(r) != sec:
                continue
            ref = clean(r.get(self.ref)) if self.ref and r.get(self.ref) not in (None, "") else str(i)
            item = {"id": str(i), "ref": ref, "kind": "mula", "text": clean(r.get(self.text))}
            comms = [{"source": k, "title": t, "text": clean(r.get(k))} for k, t in self.after if clean(r.get(k))]
            for path, key_of, title in self.commentary_files:
                c = clean(_rows(path).get(key_of(r), "")) if (DATA_MASTER / path).is_file() else ""
                if c:
                    comms.append({"source": path, "title": title, "text": c})
            pre = [{"id": f"{i}.{k}", "kind": "avatarika", "position": "before", "text": clean(r.get(k)),
                    "commentaries": []} for k, _t in self.before if clean(r.get(k))]
            if full:
                item.update(passages=pre, commentaries=comms, links={})
            else:
                item["commentary_titles"] = [c["title"] for c in comms]
            out.append(item)
        return out


class _Mahabhashya(_Work):
    """Mahābhāṣya by āhnika file, each chunk with Pradīpa and Uddyota."""

    def __init__(self):
        super().__init__("mahabhashya", "महाभाष्यम्", "पतञ्जलिः", ["mahabhashyam/1.txt"])

    def _files(self):
        return sorted((DATA_MASTER / "mahabhashyam").glob("*.txt"), key=lambda p: _num_key(p.stem))

    def sections(self) -> list[dict]:
        return [{"id": p.stem, "label": _json(f"mahabhashyam/{p.name}").get("ahnika_name", p.stem)}
                for p in self._files()]

    def items(self, sec: str, full: bool = False) -> list[dict]:
        out = []
        for r in _rows(f"mahabhashyam/{sec}.txt"):
            comms = [{"source": k, "title": t, "text": clean(r.get(k))}
                     for k, t in (("pradeep", "प्रदीपः (कैयटः)"), ("uddyot", "उद्द्योतः (नागेशः)")) if clean(r.get(k))]
            item = {"id": str(r["chunk_id"]), "ref": f"{clean(r.get('adhikarana_name'))} · {_dev(r['chunk_id'])}",
                    "kind": "prose", "text": clean(r.get("bhashya"))}
            item.update({"passages": [], "commentaries": comms, "links": {}} if full
                        else {"commentary_titles": [c["title"] for c in comms]})
            out.append(item)
        return out


def _ac_works() -> list[_Work]:
    return [
        _Sutrapatha("ashtadhyayi", "अष्टाध्यायी (सवृत्तिः)", "पाणिनिः"),
        _Sutrapatha("siddhanta-kaumudi", "सिद्धान्तकौमुदी", "भट्टोजिदीक्षितः", order="skn", chapter="sk_chapter",
                    main="kaumudi"),
        _Sutrapatha("laghu-siddhanta-kaumudi", "लघुसिद्धान्तकौमुदी", "वरदराजः", order="lskn", chapter="lsk_chapter",
                    main="laghukaumudi"),
        _Mahabhashya(),
        _Rows("vakyapadiya", "वाक्यपदीयम्", "भर्तृहरिः", "vakyapadeeyam/data.txt", "text", sec="kanda",
              ref="id", after=(("artha", "अर्थः"),),
              commentary_files=(("vakyapadeeyam/swopajna.txt", lambda r: f"{r['kanda']}.{r['id']}",
                                 "स्वोपज्ञवृत्तिः"),
                                ("vakyapadeeyam/swopajna2.txt", lambda r: f"{r['kanda']}.{r['id']}",
                                 "स्वोपज्ञवृत्तिः"),
                                ("vakyapadeeyam/ambakartri.txt", lambda r: f"{r['kanda']}.{r['id']}",
                                 "अम्बाकर्त्री"))),
        _Rows("paribhashendushekhara", "परिभाषेन्दुशेखरः", "नागेशभट्टः", "paribhashendushekhar/data.txt", "paribhasha",
              ref="num", before=(("prelude", "अवतरणम्"),), after=(("text", "व्याख्या"),)),
        _Rows("vaiyakarana-bhushanasara", "वैयाकरणभूषणसारः", "कौण्डभट्टः", "bhushanasara/data.txt", "kaarika",
              sec="section_id", sec_label="section", ref="kaarika_id", before=(("prelude", "अवतरणम्"),),
              after=(("vyakhyaa", "व्याख्या"),)),
        _Rows("parama-laghu-manjusha", "परमलघुमञ्जूषा", "नागेशभट्टः", "paramalaghumanjoosha/data.txt", "text",
              sec="chapter", sec_label="name", ref="name"),
        _Rows("linganushasana", "लिङ्गानुशासनम्", "पाणिनिः", "linganushasanam/data.txt", "sutra", sec="adhikaar",
              sec_label="adhikaar", ref="id", after=(("sk", "सिद्धान्तकौमुदी"),)),
        _Rows("unadi-sutra", "उणादिसूत्राणि", None, "unaadi/data.txt", "sutra", ref="i",
              after=(("pratyay", "प्रत्ययः"), ("sk", "सिद्धान्तकौमुदी"))),
        _Rows("paniniya-shiksha", "पाणिनीयशिक्षा", None, "shiksha/data.txt", "text", ref="id",
              after=(("pc", "पदच्छेदः"), ("anvaya", "अन्वयः"), ("artha", "अर्थः"), ("tatparya", "तात्पर्यम्"))),
        _Rows("tarkasangraha", "तर्कसङ्ग्रहः", "अन्नंभट्टः", "tarkasangraha/data.txt", "text", ref="topic",
              after=(("category", "विभागः"), ("teeka", "दीपिका"))),
    ]


class AshtadhyayiCom:
    id = "ac"
    rights = "ashtadhyayi.com data (github.com/ashtadhyayi-com/data) — credit ashtadhyayi.com; texts public domain."

    @lru_cache(maxsize=1)
    def _works(self) -> dict[str, _Work]:
        return {w.slug: w for w in _ac_works() if w.available()}

    def _w(self, slug: str) -> _Work:
        w = self._works().get(slug)
        if w is None:
            raise KeyError(slug)
        return w

    def works(self) -> list[dict]:
        return [{"id": f"{self.id}:{w.slug}", "provider": self.id, "slug": w.slug, "title": w.title,
                 "author": w.author, "group": w.group, "group_label": "व्याकरणम् · दर्शनम् (ashtadhyayi.com)",
                 "rights": self.rights, "local_only": False, "source_url": "https://ashtadhyayi.com/",
                 "has_words": False} for w in self._works().values()]

    def sections(self, slug: str) -> list[dict]:
        return self._w(slug).sections()

    def section(self, slug: str, sec: str) -> dict:
        w = self._w(slug)
        lab = next((s["label"] for s in w.sections() if s["id"] == sec), None)
        if lab is None:
            raise KeyError(sec)
        return {"label": lab, "items": w.items(sec)}

    def section_full(self, slug: str, sec: str) -> list[dict]:
        return self._w(slug).items(sec, full=True)

    def item(self, slug: str, sec: str, item_id: str) -> dict:
        it = next((x for x in self._w(slug).items(sec, full=True) if x["id"] == item_id), None)
        if it is None:
            raise KeyError(item_id)
        return it

    def search(self, q: str, limit: int) -> list[dict]:
        hits = []
        for w in self._works().values():
            for s in w.sections():
                for it in w.items(s["id"]):
                    j = it["text"].find(q)
                    if j >= 0:
                        hits.append({"work": f"{self.id}:{w.slug}", "title": w.title, "section": s["id"],
                                     "item": it["id"], "ref": it["ref"], "kind": it["kind"],
                                     "snippet": it["text"][max(0, j - 20): j + len(q) + 20]})
                        if len(hits) >= limit:
                            return hits
        return hits


# ── catalogue ─────────────────────────────────────────────────────────────

PROVIDERS = {p.id: p for p in (AdvaitaSharada(), Samsaadhanii(), AshtadhyayiCom())}


def provider_of(work_id: str):
    pid, _, slug = work_id.partition(":")
    if pid not in PROVIDERS or not slug:
        raise KeyError(work_id)
    return PROVIDERS[pid], slug


def catalogue() -> list[dict]:
    out = []
    for p in PROVIDERS.values():
        try:
            out.extend(p.works())
        except (OSError, KeyError, ValueError):
            continue  # a source not downloaded on this machine is simply absent
    return out


def work(work_id: str) -> dict:
    w = next((x for x in catalogue() if x["id"] == work_id), None)
    if w is None:
        raise KeyError(work_id)
    p, slug = provider_of(work_id)
    return {**w, "sections": p.sections(slug)}


def section(work_id: str, sec: str) -> dict:
    p, slug = provider_of(work_id)
    secs = [s["id"] for s in p.sections(slug)]
    if sec not in secs:
        raise KeyError(sec)
    i = secs.index(sec)
    return {"work": work_id, "section": sec, **p.section(slug, sec),
            "prev": secs[i - 1] if i else None, "next": secs[i + 1] if i + 1 < len(secs) else None}


def item(work_id: str, sec: str, item_id: str) -> dict:
    p, slug = provider_of(work_id)
    return {"work": work_id, "section": sec, **p.item(slug, sec, item_id)}


def passages(work_id: str) -> list[dict]:
    """Every item of a work with all of its text (mūla, passages, commentaries) flattened — for a client's index.
    ``{section, item, ref, text, commentary}``; ``commentary`` kept apart so a client can weigh the two."""
    p, slug = provider_of(work_id)
    out = []
    for s in p.sections(slug):
        if hasattr(p, "section_full"):  # one pass per section instead of one per item
            fulls = p.section_full(slug, s["id"])
        else:
            fulls = [p.item(slug, s["id"], it["id"]) for it in p.section(slug, s["id"])["items"]]
        for full in fulls:
            it = full
            comm = [c.get("text") or "\n".join(r["text"] for r in c.get("rows", [])) for c in full.get("commentaries", [])]
            for ps in full.get("passages", []):
                comm.append(ps["text"])
                comm += [c.get("text") or "\n".join(r["text"] for r in c.get("rows", [])) for c in ps.get("commentaries", [])]
            out.append({"section": s["id"], "item": it["id"], "ref": it["ref"], "text": full["text"],
                        "commentary": "\n".join(x for x in comm if x)})
    return out


def search(q: str, limit: int = 60, provider: str | None = None) -> list[dict]:
    q = (q or "").strip()
    if not q:
        return []
    hits = []
    for p in PROVIDERS.values():
        if provider and p.id != provider:
            continue
        try:
            hits.extend(p.search(q, limit - len(hits)))
        except (OSError, KeyError, ValueError):
            continue
        if len(hits) >= limit:
            break
    return hits[:limit]


def is_local_only(work_id: str) -> bool:
    return work_id.partition(":")[0] == "as"
