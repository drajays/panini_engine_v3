"""
3.2.56  आढ्यसुभगस्थूलपलितनग्नान्धप्रियेषु च्व्य्र्थेष्वच्वौ कृञः करणे ख्युन्  —  VIDHI

Padaccheda: आढ्य-सुभग-स्थूल-पलित-नग्न-अन्ध-प्रियेषु च्वि-अर्थेषु अ-च्वौ कृञः करणे ख्युन्

krt-suffix rule: आढ्यसुभगस्थूलपलितनग्नान्धप्रियेषु च्व्य्र्थेष्वच्वौ कृञः करणे ख्युन् (56)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_56_AQyasuBaga_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_56_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AQyasuBagasTUlapalitanagnAnDapriyezu cvyrTezvacvO kfYaH karaRe Kyun",
    text_dev              = "आढ्यसुभगस्थूलपलितनग्नान्धप्रियेषु च्व्य्र्थेष्वच्वौ कृञः करणे ख्युन्",
    padaccheda_dev        = "आढ्य-सुभग-स्थूल-पलित-नग्न-अन्ध-प्रियेषु च्वि-अर्थेषु अ-च्वौ कृञः करणे ख्युन्",
    why_dev               = "धातोः कृत्-प्रत्ययः [आढ्यसुभगस्थूलपलितनग्नान्धप्रियेषु च्व्य्र्थेष्वच्वौ कृञः करणे ख्युन्] विहितः (३.२.56)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
