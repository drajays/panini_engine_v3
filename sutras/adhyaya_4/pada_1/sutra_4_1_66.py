"""
4.1.66  ऊङुतः  —  VIDHI

Padaccheda: ऊङ् उतः

ऊङुतः (4.1.66)
Pāṭha: ashtadhyayi.com data.txt row i=41066 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri


def _wanted(t) -> bool:
    """anupasarjana, ends in short u (utaḥ): the stem of a human class (manuṣya-jāteḥ), as the speaker intends it."""
    return bool(t.varnas) and t.varnas[-1].slp1 == "u" and "upasarjana" not in t.tags


def _site(state: State):
    return strI_site(state, _wanted) if vivaksita(state, "jAtiBeda", "manuzyajAti") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "UN") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UNutaH",
    text_dev              = "ऊङुतः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt UN utaH manuzya-jAteH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् ऊङ् उतः मनुष्य-जातेः",
    padaccheda_dev        = "ऊङ् उतः",
    why_dev               = "(सूत्रम् 4.1.66) ऊङुतः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
