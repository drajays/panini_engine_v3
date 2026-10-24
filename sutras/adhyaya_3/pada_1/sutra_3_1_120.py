"""
3.1.120  विभाषा कृवृषोः  —  VIDHI

Padaccheda: विभाषा कृ-वृषोः

Krt suffix rule from dhatu: विभाषा कृवृषोः (120)
Pāṭha: ashtadhyayi.com data.txt row i=31120 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem

def cond(state: State) -> bool:
    """kṛ, vṛṣ → kyap or the other kṛtyas (kṛtyam, kāryam; vṛṣyam)."""
    return kftya_open(state, "3.1.120") and kftya_stem(state) in ("kf", "vfz")


def act(state: State) -> State:
    return kftya_attach(state, "3.1.120", "kyap")


SUTRA = SutraRecord(
    sutra_id              = "3.1.120",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA kfvfzoH",
    text_dev              = "विभाषा कृवृषोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH viBAzA kfvfzoH kft kyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः विभाषा कृवृषोः कृत् क्यप्",
    padaccheda_dev        = "विभाषा कृ-वृषोः",
    why_dev               = "धातोः [विभाषा कृवृषोः]-प्रत्ययः विहितः (३.१.120)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.124',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
