#!/bin/sh
# tools/make_mac_app.sh — build "Panini Engine.app" (macOS) that opens "Panini Engine.command" in Terminal.
#
#   sh tools/make_mac_app.sh            # → ~/Applications/Panini Engine.app  (drag it to the Dock)
#   sh tools/make_mac_app.sh /path/dir  # → /path/dir/Panini Engine.app
#
# The app holds only the repo path; the engine, data and servers stay in the repo.
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-$HOME/Applications}"
APP="$DEST/Panini Engine.app"
mkdir -p "$DEST"
rm -rf "$APP"

osacompile -o "$APP" <<EOF
on run
	set launcher to "$REPO/Panini Engine.command"
	tell application "Terminal"
		activate
		do script quoted form of launcher
	end tell
end run
EOF

# Icon: "पा" on saffron (Pillow + iconutil); the app works without it.
PY="$REPO/.venv/bin/python3"; [ -x "$PY" ] || PY=python3
TMP="$(mktemp -d)"
if "$PY" - "$TMP/icon.iconset" <<'PYEOF'
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
out = Path(sys.argv[1]); out.mkdir()
def tile(px):
    img = Image.new("RGBA", (px, px), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, px - 1, px - 1), radius=px // 5, fill=(232, 120, 23, 255))
    font = ImageFont.truetype("/System/Library/Fonts/Kohinoor.ttc", int(px * 0.55))
    d.text((px / 2, px / 2), "पा", font=font, fill=(255, 250, 240, 255), anchor="mm")
    return img
for base in (16, 32, 128, 256, 512):          # the iconutil set: NxN and NxN@2x
    tile(base).save(out / f"icon_{base}x{base}.png")
    tile(base * 2).save(out / f"icon_{base}x{base}@2x.png")
PYEOF
then
  iconutil -c icns "$TMP/icon.iconset" -o "$APP/Contents/Resources/applet.icns"
  rm -f "$APP/Contents/Resources/Assets.car"                      # else the default script icon wins
  plutil -remove CFBundleIconName "$APP/Contents/Info.plist" 2>/dev/null || true
  plutil -replace CFBundleIconFile -string applet "$APP/Contents/Info.plist"
  codesign --force --deep -s - "$APP" 2>/dev/null || true
  touch "$APP"
fi
rm -rf "$TMP"
echo "built: $APP"
