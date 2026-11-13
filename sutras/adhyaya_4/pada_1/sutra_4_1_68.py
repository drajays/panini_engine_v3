"""
4.1.68  पङ्गोश्च  —  VIDHI

Padaccheda: पङ्गोः च

पङ्गोश्च (4.1.68)
Pāṭha: ashtadhyayi.com data.txt row i=41068 (Art. 14).
Kāśikā: पङ्गुशब्दात् स्त्रियामूङ् प्रत्ययो भवति।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

def _wanted(t) -> bool:
    """the word paṅgu itself (ūṅ for the woman of that name)."""
    return "".join(v.slp1 for v in t.varnas) == "paNgu"

def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "UN") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paNgoSca",
    text_dev              = "पङ्गोश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt paNgoH ca UN",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् पङ्गोः च ऊङ्",
    padaccheda_dev        = "पङ्गोः च",
    why_dev               = "(सूत्रम् 4.1.68) पङ्गोश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
