"""
7.4.71  तस्मान्नुड् द्विहलः  —  VIDHI

Padaccheda: तस्मात् नुट् द्वि-हलः

तस्मान्नुड् द्विहलः (7.4.71)
Pāṭha: ashtadhyayi.com data.txt row i=74071 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _abhyasa_dhatu(state: State):
    """(abhyāsa, dhātu) adjacent on the tape, or None."""
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" in t.tags and "dhatu" in state.terms[i + 1].tags:
            return t, state.terms[i + 1]
    return None


def _find(state: State):
    """तस्मान्नुड् द्विहलः: after that आ, a dhātu with two hals takes नुट् (आनर्द,
    आनञ्च; ऋ counts with its र्: आनृजे)."""
    hit = _abhyasa_dhatu(state)
    if hit is None:
        return None
    ab, dh = hit
    if not ab.meta.get("7_4_70_done") or dh.meta.get("7_4_71_done") or dh.meta.get("7_4_72_done"):
        return None
    hals = sum(1 for v in dh.varnas if v.slp1 not in _AC or v.slp1 in "fF")
    return dh if hals >= 2 else None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    dh = _find(state)
    dh.varnas.insert(0, mk("n"))
    dh.meta["7_4_71_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.4.71",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "tasmAnnuq dvihalaH",
    text_dev              = "तस्मान्नुड् द्विहलः",
    samagra_slp1          = "aNgasya aByAsasya tasmAt nuw dvihalaH liwi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासस्य तस्मात् नुट् द्विहलः लिटि",
    padaccheda_dev        = "तस्मात् नुट् द्वि-हलः",
    why_dev               = "दीर्घीभूतात् अभ्यासात् परस्य द्विहलो धातोः नुडागमः (आनर्द, आनञ्च)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
