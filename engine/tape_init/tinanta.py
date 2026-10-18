"""
engine/tape_init/tinanta.py — Structural tinanta tape bootstrap.

Sets ``derivation_class``, lakāra/prayoga **tags** (not coordinate reads in
sūtra ``cond()``), and walks phases for autonomous loop entry.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from engine.adhikara_automation import ensure_adhikara_for_phase
from engine.phase import set_phase
from engine.state import State, Term
from engine.vivaksha import set_vivaksha
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
    "AsIrliG": "asirlig_derivation",
}


_KARMAKATVA = Path(__file__).resolve().parents[2] / "data" / "inputs" / "dhatu_karmakatva.json"
# 3.4.69 लः कर्मणि च भावे चाकर्मकेभ्यः: the lakāra is taught in the meaning kartṛ, karman or bhāva
_PRAYOGA_ARTHA = {"kartari": "kartf", "karmani": "karman", "bhave": "BAva"}


@lru_cache(maxsize=1)
def dhatu_karmakatva() -> dict[str, str]:
    return json.loads(_KARMAKATVA.read_text(encoding="utf-8"))["values"]


def _record_vivaksha(state: State, prayoga: str) -> State:
    set_vivaksha(state, artha=_PRAYOGA_ARTHA.get(prayoga))
    return state


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
        # antargaṇa membership (प्वादिः, घटादिः …) — lexical, like the gaṇa
        "antarganas": tuple(row.get("antarganas") or ()),
    }
    karmakatva = dhatu_karmakatva().get(row.get("dhatupatha_id") or "")
    if karmakatva:                        # ashtadhyayi.com dhātupāṭha 'karma' (AMENDMENT 25 §4); a gap row has none
        meta["karmakatva"] = karmakatva
    if atmane:
        meta["kartari_atmanepada_licensed"] = True
    if ubhaya:
        meta["kartari_atmanepada_licensed"] = "ubhaya"

    tags = {"dhatu", "anga", "upadesha", prayoga}
    # घटादयो मितः / ज्ञपादयो मितः (gaṇasūtras): mit — 6.4.92 मितां ह्रस्वः before ṇic
    if {"घटादिः", "ज्ञपादिः"} & set(row.get("antarganas") or ()):
        tags.add("mit")
    lak_tag = _LAKARA_TAG.get(lakara)
    if lak_tag:
        tags.add(lak_tag)

    varnas = parse_slp1_upadesha_sequence(upadesha)
    for v in varnas:
        # the dhātu's own upadeśa sounds; an ādeśa (6.1.64 ṣ→s …) replaces the
        # varṇa and so drops this — 8.3.59 आदेशप्रत्यययोः reads the difference
        v.tags.add("mula_dhatu_v")
    return Term(
        kind="prakriti",
        varnas=varnas,
        tags=tags,
        meta=meta,
    )


def build_tinanta_recipe_state(row: dict, lakara: str, prayoga: str) -> State:
    """
    Recipe entry bootstrap — same structural tags/meta as autonomous tape init.

    Leaves ``phase=angakarya`` (recipe default) so existing spines unchanged.
    """
    return _record_vivaksha(State(
        terms=[dhatu_term_from_row(row, prayoga, lakara)],
        meta={
            "derivation_class": "tinanta",
            "lakara": lakara,
            "prayoga": prayoga,
        },
        trace=[],
    ), prayoga)


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
    _record_vivaksha(state, prayoga)
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
