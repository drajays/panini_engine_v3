"""
7.1.17  जसः शी  —  VIDHI

For adant sarvanāma aṅgas (e.g. sarva), the sup upadeśa **jas**
(prathamā-pl / sambuddhi-pl) is replaced by **śī**.

In v3, we represent this as pratyaya varṇas: S + I.
The initial S is cuṭu-it (1.3.7) and will be removed by 1.3.9 when
the recipe re-fires the it-prakaraṇa after this substitution.

After S is deleted, the boundary a + I is resolved by 6.1.87 (guṇa) to
produce final 'e' (sarve).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "sarvanama" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "jas":
        return False
    if pr.meta.get("jas_to_SI_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    pr.varnas = [mk("S"), mk("I")]
    pr.meta["jas_to_SI_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "jas")
    pr.meta["upadesha_slp1"] = "SI"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.17",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "jasaH SI",
    text_dev       = "जसः शी",
    padaccheda_dev = "जसः शी",
    why_dev        = "अदन्त-सर्वनाम-अङ्गात् परस्य जस्-प्रत्ययस्य ‘शी’-आदेशः (सर्वे)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

