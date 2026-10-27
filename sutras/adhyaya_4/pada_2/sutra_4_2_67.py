"""
4.2.67  तदस्मिन्नस्तीति देशे तन्नाम्नि  —  VIDHI

Padaccheda: तत् अस्मिन् अस्ति (क्रियापदम्) इति देशे तन्नाम्नि

तदस्मिन्नस्तीति देशे तन्नाम्नि (4.2.67)
Pāṭha: ashtadhyayi.com data.txt row i=42067 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import frame_open, stem_ends_tape
from engine.vivaksha import vivaksita


def cond(state: State) -> bool:
    return stem_ends_tape(state) and vivaksita(state, "taddhitArtha", "asti") and not frame_open(state, "cAturarTika")


def act(state: State) -> State:
    if cond(state):
        state.adhikara_stack.append({"id": "4.2.67", "scope_end": "4.3.168", "artha": "cAturarTika", "text_dev": "asti"})      # aṇ comes from 4.1.83 under the frame
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadasminnastIti deSe tannAmni",
    text_dev              = "तदस्मिन्नस्तीति देशे तन्नाम्नि",
    samagra_slp1          = "tad asmin deSe astIti tannAmni iti samarTAnAm praTamAt paraH tadDitaH pratyayaH aR vA",
    samagra_dev           = "'तद् अस्मिन् देशे अस्तीति तन्नाम्नि' (इति) समर्थानाम् प्रथमात् परः तद्धितः प्रत्ययः अण् वा",
    padaccheda_dev        = "तत् अस्मिन् अस्ति (क्रियापदम्) इति देशे तन्नाम्नि",
    why_dev               = "(सूत्रम् 4.2.67) तदस्मिन्नस्तीति देशे तन्नाम्नि।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the sense-frame is opened by the loop: the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
