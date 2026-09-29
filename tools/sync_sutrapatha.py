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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    return sync(ap.parse_args(argv).write)


if __name__ == "__main__":
    raise SystemExit(main())
