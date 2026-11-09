"""
7.4.48  अपो भि  —  VIDHI

Padaccheda: अपः भि

अपो भि (7.4.48)
Pāṭha: ashtadhyayi.com data.txt row i=74048 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

# S145 (docs/SHORTCUT_LEDGER.md): the aṅga "ap" and its tadanta (su-ap = svap) are named by stem, because the samāsa machine does not yet say that a stem ends in the word ap
_APAH = ("ap", "svap")


def _find(state: State):
    """अप् before a bh-initial sup: ap + bhyām → at + bhyām (then 8.4.53: adbhyām)."""
    for i, t in enumerate(state.terms[:-1]):
        if "sup" in t.tags or not t.varnas or "".join(v.slp1 for v in t.varnas) not in _APAH:
            continue
        nxt = state.terms[i + 1]
        if "sup" in nxt.tags and nxt.varnas and nxt.varnas[0].slp1 == "B":
            return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    _find(state).varnas[-1] = mk("t")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.48",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "apo Bi",
    text_dev              = "अपो भि",
    samagra_slp1          = "aNgasya apaH Bi taH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अपः भि तः",
    padaccheda_dev        = "अपः भि",
    why_dev               = "(सूत्रम् 7.4.48) अपो भि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
