"""
7.4.70  अत आदेः  —  VIDHI

Padaccheda: अतः आदेः

अत आदेः (7.4.70)
Pāṭha: ashtadhyayi.com data.txt row i=74070 (Art. 14).
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
    """अत आदेः: the abhyāsa's initial अ becomes आ (अट् → आ+अट् → आट)."""
    hit = _abhyasa_dhatu(state)
    if hit is None or hit[0].meta.get("7_4_70_done"):
        return None
    ab, _ = hit
    return ab if ab.varnas and ab.varnas[0].slp1 == "a" else None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    ab = _find(state)
    ab.varnas[0] = mk("A")
    ab.meta["7_4_70_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.4.70",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "ata AdeH",
    text_dev              = "अत आदेः",
    samagra_slp1          = "aNgasya aByAsasya ataH AdeH liwi dIrGaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासस्य अतः आदेः लिटि दीर्घः",
    padaccheda_dev        = "अतः आदेः",
    why_dev               = "अभ्यासस्य आदेः अकारस्य दीर्घः (आट, आनर्द)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
