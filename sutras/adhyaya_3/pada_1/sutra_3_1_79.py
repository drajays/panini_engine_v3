"""
3.1.79  तनादिकृञ्भ्यः उः  —  VIDHI (narrow demo)

Demo slice (कुरुतः):
  For tanādi dhātu `kf` (कृ) in laṭ, insert the vikaraṇa `u` (उ) as a pratyaya
  immediately after the dhātu (exception to śap).

Engine:
  - recipe arms via ``state.meta['3_1_79_tanadi_u_arm']``.
  - inserts a pratyaya Term with SLP1 ``u`` tagged as ``sarvadhatuka`` so
    **7.3.84** triggers guṇa on the dhātu.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _first_dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _matches(state: State) -> bool:
    if not state.meta.get("3_1_79_tanadi_u_arm"):
        return False
    di = _first_dhatu_index(state)
    if di is None:
        return False
    dh = state.terms[di]
    if (dh.meta.get("upadesha_slp1") or "").strip() not in {"kf", "qukfY"}:
        return False
    if dh.meta.get("3_1_79_u_done"):
        return False
    # already inserted?
    if di + 1 < len(state.terms) and (state.terms[di + 1].meta.get("upadesha_slp1") or "").strip() == "u":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    di = _first_dhatu_index(state)
    assert di is not None
    u = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("u")),
        tags={"pratyaya", "vikarana", "sarvadhatuka"},
        meta={"upadesha_slp1": "u"},
    )
    state.terms.insert(di + 1, u)
    state.terms[di].meta["3_1_79_u_done"] = True
    state.meta["3_1_79_tanadi_u_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.79",
    sutra_type=SutraType.VIDHI,
    text_slp1="tanAdi-kfYByaH uH",
    text_dev="तनादिकृञ्भ्यः उः",
    padaccheda_dev="तनादि-कृञ्भ्यः / उः",
    why_dev="तनादि-गणे कृञ्-आदिभ्यः शप्-अपवादरूपेण उ-विकरणः (कुरुतः)।",
    anuvritti_from=("3.1.68",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

