"""
1.4.15  नः क्ये  (naḥ kye)  —  NIYAMA

**Pāṭha:** [Something involving] *n* (*naḥ*) [operates] before the suffix
*kya* (*kye*).

v3: sets the interpretive gate ``1_4_15_naH_kye`` in
``state.paribhasha_gates`` to mark that the n-before-kya context is
operative.  The actual phonemic operation is handled by downstream VIDHI
rules that consult this gate.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    return state.paribhasha_gates.get("1_4_15_naH_kye") is not True


def act(state: State) -> State:
    state.paribhasha_gates["1_4_15_naH_kye"] = True
    state.samjna_registry["naH_kye_gate"] = frozenset({"n_before_kya"})
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.15",
    sutra_type             = SutraType.NIYAMA,
    text_slp1              = "naH kye",
    text_dev               = "नः क्ये",
    padaccheda_dev         = "नः / क्ये",
    why_dev                = "क्य-प्रत्यये परे नस्य विशेष-कार्यं प्रवर्तते।",
    anuvritti_from         = ("1.4.1",),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
