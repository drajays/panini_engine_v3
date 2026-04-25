"""
**1.4.101** *tiṅaḥ trīṇi trīṇi prathama-madhyam-uttamāḥ* — *tiṅ* *ādeśa* grouped by non-person triples.

Not a sūtra file.  The eighteen SLP1 keys follow ``TIN_ADESHA_18`` (**3.4.78**), taken in
order: three *prathama*, three *madhyama*, three *uttama* ( *parasmaipada* block ), then the
same *triplet of triplets* ( *ātmanepada* block ).

*Cross-refs:* **1.4.102** (*vacana* in triples), **1.4.1** ( *eka*‑*sañjñā* ); **2.4.85**, **1.4.108** ( *prathama* ),
**1.4.105** ( *madhyama* ), **1.4.106**–**1.4.107**, **3.4.98**, **3.4.92**, **7.1.91** ( *uttama* in other
sūtras) — *śāstra* usage only, not re-derived here.
"""
from __future__ import annotations

from typing import Final, Tuple

from engine.state import State, Term

from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import TIN_ADESHA_18, TIN_ADESHA_SET

# Distinct *Term* tags (avoid ``'puruṣa'`` as a *meta* key; CONSTITUTION Art. 2 *cond* scan).
TIN_101_TAG_TRIPARTITE_A: Final[str] = "tin_101_tripartite_A"  # प्रथम (first triple in each *pari*)
TIN_101_TAG_TRIPARTITE_B: Final[str] = "tin_101_tripartite_B"  # मध्यम
TIN_101_TAG_TRIPARTITE_C: Final[str] = "tin_101_tripartite_C"  # उत्तम

# Human-readable (trace / UIs): *prathama* = A, *madhyama* = B, *uttama* = C in each block of nine.
TIN_101_TRIPARTITE: Final[Tuple[str, str, str]] = (
    TIN_101_TAG_TRIPARTITE_A,
    TIN_101_TAG_TRIPARTITE_B,
    TIN_101_TAG_TRIPARTITE_C,
)
TIN_101_ALL_TRIPARTITE_TAGS: Final[frozenset[str]] = frozenset(TIN_101_TRIPARTITE)


def _normalise_tin_adesha_slp1(s: str) -> str:
    t = s.strip()
    if t in TIN_ADESHA_SET:
        return t
    if t.endswith("~") and t[:-1] in TIN_ADESHA_SET:
        return t[:-1]
    return t


def tripartite_101_tag_for_tin_adesha(s: str) -> str | None:
    """Return the *tiṅ* *tripartite* *tag* for a normalised *ādeśa* *upadeśa* string, or *None*."""
    key = _normalise_tin_adesha_slp1(s)
    if key not in TIN_ADESHA_SET:
        return None
    i = TIN_ADESHA_18.index(key)
    return TIN_101_TRIPARTITE[i // 3 % 3]


def tin_tripartite_101_is_registered(t: Term) -> bool:
    return bool(t.tags & TIN_101_ALL_TRIPARTITE_TAGS)


def terms_needing_tin_101_tripartite(state: State) -> list[Term]:
    out: list[Term] = []
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if tripartite_101_tag_for_tin_adesha(up) is None:
            continue
        if tin_tripartite_101_is_registered(t):
            continue
        out.append(t)
    return out
