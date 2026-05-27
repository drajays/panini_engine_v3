"""
3.1.81  क्र्यादिभ्यः श्ना  —  VIDHI (narrow)

*Śāstra (laghu):* Kryādi roots take the *vikaraṇa* **śnā** before a *sarvadhātuka*
*tiṅ* *ādeśa*.

Engine (recipe-armed, CONSTITUTION Art. 2):
  • ``corrected_v2_P009_3_1_81_arm`` — **``krI``** dhātu + ``ta`` (**P009**).
  • ``corrected_v2_P012_3_1_81_arm`` — **``jYA``** dhātu + ``ta`` (**P012**).
Insert **SnA** immediately before the ``ta`` ``Term`` (optional *upasarga* etc.
before the dhātu).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_META_P009 = "corrected_v2_P009_3_1_81_arm"
_META_P012 = "corrected_v2_P012_3_1_81_arm"


def _stem(prev: Term) -> str:
    return "".join(v.slp1 for v in prev.varnas)


def _ta_idx_kryadi_snA(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "ta":
            continue
        if i == 0:
            continue
        prev = state.terms[i - 1]
        if "dhatu" not in prev.tags:
            continue
        st = _stem(prev)
        if st == "krI":
            return i
        if st == "jYA":
            return i
    return None


def cond(state: State) -> bool:
    return _ta_idx_kryadi_snA(state) is not None


def act(state: State) -> State:
    i = _ta_idx_kryadi_snA(state)
    if i is None:
        return state
    sna = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("SnA")),
        tags={"pratyaya", "upadesha", "vikaraṇa", "SnA_vikaraṇa", "ardhadhatuka"},
        meta={"upadesha_slp1": "SnA"},
    )
    state.terms.insert(i, sna)
    state.samjna_registry["3.1.81_kryAdi_SnA"] = True
    state.meta.pop(_META_P009, None)
    state.meta.pop(_META_P012, None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.81",
    sutra_type=SutraType.VIDHI,
    text_slp1="kryAdibhyaH SnA",
    text_dev="क्र्यादिभ्यः श्ना",
    padaccheda_dev="क्र्यादिभ्यः / श्ना",
    why_dev="क्र्यादिभ्यः श्ना-विकरणः — प००९ / प०१२ (संक्षिप्तम्)।",
    anuvritti_from=("3.1.75",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
