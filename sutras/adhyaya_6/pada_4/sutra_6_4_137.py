"""
6.4.137  न संयोगाद्वमन्तात्  —  VIDHI

Padaccheda: न संयोगात् व-म-अन्तात्

न संयोगाद्वमन्तात् (6.4.137)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
_VOWELS = frozenset("aAiIuUfFxXeEoO")


def samyogad_vamanta(vs: list[str]) -> bool:
    """न संयोगाद्वमन्तात्: an -an aṅga whose n follows m/v preceded by a consonant
    (कर्मन्, आत्मन्, यज्वन्) keeps its a against 6.4.134 अल्लोपोऽनः."""
    return (len(vs) >= 4 and vs[-1] == "n" and vs[-2] == "a" and vs[-3] in "mv"
            and vs[-4] not in _VOWELS)


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms[:-1]):
        if "anga" in t.tags and "bha" in t.tags and not t.meta.get("6_4_137_done") \
                and samyogad_vamanta([v.slp1 for v in t.varnas]):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is not None:
        state.terms[i].meta["6_4_137_done"] = True     # trace: 6.4.134 is barred here
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na saMyogAdvamantAt",
    text_dev              = "न संयोगाद्वमन्तात्",
    padaccheda_dev        = "न संयोगात् व-म-अन्तात्",
    why_dev               = "संयोगात् परौ मकार-वकारौ यस्य अनः तस्य अकारलोपो न (कर्मणा, आत्मना)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
