"""
7.2.101  जराया जरसन्यतरस्याम्  —  VIDHI

Padaccheda: जराया जरस् अन्यतरस्याम्

जराया जरसन्यतरस्याम् (7.2.101)
Pāṭha: ashtadhyayi.com data.txt row i=72101 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_VOWELS = frozenset("aAiIuUfFxXeEoO")


def _site(state: State):
    """jarA (the word the sūtra names) before a vowel-initial vibhakti: jaras in its place (jarasau, jarase; jarayā by the other reading)."""
    if not adhikara_in_effect("7.2.101", state, "6.4.1"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        nxt = state.terms[i + 1]
        if ("anga" in t.tags and "".join(v.slp1 for v in t.varnas) == "jarA" and not t.meta.get("7_2_101_done")
                and "sup" in nxt.tags and nxt.varnas and nxt.varnas[0].slp1 in _VOWELS):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.varnas = list(parse_slp1_upadesha_sequence("jaras"))
        t.meta["7_2_101_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.101",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default        = True,
    vibhasha_scope          = lambda state: _site(state) is not None,
    text_slp1             = "jarAyA jarasanyatarasyAm",
    text_dev              = "जराया जरसन्यतरस्याम्",
    samagra_slp1          = "jarAyAH aci viBaktO jaras anyatarasyAm",
    samagra_dev           = "जरायाः अचि विभक्तौ जरस् अन्यतरस्याम्",
    padaccheda_dev        = "जराया जरस् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 7.2.101) जराया जरसन्यतरस्याम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
