"""
3.2.21  दिवाविभानिशाप्रभाभास्करान्तानन्तादिबहुनान्दीकिम्लिपिलिबिबलिभक्तिकर्तृचित्रक्षेत्रसंख्याजङ्घाबाह्वहर्यत्तत्धनुररुष्षु  —  VIDHI

Padaccheda: दिवा-विभा-निशा-प्रभा-भास्-कार-अन्त-अनन्त-आदि-बहु-नान्दी-किम्-लिपि-लिबि-बलि-भक्ति-कर्तृ-चित्र-क्षेत्र-संख्या-जङ्घा-बाहु-अहर्-यत्-तत्-धनुर्-अरुष्षु

krt-suffix rule: दिवाविभानिशाप्रभाभास्करान्तानन्तादिबहुनान्दीकिम्लिपिलिबिबलिभक्तिकर्तृचित्रक्षेत्रसंख्याजङ्घाबाह्वहर्यत्तत्धनुररुष्षु (21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_21_divAviBAni_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_21_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "divAviBAniSApraBABAskarAntAnantAdibahunAndIkimlipilibibaliBaktikartfcitrakzetrasaMKyAjaNGAbAhvaharyattatDanuraruzzu",
    text_dev              = "दिवाविभानिशाप्रभाभास्करान्तानन्तादिबहुनान्दीकिम्लिपिलिबिबलिभक्तिकर्तृचित्रक्षेत्रसंख्याजङ्घाबाह्वहर्यत्तत्धनुररुष्षु",
    padaccheda_dev        = "दिवा-विभा-निशा-प्रभा-भास्-कार-अन्त-अनन्त-आदि-बहु-नान्दी-किम्-लिपि-लिबि-बलि-भक्ति-कर्तृ-चित्र-क्षेत्र-संख्या-जङ्घा-बाहु-अहर्-यत्-तत्-धनुर्-अरुष्षु",
    why_dev               = "धातोः कृत्-प्रत्ययः [दिवाविभानिशाप्रभाभास्करान्तानन्तादिबहुनान्दीकिम्लिपिलिबिबलिभक्तिकर्तृचित्रक्षेत्रसंख्याजङ्घाबाह्वहर्यत्तत्धनुररुष्षु] विहितः (३.२.21)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
