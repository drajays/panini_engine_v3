"""
7.1.58  इदितो नुम् धातोः  —  VIDHI

*Idit* dhātus (roots bearing the indicatory vowel *i* in upadeśa, marked ``"idit"``
in tags after *it*-lopa) receive the nasal augment *num* (``n``) inserted after the
last vowel of the dhātu (placement per **1.1.47**).

Engine: fires on any dhātu ``Term`` whose ``tags`` include ``"idit"`` and which
has not yet been augmented.  No arm flag — the grammatical property alone drives
the rule.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import is_dirgha, is_hrasva


def _is_ac(ch: str) -> bool:
    return bool(is_hrasva(ch) or is_dirgha(ch) or ch in {"e", "E", "o", "O"})


def _find_idit_dhatu(state: State):
    """Return the first dhātu Term tagged ``idit`` that has not yet received nuṃ."""
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if "idit" not in t.tags:
            continue
        if t.meta.get("7_1_58_num_done"):
            continue
        return t
    return None


def cond(state: State) -> bool:
    return _find_idit_dhatu(state) is not None


def act(state: State) -> State:
    dh = _find_idit_dhatu(state)
    if dh is None:
        return state
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

