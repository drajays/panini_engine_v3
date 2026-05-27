"""
2.2.12  क्तेन च पूजायाम्  —  VIDHI

पदच्छेदः  क्तेन / च / पूजायाम्

अनुवृत्तिः  समानाधिकरणेन 2.2.11

Kāśikā summary: a past participle (*kta*-ending) compounds with another
*prātipadika* in a same-locus (*samāna-adhikaraṇa*) sense specifically for
expressing honour/respect (*pūjā*) — this is a karmadhāraya.
Examples: *pūjita-brāhmaṇaḥ* (the revered Brahmin), *ādṛta-sakhaḥ*
(the honoured friend).

Engine (narrow, mechanically blind):
  Gate key ``2_2_12_kta_puja_gate``.  Recipe arms
  ``state.meta['2_2_12_arm']`` and tags a Term with ``kta_puja`` indicating
  a kta-compound in the pūjā sense.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_12_kta_puja_gate") is True:
        return False
    return any("kta_puja" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates["2_2_12_kta_puja_gate"] = True
    state.samjna_registry["2_2_12_kta_puja_samasa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.12",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="ktena ca pUjAyAm",
    text_dev="क्तेन च पूजायाम्",
    padaccheda_dev="क्तेन / च / पूजायाम्",
    why_dev=(
        "क्तान्तेन च पूजार्थे समानाधिकरणे समासः — पूजितब्राह्मणः, आदृतसखः इत्यादि।"
    ),
    anuvritti_from=("2.2.11",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
