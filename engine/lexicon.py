"""
engine/lexicon.py — the Lexicon (AMENDMENT 22): stem origin as data, saṃjñās derived.

Input file: ``data/inputs/subanta_lexicon.json`` (Art. 6). Entry::

    {"stem": "Bagavat", "linga": "pulliṅga",
     "components": [{"kind": "prakriti", "upadesha": "Baga"},
                    {"kind": "taddhita", "upadesha": "matu~p", "artha": "tadasyAstyasminniti"}]}

kinds: ``prakriti`` (a nominal base), ``dhatu`` (an upadeśa of the Dhātupāṭha), ``krt`` / ``taddhita`` (an upadeśa from
``krit_pratyaya.json`` / ``taddhita_pratyaya.json``). **Only lexical facts live here** — never a derived property (ugit, nadī,
kvip-ness, bha, pada …): ``validate`` rejects every key outside the schema.

``compose`` puts the components on a tape as separate Terms, lets the *real* it-prakaraṇa (1.3.2–1.3.9) and, for matup, the
real 8.2.9 / 8.2.10 run, and reads the record from the Terms afterwards. It refuses (``LexiconGap``, Art. 17/18) when the
composed surface is not the entry's stem — an analysis the engine cannot reproduce is a gap, not a guess.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from engine import origin

_ROOT = Path(__file__).resolve().parent.parent / "data" / "inputs"
LEXICON_PATH = _ROOT / "subanta_lexicon.json"

KINDS = frozenset({"prakriti", "dhatu", "krt", "taddhita"})
ENTRY_KEYS = frozenset({"stem", "linga", "components", "source"})   # source: the citation that licenses the analysis (Art. 14)
COMPONENT_KEYS = frozenset({"kind", "upadesha", "artha", "dhatu_id"})
LINGAS = frozenset({"pulliṅga", "strīliṅga", "napuṃsaka"})


class LexiconGap(Exception):
    """The entry's analysis does not reproduce its stem (Art. 17); names what is missing (Art. 18)."""


@lru_cache(maxsize=1)
def _entries() -> dict[tuple[str, str], dict]:
    if not LEXICON_PATH.exists():
        return {}
    data = json.loads(LEXICON_PATH.read_text(encoding="utf-8"))
    return {(e["stem"], e["linga"]): e for e in data.get("entries", [])}


def lookup(stem_slp1: str, linga: str) -> dict | None:
    return _entries().get((stem_slp1, linga))


def reload() -> None:
    _entries.cache_clear()


@lru_cache(maxsize=1)
def _known_upadeshas() -> dict[str, frozenset[str]]:
    def _base(u: str) -> str:
        return u.replace("~", "").replace("\\", "").replace("^", "")

    krt = json.loads((_ROOT / "krit_pratyaya.json").read_text(encoding="utf-8"))
    tad = json.loads((_ROOT / "taddhita_pratyaya.json").read_text(encoding="utf-8"))
    dh = json.loads((_ROOT / "dhatupatha_upadesha.json").read_text(encoding="utf-8"))
    dhatus: set[str] = set()
    for r in dh["entries"]:                       # the upadeśa (with its it-letters) and the root after it-lopa both name the dhātu
        for k in ("upadesha_slp1", "raw_dhatu_after_it_lopa_slp1", "citation_dhatu_slp1"):
            if r.get(k):
                dhatus.add(_base(r[k]))
    return {
        "krt": frozenset(_base(v.get("upadesha_slp1", k)) if isinstance(v, dict) else _base(k)
                         for k, v in krt.items() if not k.startswith("_")) | frozenset(k for k in krt if not k.startswith("_")),
        "taddhita": frozenset(k for k in tad if not k.startswith("_")),
        "dhatu": frozenset(dhatus),
        "_base": frozenset(),
    }


def validate(entry: dict) -> list[str]:
    """Problems with one entry (empty list = valid). The schema is closed: a derived property is an error."""
    errs: list[str] = []
    extra = set(entry) - ENTRY_KEYS
    if extra:
        errs.append(f"{entry.get('stem')}: keys outside the schema {sorted(extra)} (a derived property is not a lexical fact)")
    if entry.get("linga") not in LINGAS:
        errs.append(f"{entry.get('stem')}: bad liṅga {entry.get('linga')!r}")
    comps = entry.get("components") or []
    if not comps:
        errs.append(f"{entry.get('stem')}: no components")
    known = _known_upadeshas()
    for c in comps:
        bad = set(c) - COMPONENT_KEYS
        if bad:
            errs.append(f"{entry.get('stem')}: component keys outside the schema {sorted(bad)}")
        if c.get("kind") not in KINDS:
            errs.append(f"{entry.get('stem')}: bad component kind {c.get('kind')!r}")
            continue
        u = (c.get("upadesha") or "").replace("~", "").replace("\\", "").replace("^", "")
        if c["kind"] in ("krt", "taddhita") and u not in known[c["kind"]]:
            errs.append(f"{entry.get('stem')}: {c['kind']} upadeśa {c.get('upadesha')!r} is in no input table")
        if c["kind"] == "dhatu" and u not in known["dhatu"]:
            errs.append(f"{entry.get('stem')}: dhātu {c.get('upadesha')!r} is not in the Dhātupāṭha input")
    return errs


def _dhatu_row(c: dict) -> dict:
    from pipelines.dhatupatha import resolve_dhatu_identifier
    return resolve_dhatu_identifier(c.get("dhatu_id") or c["upadesha"])


def compose(entry: dict) -> tuple[str, set[str]]:
    """:func:`generate` and require that the result is the entry's stem (Art. 17); else :class:`LexiconGap` (Art. 18)."""
    surface, tags = generate(entry)
    if surface != entry["stem"]:
        raise LexiconGap(f"{entry['stem']}: the components give {surface!r} — a sūtra between them is not written (Art. 18)")
    return surface, tags


def generate(entry: dict) -> tuple[str, set[str]]:
    """Make the stem from its components by the engine's own rules; return (surface, origin tags).

    * dhātu + kṛt (kartṛ = kṛ + tṛc): the tape [dhātu][kṛt] goes to the autonomous loop — it-lopa, 3.4.114, iṭ (7.2.35 / 7.2.10),
      guṇa (7.3.84), raparatva (1.1.51) … — exactly as a tiṅanta tape does. Nothing is concatenated.
    * a nominal base + taddhita matup, or upapada + dhātu + kvip: the components are laid out as Terms, the real it-prakaraṇa
      (1.3.2–1.3.9) runs, then 6.1.67 (kvip) and the tripāḍī 8.2.9 / 8.2.10 (matup's m → v).

    ``entry['stem']`` is only the expected surface; the tool ``propose_vyutpatti`` calls this with a placeholder to enumerate what
    the engine *can* generate (Art. 17: analysis proposes, generation verifies)."""
    import sutras  # noqa: F401  (register the rules)
    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence
    from pipelines.it_prakarana import run_it_prakarana

    comps = entry["components"]
    if len(comps) == 2 and comps[0]["kind"] == "dhatu" and comps[1]["kind"] == "krt":
        from engine.tape_init.tinanta import dhatu_term_from_row
        from tools.autonomy_report import run_autonomously

        dh = dhatu_term_from_row(_dhatu_row(comps[0]), "kartari", "laT")
        dh.tags.discard("kartari")
        pr = Term(kind="pratyaya", varnas=parse_slp1_upadesha_sequence(comps[1]["upadesha"]),
                  tags={"pratyaya", "krt", "upadesha"}, meta={"upadesha_slp1": comps[1]["upadesha"]})
        if comps[1].get("artha"):
            pr.meta["artha"] = comps[1]["artha"]
        s = State(terms=[dh, pr])
        s.phase = "pratyaya"
        run = run_autonomously(s, entry["stem"], entry["stem"], 300)
        return run.surface, {g for t in run.state.terms for g in t.tags if g.startswith(origin.ORIGIN_PREFIXES)}

    terms: list[Term] = []
    for c in comps:
        up = c["upadesha"]
        if c["kind"] in ("krt", "taddhita"):
            t = Term(kind="pratyaya", varnas=parse_slp1_upadesha_sequence(up),
                     tags={"pratyaya", c["kind"], "upadesha"}, meta={"upadesha_slp1": up})
        elif c["kind"] == "dhatu":
            t = Term(kind="prakriti", varnas=parse_slp1_upadesha_sequence(_dhatu_row(c)["upadesha_slp1"]),
                     tags={"dhatu", "upadesha"}, meta={"upadesha_slp1": _dhatu_row(c)["upadesha_slp1"]})
        else:
            t = Term(kind="prakriti", varnas=parse_slp1_upadesha_sequence(up), tags={"prātipadika"}, meta={"upadesha_slp1": up})
        if c.get("artha"):
            t.meta["artha"] = c["artha"]
        terms.append(t)
    s = State(terms=terms)
    s = run_it_prakarana(s)
    rules = json.loads((_ROOT / "lexicon_compose_rules.json").read_text(encoding="utf-8"))
    for sid in rules["after_it_prakarana"]:         # kvip's apṛkta v is lopa'd (the kṛt stays on the tape as the stem's last pratyaya)
        s = apply_rule(sid, s)
    if any((t.meta.get("upadesha_slp1") or "") == "matu~p" for t in s.terms):
        s.tripadi_zone = True                      # 8.2.9 / 8.2.10 are tripāḍī rules
        for sid in rules["tripadi_when_matup"]:
            s = apply_rule(sid, s)
    return s.flat_slp1(), origin.record_from_terms(s.terms)
