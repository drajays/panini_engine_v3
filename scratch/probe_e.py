"""probe: python3 scratch/probe_e.py <sense> <stem> [key=val ...] [tag:lexname ...] -> the forms the loop gives"""
import sys

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

import os
LINGA = os.environ.get("LINGA", "napuṃsaka")
sense = sys.argv[1]
stems = sys.argv[2].split(",")
tags = {a[4:] for a in sys.argv[3:] if a.startswith("tag:")}
extra = dict(a.split("=") for a in sys.argv[3:] if "=" in a)
for stem in stems:
    got = sorted({b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, LINGA, origin_tags=tags or None, taddhitArtha=sense, **extra))})
    print(stem, got)
