"""
1.1.17  उञः  (uYaH)  —  PARIBHASHA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11017, ``e`` = *unyah*):** *uÞ* *aḥ* (*uÞ* *aḥ* );
SLP1 ``Y`` = ञ् in this engine.  Continues **1.1.11** and **1.1.16** (*saṃjñā*); v3: R3 *paribhāṣā* *gate* for *aś* *it*
( **1.3.2** –**1.3.9** ) in *uÞ* *prakaraṇa*.

CONSTITUTION Art. 2: *cond* is idempotent; no *vibhakti* in *cond*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

GATE_KEY: str = "1.1.17_uYaH"


def uYaH_gate_is_set(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "active": True,
        "pATha": "1.1.17",
    }
    return state


_WHY = (
    "उञ-कृत-प्रगृह्य-नियमः, ष्-छ-प्रकृतौ, इति।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.17",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "uYaH",
    text_dev       = "उञः",
    padaccheda_dev = "उञः",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.11", "1.1.16"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
