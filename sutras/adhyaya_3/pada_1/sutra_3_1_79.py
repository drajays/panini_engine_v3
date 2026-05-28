"""
3.1.79  तनादिकृञ्भ्यः उः  —  VIDHI

For tanādi (gaṇa 8) and kṛñ roots, insert vikaraṇa ``u`` after the dhātu,
displacing śap (3.1.68 apavāda). The ``u`` is sārvadhatuka-tagged so 7.3.84
fires guṇa on the dhātu (kṛ → kar).

Structural trigger (CONSTITUTION Art. 13):
- dhātu ``gana == 8`` OR stem in ``_TANADI_STEMS``
- a ``tin_adesha_3_4_78``-tagged term is on tape (sārvadhatuka context)
- no ``u`` vikaraṇa already inserted

No arm flag required (Art. 13).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

# Post-it-lopa stems of tanādi roots currently exercised in this repository.
_TANADI_STEMS: frozenset[str] = frozenset({"kf", "tan", "man", "san", "van", "kan"})


def _find_dhatu_for_u(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        gana = t.meta.get("gana")
        stem = "".join(v.slp1 for v in t.varnas)
        if gana != 8 and stem not in _TANADI_STEMS:
            continue
        if t.meta.get("3_1_79_u_done"):
            continue
        # already inserted?
        if i + 1 < len(state.terms):
            nxt = state.terms[i + 1]
            if (nxt.meta.get("upadesha_slp1") or "").strip() == "u":
                continue
        # sārvadhatuka tin must be on tape
        if not any("tin_adesha_3_4_78" in t2.tags for t2 in state.terms):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_dhatu_for_u(state) is not None


def act(state: State) -> State:
    di = _find_dhatu_for_u(state)
    if di is None:
        return state
    u = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("u")),
        tags={"pratyaya", "vikarana", "sarvadhatuka"},
        meta={"upadesha_slp1": "u"},
    )
    state.terms.insert(di + 1, u)
    state.terms[di].meta["3_1_79_u_done"] = True
    state.meta.pop("3_1_79_tanadi_u_arm", None)
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

