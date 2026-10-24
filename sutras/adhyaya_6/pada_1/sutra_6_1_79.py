"""
6.1.79  वान्तो यि प्रत्यये  —  VIDHI

Padaccheda: वान्तः यि प्रत्यये

वान्तो यि प्रत्यये (6.1.79)
Pāṭha: ashtadhyayi.com data.txt row i=61079 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_VANTA = {"o": ("a", "v"), "O": ("A", "v")}


def _site(state: State):
    """वान्तो यि प्रत्यये — o / au at the end of what stands before a pratyaya that begins with y: Bavya (Bo + ya), gavya, nAvya."""
    live = [t for t in state.terms if t.varnas]
    for left, nxt in zip(live, live[1:]):
        if left.varnas[-1].slp1 in _VANTA and "pratyaya" in nxt.tags and nxt.varnas[0].slp1 == "y" and not left.meta.get("eco_ayavayava_done"):
            return left
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    left = _site(state)
    a, v = _VANTA[left.varnas[-1].slp1]
    left.varnas[-1] = mk(a)
    left.varnas.append(mk(v))
    left.meta["eco_ayavayava_done"] = True
    left.tags.discard("upadesha")          # as 6.1.78: the new final v is no halantyam it
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.79",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAnto yi pratyaye",
    text_dev              = "वान्तो यि प्रत्यये",
    samagra_slp1          = "ecaH yi-pratyaye vAntaH saMhiyAtAm",
    samagra_dev           = "एचः यि-प्रत्यये वान्तः संहियाताम्",
    padaccheda_dev        = "वान्तः यि प्रत्यये",
    why_dev               = "(सूत्रम् 6.1.79) वान्तो यि प्रत्यये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
