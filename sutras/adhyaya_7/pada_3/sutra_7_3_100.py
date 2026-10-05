"""
7.3.100  अदः सर्वेषाम्  —  VIDHI

Padaccheda: अदः सर्वेषाम्

अदः सर्वेषाम् (7.3.100)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk


def _site(state: State):
    """अदः सर्वेषाम्: ad takes an अट् before the apṛkta त्/स् of laṅ — आदत्, आदः (KV/SK; 'सर्वेषाम्' ⇒ nitya)."""
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("7_3_100_done") or (dh.meta.get("upadesha_slp1") or "").strip() != "ada~":
            continue
        tin = state.terms[i + 1]
        if len(tin.varnas) == 1 and tin.varnas[0].slp1 in ("t", "s") and "tin_adesha_3_4_78" in tin.tags \
                and (tin.meta.get("source_lakara_upadesha") or "").strip() == "laG":
            return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is not None:
        state.terms[i].meta["7_3_100_done"] = True
        state.terms.insert(i + 1, Term(kind="pratyaya", varnas=[mk("a")], tags={"pratyaya", "agama", "at_agama_7_3_100"},
                                       meta={"upadesha_slp1": "aw"}))
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "adaH sarvezAm",
    text_dev              = "अदः सर्वेषाम्",
    padaccheda_dev        = "अदः सर्वेषाम्",
    why_dev               = "(सूत्रम् 7.3.100) अदः सर्वेषाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
