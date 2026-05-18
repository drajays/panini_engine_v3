"""
1.1.35  स्वमज्ञातिधनाख्यायाम्  —  SAMJNA  (NIYAMA)

Anuvṛtti: sarvanāma from 1.1.27.

Meaning: The word "sva" gets the sarvanāma-saṃjñā EXCEPT when it
denotes a relative/kin (ajñāti) or wealth (dhana).

Engine (glass-box):
  - When a Term has "anga" + "prātipadika" tags, upadesha_slp1 == "sva",
    does NOT yet carry "sarvanama", and does NOT carry either the
    "ajnati_samjna" or "dhana_samjna" semantic marker (set by the pipeline),
    tag it "sarvanama".
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
        if upa != "sva":
            continue
        # Niyama: blocked when the stem is used in ajñāti or dhana sense.
        if "ajnati_samjna" in t.tags or "dhana_samjna" in t.tags:
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    for t in _eligible(state):
        t.tags.add("sarvanama")
    state.samjna_registry["1_1_35_sva_sarvanama"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.1.35",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = "svam ajJAtiDanAKyAyAm",
    text_dev              = "स्वमज्ञातिधनाख्यायाम्",
    padaccheda_dev        = "स्वम् / अज्ञाति-धन-आख्यायाम्",
    why_dev               = (
        "«स्व»-शब्दस्य सर्वनाम-संज्ञा, अज्ञाति-धन-वाचके तु न।"
    ),
    anuvritti_from        = ("1.1.27",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
