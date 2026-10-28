"""
4.4.24  लवणाल्लुक्  —  VIDHI

Padaccheda: लवणात् लुक्

लवणाल्लुक् (4.4.24)
Pāṭha: ashtadhyayi.com data.txt row i=44024 (Art. 14).

Kāśikā: संसृष्ट इत्यनेनोत्पन्नस्य ठको लवणशब्दाद् लुग् भवति — लवणः सूपः, लवणं शाकम्, लवणा यवागूः.
The ṭhak (4.4.1) of the saṃsṛṣṭa sense (4.4.22) is taken away as *luk* (``engine.luk``): the word keeps the liṅga of the thing it qualifies, which is the speaker's vivakṣā.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.luk   import live_taddhita, take_away
from engine.state import State
from engine.taddhita_attach import frame_open


def _site(state: State):
    i = live_taddhita(state, upadesha=("Wak",))
    if i is None or i == 0 or not frame_open(state, "saMsfzwa"):
        return None
    return i if state.terms[i - 1].meta.get("upadesha_slp1") == "lavaRa" else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return take_away(state, _site(state), "luk")


SUTRA = SutraRecord(
    sutra_id              = "4.4.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lavaRAlluk",
    text_dev              = "लवणाल्लुक्",
    samagra_slp1          = "tena saMsfzwe iti lavaRAt luk",
    samagra_dev           = "'तेन संसृष्टे' इति लवणात् लुक्",
    padaccheda_dev        = "लवणात् लुक्",
    why_dev               = "(सूत्रम् 4.4.24) लवणाल्लुक्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
