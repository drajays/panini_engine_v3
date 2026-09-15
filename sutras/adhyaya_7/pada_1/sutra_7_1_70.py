"""
7.1.70  उगिदचां सर्वनामस्थानेऽधातोः  —  VIDHI

Glass-box slice: *nuṃ* (*n*) after the last *ac* of a non-dhātu *aṅga* tagged
``ugit`` when a *sarvanāmasthāna* *sup* follows (**1.1.43**), and the recipe
arms ``state.meta["7_1_70_arm"]``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 71070 · उगिदचां सर्वनामस्थानेऽधातोः
              padaccheda: उक्-इत्-अचाम् सर्वनामस्थाने अ-धातोः
              anuvṛtti:   64001: अङ्गस्य | 71058: नुम्
  Source #2 — Kāśikā 7.1.70 udāharaṇa:
                भवतु — भवान्
                ईयसुन् — श्रेयान् श्रेयांसौ
                शतृ — पचन्
  Cross-check — surface pinned by: tests/unit/test_gomAn_pipeline.py
  Reference record: sutra_ref_out/7_1_70.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.varna import AC_DEV


def _eligible(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags or "ugit" not in anga.tags:
        return False
    if "dhatu" in anga.tags:
        return False
    if "sup" not in pr.tags or "sarvanamasthana" not in pr.tags:
        return False
    if anga.meta.get("7_1_70_num_done"):
        return False
    if not anga.varnas:
        return False
    return True


def _last_ac_j(varnas) -> int | None:
    j_best = None
    for j, v in enumerate(varnas):
        if v.slp1 in AC_DEV:
            j_best = j
    return j_best


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    anga = state.terms[-2]
    j = _last_ac_j(anga.varnas)
    if j is None:
        return state
    n_v = mk("n")
    n_v.tags.add("mit")
    anga.varnas.insert(j + 1, n_v)
    anga.meta["7_1_70_num_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.70",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ugidacAM sarvanAmasthAne adhAtoH",
    text_dev       = "उगिदचां सर्वनामस्थानेऽधातोः",
    padaccheda_dev = "उगिद्-अचाम् / सर्वनामस्थाने / अधातोः",
    why_dev        = "उगित्-अङ्गस्य सर्वनामस्थाने परे नुम्-आगमः (चितवन्त्)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
