"""
1.4.11  संयोगे गुरु  (saṃyoge guru)  —  SAMJNA

**Pāṭha:** [A syllable] followed by a conjunct consonant (*saṃyoga*) is
called *guru*.

v3: sets the ``1_4_11_saMYoge_guru`` gate in ``state.paribhasha_gates`` to
signal that the saṃyoge-guru rule is operative.  The actual syllable-weight
computation is done by phonology utilities consulting this gate.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    return state.paribhasha_gates.get("1_4_11_saMYoge_guru") is not True


def act(state: State) -> State:
    state.paribhasha_gates["1_4_11_saMYoge_guru"] = True
    state.samjna_registry["guru_saMYoge"] = frozenset({"conjunct_cluster_guru"})
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.11",
    sutra_type             = SutraType.SAMJNA,
    text_slp1              = "saMYoge guru",
    text_dev               = "संयोगे गुरु",
    padaccheda_dev         = "संयोगे / गुरु",
    why_dev                = "संयोग-पूर्वो ह्रस्वः स्वरो गुरु-संज्ञकः।",
    anuvritti_from         = ("1.4.1", "1.4.10"),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
