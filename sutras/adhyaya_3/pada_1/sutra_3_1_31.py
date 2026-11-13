"""
3.1.31  आयादय आर्धधातुके वा  —  VIBHASHA

Kāśikā: "आर्धधातुकविषय आर्धधातुकविवक्षायामायादयः प्रत्यया वा भवन्ति। गोप्ता, गोपायिता।"
Narrow: the āya of 3.1.28 (gupū, dhūp, vicch, paṇ, pan) in an ārdhadhātuka lakāra; īyaṅ (3.1.29), ṇiṅ (3.1.30) not yet.
Same insertion as 3.1.28 (`insert_aya`); the vā is the vibhāṣā machinery (engine.vikalpa): taken -> gopāyitā, declined -> gopitā.

Pāṭha: ashtadhyayi.com data.txt row i=31031 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_3.pada_1.sutra_3_1_28 import _ARDHA, aya_site, insert_aya


def cond(state: State) -> bool:
    return aya_site(state, _ARDHA) is not None


def act(state: State) -> State:
    i = aya_site(state, _ARDHA)
    return state if i is None else insert_aya(state, i)


SUTRA = SutraRecord(
    sutra_id              = "3.1.31",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = 'AyAdaya ArDaDAtuke vA',
    text_dev              = 'आयादय आर्धधातुके वा',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH AyAdayaH ArDaDAtuke vA",
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः आयादयः आर्धधातुके वा",
    padaccheda_dev        = "आय्-आदयः आर्धधातुके वा",
    why_dev               = "आर्धधातुके आयादयो वा (गोप्ता, गोपायिता)।",
    anuvritti_from        = ('3.1.28',),
    vibhasha_default      = False,      # the plain ārdhadhātuka is the first reading: gopitā (the vā adds gopāyitā)
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
