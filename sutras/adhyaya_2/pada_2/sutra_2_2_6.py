"""
2.2.6  नञ्  —  VIDHI

पदच्छेदः  नञ्

अनुवृत्तिः  (समास 2.1.3; सुप्सुपा 2.1.4)

Kāśikā summary: the negative particle *na* (realized as *a-* / *an-* before
vowels) compounds with any *prātipadika* to form a tatpuruṣa of negation —
the *nanñ-tatpuruṣa*.  Examples: *a-brahmaṇaḥ* → *abrāhmaṇaḥ*,
*an-aśvaḥ* → *anaśvaḥ*.

Engine (narrow, mechanically blind):
  Gate key ``2_2_6_nan_gate``.  Recipe arms ``state.meta['2_2_6_arm']``
  and tags a Term with ``nan_negative`` indicating the nañ compound context.
  The gate is raised on first fire; registry stamp records the formation.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_6_nan_gate") is True:
        return False
    if not state.meta.get("2_2_6_arm"):
        return False
    return any("nan_negative" in t.tags for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    state.paribhasha_gates["2_2_6_nan_gate"] = True
    state.samjna_registry["2_2_6_nan_tatpurusa"] = True
    state.meta.pop("2_2_6_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.6",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="naY",
    text_dev="नञ्",
    padaccheda_dev="नञ्",
    why_dev=(
        "नञ् सुबन्तेन समस्यते — अब्राह्मणः, अनश्वः इत्यादि नञ्-तत्पुरुषः।"
    ),
    anuvritti_from=("2.1.3", "2.1.4"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
