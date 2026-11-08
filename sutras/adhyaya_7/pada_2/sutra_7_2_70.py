"""
7.2.70  ऋद्धनोः स्ये  —  VIDHI

Padaccheda: ऋत्-हनोः स्ये

ऋद्धनोः स्ये (7.2.70)
Pāṭha: ashtadhyayi.com data.txt row i=72070 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_AFFIX = frozenset({"sya", "syat"})


def _site(state: State):
    """ऋद्धनोः स्ये — an ṛ-final dhātu and han take the iṭ before sya (जरिष्यति, हनिष्यति)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip().replace("^", "").replace("\\", "")
        if not (up.replace("~", "").endswith(("f", "F")) or up.replace("~", "") == "han"):
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is not None and (nxt.meta.get("upadesha_slp1") or "").strip() in _AFFIX and "it_7_2_70" not in nxt.tags:
            return nxt
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    nxt = _site(state)
    if nxt is not None:
        nxt.tags.add("it_7_2_70")
        state.blocked_sutras.discard("7.2.35")      # the iṭ is given even to an aniṭ dhātu (7.2.10 is set aside)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fdDanoH sye",
    text_dev              = "ऋद्धनोः स्ये",
    samagra_slp1          = "aNgasya fdDanoH sye ArDaDAtukasya iw valAdeH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ऋद्धनोः स्ये आर्धधातुकस्य इट् वलादेः",
    padaccheda_dev        = "ऋत्-हनोः स्ये",
    why_dev               = "(सूत्रम् 7.2.70) ऋद्धनोः स्ये।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
