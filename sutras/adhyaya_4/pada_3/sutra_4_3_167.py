"""
4.3.167  हरीतक्यादिभ्यश्च  —  VIDHI

Sense: see the Kāśikā on this sūtra (`make brain S=4.3.167`); examples — harītakī, kośātakī.
Pāṭha: ashtadhyayi.com data.txt row i=43167 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine       import gana
from engine.luk   import live_taddhita, take_away
from engine.state import State
from engine.taddhita_attach import frame_open
from engine.vivaksha import vivaksita

def _site(state: State):
    i = live_taddhita(state)
    if i is None or i == 0 or not (frame_open(state, "vikAra") or frame_open(state, "avayava")):
        return None
    t = state.terms[i - 1]
    if not gana.in_gana_of_sutra("4.3.167", t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)):
        return None
    return i if vivaksita(state, "vikAraBeda", "Pala") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return take_away(state, _site(state), "lup")

SUTRA = SutraRecord(
    sutra_id              = "4.3.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "harItakyAdiByaS ca",
    text_dev              = "हरीतक्यादिभ्यश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA harItaky-AdiByaH ca tasya vikAraH avayave Pale lup",
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा हरीतक्य-आदिभ्यः च तस्य विकारः अवयवे फले लुप्",
    padaccheda_dev        = "हरीतक्य-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.3.167) हरीतक्यादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.3.163',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
