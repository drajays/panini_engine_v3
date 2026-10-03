#!/bin/sh
# ─────────────────────────────────────────────────────────────────
# Pāṇini Engine — double-click launcher (macOS).
#
# Double-click starts the full local system (offline after first
# dependency install).  Pass `menu` for tests / benches / publish.
# ─────────────────────────────────────────────────────────────────
cd "$(dirname "$0")" || exit 1

API_PORT=8000
WEB_PORT=5050

# Pick a python that already has the deps; else install into the first one.
PY=""
for cand in .venv/bin/python3 python3; do
  command -v "$cand" >/dev/null 2>&1 || [ -x "$cand" ] || continue
  if "$cand" -c 'import flask, fastapi, uvicorn, pytest' 2>/dev/null; then PY="$cand"; break; fi
  [ -z "$PY" ] && PY="$cand"          # remember the first usable interpreter
done
[ -z "$PY" ] && { echo "python3 not found — install it from python.org"; read -r _; exit 1; }

if ! "$PY" -c 'import flask, fastapi, uvicorn, pytest' 2>/dev/null; then
  echo "Installing dependencies into $PY (once; afterwards this is fully offline) …"
  "$PY" -m pip install -q -r requirements-api.txt flask pytest || {
    echo "install failed — see the errors above"; read -r _; exit 1; }
fi

pause() { printf '\n  Press Enter to return to the menu… '; read -r _; }

# ashtadhyayi.com data (test gold) is gitignored; fetch it once when a bench needs it.
need_gold() {
  [ -f data/reference/ashtadhyayi_com/dhatu__data.txt ] && return 0
  echo "Downloading the ashtadhyayi.com data (once, ~50 MB) …"
  "$PY" -m tools.fetch_ashtadhyayi_data
}

start_apps() {
  busy() { lsof -ti "tcp:$1" >/dev/null 2>&1; }
  trap 'kill 0' EXIT INT TERM       # closing this window stops the servers

  if busy "$API_PORT"; then echo "Port $API_PORT already serving — reusing it."
  else "$PY" -m uvicorn api.main:app --host 127.0.0.1 --port "$API_PORT" & fi

  if busy "$WEB_PORT"; then echo "Port $WEB_PORT already serving — reusing it."
  else PANINI_PORT="$WEB_PORT" "$PY" -m webui.app & fi

  cat <<EOF

  पाणिनि-यन्त्रम् — local (offline)

  Home      http://127.0.0.1:${API_PORT}/
  Lab       http://127.0.0.1:${API_PORT}/lab
  अभ्यास    http://127.0.0.1:${API_PORT}/practice
  संशोधनम्  http://127.0.0.1:${API_PORT}/review
  सूत्र-व्याप्तिः http://127.0.0.1:${API_PORT}/coverage   (confident sūtras · recipe-free derivation)
  पाठः      http://127.0.0.1:${API_PORT}/pages/learn.html
  API docs  http://127.0.0.1:${API_PORT}/docs
  पूर्ण-UI   http://127.0.0.1:${WEB_PORT}/

  Close this window (or press Ctrl-C) to stop.
  (the engine loads ~4000 sūtras — the full UI needs a few more seconds)

EOF
  i=0
  while [ "$i" -lt 90 ] && ! curl -sf -o /dev/null "http://127.0.0.1:${API_PORT}/v1/health"; do
    i=$((i + 1)); sleep 1
  done
  j=0
  while [ "$j" -lt 90 ] && ! curl -sf -o /dev/null "http://127.0.0.1:${WEB_PORT}/"; do
    j=$((j + 1)); sleep 1
  done
  open "http://127.0.0.1:${API_PORT}/"
  wait
  exit 0
}

publish() {
  echo "Rebuilding the website data from the current engine …"
  "$PY" -m tools.build_pages && "$PY" -m tools.build_shabda_page || { echo "build failed"; return; }
  echo; echo "Running the test suite before publishing …"
  "$PY" -m pytest -q -p no:cacheprovider || { echo; echo "Tests failed — not publishing."; return; }
  git add -A
  git diff --cached --quiet || git commit -qm "Update engine and website data" || return
  branch=$(git branch --show-current)
  printf '\n  Push %s to GitHub main (updates the live site)? [y/N] ' "$branch"
  read -r ok
  case "$ok" in y|Y|yes) ;; *) echo "  Not published (committed locally)."; return;; esac
  git push origin "$branch:main" "$branch" && {
    echo; echo "  Pushed. The site updates in about a minute."; }
}

show_menu() {
while :; do
  clear
  cat <<'EOF'

   पाणिनि-यन्त्रम् — Pāṇini Engine

   1  Start the local apps    Lab · Practice · Review · Learn · full UI   [Enter]
   2  Open the local home     (servers must already be running)

   3  Run all tests
   4  Verb accuracy          vs ashtadhyayi.com (455k forms, ~2 min)
   5  Noun accuracy          vs ashtadhyayi.com (215k forms)
   6  Derivation paths       our sūtras vs theirs (4.8k noun forms)
   7  Download ashtadhyayi.com data   (needed once for 4–6)
   c  Coverage refresh      run suite ledger → confident list → autonomy → open /coverage
   i  It-letters of an upadeśa  which it, which sūtra, kit/ṅit/ñīt …

   8  Rebuild website data   (docs/data, local only)
   9  Publish                rebuild → test → commit → push → site updates

   0  Quit

EOF
  printf '   Choose: '
  read -r choice
  case "${choice:-1}" in
    1) start_apps ;;
    2) open "http://127.0.0.1:${API_PORT}/" ;;
    3) "$PY" -m pytest -q -p no:cacheprovider; pause ;;
    4) need_gold && "$PY" -m bench.ashtadhyayi_gold; pause ;;
    5) need_gold && "$PY" -m bench.ashtadhyayi_gold --kind subanta; pause ;;
    6) need_gold && "$PY" -m bench.ashtadhyayi_gold --kind prakriya; pause ;;
    7) "$PY" -m tools.fetch_ashtadhyayi_data; pause ;;
    c|C)
      "$PY" -m tools.firing_coverage >/dev/null 2>&1
      "$PY" -m tools.sutra_class && "$PY" -m tools.autonomy_report | tail -4
      open "http://127.0.0.1:${API_PORT}/coverage"
      pause ;;
    i|I)
      echo
      echo "  SLP1 upadeśas — dhātu id/upadeśa, or --krt / --taddhita / --sup / --tin before pratyayas"
      echo "  e.g.  qukfY wuo~Svi Bidi~r --krt Kac Rvul kvasu~ --taddhita cPaY --sup jas Sas"
      printf '  upadeśa: '
      read -r it_args
      # shellcheck disable=SC2086
      [ -n "$it_args" ] && "$PY" -m tools.it_report $it_args
      pause ;;
    8) "$PY" -m tools.build_pages && "$PY" -m tools.build_shabda_page; pause ;;
    9) publish; pause ;;
    0|q|Q) exit 0 ;;
    *) ;;
  esac
done
}

case "${1:-}" in
  menu|--menu|-m) show_menu ;;
  *) start_apps ;;
esac
