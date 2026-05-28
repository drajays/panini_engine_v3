"""
3.2.142  संपृचानुरुधाङ्यमाङ्यसपरिसृसंसृजपरिदेविसंज्वरपरिक्षिपपरिरटपरिवदपरिदहपरिमुहदुषद्विषद्रुहदुहयुजाक्रीडविविचत्यजरजभजातिचरापचरामुषाभ्याहनश्च  —  VIDHI

Padaccheda: संपृच-अनुरुध-आङ्यम्-आङ्यस्-परिसृ-संसृज-परिदेवि-संज्वर-परिक्षिप-परिरट-परिवद-परिदह-परिमुह-दुष-द्विष-द्रुह-दुह-युज-आक्रीड-विविच-त्यज-रज-भज-अतिचर-अपचर-आमुष-अभ्याहनः च

krt-suffix rule: संपृचानुरुधाङ्यमाङ्यसपरिसृसंसृजपरिदेविसंज्वरपरिक्षिपपरिरटपरिवदपरिदहपरिमुहदुषद्विषद्रुहदुहयुजाक्रीडविविचत्यजरजभजातिचरापचरामुषाभ्याहनश्च (142)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_142_saMpfcAnur_142"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.142"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.142",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMpfcAnuruDANyamANyasaparisfsaMsfjaparidevisaMjvaraparikzipaparirawaparivadaparidahaparimuhaduzadvizadruhaduhayujAkrIqavivicatyajarajaBajAticarApacarAmuzAByAhanaSca",
    text_dev              = "संपृचानुरुधाङ्यमाङ्यसपरिसृसंसृजपरिदेविसंज्वरपरिक्षिपपरिरटपरिवदपरिदहपरिमुहदुषद्विषद्रुहदुहयुजाक्रीडविविचत्यजरजभजातिचरापचरामुषाभ्याहनश्च",
    padaccheda_dev        = "संपृच-अनुरुध-आङ्यम्-आङ्यस्-परिसृ-संसृज-परिदेवि-संज्वर-परिक्षिप-परिरट-परिवद-परिदह-परिमुह-दुष-द्विष-द्रुह-दुह-युज-आक्रीड-विविच-त्यज-रज-भज-अतिचर-अपचर-आमुष-अभ्याहनः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [संपृचानुरुधाङ्यमाङ्यसपरिसृसंसृजपरिदेविसंज्वरपरिक्षिपपरिरटपरिवदपरिदहपरिमुहदुषद्विषद्रुहदुहयुजाक्रीडविविचत्यजरजभजातिचरापचरामुषाभ्याहनश्च] विहितः (३.२.142)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
