"""
8.2.36  व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः  —  VIDHI (narrow: j → z in mArj)

Glass-box scope for `mArzwi`:
  When the stem contains "...rj" (from mFj vṛddhi), replace that final 'j' with 'z' (ष्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    if not state.terms:
        return None
    t = state.terms[0]
    if t.meta.get("8_2_36_sha_done"):
        return None
    for i in range(1, len(t.varnas)):
        if t.varnas[i - 1].slp1 == "r" and t.varnas[i].slp1 == "j":
            return (0, i)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, i = hit
    state.terms[ti].varnas[i] = mk("z")
    state.terms[ti].meta["8_2_36_sha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.36",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "vrazca-Brasja-sfja-mfja-yaja-rAja-BrAja-cCa-SAM zaH",
    text_dev       = "व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः",
    padaccheda_dev = "व्रश्च-भ्रस्ज-सृज-मृज-यज-राज-भ्राज-च्छ-शाम् / षः",
    why_dev        = "एतेषु धातुषु अन्त्य-जकारस्य षकारादेशः (ग्लास-बॉक्स् narrow)।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

