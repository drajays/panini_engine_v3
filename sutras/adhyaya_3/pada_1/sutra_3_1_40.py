"""
3.1.40  कृञ्चानुप्रयुज्यते लिटि  —  VIDHI (narrow: *kṛñ* anuprayoga in *liṭ*)

Teaching **P014** (*īkṣāñcakre*): after the **ām**-periphrastic stem
(**``IkzAm``**), append **``kf``** as the auxiliary root and a fresh **liṭ**
placeholder for the *tin* spine.

Engine:
  • ``state.meta['corrected_v2_P014_3_1_40_anuprayoga_arm']``
  • expects final *Term* to be **``IkzAm``** *prātipadika* (no *liṭ* yet)
Pāṭha: ashtadhyayi.com data.txt row i=31040 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> bool:
    if not state.terms:
        return False
    t = state.terms[-1]
    return "prātipadika" in t.tags and bool(t.meta.get("am_anta_2_4_81"))   # ām-anta, liṭ luk'd (2.4.81)


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    kf = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kf")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "kf"},
    )
    lit = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("liT")),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "liT"},
    )
    if lit.varnas and lit.varnas[-1].slp1 == "T":
        del lit.varnas[-1]
    state.terms.extend([kf, lit])
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.40",
    sutra_type=SutraType.VIDHI,
    text_slp1="kfY cAnuprayujyate liwi",
    text_dev="कृञ्चानुप्रयुज्यते लिटि",
    samagra_slp1="AmaH kfY liwi anuprayujyate",
    samagra_dev="आमः कृञ् लिटि अनुप्रयुज्यते",
    padaccheda_dev="कृञ् / च / अनुप्रयुज्यते / लिटि",
    why_dev="लिटि अनुप्रयोगे कृञ्-धातुः पुनः लिट्-प्रत्ययः — P014।",
    anuvritti_from=("3.1.35",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
