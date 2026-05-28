"""
6.1.63  पद्दन्नोमास्हृन्निशसन्यूषन्दोषन्यकञ्छकन्नुदन्नासञ्छस्प्रभृतिषु  —  VIDHI

Padaccheda: पद्‍-दत्-नस्-मास्-हृत्-निश्-असन्-यूषन्-दोषन्-यकन्-शकन्-उदन्-आसन् (सर्वे पृथक् पृथक् लुप्तप्रथमान्तनिर्द्दिष्टाः) शस्-प्रभृतिषु

पद्दन्नोमास्हृन्निशसन्यूषन्दोषन्यकञ्छकन्नुदन्नासञ्छस्प्रभृतिषु (6.1.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_63_paddannomA_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_63_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paddannomAshfnniSasanyUzandozanyakaYCakannudannAsaYCaspraBftizu",
    text_dev              = "पद्दन्नोमास्हृन्निशसन्यूषन्दोषन्यकञ्छकन्नुदन्नासञ्छस्प्रभृतिषु",
    padaccheda_dev        = "पद्‍-दत्-नस्-मास्-हृत्-निश्-असन्-यूषन्-दोषन्-यकन्-शकन्-उदन्-आसन् (सर्वे पृथक् पृथक् लुप्तप्रथमान्तनिर्द्दिष्टाः) शस्-प्रभृतिषु",
    why_dev               = "(सूत्रम् 6.1.63) पद्दन्नोमास्हृन्निशसन्यूषन्दोषन्यकञ्छकन्नुदन्नासञ्छस्प्रभृतिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
