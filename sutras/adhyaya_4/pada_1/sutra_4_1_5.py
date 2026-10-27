"""
4.1.5  ऋन्नेभ्यो ङीप्  —  VIDHI

Padaccheda: ऋत्-नेभ्यः ङीप्

ऋन्नेभ्यो ङीप् (4.1.5)
Pāṭha: ashtadhyayi.com data.txt row i=41005 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_nip


def _site(state: State):
    """A prātipadika that ends in ṛ (short or long) or in n.

    SHORTCUT S8: only a derived stem (a kṛt / taddhita made it: kartṛ, daṇḍin) — svasṛ, mātṛ, duhitṛ are strī words already and
    take no ṅīp, and the Lexicon does not yet say which avyutpanna stems are masculine words (rājan → rājñī)."""
    return strI_site(state, lambda t: bool(t.varnas) and t.varnas[-1].slp1 in ("f", "F", "n") and origin.last_pratyaya(t) is not None)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_nip(state) if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fnneByo NIp",
    text_dev              = "ऋन्नेभ्यो ङीप्",
    samagra_slp1          = "ft-neByaH prAtipadikAta striyAm NIp pratyayaH",
    samagra_dev           = "ऋत्-नेभ्यः प्रातिपदिकात स्त्रियाम् ङीप् प्रत्ययः",
    padaccheda_dev        = "ऋत्-नेभ्यः ङीप्",
    why_dev               = "(सूत्रम् 4.1.5) ऋन्नेभ्यो ङीप्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
