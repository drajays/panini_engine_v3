"""
**1.4.102** *tāni trīṇi trīṇi tiṅaḥ … ekavacana-dvivacana-bahuvacanāni ekaśaḥ* — *tiṅ* *vacana* triples.

Not a sūtra file.  Within each *puruṣa* triplet from **1.4.101** (three *tiṅ* *ādeśa* in **3.4.78** order),
the first, second, and third receive *ekavacana*, *dvivacana*, *bahuvacana* respectively (*ekaśaḥ* =
one-by-one).

*Cross-refs:* **1.4.101** ( *prathama* / *madhyama* / *uttama* triples ), **1.4.1** ( *eka*‑*sañjñā* ),
**1.4.104** (*vibhakti* of *tiṅ* — separate).
"""
from __future__ import annotations

from typing import Final, Tuple

from engine.state import State, Term

from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import TIN_ADESHA_18, TIN_ADESHA_SET

# *Term* tags (no ``meta['vacana']``; CONSTITUTION Art. 2 *cond* scan on *sūtra* files).
TIN_102_TAG_EKA: Final[str] = "tin_102_ekavacana"
TIN_102_TAG_DVI: Final[str] = "tin_102_dvivacana"
TIN_102_TAG_BAHU: Final[str] = "tin_102_bahuvacana"

TIN_102_VACANA_ORDER: Final[Tuple[str, str, str]] = (TIN_102_TAG_EKA, TIN_102_TAG_DVI, TIN_102_TAG_BAHU)
TIN_102_ALL_VACANA_TAGS: Final[frozenset[str]] = frozenset(TIN_102_VACANA_ORDER)


def _normalise_tin_adesha_slp1(s: str) -> str:
    t = s.strip()
    if t in TIN_ADESHA_SET:
        return t
    if t.endswith("~") and t[:-1] in TIN_ADESHA_SET:
        return t[:-1]
    return t


def vacana_102_tag_for_tin_adesha(s: str) -> str | None:
    """Return the *1.4.102* *vacana* *tag* for a normalised *tiṅ* *ādeśa* *upadeśa*, or *None*."""
    key = _normalise_tin_adesha_slp1(s)
    if key not in TIN_ADESHA_SET:
        return None
    i = TIN_ADESHA_18.index(key)
    return TIN_102_VACANA_ORDER[i % 3]


def tin_vacana_102_is_registered(t: Term) -> bool:
    return bool(t.tags & TIN_102_ALL_VACANA_TAGS)


def terms_needing_tin_102_vacana(state: State) -> list[Term]:
    out: list[Term] = []
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if vacana_102_tag_for_tin_adesha(up) is None:
            continue
        if tin_vacana_102_is_registered(t):
            continue
        out.append(t)
    return out
