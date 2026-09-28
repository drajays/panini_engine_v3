"""
7.3.98  रुदश्च पञ्चभ्यः  —  VIDHI

Padaccheda: रुदः (व्यत्ययेन बहुवचनस्यैकत्वम्) च पञ्चभ्यः

रुदश्च पञ्चभ्यः (7.3.98)
"""
from __future__ import annotations
from engine.state import Term
from phonology import mk

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_98_rudaSca_98"


_RUDADI = frozenset({"rudi~r", "Yizvapa~", "Svasa~", "ana~", "jakza~"})


def _find(state: State) -> int | None:
    """रुदश्च पञ्चभ्यः (अस्तिसिचोऽपृक्ते, 7.3.96 — ईट्): after the rudādi five, an
    apṛkta ending (laṅ's t / s after 3.4.100 इतश्च) takes īṭ — अरोदीत्, अरोदीः."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() not in _RUDADI:
            return None
        tin = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if tin is None or "tin_adesha_3_4_78" not in tin.tags or tin.meta.get("7_3_98_done"):
            return None
        sthani = (tin.meta.get("source_lakara_upadesha") or "").strip()
        up = (tin.meta.get("upadesha_slp1") or "").strip()
        if sthani.endswith("G") and up in {"tip", "sip"}:
            return state.terms.index(tin)
        return None
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    j = _find(state)
    if j is None:
        return state
    tin = state.terms[j]
    # the āgama belongs to its affix (1.1.46): same sārvadhātuka/kṅit status,
    # so the root still takes guṇa before pit t (अरोदीत्)
    keep = {"sarvadhatuka", "sarvadhatuka_3_4_113", "kngiti"} & tin.tags
    state.terms.insert(j, Term(kind="pratyaya", varnas=[mk("I")], tags={"agama"} | keep,
                               meta={"upadesha_slp1": "Iw"}))
    state.terms[j + 1].meta["7_3_98_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.98",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "rudaSca paYcaByaH",
    text_dev              = "रुदश्च पञ्चभ्यः",
    padaccheda_dev        = "रुदः (व्यत्ययेन बहुवचनस्यैकत्वम्) च पञ्चभ्यः",
    why_dev               = "(सूत्रम् 7.3.98) रुदश्च पञ्चभ्यः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
