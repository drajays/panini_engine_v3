"""
7.1.21  अष्टाभ्य औश्  —  VIDHI

Padaccheda: अष्टाभ्यः औश्

अष्टाभ्य औश् (7.1.21)
Pāṭha: ashtadhyayi.com data.txt row i=71021 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup, is_stem
from engine.state import State
from phonology    import mk


def _site(state: State):
    """aṣṭā (the aṣṭan whose n has become ā, 7.2.84) before jas / śas: the sup is auś (aṣṭau)."""
    hit = anga_and_sup(state)      # no 6.4.1 gate: 6.4.8 is not gated either, and the luk / ādeśa must meet it as a rival (vipratiṣedha, para)
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "azwan") or anga.varnas[-1].slp1 != "A":
        return None
    if (sup.meta.get("upadesha_slp1") or "").strip() not in ("jas", "Sas") or sup.meta.get("aush_7_1_21") or "luk_lopa" in sup.tags:
        return None
    return sup


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    sup = _site(state)
    sup.meta["upadesha_slp1_original"] = sup.meta.get("upadesha_slp1")
    sup.meta["upadesha_slp1"] = "OS"
    sup.varnas = [mk("O")]            # auś: a śit ādeśa takes the place of the whole sup (1.1.55)
    sup.meta["aush_7_1_21"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "azwABya OS",
    text_dev              = "अष्टाभ्य औश्",
    samagra_slp1          = "azwAByaH jaS-SasoH OS",
    samagra_dev           = "अष्टाभ्यः जश्-शसोः औश्",
    padaccheda_dev        = "अष्टाभ्यः औश्",
    why_dev               = "(सूत्रम् 7.1.21) अष्टाभ्य औश्।",
    anuvritti_from        = ('7.1.1',),
    apavada_of            = ('7.1.22',),      # ṣaḍbhyo luk
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
