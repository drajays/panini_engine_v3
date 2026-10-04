"""Art. 7: one sūtra = one file = one id = one register_sutra() call.
Static (no imports), so it is cheap and cannot be fooled by import order."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "sutras"
FILES = sorted(ROOT.glob("adhyaya_*/pada_*/sutra_*.py"))


def test_identity():
    seen, bad = {}, []
    for f in FILES:
        t = f.read_text(encoding="utf-8")
        ids = re.findall(r'sutra_id\s*=\s*"([^"]+)"', t)
        fid = re.match(r"sutra_(\d+)_(\d+)_(\d+)", f.name)
        want = ".".join(fid.groups()) if fid else None
        if len(re.findall(r"\bregister_sutra\(", t)) != 1:
            bad.append(f"{f.name}: need exactly one register_sutra()")
        if set(ids) != {want}:
            bad.append(f"{f.name}: sutra_id {ids} != filename id {want}")
        if want in seen:
            bad.append(f"{f.name}: duplicate of {seen[want]}")
        seen[want] = f.name
    assert not bad, "\n".join(bad[:30])
