"""
3.1.58  जॄस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च  —  VIDHI

Padaccheda: जॄ-स्तम्भु-म्रुचु-म्लुचु-ग्रुचु-ग्लुचु-ग्लुञ्चु-श्विभ्यः च

Krt suffix rule from dhatu: जृस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च (58)
Pāṭha: ashtadhyayi.com data.txt row i=31058 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.ang_adesha import cli_and_root, parasmaipada, stem, to_ang, vikalpa_ang

_STEMS = frozenset({"stamB", "mruc", "mluc", "gruc", "gluc", "glunc", "zasj", "Svi"})   # Kāśikā 3.1.58 (जृष् is not in our dhātupāṭha data yet: ajarat/ajArIt)


def _site(state: State):
    hit = cli_and_root(state)
    if hit is None or not parasmaipada(state) or stem(hit[1]) not in _STEMS:
        return None
    return hit if vikalpa_ang("3.1.58") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    to_ang(_site(state)[0])
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.58",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'jFstamBumrucumlucugrucuglucugluYcuSviByaSca',
    text_dev              = 'जॄस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च',
    samagra_slp1          = "jF-stanBu-mrucu-mlucu-grucu-glucu-gluYcu-SviByaH cleH aN vA",
    samagra_dev           = "जॄ-स्तन्भु-म्रुचु-म्लुचु-ग्रुचु-ग्लुचु-ग्लुञ्चु-श्विभ्यः च्लेः अङ् वा",
    padaccheda_dev        = "जॄ-स्तम्भु-म्रुचु-म्लुचु-ग्रुचु-ग्लुचु-ग्लुञ्चु-श्विभ्यः च",
    why_dev               = "धातोः [जृस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च]-प्रत्ययः विहितः (३.१.58)।",
    anuvritti_from        = ('3.1.43', '3.1.44', '3.1.48', '3.1.52'),
    apavada_of            = ('3.1.44',),     # cli → sic is the utsarga; aṅ displaces it for these roots
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
