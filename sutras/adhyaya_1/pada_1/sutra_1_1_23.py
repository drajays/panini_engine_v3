"""
1.1.23  (bahuganavatuḍati saṅkhyā)  —  SAMJNA; *devanāgarī* = ``_TEXT_DEV`` (ashtadhyayi *i* 11023 *s* line).

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11023):** *bahu*–*gaṇa*–*vatu*–*ḍa*+**ti** (four *śāstrīya* loci) receive the
technical name *saṅkhyā* (as per index ``type``: *संख्यासंज्ञा*).  *Padaccheda* follows ``pc``:
*बहु*–*गण*–*वतु*–*डति* · *संख्या*.

v3: ``samjna_registry['saṅkhyā']`` = *frozenset* of the four canonical **prātipadika** SLP1 stems this engine
uses: ``bahu`` , ``gaNa`` , ``vatu`` , ``qati`` (``q`` = ड् in ``phonology.varna``).  *Vidhi* may use
``pratipadika_slp1_in_sankhya_samjna``; no *Term* mutation here.
"""
from __future__ import annotations

from typing import FrozenSet

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# 1.1.23: *bahu* / *gaṇa* / *vatu* / *ḍati* — prātipadika shape in SLP1/Velthuis (as in *gaṇapāṭha* *bahv*-*ādi* *lists* / engine).
SANKHYA_1_1_23_PRATIPADIKA_SLP1: FrozenSet[str] = frozenset(
    {
        "bahu",
        "gaNa",  # गण
        "vatu",  # वतु
        "qati",  # q + a + t + i = डति (q = ड् *varna*)
    }
)

# R2: *saṅkhyā* *saṃjñā* as a prātipadika *set* (same *symbol* *key* idiom as ``vṛddhi`` / ``guṇa`` in **1.1.1** / **1.1.2**).
SANKHYA_KEY: str = "saṅkhyā"

# Exact ``s`` (i=11023) — *anusvara* in *सं* as in index.
_TEXT_DEV: str = "बहुगणवतुडति संख्या"


def cond(state: State) -> bool:
    return state.samjna_registry.get(SANKHYA_KEY) != SANKHYA_1_1_23_PRATIPADIKA_SLP1


def act(state: State) -> State:
    state.samjna_registry[SANKHYA_KEY] = SANKHYA_1_1_23_PRATIPADIKA_SLP1
    return state


def pratipadika_slp1_in_sankhya_samjna(state: State, pratipadika_slp1: str) -> bool:
    m = state.samjna_registry.get(SANKHYA_KEY)
    if not isinstance(m, frozenset):
        return False
    return pratipadika_slp1 in m


def sankhya_samjna_1_1_23_is_registered(state: State) -> bool:
    return state.samjna_registry.get(SANKHYA_KEY) == SANKHYA_1_1_23_PRATIPADIKA_SLP1


_WHY = (
    "बहु-गण-वतु-डति, संख्येयाः — ईदादि-तदन्त-तात्पर्यम्, इति।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.23",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "bahuganavatuqati saMkhyA",
    text_dev       = _TEXT_DEV,
    padaccheda_dev = "बहु-गण-वतु-डति / संख्या",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
