"""
7.3.50  ठस्येकः  —  VIDHI (narrow: Tak → ika)

Sources consulted:
- ashtadhyayi.com data.txt row i=703050
- Kāśikā: ठञ् → इक (संवत्सरिक-प्रयोगः)
- Cross-validation: pipelines/dADikam_taddhita_split_prakriyas.py

**1.1.56** extends *taddhita-pratyayatva* to *ika* for **7.2.117** *ādi-vṛddhi*.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import TADDHITA_PRATYAYATVA, adesha_substitute_varnas


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or "taddhita" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "Tak":
            continue
        if t.meta.get("7_3_50_Tak_to_ika_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    pr = state.terms[i]
    adesha_substitute_varnas(
        pr,
        "ika",
        state,
        sutra_id="7.3.50",
        gunadharmas=frozenset({TADDHITA_PRATYAYATVA}),
    )
    pr.meta["7_3_50_Tak_to_ika_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.50",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Thasya ekaH (Tak→ika) (narrow)",
    text_dev       = "ठस्येकः (ठक्→इक) — संक्षेपः",
    padaccheda_dev = "ठस्य / एकः",
    why_dev        = "ठक्-प्रत्ययस्य ‘इक’ आदेशः (P018 narrow demo).",
    anuvritti_from = ("7.3.45",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

