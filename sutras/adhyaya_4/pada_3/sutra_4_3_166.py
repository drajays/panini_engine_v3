"""
4.3.166  लुप् च  —  VIDHI

Sense: see the Kāśikā on this sūtra (`make brain S=4.3.166`); examples — jambūḥ, jambu, jāmbavam.
(aṇ stays) and jambu (the aṇ of 4.1.83 taken by luk 4.3.163, the ūṅ by 1.2.49).
Pāṭha: ashtadhyayi.com data.txt row i=43166 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine       import gana
from engine.luk   import live_taddhita, take_away
from engine.state import State
from engine.taddhita_attach import frame_open
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

def _site(state: State):
    i = live_taddhita(state, only_from=("4.3.165",))
    if i is None or not (frame_open(state, "vikAra") or frame_open(state, "avayava")):
        return None
    return i if vivaksita(state, "vikAraBeda", "Pala") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if policy_pick(state, "4.3.166", 2) == 1:
        return state                      # vā: the aṇ of 4.3.165 stays a reading
    return take_away(state, _site(state), "lup")

SUTRA = SutraRecord(
    sutra_id              = "4.3.166",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lup ca",
    text_dev              = "लुप् च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA lup ca vikAraH tasya avayave Pale jambvAH vA",
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा लुप् च विकारः तस्य अवयवे फले जम्ब्वाः वा",
    padaccheda_dev        = "लुप् च",
    why_dev               = "(सूत्रम् 4.3.166) लुप् च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.3.163',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
