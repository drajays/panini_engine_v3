"""
1.1.36  अन्तरं बहिर्योगोपसंव्यानयोः  —  SAMJNA

Anuvṛtti: sarvanāma from 1.1.27.

Meaning: The word "antara" gets the sarvanāma-saṃjñā when it is used in
the sense of "bahiryoga" (external connection / outside relationship) or
"upasaṃvyāna" (covering garment / under-garment).

Engine (glass-box):
  - A Term with "anga" + "prātipadika", upadesha_slp1 == "antara",
    not yet "sarvanama", AND carrying tag "bahiryoga" OR "upasaMvyAna"
    (set by the pipeline to signal the semantic context) gets "sarvanama".
  - Metadata-only change; no surface phoneme altered.

Mechanical blindness (CONSTITUTION Art. 2):
  - cond() reads only Term.meta['upadesha_slp1'] and Term.tags.
  - No vibhakti/vacana/lakāra/gold access.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _eligible(state: State):
    for t in state.terms:
        if "anga" not in t.tags:
            continue
        if "prātipadika" not in t.tags:
            continue
        if "sarvanama" in t.tags:
            continue
        upa = t.meta.get("upadesha_slp1")
        if upa != "antara":
            continue
        # Conditional grant: only in bahiryoga or upasaṃvyāna sense.
        if "bahiryoga" not in t.tags and "upasaMvyAna" not in t.tags:
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    for t in _eligible(state):
        t.tags.add("sarvanama")
    state.samjna_registry["1_1_36_antara_sarvanama"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.1.36",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = "antaram bahiryogopasaMvyAnayoH",
    text_dev              = "अन्तरं बहिर्योगोपसंव्यानयोः",
    padaccheda_dev        = "अन्तरम् / बहिर्-योग-उपसंव्यानयोः",
    why_dev               = (
        "बहिर्योगे उपसंव्याने च «अन्तर»-शब्दस्य सर्वनाम-संज्ञा।"
    ),
    anuvritti_from        = ("1.1.27",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
