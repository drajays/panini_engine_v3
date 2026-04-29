"""
6.4.24  अनिदितां हल उपधायाः क्ङिति  —  VIDHI (narrow demo)

Demo slice (ईधे):
  For dhātu `inD` (इन्ध्), delete the upadhā consonant `n` when a following
  pratyaya is in the kṅit locus (tagged ``kngiti`` by 1.2.6/1.2.5 etc.).

Engine:
  - narrowly searches for the first dhātu term and removes `n` if it is the
    penultimate varṇa.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _kngiti_present(state: State) -> bool:
    return any("kngiti" in t.tags for t in state.terms if "pratyaya" in t.tags)


def cond(state: State) -> bool:
    if not _kngiti_present(state):
        return False
    if not state.terms or "dhatu" not in state.terms[0].tags:
        return False
    dh = state.terms[0]
    if (dh.meta.get("upadesha_slp1") or "").strip() != "inD":
        return False
    if dh.meta.get("6_4_24_n_lopa_done"):
        return False
    if len(dh.varnas) < 2:
        return False
    return dh.varnas[-2].slp1 == "n"


def act(state: State) -> State:
    if not cond(state):
        return state
    dh = state.terms[0]
    del dh.varnas[-2]
    dh.meta["6_4_24_n_lopa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.24",
    sutra_type=SutraType.VIDHI,
    text_slp1="aniditAm hal upaDAyAH kNgiti",
    text_dev="अनिदितां हल उपधायाः क्ङिति",
    padaccheda_dev="अनिदिताम् / हल् / उपधायाः / क्‍ङिति",
    why_dev="क्ङिति परे अनिदित्-धातोः उपधा-हल्-लोपः (इन्ध्→इध्; ईधे)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

