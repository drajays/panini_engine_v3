"""
1.4.2  विप्रतिषेधे परं कार्यम्  (vipratiṣedhe paraṃ kāryam)  —  PARIBHASHA

**Pāṭha:** In a conflict between two rules of equal strength (*vipratiṣedha*),
the later (*para*) rule wins.

v3: sets the ``1_4_2_vipratiSeDe`` gate in ``state.paribhasha_gates`` and
records the logical set in ``state.samjna_registry``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    return state.paribhasha_gates.get("1_4_2_vipratiSeDe") is not True


def act(state: State) -> State:
    state.paribhasha_gates["1_4_2_vipratiSeDe"] = True
    state.samjna_registry["vipratiSeDe_param_kAryam"] = frozenset({"para_wins"})
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.2",
    sutra_type             = SutraType.PARIBHASHA,
    text_slp1              = "vipratiSeDe paraM kAryam",
    text_dev               = "विप्रतिषेधे परं कार्यम्",
    padaccheda_dev         = "विप्रतिषेधे परम् कार्यम्",
    why_dev                = "विप्रतिषेधे — समबलयोः सूत्रयोः संघर्षे — परं (उत्तरं) सूत्रं कार्यं भवति।",
    anuvritti_from         = ("1.4.1",),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
