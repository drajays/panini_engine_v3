"""
3.1.54  आत्मनेपदेष्वन्यतरस्याम्  —  VIDHI

Padaccheda: आत्मनेपदेषु अन्यतरस्याम्

Krt suffix rule from dhatu: आत्मनेपदेष्वन्यतरस्याम् (54)
Pāṭha: ashtadhyayi.com data.txt row i=31054 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.ang_adesha import cli_and_root, parasmaipada, stem, to_ang, vikalpa_ang

_ROOTS = frozenset({"lipa~", "zica~", "hveY"})


def _site(state: State):
    """लिपिसिचिह्वः… वा, ātmanepada (3.1.53 gave the parasmaipada): either reading is an output — अलिपत / अलिप्त."""
    hit = cli_and_root(state)
    if hit is None or parasmaipada(state) or not vikalpa_ang("3.1.54"):
        return None
    return hit if (hit[1].meta.get("upadesha_slp1") or "").strip() in _ROOTS else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    to_ang(_site(state)[0])
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.54",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "AtmanepadezvanyatarasyAm",
    text_dev              = "आत्मनेपदेष्वन्यतरस्याम्",
    samagra_slp1          = "Atmanepadezu lipi-si-cihvaH cleH anyatarasyAmaN",
    samagra_dev           = "आत्मनेपदेषु लिपि-सि-चिह्वः च्लेः अन्यतरस्यामङ्",
    padaccheda_dev        = "आत्मनेपदेषु अन्यतरस्याम्",
    why_dev               = "धातोः [आत्मनेपदेष्वन्यतरस्याम्]-प्रत्ययः विहितः (३.१.54)।",
    anuvritti_from        = ('3.1.43', '3.1.44', '3.1.48', '3.1.52'),
    apavada_of            = ('3.1.44',),     # cli → sic is the utsarga; aṅ displaces it for these roots
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
