"""
7.4.72  अश्नोतेश्च  —  VIDHI

Padaccheda: अश्नोतेः च

अश्नोतेश्च (7.4.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_72_aSnoteSca_72"


def _site(state: State):
    """अश्नोतेश्च: aś (aśū vyāptau, svādi) takes nuṭ after the lengthened abhyāsa though it has but one hal — ānaśe."""
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" not in t.tags or not t.meta.get("7_4_70_done"):
            continue
        dh = state.terms[i + 1]
        if ("dhatu" in dh.tags and not dh.meta.get("7_4_71_done") and not dh.meta.get("7_4_72_done")
                and (dh.meta.get("upadesha_slp1") or "").replace("~", "") == "aSU"):
            return dh
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    dh = _site(state)
    if dh is None:
        return state
    from phonology import mk
    dh.varnas.insert(0, mk("n"))
    dh.meta["7_4_72_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.72",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "aSnoteSca",
    text_dev              = "अश्नोतेश्च",
    padaccheda_dev        = "अश्नोतेः च",
    why_dev               = "(सूत्रम् 7.4.72) अश्नोतेश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
