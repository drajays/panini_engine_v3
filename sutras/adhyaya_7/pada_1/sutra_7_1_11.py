"""
7.1.11  नेदमदसोरकोः  —  PRATISHEDHA

The bhis → ais of 7.1.9 (अतो भिस ऐस्) does not apply to idam / adas that are *not* aka-extended:
इदम् + भिस् stays भिस् (→ एभिः, not *ऐः*), अदस् + भिस् → अमीभिः.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 7.1.11 (padaccheda: न इदम्-अदसोः अकोः)
  Source #2 — ashtadhyayi.com śabda-prakriyā for इदम् 3-3: इद+भिस् [7.1.11] → अ+भिस् [7.2.113] → ए+भिस् [7.3.103]

Engine: reads the lexical identity of the aṅga (idam / adas, as 7.2.94 reads asmad) and the sup's identity
(Bis). The aka-extended stems (idakam) carry another identity and are untouched.
Pāṭha: ashtadhyayi.com data.txt row i=71011 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_STEMS = frozenset({"idam", "adas"})


def cond(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga, sup = state.terms[-2], state.terms[-1]
    return ("anga" in anga.tags and (anga.meta.get("upadesha_slp1") or "").strip() in _STEMS
            and "sup" in sup.tags and (sup.meta.get("upadesha_slp1") or "").strip() == "Bis")


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.11",
    sutra_type=SutraType.PRATISHEDHA,
    text_slp1="nedamadasorakoH",
    text_dev="नेदमदसोरकोः",
    samagra_slp1="akoH idam-adasoH BisaH Es na",
    samagra_dev="अकोः इदम्-अदसोः भिसः ऐस् न",
    padaccheda_dev="न इदम्-अदसोः अकोः",
    why_dev="अक-रहित इदम् / अदस् से परे भिस् को ऐस् नहीं होता (७.१.९ का निषेध): एभिः, अमीभिः।",
    anuvritti_from=("6.4.1",),
    blocks_sutra_ids=("7.1.9",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
