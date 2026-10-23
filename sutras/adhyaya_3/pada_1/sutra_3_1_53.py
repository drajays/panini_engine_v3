"""
3.1.53  लिपिसिचिह्वश्च  —  VIDHI

Padaccheda: लिपि-सिचि-ह्वः च

Krt suffix rule from dhatu: लिपिसिचिह्वश्च (53)
Pāṭha: ashtadhyayi.com data.txt row i=31053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.ang_adesha import cli_and_root, parasmaipada, stem, to_ang, vikalpa_ang

_ROOTS = frozenset({"lipa~", "zica~", "hveY"})      # लिप् (उपदेहे), सिच् (क्षरणे), ह्वेञ् (स्पर्धायाम्): Kāśikā 3.1.53


def _site(state: State):
    hit = cli_and_root(state)
    if hit is None or not parasmaipada(state):
        return None
    return hit if (hit[1].meta.get("upadesha_slp1") or "").strip() in _ROOTS else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    to_ang(_site(state)[0])
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.53",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "lipisicihvaSca",
    text_dev              = "लिपिसिचिह्वश्च",
    samagra_slp1          = "lipi-sici-hvaH cleH aN",
    samagra_dev           = "लिपि-सिचि-ह्वः च्लेः अङ्",
    padaccheda_dev        = "लिपि-सिचि-ह्वः च",
    why_dev               = "धातोः [लिपिसिचिह्वश्च]-प्रत्ययः विहितः (३.१.53)।",
    anuvritti_from        = ('3.1.43', '3.1.44', '3.1.48', '3.1.52'),
    apavada_of            = ('3.1.44',),     # cli → sic is the utsarga; aṅ displaces it for these roots
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
