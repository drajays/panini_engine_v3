"""
2.2.7  ईषदकृता  —  VIDHI

पदच्छेदः  ईषत् / अकृता

अनुवृत्तिः  नञ् 2.2.6 (अनुवृत्तिः); समास 2.1.3

Kāśikā summary: *īṣat* ('slightly') compounds with a past participle formed
with kṛt affix *kta* to yield a tatpuruṣa expressing incomplete action.
Examples: *īṣat-pakvaḥ* (slightly cooked), *īṣat-kṛtam* (slightly done).

Engine (narrow, mechanically blind):
  Gate key ``2_2_7_isadat_akrta_gate``.  Recipe arms
  ``state.meta['2_2_7_arm']`` and tags a Term with ``isadat_akrta``
  indicating the *īṣat* + kṛt compound context.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_7_isadat_akrta_gate") is True:
        return False
    return any("isadat_akrta" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates["2_2_7_isadat_akrta_gate"] = True
    state.samjna_registry["2_2_7_isadat_akrta"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.7",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="IzadakftA",
    text_dev="ईषदकृता",
    padaccheda_dev="ईषत् / अकृता",
    why_dev=(
        "ईषच्छब्दः कृदन्तेन समस्यते — ईषत्पक्वः, ईषत्कृतम् इत्यादि।"
    ),
    anuvritti_from=("2.1.3", "2.2.6"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
