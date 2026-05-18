"""
4.2.80  वुञ्छण्कठजिलशेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः  —  VIDHI

Padaccheda: वुञ्-छण्-क-ठच्-इल-स-इनि-र-ढञ्-ण्य-य-फक्-फिञ्-इञ्-ञ्य-कक्-ठकः अरीहण-कृशाश्वर्श्य-कुमुद-काश-तृण-प्रेक्ष-अश्म-सखि-संकाश-बल-पक्ष-कर्ण-सुतंगम-प्रगदिन्-वराह-कुमुद-आदिभ्यः

वुञ्छण्कठजिलशेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः (4.2.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_80_vuYCaRkaWa_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_80_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vuYCaRkaWajilaSeniraQaYRyayaPakPiYiYYyakakWako'rIhaRakfSASvarSyakumudakASatfRaprekzA'SmasaKisaMkASabalapakzakarRasutaMgamapragadinvarAhakumudAdiByaH",
    text_dev              = "वुञ्छण्कठजिलशेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः",
    padaccheda_dev        = "वुञ्-छण्-क-ठच्-इल-स-इनि-र-ढञ्-ण्य-य-फक्-फिञ्-इञ्-ञ्य-कक्-ठकः अरीहण-कृशाश्वर्श्य-कुमुद-काश-तृण-प्रेक्ष-अश्म-सखि-संकाश-बल-पक्ष-कर्ण-सुतंगम-प्रगदिन्-वराह-कुमुद-आदिभ्यः",
    why_dev               = "(सूत्रम् 4.2.80) वुञ्छण्कठजिलशेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
