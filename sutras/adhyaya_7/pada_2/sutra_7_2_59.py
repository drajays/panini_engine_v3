"""
7.2.59  न वृद्भ्यश्चतुर्भ्यः  —  VIDHI

Padaccheda: न वृद्‍भ्यः चतुर्भ्यः

न वृद्भ्यश्चतुर्भ्यः (7.2.59)
Pāṭha: ashtadhyayi.com data.txt row i=72059 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_ROOTS = frozenset({"vftu~", "vfDu~", "SfDu~", "syandU~"})      # vṛt, vṛdh, śṛdh, syand
_BLOCKS = ("7.2.35",)                                            # the iṭ of a val-initial ārdhadhātuka


def _site(state: State):
    """One of the four roots, in parasmaipada, before an s-initial ārdhadhātuka (sya: se)."""
    if not adhikara_in_effect("7.2.59", state, "6.4.1"):
        return None
    if not any("parasmaipada" in t.tags for t in state.terms):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or (t.meta.get("upadesha_slp1") or "").strip() not in _ROOTS:
            continue
        pr = next((u for u in state.terms[i + 1:] if "ardhadhatuka" in u.tags and u.varnas), None)
        if pr is not None and pr.varnas[0].slp1 == "s":
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None and not set(_BLOCKS) <= state.blocked_sutras


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.59",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na vfdByaScaturByaH",
    text_dev              = "न वृद्भ्यश्चतुर्भ्यः",
    samagra_slp1          = "aNgasya na vfdByaH caturByaH valAdeH iw ArDaDAtukasya se parasmEpadezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य न वृद्भ्यः चतुर्भ्यः वलादेः इट् आर्धधातुकस्य से परस्मैपदेषु",
    padaccheda_dev        = "न वृद्‍भ्यः चतुर्भ्यः",
    why_dev               = "न वृद्भ्यश्चतुर्भ्यः — वृतुवृधुशृधुस्यन्दूभ्यः सकारादेः आर्धधातुकस्य इण् न (वर्त्स्यति)।",
    anuvritti_from        = ('7.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
