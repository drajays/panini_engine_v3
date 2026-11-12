"""
3.4.111  लङः शाकटायनस्यैव  —  VIDHI

Padaccheda: लङः शाकटायनस्य एव

krt-suffix rule: लङः शाकटायनस्यैव
Pāṭha: ashtadhyayi.com data.txt row i=34111 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_3.pada_4.sutra_3_4_108 import _find_jhi_tin, act as _jus


def cond(state: State) -> bool:
    return _find_jhi_tin(state, "3.4.111") is not None


def act(state: State) -> State:
    return _jus(state, "3.4.111")


SUTRA = SutraRecord(
    sutra_id              = "3.4.111",
    sutra_type            = SutraType.VIBHASHA,      # Śākaṭāyana's view only: the others keep 7.1.3 (ayAn)
    vibhasha_default      = False,
    r1_form_identity_exempt = True,
    text_slp1             = "laNaH SAkawAyanasyEva",
    text_dev              = "लङः शाकटायनस्यैव",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH lasya laNaH SAkawAyanasya eva JeH jus AtaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः लस्य लङः शाकटायनस्य एव झेः जुस् आतः",
    padaccheda_dev        = "लङः शाकटायनस्य एव",
    why_dev               = "धातोः प्रत्ययः (३.4.111)।",
    anuvritti_from        = ('3.1.1',),
    apavada_of            = ("7.1.3", "7.1.4"),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
