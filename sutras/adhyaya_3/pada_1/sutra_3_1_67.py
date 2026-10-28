"""
3.1.67  सार्वधातुके यक्  —  VIDHI

*Padaccheda:* *sārvadhātake* (**3.1.66** *anuvṛtti*) / *yak* (प्रत्यय).

*Śāstra:* karmaṇi / bhāve (*bhāvakarmaṇoः* **1.3.13**), insert *yaḳ* *vikaraṇa* between *dhātu* and
the following *sārvadhātuka* *tiṅ* *ādeśa*.

*Engine:* ``bhava_karma_usage`` on *dhātu*; no ``3_1_67_arm`` (Art. 13).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31067 · सार्वधातुके यक्
              padaccheda: सार्वधातुके यक्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31022: धातोः | 31066: भावकर्मणोः
  Source #2 — Kāśikā 3.1.67 udāharaṇa:
                आस्यते भवता
                शय्यते भवता
                कर्मणि — क्रियते कटः
  Cross-check — surface pinned by: tests/unit/test_autonomous_vs_recipe.py, tests/unit/test_tinanta_bhave_lat.py
  Reference record: sutra_ref_out/3_1_67.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


# --- helpers of this sūtra (formerly yak_vik_3_1_67.py; one sūtra, one file) ---
from typing import Final

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_3.pada_4.sutra_3_4_113 import is_sarvadhatuka_upadesha_slp1
from sutras.adhyaya_3.pada_4.sutra_3_4_78 import TIN_ADESHA_SET

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
        tags={"pratyaya", "vikarana", "upadesha", YAK_INSERT_TAG, "ardhadhatuka"},  # 3.4.114
        meta={"upadesha_slp1": "yak"},
    )
    state.terms.insert(i + 1, yak)
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["krt_kind"] = "3.1.67"
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.67",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="sArvaDAtuke yak",
    text_dev="सार्वधातुके यक्",
    samagra_slp1="BAvakarmaRoH sArvaDAtuke DAtoH yak-pratyayaH",
    samagra_dev="भावकर्मणोः सार्वधातुके धातोः यक्-प्रत्ययः",
    padaccheda_dev="सार्वधातुके यक्",
    why_dev="भाव-कर्म-प्रयोगे धातोः परे यक्-विकरण-आगमः (३.१.६७)।",
    anuvritti_from=("3.1.66", "3.1.1"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

