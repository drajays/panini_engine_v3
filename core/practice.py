"""
core/practice.py — अभ्यास: practice questions drawn from what the engine derives.
────────────────────────────────────────────────────────────────────────────────

Every question comes from ``data/index/forms.db`` (so the answer key is the
engine's own derivation, re-derivable by cell key), and every answer can be
explained sūtra by sūtra through ``/v1/subanta`` / ``/v1/tinanta``.

Where a vendored attested paradigm exists (``tools.shabda_table``), a cell the
engine disagrees with is never asked — a wrong answer key teaches the wrong form.

Kinds:
  mcq     — "put X into cell B": pick one of four forms of the same lemma
  recall  — same prompt, type the answer
  tf      — "Y is cell B of X": सत्य / असत्य
  sutra   — one derivation step shown (before → after): which sūtra did it?

Presentation code only: never imported by engine / sutras / phonology / pipelines.
"""
from __future__ import annotations

import json
import random
from contextlib import closing
from functools import cache
from pathlib import Path
from typing import Any

from core.transliterate import slp1_to_dev
from engine.form_index import connect

VIBHAKTI = ["", "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन"]
VACANA = ["", "एकवचन", "द्विवचन", "बहुवचन"]
PURUSHA = ["", "उत्तम", "मध्यम", "प्रथम"]   # engine: 1 = uttama … 3 = prathama
LAKARA = {"laT": "लट्", "liT": "लिट्", "luT": "लुट्", "lRT": "लृट्", "loT": "लोट्",
          "laG": "लङ्", "vidhiliG": "विधिलिङ्", "ASIrliG": "आशीर्लिङ्", "luG": "लुङ्",
          "lRG": "लृङ्"}   # engine spellings (data/inputs/tin_upadesha.json keys)
KINDS = ("mcq", "recall", "tf", "sutra")


def cell_label(kind: str, f: dict[str, Any]) -> str:
    if kind == "subanta":
        return f"{VIBHAKTI[f['vibhakti']]} {VACANA[f['vacana']]}"
    lak = LAKARA.get(f["lakara"], f["lakara"])
    return f"{lak} {PURUSHA[f['purusha']]}-पुरुष {VACANA[f['vacana']]}"


def _gold_ok(lemma: str, f: dict[str, Any], dev: str) -> bool:
    """False only when an attested paradigm exists and does not list this form."""
    from tools.shabda_table import paradigms

    gold = paradigms().get(lemma)
    if not gold or gold.get("linga") != f.get("linga"):
        return True
    return dev in gold["cells"].get(f"{f['vibhakti']}-{f['vacana']}", [dev])


VERIFIED_PATH = Path(__file__).resolve().parent.parent / "bench" / "oracle" / "practice_verified.json"


@cache
def verified_keys() -> frozenset[str]:
    """Cells where our form is among Vidyut's (bench/practice_key). Missing file → empty:
    no answer key is trusted until it has been cross-checked."""
    try:
        return frozenset(json.loads(VERIFIED_PATH.read_text())["verified"])
    except FileNotFoundError:
        return frozenset()


@cache
def path_ok_keys() -> frozenset[str]:
    """Verified cells whose every surface-changing sūtra is also in Vidyut's path:
    the only cells a "which sūtra?" question or a sūtra example may come from."""
    try:
        return frozenset(json.loads(VERIFIED_PATH.read_text()).get("path_ok", ()))
    except FileNotFoundError:
        return frozenset()


def _rows(kind: str, lemma: str | None, linga: str | None) -> list[dict[str, Any]]:
    q = "SELECT surface_slp1, surface_dev, lemma, features, cell_key FROM forms WHERE kind = ?"
    args: list[Any] = [kind]
    if lemma:
        q += " AND lemma = ?"
        args.append(lemma)
    if linga and kind == "subanta":
        q += " AND json_extract(features, '$.linga') = ?"
        args.append(linga)
    with closing(connect()) as conn:
        rows = [{**dict(r), "features": json.loads(r["features"])} for r in conn.execute(q, args)]
    ok = verified_keys()
    return [r for r in rows if r["cell_key"] in ok
            and (kind != "subanta" or _gold_ok(r["lemma"], r["features"], r["surface_dev"]))]


def sutra_examples(sutra_id: str, limit: int = 12) -> dict[str, Any]:
    """Cross-checked forms in which this sūtra changed the surface."""
    from engine.form_index import examples

    rows = examples(sutra_id, limit, keep=path_ok_keys())
    return {"total": rows[0]["total"] if rows else 0,
            "forms": [{"dev": r["surface_dev"], "slp1": r["surface_slp1"], "kind": r["kind"],
                       "lemma": r["lemma"], "lemma_dev": _lemma_dev(r["kind"], r["lemma"]),
                       "cell_label": cell_label(r["kind"], r["features"]),
                       "features": r["features"]} for r in rows]}


def lemmas(kind: str) -> list[dict[str, Any]]:
    """Lemmas with at least 8 verified cells, in dhātupāṭha / alphabetical order."""
    count: dict[tuple[str, str | None], int] = {}
    for r in _rows(kind, None, None):
        k = (r["lemma"], r["features"].get("linga"))
        count[k] = count.get(k, 0) + 1
    names = dhatu_names() if kind == "tinanta" else {}
    out = [{"lemma": l, "dev": _lemma_dev(kind, l), "linga": g, "cells": n,
            "id": names.get(l, ("",))[0] if names else ""}
           for (l, g), n in count.items() if n >= 8]
    return sorted(out, key=lambda x: (x["id"], x["lemma"]))


def _lemma_dev(kind: str, lemma: str) -> str:
    if kind == "tinanta":
        return dhatu_names().get(lemma, (None, slp1_to_dev(lemma)))[1]
    return slp1_to_dev(lemma)


@cache
def dhatu_names() -> dict[str, tuple[str, str]]:
    """upadeśa SLP1 → (dhātupāṭha id, mūla-dhātu Devanāgarī); first gaṇa wins."""
    from pipelines.dhatupatha import _envelope, _payload

    out: dict[str, tuple[str, str]] = {}
    for e in _envelope(_payload())["entries"]:
        out.setdefault(e["upadesha_slp1"], (e.get("dhatupatha_id") or "99", e.get("mula_dhatu_dev") or slp1_to_dev(e["upadesha_slp1"])))
    return out


def question(kind: str = "subanta", qtype: str = "mcq", *, lemma: str | None = None,
             linga: str | None = None, level: str = "easy",
             seed: int | None = None) -> dict[str, Any]:
    """One practice question. ``level``: easy | hard (distractors share vibhakti/vacana
    or lakāra/puruṣa with the answer — the near misses learners actually make)."""
    rng = random.Random(seed)
    rows = _rows(kind, lemma, linga)
    pool = [r for r in rows if r["cell_key"] in path_ok_keys()] if qtype == "sutra" else rows
    if not pool:
        raise LookupError(f"no derived {kind} forms for lemma={lemma!r} linga={linga!r}")
    target = rng.choice(pool)
    paradigm = [r for r in rows if r["lemma"] == target["lemma"]]
    accepted = sorted({r["surface_dev"] for r in paradigm if r["cell_key"] == target["cell_key"]})
    others = [r for r in paradigm if r["surface_dev"] not in accepted]
    source = rng.choice(others or [target])
    tf = target["features"]
    cells_of: dict[str, list[str]] = {}          # रामाभ्याम् is 3/2, 4/2 and 5/2 at once
    for r in paradigm:
        cells_of.setdefault(r["surface_dev"], []).append(cell_label(kind, r["features"]))
    label = lambda dev: " / ".join(dict.fromkeys(cells_of[dev]))

    base = {
        "kind": kind, "type": qtype, "lemma": target["lemma"],
        # the pāṭha id disambiguates homonymous upadeśas for the explanation
        "dhatu_ref": target["cell_key"].split("@")[1].split(":")[0] if kind == "tinanta" else None,
        "lemma_dev": _lemma_dev(kind, target["lemma"]),
        "features": tf, "cell_label": cell_label(kind, tf),
        "source": {"dev": source["surface_dev"],
                   "cell_label": cell_label(kind, source["features"])},
        "labels": {d: label(d) for d in cells_of},
        "accepted": accepted,
    }
    base["attested"] = _attested(base["dhatu_ref"], tf)
    if qtype in ("mcq", "recall"):
        if level == "hard":
            near = [r for r in others if any(r["features"].get(k) == tf.get(k)
                                             for k in ("vibhakti", "vacana", "lakara", "purusha"))]
            others = near if len(near) >= 3 else others
        wrong = list(dict.fromkeys(r["surface_dev"] for r in rng.sample(others, len(others))))[:3]
        options = [{"dev": d, "cell_label": label(d)} for d in [*wrong, accepted[0]]]
        rng.shuffle(options)
        return {**base, "options": options if qtype == "mcq" else []}
    if qtype == "tf":
        truth = rng.random() < 0.5 or not others
        shown = accepted[0] if truth else rng.choice(others)["surface_dev"]
        return {**base, "claim": shown, "answer": truth}
    if qtype == "sutra":
        return {**base, **_sutra_step(kind, target, rng)}
    raise ValueError(f"unknown question type {qtype!r}; one of {KINDS}")


def _attested(dhatu_id: str | None, f: dict[str, Any]) -> list[dict[str, Any]]:
    """Kāvya lines using this very tiṅanta cell (ashtadhyayi.com; display only)."""
    if not dhatu_id or f.get("prayoga", "kartari") != "kartari":
        return []
    from core.lab import _ASHT_LAKARA
    from core.trace_view import attested_for_dhatu
    a, tail = attested_for_dhatu(dhatu_id), f"{_ASHT_LAKARA[f['lakara']]}_{4 - f['purusha']}_{f['vacana']}"
    return (a.get("p" + tail) or a.get("a" + tail) or [])[:2]


def _sutra_step(kind: str, row: dict[str, Any], rng: random.Random) -> dict[str, Any]:
    """Pick one surface-changing step of the target's derivation; distractors are
    other sūtras that changed the surface in the same derivation, else anywhere."""
    from core.trace_view import enrich_trace, filter_surface_changed, lsk_pages
    from tools.build_form_index import derive_cell

    state = derive_cell({"kind": kind, "lemma": row["lemma"], "features": row["features"]})
    steps = [s for s in filter_surface_changed(enrich_trace(list(state.trace)))
             if s.get("sutra_id") and not s["sutra_id"].startswith("__") and s.get("_sutra_text_dev")]
    if not steps:
        raise LookupError(f"no surface-changing sūtra step for {row['cell_key']}")
    step = rng.choice(steps)
    sid = step["sutra_id"]
    pool = {s["sutra_id"]: s["_sutra_text_dev"] for s in steps if s["sutra_id"] != sid}
    if len(pool) < 3:
        from engine import SUTRA_REGISTRY
        pada = sid.rsplit(".", 1)[0] + "."   # same pada first: plausible, not random
        extra = [r for r in SUTRA_REGISTRY.values() if r.text_dev and r.sutra_id != sid]
        near = [r for r in extra if r.sutra_id.startswith(pada)]
        for r in rng.sample(near, min(6, len(near))) + rng.sample(extra, 12):
            pool.setdefault(r.sutra_id, r.text_dev)
    opts = [{"sutra_id": k, "text_dev": v} for k, v in list(pool.items())[:3]]
    opts.append({"sutra_id": sid, "text_dev": step["_sutra_text_dev"]})
    rng.shuffle(opts)
    return {"before_dev": step["form_before_dev"], "after_dev": step["form_after_dev"],
            "options": opts, "answer_sutra": sid, "lsk": lsk_pages(sid)}


if __name__ == "__main__":   # smoke check: every kind produces a well-formed question
    for k in KINDS:
        q = question("subanta", k, lemma="rAma", seed=1)
        assert q["accepted"] and q["cell_label"], q
        if k == "mcq":
            assert sum(o["dev"] in q["accepted"] for o in q["options"]) == 1, q
        if k == "sutra":
            assert q["answer_sutra"] in {o["sutra_id"] for o in q["options"]}, q
        print(k, "ok:", q["source"]["dev"], "→", q["cell_label"], q["accepted"])
    print("tinanta ok:", question("tinanta", "mcq", lemma="BU", seed=2)["accepted"])
