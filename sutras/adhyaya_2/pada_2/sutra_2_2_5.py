"""
2.2.5  कालाः परिमाणिना  —  VIDHI

पदच्छेदः  कालाः / परिमाणिना

अनुवृत्तिः  (समास 2.1.3; द्वितीयया 2.2.4)

Kāśikā summary: time-words (*kāla*) compound with a measure-word (*parimāṇin*)
in the accusative to form a tatpuruṣa.  Examples: *māsaṃ parimāṇamasyāḥ*
→ *māsaparimāṇā* (of the duration of one month).

Engine (narrow, mechanically blind):
  Gate key ``2_2_5_kala_parimana_gate``.  Recipe arms
  ``state.meta['2_2_5_arm']`` and tags a Term with ``kala_parimana``
  indicating a time + measure compound context.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_5_kala_parimana_gate") is True:
        return False
    if not state.meta.get("2_2_5_arm"):
        return False
    return any("kala_parimana" in t.tags for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    state.paribhasha_gates["2_2_5_kala_parimana_gate"] = True
    state.samjna_registry["2_2_5_kala_parimana"] = True
    state.meta.pop("2_2_5_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.5",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="kAlAH parimARinA",
    text_dev="कालाः परिमाणिना",
    padaccheda_dev="कालाः / परिमाणिना",
    why_dev=(
        "कालवाचिनः परिमाणिना समस्यन्ते — मासपरिमाणा इत्यादि तत्पुरुषः।"
    ),
    anuvritti_from=("2.1.3", "2.2.4"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
