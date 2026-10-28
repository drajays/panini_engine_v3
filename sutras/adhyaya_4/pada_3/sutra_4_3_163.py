"""
4.3.163  फले लुक्  —  VIDHI

Padaccheda: फले लुक्

फले लुक् (4.3.163)
Pāṭha: ashtadhyayi.com data.txt row i=43163 (Art. 14).

Sense: see the Kāśikā on this sūtra (`make brain S=4.3.163`); examples — āmalakam, badaram.
The pratyaya of the vikāra / avayava senses (4.3.134 ff) is taken away (``engine.luk``, named luk) when the thing meant is a fruit (vivakṣā vikAraBeda=Pala).
Apavādas that keep or re-teach it: 4.3.164 plakṣādibhyo'ṇ and 4.3.165 jambvā vā keep the aṇ (their varṇas carry ``origin:<sūtra>``); 4.3.167 harītakyādi
(lup) and 4.3.166 stand instead of luk.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine       import gana
from engine.luk   import live_taddhita, take_away
from engine.state import State
from engine.taddhita_attach import frame_open
from engine.vivaksha import vivaksita


def _site(state: State):
    i = live_taddhita(state, not_from=("4.3.164", "4.3.165"))
    if i is None or i == 0 or not (frame_open(state, "vikAra") or frame_open(state, "avayava")):
        return None
    t = state.terms[i - 1]
    if gana.in_gana_of_sutra("4.3.167", t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)):
        return None            # harītakyādi: lup (4.3.167) is taught for these, not luk
    return i if vivaksita(state, "vikAraBeda", "Pala") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return take_away(state, _site(state), "luk")


SUTRA = SutraRecord(
    sutra_id              = "4.3.163",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Pale luk",
    text_dev              = "फले लुक्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA Pale luk tasya vikAraH avayave",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा फले लुक् तस्य विकारः अवयवे",
    padaccheda_dev        = "फले लुक्",
    why_dev               = "(सूत्रम् 4.3.163) फले लुक्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
