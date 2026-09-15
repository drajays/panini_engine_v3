#!/bin/sh
# Panini Engine v3 — unified local web UI (Flask webui/)
# Usage: ./run_web.sh [port]
# Default 5050 — macOS AirPlay often occupies 5000.
PORT="${1:-5050}"
ROOT="$(cd "$(dirname "$0")" && pwd)"
export PANINI_PORT="$PORT"

echo "Starting Pāṇini Engine v3 web UI on http://127.0.0.1:${PORT}"
cd "$ROOT" || exit 1

# Open browser on macOS/Linux when possible (background, non-blocking)
if command -v open >/dev/null 2>&1; then
  (sleep 1.5 && open "http://127.0.0.1:${PORT}") &
elif command -v xdg-open >/dev/null 2>&1; then
  (sleep 1.5 && xdg-open "http://127.0.0.1:${PORT}") &
fi

exec python3 -m webui.app
