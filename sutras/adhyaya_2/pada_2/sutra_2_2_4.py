"""
2.2.4  प्राप्तापन्ने च द्वितीयया  —  VIDHI

पदच्छेदः  प्राप्त-आपन्ने / च / द्वितीयया

अनुवृत्तिः  (समास 2.1.3)

Kāśikā summary: *prāpta* ('reached') and *āpanna* ('fallen into') compound
with an accusative (*dvitīyā*) subanta to form a tatpuruṣa.  Examples:
*grāmaṃ prāptaḥ* → *grāmaprāptaḥ*, *āpadamāpannaḥ* → *āpadāpannaḥ*.

Engine (narrow, mechanically blind):
  Gate key ``2_2_4_prapta_apanne_gate``.  Recipe arms
  ``state.meta['2_2_4_arm']`` and tags a Term with ``prapta_apanna``
  indicating that the accusative compound context holds.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_4_prapta_apanne_gate") is True:
        return False
    if not state.meta.get("2_2_4_arm"):
        return False
    return any("prapta_apanna" in t.tags for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    state.paribhasha_gates["2_2_4_prapta_apanne_gate"] = True
    state.samjna_registry["2_2_4_prapta_apanna"] = True
    state.meta.pop("2_2_4_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.4",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="prApta-Apanne ca dvitIyayA",
    text_dev="प्राप्तापन्ने च द्वितीयया",
    padaccheda_dev="प्राप्त-आपन्ने / च / द्वितीयया",
    why_dev=(
        "प्राप्त-आपन्नौ द्वितीयान्तेन समस्येते — ग्रामप्राप्तः, आपदापन्नः इत्यादि।"
    ),
    anuvritti_from=("2.1.3",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
