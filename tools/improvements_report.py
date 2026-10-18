"""tools/improvements_report.py — docs/improvements.html: what the 2026-10-18 work changed, measured live.

    .venv/bin/python -m tools.improvements_report      # ~30 s: runs every probe case through the autonomous loop

Each row: the Kāśikā form (tools/findings_probe.py), the loop's output at 45e6f9a3 (measured 2026-10-18 before the
Phase 1 commit; "—" where that cell was not measured), the loop's output now, and the form-changing sūtra steps.
"""
from __future__ import annotations

import html
import sys
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace as NS

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))
OUT = _ROOT / "docs" / "improvements.html"

BEFORE = {   # loop surface at 45e6f9a3, from the first findings_probe run of 2026-10-18
    ("Adadi_02_0061", "laT", 3, 1): "markti", ("BvAdi_01_1144", "laT", 3, 1): "daMSati",
    ("BvAdi_01_0642", "liT", 3, 1): "jijAya", ("Adadi_02_0040", "liT", 3, 2): "iyatuH",
    ("Adadi_02_0025", "loT", 1, 3): "savAmahE", ("Adadi_02_0025", "loT", 1, 1): "savE",
    ("BvAdi_01_1124", "liT", 3, 2): "tataratuH", ("BvAdi_01_0868", "liT", 3, 1): "vavyaTe",
    ("BvAdi_01_1160", "liT", 3, 2): "UsatuH", ("JuhotyAdi_03_0025", "laT", 3, 2): "jajantaH",
    ("BvAdi_01_1163", "liT", 3, 1): "jahvO", ("BvAdi_01_1162", "liT", 3, 1): "vavyO",
    ("JuhotyAdi_03_0002", "loT", 1, 1): "biByAni", ("Adadi_02_0070", "laT", 3, 2): "SAstaH",
}
NUMBERS = [  # measured: sig/ ledgers and suite runs of 2026-10-18
    ("Confident sūtras (sig/sutra_class.json)", "222", "286"),
    ("Implemented sūtras (tools.sutra_lint, Art. 16)", "312", "315"),
    ("Sūtras invoked / moving the tape (firing ledger)", "—", "714 / 428"),
    ("Test suite", "20,314 passed", "20,357 passed"),
    ("Kāśikā forms right in the autonomous loop (probe)", "15 / 26", "26 / 30"),
]
AMENDMENT = [
    "Accepted with the owner's ruling: every value from the Aṣṭādhyāyī data, nothing discovered by the engine.",
    "Meaning (vivakṣā) vocabulary generated from the sūtras' own samagra texts — each value cites the sūtras that name it.",
    "A rule may ask about a meaning only if its own samagra contains that word (constitutional test).",
    "Transitivity per dhātu from ashtadhyayi.com dhātupāṭha <code>karma</code>: 2,229 rows, 10 recorded gaps.",
    "Every varṇa a rule creates carries <code>origin:&lt;sūtra&gt;</code> — 6.4.22 asiddhatva now reads it (जजातः).",
]


def _dev(s: str) -> str:
    from phonology import mk
    from phonology.joiner import slp1_to_devanagari
    try:
        return slp1_to_devanagari([mk(c) for c in s if c.isalpha()])
    except Exception:
        return s


def main() -> int:
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY
    from tools.autonomy_report import run_autonomously, start_state
    from tools.findings_probe import CASES
    from pipelines.dhatupatha import iter_dhatu_entries

    root_dev = {r["id"]: r.get("upadesha_dev") or r["upadesha_slp1"] for r in iter_dhatu_entries()}
    rows = []
    for ref, lak, pu, vc, pada, want in CASES:
        run = run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250)
        now, before = run.surface, BEFORE.get((ref, lak, pu, vc))
        ok = now in want
        status = ("fixed today" if ok and before and before not in want else
                  "right" if ok else "known gap")
        steps = "".join(
            f"<li><b>{html.escape(sid)}</b> {html.escape(getattr(SUTRA_REGISTRY.get(sid), 'text_dev', '') or '')}"
            f" — {_dev(b)} → {_dev(a)}</li>"
            for sid, b, a, _why in run.steps if b != a)
        rows.append((status, ref, lak, pu, vc, want, before, now, steps))

    order = {"fixed today": 0, "known gap": 1, "right": 2}
    rows.sort(key=lambda r: order[r[0]])
    count = {k: sum(r[0] == k for r in rows) for k in order}
    trs = "".join(
        f"<tr class='{s.replace(' ', '-')}'><td>{s}</td><td class='dev'>{html.escape(root_dev.get(ref, ref))}"
        f"<br><small>{html.escape(ref)} · {lak} {pu}-{vc}</small></td>"
        f"<td class='dev'>{' / '.join(_dev(w) for w in sorted(want))}</td>"
        f"<td class='dev'>{_dev(before) if before else '—'}</td><td class='dev'>{_dev(now)}</td>"
        f"<td><details><summary>{steps.count('<li>')} steps</summary><ol>{steps}</ol></details></td></tr>"
        for s, ref, lak, pu, vc, want, before, now, steps in rows)
    nums = "".join(f"<tr><td>{a}</td><td>{b}</td><td><b>{c}</b></td></tr>" for a, b, c in NUMBERS)
    amend = "".join(f"<li>{x}</li>" for x in AMENDMENT)
    page = f"""<!doctype html><html lang="sa"><head><meta charset="utf-8">
<title>पाणिनि-यन्त्रम् — improvements 2026-10-18</title>
<style>
body{{font-family:-apple-system,"Noto Sans Devanagari",sans-serif;margin:2rem auto;max-width:1100px;color:#222;padding:0 1rem}}
h1{{font-weight:600}} table{{border-collapse:collapse;width:100%;margin:1rem 0}} td,th{{border-bottom:1px solid #ddd;padding:.45rem;
text-align:left;vertical-align:top}} th{{background:#f6f1e7}} .dev{{font-size:1.25rem}} .fixed-today td:first-child{{color:#0a7a2f;font-weight:600}}
.known-gap td:first-child{{color:#b45309;font-weight:600}} .right td:first-child{{color:#666}} details ol{{margin:.3rem 0 0 1rem;font-size:.95rem}}
.cards span{{display:inline-block;margin:.3rem .8rem .3rem 0;padding:.6rem 1rem;border-radius:.5rem;background:#f6f1e7}}
small{{color:#666}}
</style></head><body>
<h1>पाणिनि-यन्त्रम् — what improved (18 Oct 2026)</h1>
<p>Every form below is derived <b>now</b> by the autonomous rule loop (no recipe), and compared with the Kāśikā form recorded
in the brain. Generated {datetime.now():%Y-%m-%d %H:%M} by <code>tools/improvements_report.py</code>.</p>
<div class="cards"><span>✅ fixed today: <b>{count['fixed today']}</b></span><span>⚠️ known gaps: <b>{count['known gap']}</b></span>
<span>already right: <b>{count['right']}</b></span></div>
<h2>Numbers</h2><table><tr><th>measure</th><th>before</th><th>now</th></tr>{nums}</table>
<h2>Forms (Kāśikā vs the loop)</h2>
<table><tr><th>status</th><th>dhātu</th><th>Kāśikā</th><th>loop before</th><th>loop now</th><th>sūtras that changed the form</th></tr>{trs}</table>
<h2>AMENDMENT 25 — vivakṣā inputs, from authentic data only</h2><ul>{amend}</ul>
<p><small>Known gaps stay strict xfails in <code>tests/regression/test_findings_probe_loop.py</code>; a fixed gap fails the test
until it is moved out. Fixed the same day: the loop no longer depends on Python's set-hash order (tests/regression/test_hash_seed_independence.py).</small></p>
</body></html>
"""
    OUT.write_text(page, encoding="utf-8")
    print(f"{OUT.relative_to(_ROOT)}: fixed {count['fixed today']}, gaps {count['known gap']}, right {count['right']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
