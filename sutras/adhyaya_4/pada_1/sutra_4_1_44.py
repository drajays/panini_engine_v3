"""
4.1.44  वोतो गुणवचनात्  —  VIDHI

Padaccheda: वा उतः गुणवचनात्

वोतो गुणवचनात् (4.1.44)
Pāṭha: ashtadhyayi.com data.txt row i=41044 (Art. 14).
Kāśikā: गुणमुक्त वान् गुणवचनः। गुणवचनात् प्रातिपदिकाद् उकारान्तात् स्त्रियां वा ङीष् प्रत्ययो भवति।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

def _wanted(t) -> bool:
    """u-final guṇavacana (paṭu, mṛdu): the lexical fact lex:guRavacana."""
    return bool(t.varnas) and t.varnas[-1].slp1 == "u" and "upasarjana" not in t.tags and "lex:guRavacana" in t.tags

def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "NIz") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.44",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    r1_form_identity_exempt = True,
    text_slp1             = "voto guRavacanAt",
    text_dev              = "वोतो गुणवचनात्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt vA utaH guRa-vacanAt NIz",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् वा उतः गुण-वचनात् ङीष्",
    padaccheda_dev        = "वा उतः गुणवचनात्",
    why_dev               = "(सूत्रम् 4.1.44) वोतो गुणवचनात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
