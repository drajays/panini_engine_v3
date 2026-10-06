"""
1.3.6  षः प्रत्ययस्य  —  SAMJNA

Sources consulted:
- ashtadhyayi.com data.txt row i=13006
- Kāśikā: "नर्तकी, रजकी (ष्वुन्)" — pratyudāharaṇa: "प्रत्ययस्येति किम्? षोडः, षण्डः"
- Cross-validation: regression tests tests/unit/test_it_prakarana.py
  (ष्वुन् → वु with ṣit; dhātu षह् and stem-medial ष् untouched)

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — the **first sound** (*ādiḥ*, anuvṛtti from 1.3.5) of a
  **pratyaya** upadeśa, if it is ष्, is *it*.  Not a dhātu's ष् (षोडः) and not
  a later ष् (इष्ठन्'s ष् is not *ādi*).

• **Scope:** every Term for which ``is_pratyaya_upadesha`` holds; a Term already
  through **1.3.9** is not re-examined.  **1.3.9** records the *ṣit* name used by
  4.1.41 *ṣidgaurādibhyaś ca*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.it_phonetic import IT_LOPA_TAGS
from engine.it_samjna import TAG_SHA, is_pratyaya_upadesha, it_lopa_already_done, register_candidate_tag
from engine.state  import State


def term_candidates(state: State, ti: int) -> list[int]:
    t = state.terms[ti]
    if not is_pratyaya_upadesha(t) or it_lopa_already_done(t) or not t.varnas:
        return []
    v = t.varnas[0]
    if v.slp1 != "z" or v.tags & IT_LOPA_TAGS:
        return []
    return [0]


def cond(state: State) -> bool:
    return any(term_candidates(state, ti) for ti in range(len(state.terms)))


def act(state: State) -> State:
    for ti, t in enumerate(state.terms):
        for j in term_candidates(state, ti):
            t.varnas[j].tags.add("it_candidate_sha_pratyaya")
            state.samjna_registry[("it_sha_pratyaya", ti, j)] = frozenset({"z"})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.6",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "zaH pratyayasya",
    text_dev       = "षः प्रत्ययस्य",
    samagra_slp1   = "upadeSe pratyayasya AdiH zaH it",
    samagra_dev    = "उपदेशे प्रत्ययस्य आदिः षः इत्",
    padaccheda_dev = "षः प्रत्ययस्य",
    why_dev        = "प्रत्ययस्य आदौ ष्-वर्णः ‘इत्’ संज्ञकः; लोपः १.३.९।",
    anuvritti_from = ("1.3.2", "1.3.5"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
register_candidate_tag(TAG_SHA, SUTRA.sutra_id)
