"""
1.4.19  तसौ मत्वर्थे  (tasau matvārthe)  —  SAMJNA

**Pāṭha:** The suffixes *ta* and *su* (in *matvārtha* — possessive context)
[are called …].

v3: sets the interpretive gate ``1_4_19_tasau_matvArTe`` in
``state.paribhasha_gates`` to mark that the *ta*/*su*-in-matvārtha
designation is operative for downstream matvārtha processing.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    return state.paribhasha_gates.get("1_4_19_tasau_matvArTe") is not True


def act(state: State) -> State:
    state.paribhasha_gates["1_4_19_tasau_matvArTe"] = True
    state.samjna_registry["tasau_matvArTe"] = frozenset({"ta_su_matvArtha"})
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.19",
    sutra_type             = SutraType.SAMJNA,
    text_slp1              = "tasO matvArTe",
    text_dev               = "तसौ मत्वर्थे",
    padaccheda_dev         = "तसौ / मत्वर्थे",
    why_dev                = "मत्वर्थे 'त' 'स' इति द्वयोः प्रत्यययोः संज्ञा।",
    anuvritti_from         = ("1.4.1",),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
