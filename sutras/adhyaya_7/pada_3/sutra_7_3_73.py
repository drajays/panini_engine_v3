"""
7.3.73  लुग्वा दुहदिहलिहगुहामात्मनेपदे दन्त्ये  —  VIBHASHA

Padaccheda: लुक् वा दुह-दिह-लिह-गुहाम् आत्मनेपदे दन्त्ये

Kāśikā 7.3.73: duh, dih, lih, guh before an ātmanepada ending that begins with a dental: the ksa (3.1.45) may be luk-deleted
(adugdha / adhukṣata, adihvahi / adhikṣāvahi, alīḍha / alikṣata). The v of vahi counts as dental (dantyoṣṭhya, Kāśikā:
'दन्त्योष्ठ्योऽपि वकारो दन्त्य इति गृह्यते'). The kept ksa is the default reading; explore() gives the luk one.
luk = the pratyaya is deleted without leaving a sthānivadbhāva trace (1.1.61 lup family; compare 2.4.72).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_ROOTS = frozenset({"duh", "dih", "lih", "guh"})
_DANTYA = frozenset("tTdDnslv")          # the dental series, ṣ/ś excluded; v = dantyoṣṭhya


def _site(state: State):
    for i, t in enumerate(state.terms[:-2]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or "".join(v.slp1 for v in t.varnas) not in _ROOTS:
            continue
        k, tin = state.terms[i + 1], state.terms[i + 2]
        if (k.meta.get("upadesha_slp1") or "").strip() != "ksa" or not tin.varnas:
            continue
        if "tin_adesha_3_4_78" in tin.tags and "atmanepada" in tin.tags and tin.varnas[0].slp1 in _DANTYA:
            return i + 1
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    k = _site(state)
    state.terms[k - 1].tags.add("ksa_luk")
    del state.terms[k]
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.73",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "lugvA duhadihalihaguhAmAtmanepade dantye",
    text_dev              = "लुग्वा दुहदिहलिहगुहामात्मनेपदे दन्त्ये",
    samagra_slp1          = "aNgasya luk vA duhadihalihaguhAm Atmanepade dantye ksasya aci",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य लुक् वा दुहदिहलिहगुहाम् आत्मनेपदे दन्त्ये क्सस्य अचि",
    padaccheda_dev        = "लुक् वा दुह-दिह-लिह-गुहाम् आत्मनेपदे दन्त्ये",
    why_dev               = "(सूत्रम् 7.3.73) लुग्वा दुहदिहलिहगुहामात्मनेपदे दन्त्ये।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # the ksa stays by default (adhukṣata); explore() gives the luk reading (adugdha)
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
