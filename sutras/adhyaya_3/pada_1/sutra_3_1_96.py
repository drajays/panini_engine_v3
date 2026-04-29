"""
3.1.96  तव्यत्तव्यानीयरः  —  VIDHI (narrow demo)

Demo slice: attach kṛtya ``anIyar`` (अनीयर्) after **6.4.1**-scoped dhātukārya
recipe prep — recipe must arm via ``state.meta['3_1_96_anIyar_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if not state.meta.get("3_1_96_anIyar_arm"):
        return False
    if not state.terms:
        return False
    if state.meta.get("3_1_96_anIyar_done"):
        return False
    # Already attached?
    if any((t.meta.get("upadesha_slp1") or "").strip() == "anIyar" for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("anIyar")),
        tags={"pratyaya", "upadesha", "krt", "ardhadhatuka"},
        meta={
            "upadesha_slp1": "anIyar",
            "krit_pratyaya": "anIyar",
            "anit_ardhadhatuka": True,
        },
    )
    state.terms.append(pr)
    state.meta["3_1_96_anIyar_done"] = True
    state.meta["3_1_96_anIyar_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.96",
    sutra_type=SutraType.VIDHI,
    text_slp1="tavyat-tavyA-nIyar",
    text_dev="तव्यत्तव्यानीयरः",
    padaccheda_dev="तव्यत्-तव्य-अनीयर्",
    why_dev="कृत्य-प्रत्यय अनीयर् (अर्थः विधिलिङ् / भाव्यम् / कार्यम् इत्यादि)।",
    anuvritti_from=("3.1.91",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
