"""
Tripāḍī helpers for 8.2.x rules that read a dhātu inside the pada.

The tape is read flat across terms (pre- or post-merge alike). A varṇa belongs
to the dhātu when its term is a (non-abhyāsa) dhātu, or — after the pada merge —
when it carries the dhātu's own varṇa tag (``dhatu_v`` / ``mula_dhatu_v``).
"""
from __future__ import annotations

from engine.state import State

JHAL = frozenset("kKgGcCjJwWqQtTdDpPbBSzsh")
JHAS = frozenset("GJQDB")                     # झष्: the voiced aspirates
BAS_TO_BHAS = {"b": "B", "g": "G", "q": "Q", "d": "D"}
AC = frozenset("aAiIuUfFxXeEoO")


def flat(state: State) -> list[tuple]:
    """[(term, index, is_dhatu_varna)] in tape order."""
    out = []
    for t in state.terms:
        # varṇa-level marks, when the term has them, are finer than its tag (a
        # merged sanādyanta or pada holds abhyāsa + root + pratyaya together)
        mula = any("mula_dhatu_v" in v.tags for v in t.varnas)   # the root itself
        fine = mula or any("dhatu_v" in v.tags for v in t.varnas)
        in_dhatu = "dhatu" in t.tags and "abhyasa" not in t.tags and not fine
        for i, v in enumerate(t.varnas):
            mine = ("dhatu_adesha_v" in v.tags
                    or (("mula_dhatu_v" in v.tags) if mula else ("dhatu_v" in v.tags)))
            out.append((t, i, "abhyasa" not in t.tags and "abhyasa_v" not in v.tags
                        and (in_dhatu or mine)))
    return out


def slp(cell) -> str:
    t, i, _ = cell
    return t.varnas[i].slp1


def dhatu_span(cells, k: int) -> tuple[int, int] | None:
    """(start, end) of the dhātu run containing position k, inclusive."""
    if not cells[k][2]:
        return None
    a = k
    while a > 0 and cells[a - 1][2]:
        a -= 1
    b = k
    while b + 1 < len(cells) and cells[b + 1][2]:
        b += 1
    return a, b


def followed_by_jhal_or_end(cells, k: int) -> bool:
    """झलि / पदान्ते: the next varṇa is a jhal, or there is none."""
    return k + 1 >= len(cells) or slp(cells[k + 1]) in JHAL


def substitute(cell, new_slp1: str) -> None:
    """Replace the varṇa at ``cell`` by an ādeśa that stays part of the dhātu
    (sthānivat for span purposes); the mūla-upadeśa mark is not carried over."""
    from phonology import mk
    t, i, _ = cell
    old = t.varnas[i]
    v = mk(new_slp1)
    if old.tags & {"dhatu_v", "mula_dhatu_v", "dhatu_adesha_v"}:
        v.tags.add("dhatu_v")
        v.tags.add("dhatu_adesha_v")   # an ādeśa inside the root is still the root
    t.varnas[i] = v
