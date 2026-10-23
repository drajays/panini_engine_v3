"""
3.1.56  सर्त्तिशास्त्यर्तिभ्यश्च  —  VIDHI

Padaccheda: सर्त्ति-शास्ति-अर्तिभ्यः च

Krt suffix rule from dhatu: सर्त्तिशास्त्यर्तिभ्यश्च (56)
Pāṭha: ashtadhyayi.com data.txt row i=31056 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.ang_adesha import cli_and_root, parasmaipada, stem, to_ang, vikalpa_ang

_STEMS = frozenset({"sf", "SAs", "f"})      # सृ गतौ, शासु अनुशिष्टौ, ऋ गतौ: असरत्, अशिषत्, आरत्


def _site(state: State):
    hit = cli_and_root(state)
    return hit if hit is not None and parasmaipada(state) and stem(hit[1]) in _STEMS else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    to_ang(_site(state)[0])
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.56",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "sarttiSAstyartiByaSca",
    text_dev              = "सर्त्तिशास्त्यर्तिभ्यश्च",
    samagra_slp1          = "sarti-SAs-artiByaH cleH aN",
    samagra_dev           = "सर्ति-शास्-अर्तिभ्यः च्लेः अङ्",
    padaccheda_dev        = "सर्त्ति-शास्ति-अर्तिभ्यः च",
    why_dev               = "धातोः [सर्त्तिशास्त्यर्तिभ्यश्च]-प्रत्ययः विहितः (३.१.56)।",
    anuvritti_from        = ('3.1.43', '3.1.44', '3.1.48', '3.1.52'),
    apavada_of            = ('3.1.44',),     # cli → sic is the utsarga; aṅ displaces it for these roots
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
