"""Neelesh Bodas, अ-इ-उकारान्तशब्दा: (2015) as a gate: for 11 stems (rAma muni sAdhu mAlA mati nadI Denu vaDU Pala vAri maDu) × the
cells the PDF's सङ्क्षेपः tables cover, (1) the form is among the engine's vikalpa readings and (2) every sūtra the PDF says fires does
APPLY in a branch that yields that form. Teaching aid, not authority (Art. 23): the sūtra SET is asserted, never the order, and a miss is
classified in docs/AI_U_SUBANTA_GOLD.md (KNOWN below, each with its class) — never loosened. rAma / Pala / nadI forms come from the attested
shabda tables (data/reference/shabda_gold); the other eight are written out in the gold file."""
from __future__ import annotations

import json
import pathlib

import pytest

import sutras  # noqa: F401
from core.transliterate import dev_to_slp1
from engine.vikalpa import explore
from pipelines.subanta import derive

ROOT = pathlib.Path(__file__).resolve().parents[2]
GOLD = json.loads((pathlib.Path(__file__).parent / "data" / "paddhati_subanta_ai_u.json").read_text(encoding="utf-8"))
SHABDA = {"rAma": "pulliṅga", "Pala": "napuṃsaka", "nadI": "strīliṅga"}

# (stem, cell) -> "class: why". Classes: gap (engine lacks the PDF's step) | order-equivalent (same form, engine licenses it by another sūtra)
# | pdf-lists-vacuous (PDF names a sūtra that has nothing to do on this stem). Detail: docs/AI_U_SUBANTA_GOLD.md. strict xfail: a fix flips it.
_G61090 = "gap: the sup's āṭ (7.3.112) sits inside the affix, so 6.1.90 (reads a separate aTa_agama Term) never sees it; 6.1.88 yields the same ai"
_GS2 = "gap: ledger S2 — ṭāp stays a separate Term, so the ā-stem ṅit-sup route (7.3.105 / 7.3.113 / 7.3.116 + 6.1.101) is not walked"
_V6403 = "pdf-lists-vacuous: the stem is already long, 6.4.3 has nothing to lengthen"
_G7124 = "gap: 7.1.24 am→am is an identity ādeśa and is SKIPPED (7.1.23 never contends for an a-final neuter)"
KNOWN: dict[tuple[str, str], str] = {
    **{(s, c): _G61090 for s in ("mati", "Denu", "nadI", "vaDU") for c in ("4-1", "5-1", "6-1")},
    ("mAlA", "3-1"): _GS2, ("mAlA", "5-1"): _GS2, ("mAlA", "6-1"): _GS2, ("mAlA", "7-1"): _GS2,
    **{(s, "6-3"): _V6403 for s in ("mAlA", "nadI", "vaDU")},

    ("Pala", "2-1"): _G7124,   # ("Pala", "8-1") fixed 2026-11-16: 7.1.24 now also takes the sambuddhi su (Kāśikā 6.1.69), S188
}


def _forms(stem: str) -> dict[str, list[str]]:
    if stem in GOLD["forms"]:
        return GOLD["forms"][stem]
    g = json.loads((ROOT / "data/reference/shabda_gold" / f"{stem}_{SHABDA[stem]}.json").read_text(encoding="utf-8"))
    return {c: [dev_to_slp1(f) for f in g["cells"][c]] for c in g["cells"]}


def _cases():
    out = []
    for r in GOLD["rows"]:
        for stem in r["stems"]:
            for cell in r["cells"]:
                out.append((stem, cell, r["sutras"], r.get("alt_sutras")))
    return out


CASES = [
    pytest.param(*c, id=f"{c[0]}-{c[1]}", marks=pytest.mark.xfail(reason=KNOWN[c[:2]], strict=True) if c[:2] in KNOWN else ())
    for c in _cases()
]


@pytest.mark.parametrize("stem,cell,want_sutras,alt", CASES)
def test_cell(stem, cell, want_sutras, alt):
    vib, vac = map(int, cell.split("-"))
    forms = _forms(stem)[cell]
    branches = explore(lambda: derive(stem, vib, vac, linga=GOLD["stems"][stem]))
    got = {b.surface_slp1 for b in branches}
    for i, form in enumerate(forms):
        assert form in got, f"{stem} {cell}: {form} not among {sorted(got)}"
        sset = want_sutras if i == 0 else alt
        if not sset:
            continue
        applied = [{t.get("sutra_id") for t in b.state.trace if t.get("status") == "APPLIED"} for b in branches if b.surface_slp1 == form]
        assert any(set(sset) <= a for a in applied), f"{stem} {cell} {form}: PDF sūtras {sset}; best branch lacks {min((set(sset) - a for a in applied), key=len)}"
