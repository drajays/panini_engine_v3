"""
4.1.96  बाह्वादिभ्यश्च  —  VIDHI

Padaccheda: बाहु-आदिभ्यः च

बाह्वादिभ्यश्च (4.1.96)
Pāṭha: ashtadhyayi.com data.txt row i=41096 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401


def _site(state: State):
    return taddhita_site(state, "apatya", gana_name="bAhvAdiH")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "iY")


SUTRA = SutraRecord(
    sutra_id              = "4.1.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bAhvAdiByaSca",
    text_dev              = "बाह्वादिभ्यश्च",
    samagra_slp1          = "tasya apatyam iti bAhvAdiByaH iY pratyayaH",
    samagra_dev           = "'तस्य अपत्यम्' इति बाह्वादिभ्यः इञ् प्रत्ययः",
    padaccheda_dev        = "बाहु-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.1.96) बाह्वादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
