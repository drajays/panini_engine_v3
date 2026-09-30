"""
7.1.25  अद्ड् डतरादिभ्यः पञ्चभ्यः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=71025
- Kāśikā: "अन्यत्, अन्यतरत्, इतरत्, यत्, तत्।"
- Cross-validation: tests/unit/test_gita_15_3_4_yantra.py (तत्)

Napuṃsaka *tyadādi* / *ḍatarādi* take **अद्** (not 7.1.24 अम्) for *su*/*am*.
तद् + सुँ → अद् → तत् (8.4.56 चर्त्व).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "7_1_25_adq_25"
_STEMS = frozenset({
    "tad", "tyad", "etad", "idam", "yad", "adas",
    "anya", "anyatara", "itara", "ekatara", "katara", "katama",
})


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr = state.terms[-1]
    if "anga" not in anga.tags or "napuṃsaka" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("adq_done") or state.paribhasha_gates.get(_GATE_KEY):
        return False
    up = (anga.meta.get("upadesha_slp1") or "").strip()
    if up not in _STEMS:
        return False
    pu = (pr.meta.get("upadesha_slp1") or "").strip()
    if pu not in {"s~", "am", "su"}:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    pr = state.terms[-1]
    pr.varnas = list(parse_slp1_upadesha_sequence("at"))
    # अतो गुणे: अङ्ग-अ + अद्-अ → पररूप, leftover त्. Undo 7.3.102 dīrgha (तत्).
    if anga.varnas and anga.varnas[-1].slp1 in {"a", "A"}:
        anga.varnas[-1] = mk("a")
        pr.varnas = [mk("t")]
    pr.meta["upadesha_slp1"] = "ad"
    pr.meta["adq_done"] = True
    pr.tags.add("sup")
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.25",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "adq qatarAdiByaH paYcaByaH",
    text_dev              = "अद्ड् डतरादिभ्यः पञ्चभ्यः",
    padaccheda_dev        = "अद्ड् / डतर-आदिभ्यः / पञ्चभ्यः",
    why_dev               = "नपुंसक-त्यदादेः सुँ/अम्-स्थाने अद् (तत्, यत्, अन्यत्)।",
    anuvritti_from        = ("7.1.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
