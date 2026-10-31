"""
4.1.123  शुभ्रादिभ्यश्च  —  VIDHI

Padaccheda: शुभ्र-आदिभ्यः च

शुभ्रादिभ्यश्च (4.1.123)
Pāṭha: ashtadhyayi.com data.txt row i=41123 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita


def _site(state: State):
    """The apatya frame (4.1.92) is open and the stem is one of the Gaṇapāṭha's śubhrādi (an ākṛtigaṇa: only the listed words)."""
    return taddhita_site(state, "apatya", gana_name="SuBrAdiH")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return attach_taddhita(state, "Qak") if _site(state) is not None else state      # Q: 7.1.2 -> eya; k: kit (7.2.118 vṛddhi, 6.4.148)


SUTRA = SutraRecord(
    sutra_id              = "4.1.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SuBrAdiByaSca",
    text_dev              = "शुभ्रादिभ्यश्च",
    samagra_slp1          = "tasya apatyam iti SuBrAdiByaH Qak",
    samagra_dev           = "'तस्य अपत्यम्' (इति) शुभ्रादिभ्यः ढक्",
    padaccheda_dev        = "शुभ्र-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.1.123) शुभ्रादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.1.83', '4.1.86'),      # Kāśikā: yathāyogam iñādīnām apavādaḥ
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
