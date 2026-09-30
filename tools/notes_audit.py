"""
tools/notes_audit.py — compare hand-written prakriyā notes with the engine's traces.

A folder of Markdown notes, one form per file (the filename is the form). For
each note the sūtras it cites are collected (by number, Devanāgarī or Latin
digits, and by quoted pāṭha text); the engine derivation of the same form is
found among the recipe pipelines (docs/data/index.json); and the two sets are
compared:

    note-only    the note applies it, the engine never does → check the engine
    engine-only  the engine applies it, the note never cites it → check the note
                 (or it is a saṃjñā/paribhāṣā the note takes for granted)

The notes are a reference, not gold: they are read, never loaded by the engine.

    python3 -m tools.notes_audit "/path/to/my panini notes"   # → docs/NOTES_AUDIT.md
"""
from __future__ import annotations

import argparse
import importlib
import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")
_ID = re.compile(r"(?<![\d.])([1-8])\.([1-4])\.(\d{1,3})(?![\d.])")
OUT = _ROOT / "docs" / "NOTES_AUDIT.md"


def cited_sutras(text: str, patha: dict[str, str]) -> set[str]:
    from tools.sync_sutrapatha import norm
    t = text.translate(_DIGITS)
    ids = {f"{a}.{b}.{c}" for a, b, c in _ID.findall(t)}
    flat = norm(text)
    for sid, s in patha.items():                  # quoted by text (≥ 5 letters, to stay specific)
        n = norm(s)
        if len(n) >= 5 and n in flat:
            ids.add(sid)
    return {i for i in ids if i in patha}


def engine_forms() -> dict[str, list[tuple[str, str]]]:
    """SLP1 form → [(module, callable)] from the Pages index of recipe pipelines."""
    idx = json.loads((_ROOT / "docs" / "data" / "index.json").read_text())
    out: dict[str, list[tuple[str, str]]] = {}
    for r in idx["derivations"]:
        if r.get("ok") and r.get("form"):
            out.setdefault(r["form"], []).append((r["module"], r["callable"]))
    return out


def applied(module: str, fn: str) -> set[str]:
    mod = importlib.import_module(f"pipelines.{module}")
    st = getattr(mod, fn)()
    return {e["sutra_id"] for e in st.trace
            if e.get("status") == "APPLIED" and not (e.get("sutra_id") or "").startswith("__")}


# सर्वादि/त्यादि: closed, well-known pronoun stems whose declined surface forms
# (सर्वे, सर्वस्मै, अमी, अमू, …) never equal the stem itself, so a note's key
# can't be tried as its own stem the way an ordinary prātipadika can. Same set
# pipelines.subanta.derive() already special-cases for sambodhana exclusion,
# plus सर्व (handled separately there, but an ordinary derive() call).
_PRONOUN_STEMS = ("sarva", "tad", "yad", "etad", "idam", "adas")
# Ordinary paradigm stems the notes decline (अग्नी, वायो, गौरी, यशांसि, माले): the same
# "key must equal a declined form, never the stem itself" discipline applies.
_COMMON_STEMS = ("agni", "vAyu", "gOrI", "yaSas", "mAlA")
_LINGAS = ("pulliṅga", "strīliṅga", "napuṃsaka")


def _applied_from_state(st) -> set[str]:
    return {e["sutra_id"] for e in st.trace
            if e.get("status") == "APPLIED" and not (e.get("sutra_id") or "").startswith("__")}


def general_subanta_match(key: str) -> tuple[str, set[str]] | None:
    """Try the *generic* subanta pipeline (not a curated one-off recipe) as a
    सर्वादि/त्यादि pronoun declension — covers notes like सर्वे/सर्वस्मै (सर्व)
    or अमी/अमू (अदस्) that a curated index of hand-written recipes was never
    going to list by name.

    Deliberately does **not** try ``stem == key`` (the note's own surface
    form) as a candidate stem: subanta.derive() doesn't validate that a
    string is a real prātipadika, and most stems produce a bare-visarga
    prathamā-ekavacana by default — trying the surface form against itself
    at (1,1) would "match" almost anything, verifying nothing.
    """
    from pipelines.subanta import derive as subanta_derive

    for targets in ({key}, {key.rstrip("H") + "H", key.rstrip("H")}):   # exact surface first
        for stem in _PRONOUN_STEMS + _COMMON_STEMS:
            lingas = ("strīliṅga", "pulliṅga", "napuṃsaka") if stem[-1] in "IA" else _LINGAS   # ī/ā stems: strī first
            for linga in lingas:
                for vibhakti in range(1, 9):
                    if vibhakti == 8 and stem in {"tad", "yad", "etad", "idam", "adas"}:
                        continue   # subanta.derive() raises: tyadādi take no sambodhana
                    for vacana in (1, 2, 3):
                        try:
                            st = subanta_derive(stem, vibhakti, vacana, linga)
                        except Exception:
                            continue
                        if st.flat_slp1() in targets:
                            label = f"subanta.derive({stem!r}, {vibhakti}, {vacana}, {linga!r})"
                            return label, _applied_from_state(st)
    return None


_UPASARGAS = ("pra", "parA", "apa", "sam", "anu", "ava", "nis", "nir", "dus", "dur", "vi", "A",
              "ni", "aDi", "api", "ati", "su", "ut", "aBi", "prati", "pari", "upa")


def _upasarga_splits(key: str):
    """(prefix list, remainder) for 0–2 leading upasargas; ṇatva tolerated (praRi = pra+ni)."""
    yield [], key
    for a in _UPASARGAS:
        for b in (None, *_UPASARGAS):
            ups = [a] if b is None else [a, b]
            joined = "".join(ups)
            for pre in {joined, joined.replace("n", "R")}:
                if key.startswith(pre) and len(key) > len(pre):
                    yield ups, key[len(pre):]


def general_tinanta_match(key: str) -> tuple[str, set[str]] | None:
    """Look the verb form up in the generated-forms index (after stripping leading
    upasargas), re-derive that exact cell, and accept only an exact surface match."""
    from engine.form_index import lookup
    from pipelines.dhatupatha import resolve_dhatu_identifier
    from pipelines.tinanta import derive as tin_derive

    for ups, rest in _upasarga_splits(key):
        for hit in lookup(rest):
            if hit["kind"] != "tinanta":
                continue
            f = hit["features"]
            ref = hit["cell_key"].split("@")[1].split(":")[0]
            try:
                resolve_dhatu_identifier(ref)
            except KeyError:
                ref = hit["lemma"]
            try:
                st = tin_derive(ref, f["lakara"], f["prayoga"], f["purusha"], f["vacana"],
                                upasargas=ups or None)
            except Exception:
                continue
            if st.flat_slp1() == key:
                label = (f"tinanta.derive({ref!r}, {f['lakara']!r}, {f['prayoga']!r}, "
                         f"{f['purusha']}, {f['vacana']}, upasargas={ups!r})")
                return label, _applied_from_state(st)
    return None


def audit(notes_dir: Path) -> str:
    from phonology.tokenizer import devanagari_to_slp1_flat
    from tools.sync_sutrapatha import patha
    ref = patha()
    forms = engine_forms()
    rows, unmatched = [], []
    for f in sorted(notes_dir.glob("*.md")):
        name = f.stem.strip(" ‘’'\"")
        try:
            key = devanagari_to_slp1_flat(name.split()[0])
        except Exception:
            unmatched.append((f.name, "not a form"))
            continue
        cands = forms.get(key) or forms.get(key.rstrip("H") + "H") or forms.get(key.rstrip("H"))
        note = cited_sutras(f.read_text(encoding="utf-8"), ref)
        if not cands:
            general = (general_subanta_match(key) or general_tinanta_match(key)) if key else None
            if general is None:
                unmatched.append((f.name, f"no engine recipe for {key}"))
                continue
            where, eng = general
            rows.append((f.name, key, where, sorted(note - eng, key=_k), sorted(eng - note, key=_k),
                         len(note & eng)))
            continue
        mod, fn = cands[0]
        try:
            eng = applied(mod, fn)
        except Exception as ex:
            unmatched.append((f.name, f"{mod}.{fn} raised {type(ex).__name__}"))
            continue
        rows.append((f.name, key, f"{mod}.{fn}", sorted(note - eng, key=_k), sorted(eng - note, key=_k),
                     len(note & eng)))
    lines = ["# Notes vs engine — sūtra paths", "",
             f"{len(rows)} notes matched to an engine recipe; {len(unmatched)} not matched.",
             "note-only: the note applies it, the engine never does. engine-only: the "
             "engine applies it, the note does not cite it (often a saṃjñā the note assumes).", ""]
    for name, key, where, n_only, e_only, both in rows:
        lines += [f"## {name} — `{key}`", f"engine: `{where}` · shared: {both}",
                  f"- note-only: {', '.join(n_only) or '—'}",
                  f"- engine-only: {', '.join(e_only) or '—'}", ""]
    lines += ["## Not matched", ""] + [f"- {n}: {why}" for n, why in unmatched]
    return "\n".join(lines) + "\n"


def _k(sid: str):
    return tuple(int(x) for x in sid.split("."))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("notes_dir", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=OUT)
    a = ap.parse_args(argv)
    a.out.write_text(audit(a.notes_dir), encoding="utf-8")
    print(f"→ {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
