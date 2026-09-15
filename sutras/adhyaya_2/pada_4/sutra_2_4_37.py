"""
2.4.37  लुङ्सनोर्घसॢ  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=20437
- Kāśikā: «लुङि सनोः अदः घसॢ आदेशः» (अघसत्)
- Cross-validation: tests/unit/test_tinanta_ad_lug_kartari.py

In *luṅ* (and *san*), the root *ad* is replaced by *ghas* (tape: **Gas**).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import DHATUTVA, adesha_substitute_varnas


def _first_dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _dhatu_flat(state: State) -> str | None:
    i = _first_dhatu_index(state)
    if i is None:
        return None
    return "".join(v.slp1 for v in state.terms[i].varnas)


def _site(state: State) -> bool:
    if (state.meta.get("lakara") or "").strip() != "luG":
        return False
    if _first_dhatu_index(state) is None:
        return False
    flat = _dhatu_flat(state)
    if flat == "ad":
        return True
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip().replace("~", "")
        if up in {"ada", "ad", "ada~", "ad~"}:
            return True
    return False


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    i = _first_dhatu_index(state)
    assert i is not None
    t = state.terms[i]
    adesha_substitute_varnas(
        t, "Gas", state,
        sutra_id="2.4.37",
        gunadharmas=frozenset({DHATUTVA}),
    )
    state.meta["2_4_37_ad_to_gas"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.4.37",
    sutra_type=SutraType.VIDHI,
    text_slp1="luNsanorGasx",
    text_dev="लुङ्सनोर्घसॢ",
    padaccheda_dev="लुङ्-सनोः / घसॢ",
    why_dev="लुङि सनोः अद्-धातोः घस्-आदेशः — अघसत्।",
    anuvritti_from=("2.4.35",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
