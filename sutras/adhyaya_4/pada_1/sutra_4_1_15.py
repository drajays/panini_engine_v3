"""
4.1.15  टिड्ढाणञ्द्वयसज्दघ्नञ्मात्रच्तयप्ठक्ठञ्कञ्क्वरपः  —  VIDHI (narrow: **P005-A** *kurucarī*)

*Śāstra (laghu):* under the *ṭit* *kṛt* class, *strīliṅga* takes **ṅīp**.

Engine: the strī adhikāra (4.1.3) is open and the stem is a-final, anupasarjana and ends in a ṭit or listed pratyaya (origin record):
**NIp** is appended (``append_nip``). The older P005-A arm (``kurucarī``) is kept beside it until that demo is retired.
Pāṭha: ashtadhyayi.com data.txt row i=41015 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra, origin
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_nip

_META_ARM = "corrected_v2_P005_A_4_1_15_arm"

# ṭit (an it-letter ṭ) and the listed pratyayas: ḍha, aṇ, añ, dvayasac, daghnac, mātrac, tayap, ṭhak, ṭhañ, kañ, kvarap
_LISTED = frozenset({"Qa", "aR", "aY", "dvayasac", "daGnac", "mAtrac", "tayap", "Wak", "WaY", "kaY", "kvarap"})


def _wanted(t) -> bool:
    """anupasarjana, a-final (``at`` runs through the whole strī adhikāra), made by a ṭit or listed pratyaya."""
    return (bool(t.varnas) and t.varnas[-1].slp1 == "a" and "upasarjana" not in t.tags
            and (origin.last_pratyaya(t) in _LISTED or origin.IT + "w" in t.tags))


def _site(state: State):
    return strI_site(state, _wanted)


def _legacy(state: State) -> bool:
    return len(state.terms) == 1 and bool(state.terms[0].meta.get("corrected_v2_P005_A_kurucara_stem"))


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy(state)


def act(state: State) -> State:
    if _site(state) is not None:
        return append_nip(state)
    if _legacy(state):
        state.terms.append(Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("NIp")),
            tags={"pratyaya", "upadesha"},
            meta={"upadesha_slp1": "NIp"},
        ))
        state.samjna_registry["4.1.15_P005_A_NIp"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="4.1.15",
    sutra_type=SutraType.VIDHI,
    text_slp1='wiqQARaYdvayasajdaGnaYmAtractayapWakWaYkaYkvarapaH',
    text_dev='टिड्ढाणञ्द्वयसज्दघ्नञ्मात्रच्तयप्ठक्ठञ्कञ्क्वरपः',
    samagra_slp1="pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt wit-Qa-aR-aY-dvayasac-daGnac-mAtrac-tayap-Wak-WaY-kaY-kvarapaH NIp",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् टित्-ढ-अण्-अञ्-द्वयसच्-दघ्नच्-मात्रच्-तयप्-ठक्-ठञ्-कञ्-क्वरपः ङीप्",
    padaccheda_dev="टि-इति / ङीप्",
    why_dev="टितः कृतः स्त्रियां ङीप् (प००५-अ, संक्षिप्तम्)।",
    anuvritti_from=("4.1.4",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
