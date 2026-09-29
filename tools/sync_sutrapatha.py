"""
tools/sync_sutrapatha.py — make every sūtra file quote Pāṇini's own text.

The sūtrapāṭha (ashtadhyayi.com ``sutraani/data.txt``, pinned, fetched by
``tools.fetch_ashtadhyayi_data``) is lexical data like the dhātupāṭha: it is
what the sūtra *says*. This tool rewrites each registered sūtra's ``text_dev``
and ``text_slp1`` fields (found by AST, so docstrings and code are untouched)
and the id line of the module docstring. It never touches cond()/act().

    python3 -m tools.sync_sutrapatha            # report only
    python3 -m tools.sync_sutrapatha --write    # rewrite the files
"""
from __future__ import annotations

import argparse
import ast
import inspect
import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tools.fetch_ashtadhyayi_data import path as ref_path  # noqa: E402

_NOISE = re.compile(r"[\s‌‍ऽ'’।॥.,\-–—]")


def norm(s: str | None) -> str:
    return _NOISE.sub("", s or "")


def patha() -> dict[str, str]:
    rows = json.loads(ref_path("sutraani/data.txt").read_text())["data"]
    return {f"{r['a']}.{r['p']}.{r['n']}": r["s"].strip() for r in rows}


def slp1(dev: str) -> str:
    from phonology.tokenizer import devanagari_to_slp1_flat
    return " ".join(devanagari_to_slp1_flat(w) for w in dev.replace("ऽ", "'").split())


def _field_nodes(tree: ast.AST, name: str):
    """String-valued ``name=...`` keywords and ``"name": ...`` dict entries."""
    for node in ast.walk(tree):
        if isinstance(node, ast.keyword) and node.arg == name:
            yield node.value
        elif isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and k.value == name:
                    yield v


def _replace_nodes(src: str, repl: list[tuple[ast.AST, str]]) -> str:
    lines = src.splitlines(keepends=True)
    offs = [0]
    for ln in lines:
        offs.append(offs[-1] + len(ln))
    b = src.encode()
    # byte offsets (ast col offsets are utf-8 byte based)
    lb = [0]
    for ln in lines:
        lb.append(lb[-1] + len(ln.encode()))
    spans = sorted(((lb[n.lineno - 1] + n.col_offset, lb[n.end_lineno - 1] + n.end_col_offset, t)
                    for n, t in repl), reverse=True)
    for s, e, t in spans:
        b = b[:s] + t.encode() + b[e:]
    return b.decode()


def sync(write: bool) -> int:
    import sutras  # noqa: F401 — registers every sūtra
    from engine.registry import SUTRA_REGISTRY as REG

    ref = patha()
    changed = 0
    for sid, rec in sorted(REG.items()):
        want = ref.get(sid)
        if want is None or (norm(rec.text_dev) == norm(want) and rec.text_slp1 == slp1(want)):
            continue
        fn = rec.cond or rec.act
        f = Path(inspect.getsourcefile(fn)) if fn else None
        if f is None or not f.name.startswith("sutra_"):
            print(f"  ? {sid}: no module file")
            continue
        src = f.read_text()
        tree = ast.parse(src)
        repl = [(n, repr(want)) for n in _field_nodes(tree, "text_dev")]
        repl += [(n, repr(slp1(want))) for n in _field_nodes(tree, "text_slp1")]
        if not repl:
            print(f"  ? {sid}: no text_dev field in {f.name}")
            continue
        new = _replace_nodes(src, repl)
        # module docstring id line: "6.1.66  <old text>  —  TYPE"
        new = re.sub(rf'^(\s*{re.escape(sid)}\s+)(.+?)(\s+—)', lambda m: m.group(1) + want + m.group(3),
                     new, count=1, flags=re.M)
        print(f"  {sid}: {rec.text_dev!r} → {want!r}")
        changed += 1
        if write:
            f.write_text(new)
    print(f"{changed} sūtra texts {'rewritten' if write else 'differ'}")
    return 0


def patha_classes() -> dict[str, set[str]]:
    """Sūtra id → its lakṣaṇa classes in the pāṭha: V, S, P, AT, AD."""
    rows = json.loads(ref_path("sutraani/data.txt").read_text())["data"]
    return {f"{r['a']}.{r['p']}.{r['n']}": {t.split("$")[0] for t in r["type"].split("##")} for r in rows}


# Where the tradition classes a sūtra differently from ashtadhyayi.com's type
# field, the tradition wins; each entry names its source.
TYPE_OVERRIDES = {
    "1.1.6":  ("PRATISHEDHA", "न from 1.1.4 by anuvṛtti — Kāśikā: दीधीवेवीटां गुणवृद्धी न भवतः"),
    "1.1.69": ("PARIBHASHA", "Siddhānta Kaumudī, paribhāṣā-prakaraṇa"),
    "1.1.70": ("PARIBHASHA", "Siddhānta Kaumudī, paribhāṣā-prakaraṇa"),
    "1.1.72": ("PARIBHASHA", "Siddhānta Kaumudī, paribhāṣā-prakaraṇa (तदन्तविधि)"),
    "4.2.92": ("ADHIKARA", "Kāśikā: शेष इत्यधिकारोऽयम् (to 4.3.134)"),
}


def _is_nisedha(sid, rec) -> bool:
    from tools.sutra_lint import _is_nisedha as f
    return f(sid, rec)


def type_mismatches():
    """(sid, record, wanted SutraType) where the engine's core class contradicts
    the pāṭha. Niyama/pratiṣedha/vibhāṣā/nipātana/anuvāda are refinements of any
    class and are left alone."""
    import sutras  # noqa: F401
    from engine.registry import SUTRA_REGISTRY as REG
    from engine.sutra_type import SutraType as T
    core = {"V": T.VIDHI, "S": T.SAMJNA, "P": T.PARIBHASHA, "AT": T.ATIDESHA, "AD": T.ADHIKARA}
    modal = {T.NIYAMA, T.PRATISHEDHA, T.VIBHASHA, T.NIPATANA, T.ANUVADA}
    out = []
    for sid, cs in sorted(patha_classes().items()):
        rec = REG.get(sid)
        if rec is None:
            continue
        if sid in TYPE_OVERRIDES:
            want = T[TYPE_OVERRIDES[sid][0]]
            if rec.sutra_type is not want:
                out.append((sid, rec, want))
            continue
        if rec.sutra_type in modal:
            continue
        allowed = {core[c] for c in cs}
        if rec.sutra_type not in allowed:
            order = ("V", "S", "AT", "P", "AD")
            want = core[next(c for c in order if c in cs)]
            if want is T.VIDHI and _is_nisedha(sid, rec):
                want = T.PRATISHEDHA          # a न-sūtra is a pratiṣedha, not a plain vidhi
            out.append((sid, rec, want))
        elif rec.sutra_type is T.VIDHI and _is_nisedha(sid, rec) and not rec.blocks_sutra_ids:
            out.append((sid, rec, T.PRATISHEDHA))
    return out


def sync_types(write: bool) -> int:
    n = 0
    for sid, rec, want in type_mismatches():
        f = Path(inspect.getsourcefile(rec.cond or rec.act))
        src = f.read_text()
        nodes = list(_field_nodes(ast.parse(src), "sutra_type"))
        if len(nodes) != 1:
            print(f"  ? {sid}: {len(nodes)} sutra_type fields")
            continue
        print(f"  {sid}: {rec.sutra_type.name} → {want.name}")
        n += 1
        if write:
            f.write_text(_replace_nodes(src, [(nodes[0], f"SutraType.{want.name}")]))
    print(f"{n} sūtra types {'rewritten' if write else 'differ'}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--types", action="store_true", help="sync sūtra types instead of texts")
    a = ap.parse_args(argv)
    return sync_types(a.write) if a.types else sync(a.write)


if __name__ == "__main__":
    raise SystemExit(main())
