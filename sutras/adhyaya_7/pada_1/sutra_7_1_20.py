"""
7.1.20  जश्शसोः शिः  —  VIDHI

Operational role (v3.6, napuṃsaka a-stems):
  For a **napuṃsaka** aṅga, the sup upadeśas **jas** (1-3 / 8-3) and
  **Sas** (2-3) are replaced by **Si** (शि).

We represent 'Si' as varṇas [S, i]. The initial S is cuṭu-it (1.3.7)
and will be removed by 1.3.9 when the recipe re-fires the it-prakaraṇa.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


_TARGETS = frozenset({"jas", "Sas"})


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "napuṃsaka" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") not in _TARGETS:
        return False
    if pr.meta.get("jas_sas_to_si_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    pr.varnas = [mk("S"), mk("i")]
    pr.meta["jas_sas_to_si_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", pr.meta.get("upadesha_slp1"))
    pr.meta["upadesha_slp1"] = "Si"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.20",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "jasSasoH SiH (napuMsake)",
    text_dev       = "जश्शसोः शिः",
    padaccheda_dev = "जस्-शसोः शिः",
    why_dev        = "नपुंसक-अङ्गात् परयोः जस्/शस्-प्रत्यययोः ‘शि’-आदेशः (ज्ञानानि)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

