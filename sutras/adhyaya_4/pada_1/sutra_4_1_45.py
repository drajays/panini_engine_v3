"""
4.1.45  बह्वादिभ्यश्च  —  VIDHI

Padaccheda: बहु-आदिभ्यः च

बह्वादिभ्यश्च (4.1.45)
Pāṭha: ashtadhyayi.com data.txt row i=41045 (Art. 14).
Kāśikā: बहु इत्येवमादिभ्यः प्रातिपदिकेभ्यः स्त्रियां वा ङीष् प्रत्ययो भवति।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin, gana
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

def _wanted(t) -> bool:
    """a member of the bahvādi gaṇa (bahu, padhati, śakti …)."""
    return gana.in_gana("bahvAdiH", t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas))

def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "NIz") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.45",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    r1_form_identity_exempt = True,
    text_slp1             = "bahvAdiByaSca",
    text_dev              = "बह्वादिभ्यश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt bahva-AdiByaH ca NIz vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् बह्व-आदिभ्यः च ङीष् वा",
    padaccheda_dev        = "बहु-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.1.45) बह्वादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
