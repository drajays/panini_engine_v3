"""
7.2.32  अपरिह्वृताश्च  —  VIDHI

Padaccheda: अपरिह्वृताः च

अपरिह्वृताश्च (7.2.32)
Pāṭha: ashtadhyayi.com data.txt row i=72032 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_32_aparihvftA_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.32", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aparihvftASca",
    text_dev              = "अपरिह्वृताश्च",
    samagra_slp1          = "aNgasya aparihvftAH ca na iw nizWAyAm Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अपरिह्वृताः च न इट् निष्ठायाम् छन्दसि",
    padaccheda_dev        = "अपरिह्वृताः च",
    why_dev               = "(सूत्रम् 7.2.32) अपरिह्वृताश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
