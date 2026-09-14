# xxweb/ — DEPRECATED

**Do not run.** This folder is kept for reference only.

The canonical web UI is **[`webui/`](../webui/)**, launched via:

```bash
./run_web.sh
# → http://127.0.0.1:5050/
```

## What this was

Early FastAPI + HTMX prototype with six pages (paradigm, tinanta, krdanta,
special stems, devendra, dik). All features are superseded by the Flask app
in `webui/`.

## Old launch command (do not use)

```bash
cd xxweb
uvicorn app:app --reload --port 8000
```

Shared display helpers (`filter_surface_changed`, etc.) now live in
[`webui/display.py`](../webui/display.py).
