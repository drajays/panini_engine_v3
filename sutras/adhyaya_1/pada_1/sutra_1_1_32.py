"""
1.1.32  विभाषा जसि  —  VIBHASHA

*Śruti* (with anuvṛtti from **1.1.27**): in a *dvandva* samāsa, the
*sarvādi* → *sarvanāma*-*saṃjñā* is **optional** when the following *sup* is **jas**
(*vibhāṣā jasi*).

Engine (glass-box):
  - **1.1.31** (*dvandve ca*) is a strict NIYAMA that removes ``sarvanama`` in dvandva.
  - **1.1.32** is the optional counter-path that (optionally) restores ``sarvanama``
    on a dvandva aṅga when a *jas* *sup* follows, so **7.1.17** (*jasaḥ śī*) may apply.

Mechanical blindness (CONSTITUTION Art. 2):
  - ``cond`` reads only structural tags + *sup* identity (``upadesha_slp1``).
  - No paradigm coordinate reads.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_1.sutra_1_1_31 import TAG_DVANDVA_SAMASA

META_1_1_32_JASI_VIBHASHA: str = "1_1_32_vibhASa_jasi_sarvanama_restored"
"""Set on aṅga when **1.1.32** restores *sarvanāma* in dvandva before *jas*."""


def _eligible_pairs(state: State):
    for i in range(len(state.terms) - 1):
        anga = state.terms[i]
        pr = state.terms[i + 1]
        if "anga" not in anga.tags or "prātipadika" not in anga.tags:
            continue
        if TAG_DVANDVA_SAMASA not in anga.tags:
            continue
        if anga.meta.get(META_1_1_32_JASI_VIBHASHA):
            continue
        # We only need to restore if sarvanāma is currently absent.
        if "sarvanama" in anga.tags:
            continue
        if "sup" not in pr.tags:
            continue
        if pr.meta.get("upadesha_slp1") != "jas":
            continue
        yield anga


def cond(state: State) -> bool:
    return next(_eligible_pairs(state), None) is not None


def act(state: State) -> State:
    for anga in _eligible_pairs(state):
        anga.tags.add("sarvanama")
        anga.meta[META_1_1_32_JASI_VIBHASHA] = True
    state.samjna_registry["1_1_32_vibhASa_jasi"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.32",
    sutra_type     = SutraType.VIBHASHA,
    r1_form_identity_exempt=True,
    text_slp1      = "vibhASA jasi",
    text_dev       = "विभाषा जसि",
    padaccheda_dev = "विभाषा / जसि (द्वन्द्वे सर्वनाम-विकल्पः)",
    why_dev        = "द्वन्द्वे जस्-परतः सर्वनाम-संज्ञा विकल्पेन (७.१.१७ शी-आदेश-प्रसङ्गः)।",
    anuvritti_from = ("1.1.27", "1.1.31"),
    vibhasha_default = True,
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["META_1_1_32_JASI_VIBHASHA", "SUTRA"]

