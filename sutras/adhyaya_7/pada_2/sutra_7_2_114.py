"""
7.2.114  मृजेर्वृद्धिः  —  VIDHI (narrow: mFj → mArj before tiṅ)

Glass-box scope for `mArzwi`:
  For dhātu `mFj` (after it-lopa from `mFjU~z`), when a tiṅ pratyaya follows,
  apply vṛddhi on vocalic ṛ (f) as: f → A and arm 1.1.51 (uRaN-rapara) to
  insert r after that A (yielding Ar).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

from sutras.adhyaya_1.pada_1.sutra_1_1_4 import ik_guna_vriddhi_blocked_by_1_1_4


def _find(state: State):
    if ik_guna_vriddhi_blocked_by_1_1_4(state):
        return None
    if len(state.terms) < 2:
        return None
    dh = state.terms[0]
    pr = state.terms[-1]
    if "dhatu" not in dh.tags:
        return None
    if pr.kind != "pratyaya":
        return None
    # Accept any parasmaipada-tiṅ residue here; glass-box pipelines commonly have `ti` after it-lopa.
    if "tin_adesha_3_4_78" not in pr.tags and (pr.meta.get("upadesha_slp1") or "").strip() not in {"tip", "ti"}:
        return None
    if dh.meta.get("7_2_114_mrje_vrddhi_done"):
        return None
    # Accept this dhātu by phonemic shape (after it-lopa cleanup).
    if "".join(v.slp1 for v in dh.varnas)[:3] != "mFj":
        return None
    for j, v in enumerate(dh.varnas):
        if v.slp1 in {"f", "F"}:
            return (0, j)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, j = hit
    dh = state.terms[ti]
    dh.varnas[j] = mk("A")
    dh.meta["urN_rapara_pending"] = "r"
    dh.meta["urN_rapara_after_index"] = j
    dh.meta["7_2_114_mrje_vrddhi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.114",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "mfjeH vRddhiH",
    text_dev       = "मृजेर्वृद्धिः",
    padaccheda_dev = "मृजेः / वृद्धिः",
    why_dev        = "मृज्-धातोः सार्वधातुके परे ऋ-स्थाने वृद्धि (आर्) — ग्लास-बॉक्स्।",
    anuvritti_from = ("1.1.1", "1.1.3", "1.1.50", "1.1.51"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

