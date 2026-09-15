"""
tools/build_shabda_page.py — the śabda table as data for the web page.

For every vendored paradigm, derive all 24 cells and record each one as a
*reading sequence*: the form after each change, and the sūtras that made it.
That is the shape ashtadhyayi.com's detail panel uses, and it is the shape a
scholar reads —

    राम
    → राम + टा   [ स्वौजसमौट्… ४.१.२ इति टा-प्रत्ययः । सुप्तिङन्तं पदम् १.४.१४ … ]
    → राम + आ    [ चुटू १.३.७ इति इत्संज्ञा । तस्य लोपः १.३.९ इति लोपः । ]
    → रामेन      [ आद्गुणः ६.१.८७ इति गुणैकादेशः । ]
    → रामेण      [ अट्कुप्वाङ्… ८.४.२ इति णत्वम् । ]

Steps that leave the form untouched (saṃjñā, adhikāra) are not dropped — they
are folded into the bracket of the change they licensed, which is how the
tradition cites them.

    python3 -m tools.build_shabda_page      # writes docs/data/shabda.json
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from core.prakriya_view import TermRecorder, reading  # noqa: E402

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

OUT = _ROOT / "docs" / "data" / "shabda.json"

# This writes the *snapshot* the public GitHub Pages copy reads, because a
# static host has no engine. The live table is served by api/ and derives on
# every click; see api/shabda.html.

VIBHAKTI_DEV = ("प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी",
                "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधनम्")
VACANA_DEV = ("एकवचनम्", "द्विवचनम्", "बहुवचनम्")


def build() -> dict[str, Any]:
    import sutras  # noqa: F401
    from pipelines.subanta import derive
    from tools.shabda_table import paradigms

    words = []
    for stem, data in paradigms().items():
        cells = {}
        for vibhakti in range(1, 9):
            for vacana in range(1, 4):
                key = f"{vibhakti}-{vacana}"
                attested = data["cells"].get(key, [])
                try:
                    with TermRecorder() as recorder:
                        state = derive(stem, vibhakti, vacana, linga=data["linga"])
                    form, steps, error = state.flat_dev(), reading(state, recorder), ""
                except Exception as ex:                    # a gap, shown as one
                    form, steps, error = "", [], f"{type(ex).__name__}: {ex}"
                cells[key] = {
                    "form_dev": form,
                    "attested": attested,
                    "agrees": bool(form) and form in attested,
                    "steps": steps,
                    "error": error,
                }
        words.append({
            "stem_slp1": stem,
            "word": data["word"],
            "linga": data["linga"],
            "artha": data.get("artha", ""),
            "cells": cells,
        })
    return {
        "labels": {"vibhakti": VIBHAKTI_DEV, "vacana": VACANA_DEV},
        "source": "derived by this engine; attested forms from ashtadhyayi-com/data",
        "built_at": date.today().isoformat(),
        "words": sorted(words, key=lambda w: w["stem_slp1"].lower()),
    }


def main() -> int:
    payload = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
                   encoding="utf-8")
    cells = sum(len(w["cells"]) for w in payload["words"])
    agree = sum(1 for w in payload["words"] for c in w["cells"].values() if c["agrees"])
    size = OUT.stat().st_size / 1024
    print(f"  {len(payload['words'])} paradigms · {cells} cells · {agree} agree")
    print(f"  {OUT.relative_to(_ROOT)}  ({size:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
