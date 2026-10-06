"""
3.2.142  संपृचानुरुधाङ्यमाङ्यसपरिसृसंसृजपरिदेविसंज्वरपरिक्षिपपरिरटपरिवदपरिदहपरिमुहदुषद्विषद्रुहदुहयुजाक्रीडविविचत्यजरजभजातिचरापचरामुषाभ्याहनश्च  —  VIDHI

Padaccheda: संपृच-अनुरुध-आङ्यम्-आङ्यस्-परिसृ-संसृज-परिदेवि-संज्वर-परिक्षिप-परिरट-परिवद-परिदह-परिमुह-दुष-द्विष-द्रुह-दुह-युज-आक्रीड-विविच-त्यज-रज-भज-अतिचर-अपचर-आमुष-अभ्याहनः च

krt-suffix rule: संपृचानुरुधाङ्यमाङ्यसपरिसृसंसृजपरिदेविसंज्वरपरिक्षिपपरिरटपरिवदपरिदहपरिमुहदुषद्विषद्रुहदुहयुजाक्रीडविविचत्यजरजभजातिचरापचरामुषाभ्याहनश्च (142)
Pāṭha: ashtadhyayi.com data.txt row i=32142 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_142_saMpfcAnur_142"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.142", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


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
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu sampfca-anuruDa-ANyama-ANyasa-parisf-saMsfja-paridevi-saMjvara-parikzipa-parirawa-parivada-paridaha-parimuha-duza-dviza-druha-duha-yuja-AkrIqa-vivica-tyaja-raja-Baja-aticara-apacara-Amuza-aByAhanaH ca kft GinuR",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु सम्पृच-अनुरुध-आङ्यम-आङ्यस-परिसृ-संसृज-परिदेवि-संज्वर-परिक्षिप-परिरट-परिवद-परिदह-परिमुह-दुष-द्विष-द्रुह-दुह-युज-आक्रीड-विविच-त्यज-रज-भज-अतिचर-अपचर-आमुष-अभ्याहनः च कृत् घिनुण्",
    padaccheda_dev        = "संपृच-अनुरुध-आङ्यम्-आङ्यस्-परिसृ-संसृज-परिदेवि-संज्वर-परिक्षिप-परिरट-परिवद-परिदह-परिमुह-दुष-द्विष-द्रुह-दुह-युज-आक्रीड-विविच-त्यज-रज-भज-अतिचर-अपचर-आमुष-अभ्याहनः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [संपृचानुरुधाङ्यमाङ्यसपरिसृसंसृजपरिदेविसंज्वरपरिक्षिपपरिरटपरिवदपरिदहपरिमुहदुषद्विषद्रुहदुहयुजाक्रीडविविचत्यजरजभजातिचरापचरामुषाभ्याहनश्च] विहितः (३.२.142)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
