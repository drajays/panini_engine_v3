"""
1.2.49  लुक् तद्धितलुकि  —  VIDHI

*Padaccheda:* **लुक्** / **तद्धितलुकि**   (anuvṛtti: 1.2.48 striyoḥ — the strī-pratyaya of the prātipadika)

Kāśikā: when a taddhita takes luk, the strī-pratyaya before it takes luk too — āmalakyāḥ phalam āmalakam, badaram, kuvalam (4.3.163), jambu (jambūḥ, 4.3.165).

Engine: fires on a taddhita pratyaya that ``engine.luk`` took away *as luk* (not ślu/lup) while the stem ends in a strī-pratyaya (``origin_pratyaya:`` ṅīp, ṅīṣ,
ṅīn, ṭāp, cāp, ūṅ).  SHORTCUT S25: a lexical stem is one Term, so the strī-pratyaya is not a Term of its own; its luk is done on the stem's last varṇa and the
vowel the pratyaya had displaced comes back (ī, ā → a by the nimittāpāya of 6.4.148; ū → u) — "naimittikasyāpy apāyaḥ".
Pāṭha: ashtadhyayi.com data.txt row i=12049 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.luk   import lopa_kind
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_STRI = frozenset({"NIp", "NIz", "NIn", "wAp", "cAp", "qAp", "UN"})
_BACK = {"I": "a", "A": "a", "U": "u"}            # S25: what the strī-pratyaya had displaced


def _site(state: State):
    if len(state.terms) < 2:
        return None
    pr, stem = state.terms[-1], state.terms[-2]
    if pr.kind != "pratyaya" or "taddhita" not in pr.tags or lopa_kind(pr) != "luk":
        return None
    if not any(f"origin_pratyaya:{p}" in stem.tags for p in _STRI) or stem.meta.get("1.2.49_done"):
        return None
    if not stem.varnas or stem.varnas[-1].slp1 not in _BACK:
        return None
    return stem


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    stem = _site(state)
    stem.varnas[-1:] = parse_slp1_upadesha_sequence(_BACK[stem.varnas[-1].slp1])
    stem.meta["1.2.49_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.49",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "luk tadDitaluki",
    text_dev                = "लुक् तद्धितलुकि",
    samagra_slp1            = "luk tadDita-luki striyoH upasarjanasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev             = "लुक् तद्धित-लुकि स्त्रियोः उपसर्जनस्य",
    padaccheda_dev          = "लुक् / तद्धितलुकि",
    why_dev                 = "तद्धितस्य लुकि सति तत्पूर्वस्य स्त्रीप्रत्ययस्यापि लुक् (आमलक्याः फलम् → आमलकम्)।",
    anuvritti_from          = ("1.2.48",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
