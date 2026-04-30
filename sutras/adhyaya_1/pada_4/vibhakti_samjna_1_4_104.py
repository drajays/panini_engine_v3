"""
**1.4.104** *supas tiṅś ca vibhaktiḥ* — *vibhakti* *sañjñā* on *sup* and *tiṅ* *pratyaya*.

Not a sūtra file.  *Śāstra:* the twenty-one *sup* *pratyaya* (**4.1.2** inventory) fall in seven triples
(*prathamā* … *saptamī* in teaching order); the eighteen *tiṅ* *ādeśa* (**3.4.78**) fall in six triples — all
are named *vibhakti*.

*Engine:* ``terms_needing_1_4_104_vibhakti`` finds *pratyaya* ``Term``s that carry ``"sup"`` (from **4.1.2**)
or whose ``upadesha_slp1`` is a *tiṅ* *ādeśa* in ``TIN_ADESHA_18`` — not *śap* / *kṛt* / *lakāra* *upadeśa*.
``cond`` uses only ``kind`` / ``tags`` / ``upadesha_slp1`` (CONSTITUTION Art. 2).

*Cross-refs:* **1.4.101**–**1.4.102** (*tiṅ* triples), **1.4.103** (*sup* triples — *śāstra*; not a separate
engine file here), **1.4.1** (*ekasañjñā*), **3.4.78**, **4.1.2**, **5.3.1** (*taddhita* *vibhakti* — other path).
"""
from __future__ import annotations

from typing import Final, Tuple

from engine.lopa_ghost import LUK_LOPA_GHOST_TAG
from engine.state import State, Term

from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import TIN_ADESHA_18, TIN_ADESHA_SET

# One *Term* tag: *sup* / *tiṅ* *ādeśa* both receive the same *sañjñā* name in *śāstra*.
TAG_1_4_104_VIBHAKTI: Final[str] = "samjna_1_4_104_vibhakti"

# Seven triples = *sup* *upadeśa* SLP1 strings (``data/inputs/sup_upadesha.json``, *vibhakti* 1–7 × *vacana*).
SUP_VIBHAKTI_TRIPLES_SLP1: Final[Tuple[Tuple[str, str, str], ...]] = (
    ("s~", "O", "jas"),
    ("am", "Ow", "Sas"),
    ("wA", "ByAm", "Bis"),
    ("Ne", "ByAm", "Byas"),
    ("Nasi", "ByAm", "Byas"),
    ("Nas", "os", "Am"),
    ("Ni", "os", "sup"),
)

SUP_VIBHAKTI_UPADESHA_SLP1: Final[frozenset[str]] = frozenset(
    p for triple in SUP_VIBHAKTI_TRIPLES_SLP1 for p in triple
)

# Six triples of *tiṅ* *ādeśa* in **3.4.78** order.
TIN_VIBHAKTI_TRIPLES_SLP1: Final[Tuple[Tuple[str, str, str], ...]] = tuple(
    tuple(TIN_ADESHA_18[i : i + 3]) for i in range(0, len(TIN_ADESHA_18), 3)
)


def _norm_upadesha_slp1(s: str) -> str:
    t = s.strip()
    if t in TIN_ADESHA_SET or t in SUP_VIBHAKTI_UPADESHA_SLP1:
        return t
    if t.endswith("~"):
        u = t[:-1]
        if u in TIN_ADESHA_SET or u in SUP_VIBHAKTI_UPADESHA_SLP1:
            return u
    return t


def is_sup_vibhakti_pratyaya(t: Term) -> bool:
    """``Term`` tagged ``sup`` by **4.1.2** (or compatible loaders)."""
    if t.kind != "pratyaya" or "sup" not in t.tags:
        return False
    # **2.4.71** *luk* leaves a zero-width *sup* ghost — not a *vibhakti* bearer.
    return LUK_LOPA_GHOST_TAG not in t.tags


# **3.4.101** *tas* → **tām** in *laṅ* / *lit* … — surface *tiṅ* not in ``TIN_ADESHA_18``.
TIN_SURFACE_AADESHA_SLP1_EXTRA: Final[frozenset[str]] = frozenset({"tAm"})


def is_tin_vibhakti_pratyaya(t: Term) -> bool:
    """*Tiṅ* *ādeśa* replacers of *lac* only (**3.4.78**), not *śap* / *śyan* / *lakāra* *upadeśa*."""
    if t.kind != "pratyaya":
        return False
    up = _norm_upadesha_slp1(t.meta.get("upadesha_slp1") or "")
    if up in TIN_ADESHA_SET:
        return True
    return up in TIN_SURFACE_AADESHA_SLP1_EXTRA and "tin_adesha_3_4_78" in t.tags


def term_has_1_4_104_vibhakti(t: Term) -> bool:
    return TAG_1_4_104_VIBHAKTI in t.tags


def terms_needing_1_4_104_vibhakti(state: State) -> list[Term]:
    out: list[Term] = []
    for t in state.terms:
        if term_has_1_4_104_vibhakti(t):
            continue
        if is_sup_vibhakti_pratyaya(t) or is_tin_vibhakti_pratyaya(t):
            out.append(t)
    return out
