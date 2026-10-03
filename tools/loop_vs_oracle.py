"""
tools/loop_vs_oracle.py — the rule-driven tiṅanta loop against the *independent* oracle (Vidyut, committed
as ``bench/oracle/vidyut.csv``), not against our own recipe. The recipe can be wrong where the loop is right
(its liṭ uttama is ``BUvmi``); an external oracle can prove us wrong, never right (Art. 19).

    python3 -m tools.loop_vs_oracle [--lakara loT] [--root BU]
"""
from __future__ import annotations

import argparse
import collections
import csv
import sys
from pathlib import Path
from types import SimpleNamespace as NS

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def cells(lakara: str | None, root: str | None):
    with (ROOT / "bench" / "oracle" / "vidyut.csv").open(encoding="utf-8") as fp:
        for row in csv.DictReader(fp):
            parts = row["key"].split(":")
            if parts[0] != "tinanta":
                continue
            _, dhatu, lak, purusha, vacana = parts
            if (lakara and lak != lakara) or (root and dhatu != root):
                continue
            yield dhatu, lak, int(purusha), int(vacana), [f for f in row["forms"].split("|") if f]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lakara")
    ap.add_argument("--root")
    args = ap.parse_args(argv)
    import sutras  # noqa: F401
    from tools.autonomy_report import run_autonomously, start_state

    tally: dict = collections.defaultdict(lambda: [0, 0])
    misses = []
    for dhatu, lak, p, v, forms in cells(args.lakara, args.root):
        tally[(lak, dhatu)][1] += 1
        try:
            run = run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lak, p, v))), forms[0], dhatu, 200)
            got = run.surface
        except Exception as ex:                     # a lakāra whose attach sūtra is not written yet
            got = f"<{type(ex).__name__}>"
        if got in forms:
            tally[(lak, dhatu)][0] += 1
        else:
            misses.append((lak, dhatu, p, v, got, forms))
    for (lak, dhatu), (ok, n) in sorted(tally.items()):
        print(f"  {lak:<8}{dhatu:<10}{ok}/{n}")
    print(f"  total {sum(a for a, _ in tally.values())}/{sum(n for _, n in tally.values())}")
    for m in misses[:40]:
        print("   ✗", m)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
