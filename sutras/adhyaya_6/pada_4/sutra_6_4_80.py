"""
6.4.80  वाऽम्शसोः  —  VIDHI

Padaccheda: वा अम्-शसोः

वाऽम्शसोः (6.4.80)
Pāṭha: ashtadhyayi.com data.txt row i=64080 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup, is_stem, vowel_initial
from engine.state import State

def _site(state: State):
    """वाऽम्शसोः — before am / śas the iyaṅ of 6.4.79 is optional: स्त्रियम् / स्त्रीम्, स्त्रियः / स्त्रीः. The reading that keeps ī is this rule's."""
    hit = anga_and_sup(state, "6.4.80")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "strI", tadanta=True) or anga.varnas[-1].slp1 != "I" or anga.meta.get("6_4_79_done") or anga.meta.get("6_4_80_kept"):
        return None
    if (sup.meta.get("upadesha_slp1") or "").strip() not in {"am", "Sas", "am~", "Sas~"} or not vowel_initial(sup):
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).meta["6_4_80_kept"] = True      # the ī stays; 6.4.79 stands aside, 6.1.101 / 6.1.102 / 6.1.103 join the vowels
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.80",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_scope        = lambda state: _site(state) is not None,     # the vā gate only where the rule has a site (else explore() would see a phantom option)
    vibhasha_default      = False,     # iyaṅ (6.4.79) is the default reading; choose({"6.4.80": True}) / explore() give strIm, strIH
    text_slp1             = 'vAmSasoH',
    text_dev              = 'वाऽम्शसोः',
    samagra_slp1          = "amSasoH striyAH vA iyaN",
    samagra_dev           = "अम्शसोः स्त्रियाः वा इयङ्",
    padaccheda_dev        = "वा अम्-शसोः",
    why_dev               = "(सूत्रम् 6.4.80) वाऽम्शसोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
