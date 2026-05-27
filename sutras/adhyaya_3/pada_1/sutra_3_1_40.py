"""
3.1.40  कृञ्चानुप्रयुज्यते लिटि  —  VIDHI (narrow: *kṛñ* anuprayoga in *liṭ*)

Teaching **P014** (*īkṣāñcakre*): after the **ām**-periphrastic stem
(**``IkzAm``**), append **``kf``** as the auxiliary root and a fresh **liṭ**
placeholder for the *tin* spine.

Engine:
  • ``state.meta['corrected_v2_P014_3_1_40_anuprayoga_arm']``
  • expects final *Term* to be **``IkzAm``** *prātipadika* (no *liṭ* yet)
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> bool:
    if not state.terms:
        return False
    t = state.terms[-1]
    if "prātipadika" not in t.tags:
        return False
    flat = "".join(v.slp1 for v in t.varnas)
    return flat == "IkzAm"


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
    padaccheda_dev="कृञ् / च / अनुप्रयुज्यते / लिटि",
    why_dev="लिटि अनुप्रयोगे कृञ्-धातुः पुनः लिट्-प्रत्ययः — P014।",
    anuvritti_from=("3.1.35",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
