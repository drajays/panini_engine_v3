"""
7.3.89  उतो वृद्धिर्लुकि हलि  —  VIDHI

Padaccheda: उतः वृद्धिः लुकि हलि

उतो वृद्धिर्लुकि हलि (7.3.89)
Pāṭha: ashtadhyayi.com data.txt row i=73089 (Art. 14).
"""
from __future__ import annotations
from phonology import mk

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_89_uto_89"


_AC = frozenset("aAiIuUfFxXeEoO")


def _find(state: State) -> int | None:
    """उतो वृद्धिर्लुकि हलि (नाभ्यस्तस्य): after śap-luk, a root ending in short u
    takes vṛddhi before a hal-initial pit ending — क्षौति, यौति, स्तौति."""
    if not state.meta.get("2_4_72_sap_luk"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("7_3_89_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "u":
            return None
        if (t.meta.get("upadesha_slp1") or "").strip() == "UrRuY":
            return None          # ऊर्णोतेर्विभाषा (7.3.90): vṛddhi or guṇa (7.3.91 गुणोऽपृक्ते); the guṇa branch is the one output (और्णोत्)
        tin = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if tin is None or tin.varnas[0].slp1 in _AC or "kngiti" in tin.tags or tin.meta.get("is_apit"):
            return None
        up = (tin.meta.get("upadesha_slp1") or "").strip()
        return i if up.endswith(("p", "P")) else None
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[-1] = mk("O")
    t.meta["7_3_89_done"] = True
    t.meta["anga_guna_7_3_84"] = True        # the ik has had its vṛddhi; no guṇa after
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.3.89",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "uto vfdDirluki hali",
    text_dev              = "उतो वृद्धिर्लुकि हलि",
    samagra_slp1          = "aNgasya utaH vfdDiH luki hali piti sArvaDAtuke",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य उतः वृद्धिः लुकि हलि पिति सार्वधातुके",
    padaccheda_dev        = "उतः वृद्धिः लुकि हलि",
    why_dev               = "(सूत्रम् 7.3.89) उतो वृद्धिर्लुकि हलि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
