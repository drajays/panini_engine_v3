"""
4.1.73  शार्ङ्गरवाद्यञो ङीन्  —  VIDHI

Padaccheda: शार्ङ्गरव-आदि-अञः ङीन्

शार्ङ्गरवाद्यञो ङीन् (4.1.73)
Pāṭha: ashtadhyayi.com data.txt row i=41073 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, gana
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri


def _wanted(t) -> bool:
    """anupasarjana, a member of the śārṅgaravādi gaṇa.
    SHORTCUT S138: the añ branch of the sūtra (a stem made by añ) is not modelled: 4.1.15 lists añ for ṅīp and the Kāśikā line that divides them is not in the repo."""
    name = t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)
    return "upasarjana" not in t.tags and gana.in_gana("SArNgaravAdiH", name)


def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "NIn") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SArNgaravAdyaYo NIn",
    text_dev              = "शार्ङ्गरवाद्यञो ङीन्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt SArNgaravAt aYaH NIn",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् शार्ङ्गरवात् अञः ङीन्",
    padaccheda_dev        = "शार्ङ्गरव-आदि-अञः ङीन्",
    why_dev               = "(सूत्रम् 4.1.73) शार्ङ्गरवाद्यञो ङीन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
