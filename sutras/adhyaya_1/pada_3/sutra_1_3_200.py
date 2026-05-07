"""
1.3.200  (narrow — corrected-v2 **P007** *Bhajo* final **o** *it*)

**Note:** This index is an engine-local extension (does not collide with standard
**1.3.n** modules shipped here).  It marks the **o** tail of *dhātu* upadeśa
``BaYjo`` as deletable **it** so **1.3.9** can drop it **before** *halantyam*
would touch root-final **j** (after **o**, the tape is ``BaYj``).

Armed only by ``state.meta['corrected_v2_P007_BaYjo_ovarga_arm']`` (CONSTITUTION
Art. 7).  Cross-check commentary bundle / *dhātupāṭha* row *bhajo* — *anudāttet*
**o** as upadeśa anubandha.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

META_ARM = "corrected_v2_P007_BaYjo_ovarga_arm"
_UPA = "BaYjo"


def cond(state: State) -> bool:
    if not state.meta.get(META_ARM):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags or "upadesha" not in t0.tags:
        return False
    if (t0.meta.get("upadesha_slp1") or "").strip() != _UPA:
        return False
    if not t0.varnas or t0.varnas[-1].slp1 != "o":
        return False
    if "it_candidate_ovarga_anubandha" in t0.varnas[-1].tags:
        return False
    return True


def act(state: State) -> State:
    if not cond(state):
        return state
    t0 = state.terms[0]
    t0.varnas[-1].tags.add("it_candidate_ovarga_anubandha")
    state.samjna_registry[("it_ovarga_anubandha", 0, len(t0.varnas) - 1)] = frozenset({"o"})
    state.meta.pop(META_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.200",
    sutra_type=SutraType.SAMJNA,
    text_slp1="BaYjo ovarga it (P007 narrow)",
    text_dev="भञ्जो-अन्त्य-ओ इत् (प००७ संकीर्ण)",
    padaccheda_dev="भञ्जोः / अन्त्य-ओ-कारः / इत्",
    why_dev="सेटाङ्ग-उपदेशान्त्य-ओ इत्-संज्ञा — प००७; लोपः १.३.९।",
    anuvritti_from=("1.3.2",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
