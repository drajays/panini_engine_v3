"""
4.1.21  द्विगोः  —  VIDHI

Padaccheda: द्विगोः

द्विगोः (4.1.21)
Pāṭha: ashtadhyayi.com data.txt row i=41021 (Art. 14).
Kāśikā: द्विगुसंज्ञकात् प्रातिपदिकात् स्त्रियां ङीप् प्रत्ययो भवति। पञ्चपूली।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

def _wanted(t) -> bool:
    """a prātipadika with the dvigu saṃjñā (pañcapūla): the lexical fact lex:dvigu the samāsa vidhi leaves on it."""
    return bool(t.varnas) and "upasarjana" not in t.tags and "lex:dvigu" in t.tags

def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "NIp") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvigoH",
    text_dev              = "द्विगोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt dvigoH NIp",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् द्विगोः ङीप्",
    padaccheda_dev        = "द्विगोः",
    why_dev               = "(सूत्रम् 4.1.21) द्विगोः।",
    anuvritti_from        = ('4.1.1',),
    apavada_of = ("4.1.4",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
