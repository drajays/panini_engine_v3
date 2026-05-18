"""
3.4.82  परस्मैपदानां णलतुसुस्थलथुसणल्वमाः  —  VIDHI

Demo slice (विभिदतुः):
  In liṭ, for parasmaipada 3rd dual, replace `tas` with `atus`.

Teaching JSON **P036** (*nināya*): in liṭ, for parasmaipada 3rd singular, replace
``tip``/``ti`` (after **3.4.78**) with ``ṇal`` (machine ``Nal``).

General liṭ-parasmaipada ādeśa arm:
  ``state.meta['3_4_82_arm']`` is True AND
  ``state.meta['3_4_82_lit_adesha_slp1']`` is set — finds the rightmost
  pratyaya term and replaces its varṇas with the given ādeśa.

Engine:
  • *atus*: ``state.meta['3_4_82_lit_atus_arm']`` + ``tas`` from **3.4.78**.
  • **P036**: ``state.meta['P036_3_4_82_lit_Nal_arm']`` + ``tip``/``ti`` *tiṅ* row.
  • **General liṭ**: ``state.meta['3_4_82_arm']`` + ``state.meta['3_4_82_lit_adesha_slp1']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import CUTU
from phonology.varna import parse_slp1_upadesha_sequence, HAL_DEV


def _find_tas(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "tas":
            return i
    return None


def _find_lit_tip(state: State) -> int | None:
    if not state.meta.get("P036_3_4_82_lit_Nal_arm"):
        return None
    if not state.meta.get("lakara_liT"):
        return None
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"tip", "ti"}:
            return i
    return None


def _find_rightmost_pratyaya(state: State) -> int | None:
    """Find the rightmost pratyaya term not already marked done for 3.4.82."""
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if "pratyaya" not in t.tags:
            continue
        if t.meta.get("3_4_82_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("lakara_liT"):
        return False
    # General liṭ arm
    if state.meta.get("3_4_82_arm") and state.meta.get("3_4_82_lit_adesha_slp1"):
        return _find_rightmost_pratyaya(state) is not None
    if state.meta.get("3_4_82_lit_atus_arm"):
        return _find_tas(state) is not None
    if state.meta.get("P036_3_4_82_lit_Nal_arm"):
        return _find_lit_tip(state) is not None
    return False


# Map: ādeśa string → (set of varna indices that are it-candidates and their tag)
# Only ādeśas that have genuine it-markers (anubandhas) are listed here.
# atus/us/aTus/a/va/ma have NO it-letters — they are pure residues.
_ADESHA_IT_MAP: dict[str, list[tuple[int, str]]] = {
    # Ral = R(cutu-it) + a + l(halantyam-it) → residue: a
    "Ral": [(0, "it_candidate_cutu"), (2, "it_candidate_halantyam")],
    # Tal = T(tha, NOT cutu) + a + l(halantyam-it) → residue: Ta (= tha)
    "Tal": [(2, "it_candidate_halantyam")],
}


def _mark_it_candidates(adesha: str, varnas: list) -> None:
    """
    Mark specific varṇas in the ādeśa as it-candidates according to the
    Pāṇinian anubandha conventions for liṭ ādeśas.
    Only Ral and Tal have anubandha it-markers; others (atus, us, va, ma, etc.)
    are pure residues and need no it-marking here.
    """
    it_specs = _ADESHA_IT_MAP.get(adesha, [])
    for idx, tag in it_specs:
        if idx < len(varnas):
            varnas[idx].tags.add(tag)


def act(state: State) -> State:
    # General liṭ arm — replaces rightmost pratyaya with the given ādeśa
    if state.meta.get("3_4_82_arm") and state.meta.get("3_4_82_lit_adesha_slp1"):
        ti = _find_rightmost_pratyaya(state)
        if ti is None:
            return state
        adesha = state.meta["3_4_82_lit_adesha_slp1"]
        varnas = list(parse_slp1_upadesha_sequence(adesha))
        # Mark cuṭū and halantyam it-candidates for 1.3.7 / 1.3.3 / 1.3.9
        _mark_it_candidates(adesha, varnas)
        new_term = Term(
            kind="pratyaya",
            varnas=varnas,
            tags={"pratyaya", "tin", "ardhadhatuka", "upadesha"},
            meta={"upadesha_slp1": adesha, "3_4_82_done": True},
        )
        state.terms[ti] = new_term
        state.meta["3_4_82_arm"] = False
        state.meta.pop("3_4_82_lit_adesha_slp1", None)
        state.samjna_registry["3_4_82_lit_adesha"] = adesha
        return state

    if state.meta.get("P036_3_4_82_lit_Nal_arm"):
        ti = _find_lit_tip(state)
        if ti is None:
            return state
        nal = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("Nal")),
            tags={"pratyaya", "tin", "ardhadhatuka", "upadesha"},
            meta={"upadesha_slp1": "Nal", "lit_Nal": True},
        )
        # **1.3.9** *it*-lopa on ``ṇal`` requires the final ``l`` to carry an *it* tag
        # (``parse_slp1_upadesha_sequence`` does not mark ``Nal`` like ``tip``).
        if nal.varnas and nal.varnas[-1].slp1 == "l":
            nal.varnas[-1].tags.add("it_candidate_halantyam")
        state.terms[ti] = nal
        state.meta["P036_3_4_82_lit_Nal_arm"] = False
        return state

    ti = _find_tas(state)
    if ti is None:
        return state
    atus = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("atus")),
        tags={"pratyaya", "tin", "ardhadhatuka"},
        meta={"upadesha_slp1": "atus", "lit_atus": True},
    )
    state.terms[ti] = atus
    state.meta["3_4_82_lit_atus_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.82",
    sutra_type=SutraType.VIDHI,
    text_slp1="parasmaipadAnAm Ralatusu... (narrow)",
    text_dev="परस्मैपदानां णलतुसुस्थलथुसणल्वमाः",
    padaccheda_dev="परस्मैपदानाम् / णल-तुसु-स्थ-लथुस्-णल्-वमाः",
    why_dev="लिटि परस्मैपदे तस् → अतुस्; एकवचने तिप् → णल् (प०३६); सामान्य-लिट्-आदेशः।",
    anuvritti_from=("3.4.78",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
