"""
4.1.16  यञश्च  —  VIDHI

Padaccheda: यञः च

यञश्च (4.1.16)
Pāṭha: ashtadhyayi.com data.txt row i=41016 (Art. 14).
Kāśikā: यञन्ताच्च प्रातिपदिकात् स्त्रियां ङीप् प्रत्ययो भवति। गार्गी। वात्सी॥
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_nip


def _wanted(t) -> bool:
    """anupasarjana prātipadika whose last pratyaya is yañ (gārgya, vātsya): ṅīp, not ṭāp (Kāśikā: ṭāpo 'pavādaḥ)."""
    return bool(t.varnas) and "upasarjana" not in t.tags and origin.last_pratyaya(t) == "yaY"


def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_nip(state) if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaYaSca",
    text_dev              = "यञश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt yaYaH ca NIp",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् यञः च ङीप्",
    padaccheda_dev        = "यञः च",
    why_dev               = "(सूत्रम् 4.1.16) यञश्च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ("4.1.4",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
