"""
**3.1.67** *sārvadhātake yak* — helpers for *yaḳ* *vikaraṇa* insertion (karmaṇi / bhāve).

*Śāstra:* after the *dhātu*, before a following *sārvadhātuka* *tiṅ* *ādeśa*, insert *yaḳ*
(**3.1.67** *anuvṛtti* **3.1.66** *sārvadhātuke*).

*Engine:* primary *dhātu* carries ``bhava_karma_usage`` (recipe, from **1.3.13** prayoga).
"""
from __future__ import annotations

from typing import Final

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import is_sarvadhatuka_upadesha_slp1
from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import TIN_ADESHA_SET

YAK_INSERT_TAG: Final[str] = "3_1_67_yak"
_GATE_KEY: Final[str] = "3_1_67_sArvaDAtuke_67"


def _norm_upadesha(up: str) -> str:
    t = up.strip()
    if t.endswith("~"):
        return t[:-1]
    return t


def _yak_trigger_next_pratyaya(up: str) -> bool:
    k = _norm_upadesha(up)
    if k in {"yak", "ya"}:
        return False
    if k in TIN_ADESHA_SET:
        return True
    return is_sarvadhatuka_upadesha_slp1(k) and k not in {"laT", "liT", "luT", "lRT", "loT", "laG", "liG", "luG", "lRG", "AsIrliG"}


def find_yak_insertion_dhatu_index(state: State) -> int | None:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return None
    if not any("bhava_karma_usage" in t.tags for t in state.terms if "dhatu" in t.tags):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if i + 1 >= len(state.terms):
            continue
        j = i + 1
        while j < len(state.terms) and "ling_sIyuw" in state.terms[j].tags:
            j += 1
        if j >= len(state.terms):
            continue
        nxt = state.terms[j]
        if nxt.kind != "pratyaya":
            continue
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if up in {"yak", "ya"} or YAK_INSERT_TAG in nxt.tags:
            continue
        if not _yak_trigger_next_pratyaya(up):
            continue
        return i
    return None
