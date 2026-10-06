"""
7.4.10  ऋतश्च संयोगादेर्गुणः  —  VIDHI

Padaccheda: ऋतः च संयोग-आदेः गुणः

ऋतश्च संयोगादेर्गुणः (7.4.10)
Pāṭha: ashtadhyayi.com data.txt row i=74010 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _lit_dhatu(state: State):
    """The non-abhyāsa dhātu of a liṭ derivation, or None."""
    if not any("abhyasa" in t.tags for t in state.terms):
        return None
    return next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)


def _guna_ar(t, j: int) -> None:
    t.varnas[j:j + 1] = [mk("a"), mk("r")]          # गुण + उरण् रपरः (1.1.51)


def _find(state: State):
    """ऋतश्च संयोगादेर्गुणः (लिटि): a ऋ-final root beginning with a conjunct takes guṇa
    even before a kit ending — सस्मरतुः, सस्मरे, दध्वरे."""
    t = _lit_dhatu(state)
    if t is None or len(t.varnas) < 3 or t.varnas[-1].slp1 != "f":
        return None
    if t.varnas[0].slp1 in _AC or t.varnas[1].slp1 in _AC:
        return None
    return t


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = _find(state)
    _guna_ar(t, len(t.varnas) - 1)
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.4.10",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "ftaSca saMyogAderguRaH",
    text_dev              = "ऋतश्च संयोगादेर्गुणः",
    samagra_slp1          = "aNgasya ftaH ca saMyogAdeH guRaH liwi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ऋतः च संयोगादेः गुणः लिटि",
    padaccheda_dev        = "ऋतः च संयोग-आदेः गुणः",
    why_dev               = "संयोगादेः ऋदन्तस्य लिटि गुणः (सस्मरे, सस्मरतुः)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
