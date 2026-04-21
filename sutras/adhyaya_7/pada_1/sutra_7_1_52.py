"""
7.1.52  आमि सर्वनाम्नः सुट्  —  VIDHI

For adant sarvanāma aṅgas (e.g. sarva), before the sup upadeśa **Am**
genitive plural, insert suṭ-āgama (s + ṭ-it). After it-lopa, only 's'
remains, yielding sAm.

This sets up:
  sarva + (sAm) → (7.3.103-like a→e, then 8.3.59 ṣatva) → sarveṣām

We implement:
  - prepend varṇas: s, w (ṭ)
  - update pratyaya.meta['upadesha_slp1'] to 'sAm' so downstream rules
    can key off identity without reading paradigm coords.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "sarvanama" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "Am":
        return False
    if pr.meta.get("sut_agama_done"):
        return False
    if pr.varnas and pr.varnas[0].slp1 == "s":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    # suṭ = s + ṭ(it). Since v3's 1.3.5 only tags *initial* ṭ, we tag this
    # inserted ṭ varṇa directly so 1.3.9 can remove it regardless of position.
    t_it = mk("w")
    t_it.tags.add("it_candidate_nit_tu_du")
    pr.varnas.insert(0, t_it)
    pr.varnas.insert(0, mk("s"))
    pr.meta["sut_agama_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "Am")
    pr.meta["upadesha_slp1"] = "sAm"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.52",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Ami sarvanAmnaH suw",
    text_dev       = "आमि सर्वनाम्नः सुट्",
    padaccheda_dev = "आमि सर्वनाम्नः सुट्",
    why_dev        = "अदन्त-सर्वनाम-अङ्गात् परस्य आम्-प्रत्ययस्य आदौ सुट्-आगमः (सर्वेषाम्)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

