"""
3.1.126  आसुयुवपिरपिलपित्रपिचमश्च  —  VIDHI

Padaccheda: आसु-यु-वपि-रपि-लपि-त्रपि-चमः च

Krt suffix rule from dhatu: आसुयुवपिरपिलपित्रपिचमश्च (126)
Pāṭha: ashtadhyayi.com data.txt row i=31126 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem

def cond(state: State) -> bool:
    """yu, vap, rap, lap, trap, cam, dabh → ṇyat, the apavāda of yat (3.1.97) and of 3.1.98 (yāvyam, vāpyam, cāmyam)."""
    return kftya_open(state, "3.1.126") and kftya_stem(state) in ("yu", "vap", "rap", "lap", "trap", "cam", "daB")


def act(state: State) -> State:
    return kftya_attach(state, "3.1.126", "Ryat")


SUTRA = SutraRecord(
    sutra_id              = "3.1.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AsuyuvapirapilapitrapicamaSca",
    text_dev              = "आसुयुवपिरपिलपित्रपिचमश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH Asu-yu-vapi-rapi-lapi-trapi-camaH ca kft Ryat",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः आसु-यु-वपि-रपि-लपि-त्रपि-चमः च कृत् ण्यत्",
    padaccheda_dev        = "आसु-यु-वपि-रपि-लपि-त्रपि-चमः च",
    why_dev               = "धातोः [आसुयुवपिरपिलपित्रपिचमश्च]-प्रत्ययः विहितः (३.१.126)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.97', '3.1.98'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
