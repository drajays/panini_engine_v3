"""
4.1.138  क्षत्राद्घः  —  VIDHI

Padaccheda: क्षत्रात् घः

क्षत्राद्घः (4.1.138)
Pāṭha: ashtadhyayi.com data.txt row i=41138 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401


def _site(state: State):
    return taddhita_site(state, final=lambda f: f == "kzatra")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "Ga")


SUTRA = SutraRecord(
    sutra_id              = "4.1.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzatrAdGaH",
    text_dev              = "क्षत्राद्घः",
    samagra_slp1          = "tasya apatyam iti kzatrAt GaH",
    samagra_dev           = "'तस्य अपत्यम्' (इति) क्षत्रात् घः",
    padaccheda_dev        = "क्षत्रात् घः",
    why_dev               = "(सूत्रम् 4.1.138) क्षत्राद्घः।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83', '4.1.95'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
