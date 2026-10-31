"""
4.1.41  षिद्गौरादिभ्यश्च  —  VIDHI

Padaccheda: षित्-गौरादिभ्यः च

षिद्गौरादिभ्यश्च (4.1.41)
Pāṭha: ashtadhyayi.com data.txt row i=41041 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin, gana
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri


def _wanted(t) -> bool:
    """anupasarjana, and either made by a ṣit pratyaya (ṣvun: nartakī) or a word of the gaurādi gaṇa (gaurī)."""
    name = t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)
    return "upasarjana" not in t.tags and (origin.IT + "z" in t.tags or gana.in_gana("gOrAdiH", name))


def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "NIz") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zidgOrAdiByaSca",
    text_dev              = "षिद्गौरादिभ्यश्च",
    samagra_slp1          = "anupasarjanAt zit-gOrAdiByaH striyAm NIz pratyayaH paraSca",
    samagra_dev           = "अनुपसर्जनात् षित्-गौरादिभ्यः स्त्रियाम् ङीष् प्रत्ययः परश्च",
    padaccheda_dev        = "षित्-गौरादिभ्यः च",
    why_dev               = "(सूत्रम् 4.1.41) षिद्गौरादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.1.4',),      # ṭāpo 'pavādaḥ
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
