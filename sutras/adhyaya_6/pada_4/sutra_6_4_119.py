"""
6.4.119  घ्वसोरेद्धावभ्यासलोपश्च  —  VIDHI

Padaccheda: घु-असोः एत् हौ अभ्यास-लोपः च

घ्वसोरेद्धावभ्यासलोपश्च (6.4.119)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_GHU = frozenset({"quDAY", "qudAY", "dAN", "dAN~"})        # ghu (1.1.20 दाधा घ्वदाप्) — not dāp / dai
_HI = frozenset({"hi", "Di"})


def _site(state: State):
    """घ्वसोरेद्धौ: before hi, the ā of ghu (dā, dhā) and the as of 'as' become e, and the abhyāsa goes — धेहि, देहि, एधि."""
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or "abhyasa" in dh.tags or dh.meta.get("6_4_119_done"):
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None or "pratyaya" not in nxt.tags or (nxt.meta.get("upadesha_slp1") or "").strip() not in _HI:
            continue
        flat = "".join(v.slp1 for v in dh.varnas)
        up = (dh.meta.get("upadesha_slp1") or "").strip()
        if (up == "asa~" and flat == "as") or (up in _GHU and flat in ("dA", "DA")):
            return i, dh
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    hit = _site(state)
    if hit is None:
        return state
    i, dh = hit
    keep = {"dhatu_adesha_v"}
    if "".join(v.slp1 for v in dh.varnas) == "as":
        dh.varnas = [mk("e", *keep)]
    else:
        old = dh.varnas[-1]
        dh.varnas[-1] = mk("e", *((old.tags - {"mula_dhatu_v"}) | keep))
        state.terms[:] = [t for t in state.terms if not ("abhyasa" in t.tags and t is not dh)]     # abhyāsalopaḥ
    dh.meta["6_4_119_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "GvasoredDAvaByAsalopaSca",
    text_dev              = "घ्वसोरेद्धावभ्यासलोपश्च",
    padaccheda_dev        = "घु-असोः एत् हौ अभ्यास-लोपः च",
    why_dev               = "(सूत्रम् 6.4.119) घ्वसोरेद्धावभ्यासलोपश्च।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ("6.4.112",),        # e (and the abhyāsa-lopa) over the ā-lopa of an abhyasta aṅga
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
