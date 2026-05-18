"""
1.4.6  ङिति ह्रस्वश्च  (ṅiti hrasvaś ca)  —  NIYAMA

**Pāṭha:** Before a *ṅit* suffix (one marked with the *it* marker *ṅ*), the
stem also undergoes *hrasva* (shortening, if applicable).

v3: sets the interpretive gate ``1_4_6_Ngiti_hrasva`` in
``state.paribhasha_gates`` to signal downstream rules that hrasva-before-ṅit
is operative.  No phonemic mutation is performed here; the actual shortening
is executed by the relevant VIDHI rules.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    return state.paribhasha_gates.get("1_4_6_Ngiti_hrasva") is not True


def act(state: State) -> State:
    state.paribhasha_gates["1_4_6_Ngiti_hrasva"] = True
    state.samjna_registry["Ngiti_hrasva_gate"] = frozenset({"hrasva_before_Ngit"})
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.6",
    sutra_type             = SutraType.NIYAMA,
    text_slp1              = "Ngiti hrasvaSca",
    text_dev               = "ङिति ह्रस्वश्च",
    padaccheda_dev         = "ङिति / ह्रस्वः च",
    why_dev                = "ङित्-प्रत्यये परे नदीसंज्ञकस्य ह्रस्वश्च भवति।",
    anuvritti_from         = ("1.4.1", "1.4.3"),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
