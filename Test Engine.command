#!/bin/sh
# ─────────────────────────────────────────────────────────────────
# Pāṇini Engine — double-click test menu (macOS).
# Derive any verb form through the rule loop and see every sūtra step,
# check the Kāśikā forms fixed on 2026-10-18, or run the test suites.
# ─────────────────────────────────────────────────────────────────
cd "$(dirname "$0")" || exit 1

PY=""
for cand in .venv/bin/python3 python3; do
  if [ -x "$cand" ] || command -v "$cand" >/dev/null 2>&1; then PY="$cand"; break; fi
done
[ -z "$PY" ] && { echo "python3 not found — install it from python.org"; read -r _; exit 1; }
"$PY" -c 'import pytest' 2>/dev/null || "$PY" -m pip install -q pytest

pause() { printf '\n  Press Enter to return to the menu… '; read -r _; }

derive() {
  cat <<'EOF'

  Dhātu: upadeśa as in the dhātupāṭha (BU, vasa~, jana~, mfjU~ …) or a row id (BvAdi_01_0001)
  Lakāra: laT liT luT lRT loT laG liG AsIrliG luG lRG
  Puruṣa: 3 prathama · 2 madhyama · 1 uttama      Vacana: 1 eka · 2 dvi · 3 bahu
  Pada (only for an ubhayapadī root): parasmai | atmane | blank
EOF
  printf '  dhātu: ';  read -r D
  printf '  lakāra [laT]: '; read -r L; [ -z "$L" ] && L=laT
  printf '  puruṣa [3]: '; read -r P; [ -z "$P" ] && P=3
  printf '  vacana [1]: '; read -r V; [ -z "$V" ] && V=1
  printf '  pada []: '; read -r PD
  echo
  "$PY" -m tools.derive_trace "$D" "$L" "$P" "$V" $PD
}

while :; do
  clear 2>/dev/null
  cat <<'EOF'

  पाणिनि-यन्त्रम् — परीक्षा (test menu)

   1  Derive a verb form — every sūtra step (autonomous loop, no recipe)
   2  Kāśikā check — 30 forms from the brain's ENGINE_FINDINGS (loop vs Kāśikā)
   3  Quick tests — AMENDMENT 25, Phase-1 forms, 7.3.88 (≈1 min)
   4  Full test suite (≈7–13 min)
   5  Start the web UI (opens the usual launcher)
   q  Quit

EOF
  printf '  choose: '; read -r c
  case "$c" in
    1) derive; pause ;;
    2) "$PY" -m tools.findings_probe; pause ;;
    3) "$PY" -m pytest -q -p no:cacheprovider tests/constitutional/test_amendment_25_vivaksha.py \
         tests/regression/test_findings_probe_loop.py tests/unit/test_7_3_88_bhusuvos_tini.py; pause ;;
    4) "$PY" -m pytest -q -p no:cacheprovider tests/; pause ;;
    5) exec sh "./Panini Engine.command" ;;
    q|Q) exit 0 ;;
  esac
done
