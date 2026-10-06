"""
5.4.91  राजाहःसखिभ्यष्टच्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=54091
- Kāśikā: "राजः, अह्नः, सखः।" (समासान्त टच्)
- Cross-validation: tests/unit/test_bhattikavya_1_1.py (विबुधसखः)

राजन्/अहन्/सखि-final samāsa takes **टच्**. Then **6.4.148** drops सखि's इ.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "5_4_91_rAjAhassa_91"
_TAILS = ("saKi", "sakhi", "rAjan", "ahan", "ahan")


def _sakhi_or_rajan_ahan(state: State) -> bool:
    for t in reversed(state.terms):
        if not t.varnas:
            continue
        flat = "".join(v.slp1 for v in t.varnas)
        if any(flat.endswith(tail) for tail in ("saKi", "rAjan", "ahan")):
            return True
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"saKi", "saki", "rAjan", "ahan"}:
            return True
    return False


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any((t.meta.get("upadesha_slp1") or "").strip() == "wac" for t in state.terms):
        return False
    if not _sakhi_or_rajan_ahan(state):
        return False
    return True


def act(state: State) -> State:
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("wac")),
        tags={"pratyaya", "taddhita", "upadesha", "samasanta"},
        meta={"upadesha_slp1": "wac", "it_markers": {"w", "c"}},
    )
    state.terms.append(pr)
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["taddhita_kind"] = "5.4.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.91",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'rAjAhassaKiByazwac',
    text_dev              = 'राजाहस्सखिभ्यष्टच्',
    samagra_slp1          = "tatpuruzasya rAjA-ahan-saKiByaH wac",
    samagra_dev           = "तत्पुरुषस्य राजा-अहन्-सखिभ्यः टच्",
    padaccheda_dev        = "राज-अहः-सखिभ्यः टच्",
    why_dev               = "राजन्-अहन्-सखि-अन्ते समासे टच् (विबुधसखः)।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
