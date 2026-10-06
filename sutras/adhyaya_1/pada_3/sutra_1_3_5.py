"""
1.3.5  आदिर्ञिटुडवः  —  SAMJNA

Sources consulted:
- ashtadhyayi.com data.txt row i=13005
- Kāśikā: "आदिशब्दः प्रत्येकमभिसंबध्यते। ञिमिदा — मिन्नः। ञिधृषा — धृष्टः। ञिक्ष्विदा — क्ष्विण्णः"
- Cross-validation: regression tests tests/unit/test_it_prakarana.py
  (डुपचँष् → पच् with ḍvit, ञिमिदाँ → मिद् with ñīt, टुओँश्वि → श्वि with ṭvit)

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — the **unit** ञि / टु / डु standing at the very beginning
  (*ādiḥ*) of a **dhātu** upadeśa is *it*.  Only dhātus are taught with these
  (``is_dhatu_upadesha``); a pratyaya's initial ट् / ञ् alone (टा, ञ्य) is **1.3.7**'s.

• **Unit, not letter:** both Varṇas get ``it_candidate_nit_tu_du``; **1.3.9**
  records one *it* named *ñīt* / *ṭvit* / *ḍvit* — the nimitta of 3.2.187
  *ñītaḥ ktaḥ*, 3.3.89 *ṭvito 'thuc*, 3.3.88 *ḍvitaḥ ktriḥ*.  A plain initial
  ट् (टिकृँ, अटँ) is untouched.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.it_phonetic import IT_LOPA_TAGS
from engine.it_samjna import TAG_NIT_TU_DU, is_dhatu_upadesha, it_lopa_already_done, register_candidate_tag
from engine.state  import State

# ञि · टु · डु — the hal and the vowel that together form the marker (SLP1).
_ADI_UNITS = {"Y": "i", "w": "u", "q": "u"}


def term_candidates(state: State, ti: int) -> list[int]:
    t = state.terms[ti]
    if not is_dhatu_upadesha(t) or it_lopa_already_done(t):
        return []
    vs = t.varnas
    if len(vs) < 2 or vs[0].slp1 not in _ADI_UNITS or vs[1].slp1 != _ADI_UNITS[vs[0].slp1]:
        return []
    if vs[0].tags & IT_LOPA_TAGS:
        return []
    return [0, 1]


def cond(state: State) -> bool:
    return any(term_candidates(state, ti) for ti in range(len(state.terms)))


def act(state: State) -> State:
    for ti, t in enumerate(state.terms):
        cands = term_candidates(state, ti)
        if not cands:
            continue
        for j in cands:
            t.varnas[j].tags.add("it_candidate_nit_tu_du")
        h, a = t.varnas[0].slp1, t.varnas[1].slp1
        state.samjna_registry[("it_nit_tu_du", ti, 0, h)] = frozenset({h, a})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.5",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'AdirYiwuqavaH',
    text_dev       = 'आदिर्ञिटुडवः',
    samagra_slp1   = "upadeSe AdiH YiwuqavaH it",
    samagra_dev    = "उपदेशे आदिः ञिटुडवः इत्",
    padaccheda_dev = "आदिः ञि-टु-ड-वः",
    why_dev        = "धातोः आदौ ञि-टु-डु इति समुदायः ‘इत्’ संज्ञकः; लोपः १.३.९।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
register_candidate_tag(TAG_NIT_TU_DU, SUTRA.sutra_id)
