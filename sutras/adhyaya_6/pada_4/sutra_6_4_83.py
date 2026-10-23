"""
6.4.83  ओः सुपि  —  VIDHI

Padaccheda: ओः सुपि

ओः सुपि (6.4.83)
Pāṭha: ashtadhyayi.com data.txt row i=64083 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, dhatu_aṅga, is_stem, n_vowels, samyoga_purva, vowel_initial
from phonology import mk

def _site(state: State):
    """ओः सुपि — the u/ū-final kṛdanta aṅga of a dhātu (खलपू, सुलू), anekāc and not after a conjunct, before an ac-initial sup: yaṇ
    (खलप्वौ, सुल्वौ); one-vowel भू / conjunct-final stems take uvaṅ (6.4.77); 6.4.85 withholds this for भू and सुधी."""
    hit = anga_and_sup(state, "6.4.83")
    if hit is None:
        return None
    anga, sup = hit
    if not dhatu_aṅga(anga) or anga.meta.get("6_4_83_yaN_done") or not vowel_initial(sup):
        return None
    if anga.varnas[-1].slp1 not in {"u", "U"} or n_vowels(anga) < 2 or samyoga_purva(anga):
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-1] = mk("v")
    anga.meta["6_4_83_yaN_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "6.4.83",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "oH supi",
    text_dev              = "ओः सुपि",
    samagra_slp1          = "anekAcaH aNgasya asaMyogapUrvasya oH DAtoH supi aci yaR",
    samagra_dev           = "अनेकाचः अङ्गस्य असंयोगपूर्वस्य ओः धातोः सुपि अचि यण्",
    padaccheda_dev        = "ओः सुपि",
    why_dev               = "(सूत्रम् 6.4.83) ओः सुपि।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.1.77', '6.4.77'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
