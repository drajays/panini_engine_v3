"""
6.1.110  ङसिङसोश्च  —  VIDHI

Operational intent for v3.4 (hari-like i-stems):
  After guṇa (7.3.111), we can get an eṅ-ending aṅga followed by
  a-pratyaya initial 'a' of ṅasi / ṅas (upadeśa: Nasi / Nas).

This rule performs the pūrvarūpa-style boundary simplification so that:
  hare + asi/as  →  hare + si/s
Then Tripāḍī makes final s → ru → H, yielding हरेः.

We implement the minimal mechanical operation:
  If aṅga ends in EC (e/o/E/O) AND pratyaya begins with 'a' AND
  pratyaya upadeśa is Nasi or Nas, delete the pratyaya-initial 'a'.

Blindness:
  - pure phoneme boundary + upadeśa identity (no paradigm coords).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import EC


_TARGET_UPADESHA = frozenset({"Nasi", "Nas"})


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") not in _TARGET_UPADESHA:
        return False
    if pr.meta.get("ngasi_ngas_purvarupa_done"):
        return False
    if not anga.varnas or not pr.varnas:
        return False
    if anga.varnas[-1].slp1 not in EC:
        return False
    if pr.varnas[0].slp1 != "a":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    del pr.varnas[0]  # drop pratyaya-initial 'a'
    # v3.4: for ṅasi specifically, drop trailing 'i' so the remaining
    # final 's' can enter Tripāḍī (→ ru → visarga).
    if pr.meta.get("upadesha_slp1") == "Nasi" and pr.varnas and pr.varnas[-1].slp1 == "i":
        del pr.varnas[-1]
    pr.meta["ngasi_ngas_purvarupa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.110",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "NasiNasos ca",
    text_dev       = "ङसिङसोश्च",
    padaccheda_dev = "ङसि-ङसोः च",
    why_dev        = "एङन्त-अङ्गात् परे ङसि/ङस्-प्रत्यययोः आद्य-अकारस्य लोपः (हरेऽसि/हरेऽस् → हरेसि/हरेस् → हरेः)।",
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

