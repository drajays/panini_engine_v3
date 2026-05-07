"""
3.3.115  ल्युट् च  —  ANUVADA (narrow **corrected-v2 P006**)

**Pāṭha:** *lyuṭ ca* — *lyuṭ* is taught (among other affixes) in *bhāva* and
related senses.

Engine role: trace-only stamp on the **चिञ्** → *cayana* (*lyuṭ*) spine when the
recipe arms ``corrected_v2_P006_3_3_115_arm`` (CONSTITUTION Art. 7).  Affixation
still proceeds via **3.4.68** + **3.1.133** (*lyuw*).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

META_ARM = "corrected_v2_P006_3_3_115_arm"
_DHATU_UPA = "ciY"


def _stem_slp1(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def cond(state: State) -> bool:
    if not state.meta.get(META_ARM):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    up = (t0.meta.get("upadesha_slp1") or "").strip()
    if up != _DHATU_UPA:
        return False
    return _stem_slp1(t0) == "ci"


SUTRA = SutraRecord(
    sutra_id="3.3.115",
    sutra_type=SutraType.ANUVADA,
    text_slp1="lyuw ca",
    text_dev="ल्युट् च",
    padaccheda_dev="ल्युट् च",
    why_dev="भावादौ धातोः ल्युट्-विधानम् — अनुवादः (प००६ आर्म्)।",
    anuvritti_from=("3.1.91",),
    cond=cond,
    act=None,
)

register_sutra(SUTRA)
