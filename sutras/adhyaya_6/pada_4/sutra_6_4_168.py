"""
6.4.168  ये चाभावकर्मणोः  —  SAMJNA (narrow)

**Pāṭha:** *ye cābhāvakarmaṇoḥ* — *prakṛtibhāva* block for **yat** after **-an**
bases in non-bhāva/karman senses, barring **6.4.144** *ṭi-lopa*.

Narrow v3 (``prakriya_18``):
  • When ``state.meta['prakriya_18_sAmanyas']`` and the last ``Term`` is ``yat``
    *taddhita* after ``sAman`` + ``Ni`` frame, register
    ``samjna_registry['6_4_168_yat_prakritibhava_sAman']`` (audit gate for **6.4.144**).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _eligible(state: State) -> bool:
    if not state.meta.get("prakriya_18_sAmanyas"):
        return False
    if len(state.terms) < 3:
        return False
    if (state.terms[-1].meta.get("upadesha_slp1") or "").strip() != "yat":
        return False
    if "6_4_168_yat_prakritibhava_sAman" in state.samjna_registry:
        return False
    return True


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    state.samjna_registry["6_4_168_yat_prakritibhava_sAman"] = frozenset({"yat"})
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.168",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "ye cAbhAvakarmaRoH",
    text_dev       = "ये चाभावकर्मणोः",
    padaccheda_dev = "ये च अभाव-कर्मणोः",
    why_dev        = "यत्-प्रत्यये प्रकृतिभावः — ६.४.१४४-टिलोप-प्रतिषेधाङ्कनम्।",
    anuvritti_from = ("6.4.144",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
