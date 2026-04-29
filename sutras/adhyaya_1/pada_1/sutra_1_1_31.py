"""
1.1.31  द्वन्द्वे च  —  NIYAMA

*Śruti* (with anuvṛtti from **1.1.27**): the *sarvādi* → *sarvanāma*-*saṃjñā*
is **not** conferred (or is revoked) in a *dvandva* samāsa (*dvandve ca*).

Engine (glass-box):
  - **1.1.27** may tag an aṅga as ``sarvanama`` from the sarvādi-gaṇa.
  - **1.1.31** removes that tag when the same aṅga carries the structural tag
    ``dvandva_samasa`` (samāsa memory).

This blocks downstream *sarvanāma*-only paths such as **7.1.52** *suṭ* on ``Am``.

Mechanical blindness (CONSTITUTION Art. 2):
  - ``cond`` reads only structural ``tags`` / allowed ``meta`` (no vibhakti/vacana,
    no gold, no surface-Devanāgarī).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

TAG_DVANDVA_SAMASA: str = "dvandva_samasa"

META_1_1_31_DVANDVA_STRIPPED: str = "1_1_31_dvandve_ca_sarvanama_stripped"
"""Set on aṅga when **1.1.31** removes *sarvanāma* in *dvandva* samāsa."""


def _eligible_angas(state: State):
    for t in state.terms:
        if "anga" not in t.tags or "prātipadika" not in t.tags:
            continue
        if TAG_DVANDVA_SAMASA not in t.tags:
            continue
        if "sarvanama" not in t.tags:
            continue
        if t.meta.get(META_1_1_31_DVANDVA_STRIPPED):
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible_angas(state), None) is not None


def act(state: State) -> State:
    for t in _eligible_angas(state):
        t.tags.discard("sarvanama")
        t.meta[META_1_1_31_DVANDVA_STRIPPED] = True
    state.samjna_registry["1_1_31_dvandve_ca"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.31",
    sutra_type     = SutraType.NIYAMA,
    r1_form_identity_exempt=True,
    text_slp1      = "dvandve ca",
    text_dev       = "द्वन्द्वे च",
    padaccheda_dev = "द्वन्द्वे च (न सर्वनाम) — १.१.२७ अनुवृत्ति",
    why_dev        = "द्वन्द्व-समासे सर्वनाम-संज्ञा न (१.१.२७-प्रसङ्गे निषेधः)।",
    anuvritti_from = ("1.1.27",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["TAG_DVANDVA_SAMASA", "META_1_1_31_DVANDVA_STRIPPED", "SUTRA"]

