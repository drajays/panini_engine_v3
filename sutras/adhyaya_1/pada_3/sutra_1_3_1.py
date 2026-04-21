"""
1.3.1  भूवादयो धातवः  —  SAMJNA

Upadeśa items listed in the Dhātupāṭha (starting with ``bhū``) receive the
technical name *dhātu* — prerequisite for ``धातोः``-scoped rules (3.1.91 ff.).

Engine: registers that the dhātu-upadeśa term has been recognized under this
sūtra (glass-box trace); does not alter ``varṇa``s.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags or "upadesha" not in t0.tags:
        return False
    return state.samjna_registry.get("1.3.1_bhuvadi_dhatu") is None


def act(state: State) -> State:
    state.samjna_registry["1.3.1_bhuvadi_dhatu"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.1",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "bhUvAdayo dhAtavaH",
    text_dev       = "भूवादयो धातवः",
    padaccheda_dev = "भू-आदयः धातवः",
    why_dev        = "धातुपाठोक्ताः भू-आदयः धातु-संज्ञां लभन्ते।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
