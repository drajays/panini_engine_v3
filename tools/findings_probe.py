"""tools/findings_probe.py — run the autonomous loop on the wrong outputs logged by the brain's carding job.

    .venv/bin/python -m tools.findings_probe

Each case is (dhātupāṭha row id, lakāra, puruṣa, vacana, pada, expected forms). Expected forms come from the
Kāśikā / Kaumudī as recorded in ~/data-master/ashtadhyayi-ai/transcript_work/ENGINE_FINDINGS.md (card ids in
the comment). Diagnostic only: prints loop vs expected; never an engine input.
"""
from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace as NS

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

CASES = [
    ("JuhotyAdi_03_0004", "laT", 3, 2, None, {"pipUrtaH"}),          # pṛ 7.1.102 (C-910..914)
    ("JuhotyAdi_03_0004", "laT", 3, 3, None, {"pipurati"}),
    ("Adadi_02_0061", "laT", 3, 1, None, {"mArzwi"}),                # mṛj 7.2.114
    ("BvAdi_01_1043", "laT", 3, 1, "parasmai", {"gUhati"}),         # guh 6.4.89
    ("BvAdi_01_1144", "laT", 3, 1, None, {"daSati"}),                # daṃś 6.4.25
    ("BvAdi_01_0919", "liT", 3, 2, None, {"sasmaratuH"}),           # smṛ 7.4.60
    ("BvAdi_01_1163", "liT", 3, 1, "parasmai", {"juhAva"}),         # hve 6.1.33 (C-940..949)
    ("BvAdi_01_1162", "liT", 3, 1, "parasmai", {"vivyAya"}),        # vye 6.1.46
    ("BvAdi_01_0642", "liT", 3, 1, None, {"jigAya"}),               # ji 7.3.57
    ("svAdi_05_0012", "liT", 3, 1, None, {"jiGAya"}),               # hi 7.3.56
    ("Adadi_02_0040", "liT", 3, 2, None, {"IyatuH"}),               # iṇ 6.4.81
    ("Adadi_02_0025", "loT", 1, 3, None, {"suvAmahE"}),             # ṣūṅ 7.3.88 / 6.4.77
    ("Adadi_02_0025", "loT", 1, 1, None, {"suvE"}),
    ("Adadi_02_0027", "loT", 1, 1, None, {"yavAni"}),               # yu 7.3.89 hali
    ("JuhotyAdi_03_0002", "loT", 1, 1, None, {"biBayAni"}),         # bhī: guṇa before āni (pit)
    ("BvAdi_01_1124", "liT", 3, 2, None, {"teratuH"}),              # tṝ 6.4.122 (C-1620..1622)
    ("svAdi_05_0020", "liT", 3, 1, None, {"AnaSe"}),                # aś 7.4.72
    ("BvAdi_01_0868", "liT", 3, 1, None, {"vivyaTe"}),              # vyath 7.4.68
    ("Adadi_02_0075", "liT", 3, 2, None, {"USatuH"}),               # vaś 6.1.16
    ("divAdi_04_0078", "liT", 3, 2, None, {"viviDatuH"}),           # vyadh 6.1.16
    ("tudAdi_06_0013", "liT", 3, 2, None, {"vivicatuH"}),           # vyac 6.1.16
    ("BvAdi_01_1160", "liT", 3, 2, None, {"UzatuH"}),               # vas 6.1.15, 8.3.60
    ("BvAdi_01_0812", "liT", 3, 3, None, {"jakzuH"}),               # ghas 8.3.60 after ku
    ("Adadi_02_0070", "laT", 3, 2, None, {"SizwaH"}),               # śās 6.4.34, 8.3.60
    ("tudAdi_06_0149", "liT", 3, 2, None, {"papracCatuH"}),         # pracch 7.4.60 halādiḥ śeṣaḥ
    ("kryAdi_09_0071", "liT", 3, 2, "parasmai", {"jagfhatuH"}),     # grah 6.1.16 + 7.4.60/62
    ("tudAdi_06_0004", "liT", 3, 2, "parasmai", {"baBrajjatuH", "baBarjatuH"}),  # bhrasj 6.4.47
    ("BvAdi_01_0001", "AsIrliG", 3, 1, None, {"BUyAt"}),            # bhū āśīrliṅ (C-1530..1533)
    ("JuhotyAdi_03_0025", "laT", 3, 2, None, {"jajAtaH"}),          # jan 6.4.42 (C-585)
    ("JuhotyAdi_03_0009", "laT", 3, 2, None, {"jahitaH", "jahItaH"}),  # hā 6.4.116 (C-580)
]


def main() -> int:
    import sutras  # noqa: F401
    from tools.autonomy_report import run_autonomously, start_state

    if sys.argv[1:2] == ["trace"]:   # trace <row id> <lakāra> <puruṣa> <vacana> [pada]
        ref, lak, pu, vc = sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
        pada = sys.argv[6] if len(sys.argv) > 6 else None
        run = run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250)
        for step in run.steps:
            print("  ".join(str(x) for x in step))
        print("=>", run.surface, run.outcome)
        return 0

    bad = 0
    for ref, lak, pu, vc, pada, want in CASES:
        try:
            got = run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250).surface
        except Exception as e:  # diagnostic: show the failure, keep going
            got = f"ERR {type(e).__name__}"
        ok = got in want
        bad += not ok
        print(f"{'ok ' if ok else 'BAD'} {ref:<20} {lak:<7} {pu}-{vc} {pada or '':<8} loop {got:<16} want {'/'.join(sorted(want))}")
    print(f"{len(CASES) - bad}/{len(CASES)} match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
