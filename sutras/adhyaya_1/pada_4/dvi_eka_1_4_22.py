"""
**1.4.22** *dvi-ekayoḥ divivacana-ekavacane* — *niyama* helper for *dvi* / *eka* *sup* and *tiṅ* *ādeśa*.

Not a sūtra file.  *Śāstra (laghu):* for denoting *dva* (two) use *divivacana* *pratyaya*; for *eka* (one) use
*ekavacana* *pratyaya* ( **1.4.102** for *tiṅ*; **1.4.103** for *sup* ).  This is a *niyama* of *vivakṣā* — the
engine does not count referents; the recipe sets ``1_4_22_affix_class`` on the primary *dhātu* *Term* to
``\"dvi\"`` or ``\"eka\"`` so *paribhāṣā* *gates* line up with **1.4.102** *tags* and *sup* choice.

*Cross-refs:* **1.2.63** ( *dvi* for *bahutva* in *nakṣatra-dvandva* — *śāstra* only here), **1.4.1** ( *ekasañjñā* ).
"""
from __future__ import annotations

from typing import Final, Literal

from engine.state import State, Term

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import find_primary_dhatu

GATE_KEY: Final[str] = "prayoga_1_4_22_dvi_eka_affix_niyama"

# ``"dvi"`` ⇒ *divivacana*; ``"eka"`` ⇒ *ekavacana* — not *meta['vacana']* (CONSTITUTION Art. 2).
NIMITTA_VALUES: Final[tuple[str, ...]] = ("dvi", "eka")
DVI_EKA_NIMITTA_KEY: Final[str] = "1_4_22_affix_class"

def dvi_eka_22_licences(state: State) -> bool:
    g = state.paribhasha_gates.get(GATE_KEY, {})
    if g.get("active") is not True:
        return False
    return g.get("nimitta") in NIMITTA_VALUES


def _read_nimitta(d: Term) -> Literal["dvi", "eka"] | None:
    v = d.meta.get(DVI_EKA_NIMITTA_KEY)
    if v == "dvi" or v == "eka":
        return v
    return None


def dvi_eka_22_gate_needs_update(state: State) -> bool:
    d = find_primary_dhatu(state)
    if d is None:
        return False
    n = _read_nimitta(d)
    if n is None:
        return False
    cur = state.paribhasha_gates.get(GATE_KEY, {})
    if cur.get("nimitta") == n and cur.get("active") is True:
        return False
    return True
