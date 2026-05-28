"""
7.4.65  दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च  —  VIDHI

Padaccheda: दाधर्ति दर्धर्ति दर्धर्षि बोभूतु तेतिक्ते अलर्षि आपनीफणत् संसनिष्यदत् करिक्रत् कनिक्रदत् भरिभ्रत् दविध्वतः दविद्युतत् तरित्रतः सरीसृपतम् वरीवृजत् मर्मृज्य आगनीगन्ति इति च

दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च (7.4.65)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_65_dADartidar_65"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.65", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_4_65_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dADartidarDartidarDarziboBUtutetikte'larzyApanIPaRatsaMsanizyadatkarikratkanikradadBariBraddaviDvatodavidyutattaritrataHsarIsfpataMvarIvfjanmarmfjyAganIgantIti ca",
    text_dev              = "दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च",
    padaccheda_dev        = "दाधर्ति दर्धर्ति दर्धर्षि बोभूतु तेतिक्ते अलर्षि आपनीफणत् संसनिष्यदत् करिक्रत् कनिक्रदत् भरिभ्रत् दविध्वतः दविद्युतत् तरित्रतः सरीसृपतम् वरीवृजत् मर्मृज्य आगनीगन्ति इति च",
    why_dev               = "(सूत्रम् 7.4.65) दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
