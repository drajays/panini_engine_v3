"""
7.2.7  अतो हलादेर्लघोः  —  VIDHI (narrow demo: luṅ *iṭ* before *sic*)

Glass-box **P026** (*avaDIt*): lengthen the **iṭ** vowel **i** → **ī** (SLP1 ``I``)
on the *sic* *pratyaya* ``Term`` when it still begins with the *iṭ-āgama*
marker and the recipe arms ``state.meta['7_2_7_luN_it_vrddhi_arm']``.

This is a teaching slice for the JSON’s *iṭ* → *ī* step before *sic*-``s`` loss;
it does not implement full **7.2.7** scope.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _sic_term(state: State):
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sic":
            continue
        return t
    return None


def _matches(state: State) -> bool:
    if not state.meta.get("7_2_7_luN_it_vrddhi_arm"):
        return False
    pr = _sic_term(state)
    if pr is None or not pr.varnas:
        return False
    if pr.meta.get("7_2_7_luN_it_vrddhi_done"):
        return False
    v0 = pr.varnas[0]
    if v0.slp1 != "i":
        return False
    if "it_agama" not in v0.tags:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = _sic_term(state)
    if pr is None:
        return state
    pr.varnas[0] = mk("I")
    pr.varnas[0].tags.add("it_agama")
    pr.meta["7_2_7_luN_it_vrddhi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.7",
    sutra_type=SutraType.VIDHI,
    text_slp1="ato halAder laghoH",
    text_dev="अतो हलादेर्लघोः",
    padaccheda_dev="अतः / हलादेः / लघोः",
    why_dev="लुङ्-सिच्-पथे इट्-कार्यम् (इ→ई, P026 अवधीत्)।",
    anuvritti_from=("7.2.6",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
