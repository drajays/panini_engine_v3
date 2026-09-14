#!/bin/sh
# ─────────────────────────────────────────────────────────────────
# Pāṇini Engine — double-click launcher (macOS).
#
# Starts both local UIs and opens the browser:
#   :8000/review  — derive a form and correct the prakriyā (+ /docs for the API)
#   :5050         — the full Flask UI (paradigms, dhātupāṭha, SIG, tests)
#
# Closing this Terminal window stops both servers.
# ─────────────────────────────────────────────────────────────────
cd "$(dirname "$0")" || exit 1

API_PORT=8000
WEB_PORT=5050

# Pick a python that already has the deps; else install into the first one.
PY=""
for cand in .venv/bin/python3 python3; do
  command -v "$cand" >/dev/null 2>&1 || [ -x "$cand" ] || continue
  if "$cand" -c 'import flask, fastapi, uvicorn' 2>/dev/null; then PY="$cand"; break; fi
  [ -z "$PY" ] && PY="$cand"          # remember the first usable interpreter
done
[ -z "$PY" ] && { echo "python3 not found — install it from python.org"; read -r _; exit 1; }

if ! "$PY" -c 'import flask, fastapi, uvicorn' 2>/dev/null; then
  echo "Installing dependencies into $PY …"
  "$PY" -m pip install -q -r requirements-api.txt flask || {
    echo "install failed — see the errors above"; read -r _; exit 1; }
fi

busy() { lsof -ti "tcp:$1" >/dev/null 2>&1; }

trap 'kill 0' EXIT INT TERM       # closing this window stops the servers

if busy "$API_PORT"; then
  echo "Port $API_PORT already serving — reusing it."
else
  "$PY" -m uvicorn api.main:app --port "$API_PORT" &
fi

if busy "$WEB_PORT"; then
  echo "Port $WEB_PORT already serving — reusing it."
else
  PANINI_PORT="$WEB_PORT" "$PY" -m webui.app &
fi

cat <<EOF

  पाणिनि-यन्त्रम् — running locally

  संशोधनम्  http://127.0.0.1:${API_PORT}/review   derive + correct
  API docs  http://127.0.0.1:${API_PORT}/docs
  पूर्ण-UI   http://127.0.0.1:${WEB_PORT}/        paradigms · धातुपाठ · SIG

  Close this window (or press Ctrl-C) to stop.
  (the engine loads 3985 sūtras — the full UI needs a few more seconds)

EOF

# Open the browser only once the API actually answers.
i=0
while [ "$i" -lt 60 ] && ! curl -sf -o /dev/null "http://127.0.0.1:${API_PORT}/v1/health"; do
  i=$((i + 1)); sleep 1
done
open "http://127.0.0.1:${API_PORT}/review"

wait
