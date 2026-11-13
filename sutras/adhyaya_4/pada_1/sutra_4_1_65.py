"""
4.1.65  इतो मनुष्यजातेः  —  VIDHI

Padaccheda: इतः मनुष्य-जातेः

इतो मनुष्यजातेः (4.1.65)
Pāṭha: ashtadhyayi.com data.txt row i=41065 (Art. 14).
Kāśikā: इकारान्तात् प्रातिपदिकात् मनुष्यजातिवाचिनः स्त्रियां ङीष् प्रत्ययो भवति।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

def _wanted(t) -> bool:
    """i-final word of a human class (avanti, kunti, dākṣi): ṅīṣ by the speaker's vivakṣā jAtiBeda=manuzyajAti."""
    return bool(t.varnas) and t.varnas[-1].slp1 == "i" and "upasarjana" not in t.tags

def _site(state: State):
    return strI_site(state, _wanted) if vivaksita(state, "jAtiBeda", "manuzyajAti") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "NIz") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ito manuzyajAteH",
    text_dev              = "इतो मनुष्यजातेः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt itaH manuzya-jAteH NIz",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् इतः मनुष्य-जातेः ङीष्",
    padaccheda_dev        = "इतः मनुष्य-जातेः",
    why_dev               = "(सूत्रम् 4.1.65) इतो मनुष्यजातेः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
