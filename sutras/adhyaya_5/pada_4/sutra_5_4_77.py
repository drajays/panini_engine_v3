"""
5.4.77  अचतुरविचतुरसुचतुरस्त्रीपुंसधेन्वनडुहर्क्सामवाङ्मनसाक्षिभ्रुवदारगवोर्वष्ठीवपदष्ठीवनक्तंदिवरत्रिंदिवाहर्दिवसरजसनिःश्रेयसपुरुषायुषद्व्यायुषत्र्यायुषर्ग्यजुषजातोक्षमहोक्षवृद्धोक्षोपशुनगोष्ठश्वाः  —  VIDHI

Padaccheda: अचतुर-विचतुर-सुचतुर-स्त्रीपुंस-धेन्वनडुह-ऋक्साम-वाङ्मनस्-अक्षिभ्रुव-दारगव-उर्वष्ठीव-पदष्ठीव-नक्तंदिव-रात्रिंदिव-अहर्दिव-सरजस-निःश्रेयस-पुरुषायुष-द्व्यायुष-त्र्यायुष-ऋग्यजुष-जातोक्ष-महोक्ष-वृद्धोक्ष-उपशुन-गोष्ठश्वाः

अचतुरविचतुरसुचतुरस्त्रीपुंसधेन्वनडुहर्क्सामवाङ्मनसाक्षिभ्रुवदारगवोर्वष्ठीवपदष्ठीवनक्तंदिवरत्रिंदिवाहर्दिवसरजसनिःश्रेयसपुरुषायुषद्व्यायुषत्र्यायुषर्ग्यजुषजातोक्षमहोक्षवृद्धोक्षोपशुनगोष्ठश्वाः (5.4.77)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_77_acaturavic_77"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_77_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "acaturavicaturasucaturastrIpuMsaDenvanaquharksAmavANmanasAkziBruvadAragavorvazWIvapadazWIvanaktaMdivaratriMdivAhardivasarajasaniHSreyasapuruzAyuzadvyAyuzatryAyuzargyajuzajAtokzamahokzavfdDokzopaSunagozWaSvAH",
    text_dev              = "अचतुरविचतुरसुचतुरस्त्रीपुंसधेन्वनडुहर्क्सामवाङ्मनसाक्षिभ्रुवदारगवोर्वष्ठीवपदष्ठीवनक्तंदिवरत्रिंदिवाहर्दिवसरजसनिःश्रेयसपुरुषायुषद्व्यायुषत्र्यायुषर्ग्यजुषजातोक्षमहोक्षवृद्धोक्षोपशुनगोष्ठश्वाः",
    padaccheda_dev        = "अचतुर-विचतुर-सुचतुर-स्त्रीपुंस-धेन्वनडुह-ऋक्साम-वाङ्मनस्-अक्षिभ्रुव-दारगव-उर्वष्ठीव-पदष्ठीव-नक्तंदिव-रात्रिंदिव-अहर्दिव-सरजस-निःश्रेयस-पुरुषायुष-द्व्यायुष-त्र्यायुष-ऋग्यजुष-जातोक्ष-महोक्ष-वृद्धोक्ष-उपशुन-गोष्ठश्वाः",
    why_dev               = "(सूत्रम् 5.4.77) अचतुरविचतुरसुचतुरस्त्रीपुंसधेन्वनडुहर्क्सामवाङ्मनसाक्षिभ्रुवदारगवोर्वष्ठीवपदष्ठीवनक्तंदिवरत्रिंदिवाहर्दिवसरजसनिःश्रेयसपुरुषायुषद्व्यायुषत्र्यायुषर्ग्यजुषजातोक्षमहोक्षवृद्धोक्षोपशुनगोष्ठश्वाः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
