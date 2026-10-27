"""
4.1.101  यञिञोश्च  —  VIDHI

Padaccheda: यञ्-इञोः च

यञिञोश्च (4.1.101)
Pāṭha: ashtadhyayi.com data.txt row i=41101 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita


def _site(state: State):
    """The apatya of a gotra-pratyayānta stem (one that ends in yañ or iñ): the yuvan (4.1.94), taught phak."""
    return taddhita_site(state, origin="yaY") or taddhita_site(state, origin="iY")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "Pak")


SUTRA = SutraRecord(
    sutra_id              = "4.1.101",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaYiYoSca",
    text_dev              = "यञिञोश्च",
    samagra_slp1          = "tasya gotre apatyam iti yaY-iYoH Pak",
    samagra_dev           = "'तस्य गोत्रे अपत्यम्' (इति) यञ्-इञोः  फक्",
    padaccheda_dev        = "यञ्-इञोः च",
    why_dev               = "(सूत्रम् 4.1.101) यञिञोश्च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83', '4.1.95', '4.1.105'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
