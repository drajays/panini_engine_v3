"""
2.2.2  अर्धं नपुंसकम्  —  VIDHI

पदच्छेदः  अर्धम् / नपुंसकम्

अनुवृत्तिः  एकदेशिना एकाधिकरणे 2.2.1

Kāśikā summary: *ardha* 'half' (neuter) compounds with a *prātipadika* that
denotes a whole to yield a tatpuruṣa of the nanapuṃsaka (neuter) gender —
e.g. *ardha-pippalam* (half a pepper), *ardha-māsam* (half a month).

Engine (narrow, mechanically blind):
  Gate key ``2_2_2_ardha_napumsaka_gate``.  Recipe arms
  ``state.meta['2_2_2_arm']`` and supplies a Term tagged ``ardha_napumsaka``
  preceding a *prātipadika* Term.  Gate is raised on first fire; registry
  stamp records the formation.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_2_ardha_napumsaka_gate") is True:
        return False
    return any("ardha_napumsaka" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates["2_2_2_ardha_napumsaka_gate"] = True
    state.samjna_registry["2_2_2_ardha_napumsaka"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.2",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="arDaM napuMsakam",
    text_dev="अर्धं नपुंसकम्",
    padaccheda_dev="अर्धम् / नपुंसकम्",
    why_dev=(
        "अर्धं नपुंसकं सुबन्तेन समस्यते — अर्धपिप्पलम्, अर्धमासम् इत्यादि।"
    ),
    anuvritti_from=("2.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
