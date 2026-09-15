"""
3.1.43  च्लि लुङि  —  VIDHI (narrow: insert cli before luG)

Engine: when `lakara == luG` and a dhātu is present, insert a pratyaya Term
with upadeśa "cli" before the lakāra placeholder. This is a glass-box
implementation used for the aorist (luṅ) sic path.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31043 · च्लि लुङि
              padaccheda: च्लि (लुप्तप्रथमान्तनिर्देशः) लुङि
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31022: धातोः
  Source #2 — Kāśikā 3.1.43 udāharaṇa:
                इकार उच्चारणार्थः
                तत्रैवोदाहरिष्यामः
  Cross-check — surface pinned by: tests/unit/test_acaEzIt_pipeline.py, tests/unit/test_tinanta_abhut_lung.py
  Reference record: sutra_ref_out/3_1_43.json
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


def _cli_insert_index(state: State) -> int | None:
    """Before *luG* placeholder, or before *tiṅ* when *luG* was already resolved (*अघसत्*).
    Note: lakāra coordinate not read here — caller's cond() gates on cli_luG_recipe."""
    li = _lakara_index(state)
    if li is not None:
        return li
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or "tin_adesha_3_4_78" not in t.tags:
            continue
        if i > 0 and (state.terms[i - 1].meta.get("upadesha_slp1") or "").strip() == "cli":
            return None
        return i
    return None


def cond(state: State) -> bool:
    # Glass-box arming: pipelines must opt-in (CONSTITUTION: cond() may not read paradigm selectors).
    if not state.meta.get("cli_luG_recipe", False):
        return False
    if not any("dhatu" in t.tags for t in state.terms):
        return False
    return _cli_insert_index(state) is not None


def act(state: State) -> State:
    li = _cli_insert_index(state)
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

