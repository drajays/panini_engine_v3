"""
engine/tape_init/tinanta.py — Structural tinanta tape bootstrap.

Sets ``derivation_class``, lakāra/prayoga **tags** (not coordinate reads in
sūtra ``cond()``), and walks phases for autonomous loop entry.
"""
from __future__ import annotations

from engine.adhikara_automation import ensure_adhikara_for_phase
from engine.phase import set_phase
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence

_LAKARA_TAG = {
    "laT": "lat_derivation",
    "liT": "lit_derivation",
    "luT": "lut_derivation",
    "lRT": "lrt_derivation",
    "loT": "lot_derivation",
    "liG": "lig_derivation",
    "luG": "lug_derivation",
    "lRG": "lrg_derivation",
    "laG": "lag_derivation",
    "lRN": "lrn_derivation",
}


def dhatu_term_from_row(row: dict, prayoga: str, lakara: str) -> Term:
    """
    Dhātu ``Term`` from a dhātupāṭha row — shared by recipe and autonomous paths.

    Sets lakāra/prayoga **tags** (Art. 2: sūtra ``cond()`` reads tags, not
    ``state.meta['lakara']``).
    """
    upadesha = row["upadesha_slp1"]
    pada_label = row.get("pada_label_dev", "")
    atmane = "आत्मनेपदी" in pada_label
    ubhaya = "उभयपदी" in pada_label

    meta: dict = {
        "upadesha_slp1": upadesha,
        "gana": row.get("gana", 1),
        "dhatu_it": set(row.get("it_markers") or []),
        "ekac_dhatu": bool(row.get("flags", {}).get("ekac", False)),
        "udatta_dhatu": bool(row.get("flags", {}).get("udatta", False)),
        "anit_dhatu": bool(row.get("flags", {}).get("anit", False)),
        "set_dhatu": bool(row.get("flags", {}).get("set", True)),
    }
    if atmane:
        meta["kartari_atmanepada_licensed"] = True
    if ubhaya:
        meta["kartari_atmanepada_licensed"] = "ubhaya"

    tags = {"dhatu", "anga", "upadesha", prayoga}
    lak_tag = _LAKARA_TAG.get(lakara)
    if lak_tag:
        tags.add(lak_tag)

    return Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(upadesha),
        tags=tags,
        meta=meta,
    )


def build_tinanta_recipe_state(row: dict, lakara: str, prayoga: str) -> State:
    """
    Recipe entry bootstrap — same structural tags/meta as autonomous tape init.

    Leaves ``phase=angakarya`` (recipe default) so existing spines unchanged.
    """
    return State(
        terms=[dhatu_term_from_row(row, prayoga, lakara)],
        meta={
            "derivation_class": "tinanta",
            "lakara": lakara,
            "prayoga": prayoga,
        },
        trace=[],
    )


def _base_dhatu_term(upadesha_slp1: str, prayoga: str, lakara: str) -> Term:
    varna_slp1: tuple[str, ...]
    if upadesha_slp1 == "BU":
        varna_slp1 = ("B", "U")
    elif len(upadesha_slp1) >= 2:
        varna_slp1 = tuple(upadesha_slp1[:2])
    else:
        varna_slp1 = ("a",)

    tags = {"dhatu", "anga", "prakriti", prayoga}
    lak_tag = _LAKARA_TAG.get(lakara)
    if lak_tag:
        tags.add(lak_tag)

    return Term(
        kind="prakriti",
        varnas=[mk(v) for v in varna_slp1],
        tags=tags,
        meta={"upadesha_slp1": upadesha_slp1},
    )


def build_tinanta_initial_state(
    upadesha_slp1: str,
    lakara: str,
    prayoga: str,
) -> State:
    """
    Tinanta ``State`` at ``upadesha`` phase for ``run_sapadasaptadhyayi``.

    Pipeline coordination meta (``lakara``, ``prayoga``) is set here for
    recipes only — sūtra ``cond()`` must use tags / ``derivation_class``.
    """
    state = State(
        terms=[_base_dhatu_term(upadesha_slp1, prayoga, lakara)],
        phase="upadesha",
    )
    state.meta["derivation_class"] = "tinanta"
    state.meta["lakara"] = lakara
    state.meta["prayoga"] = prayoga
    ensure_adhikara_for_phase(state, "upadesha")
    return state


def build_tinanta_probe_state(
    upadesha_slp1: str,
    lakara: str,
    prayoga: str,
    *,
    varna_slp1: tuple[str, ...] | None = None,
) -> State:
    """
    Probe state advanced to ``angakarya`` for scheduler discipline tests.
    """
    state = build_tinanta_initial_state(upadesha_slp1, lakara, prayoga)
    if varna_slp1 is not None:
        state.terms[0].varnas = [mk(v) for v in varna_slp1]
    set_phase(state, "pratyaya")
    ensure_adhikara_for_phase(state, "pratyaya")
    set_phase(state, "angakarya")
    ensure_adhikara_for_phase(state, "angakarya")
    return state
