"""
7.1.58  इदितो नुम् धातोः  —  VIDHI (narrow demo)

Demo slice (वन्दे .md):
  For dhātu `vad` (from upadeśa `vadi~`), insert nuṃ (n) after the last vowel
  (1.1.47 placement), yielding `vand`.

Engine:
  - recipe-armed by ``state.meta['7_1_58_num_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import is_dirgha, is_hrasva


def _is_ac(ch: str) -> bool:
    return bool(is_hrasva(ch) or is_dirgha(ch) or ch in {"e", "E", "o", "O"})


def _matches(state: State) -> bool:
    if not state.meta.get("7_1_58_num_arm"):
        return False
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    if (dh.meta.get("upadesha_slp1") or "").strip() != "vad":
        return False
    if dh.meta.get("7_1_58_num_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    dh = state.terms[0]
    j = None
    for k in range(len(dh.varnas) - 1, -1, -1):
        if _is_ac(dh.varnas[k].slp1):
            j = k
            break
    if j is None:
        return state
    dh.varnas.insert(j + 1, mk("n"))
    dh.meta["7_1_58_num_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.58",
    sutra_type=SutraType.VIDHI,
    text_slp1="idito num DAtoH",
    text_dev="इदितो नुम् धातोः",
    padaccheda_dev="इदितः / नुम् / धातोः",
    why_dev="इदित्-धातोः नुम्-आगमः (डेमो: वन्दे)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

