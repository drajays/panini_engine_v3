"""
2.2.3  द्वितीयतृतीयचतुर्थतुर्याण्यन्यतरस्याम्  —  VIDHI

पदच्छेदः  द्वितीय-तृतीय-चतुर्थ-तुर्याणि / अन्यतरस्याम्

अनुवृत्तिः  एकदेशिना एकाधिकरणे 2.2.1

Kāśikā summary: the ordinals *dvitīya*, *tṛtīya*, *caturtha*, *turya* —
when an *ekadeśin* meaning within an *ekādhikaraṇa* — optionally (*anyatarasya*)
compound in tatpuruṣa.  Examples: *dvitīyakāyaḥ*, *tṛtīyakāyaḥ*.

Engine (narrow, mechanically blind):
  Gate key ``2_2_3_ordinal_ekadesha_gate``.  Recipe arms
  ``state.meta['2_2_3_arm']``.  The optionality (*anyatarasya*) is modelled by
  the recipe — the gate is simply stamped when armed.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_ORDINALS = frozenset({"dvitIya", "tftIya", "caturTa", "turya"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_3_ordinal_ekadesha_gate") is True:
        return False
    return any(
        t.meta.get("ordinal_ekadesha") in _ORDINALS or "ordinal_ekadesha" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates["2_2_3_ordinal_ekadesha_gate"] = True
    state.samjna_registry["2_2_3_ordinal_ekadesha"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.3",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="dvitIya-tftIya-caturTa-turyARi anyatarasyfm",
    text_dev="द्वितीयतृतीयचतुर्थतुर्याण्यन्यतरस्याम्",
    padaccheda_dev="द्वितीय-तृतीय-चतुर्थ-तुर्याणि / अन्यतरस्याम्",
    why_dev=(
        "द्वितीयादयः एकदेशिनैकाधिकरणे विभाषा समस्यन्ते — "
        "द्वितीयकायः इत्यादि।"
    ),
    anuvritti_from=("2.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
