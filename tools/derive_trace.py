"""tools/derive_trace.py — one tiṅanta form through the autonomous loop, every sūtra step shown.

    .venv/bin/python -m tools.derive_trace BU laT 3 1            # dhātu (upadeśa or row id) lakāra puruṣa vacana
    .venv/bin/python -m tools.derive_trace hveY liT 3 1 parasmai  # an ubhayapadī root: give the pada

puruṣa 3 = prathama, 2 = madhyama, 1 = uttama · vacana 1 = eka, 2 = dvi, 3 = bahu ·
lakāra: laT liT luT lRT loT laG liG AsIrliG luG lRG. Presentation only.
"""
from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace as NS

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        print(__doc__)
        return 1
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY
    from phonology.joiner import slp1_to_devanagari
    from tools.autonomy_report import run_autonomously, start_state

    dhatu, lakara, purusha, vacana = argv[0], argv[1], int(argv[2]), int(argv[3])
    pada = argv[4] if len(argv) > 4 else None
    run = run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, purusha, vacana), pada=pada)), "", dhatu, 250)
    from phonology import mk

    def dev(s: str) -> str:
        try:
            return slp1_to_devanagari([mk(c) for c in s if c.isalpha()])
        except Exception:          # a display helper: fall back to the SLP1 string
            return s
    for n, (sid, before, after, why) in enumerate(run.steps, 1):
        text = getattr(SUTRA_REGISTRY.get(sid), "text_dev", "") or ""
        mark = "→" if before != after else " "
        print(f"{n:>3}. {sid:<8} {text[:28]:<28} {dev(before):<16} {mark} {dev(after):<16} [{why}]")
    print(f"\n  {dhatu} {lakara} {purusha}-{vacana}{' ' + pada if pada else ''}:  {dev(run.surface)}   ({run.surface})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
