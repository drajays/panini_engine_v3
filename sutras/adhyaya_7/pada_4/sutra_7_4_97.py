"""
7.4.97  ई च गणः  —  VIDHI

Padaccheda: ई (लुप्तप्रथमान्तनिर्देशः) च गणः

ई च गणः (7.4.97)
Pāṭha: ashtadhyayi.com data.txt row i=74097 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _site(state: State):
    """The abhyāsa of gaṇ before caṅ (after Ṇic): its vowel (Kāśikā: अजीगणत्, अजगणत्)."""
    if not any((t.meta.get("upadesha_slp1") or "").strip() == "caG" for t in state.terms):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" not in t.tags or t.meta.get("7_4_97_done") or len(t.varnas) != 2:      # hal + vowel: after 7.4.60 has trimmed it
            continue
        r = state.terms[i + 1]
        if "dhatu" in r.tags and "".join(v.slp1 for v in r.varnas if "aT_agama_v" not in v.tags) == "gaR" \
                and t.varnas[-1].slp1 in _AC:
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    t.varnas[-1] = mk("I")          # the other reading, caścādat, leaves the abhyāsa's a (ajagaṇat)
    t.meta["7_4_97_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.97",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "I ca gaRaH",
    text_dev              = "ई च गणः",
    samagra_slp1          = "aNgasya aByAsasya I ca gaRaH caNpare anaglope at",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासस्य ई च गणः चङ्परे अनग्लोपे अत्",
    padaccheda_dev        = "ई (लुप्तप्रथमान्तनिर्देशः) च गणः",
    why_dev               = "(सूत्रम् 7.4.97) ई च गणः।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = True,      # ī is the default reading; explore() gives the at (ajagaRat)
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
