"""
3.1.67  सार्वधातुके यक्  —  VIDHI

*Padaccheda:* *sārvadhātake* (**3.1.66** *anuvṛtti*) / *yak* (प्रत्यय).

*Śāstra:* karmaṇi / bhāve (*bhāvakarmaṇoः* **1.3.13**), insert *yaḳ* *vikaraṇa* between *dhātu* and
the following *sārvadhātuka* *tiṅ* *ādeśa*.

*Engine:* ``bhava_karma_usage`` on *dhātu*; no ``3_1_67_arm`` (Art. 13).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_3.pada_1.yak_vik_3_1_67 import (
    YAK_INSERT_TAG,
    find_yak_insertion_dhatu_index,
)

_GATE_KEY = "3_1_67_sArvaDAtuke_67"


def cond(state: State) -> bool:
    return find_yak_insertion_dhatu_index(state) is not None


def act(state: State) -> State:
    i = find_yak_insertion_dhatu_index(state)
    if i is None:
        return state
    yak = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("yak")),
        tags={"pratyaya", "vikarana", "upadesha", YAK_INSERT_TAG},
        meta={"upadesha_slp1": "yak"},
    )
    state.terms.insert(i + 1, yak)
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["krt_kind"] = "3.1.67"
    state.meta.pop("3_1_67_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.67",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="sArvaDAtuke yak",
    text_dev="सार्वधातुके यक्",
    padaccheda_dev="सार्वधातुके यक्",
    why_dev="भाव-कर्म-प्रयोगे धातोः परे यक्-विकरण-आगमः (३.१.६७)।",
    anuvritti_from=("3.1.66", "3.1.1"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
