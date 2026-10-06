"""
1.3.7  चुटू  —  SAMJNA

Sources consulted:
- ashtadhyayi.com data.txt row i=13007
- Kāśikā: "कौञ्जायन्यः (ञ्य), जस् — ब्राह्मणाः, शाण्डिक्यः, टवर्गः — कुरुचरी (ट)"
- Cross-validation: regression tests tests/unit/test_it_prakarana.py
  (णिच् → इ with ṇit, जस् → अस्, ण्वुल् → वु, चिण् → इ; झि / छ / ठक् / ढक् keep
  their first sound), tests/unit/test_dASaraThi_apatya_iY.py

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — the **first sound** (*ādiḥ*, from 1.3.5; *pratyayasya*,
  from 1.3.6) of a **pratyaya** upadeśa, if it is a **cu**-varga (च छ ज झ ञ) or
  **ṭu**-varga (ट ठ ड ढ ण) consonant, is *it*.  Every pratyaya Term on the tape
  is examined (``is_pratyaya_upadesha``) — sup, tiṅ ādeśa, kṛt, taddhita,
  vikaraṇa, sanādi alike; never a dhātu, āgama or upasarga.

• **Sounds that are sthānin of a later vidhi are not *it*:** 7.1.2
  *āyaneyīnīyiyaḥ phaḍhakhachaghāṃ pratyayādīnām* (Kāśikā: "फ इत्येतस्यायनादेशो
  भवति … ढस्य एयादेशो भवति"), 7.1.3 *jho 'ntaḥ* ("प्रत्ययावयवस्य झस्य अन्त
  इत्ययमादेशो भवति") and 7.3.50 *ṭhasyekaḥ* replace the pratyaya-initial छ् / ढ्
  / झ् / ठ्.  Those vidhis would have no sthānin if 1.3.7 deleted it, so by
  their very teaching (*vacana-sāmarthya*) the four sounds stay
  (``_STHANIN_OF_LATER_ADESHA``): झि → अन्ति, छ → ईय, ढक् → एय, ठक् → इक.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.it_phonetic import IT_LOPA_TAGS
from engine.it_samjna import TAG_CUTU, is_pratyaya_upadesha, it_lopa_already_done, register_candidate_tag
from engine.state  import State

# चु (च छ ज झ ञ) ∪ टु (ट ठ ड ढ ण), SLP1.
_CU_TU = frozenset({"c", "C", "j", "J", "Y", "w", "W", "q", "Q", "R"})
# छ् ढ् (7.1.2), झ् (7.1.3), ठ् (7.3.50).
_STHANIN_OF_LATER_ADESHA = frozenset({"C", "Q", "J", "W"})


def term_candidates(state: State, ti: int) -> list[int]:
    t = state.terms[ti]
    if not is_pratyaya_upadesha(t) or it_lopa_already_done(t) or not t.varnas:
        return []
    v = t.varnas[0]
    if v.slp1 not in _CU_TU or v.slp1 in _STHANIN_OF_LATER_ADESHA:
        return []
    if v.tags & IT_LOPA_TAGS:
        return []
    return [0]


def cond(state: State) -> bool:
    return any(term_candidates(state, ti) for ti in range(len(state.terms)))


def act(state: State) -> State:
    for ti, t in enumerate(state.terms):
        for j in term_candidates(state, ti):
            v = t.varnas[j]
            v.tags.add("it_candidate_cutu")
            upa = t.meta.get("upadesha_slp1")
            state.samjna_registry[("it_cutu", ti, j, upa)] = frozenset({v.slp1})
    state.meta["__why_now_dev__"] = (
        "उपदेशे प्रत्ययस्य आदौ चवर्ग-टवर्गीयः वर्णः 'इत्'-संज्ञां प्राप्नोति; "
        "अयं वर्णः अनन्तरं १.३.९ इति लुप्यते (यथा णिच्, ण्वुल्, जस्, चिण्)। (१.३.७)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.7",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'cuwU',
    text_dev       = 'चुटू',
    samagra_slp1   = "upadeSe pratyayasya AdiH cuwU it",
    samagra_dev    = "उपदेशे प्रत्ययस्य आदिः चुटू इत्",
    padaccheda_dev = "चुटु",
    why_dev        = "प्रत्ययस्य आदौ चवर्ग-टवर्गीयः वर्णः ‘इत्’ संज्ञकः; लोपः १.३.९।",
    anuvritti_from = ("1.3.2", "1.3.5", "1.3.6"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
register_candidate_tag(TAG_CUTU, SUTRA.sutra_id)
