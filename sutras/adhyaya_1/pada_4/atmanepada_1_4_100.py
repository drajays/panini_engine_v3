"""
**1.4.100** *lakārāpāda* — inventory of *ādeśa* that carry the *ātmanepada* *sañjñā*.

Not a sūtra file.  Lists SLP1 ``upadesha_slp1`` keys for ``sutra_1_4_100``.

*Śāstra:* **1.4.100** *l̥ taṅānāv ātmanepadam* with *anuvṛtti* of **1.4.99** (*l̥*) and **1.4.1**
(*eka*‑*sañjñā*).  The *taṅ* block (nine *tiṅ* *ādeśa* from the second half of **3.4.78**)
plus *śānac* / *kānac* (**3.2.124**, **3.2.106**) — *ānau* — get *ātmanepadam* and *bādhate*
*parasmaipadam* from **1.4.99** for these *lakārāpāda* items (*cānaś* etc., not standing for
*lac*, is excluded by the *l̥* *anuvṛtti* in the *śāstra*; we encode only *upadeśa* keys that
the engine treats as *lakārāsthāni* *ādeśa*).

*Cross-refs:* **1.3.12**, **7.1.5**, **2.4.44** (downstream *vidhi*).
"""
from __future__ import annotations

from typing import Final, FrozenSet, Tuple

from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import TIN_ADESHA_18

# Last nine of **3.4.78** = *taṅ* block (*ta* … *mahiG*) + *śānac* + *kānac*.
_ATMANE_TIN9: Final[Tuple[str, ...]] = TIN_ADESHA_18[9:]
ATMANE_UPADESHA_SLP1: Final[FrozenSet[str]] = (
    frozenset(_ATMANE_TIN9) | frozenset({"SAnac", "kAnac"})
)


def is_atmanepada_upadesha_slp1(s: str) -> bool:
    t = s.strip()
    if t in ATMANE_UPADESHA_SLP1:
        return True
    if t.endswith("~") and t[:-1] in ATMANE_UPADESHA_SLP1:
        return True
    return False
