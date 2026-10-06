"""
7.4.65  दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च  —  VIDHI

Padaccheda: दाधर्ति दर्धर्ति दर्धर्षि बोभूतु तेतिक्ते अलर्षि आपनीफणत् संसनिष्यदत् करिक्रत् कनिक्रदत् भरिभ्रत् दविध्वतः दविद्युतत् तरित्रतः सरीसृपतम् वरीवृजत् मर्मृज्य आगनीगन्ति इति च

दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च (7.4.65)
Pāṭha: ashtadhyayi.com data.txt row i=74065 (Art. 14).
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

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'dADartidarDartidarDarziboBUtutetiktelarzyApanIPaRatsaMsanizyadatkarikratkanikradadBariBraddaviDvatodavidyutattaritrataHsarIsfpataMvarIvfjanmarmfjyAganIgantIti ca',
    text_dev              = 'दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च',
    samagra_slp1          = "aNgasya aByAsasya dADarti darDarti darDarzi boBUtu tetikte alarzi ApanIPaRat saMsanizyadat karikrat kanikradat BariBrat daviDvataH davidyutat taritrataH sarIsfpatam varIvfjat marmfjya AganIganti iti ca Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासस्य दाधर्ति दर्धर्ति दर्धर्षि बोभूतु तेतिक्ते अलर्षि आपनीफणत् संसनिष्यदत् करिक्रत् कनिक्रदत् भरिभ्रत् दविध्वतः दविद्युतत् तरित्रतः सरीसृपतम् वरीवृजत् मर्मृज्य आगनीगन्ति इति च छन्दसि",
    padaccheda_dev        = "दाधर्ति दर्धर्ति दर्धर्षि बोभूतु तेतिक्ते अलर्षि आपनीफणत् संसनिष्यदत् करिक्रत् कनिक्रदत् भरिभ्रत् दविध्वतः दविद्युतत् तरित्रतः सरीसृपतम् वरीवृजत् मर्मृज्य आगनीगन्ति इति च",
    why_dev               = "(सूत्रम् 7.4.65) दाधर्तिदर्धर्तिदर्धर्षिबोभूतुतेतिक्तेऽलर्ष्यापनीफणत्संसनिष्यदत्करिक्रत्कनिक्रदद्भरिभ्रद्दविध्वतोदविद्युतत्तरित्रतःसरीसृपतंवरीवृजन्मर्मृज्यागनीगन्तीति च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
