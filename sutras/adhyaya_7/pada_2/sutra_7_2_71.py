"""
7.2.71  अञ्जेः सिचि  —  VIDHI

Padaccheda: अञ्जेः सिचि

अञ्जेः सिचि (7.2.71)
Pāṭha: ashtadhyayi.com data.txt row i=72071 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_AFFIX = frozenset({"sic"})


def _site(state: State):
    """अञ्जेः सिचि — añj takes the iṭ before sic (आञ्जीत्)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip().replace("^", "").replace("\\", "")
        if up.replace("~", "") != "anjU":
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is not None and (nxt.meta.get("upadesha_slp1") or "").strip() in _AFFIX and "it_7_2_71" not in nxt.tags:
            return nxt
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    nxt = _site(state)
    if nxt is not None:
        nxt.tags.add("it_7_2_71")
        state.blocked_sutras.discard("7.2.35")      # the iṭ is given even to an aniṭ dhātu (7.2.10 is set aside)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aYjeH sici",
    text_dev              = "अञ्जेः सिचि",
    samagra_slp1          = "aNgasya aYjeH sici ArDaDAtukasya iw valAdeH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अञ्जेः सिचि आर्धधातुकस्य इट् वलादेः",
    padaccheda_dev        = "अञ्जेः सिचि",
    why_dev               = "(सूत्रम् 7.2.71) अञ्जेः सिचि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
