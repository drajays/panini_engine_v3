"""
4.2.80  वुञ्छण्कठजिलसेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः  —  VIDHI

Padaccheda: वुञ्-छण्-क-ठच्-इल-स-इनि-र-ढञ्-ण्य-य-फक्-फिञ्-इञ्-ञ्य-कक्-ठकः अरीहण-कृशाश्वर्श्य-कुमुद-काश-तृण-प्रेक्ष-अश्म-सखि-संकाश-बल-पक्ष-कर्ण-सुतंगम-प्रगदिन्-वराह-कुमुद-आदिभ्यः

वुञ्छण्कठजिलशेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः (4.2.80)
Pāṭha: ashtadhyayi.com data.txt row i=42080 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_80_vuYCaRkaWa_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.80", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'vuYCaRkaWajilaseniraQaYRyayaPakPiYiYYyakakWakorIhaRakfSASvarSyakumudakASatfRaprekzASmasaKisaMkASabalapakzakarRasutaMgamapragadinvarAhakumudAdiByaH',
    text_dev              = 'वुञ्छण्कठजिलसेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA vuY-CaR-ka-Wac-il-sa-ini-ra-QaY-Rya-ya-Pak-PiY-iY-Yya-kak-WakaH arIhaRa-kfSASva-fSya-kumuda-kASa-tfRa-prekzA-aSma-saKi-saMkASa-bala-pakza-karRa-sutaNgama-pragadin-varAha-kumudAdiByaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा वुञ्-छण्-क-ठच्-इल्-स-इनि-र-ढञ्-ण्य-य-फक्-फिञ्-इञ्-ञ्य-कक्-ठकः अरीहण-कृशाश्व-ऋश्य-कुमुद-काश-तृण-प्रेक्षा-अश्म-सखि-संकाश-बल-पक्ष-कर्ण-सुतङ्गम-प्रगदिन्-वराह-कुमुदादिभ्यः",
    padaccheda_dev        = "वुञ्-छण्-क-ठच्-इल-स-इनि-र-ढञ्-ण्य-य-फक्-फिञ्-इञ्-ञ्य-कक्-ठकः अरीहण-कृशाश्वर्श्य-कुमुद-काश-तृण-प्रेक्ष-अश्म-सखि-संकाश-बल-पक्ष-कर्ण-सुतंगम-प्रगदिन्-वराह-कुमुद-आदिभ्यः",
    why_dev               = "(सूत्रम् 4.2.80) वुञ्छण्कठजिलशेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
