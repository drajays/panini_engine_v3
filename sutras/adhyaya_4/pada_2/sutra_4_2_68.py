"""
4.2.68  तेन निर्वृत्तम्  —  VIDHI

Padaccheda: तेन निर्वृत्तम्

तेन निर्वृत्तम् (4.2.68)
Pāṭha: ashtadhyayi.com data.txt row i=42068 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import frame_open, stem_ends_tape
from engine.vivaksha import vivaksita


def cond(state: State) -> bool:
    return stem_ends_tape(state) and vivaksita(state, "taddhitArtha", "nirvfta") and not frame_open(state, "cAturarTika")


def act(state: State) -> State:
    if cond(state):
        state.adhikara_stack.append({"id": "4.2.68", "scope_end": "4.3.168", "artha": "cAturarTika", "text_dev": "nirvfta"})      # aṇ comes from 4.1.83 under the frame
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tena nirvfttam",
    text_dev              = "तेन निर्वृत्तम्",
    samagra_slp1          = "tena nirvfttam iti tannAmA deSaH iti samarTAnAm praTamAt paraH tadDitaH pratyayaH aR vA",
    samagra_dev           = "'तेन निर्वृत्तम् इति तन्नामा देशः'  (इति) समर्थानाम् प्रथमात् परः तद्धितः प्रत्ययः अण् वा",
    padaccheda_dev        = "तेन निर्वृत्तम्",
    why_dev               = "(सूत्रम् 4.2.68) तेन निर्वृत्तम्।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the sense-frame is opened by the loop: the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
