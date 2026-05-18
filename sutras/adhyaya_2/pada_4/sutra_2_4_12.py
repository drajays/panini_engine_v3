"""
2.4.12  विभाषा वृक्षमृगतृणधान्यव्यञ्जनपशुशकुन्यश्ववडवपूर्वापराधरोत्तराणाम्  —  VIDHI

Padaccheda: विभाषा वृक्ष-मृग-तृण-धान्य-व्यञ्जन-पशु-शकुनी-अश्ववडव-पूर्वापर-अधरोत्तराणाम्

Optional dvandva for tree, animal, grass etc.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_12_vrksa_mrga_vibhasa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_12_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.4.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA vfkzamfgatfRaDAnyavyaYjanapaSuSakunyaSvavaqavapUrvAparADarottarARAm",
    text_dev              = "विभाषा वृक्षमृगतृणधान्यव्यञ्जनपशुशकुन्यश्ववडवपूर्वापराधरोत्तराणाम्",
    padaccheda_dev        = "विभाषा वृक्ष-मृग-तृण-धान्य-व्यञ्जन-पशु-शकुनी-अश्ववडव-पूर्वापर-अधरोत्तराणाम्",
    why_dev               = "वृक्ष-मृग-तृण-आदिषु विभाषा (२.४.१२)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
