"""
6.1.65  णो नः  —  VIDHI

Initial ``R`` (ण्) of a dhātu stem (after it-lopa of following anubandhas)
is replaced by ``n`` (न्) in the stated contexts (ṇaḥ → na).

Narrow engine use (``RIY`` / णीञ् → ``nI``): fires once on the dhātu Term
when its first Varṇa is ``R``, **before** kṛt-pratyaya attachment (see
``pipelines/krdanta.derive_nAyaka_pratipadika`` ordering).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def cond(state: State) -> bool:
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    if not t0.varnas:
        return False
    if t0.varnas[0].slp1 != "R":
        return False
    if t0.meta.get("no_naH_6_1_65_done"):
        return False
    return True


def act(state: State) -> State:
    t0 = state.terms[0]
    t0.varnas[0] = mk("n")
    t0.meta["no_naH_6_1_65_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.65",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Ro naH",
    text_dev       = "णो नः",
    padaccheda_dev = "णः नः",
    why_dev        = "धात्वादौ णकारस्य नकारः (णीञ् → नी)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
