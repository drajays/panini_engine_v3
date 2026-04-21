"""
7.1.24  अतोऽम्  —  VIDHI

Operational role (v3.6, napuṃsaka a-stems):
  For an **a-ending napuṃsaka aṅga**, the sup upadeśas **su** (1-1 / 8-1)
  and **am** (2-1) yield **am**.

We implement as: if aṅga is tagged `napuṃsaka` and ends in 'a', and the
pratyaya upadeśa is either 's~' (su) or 'am', replace the pratyaya varṇas
with 'a' 'm' and set upadeśa identity to 'am'.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


# Only su (s~) needs conversion. The am upadeśa is already am; applying
# a VIDHI that leaves the form unchanged would violate R1.
_TARGETS = frozenset({"s~"})


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "napuṃsaka" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if "sambuddhi" in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") not in _TARGETS:
        return False
    if pr.meta.get("ato_am_done"):
        return False
    if not anga.varnas:
        return False
    if anga.varnas[-1].slp1 != "a":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    pr.varnas = [mk("a"), mk("m")]
    pr.meta["ato_am_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", pr.meta.get("upadesha_slp1"))
    pr.meta["upadesha_slp1"] = "am"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.24",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ataH am (napuMsake)",
    text_dev       = "अतोऽम्",
    padaccheda_dev = "अतः अम्",
    why_dev        = "अकारान्त-नपुंसक-अङ्गात् परस्य सुँ/अम्-प्रत्ययस्य ‘अम्’-आदेशः (ज्ञानम्)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

