"""
4.1.15  टिड्ढाणञ्द्वयसज्दघ्नञ्मात्रच्तयप्ठक्ठञ्कञ्क्वरपः  —  VIDHI (narrow: **P005-A** *kurucarī*)

*Śāstra (laghu):* under the *ṭit* *kṛt* class, *strīliṅga* takes **ṅīp**.

Engine: when ``corrected_v2_P005_A_4_1_15_arm`` and a single merged stem carries
``corrected_v2_P005_A_kurucara_stem``, append **NIp** (ङीप्; SLP1 ``N`` = ङ्, not ``Ng``)
as an affix ``Term``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_META_ARM = "corrected_v2_P005_A_4_1_15_arm"


def cond(state: State) -> bool:
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    return bool(t0.meta.get("corrected_v2_P005_A_kurucara_stem"))


def act(state: State) -> State:
    if not cond(state):
        return state
    nIp = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("NIp")),
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "NIp"},
    )
    state.terms.append(nIp)
    state.samjna_registry["4.1.15_P005_A_NIp"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="4.1.15",
    sutra_type=SutraType.VIDHI,
    text_slp1="tiqqARaYdvayasaj... (narrow P005-A NIp)",
    text_dev="टिड्ढाणञ्… — प००५-अ ङीप्",
    padaccheda_dev="टि-इति / ङीप्",
    why_dev="टितः कृतः स्त्रियां ङीप् (प००५-अ, संक्षिप्तम्)।",
    anuvritti_from=("4.1.4",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
