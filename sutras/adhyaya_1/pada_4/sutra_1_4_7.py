"""
1.4.7  शेषो घ्यसखि  —  SAMJNA

Scope for v3.4:
───────────────
We implement the operational core needed for **hari-like** prātipadikas:

- When an aṅga ends in a hrasva IK vowel (currently: i, u),
  register and tag it as **ghi**.

This is a SAMJNA rule:
  - MUST NOT mutate varṇas (executor contract).
  - MUST write to state.samjna_registry (R2).

Blindness:
  - cond() inspects only aṅga-final phoneme and Term tags.
  - does NOT read (vibhakti, vacana) or any gold/reference.
Pāṭha: ashtadhyayi.com data.txt row i=14007 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


GHI_HRASVA_IK = frozenset({"i", "u"})


def _eligible_angas(state: State):
    for t in state.terms:
        if "prātipadika" not in t.tags:   # a prātipadika saṃjñā, not aṅga
            continue
        if not t.varnas:
            continue
        if t.varnas[-1].slp1 not in GHI_HRASVA_IK:
            continue
        if "ghi" in t.tags:
            continue
        # शेषः: what 1.4.3–1.4.6 did not already name. A stem that has the nadī-saṃjñā keeps
        # it after 7.3.107 shortens its ī (नदि, not ghi: हे नदि).
        if "nadi" in t.tags:
            continue
        yield t


def cond(state: State) -> bool:
    # Fire only when there exists an aṅga that actually needs ghi.
    # This keeps existing a-stem derivation paths unchanged.
    return next(_eligible_angas(state), None) is not None


def act(state: State) -> State:
    # Register the definition (R2) and tag matching aṅgas.
    state.samjna_registry["ghi"] = GHI_HRASVA_IK
    for t in _eligible_angas(state):
        t.tags.add("ghi")
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.7",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'Sezo GyasaKi',
    text_dev       = 'शेषो घ्यसखि',
    samagra_slp1   = "SezaH hrasvaH yU Gi a-saKi",
    samagra_dev    = "शेषः ह्रस्वः यू घि अ-सखि",
    padaccheda_dev = "शेषः घि",
    why_dev        = "ह्रस्व-इक्-अन्तस्य अङ्गस्य घि-संज्ञा (हरि-प्रकारे प्रयोगाय)।",
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

