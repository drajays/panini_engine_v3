"""tools/speed_equal.py — digest of forms + full traces for a fixed derivation set (docs/SPEEDUP.md).

    python3 -m tools.speed_equal [out.json]     # prints a sha256; with a path, also writes the per-case digests

A speed change is accepted only if the digest is unchanged."""
import hashlib, json, sys
from pipelines.tinanta import derive

CASES = [(r, lk, pr, p, v, pada) for r, pada in (("BU", None), ("pac", None), ("SIN", "atmane"), ("vac", "parasmai"), ("kf", None), ("as", None), ("dA", None))
         for lk in ("laT", "liT", "luG", "loT", "laG", "liG", "lRT", "luT") for pr in ("kartari",) for p in (1, 2, 3) for v in (1, 3)]


def digest(st) -> str:
    form = "".join(v.slp1 for t in st.terms for v in t.varnas)
    tr = [(s.get("sutra_id"), s.get("status"), s.get("form_before"), s.get("form_after")) for s in st.trace]
    return hashlib.sha256(json.dumps([form, tr], ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    out = {}
    for c in CASES:
        try:
            out["|".join(map(str, c))] = digest(derive(c[0], c[1], c[2], c[3], c[4], **({"pada": c[5]} if c[5] else {})))
        except Exception as e:          # an engine refusal is part of the behaviour: it must stay the same
            out["|".join(map(str, c))] = "ERR " + type(e).__name__
    print(hashlib.sha256(json.dumps(out, sort_keys=True).encode()).hexdigest(), len(out), "cases")
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], "w"), indent=0)


main()
