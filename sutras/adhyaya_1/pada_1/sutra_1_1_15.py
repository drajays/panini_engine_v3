"""
1.1.15  ओत्  (ot)  —  SAMJNA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11015):** *O* in *nipāta* (the *o* + *t* cluster) is called
*pragṅhya* with *anuvṛtti* of *nipāta* (**1.1.14**) and *pragṅhyam* (**1.1.11**).

v3: **R2** — ``samjna_registry['pragrahya_ot'] = True``; *vidhi* / *śabda* *śāstra* *prayoga* consults
this together with **1.1.11** / **1.1.14**.  (*cond* has no *vibhakti* read; Art. 2.)
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

OT_KEY: str = "pragrahya_ot"


def ot_praghy_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get(OT_KEY) is True


def cond(state: State) -> bool:
    return not ot_praghy_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry[OT_KEY] = True
    return state


# Back-compat alias (older name in tests / external refs).
ot_gate_is_set = ot_praghy_samjna_is_registered


_WHY = (
    "ओ-कार-निपात-काले, प्रगृह्य-संज्ञा (१.१.११+१.१.१४)।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.15",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "ot",
    text_dev       = "ओत्",
    padaccheda_dev = "ओत्",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.11", "1.1.14"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
