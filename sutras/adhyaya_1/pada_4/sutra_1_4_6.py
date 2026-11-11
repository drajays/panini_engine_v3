"""
1.4.6  ङिति ह्रस्वश्च  —  VIBHASHA

Kāśikā 1.4.6: before a ṅit sup (ṅe ṅasi ṅas ṅi) a strī stem that is hrasva (i, u) or an iyaṅuvaṅsthāna yU (śrī, bhrū) is optionally nadī:
kṛtyai / kṛtaye, dhenvai / dhenave, śriyai / śriye, bhruvai / bhruve; not strī-ākhya (agnaye) and not the word strī (striyai).
Taking the nadī reading withdraws the ghi-saṃjñā 1.4.7 gave (śeṣaḥ: what is neither nadī nor …); declining leaves it (mataye).
Pāṭha: ashtadhyayi.com data.txt row i=14006 (Art. 14).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from sutras.adhyaya_1.pada_4.sutra_1_4_3 import FEMININE_TAGS
from sutras.adhyaya_1.pada_4.sutra_1_4_4 import iyanuvan_sthana
from sutras.adhyaya_7.pada_3.sutra_7_3_112 import NGIT_SUPS

_NGIT = NGIT_SUPS | {"Ni"}          # ṅe ṅasi ṅas ṅi


def _eligible(state: State):
    """A strī stem — hrasva i/u (kṛti, dhenu: Kāśikā 1.4.6) or an iyaṅuvaṅsthāna yU (śrī, bhrū) — before a ṅit sup: nadī, optionally.
    Not an agni-type (not strī: 'strī-ākhyau'); the ghi-saṃjñā 1.4.7 gave it is withdrawn when the nadī reading is taken."""
    for i, t in enumerate(state.terms[:-1]):
        nxt = state.terms[i + 1]
        if "prātipadika" not in t.tags or not (FEMININE_TAGS & t.tags) or "nadi" in t.tags or not t.varnas:
            continue
        if "sup" not in nxt.tags or (nxt.meta.get("upadesha_slp1_original") or nxt.meta.get("upadesha_slp1") or "") not in _NGIT:
            continue
        if t.meta.get("1_4_6_done"):
            continue
        if t.varnas[-1].slp1 in ("i", "u") or iyanuvan_sthana(t):
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["nadI_vA_Niti"] = frozenset({"hrasva_strI_or_iyaNuvaN"})
    for t in _eligible(state):
        t.tags.add("nadi")
        t.tags.discard("ghi")
        t.meta["1_4_6_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.6",
    sutra_type             = SutraType.VIBHASHA,
    vibhasha_default       = True,
    vibhasha_scope         = lambda state: next(_eligible(state), None) is not None,
    text_slp1              = 'Niti hrasvaSca',
    text_dev               = 'ङिति ह्रस्वश्च',
    samagra_slp1           = "iyaN-uvaN-sTAnO yU stryAKyO hrasvaH ca Niti nadI vA astrI",
    samagra_dev            = "इयङ्-उवङ्-स्थानौ यू स्त्र्याख्यौ, ह्रस्वः च, ङिति नदी वा, अस्त्री",
    padaccheda_dev         = "ङिति / ह्रस्वः च",
    why_dev                = "ङित्-प्रत्यये परे नदीसंज्ञकस्य ह्रस्वश्च भवति।",
    anuvritti_from         = ("1.4.1", "1.4.3"),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
