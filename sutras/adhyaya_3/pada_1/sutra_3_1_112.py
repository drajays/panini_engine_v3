"""
3.1.112  भृञोऽसंज्ञायाम्  —  VIDHI

Padaccheda: भृञः अ-संज्ञायाम्

Krt suffix rule from dhatu: भृञोऽसंज्ञायाम् (112)
Pāṭha: ashtadhyayi.com data.txt row i=31112 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem

def cond(state: State) -> bool:
    """bhṛ → kyap when no saṃjñā is meant (bhṛtyāḥ karmakarāḥ)."""
    return kftya_open(state, "3.1.112") and kftya_stem(state) == "Bf"


def act(state: State) -> State:
    return kftya_attach(state, "3.1.112", "kyap")


SUTRA = SutraRecord(
    sutra_id              = "3.1.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'BfYosaMjYAyAm',
    text_dev              = 'भृञोऽसंज्ञायाम्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH BfYaH asaMjYAyAm kft kyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः भृञः असंज्ञायाम् कृत् क्यप्",
    padaccheda_dev        = "भृञः अ-संज्ञायाम्",
    why_dev               = "धातोः [भृञोऽसंज्ञायाम्]-प्रत्ययः विहितः (३.१.112)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.97', '3.1.124'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
