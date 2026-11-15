"""tools/impl_score.py — how fully each sūtra is implemented, out of 10 (10 = fully tested AND clean under the engine policy).

    python3 -m tools.impl_score            # writes sig/impl_score.json   (the pages /sutras and /sutra/<id> read it)

Every point comes from recorded evidence, nothing is judged by hand:

  A  Exists as a real rule                      0–2   placeholder 0 · stub / gate-only 1 · real cond+act 2
  B  Fires in the full suite (firing ledger)    0–1.5 invoked 0.5 · and it changes the tape (moved) +1   (a saṃjñā / paribhāṣā / adhikāra that is invoked gets the full 1.5: it never moves the tape)
  C  Proven by cases                            0–3   LK case gate: confident 3 · working 2 · FAIL 0.5 ;  no LK cases: ≥5 test mentions 2 (confident_structural) · 1–4 mentions 1 · none 0
  D  Engine policy (glass box, rule-based)      0–2.5 starts 2.5; −1 for each OPEN row of docs/SHORTCUT_LEDGER.md that names the sūtra (a lookup, a bare augment, an order shortcut …); −1 if the file uses an `_arm` flag
  E  Source fidelity                            0–1   sūtra text registered 0.5 · padaccheda registered 0.5

  placeholder → 0/10 whatever else.  gate-only → at most 3/10.  An LK FAIL caps the total at 6.
  10/10 needs: real rule, fires and moves the tape, LK `confident`, no open ledger row, no arm flag, text + padaccheda.
The score says how far the engine is from the śāstra and the policy FOR THAT SŪTRA; it is not a verdict on a form. Shortcuts are listed in `notes`.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "sig" / "impl_score.json"
NO_MOVE = {"SAMJNA", "PARIBHASHA", "ADHIKARA", "ANUVADA", "PRATISHEDHA"}
_ID = re.compile(r"(?<![\d.])(\d)\.(\d)\.(\d{1,3})(?![\d.])")


def open_ledger_rows() -> dict[str, list[str]]:
    """sūtra id -> ids of the OPEN shortcut-ledger rows that name it."""
    out: dict[str, list[str]] = {}
    for line in (ROOT / "docs" / "SHORTCUT_LEDGER.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not re.fullmatch(r"S\d+", cells[0]):
            continue
        if not cells[-1].lower().startswith("open"):
            continue
        for m in _ID.finditer(cells[1]):
            out.setdefault(".".join(m.groups()), []).append(cells[0])
    return out


def _uses_arm(sid: str) -> bool:
    a, b, c = sid.split(".")
    p = ROOT / f"sutras/adhyaya_{a}/pada_{b}/sutra_{a}_{b}_{c}.py"
    return p.exists() and bool(re.search(r"_arm\b|_arm\"", p.read_text(encoding="utf-8")))


def score_all() -> dict:
    cls = {r["id"]: r for r in json.loads((ROOT / "sig" / "sutra_class.json").read_text(encoding="utf-8"))["rows"]}
    led = open_ledger_rows()
    out = {}
    for sid, r in cls.items():
        rec = SUTRA_REGISTRY.get(sid)
        notes: list[str] = []
        status = r["status"]
        if r["placeholder"] or rec is None:
            out[sid] = {"score": 0.0, "parts": {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}, "status": status, "notes": ["not implemented (placeholder)"]}
            continue
        A = 1.0 if (r["stub_gloss"] or status == "gate_only") else 2.0
        if A == 1.0:
            notes.append("stub / gate-only: the rule does not yet do its own work")
        B = 0.0
        if r["invoked"]:
            B = 1.5 if r["type"] in NO_MOVE else (0.5 + (1.0 if r["moved"] else 0.0))
        else:
            notes.append("never fires in the full suite")
        g = r.get("lk_grade")
        if g == "confident":
            C = 3.0
        elif g == "working":
            C = 2.0
        elif g == "FAIL":
            C = 0.5
            notes.append("an LK case fails (engine gap or case error)")
        elif r["mentions"] >= 5:
            C = 2.0
        elif r["mentions"] >= 1:
            C = 1.0
        else:
            C = 0.0
        D = 2.5
        rows = led.get(sid, [])
        if rows:
            D -= min(len(rows), 2)
            notes.append("open shortcut(s): " + ", ".join(rows))
        if _uses_arm(sid):
            D -= 1.0
            notes.append("uses an _arm flag")
        D = max(D, 0.0)
        E = (0.5 if rec.text_dev else 0.0) + (0.5 if rec.padaccheda_dev else 0.0)
        total = A + B + C + D + E
        if status == "gate_only":
            total = min(total, 3.0)
        if g == "FAIL":
            total = min(total, 6.0)
        out[sid] = {"score": round(total, 1), "parts": {"A": A, "B": B, "C": C, "D": D, "E": E}, "status": status, "notes": notes}
    return out


if __name__ == "__main__":
    from collections import Counter
    s = score_all()
    OUT.write_text(json.dumps(s, ensure_ascii=False, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    c = Counter(int(v["score"]) for v in s.values())
    print(f"{len(s)} sūtras -> {OUT.relative_to(ROOT)}; by whole mark:", dict(sorted(c.items())))
    print("10/10:", sum(v["score"] >= 10 for v in s.values()), " ≥8:", sum(v["score"] >= 8 for v in s.values()), " 0:", sum(v["score"] == 0 for v in s.values()))
