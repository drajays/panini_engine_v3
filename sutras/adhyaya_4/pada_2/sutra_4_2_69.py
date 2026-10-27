"""
4.2.69  तस्य निवासः  —  VIDHI

Padaccheda: तस्य निवासः

तस्य निवासः (4.2.69)
Pāṭha: ashtadhyayi.com data.txt row i=42069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import frame_open, stem_ends_tape
from engine.vivaksha import vivaksita


def cond(state: State) -> bool:
    return stem_ends_tape(state) and vivaksita(state, "taddhitArtha", "nivAsa") and not frame_open(state, "cAturarTika")


def act(state: State) -> State:
    if cond(state):
        state.adhikara_stack.append({"id": "4.2.69", "scope_end": "4.3.168", "artha": "cAturarTika", "text_dev": "nivAsa"})      # aṇ comes from 4.1.83 under the frame
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasya nivAsaH",
    text_dev              = "तस्य निवासः",
    samagra_slp1          = "tasya nivAsaH iti tannAmA deSaH iti samarTAnAm praTamAt paraH tadDitaH pratyayaH aR vA",
    samagra_dev           = "'तस्य निवासः इति तन्नामा देशः' (इति) समर्थानाम् प्रथमात् परः तद्धितः प्रत्ययः अण् वा",
    padaccheda_dev        = "तस्य निवासः",
    why_dev               = "(सूत्रम् 4.2.69) तस्य निवासः।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the sense-frame is opened by the loop: the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
