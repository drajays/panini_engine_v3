"""
3.1.100  गदमदचरयमश्चानुपसर्गे  —  VIDHI

Padaccheda: गद-मद-चर-यमः च अन्-उपसर्गे

Krt suffix rule from dhatu: गदमदचरयमश्चानुपसर्गे (100)
Pāṭha: ashtadhyayi.com data.txt row i=31100 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem



def cond(state: State) -> bool:
    """gad, mad, car, yam, without an upasarga → yat (gadyam, madyam, caryam, yamyam)."""
    return kftya_open(state, "3.1.100") and kftya_stem(state) in ("gad", "mad", "car", "yam") and len(state.terms) == 1


def act(state: State) -> State:
    return kftya_attach(state, "3.1.100", "yat")


SUTRA = SutraRecord(
    sutra_id              = "3.1.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gadamadacarayamaScAnupasarge",
    text_dev              = "गदमदचरयमश्चानुपसर्गे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH gada-mada-cara-yamaH ca anupasarge kft yat",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः गद-मद-चर-यमः च अनुपसर्गे कृत् यत्",
    padaccheda_dev        = "गद-मद-चर-यमः च अन्-उपसर्गे",
    why_dev               = "धातोः [गदमदचरयमश्चानुपसर्गे]-प्रत्ययः विहितः (३.१.100)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.124',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
