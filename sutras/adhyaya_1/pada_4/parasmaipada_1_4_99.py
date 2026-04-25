"""
**1.4.99** *lakārāpāda* — inventory of *ādeśa* that carry the *parasmaipada* *sañjñā*.

This is not a sūtra file.  It lists the SLP1 ``upadesha_slp1`` keys used by
``sutra_1_4_99`` to mark a *pratyaya* *Term*.

*Śāstra flow (narrative, not re-derived at runtime here):* **1.4.99** *l̥ parasmaipadam* plus
*anuvṛtti* of **1.4.1** (ā kaḍārād ekā sañjñā) assigns *parasmaipadam* to *lakāra*‑sthāni
*ādeśa* in a broad set; **1.4.100** (*taṅān āv ātmanepadam*) *bādhate* a part of that for
*ātmanepada* under *eka*‑*sañjñā* *adhikāra*.

**Engine (laghu):** we register only the *eleven* *ādeśa* types that **remain** *parasmaipadīya*
in the *śāstrīya* net: the nine *tiṅ* items from **3.4.78** (*tip* … *mas*), *śatṛ* from
**3.2.124**, and *kvasu* from **3.2.107** — the same set the *śikṣā* text identifies as
finally *parasmaipada* (complement of **1.4.100** *ātmanepada* set; see ``sutra_1_4_100``).

*Cross-refs (not all implemented as separate sūtra modules):* **1.3.7**, **1.3.8**; **7.2.1**,
**1.3.78**, **3.4.82** (downstream *vidhi* on *parasmaipada* *prakāra*), **3.1.1** (global
*pratyaya* *ārambha*).
"""
from __future__ import annotations

from typing import Final, FrozenSet, Tuple

from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import TIN_ADESHA_18

# First nine of **3.4.78** = *parasmaipadīya* *tiṅ* (see ``TIN_ADESHA_18`` order) + *śatṛ* (3.2.124) + *kvasu* (3.2.107).
# SLP1 follows ``phonology.varna`` (``T``/``Ta``/…).
_PARASMAI_TIN9: Final[Tuple[str, ...]] = TIN_ADESHA_18[:9]
PARASMAI_UPADESHA_SLP1: Final[FrozenSet[str]] = (
    frozenset(_PARASMAI_TIN9) | frozenset({"Satf", "kvasu"})
)


def is_parasmaipada_upadesha_slp1(s: str) -> bool:
    t = s.strip()
    if t in PARASMAI_UPADESHA_SLP1:
        return True
    if t.endswith("~") and t[:-1] in PARASMAI_UPADESHA_SLP1:
        return True
    return False
