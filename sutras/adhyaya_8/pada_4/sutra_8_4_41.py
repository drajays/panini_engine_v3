"""
8.4.41  ष्टुना ष्टुः  —  VIDHI (narrow demos)

(A) Canonical shard: ``z`` + ``t`` → ``z`` + ``w`` (ट्) in Tripāḍī.

(B) **P031** (*viśiṇḍhi*): dental ``n`` before palatal ``S`` (श्) → ``R`` (ण्),
    recipe-armed only (JSON’s confused *ṣṭu*-row folded here).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _find_p031(state: State):
    if not state.meta.get("P031_8_4_41_n_R_before_S_arm"):
        return None
    if not state.tripadi_zone:
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if t.meta.get("P031_8_4_41_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "n" and vs[i + 1].slp1 == "S":
            return i
    return None


def _find_p036_Na_to_a(state: State) -> bool:
    """
    Teaching **P036** (*nināya*): after **6.1.78**, ``nay`` + ``Na`` (``ṇ``+``a``) is
    reduced to ``nay`` + augment ``a`` so **6.1.8** sees **[nay, a]**.
    (Glass-box completion row for JSON’s *it*/augment step — folded under **8.4.41**
    demo namespace to avoid a fake *sūtra* id.)
    """
    if not state.meta.get("P036_8_4_41_Na_to_augment_a_arm"):
        return False
    if len(state.terms) != 2:
        return False
    a, b = state.terms[0], state.terms[1]
    if "".join(v.slp1 for v in a.varnas) != "nay":
        return False
    if "".join(v.slp1 for v in b.varnas) != "Na":
        return False
    return True


def _find_zt(state: State):
    if not state.tripadi_zone:
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if "8_4_41_done" in t.meta:
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "z" and vs[i + 1].slp1 == "t":
            return i + 1
    return None


def cond(state: State) -> bool:
    return (
        _find_p036_Na_to_a(state)
        or _find_p031(state) is not None
        or _find_zt(state) is not None
    )


def act(state: State) -> State:
    if _find_p036_Na_to_a(state):
        state.terms[1] = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("a")),
            tags={"pratyaya", "tin", "ardhadhatuka"},
            meta={"upadesha_slp1": "a", "P036_lit_augment_a": True},
        )
        state.meta.pop("P036_8_4_41_Na_to_augment_a_arm", None)
        return state
    p = _find_p031(state)
    if p is not None:
        t = state.terms[0]
        t.varnas[p] = mk("R")
        t.meta["P031_8_4_41_done"] = True
        state.meta.pop("P031_8_4_41_n_R_before_S_arm", None)
        return state
    i = _find_zt(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk("w")
    t.meta["8_4_41_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.41",
    sutra_type=SutraType.VIDHI,
    text_slp1="zwunA zwuH",
    text_dev="ष्टुना ष्टुः",
    padaccheda_dev="ष्टुना / ष्टुः",
    why_dev="ष्-समीपे तकारस्य टकारादेशः; प०३१ न्→ण् (श्-पूर्व); प०३६ ``Na``→``a`` (णल्-आदि)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
