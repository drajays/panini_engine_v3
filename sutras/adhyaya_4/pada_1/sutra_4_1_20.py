"""
4.1.20  वयसि प्रथमे  —  VIDHI

Padaccheda: वयसि प्रथमे

वयसि प्रथमे (4.1.20)
Pāṭha: ashtadhyayi.com data.txt row i=41020 (Art. 14).
Kāśikā: प्रथमे वयसि यत् प्रातिपदिकं श्रुत्या वर्तते, ततः स्त्रियां ङीप् प्रत्ययो भवति। कुमारी।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

def _wanted(t) -> bool:
    """a-final, anupasarjana, a word that by its meaning stands for the first age (kumāra, kiśora): the lexical fact lex:prathamavayas."""
    return bool(t.varnas) and t.varnas[-1].slp1 == "a" and "upasarjana" not in t.tags and "lex:prathamavayas" in t.tags

def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "NIp") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vayasi praTame",
    text_dev              = "वयसि प्रथमे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt vayasi praTame NIp",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् वयसि प्रथमे ङीप्",
    padaccheda_dev        = "वयसि प्रथमे",
    why_dev               = "(सूत्रम् 4.1.20) वयसि प्रथमे।",
    anuvritti_from        = ('4.1.1',),
    apavada_of = ("4.1.4",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
