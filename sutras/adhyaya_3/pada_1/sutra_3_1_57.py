"""
3.1.57  इरितो वा  —  VIDHI

Padaccheda: इरितः वा

Krt suffix rule from dhatu: इरितो वा (57)
Pāṭha: ashtadhyayi.com data.txt row i=31057 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.ang_adesha import cli_and_root, parasmaipada, stem, to_ang, vikalpa_ang

def _site(state: State):
    """इरितो धातोः (the dhātu bears the it-letter ir, 1.3.2 vārttika) in parasmaipada: अभिदत् / अभैत्सीत्."""
    hit = cli_and_root(state)
    if hit is None or not parasmaipada(state) or "irit" not in (hit[1].meta.get("it_samjna_names") or ()):
        return None
    return hit if vikalpa_ang("3.1.57") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    to_ang(_site(state)[0])
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.57",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "irito vA",
    text_dev              = "इरितो वा",
    samagra_slp1          = "iritaH cleH aN vA",
    samagra_dev           = "इरितः च्लेः अङ् वा",
    padaccheda_dev        = "इरितः वा",
    why_dev               = "धातोः [इरितो वा]-प्रत्ययः विहितः (३.१.57)।",
    anuvritti_from        = ('3.1.43', '3.1.44', '3.1.48', '3.1.52'),
    apavada_of            = ('3.1.44',),     # cli → sic is the utsarga; aṅ displaces it for these roots
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
