"""
6.4.105  अतो हेः  —  VIDHI

Two operational paths:
  1. ``P038_6_4_105_uw_trim_arm``: vidhi-liṅ P038 — trims uṭ residue from sīyuṭ.
  2. ``6_4_105_loT_hi_lopa_arm``: loṭ — deletes the 'hi' tiṅ ādeśa (2sg) when
     it follows an aṅga term whose final varṇa is short 'a'.
     Rule: "atō heḥ" = after short 'a', 'hi' (= heḥ) is deleted (luk).
     Effect: bhav + a(śap) + hi → bhav + a(śap)  →  bhava (2sg loṭ).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 64105 · अतो हेः
              padaccheda: अतः हेः
              anuvṛtti:   64001: अङ्गस्य | 64104: लुक्
  Source #2 — Kāśikā 6.4.105 udāharaṇa:
                पच
                पठ
                गच्छ
  Cross-check — surface pinned by: tests/unit/test_paceran_vidhi_liG_pac_Ja.py, tests/unit/test_tinanta_bhavatu_lot.py
  Reference record: sutra_ref_out/6_4_105.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find_sIyuw(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "ling_sIyuw" not in t.tags:
            continue
        if t.meta.get("P038_6_4_105_done"):
            continue
        vs = t.varnas
        if len(vs) < 4:
            continue
        if vs[-2].slp1 == "u" and vs[-1].slp1 == "w":
            return i
    return None


def _find_loT_hi(state: State) -> int | None:
    """Find 'hi' tiṅ term preceded by a term ending in short 'a'."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "hi":
            continue
        if t.meta.get("6_4_105_hi_done"):
            continue
        if i == 0:
            continue
        prev = state.terms[i - 1]
        if not prev.varnas or prev.varnas[-1].slp1 != "a":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_sIyuw(state) is not None or _find_loT_hi(state) is not None


def act(state: State) -> State:
    idx = _find_sIyuw(state)
    if idx is not None:
        t = state.terms[idx]
        t.varnas = t.varnas[:-2]
        t.meta["P038_6_4_105_done"] = True
        return state
    j = _find_loT_hi(state)
    if j is not None:
        state.terms[j].meta["6_4_105_hi_done"] = True
        state.terms.pop(j)
        state.samjna_registry["6.4.105_hi_lopa"] = True
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.105",
    sutra_type=SutraType.VIDHI,
    text_slp1="ato heH",
    text_dev="अतो हेः",
    padaccheda_dev="अतः / हेः",
    why_dev=(
        "लोटि ह्र्स्व-अकारान्त-अङ्गात् परस्य 'हि'-तिङ्-आदेशस्य लोपः "
        "(भव + हि → भव); P038-पथे सीयुट्-अवशेषात् उट्-लोपः।"
    ),
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
