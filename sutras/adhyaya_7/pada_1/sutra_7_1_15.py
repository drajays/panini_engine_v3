"""
7.1.15  ङसिङ्योः स्मात्स्मिनौ  —  VIDHI

For adant sarvanāma aṅgas (e.g. sarva):
  - Neuter/other rules aside, for puṃliṅga sarvanāma we need:
      ṅasi (Nasi) → smAt
      ṅi   (Ni)   → smin

We implement as a direct pratyaya replacement based on upadeśa identity.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


_TABLE = {
    "Nasi": ("s", "m", "A", "t"),   # स्मात्
    "Ni":   ("s", "m", "i", "n"),   # स्मिन्
}


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "sarvanama" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    up = pr.meta.get("upadesha_slp1")
    if up not in _TABLE:
        return False
    if pr.meta.get("smat_smin_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    up = pr.meta.get("upadesha_slp1")
    assert isinstance(up, str)
    pr.varnas = [mk(x) for x in _TABLE[up]]
    pr.meta["smat_smin_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", up)
    pr.meta["upadesha_slp1"] = "smAt" if up == "Nasi" else "smin"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.15",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "NasiNyoH smAt-sminau",
    text_dev       = "ङसिङ्योः स्मात्स्मिनौ",
    padaccheda_dev = "ङसि-ङ्योः स्मात्-स्मिनौ",
    why_dev        = "अदन्त-सर्वनाम-अङ्गात् परयोः ङसि/ङि-प्रत्यययोः क्रमशः ‘स्मात्’/‘स्मिन्’ आदेशौ।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

