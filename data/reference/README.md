# data/reference/ — READ-ONLY GOLD CORPUS

**Firewall notice (CONSTITUTION Article 6).**

This directory holds gold-standard paradigms, Kāśikā examples, and
Siddhāntakaumudī worked forms.  It exists **only** to test whether
the engine reproduces what classical grammarians produced.

**The engine itself must never import from this directory.**

- `engine/` — forbidden.
- `sutras/` — forbidden.
- `phonology/` — forbidden.
- `pipelines/` — forbidden.
- `tools/` — allowed (e.g. `validate_engine_against_source.py`).
- `tests/` — allowed (and expected).

The test
`tests/constitutional/test_no_reference_import_from_engine.py`
enforces this by scanning every engine / sūtra / phonology / pipeline
module for the literal string `data/reference`.

---

## Layout

```
reference/
├── subanta_gold/
│   ├── rama_pullinga.json           ← 24-cell राम paradigm
│   ├── hari_pullinga.json           ← i-stem
│   └── ...
├── tinanta_gold/
│   ├── bhu_lat_parasmai.json        ← भू, laT, parasmai, all 9 cells
│   └── ...
├── kashika_examples/
│   └── sutra_<id>_examples.json     ← sūtra-by-sūtra Kāśikā gold
└── README.md                         ← this file
```

Cells are JSON: `{ "form_dev": "...", "form_slp1": "...", "path_sutras": ["X.Y.Z", ...] }`.
