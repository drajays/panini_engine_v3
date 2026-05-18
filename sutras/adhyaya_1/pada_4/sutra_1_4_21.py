"""
1.4.21  बहुषु बहुवचनम्  (bahuṣu bahuvacana)  —  NIYAMA

**Pāṭha:** In the case of many (*bahuṣu*), [the affix used is] the plural
(*bahuvacana*).

v3: sets the gate ``1_4_21_bahu_bahuvacana`` in ``state.paribhasha_gates``
to signal that the bahuvacana–plural correspondence paribhāṣā is operative.
This is a general niyama anchoring the three-vacana system.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    return state.paribhasha_gates.get("1_4_21_bahu_bahuvacana") is not True


def act(state: State) -> State:
    state.paribhasha_gates["1_4_21_bahu_bahuvacana"] = True
    state.samjna_registry["bahu_bahuvacana"] = frozenset({"plural_niyama"})
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.21",
    sutra_type             = SutraType.NIYAMA,
    text_slp1              = "bahu zu bahuvacanaM",
    text_dev               = "बहुषु बहुवचनम्",
    padaccheda_dev         = "बहुषु / बहुवचनम्",
    why_dev                = "बहुषु (त्रयेषु वा अधिकेषु) बहुवचनं प्रयुज्यते।",
    anuvritti_from         = ("1.4.1",),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
