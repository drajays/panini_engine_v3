"""
4.1.104  अनृष्यानन्तर्ये बिदादिभ्योऽञ्  —  VIDHI

Padaccheda: अनृषि (लुप्तपञ्चम्यन्तनिर्देशः) आनन्तर्ये बिद-आदिभ्यः अञ्

अनृष्यानन्तर्ये बिदादिभ्योऽञ् (4.1.104)
Pāṭha: ashtadhyayi.com data.txt row i=41104 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401


def _site(state: State):
    return taddhita_site(state, "apatya", gana_name="bidAdiH") if vivaksita(state, "apatyaBeda", "gotra") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "aY")


SUTRA = SutraRecord(
    sutra_id              = "4.1.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'anfzyAnantarye bidAdiByoY',
    text_dev              = 'अनृष्यानन्तर्ये बिदादिभ्योऽञ्',
    samagra_slp1          = "tasya gotre apatyam iti bidAdiByaH aY tasya anantare apatyam iti anfzi aY",
    samagra_dev           = "'तस्य गोत्रे अपत्यम्' (इति) बिदादिभ्यः अञ्, 'तस्य अनन्तरे अपत्यम्' (इति) अनृषि अञ्",
    padaccheda_dev        = "अनृषि (लुप्तपञ्चम्यन्तनिर्देशः) आनन्तर्ये बिद-आदिभ्यः अञ्",
    why_dev               = "(सूत्रम् 4.1.104) अनृष्यानन्तर्ये बिदादिभ्योऽञ्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83', '4.1.95'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
