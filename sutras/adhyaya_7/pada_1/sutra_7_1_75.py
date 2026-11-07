"""
7.1.75  अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः  —  VIDHI

Padaccheda: अस्थि-दधि-सक्थि-अक्ष्णाम् अनङ् उदात्तः

अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः (7.1.75)
Pāṭha: ashtadhyayi.com data.txt row i=71075 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup, is_stem, vowel_initial
from engine.state import State
from phonology    import mk

_TRTIYADI = frozenset({"vib_trtiya", "vib_caturthi", "vib_panchami", "vib_shashthi", "vib_saptami"})


def _site(state: State):
    """asthi, dadhi, sakthi, akṣi (and what ends in them: priyadadhi, 'anapuṃsakasyāpi tadantagrahaṇam', Kāśikā) before an ac-initial sup of the
    third vibhakti on: the final i is replaced by an (anaṅ, ṅit): dadhn-ā, asthn-e, akṣṇ-oḥ."""
    hit = anga_and_sup(state)
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "asTi", "daDi", "sakTi", "akzi", tadanta=True) or anga.varnas[-1].slp1 != "i" or anga.meta.get("anan_7_1_75"):
        return None
    if not (_TRTIYADI & sup.tags) or not vowel_initial(sup) or "luk_lopa" in sup.tags:
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-1:] = [mk("a"), mk("n")]      # anaṅ replaces the final i; 6.4.134 (allopo 'naḥ) then drops its a before the bha-sup
    anga.meta["anan_7_1_75"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asTidaDisakTyakzRAmanaNudAttaH",
    text_dev              = "अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः",
    samagra_slp1          = "asTi-daDi-sakTi-akzRAm tftIyAdizu aci anaN udAttaH",
    samagra_dev           = "अस्थि-दधि-सक्थि-अक्ष्णाम् तृतीयादिषु अचि अनङ् उदात्तः",
    padaccheda_dev        = "अस्थि-दधि-सक्थि-अक्ष्णाम् अनङ् उदात्तः",
    why_dev               = "(सूत्रम् 7.1.75) अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः।",
    anuvritti_from        = ('7.1.1',),
    apavada_of            = ('7.1.73', '7.3.120'),      # iko 'ci vibhaktau (the num of the neuter) · āṇ nā (ṭā → nā after a ghi): dadhnā, not *dadhinā
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
