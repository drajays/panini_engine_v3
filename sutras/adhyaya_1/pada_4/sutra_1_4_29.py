"""
1.4.29  आख्यातोपयोगे  —  SAMJNA gate (kāraka-saṃjñā context)

**Pāṭha (anuvṛtti):** *kārake ākhyātopayoge (apādānam)* —
**1.4.23** *kārake*; **1.4.24** *apādānam* (anuvṛtti).

*Śāstra:* This sūtra qualifies the scope of the preceding apādāna rules —
they apply specifically in the context where a verb (*ākhyāta*) is in use
(ākhyātopayoge).  It serves as a gate / context-restrictor confirming that
kāraka saṃjñā assignment operates in verbalised sentence contexts.

*Engine:* Acts as a scope gate.  Fires when the state has the meta flag
``"1_4_29_akhyata_upayoga"`` set to True (pipeline signals verb-in-use context).
Writes ``state.samjna_registry["1_4_29_gate"]`` to mark the gate as activated.
``cond`` reads only structural meta (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY    = "1_4_29_gate"
META_CONTEXT  = "1_4_29_akhyata_upayoga"


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.29", state, "1.4.23"):
        return False
    if state.samjna_registry.get(SAMJNA_KEY):
        return False
    return bool(state.meta.get(META_CONTEXT))


def act(state: State) -> State:
    state.samjna_registry[SAMJNA_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.4.29",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "AKyAtopayoge",
    text_dev              = "आख्यातोपयोगे",
    padaccheda_dev        = "आख्यात-उपयोगे",
    why_dev               = (
        "आख्यातस्य उपयोगे (क्रियापदस्य व्यवहारे) एव कारक-संज्ञा-विधानम् "
        "प्रवर्तते — इति विषय-परिच्छेदकं सूत्रम्।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.24"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
