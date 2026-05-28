"""
4.1.42  जानपदकुण्डगोणस्थलभाजनागकालनीलकुशकामुककबराद्वृत्त्यमत्रावपनाकृत्रिमाश्राणास्थौल्यवर्णानाच्छादनायोविकारमैथुनेच्छाकेशवेशेषु  —  VIDHI

Padaccheda: जानपद-कुण्ड-गोण-स्थल-भाज-नाग-काल-नील-कुश-कामुक-कबरात् वृत्ति-अमत्र-आवपन-अकृत्रिमा-श्राणा-स्थौल्य-वर्ण-अनाच्छादन-अयोविकार-मैथुनेच्छा-केशवेशेषु

जानपदकुण्डगोणस्थलभाजनागकालनीलकुशकामुककबराद्वृत्त्यमत्रावपनाकृत्रिमाश्राणास्थौल्यवर्णानाच्छादनायोविकारमैथुनेच्छाकेशवेशेषु (4.1.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_42_jAnapadaku_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.42", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAnapadakuRqagoRasTalaBAjanAgakAlanIlakuSakAmukakabarAdvfttyamatrAvapanAkftrimASrARAsTOlyavarRAnAcCAdanAyovikAramETunecCAkeSaveSezu",
    text_dev              = "जानपदकुण्डगोणस्थलभाजनागकालनीलकुशकामुककबराद्वृत्त्यमत्रावपनाकृत्रिमाश्राणास्थौल्यवर्णानाच्छादनायोविकारमैथुनेच्छाकेशवेशेषु",
    padaccheda_dev        = "जानपद-कुण्ड-गोण-स्थल-भाज-नाग-काल-नील-कुश-कामुक-कबरात् वृत्ति-अमत्र-आवपन-अकृत्रिमा-श्राणा-स्थौल्य-वर्ण-अनाच्छादन-अयोविकार-मैथुनेच्छा-केशवेशेषु",
    why_dev               = "(सूत्रम् 4.1.42) जानपदकुण्डगोणस्थलभाजनागकालनीलकुशकामुककबराद्वृत्त्यमत्रावपनाकृत्रिमाश्राणास्थौल्यवर्णानाच्छादनायोविकारमैथुनेच्छाकेशवेशेषु।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
