#!/bin/sh
# Start the Panini Engine v3 web UI
# Usage: ./run_web.sh [port]
PORT=${1:-8000}
cd "$(dirname "$0")/web"
python3 -m uvicorn app:app --reload --port "$PORT" --host 0.0.0.0
