"""
7.4.33  क्यचि च  —  VIDHI

Padaccheda: क्यचि च

क्यचि च (7.4.33)
Pāṭha: ashtadhyayi.com data.txt row i=74033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _site(state: State):
    """The aṅga's final avarṇa (a / ā — 'asya', 7.4.32) before kyac; a lugged sup between them is no letter."""
    for j, ky in enumerate(state.terms):
        if ky.kind != "pratyaya" or ky.meta.get("upadesha_slp1") != "kyac":
            continue
        ang = next((t for t in reversed(state.terms[:j]) if t.varnas), None)
        if ang is not None and ang.varnas[-1].slp1 in ("a", "A") and "prakriti" == ang.kind:
            return ang
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    ang = _site(state)
    if ang is not None:
        ang.varnas[-1] = mk("I")        # the apavāda of 7.4.25: putra + kya → putrIya (and ajA → ajI)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kyaci ca",
    text_dev              = "क्यचि च",
    samagra_slp1          = "aNgasya kyaci ca I asya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य क्यचि च ई अस्य",
    padaccheda_dev        = "क्यचि च",
    why_dev               = "(सूत्रम् 7.4.33) क्यचि च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
