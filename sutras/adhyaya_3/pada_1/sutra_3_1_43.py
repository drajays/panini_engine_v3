"""
3.1.43  च्लि लुङि  —  VIDHI (narrow: insert cli before luG)

Engine: when `lakara == luG` and a dhātu is present, insert a pratyaya Term
with upadeśa "cli" before the lakāra placeholder. This is a glass-box
implementation used for the aorist (luṅ) sic path.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _lakara_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "luG":
            return i
    return None


def cond(state: State) -> bool:
    # Glass-box arming: pipelines must opt-in (CONSTITUTION: cond() may not read paradigm selectors).
    if not state.meta.get("3_1_43_cli_luG_arm", False):
        return False
    if not any("dhatu" in t.tags for t in state.terms):
        return False
    li = _lakara_index(state)
    if li is None:
        return False
    # Already inserted?
    if li > 0 and (state.terms[li - 1].meta.get("upadesha_slp1") == "cli"):
        return False
    return True


def act(state: State) -> State:
    li = _lakara_index(state)
    assert li is not None
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("cli"),
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "cli"},
    )
    state.terms.insert(li, pr)
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.43",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "cli luGi",
    text_dev       = "च्लि लुङि",
    padaccheda_dev = "च्लि / लुङि",
    why_dev        = "लुङ्-लकारे धातोः परे च्लि-आगमः (सिच्-आदेश-पूर्वः)।",
    anuvritti_from = ("3.1.91",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

